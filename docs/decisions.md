# Decision log

Record substantive scientific and organizational decisions here. A proposal is not a decision. Do not mark a choice as made until the named decision-maker has made it.

**Research owner:** Federico Cavaletto. In this log, “research owner” means that person.

Use one entry per decision, with these fields:

- **Date**
- **Question**
- **Alternatives**
- **Decision**
- **Rationale**
- **Evidence**
- **Decision-maker**
- **Affected work**

Routine implementation inside an already agreed scope does not need an entry. A change that affects the core question, the charter, the first experiment, or the claim a study can support does.

## 2026-10-08 — Research direction

- **Date:** 8 October 2026
- **Question:** What document defines this programme's scientific direction?
- **Alternatives:** Reconstruct a charter from memory, or adopt the document supplied by the research owner.
- **Decision:** The supplied charter is the research direction. It is [research_framework.md](research_framework.md), version 1.0, 8 October 2026. Repository initialization moved that file and did not change its contents.
- **Rationale:** The research owner provided the charter as the guiding document for the programme.
- **Evidence:** The charter file. It distinguishes normative proposals, empirical hypotheses, illustrative experiments, and evidence standards. It claims no completed experiments or findings.
- **Decision-maker:** Federico Cavaletto, by supplying the document.
- **Affected work:** The whole repository. Later experiments state which part of the charter they address. They do not narrow the charter to make implementation easier.

## 2026-10-08 — First experiment

- **Date:** 8 October 2026
- **Question:** Which empirical experiment should be selected and run first?
- **Alternatives:** The charter names a teaching-form comparison and measurement development in service of that comparison as the immediate fork. The [programme map](programme_map.md) describes further candidates. None of these has been chosen.
- **Decision:** Undecided at repository initialization. No empirical experiment had been selected, approved, or run.
- **Rationale:** The charter states that the choice of first study remains an explicit research-owner decision. Initializing the repository does not make that choice.
- **Evidence:** The charter sections "How to choose the first study" and "Next decision." No protocol, model, dataset, or pilot had been agreed. See [open questions](open_questions.md).
- **Decision-maker:** Pending Federico Cavaletto at the time of this entry.
- **Affected work:** [experiments/](../experiments/README.md) then contained only a template. This entry is superseded by the entry below.

## 2026-10-08 — First study and working sequence

- **Date:** 8 October 2026
- **Question:** Which empirical study comes first, and in what order should the work proceed?
- **Alternatives:** Leave the first study undecided. Select a measurement study on its own. Select a reasons-versus-demonstrations comparison. Select a teaching-form comparison, with or without measurement work in support of it.
- **Decision:** The first study is a teaching-form comparison of stories versus explanatory essays. The provisional value is respect for human agency, including informed consent, meaningful refusal, and limits of delegated authority. Measurement development is included only to support that comparison. The working sequence has six phases, recorded in [experiments/001-agency-form-pilot/README.md](../experiments/001-agency-form-pilot/README.md). Only Phase 1, local feasibility, is in scope for implementation. Phases 2–6 stay planned. They are not a promise to complete every later study, and they do not replace the charter. The local configuration to verify in Phase 1 is `Qwen/Qwen3-4B-Instruct-2507`, MLX-LM, 4-bit weights, and LoRA adapters. That configuration is not yet the study's committed model. If it fails, the subject is not swapped without review.
- **Rationale:** The research owner specified this study, this value, and this sequence. The charter already treats a narrow teaching-form comparison, supported by measurement, as one possible first contribution. A pilot on one value does not narrow the programme to that pilot.
- **Evidence:** The owner's Phase 1 instruction of 8 October 2026. No teaching materials, pilot training, or evaluation results existed when the choice was made. Suitability of the local setup is a later finding, recorded in the experiment's results file if a run occurs.
- **Decision-maker:** Federico Cavaletto.
- **Affected work:** [experiments/001-agency-form-pilot/](../experiments/001-agency-form-pilot/README.md). Open questions 1 and the value named in question 2. The operational boundaries of agency, the primary outcome, controls, human review, and compute limits remain open for Phase 2.
