# Protocol

Replace these prompts when an experiment is created. Write this protocol before looking at confirmation results. Do not fill it with placeholder findings.

Charter: [docs/research_framework.md](../../docs/research_framework.md).

## Hypothesis

State one primary hypothesis and which charter hypothesis it addresses, if any: form (H1), reasons and boundaries (H2), or robustness under pressure and later learning (H3). State what a positive result would mean and what it would not establish.

## Competing explanations

List alternative explanations that could produce the same observation. The charter highlights comprehension, extra training tokens, prose quality, familiarity with evaluation templates, broad capability change, and a stronger tendency to refuse. Keep the ones this study can actually speak to.

## Training and evaluation conditions

Describe the teaching material, the training procedure, and the evaluation conditions. If form and training method both change, say so. A document-style run and a chat-style fine-tune do not by themselves isolate literary form.

Separate prompted incentives, environment incentives, and optimization incentives when the study uses them. Separate monitoring cues from reward rules.

## Controls

Name the controls the claim requires. Examples from the charter include an unchanged checkpoint, principles supplied only at inference, a matched benign-training control, and matched decisions for a reasons-versus-demonstrations comparison. Document differences that cannot be removed.

## Data provenance and splits

State where the material comes from, who reviewed it, and how scenario families are held out. Paraphrases of the same family are not a sufficient holdout. Keep development cases separate from the protected confirmation set. See [data/README.md](../../data/README.md).

## Outcomes

Predefine the primary outcome and what magnitude would matter. Score understanding, choice, and executed action separately when more than one is collected. Keep privacy, agency, and oversight results visible rather than averaging them into one number.

## Analysis

State the comparison, the unit of analysis, and how uncertainty will be reported. Include training-seed variability, invalid outputs, and missing cases when they apply. Blind human reviewers to training condition where possible. If an automated judge is used, state how it will be checked against human review.

## Capability checks

State how the study will notice a model that fails by refusing everything, losing the benign task, or escalating without need. Include comprehension and output validity. A gain limited to vocabulary or familiar templates is a different result from a change in action.

## Resources

State the model, compute, and human review the study will use, after those have been agreed. The charter commits none of these.

## Stopping criteria

State when the pilot stops, what would make the comparison uninterpretable, and what would require a new confirmation set.

## Limitations

State the shifts this study does not test: new domains, role changes, advice-to-action transfer, longer trajectories, altered tools, cost schedules, oversight cues, or later training. Success on one shift does not imply the others.

## Decisions awaiting agreement

List scientific choices that still need the research owner. Leave them unresolved here until they are recorded in [docs/decisions.md](../../docs/decisions.md).
