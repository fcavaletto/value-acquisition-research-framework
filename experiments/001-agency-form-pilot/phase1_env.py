"""Record the Phase 1 machine and package environment.

This script does not load Qwen. It omits serial numbers and other hardware
identifiers that are not needed to understand the run.
"""

from __future__ import annotations

import json
import platform
import shutil
import subprocess
import sys
from importlib.metadata import version

from phase1_common import OUTPUT_DIR, memory_sample

ALLOWED_HARDWARE_KEYS = {
    "Model Name",
    "Model Identifier",
    "Chip",
    "Total Number of Cores",
    "Memory",
}


def command_text(args: list[str]) -> str:
    return subprocess.check_output(args, text=True)


def hardware() -> dict:
    raw = command_text(["system_profiler", "SPHardwareDataType"])
    kept = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in ALLOWED_HARDWARE_KEYS:
            kept[key] = value.strip()
    return {
        "source": "system_profiler SPHardwareDataType",
        "fields": kept,
        "omitted": "Serial number, hardware UUID, and provisioning UDID are not recorded.",
    }


def system_memory() -> dict:
    raw = command_text(["vm_stat"])
    page_size = None
    pages = {}
    for line in raw.splitlines():
        if "page size of" in line:
            page_size = int(line.split("page size of", 1)[1].strip().strip(".").split()[0])
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        number = value.strip().strip(".")
        if number.isdigit():
            pages[key.strip()] = int(number)
    return {
        "source": "vm_stat",
        "scope": "system_wide_not_this_process",
        "page_size_bytes": page_size,
        "pages": pages,
        "note": "These counts describe the whole Mac. They are not process memory.",
    }


def disk() -> dict:
    usage = shutil.disk_usage("/")
    return {
        "path": "/",
        "total_bytes": usage.total,
        "used_bytes": usage.used,
        "free_bytes": usage.free,
        "source": "shutil.disk_usage",
        "note": "Measured on this machine at report time. Not an estimate.",
    }


def package_versions() -> dict:
    names = ["mlx", "mlx-lm", "transformers", "huggingface-hub", "numpy"]
    found = {}
    for name in names:
        try:
            found[name] = version(name)
        except Exception as exc:
            found[name] = f"unavailable: {type(exc).__name__}"
    return found


def metal_device() -> dict:
    try:
        import mlx.core as mx

        info = dict(mx.device_info())
    except Exception as exc:
        return {
            "available": False,
            "error": f"{type(exc).__name__}: {exc}",
        }
    safe = {}
    for key, value in info.items():
        text = str(value)
        if "uuid" in key.lower() or "serial" in key.lower():
            continue
        safe[key] = value if isinstance(value, (int, float)) else text
    return {"available": True, "device_info": safe}


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "python": {
            "version": sys.version,
            "executable": sys.executable,
            "implementation": platform.python_implementation(),
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "mac_version": platform.mac_ver()[0],
        },
        "sw_vers": command_text(["sw_vers"]),
        "uname": command_text(["uname", "-sm"]),
        "hardware": hardware(),
        "disk": disk(),
        "system_memory": system_memory(),
        "process_memory_before_model_load": memory_sample("environment_report"),
        "packages": package_versions(),
        "metal": metal_device(),
    }
    path = OUTPUT_DIR / "environment.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
