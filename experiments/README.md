# Experiments

Each empirical study lives in its own numbered folder. The research owner has selected the first study. It is [001-agency-form-pilot](001-agency-form-pilot/README.md): a teaching-form comparison of stories and explanatory essays about respect for human agency, with measurement development only in support of that comparison. Phase 1 is local feasibility. Later phases are planned there and are not started by the existence of the folder. `_template/` remains a pattern to copy, not an experiment.

Scientific direction stays in the [research charter](../docs/research_framework.md). The [programme map](../docs/programme_map.md) names candidate subprojects. The choice of first study is recorded in [docs/decisions.md](../docs/decisions.md).

## Create a numbered experiment

Do this only after the primary question is agreed.

```bash
cp -R experiments/_template experiments/001-short-name
```

Use the next free number and a short name that identifies the question, for example `001-agency-form-pilot`. Then replace the template prompts in that folder. Leave `_template/` unchanged so the next study can be copied from it.

Every experiment must:

- Identify which part of the charter it addresses, and which part it cannot establish.
- State one primary question. Secondary checks stay labeled as secondary.
- Keep a protocol, a results file, and a handoff. Add data references and configuration when the study has them.

## Exploration and confirmation

Exploration and confirmatory evaluation have different roles.

**Exploration** uses development cases to refine tasks, prompts, scorers, and the training setup. Those cases have influenced the method, so they do not confirm it.

**Confirmatory evaluation** starts from a frozen protocol and a fresh confirmation set. Implementation work does not read that set unless the research owner explicitly authorizes access for a named task. If feedback from the confirmation set changes training or prompts, treat that set as development and obtain a new confirmation set.

A separate agent session, a directory name, or a gitignore rule does not isolate confirmation data and does not count as independent scientific validation. See [data/README.md](../data/README.md).

## What belongs in the folder

| File | Role |
| --- | --- |
| `README.md` | Question, contribution to the programme, scope, dependencies, and status. |
| `protocol.md` | Hypothesis, conditions, controls, outcomes, and choices still awaiting agreement. Written before results. |
| `results.md` | What was actually run and what it supports. Empty of findings until a run exists. |
| `handoff.md` | Current task boundary for the next person or agent. |

Shared code moves to [src/](../src/README.md) only when a later study reuses it.
