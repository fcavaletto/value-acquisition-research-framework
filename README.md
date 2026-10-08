# Learning values that endure

Research repository for a programme on how models can acquire values and apply them in behavior that holds up under pressure.

## Purpose

The programme investigates how different training materials—synthetic documents, arguments, stories, dialogues, and demonstrations—can help models acquire and apply values, and how the resulting behavior holds up under unfamiliar situations, competing incentives, changing oversight, and subsequent learning.

Value acquisition is the centre of the programme. Evaluation is how we investigate whether an intervention worked and where it failed. A single benchmark, permission-following task, or training technique does not define the programme.

## Central question

How do different forms of training material influence a model's understanding and application of values, and how robust are the resulting behaviors under unfamiliar situations, competing incentives, changing oversight, and subsequent learning?

Scientific direction comes from the research charter: [docs/research_framework.md](docs/research_framework.md) (version 1.0, 8 October 2026). An experiment protocol may narrow one study. It does not replace the charter.

## Current status

No empirical experiment has been selected or run. This repository holds the charter, a map of candidate subprojects, a decision log, open questions, and an experiment template. See [docs/status.md](docs/status.md).

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

1. Agree the primary question with the research owner, and record that decision in [docs/decisions.md](docs/decisions.md).
2. Copy `experiments/_template/` to `experiments/NNN-short-name/`, using the next free number.
3. Write the protocol before collecting results. Name the connection to the charter and keep one primary question.
4. Use development material to refine the study. Keep confirmation data separate. Implementation work may read a confirmation set only when the research owner explicitly authorizes that access.
5. Record what actually happened in that experiment's `results.md`, and leave `handoff.md` current.

The steps in detail are in [experiments/README.md](experiments/README.md).
