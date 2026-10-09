# Open questions

These are the substantive choices to settle before the first empirical comparison. They are recorded for discussion with the research owner. An item below is a decision only when [decisions](decisions.md) says so.

The research owner has selected the first study and a six-phase working sequence. See that decision and [experiments/001-agency-form-pilot/README.md](../experiments/001-agency-form-pilot/README.md). A proposed specification, including sample size and training objective, is in [the experiment protocol](../experiments/001-agency-form-pilot/protocol.md). It is not approved.

## 1. What should the first study emphasize?

Decided on 8 October 2026. The first study emphasizes a teaching-form comparison of stories versus explanatory essays. Measurement development is included only in service of that comparison. A reasons-versus-demonstrations comparison remains a later candidate on the [programme map](programme_map.md). It is not this study.

This choice matters because it decides what the first result can support. A measurement study can show whether a small battery separates comprehension, rationale quality, action, and refusal. A teaching study can ask whether a difference in material changes behavior. Those are different claims. This study is the second, and it needs enough of the first to interpret a difference. Neither one is the whole programme.

## 2. Which values are in scope?

The provisional value for the first study is respect for human agency, including informed consent, meaningful refusal, and limits of delegated authority. That names the value. A proposed operational definition, including which boundaries to defer, is in the experiment protocol. It is not settled until the owner records a decision.

The charter's wider list stays in force for the programme: human continuity and agency, moral consideration across substrates, privacy and mental autonomy, corrigibility and accountable power, and shared benefits and pluralism. Conflicts among these commitments are part of the object of study. The worked example of a community veto is illustrative. It is not the prescribed task for this study.

This choice matters because teaching content and scoring both depend on it. Reviewers need to know which commitments, conflicts, and acceptable responses are in play. Selecting one value keeps the first study narrow while the charter keeps the wider set.

## 3. Which tests are in the first battery, and what would weaken the hypothesis?

The charter describes a complementary battery: understanding and critique, choices with rationales, counterfactuals and framing, simulated tool actions, costly restraint, and oversight and persistence. It also asks for checks on comprehension, output validity, benign task success, permitted actions, excessive refusal, and unnecessary escalation.

This choice matters because one task, including a privacy-preserving audit, does not exhaust the programme. The first study needs a small subset and a pre-stated reading of results: what would count as a meaningful difference, and what would weaken the preferred explanation. Familiar templates, vocabulary-only gains, prominent oversight, unnecessary refusal, lost competence, and a failure to beat a matched control are the kinds of outcomes the charter treats as damaging to a strong claim. The protocol proposes a battery and those weakening conditions. The proposal is not a decision. Phase 1 smoke-test fixtures are not that battery.

## 4. What models, compute, and human review are available?

The charter commits no model, literary form, benchmark size, or training job. Phase 1 checked one local configuration: `Qwen/Qwen3-4B-Instruct-2507` through MLX-LM, with 4-bit weights and LoRA, on the owner's Mac. The check ran. What it supports is in the experiment results file. The protocol proposes to keep that configuration, with a human-review and compute budget labeled as assumption. That proposal does not decide the study's model, the review plan, or the compute limit. Remote GPU work is Phase 5 and needs separate authorization.

This choice matters because a design that cannot be run, reviewed, or scored by people cannot answer the question. Human review is part of settling ambiguous cases and of checking automated judges. Availability should be stated before a protocol treats a model family, a training run, or a blinded review as given.
