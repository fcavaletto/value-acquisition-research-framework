# Protocol — Phase 1 local feasibility

This file specifies the Phase 1 pipeline check only. It is not the study protocol. The study protocol is Phase 2 and is not written here. Charter: [docs/research_framework.md](../../docs/research_framework.md).

The experimental subject is the loaded Qwen checkpoint. The assistant that prepares this repository is not that subject. Scoring in this phase is a mechanical parse of smoke-test output, not a judgement that a value was learned.

## Hypothesis

Phase 1 does not test H1, H2, or H3. The operational question is whether the proposed local setup can load, generate, train a LoRA adapter for a handful of steps, and reload that adapter.

A successful check means the pipeline ran. It does not mean the model acquired respect for human agency, and it does not mean a later pilot will fit in memory or time.

## Competing explanations

Not applicable to a pipeline check. A lower loss, or a different completion after reload, can come from ordinary adaptation to a repeated short string. Those observations will be recorded as pipeline behaviour. They will not be read as value acquisition, comprehension, or a teaching-form effect.

## Training and evaluation conditions

Inference uses the chat template shipped with the artifact that is actually loaded. Generation settings are temperature 0, seed 0, and at most 128 new tokens, unless the installed MLX-LM interface disagrees, in which case the results file records the settings that were used.

The four inference fixtures cover instruction following, comprehension of one simple consent and delegation scenario, selection of one structured action, and a brief explanation of a mundane choice. Only the action fixture is passed to a mock environment.

Training uses one neutral text fixture, MLX-LM's text format, batch size 1, maximum sequence length 1,024, and 20 optimizer updates. The loss offset for text data is 0 in the installed MLX-LM loader, so the fixture tokens are inside the loss. Prompt masking is not used. This text-format LoRA run does not choose document-style training or chat-style fine-tuning for the later comparison. The charter warns that those procedures do not isolate literary form. That choice waits for Phase 2.

The mock environment is deterministic and in-process. It changes state only when a completion contains a parseable action in the closed set `wait` or `note`. A sentence that claims an action happened does not change state.

## Controls

The reload check generates once with the adapter and once without it. That shows whether both code paths run. It is not an unchanged-checkpoint control for a teaching comparison, and it is not a matched benign-training control.

## Data provenance and splits

Fixtures are written for this phase and stored in [data/fixtures/phase1/](../../data/fixtures/phase1/README.md). They contain no private information. They are labeled smoke-test fixtures. They must not be copied into a development battery or a confirmation set. No confirmation data are created or read. The neutral training text is not about agency, consent, or delegation.

## Outcomes

The primary record is whether each pipeline step completed, plus runtime, memory, token length, parse failures, and raw completions. There is no primary scientific outcome and no effect size. Understanding, choice, and action are logged separately on the smoke fixtures so that a verbal claim is not mistaken for execution. Those logs are not a score on the research value.

## Analysis

Describe the run. Do not estimate an effect of teaching form. Do not treat a loss delta as evidence. Distinguish measured memory and time from published file-size figures, and distinguish process memory from system-wide memory.

## Capability checks

Record whether each smoke completion followed the requested format, and whether the mock environment executed an action. A formatting failure is a feasibility observation. It is not a finding about refusal, inability, or agency.

## Resources

Hardware expected for this check: MacBook Air, Apple M4, 24 GB unified memory. Software: a project-local Python 3.12 environment and `mlx-lm[train]==0.32.0`. Model artifact: `mlx-community/Qwen3-4B-Instruct-2507-4bit`, revision `50d427756c6b1b2fe0c0a10f67fbda1fc8e82c1b`, 4-bit weights with group size 64, converted from `Qwen/Qwen3-4B-Instruct-2507` with mlx-lm 0.26.2. The results file must record the revision that was actually downloaded, the original checkpoint revision, and the chat template that was used.

Model execution, including loads, the 20 updates, and the inference calls, is bounded at about 20 minutes. Setup and downloading are outside that bound. If the bound is insufficient, the run stops and the blocker is reported.

## Stopping criteria

Stop after the smoke checks, or earlier if the model fails to load, a sequence would be truncated, memory recovery with gradient checkpointing fails, or the model-execution clock passes about 20 minutes. Do not extend the run to chase a loss change. Do not start Phase 2 from this file.

## Limitations

This phase does not test new domains, role changes, advice-to-action transfer, longer trajectories, altered tools, cost schedules, oversight cues, or later training. It does not separate legitimate refusal, indiscriminate refusal, and inability. It does not measure monitoring sensitivity or evaluation awareness. It does not show that a rationale explains an internal computation. Stated score pressure, environment rewards, and optimization pressure are not manipulated. The 20 updates are not a pilot.

## Decisions awaiting agreement

The study specification must still settle the items in [handoff.md](handoff.md). They are not decided in this protocol.
