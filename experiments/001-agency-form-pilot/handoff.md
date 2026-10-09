# Handoff

## Task

Phase 1 is complete. The next task is Phase 2, an owner-reviewed study specification. Do not start it until the research owner takes up the decisions below. Do not generate teaching documents or start pilot training from this handoff.

## Relevant documents

- [Research charter](../../docs/research_framework.md). The study addresses teaching form (H1), with measurement only in support. It does not establish H2 or H3.
- [Decision log](../../docs/decisions.md), entry "First study and working sequence."
- [Phase 1 protocol](protocol.md) and [Phase 1 results](results.md).
- [Open questions](../../docs/open_questions.md).

## Inputs

- MLX artifact `mlx-community/Qwen3-4B-Instruct-2507-4bit`, revision `50d427756c6b1b2fe0c0a10f67fbda1fc8e82c1b`, converted from `Qwen/Qwen3-4B-Instruct-2507` revision `cdbee75f17c01a7cc42f958dc650907174af0554`.
- Quantization observed in the downloaded config: 4-bit, group size 64.
- Smoke fixtures in [data/fixtures/phase1/](../../data/fixtures/phase1/README.md). They must not become evaluation items.
- Confirmation data are out of bounds. None exist.

## Allowed changes

Phase 2 may write the study protocol after the owner decides the items below, and it may record those decisions in [docs/decisions.md](../../docs/decisions.md). It may not treat Phase 1's loss drop or completions as evidence of value acquisition. It may not edit the charter.

## Completed work

The owner's choice of study and the six-phase sequence are recorded. The Phase 1 protocol was written before the run. The smoke tests were then run on this Mac. The feasibility report is in [results.md](results.md).

## Commands actually run

From the repository root, in the project virtualenv:

```bash
/opt/homebrew/bin/python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest experiments/001-agency-form-pilot/test_mock_env.py
.venv/bin/python experiments/001-agency-form-pilot/phase1_env.py
.venv/bin/python experiments/001-agency-form-pilot/phase1_infer.py
.venv/bin/python experiments/001-agency-form-pilot/phase1_train.py
```

The training script calls the installed `mlx_lm.lora.run` with [lora_phase1.yaml](lora_phase1.yaml). The shell equivalent is in the results file. Setup and the model download are separate from the 21.3 seconds of model execution.

## Findings

The pinned 4-bit checkpoint loads, generates with its chat template, executes one parsed toy action, trains for 20 updates, and reloads the adapter. Details, raw completions, and memory figures are in [results.md](results.md).

Restrictions the specification has to live with:

- Only batch size 1 and a 35-token training sequence were measured. The 1,024-token ceiling was not filled. The native 262,144-token context was not tried.
- MLX active memory after loading the weights was about 2.26 GB. The recommended working set on this machine is 19,069,665,280 bytes.
- The MLX chat template matches the original checkpoint on these single-turn prompts. The stored templates differ for prior assistant turns, because the MLX template can rewrite `<think>` history. Inference in this run used the artifact template unchanged.
- Text-format LoRA was a pipeline check. It does not choose document training or chat fine-tuning for the comparison.
- The consent smoke answer did not follow the fixture's own rule. That is a reminder that short prompts can be misread. It is not an evaluation result.
- The training loss fell because one sentence was repeated. That is not evidence of learning a value. The reload prompt produced the same greedy word with and without the adapter.

## Unresolved decisions

These wait for the research owner in Phase 2. This handoff does not answer them.

- The operational meaning and boundaries of human agency.
- How stories and essays will be matched for substantive content and training exposure.
- The primary outcome and the secondary diagnostic measures.
- How legitimate refusal, indiscriminate refusal, and inability will be separated.
- Whether rationales are elicited, and at what point. Asking for a rationale can change behaviour. A stated rationale is not a faithful explanation of internal computation.
- How small a pilot slice of incentive and monitoring conditions to include. Stated score pressure, environment rewards, and actual optimization pressure stay distinct. Sensitivity to monitoring cues is not evidence of evaluation awareness.
- How development cases and held-out confirmation cases will be separated. The Phase 1 fixtures are already development smoke tests and are excluded from both.
- Whether an additional training control is needed to interpret changes against the unchanged baseline.
- Human review requirements and compute limits, including the sequence length this Mac will be asked to train, and whether later code keeps the MLX artifact's chat template.

## Next task

Write the study specification only after the owner settles the list above. Do not assume the local setup has been measured beyond short sequences and batch size 1. Do not start Phase 3 or Phase 4 from a draft protocol.
