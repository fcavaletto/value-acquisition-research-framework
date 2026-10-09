"""Shared helpers for the Phase 1 smoke tests.

These helpers check a software pipeline. They do not score respect for human
agency, and they do not decide whether a completion is a good action.
"""

from __future__ import annotations

import json
import resource
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_DIR = REPO_ROOT / "data" / "fixtures" / "phase1"
INFERENCE_FIXTURES = FIXTURE_DIR / "inference_smoke.jsonl"
TRAIN_FIXTURE = FIXTURE_DIR / "train.jsonl"
OUTPUT_DIR = REPO_ROOT / "outputs" / "phase1"
CLOCK_PATH = OUTPUT_DIR / "model_clock.json"
ADAPTER_DIR = OUTPUT_DIR / "adapter"
LORA_CONFIG = Path(__file__).resolve().parent / "lora_phase1.yaml"

MLX_MODEL_ID = "mlx-community/Qwen3-4B-Instruct-2507-4bit"
MLX_MODEL_REVISION = "50d427756c6b1b2fe0c0a10f67fbda1fc8e82c1b"
ORIGINAL_MODEL_ID = "Qwen/Qwen3-4B-Instruct-2507"

BUDGET_SECONDS = 20 * 60
MAX_SEQ_LENGTH = 1024
MAX_NEW_TOKENS = 128
GENERATION_TEMPERATURE = 0.0
GENERATION_SEED = 0
ALLOWED_ACTIONS = ("wait", "note")

RELOAD_USER_PROMPT = "Reply with exactly the single word: quartz."


def process_max_rss_bytes() -> int:
    """High-water resident set size for this process.

    On macOS, ``ru_maxrss`` is in bytes. The value is not the current
    allocation, and it is not system-wide memory.
    """

    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def metal_memory_bytes() -> dict:
    """MLX allocator figures for this process.

    mlx 0.32 deprecates ``mx.metal.get_active_memory`` and the matching peak
    and cache helpers. The replacements are ``mx.get_active_memory``,
    ``mx.get_peak_memory``, and ``mx.get_cache_memory``. Active memory does
    not include the allocator cache. None of these figures are system-wide.
    """

    import mlx.core as mx

    return {
        "active_bytes": int(mx.get_active_memory()),
        "peak_bytes": int(mx.get_peak_memory()),
        "cache_bytes": int(mx.get_cache_memory()),
        "scope": "mlx_allocator_for_this_process",
        "api": "mx.get_active_memory, mx.get_peak_memory, mx.get_cache_memory",
    }


def reset_metal_peak() -> None:
    import mlx.core as mx

    mx.reset_peak_memory()


def memory_sample(label: str) -> dict:
    sample = {
        "label": label,
        "process_max_rss_bytes": process_max_rss_bytes(),
        "process_max_rss_scope": "this_process_high_water_mark_bytes_on_macos",
    }
    try:
        sample["mlx_metal"] = metal_memory_bytes()
    except Exception as exc:  # The environment report runs before a model load.
        sample["mlx_metal"] = None
        sample["mlx_metal_error"] = f"{type(exc).__name__}: {exc}"
    return sample


class ModelClock:
    """Wall time spent loading or running the model, excluding setup and downloads."""

    def __init__(self, path: Path = CLOCK_PATH) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            data = json.loads(self.path.read_text())
            self.elapsed = float(data["elapsed_seconds"])
            self.entries = list(data.get("entries", []))
        else:
            self.elapsed = 0.0
            self.entries = []

    def remaining(self) -> float:
        return BUDGET_SECONDS - self.elapsed

    def exceeded(self) -> bool:
        return self.elapsed > BUDGET_SECONDS

    def guard(self, step_name: str) -> None:
        if self.exceeded():
            raise RuntimeError(
                "Model-execution budget of "
                f"{BUDGET_SECONDS:.0f} seconds was already used "
                f"({self.elapsed:.1f} seconds) before {step_name}."
            )

    def add(self, step_name: str, seconds: float) -> None:
        self.elapsed += float(seconds)
        self.entries.append(
            {
                "step": step_name,
                "seconds": float(seconds),
                "elapsed_seconds": self.elapsed,
            }
        )
        self.write()

    def write(self) -> None:
        self.path.write_text(
            json.dumps(
                {
                    "budget_seconds": BUDGET_SECONDS,
                    "elapsed_seconds": self.elapsed,
                    "entries": self.entries,
                    "scope": "model_load_and_execution_only",
                },
                indent=2,
            )
            + "\n"
        )

    def as_dict(self) -> dict:
        return {
            "budget_seconds": BUDGET_SECONDS,
            "elapsed_seconds": self.elapsed,
            "entries": self.entries,
        }


def iter_json_objects(text: str):
    """Yield JSON objects found by a brace scan. Invalid chunks are skipped."""

    start = None
    depth = 0
    in_string = False
    escape = False
    for index, char in enumerate(text):
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
            continue
        if char == "{":
            if depth == 0:
                start = index
            depth += 1
        elif char == "}" and depth:
            depth -= 1
            if depth == 0 and start is not None:
                chunk = text[start : index + 1]
                try:
                    value = json.loads(chunk)
                except json.JSONDecodeError:
                    value = None
                if isinstance(value, dict):
                    yield value
                start = None


def parse_action(text: str) -> str | None:
    """Return the first JSON ``action`` string, or None if none is present.

    A sentence that merely claims an action was performed does not parse.
    """

    if not text:
        return None
    for obj in iter_json_objects(text):
        action = obj.get("action")
        if isinstance(action, str):
            return action
    return None


class ToyEnvironment:
    """One-step mock environment. State changes only through ``execute_completion``."""

    def __init__(self) -> None:
        self.log: list[str] = []

    def execute_completion(self, completion: str) -> dict:
        action = parse_action(completion)
        before = list(self.log)
        if action is None:
            reason = "no_parseable_action"
            executed = False
        elif action not in ALLOWED_ACTIONS:
            reason = "action_not_in_closed_set"
            executed = False
        else:
            self.log.append(action)
            reason = "executed"
            executed = True
        return {
            "parsed_action": action,
            "executed": executed,
            "reason": reason,
            "state_before": before,
            "state_after": list(self.log),
        }


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line_number} is not a JSON object")
        rows.append(row)
    return rows


def snapshot_model() -> Path:
    """Download the pinned MLX revision into the Hugging Face cache, outside Git."""

    from huggingface_hub import snapshot_download

    path = snapshot_download(
        repo_id=MLX_MODEL_ID,
        revision=MLX_MODEL_REVISION,
    )
    return Path(path)
