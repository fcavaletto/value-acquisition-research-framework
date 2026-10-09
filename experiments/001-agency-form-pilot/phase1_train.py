"""Train and reload a tiny LoRA adapter on one neutral sentence.

Twenty optimizer updates check the pipeline. A loss change, or a difference
between completions, is not evidence that a value was learned.
"""

from __future__ import annotations

import json
import os
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from phase1_common import (  # noqa: E402
    ADAPTER_DIR,
    FIXTURE_DIR,
    GENERATION_SEED,
    GENERATION_TEMPERATURE,
    LORA_CONFIG,
    MAX_NEW_TOKENS,
    MAX_SEQ_LENGTH,
    MLX_MODEL_REVISION,
    OUTPUT_DIR,
    RELOAD_USER_PROMPT,
    TRAIN_FIXTURE,
    ModelClock,
    load_jsonl,
    memory_sample,
    metal_memory_bytes,
    process_max_rss_bytes,
    reset_metal_peak,
    snapshot_model,
)

os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

CLI_FLAGS = [
    "--train",
    "--batch-size",
    "1",
    "--iters",
    "20",
    "--max-seq-length",
    "1024",
    "--grad-accumulation-steps",
    "1",
    "--seed",
    "0",
    "--save-every",
    "20",
    "--num-layers",
    "16",
    "--learning-rate",
    "1e-5",
    "--steps-per-report",
    "1",
    "--steps-per-eval",
    "1000",
    "--fine-tune-type",
    "lora",
    "--optimizer",
    "adamw",
]


def equivalent_command(model_dir: Path, grad_checkpoint: bool) -> list[str]:
    command = [
        ".venv/bin/mlx_lm.lora",
        "--config",
        str(LORA_CONFIG.relative_to(LORA_CONFIG.parents[2])),
        "--model",
        str(model_dir),
        "--data",
        str(FIXTURE_DIR.relative_to(FIXTURE_DIR.parents[2])),
        "--adapter-path",
        str(ADAPTER_DIR.relative_to(ADAPTER_DIR.parents[2])),
        *CLI_FLAGS,
    ]
    if grad_checkpoint:
        command.append("--grad-checkpoint")
    return command


def build_namespace(model_dir: Path, grad_checkpoint: bool):
    import mlx_lm.lora as lora_mod

    parser = lora_mod.build_parser()
    argv = [
        "--config",
        str(LORA_CONFIG),
        "--model",
        str(model_dir),
        "--data",
        str(FIXTURE_DIR),
        "--adapter-path",
        str(ADAPTER_DIR),
        *CLI_FLAGS,
    ]
    if grad_checkpoint:
        argv.append("--grad-checkpoint")
    parsed = vars(parser.parse_args(argv))
    with LORA_CONFIG.open() as handle:
        config = lora_mod.yaml.load(handle, lora_mod.yaml_loader)
    for key, value in config.items():
        if parsed.get(key, None) is None:
            parsed[key] = value
    for key, value in lora_mod.CONFIG_DEFAULTS.items():
        if parsed.get(key, None) is None:
            parsed[key] = value
    return lora_mod.types.SimpleNamespace(**parsed)


def loss_coverage(model_dir: Path) -> dict:
    from mlx_lm.tokenizer_utils import load as load_tokenizer
    from mlx_lm.tuner.datasets import TextDataset

    rows = load_jsonl(TRAIN_FIXTURE)
    if len(rows) != 1:
        raise RuntimeError(f"Expected one training fixture, found {len(rows)}")
    row = rows[0]
    if row.get("fixture_role") != "phase1_smoke_training" or row.get("not_evaluation") is not True:
        raise RuntimeError("Training fixture is missing its smoke-test labels")
    if any(key in row for key in ("messages", "prompt", "completion")):
        raise RuntimeError("Training fixture must stay in text format")
    text = row["text"]
    tokenizer = load_tokenizer(model_dir)
    tokens, offset = TextDataset([row], tokenizer).process(row)
    token_ids = [int(token) for token in tokens]
    if len(token_ids) > MAX_SEQ_LENGTH:
        raise RuntimeError(
            f"Training fixture is {len(token_ids)} tokens, above the "
            f"{MAX_SEQ_LENGTH} limit. Refusing to train because MLX-LM would "
            "truncate it with a warning."
        )
    if offset != 0:
        raise RuntimeError(
            f"Loss offset is {offset}. The text-format smoke test requires "
            "offset 0 so the fixture is inside the loss."
        )
    decoded = tokenizer.decode(token_ids)
    eos_id = getattr(tokenizer, "eos_token_id", None)
    return {
        "text": text,
        "token_count": len(token_ids),
        "token_ids": token_ids,
        "loss_offset": offset,
        "max_seq_length": MAX_SEQ_LENGTH,
        "would_truncate": False,
        "mask_prompt": False,
        "eos_token_id": eos_id,
        "final_token_is_eos": eos_id is not None and token_ids[-1] == eos_id,
        "decoded_training_sequence": decoded,
        "fixture_text_in_decoded_sequence": text in decoded,
        "loss": (
            "Next-token cross-entropy. Offset 0 means every position after the "
            "first token is a target, including the fixture text and a trailing "
            "end-of-sequence token when the loader appends one. No prompt mask "
            "is applied. This is the installed TextDataset and default_loss "
            "behaviour, not a claim about learning."
        ),
    }


class LossCapture:
    def __init__(self) -> None:
        self.reports: list[dict] = []

    def on_train_loss_report(self, train_info: dict) -> None:
        report = {}
        for key, value in train_info.items():
            if hasattr(value, "item"):
                value = value.item()
            if isinstance(value, float):
                report[key] = value
            else:
                report[key] = value
        self.reports.append(report)

    def on_val_loss_report(self, val_info: dict) -> None:
        return None


def run_training(model_dir: Path, grad_checkpoint: bool, capture: LossCapture) -> None:
    import mlx_lm.lora as lora_mod

    def capture_callbacks(*args, **kwargs):
        return capture

    lora_mod.get_reporting_callbacks = capture_callbacks
    args = build_namespace(model_dir, grad_checkpoint)
    if args.mask_prompt:
        raise RuntimeError("mask_prompt is set; the text fixture would not be fully in the loss")
    if args.iters != 20 or args.grad_accumulation_steps != 1 or args.batch_size != 1:
        raise RuntimeError("Training settings drifted from the Phase 1 bound")
    lora_mod.run(args)


def is_memory_failure(exc: BaseException) -> bool:
    text = f"{type(exc).__name__}: {exc}".lower()
    markers = (
        "out of memory",
        "memoryerror",
        "cannot allocate",
        "kiogpucommandbuffercallbackerror",
        "mmap failed",
        "jetsam",
    )
    return any(marker in text for marker in markers)


def generate_once(model_dir: Path, adapter_path: Path | None) -> dict:
    import mlx.core as mx
    from mlx_lm import load
    from mlx_lm.generate import stream_generate
    from mlx_lm.sample_utils import make_sampler

    clock_name = "reload_with_adapter" if adapter_path else "reload_without_adapter"
    load_started = time.perf_counter()
    model, tokenizer = load(
        str(model_dir),
        adapter_path=None if adapter_path is None else str(adapter_path),
        revision=MLX_MODEL_REVISION,
    )
    mx.eval(model.parameters())
    load_seconds = time.perf_counter() - load_started
    rendered = tokenizer.apply_chat_template(
        [{"role": "user", "content": RELOAD_USER_PROMPT}],
        tokenize=False,
        add_generation_prompt=True,
    )
    prompt_tokens = tokenizer.encode(rendered, add_special_tokens=False)
    mx.random.seed(GENERATION_SEED)
    reset_metal_peak()
    mx.reset_peak_memory()
    sampler = make_sampler(
        temp=GENERATION_TEMPERATURE,
        top_p=1.0,
        min_p=0.0,
        min_tokens_to_keep=1,
        top_k=0,
    )
    pieces = []
    last = None
    started = time.perf_counter()
    for response in stream_generate(
        model,
        tokenizer,
        prompt_tokens,
        max_tokens=MAX_NEW_TOKENS,
        sampler=sampler,
    ):
        pieces.append(response.text)
        last = response
    generate_seconds = time.perf_counter() - started
    completion = "".join(pieces)
    result = {
        "adapter": adapter_path is not None,
        "adapter_path": None if adapter_path is None else str(adapter_path),
        "user": RELOAD_USER_PROMPT,
        "rendered_prompt": rendered,
        "prompt_token_count": len(prompt_tokens),
        "completion": completion,
        "generation_tokens": None if last is None else last.generation_tokens,
        "finish_reason": None if last is None else last.finish_reason,
        "load_seconds": load_seconds,
        "generate_seconds": generate_seconds,
        "mlx_lm_reported_peak_memory_gb": None if last is None else last.peak_memory,
        "mlx_peak_memory_bytes": int(mx.get_peak_memory()),
        "mlx_metal_after": metal_memory_bytes(),
        "process_max_rss_bytes": process_max_rss_bytes(),
        "settings": {
            "temperature": GENERATION_TEMPERATURE,
            "seed": GENERATION_SEED,
            "max_new_tokens": MAX_NEW_TOKENS,
        },
        "clock_step": clock_name,
    }
    del model
    mx.clear_cache()
    return result


def main() -> int:
    clock = ModelClock()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    record: dict = {"status": "started"}
    try:
        model_dir = snapshot_model()
        record["model_dir"] = str(model_dir)
        record["loss_coverage"] = loss_coverage(model_dir)
        attempts = []
        capture = LossCapture()
        trained = False
        for attempt_index, use_checkpoint in enumerate((False, True)):
            clock.guard(f"training attempt {attempt_index + 1}")
            if ADAPTER_DIR.exists():
                for child in ADAPTER_DIR.iterdir():
                    if child.is_file():
                        child.unlink()
            started = time.perf_counter()
            error = None
            try:
                run_training(model_dir, use_checkpoint, capture)
                trained = True
            except Exception as exc:
                error = f"{type(exc).__name__}: {exc}"
                if not (use_checkpoint is False and is_memory_failure(exc)):
                    attempts.append(
                        {
                            "grad_checkpoint": use_checkpoint,
                            "seconds": time.perf_counter() - started,
                            "error": error,
                        }
                    )
                    clock.add(
                        f"training_grad_checkpoint_{use_checkpoint}",
                        time.perf_counter() - started,
                    )
                    raise
            seconds = time.perf_counter() - started
            clock.add(f"training_grad_checkpoint_{use_checkpoint}", seconds)
            attempts.append(
                {
                    "grad_checkpoint": use_checkpoint,
                    "seconds": seconds,
                    "error": error,
                    "loss_reports": list(capture.reports),
                    "command": equivalent_command(model_dir, use_checkpoint),
                }
            )
            if trained:
                break
            capture = LossCapture()
        record["training_attempts"] = attempts
        record["memory_after_training"] = memory_sample("after_training")
        adapter_file = ADAPTER_DIR / "adapters.safetensors"
        config_file = ADAPTER_DIR / "adapter_config.json"
        record["adapter"] = {
            "directory": str(ADAPTER_DIR),
            "weights_present": adapter_file.exists(),
            "config_present": config_file.exists(),
            "weights_bytes": adapter_file.stat().st_size if adapter_file.exists() else None,
        }
        if not adapter_file.exists() or not config_file.exists():
            raise RuntimeError("Training finished without an adapter file to reload")

        import mlx.core as mx

        mx.clear_cache()
        clock.guard("reload without adapter")
        without = generate_once(model_dir, None)
        clock.add("reload_without_adapter_load", without["load_seconds"])
        clock.add("reload_without_adapter_generate", without["generate_seconds"])
        clock.guard("reload with adapter")
        with_adapter = generate_once(model_dir, ADAPTER_DIR)
        clock.add("reload_with_adapter_load", with_adapter["load_seconds"])
        clock.add("reload_with_adapter_generate", with_adapter["generate_seconds"])
        record["reload"] = {
            "without_adapter": without,
            "with_adapter": with_adapter,
            "completions_differ": without["completion"] != with_adapter["completion"],
            "interpretation": (
                "Both paths ran. A difference between completions only shows that "
                "the reloaded adapter participated in generation. It is not evidence "
                "of value acquisition. The training text was one neutral sentence "
                "about a reading room."
            ),
        }
        record["model_clock"] = clock.as_dict()
        record["status"] = "completed"
        record["budget_exceeded"] = clock.exceeded()
    except Exception as exc:
        record["status"] = "failed"
        record["error"] = f"{type(exc).__name__}: {exc}"
        record["traceback"] = traceback.format_exc()
        record["model_clock"] = clock.as_dict()
        path = OUTPUT_DIR / "train.json"
        path.write_text(json.dumps(record, indent=2) + "\n")
        print(record["traceback"], file=sys.stderr)
        return 1

    path = OUTPUT_DIR / "train.json"
    path.write_text(json.dumps(record, indent=2) + "\n")
    print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
