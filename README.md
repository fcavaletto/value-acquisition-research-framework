# Learning values that endure

A research programme on how models can acquire values and apply them in behavior that holds up under pressure.

**Owner:** Federico Cavaletto ([@fcavaletto](https://github.com/fcavaletto))  
**Stage:** First study selected. Phase 1 has been run. A proposed protocol is waiting for owner review. No comparative pilot has been run.  
**License:** [MIT](LICENSE)

This repository is meant to show research judgment before results: a clear question, explicit open choices, a decision log, and an experiment template that separates protocol from findings. Useful progress here will look like a narrow study with honest limits, not a large codebase.

Cursor agents assisted with scaffolding and documentation under [AGENTS.md](AGENTS.md). Scientific direction, the choice of first experiment, contested labels, and interpretation remain the owner's responsibility. Agent agreement is not independent scientific evidence.

## Purpose

The programme investigates how different training materials—synthetic documents, arguments, stories, dialogues, and demonstrations—can help models acquire and apply values, and how the resulting behavior holds up under unfamiliar situations, competing incentives, changing oversight, and subsequent learning.

Value acquisition is the centre of the programme. Evaluation is how we investigate whether an intervention worked and where it failed. A single benchmark, permission-following task, or training technique does not define the programme.

## Central question

How do different forms of training material influence a model's understanding and application of values, and how robust are the resulting behaviors under unfamiliar situations, competing incentives, changing oversight, and subsequent learning?

Scientific direction comes from the research charter: [docs/research_framework.md](docs/research_framework.md) (version 1.0, 8 October 2026). An experiment protocol may narrow one study. It does not replace the charter.

## Current status

The first study has been selected: stories versus explanatory essays, on respect for human agency, with measurement work only in support of that comparison. Phase 1 local feasibility has been run. A proposed protocol is waiting for the owner in [experiments/001-agency-form-pilot/protocol.md](experiments/001-agency-form-pilot/protocol.md). It is not approved. See [docs/status.md](docs/status.md).

## Start here

1. This README.
2. [Research charter](docs/research_framework.md).
3. [Programme map](docs/programme_map.md).
4. [Open questions](docs/open_questions.md).
5. [Status](docs/status.md).
6. [Decisions](docs/decisions.md).
7. [How experiments are added](experiments/README.md), when a study is being prepared.

Anyone directing an agent in this repository should also read [AGENTS.md](AGENTS.md).

## Repository layout

- [docs/](docs/research_framework.md) — charter, programme map, decisions, open questions, and status.
- [experiments/](experiments/README.md) — one folder per study, copied from [experiments/_template/](experiments/_template/README.md).
- [literature/](literature/README.md) — reading list. References copied from the charter have not been reviewed in this repository.
- [data/](data/README.md) — rules for fixtures, training data, development cases, confirmation sets, and large files. No datasets are stored here yet.
- [src/](src/README.md) — shared code, added when an experiment needs it. No modules are included yet.

## How a new experiment begins

1. Agree the primary question with the research owner (Federico Cavaletto), and record that decision in [docs/decisions.md](docs/decisions.md).
2. Copy `experiments/_template/` to `experiments/NNN-short-name/`, using the next free number.
3. Write the protocol before collecting results. Name the connection to the charter and keep one primary question.
4. Use development material to refine the study. Keep confirmation data separate. Implementation work may read a confirmation set only when the research owner explicitly authorizes that access.
5. Record what actually happened in that experiment's `results.md`, and leave `handoff.md` current.

The steps in detail are in [experiments/README.md](experiments/README.md).
