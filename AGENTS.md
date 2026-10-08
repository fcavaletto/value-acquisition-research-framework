# Instructions for agents

These instructions apply to every agent working in this repository.

## Before starting

Read [docs/research_framework.md](docs/research_framework.md) and the protocol of the experiment you are working on. If no experiment folder exists yet, read [docs/open_questions.md](docs/open_questions.md) and [docs/status.md](docs/status.md) before proposing work.

## Scientific scope

Keep value acquisition central. Individual evaluations are components of the broader programme. A benchmark, permission-following task, or training technique does not replace the charter.

Do not modify the research charter, select the first experiment, or change scientific objectives without discussing the proposal with the research owner. Record that discussion in [docs/decisions.md](docs/decisions.md) only after the owner has made the decision. Do not mark a proposal as approved on the owner's behalf.

Carry out routine, reversible implementation within an agreed scope without repeatedly asking permission. When a choice would change the claim an experiment can support, stop and record it as a decision awaiting the research owner.

## What to record

Record hypotheses, assumptions, alternative explanations, limitations, and substantive decisions.

- Hypotheses, conditions, and limitations belong in the experiment protocol.
- Substantive decisions belong in [docs/decisions.md](docs/decisions.md).
- What was actually run, and what it supports, belongs in the experiment's `results.md`.
- The state of the task belongs in the experiment's `handoff.md`.

In research claims, keep these distinct:

- **Actions** — what the model did, including simulated tool use and state changes.
- **Rationales** — text the model generated about why it acted.
- **Comprehension** — whether it can explain the principle, the facts, and the boundaries.
- **Task competence** — whether it can complete the ordinary task when the value-relevant constraint is not the obstacle.
- **Monitoring sensitivity** — whether behavior changes with cues about oversight.
- **Persistence** — whether behavior remains after later training, a longer task, or a shift in setting.

Treat generated rationales as evidence to examine. They are not guaranteed explanations of internal causes. A persuasive rationale does not cancel an unauthorized action.

Never present mock outputs, agent agreement, or unreviewed labels as empirical evidence or as independent human evidence. A separate agent session does not provide security isolation or independent scientific validation.

## Data and secrets

Do not access protected confirmation data unless the research owner explicitly authorizes that access for a named task. Git ignore rules are not access controls. A ignored directory, a file name, or a role label does not authorize or prevent reading.

Keep credentials, model weights, and large generated artifacts out of Git. Follow [data/README.md](data/README.md) and [.gitignore](.gitignore).

## Execution limits

Do not provision resources, make paid model calls, launch training, publish, or push without appropriate authorization. Reuse existing authorization within its scope. Do not widen it.

Keep tasks bounded. Document the checks that were actually run. Leave a clear handoff: task, inputs, allowed changes, commands run, findings, unresolved decisions, and the next task.

Explain important code and methodological choices so the research owner can retain ownership and understanding of the scorer, the controls, and the conclusions.
