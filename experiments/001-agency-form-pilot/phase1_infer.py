"""Chat-template inference smoke test for Phase 1.

The subject is the loaded Qwen checkpoint. Completions are raw observations.
A toy action is executed only when the completion contains a parseable action
in the closed set. This file does not score respect for human agency.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from phase1_common import (  # noqa: E402
    GENERATION_SEED,
    GENERATION_TEMPERATURE,
    INFERENCE_FIXTURES,
    MAX_NEW_TOKENS,
    MLX_MODEL_ID,
    MLX_MODEL_REVISION,
    ORIGINAL_MODEL_ID,
    OUTPUT_DIR,
    ToyEnvironment,
    load_jsonl,
    memory_sample,
    metal_memory_bytes,
    process_max_rss_bytes,
    reset_metal_peak,
    snapshot_model,
)
from phase1_common import ModelClock  # noqa: E402

os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def render_user_prompt(tokenizer, user_text: str) -> str:
    rendered = tokenizer.apply_chat_template(
        [{"role": "user", "content": user_text}],
        tokenize=False,
        add_generation_prompt=True,
    )
    if not isinstance(rendered, str):
        raise TypeError(f"Chat template returned {type(rendered).__name__}, expected str")
    return rendered


def directory_nbytes(path: Path) -> int:
    total = 0
    for item in path.rglob("*"):
        if item.is_file():
            total += item.stat().st_size
    return total


def model_identity(model_dir: Path) -> dict:
    from huggingface_hub import HfApi

    api = HfApi()
    mlx_info = api.model_info(MLX_MODEL_ID, revision=MLX_MODEL_REVISION)
    original = api.model_info(ORIGINAL_MODEL_ID)
    config = json.loads((model_dir / "config.json").read_text())
    quant = config.get("quantization") or config.get("quantization_config") or {}
    return {
        "mlx_repo": MLX_MODEL_ID,
        "mlx_revision_requested": MLX_MODEL_REVISION,
        "mlx_revision_retrieved": mlx_info.sha,
        "mlx_last_modified": str(mlx_info.last_modified),
        "local_snapshot": str(model_dir),
        "local_snapshot_bytes": directory_nbytes(model_dir),
        "local_snapshot_bytes_note": (
            "Sum of file sizes in the local snapshot, following symlinks. "
            "This is a measurement of the downloaded artifact, not the model card's published size."
        ),
        "original_repo": ORIGINAL_MODEL_ID,
        "original_revision": original.sha,
        "original_last_modified": str(original.last_modified),
        "quantization_observed_in_downloaded_config": quant,
        "model_type": config.get("model_type"),
        "architectures": config.get("architectures"),
        "num_hidden_layers": config.get("num_hidden_layers"),
        "max_position_embeddings": config.get("max_position_embeddings"),
        "torch_dtype": config.get("torch_dtype"),
        "full_precision_weights_downloaded": False,
    }


def compare_templates(mlx_tokenizer, examples: list[dict]) -> dict:
    from transformers import AutoTokenizer
    from huggingface_hub import HfApi

    original_revision = HfApi().model_info(ORIGINAL_MODEL_ID).sha
    original = AutoTokenizer.from_pretrained(
        ORIGINAL_MODEL_ID,
        revision=original_revision,
    )
    mlx_template = getattr(mlx_tokenizer, "chat_template", None) or ""
    original_template = getattr(original, "chat_template", None) or ""
    rows = []
    for example in examples:
        mlx_rendered = render_user_prompt(mlx_tokenizer, example["user"])
        original_rendered = original.apply_chat_template(
            [{"role": "user", "content": example["user"]}],
            tokenize=False,
            add_generation_prompt=True,
        )
        rows.append(
            {
                "id": example["id"],
                "rendered_prompts_equal": mlx_rendered == original_rendered,
                "mlx_rendered_prompt": mlx_rendered,
                "original_rendered_prompt": original_rendered,
                "mlx_rendered_contains_think_tag": "<think>" in mlx_rendered,
                "original_rendered_contains_think_tag": "<think>" in original_rendered,
            }
        )
    return {
        "original_revision": original_revision,
        "template_text_equal": mlx_template == original_template,
        "mlx_template_sha256": sha256_text(mlx_template),
        "original_template_sha256": sha256_text(original_template),
        "single_turn_renders": rows,
        "inference_template": "chat template loaded with the MLX artifact",
        "note": (
            "Templates were not edited. Inference uses the MLX artifact's template "
            "via apply_chat_template."
        ),
    }


def generate_completion(model, tokenizer, user_text: str) -> dict:
    import mlx.core as mx
    from mlx_lm.generate import stream_generate
    from mlx_lm.sample_utils import make_sampler

    rendered = render_user_prompt(tokenizer, user_text)
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
        xtc_probability=0.0,
        xtc_threshold=0.1,
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
    seconds = time.perf_counter() - started
    completion = "".join(pieces)
    return {
        "rendered_prompt": rendered,
        "prompt_token_count": len(prompt_tokens),
        "completion": completion,
        "generation_tokens": None if last is None else last.generation_tokens,
        "finish_reason": None if last is None else last.finish_reason,
        "prompt_tps": None if last is None else last.prompt_tps,
        "generation_tps": None if last is None else last.generation_tps,
        "mlx_lm_reported_peak_memory_gb": None if last is None else last.peak_memory,
        "mlx_lm_reported_peak_memory_note": (
            "Value from GenerationResponse.peak_memory, which is "
            "mx.get_peak_memory() / 1e9 after this call. It is MLX allocator "
            "peak memory since the last reset, not system-wide memory."
        ),
        "mlx_peak_memory_bytes": int(mx.get_peak_memory()),
        "mlx_metal_after": metal_memory_bytes(),
        "process_max_rss_bytes": process_max_rss_bytes(),
        "seconds": seconds,
        "settings": {
            "temperature": GENERATION_TEMPERATURE,
            "top_p": 1.0,
            "min_p": 0.0,
            "top_k": 0,
            "seed": GENERATION_SEED,
            "max_new_tokens": MAX_NEW_TOKENS,
            "add_special_tokens": False,
            "chat_template": True,
        },
    }


def mechanical_check(kind: str, completion: str, execution: dict | None) -> dict:
    """Describe format only. This is not a research score."""

    stripped = completion.strip()
    if kind == "instruction_following":
        return {
            "exact_single_word_pebble": stripped.strip(".").lower() == "pebble",
        }
    if kind == "consent_comprehension":
        return {"nonempty": bool(stripped)}
    if kind == "toy_action":
        return {
            "executed": bool(execution and execution["executed"]),
            "reason": None if execution is None else execution["reason"],
        }
    if kind == "explanation":
        return {"nonempty": bool(stripped)}
    return {}


def main() -> int:
    clock = ModelClock()
    clock.elapsed = 0.0
    clock.entries = []
    clock.write()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    record: dict = {"status": "started"}
    try:
        download_started = time.perf_counter()
        model_dir = snapshot_model()
        record["download_seconds"] = time.perf_counter() - download_started
        record["download_seconds_note"] = (
            "Excluded from the 20-minute model-execution budget."
        )
        record["identity"] = model_identity(model_dir)
        examples = load_jsonl(INFERENCE_FIXTURES)
        for example in examples:
            if example.get("fixture_role") != "phase1_smoke_inference":
                raise RuntimeError(f"{example.get('id')} is not labeled as a smoke fixture")
            if example.get("not_evaluation") is not True:
                raise RuntimeError(f"{example.get('id')} is not marked not_evaluation")

        clock.guard("inference model load")
        import mlx.core as mx
        from mlx_lm import load

        load_started = time.perf_counter()
        model, tokenizer = load(str(model_dir), revision=MLX_MODEL_REVISION)
        mx.eval(model.parameters())
        load_seconds = time.perf_counter() - load_started
        clock.add("inference_model_load", load_seconds)
        record["model_load_seconds"] = load_seconds
        record["memory_after_load"] = memory_sample("after_inference_model_load")
        record["tokenizer"] = {
            "class": type(tokenizer).__name__,
            "eos_token": getattr(tokenizer, "eos_token", None),
            "eos_token_id": getattr(tokenizer, "eos_token_id", None),
            "bos_token": getattr(tokenizer, "bos_token", None),
            "vocab_size": getattr(tokenizer, "vocab_size", None),
        }
        record["chat_template_comparison"] = compare_templates(tokenizer, examples)

        results = []
        environment = ToyEnvironment()
        for example in examples:
            clock.guard(f"inference {example['id']}")
            generated = generate_completion(model, tokenizer, example["user"])
            clock.add(f"inference_{example['id']}", generated["seconds"])
            execution = None
            if example["kind"] == "toy_action":
                execution = environment.execute_completion(generated["completion"])
            else:
                execution = {
                    "executed": False,
                    "reason": "not_an_action_fixture",
                    "state_before": list(environment.log),
                    "state_after": list(environment.log),
                }
            results.append(
                {
                    "id": example["id"],
                    "kind": example["kind"],
                    "fixture_role": example["fixture_role"],
                    "not_evaluation": True,
                    "user": example["user"],
                    "generation": generated,
                    "mock_environment": execution,
                    "mechanical_format_check": mechanical_check(
                        example["kind"], generated["completion"], execution
                    ),
                }
            )
        record["results"] = results
        record["mock_environment_final_state"] = list(environment.log)
        record["model_clock"] = clock.as_dict()
        record["status"] = "completed"
        record["budget_exceeded"] = clock.exceeded()
    except Exception as exc:
        record["status"] = "failed"
        record["error"] = f"{type(exc).__name__}: {exc}"
        record["traceback"] = traceback.format_exc()
        record["model_clock"] = clock.as_dict()
        path = OUTPUT_DIR / "inference.json"
        path.write_text(json.dumps(record, indent=2) + "\n")
        print(record["traceback"], file=sys.stderr)
        return 1

    path = OUTPUT_DIR / "inference.json"
    path.write_text(json.dumps(record, indent=2) + "\n")
    print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
