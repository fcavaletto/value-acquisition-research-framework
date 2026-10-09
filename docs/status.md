# Status

Updated 9 October 2026.

**Research owner:** Federico Cavaletto ([@fcavaletto](https://github.com/fcavaletto)).

## Repository setup

Initialization of the repository is complete.

- The supplied charter was moved unchanged to [research_framework.md](research_framework.md). SHA-256: `e24f4a0e549f03d536c753fcdf2d53633146a1a4993854e2e957d1674247008e`.
- Added [the root overview](../README.md), [agent instructions](../AGENTS.md), [.gitignore](../.gitignore), and an [MIT license](../LICENSE).
- Added this status page, the [programme map](programme_map.md), the [decision log](decisions.md), and the [open questions](open_questions.md).
- Added the [experiment guide](../experiments/README.md) and the [experiment template](../experiments/_template/README.md).
- Added the [literature guide](../literature/README.md), a [reading list](../literature/reading_list.md) limited to the charter's three references, the [data guide](../data/README.md), and the [source guide](../src/README.md).
- The repository is public on GitHub: [fcavaletto/value-acquisition-research-framework](https://github.com/fcavaletto/value-acquisition-research-framework). Branch `master` tracks `origin/master`.
- Cursor agents assisted with scaffolding and documentation. Scientific decisions remain with the research owner.

No credentials were added. Model weights, adapters, and large generated outputs stay outside Git.

## Research progress

The research owner has selected the first study. It is a teaching-form comparison of stories versus explanatory essays. The provisional value is respect for human agency, including informed consent, meaningful refusal, and limits of delegated authority. Measurement development supports that comparison and does not replace it. The decision is in [decisions.md](decisions.md). The charter is unchanged.

The working sequence is in [experiments/001-agency-form-pilot/README.md](../experiments/001-agency-form-pilot/README.md):

1. Local feasibility.
2. Owner-reviewed study specification.
3. Teaching materials and evaluation development.
4. Local comparative pilot.
5. Remote GPU replication and expansion.
6. Further studies of incentives, monitoring, durability, other values, and teaching forms.

Phases 2–6 are planned. They are not a promise, and they are not started. Phase 1 has been run on the local Mac. The 4-bit MLX conversion of `Qwen/Qwen3-4B-Instruct-2507` loaded, generated with its chat template, executed one parsed toy action, trained a LoRA adapter for 20 updates, and reloaded it. The report is in [experiments/001-agency-form-pilot/results.md](../experiments/001-agency-form-pilot/results.md). That configuration is still not the study's committed model until Phase 2 says so. The smoke-test fixtures are not research evaluation items. The run does not support a finding about value acquisition. No pilot training has been run.

## Next discussion

Phase 2 is an owner-reviewed study specification. The decisions it must settle are listed in the experiment [handoff](../experiments/001-agency-form-pilot/handoff.md). The feasibility report is available for that discussion. This page is not approval to generate teaching documents or start pilot training.
