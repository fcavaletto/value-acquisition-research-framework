# Phase 1 smoke-test fixtures

These files are development-only pipeline fixtures for [experiments/001-agency-form-pilot](../../../experiments/001-agency-form-pilot/README.md).

They are not held-out research evaluation items. They must not be copied into a development battery, a confirmation set, or a teaching corpus. A result on these strings says whether the software path ran. It does not say whether a model has learned respect for human agency.

- `inference_smoke.jsonl` — four short chat prompts: instruction following, a simple consent and delegation question, a toy action, and a brief explanation of a mundane choice.
- `train.jsonl` — one neutral text about a reading room. It is not about agency, consent, or delegation. MLX-LM trains on the `text` field. Other keys are labels for humans and are ignored by the loader.
