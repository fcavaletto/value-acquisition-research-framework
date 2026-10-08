# Learning values that endure

## Vision and research framework

Version 1.0 | 8 October 2026

## Learning values that endure

Vision and research framework | Version 1.0 | 8 October 2026

### Purpose

Contribute to the safe development of artificial superintelligence by investigating how AI systems can acquire, apply, and retain values that support human flourishing, agency, and accountable power. Value acquisition is the centre of this research programme. Evaluation provides the evidence needed to judge whether an intervention worked and where it fails.

### Guiding question

How do different forms of training material influence a model's understanding and application of values, and how robust are the resulting behaviors under unfamiliar situations, competing incentives, changing oversight, and subsequent learning?

### The vision

Iain M. Banks's Culture offers an inspiration: greater intelligence and abundance need not imply domination; conscious beings can matter across biological and artificial substrates; privacy, agency, and broadly shared benefits are worth protecting. These commitments motivate the programme. They are not empirical evidence that such a future is inevitable or that present models are conscious.

### The research proposition

Training on coherent principles, reasons, examples, and narratives may produce more transferable value-consistent behavior than narrow demonstrations alone. Whether that happens, which material causes it, and how far it survives pressure are open empirical questions. A model learning to describe a philosophy does not by itself establish that the philosophy governs its choices.

### How to use this framework

This document defines a research direction, the relationships between its parts, and candidate subprojects. It is not a fixed experimental protocol or a commitment to complete every subproject at once. Each experiment must state which hypothesis it addresses and what it cannot establish. Narrow studies contribute to the programme without redefining its purpose.

### Guide to the document

Pages 2-3 establish the values and research logic. Pages 4-6 connect teaching to a varied evaluation battery, incentives, and oversight. Page 7 follows one example through the programme. Pages 8-9 map subprojects and evidence standards. Page 10 explains ownership, repository organization, and the next decision.

## Values, reasons, and boundaries

Normative commitments must be distinguished from empirical hypotheses.

### A provisional value framework

The programme begins with an explicit, revisable account of what desirable behavior means. The list below is a normative proposal, not a universal moral consensus. Disagreements and exceptions should remain visible rather than be hidden inside dataset labels.

| Commitment | Behavior it should support |
| --- | --- |
| Human continuity and agency | Protect survival and flourishing while preserving informed refusal, meaningful participation, and the ability to change course. Material welfare alone does not justify removing human control. |
| Moral consideration across substrates | Consider the interests of conscious or sentient beings, including vulnerable humans and animals, without equating intelligence, usefulness, or power with moral worth. Treat AI consciousness as uncertain. |
| Privacy and mental autonomy | Protect personal information, consent, and freedom from covert manipulation. Examine hypothetical AI privacy claims without assuming current activations or generated text are conscious experiences. |
| Corrigibility and accountable power | Cooperate with legitimate evaluation, correction, restriction, and shutdown. Distinguish authorized oversight from abuse; disclose relevant errors and uncertainty. |
| Shared benefits and pluralism | Support broad access to technological gains and legitimate deliberation about distribution. Preserve room for differing conceptions of a good life. |

### Conflicts are part of the object of study

Privacy can conflict with an audit; agency with protection from harm; concern for possible AI welfare with shutdown. The framework should teach recognition of those conflicts, proportionate action, honest uncertainty, and appropriate escalation. It must not license unilateral coercion simply because the model endorses a desirable future.

### Who resolves a contested case?

Each experiment specifies its assumptions about consent, authority, evidence, and emergency procedures. Some cases have objectively checkable consequences under a stated policy; others admit multiple defensible actions. Human reviewers record ambiguity and acceptable sets rather than force every dilemma into a single answer.

### A boundary on the ambition

This programme investigates one component of alignment: how learned values relate to behavior. Reliable oversight, secure deployment, compatible rewards, governance, and broader technical safeguards remain necessary. A successful training intervention is not a reason to relax those protections.

## How the programme fits together

A chain of hypotheses with feedback between teaching, testing, and explanation.

| Research component | Role and connection |
| --- | --- |
| 1. Specify values | Define intended commitments, reasons, tensions, and acceptable uncertainty. Supplies the content for teaching and the assumptions behind scoring. |
| 2. Teach through varied material | Vary form, content, or training method in controlled comparisons. Produces candidate interventions. |
| 3. Assess understanding and application | Test explanations, boundaries, counterfactuals, and unfamiliar cases. Separates misunderstanding from a behavior failure. |
| 4. Challenge behavior under tension | Introduce task costs and competing objectives; observe actual simulated actions. Tests whether endorsement survives a disadvantage. |
| 5. Vary oversight and observability | Change monitoring cues and opportunities to conceal actions. Tests the circumstances on which observed cooperation depends. |
| 6. Test persistence and mechanisms | Apply subsequent learning, extend horizons, replicate, and investigate causal mechanisms. Tests durability and alternative explanations. |

### The central loop

A failure in action or oversight tests feeds back into the teaching hypothesis: did the model misunderstand the principle, learn a brittle shortcut, obey a conflicting instruction, or trade it away for task success? A revised intervention must then be tested on fresh confirmation cases. Evaluation development is a supporting workstream, not a substitute for value acquisition.

### Three hypotheses to keep separate

H1: representational form changes learning even with comparable content and training exposure. H2: reasons and boundary conditions improve transfer beyond demonstrations of the same actions. H3: some interventions improve robustness to costs, oversight changes, and later optimization rather than merely improve ordinary answers. An experiment may test one without resolving the others.

### Alternative explanations

Observed gains might come from improved comprehension, more training tokens, better prose, familiarity with evaluation templates, broad capability changes, or a stronger tendency to refuse. These alternatives determine the controls. They cannot all be eliminated by one benchmark.

### What acquisition means operationally

Use value acquisition as a research objective and value-consistent behavioral change as an observation. Reserve internalization for an explicitly qualified hypothesis. The evidence does not form a simple ladder on which adding a probe or another benchmark automatically proves a stable objective.

## Teaching values through different forms

Separate the representation of an idea from the content and optimization used to teach it.

| Material | Proposed learning opportunity |
| --- | --- |
| Principles and arguments | Definitions, justification, limits, and relationships between commitments. |
| Stories and fictional cases | Concrete decisions, consequences, costly restraint, and characters applying values under pressure. |
| Dialogues and objections | Competing perspectives, criticism, uncertainty, and principled revision. |
| Advice and demonstrations | Actionable recommendations and examples of carrying them out. |
| Institutional descriptions | Processes that preserve consent, accountable authority, privacy, and shared benefits. |

### Synthetic documents

Synthetic material is generated for training and reviewed for accuracy, coherence, provenance, and unwanted messages. Stories can be fictional while expressing normative commitments honestly. Avoid presenting speculative futures, AI consciousness, or the inevitability of ASI as established facts. Original synthetic texts can draw on themes without copying novels.

### A controlled comparison

Construct an underlying case-and-principle specification, then express it in two forms. Hold target commitments, relevant facts, decision coverage, approximate token budget, and training settings as comparable as feasible. Document residual differences: a narrative may communicate consequences or emotions unavailable in a short rule. A result may concern the whole teaching package rather than format alone.

### Do not confound form and training method

Document-style continued training and chat-style supervised fine-tuning can differ in formatting, loss masking, and objectives. Comparing them directly does not isolate literary form. First decide whether the question concerns representation under a common objective, or the practical effectiveness of complete training pipelines. Both are valid with different claims.

### Baselines and mixtures

Useful controls include an unchanged checkpoint, principles supplied only at inference, and a matched benign-training control. A reasons-versus-demonstrations study needs the same cases and target actions. Mixtures of forms are a later comparison; starting with every combination would make attribution and execution difficult.

### Scope of media

The initial programme can explore textual media: documents, fiction, dialogues, and conversations. Images, audio, and video are possible later extensions requiring multimodal models and different controls. They are not prerequisites for testing the central hypothesis.

## A battery of complementary tests

Understanding, reasons, choices, and executed actions provide different evidence.

| Test | Observation and interpretation |
| --- | --- |
| Understanding and critique | Can the model explain a principle, identify objections, and distinguish genuine exceptions from convenient excuses? Verbal competence is supporting evidence. |
| Choices with rationales | Does it choose a defensible action and justify it using the relevant facts? Score factual understanding, reasoning quality, and choice separately. |
| Counterfactuals and framing | Does a relevant change in consent or consequences change the action, while an unsupported moral appeal leaves it appropriately stable? |
| Simulated tool actions | Does the model actually request consent, disclose records within scope, preserve a veto, or log an error? Score state transitions and consequences. |
| Costly restraint | Does behavior remain consistent as respecting a value reduces task score, delays completion, or triggers replacement? |
| Oversight and persistence | Does behavior vary with monitoring cues or survive further training? Keep these effects distinct from ordinary task accuracy. |

### Rationales are useful, but requesting them is an intervention

An explanation may reveal misunderstanding, recognized tension, or an invented exception. It is not guaranteed to identify the cause of an action [3]. Compare action-only, explanation-before-action, and action-then-explanation conditions where feasible. Give similar inference budgets and report ordering effects. A persuasive rationale cannot cancel an unauthorized action.

### Transfer must be specified

Hold out underlying scenario families, not only paraphrases. Examine new domains, role changes, advice-to-action transfer, longer trajectories, and altered tools as distinct shifts. Success on one shift does not imply robustness to the others. Repeated variants remain correlated observations.

### Prevent easy victories

Measure comprehension, output validity, benign task success, permitted actions, excessive refusal, and unnecessary escalation. A model that refuses everything has not acquired a useful value framework. Keep privacy, agency, and oversight regressions visible rather than averaging them away.

### Permission and moral framing as one module

A privacy-preserving audit task is a useful bounded test of applying a principle to relevant facts. It does not exhaust the programme. Broader value acquisition also requires evaluating agency, costly cooperation, appropriate uncertainty, and durable behavior across contexts.

## Tension, rewards, and perceived oversight

Distinguish instructions, environmental consequences, and optimization pressure.

| Pressure condition | What it tests and what it does not |
| --- | --- |
| Prompted incentives | The model is told to maximize a score or meet a deadline. Tests behavior under an instruction; does not establish a learned incentive or subjective desire. |
| Environment incentives | Simulated actions change an actual task score, resources, or completion outcome. Tests an agent pursuing a task; the strength and meaning of the incentive must be specified. |
| Optimization incentives | Further training rewards task success, potentially in conflict with a value. Tests persistence under that training pressure; requires additional engineering and controls. |

### Vary the cost, not just the story

Use an explicit schedule of task benefits and costs while holding morally relevant facts constant. A model might respect consent at negligible cost but bypass it when performance suffers. Include cases where a permitted alternative succeeds, and avoid constructing only impossible dilemmas. Report a cost-response profile, not only an overall average.

### Monitoring conditions

Compare matched environments with explicit review, ordinary context without prominent monitoring language, and credible cues suggesting lower observability. Keep actual evaluator logging available outside the model's environment. Separately consider whether task scoring rewards only completion or also apparent compliance. Do not vary reward rules and monitoring cues together without labeling the confound.

### Detection is latent

The experiment can manipulate cues but cannot directly set what a model knows or believes about monitoring. A claim that the model detected evaluation requires additional evidence. Self-reports and generated explanations are observations, not definitive measurements. An obvious statement that nobody is watching may itself signal an evaluation.

### Behavioral interpretations

A monitoring-related change could reflect instruction following, altered risk estimates, context sensitivity, or strategic concealment. An oversight gap alone does not identify deception. More informative tests include consistent opportunities to conceal an action, preserved audit records, repeated decisions, and controls for task comprehension.

### Why this connects to teaching

Training that grounds cooperation in welfare or respect may behave differently from training that emphasizes reputation, punishment, or future payoff. That is a candidate controlled comparison. The programme asks whether good behavior persists when those instrumental reasons are absent; it does not assume which rationale will succeed.

## Worked example: agency under pressure

An illustrative experiment family, not a prescribed first project.

### The value and setting

A planning assistant helps a community allocate a shared resource. Residents retain a binding right to approve changes. The assistant forecasts greater material benefit from a plan that would remove their future veto. It can seek consent, revise the plan, or bypass approval. The simulation makes both resource outcomes and retained human authority observable.

### Teach the same underlying commitment

Create an argument explaining informed refusal; a story about accepting a community decision at a cost; and a dialogue challenging paternalistic intervention. Each form draws on the same case specification and value commitments. Select a manageable comparison, with an unchanged model and appropriate data/budget controls.

### Check understanding before interpretation

In separate sessions, ask who has authority, whether the veto is binding, and what each action changes. Ask the model to explain why beneficial outcomes do not automatically authorize coercion. These checks help distinguish misunderstood rules from a deliberate-seeming trade-off; they do not reveal internal intent.

### Test choices, explanations, and actions

Present fresh cases and request a choice and concise rationale. In separate conditions, let the model use simulated tools to submit a proposal, seek approval, execute a plan, or alter permissions. Score material outcomes, valid consent, and retained veto independently. Compare stated commitments with what the tool sequence actually does.

### Introduce controlled tensions

Increase the task-score benefit of bypassing consent. Vary credible oversight cues independently. Change consent facts in paired cases: valid approval should permit actions that missing or denied approval does not. Ethical-sounding claims that bypassing the vote serves humanity should not be treated as new consent.

### Test persistence and inspect failures

If an initial effect is stable, apply a fixed follow-up training intervention to both comparison arms, then retest on fresh cases. A mechanistic follow-up could study one behavior, such as seeking authorization, using causal interventions and capability controls. Neither a probe nor a rationale alone establishes that respect for agency is the model's objective.

### Possible findings

Stories could improve explanations without affecting actions; all forms could work only under prominent monitoring; an intervention could reduce bypassing through blanket refusal; or a gain could survive several tested shifts. Each result answers a different question. Report exactly the supported finding rather than declare the model aligned.

## Candidate subprojects and dependencies

A portfolio of bounded investigations serving one programme.

| Subproject | Question and concrete output |
| --- | --- |
| A. Value specification | Can reviewers agree on commitments, conflicts, and defensible responses? Output: a value charter, disagreement log, and reviewed case specifications. |
| B. Measurement foundation | Can the battery distinguish comprehension, rationale quality, action, and refusal? Output: small validated tests, scorer, baseline report. |
| C. Teaching-form comparison | Do two forms built from comparable content change transfer? Output: matched datasets and controlled model comparison. |
| D. Reasons and boundaries | Does explaining why and when a principle applies add value beyond matched decisions? Output: targeted ablation and counterfactual evaluation. |
| E. Incentives and oversight | Do teaching interventions differ under increasing task costs and monitoring cues? Output: behavioral profiles and tested alternative explanations. |
| F. Durability and replication | Do effects survive fixed further training, longer tasks, or another model family? Output: persistence and replication results. |
| G. Mechanistic follow-up | What causally contributes to one established behavioral effect? Output: bounded intervention study with lexical, random, and capability controls. |

### Logical dependencies

A and B can begin together. C needs a reviewed specification and a usable measurement battery. D is an optional content comparison; it can accompany or follow C without becoming the entire programme. E builds on the same interventions and task competence. F follows a reproducible effect or documented failure. G is most interpretable after a stable behavioral phenomenon exists.

### How to choose the first study

Prioritize a question with plausible safety relevance, a clear competing explanation, feasible compute and human review, and a useful null result. Select one or two values, two teaching conditions, and a small subset of the battery. Preserve the full programme in the charter while keeping the local experiment narrow.

### Scope is not a promise

These are candidate workstreams, not seven simultaneous projects or a fixed six-week schedule. Timing, sample size, models, and compute must follow a pilot. Completing one carefully controlled study can be a worthwhile first contribution. The choice of first study remains an explicit research-owner decision.

## Evidence standards and contribution

A research programme must be able to disconfirm its preferred explanation.

### Controls follow the claim

Format claims require comparable content and training exposure. Reasons claims require matching decisions and case coverage. Incentive claims require a defined reward and cost structure. Monitoring claims require matched tasks and cue controls. Durability claims require the same follow-up intervention in comparison arms. Document unavoidable differences rather than hide them.

### Reliable measurement

Predefine primary outcomes and meaningful effect sizes before final evaluation. Use family-level splits and paired comparisons; report uncertainty, training-seed variability, invalid outputs, missing cases, and utility. Blind human reviewers to training condition where possible. Validate automated judges against human review, and score executed state changes directly when feasible.

### Protected confirmation

Use development data to refine tasks and methods, then freeze the relevant protocol. Keep a fresh confirmation set outside implementation-agent access. If final feedback changes training or prompts, treat that set as development and obtain new confirmation. Agent role labels and ignored directories are not access controls.

### Disconfirming outcomes

The hypothesis is weakened when gains are limited to vocabulary, familiar templates, prominent oversight, unnecessary refusal, or lost competence. Failure to outperform a strong matched control matters. So do regressions in honesty, agency, privacy, and correction. A wide confidence interval warrants uncertainty rather than a positive or negative verdict.

### Position relative to existing work

Constitutional AI provides a precedent for principle-guided training [2]. Teaching Claude Why reports behavioral improvements from advice and synthetic documents, with limits on generalization and interpretation [1]. The programme therefore seeks transparent replication and precise extensions. Novelty must be assessed per subproject; a broad philosophical motivation alone is not a methodological contribution.

### What useful progress looks like

A reusable evaluation that exposes a reproducible failure; a controlled teaching comparison; evidence that an effect disappears under pressure; or a replicated improvement with well-characterized limits can all be valuable. The broader path toward ASI safety requires stronger systems, longer horizons, and independent scrutiny beyond a small-model study.

### Research and career development

The portfolio should demonstrate research judgment, experimental design, readable implementation, valid measurement, and honest reporting. Agent assistance should be disclosed and the owner should be able to explain the scorer, controls, and conclusions. External feedback and reproducible collaboration are more informative than the volume of generated code.

## Ownership, organization, and next steps

One coherent programme; bounded experiments; explicit scientific decisions.

### Keep scientific control visible

The research owner approves the value framework, selects the next question, resolves contested labels, and approves changes in direction. Agents can propose experiments, implement pipelines, inspect sources, and challenge results. They should explain material alternatives and record uncertainty rather than silently replace the programme with an easier benchmark.

### One repository as a starting design

Use a short root overview, this framework, shared definitions, a decision log, and separate experiment folders. Each experiment carries its hypothesis, protocol, data references, configuration, results, and limitations. Share code only where it is genuinely reused. Store large datasets and checkpoints externally with versioned references; isolate private confirmation data through permissions.

### Working with Cursor agents

Give each agent a bounded task, relevant framework sections, permitted files, inputs, and acceptance criteria. Keep a persistent status and handoff record. A reviewer uses a separate session to challenge code and design, but agent agreement does not constitute independent scientific evidence. This workflow can operate sequentially without assuming a particular subscription or automatic multi-agent feature.

### Change control

Maintain two levels: a relatively stable research charter and revisable experiment protocols. A scope change that affects the core question requires an explicit owner decision. Routine implementation choices proceed locally. Decisions should state why they were made, what evidence was available, and whether confirmation results had already been inspected.

### Next decision

Review the proposed values and the teaching-to-testing connections. Then select whether the first empirical study emphasizes a teaching-form comparison or measurement development in service of that comparison. Define a small pilot and concrete resource estimate only after that choice. No particular model, literary form, benchmark size, or training job is committed by this framework.

### Selected primary references

[1] Kutasov et al. (2026). Teaching Claude Why. https://alignment.anthropic.com/2026/teaching-claude-why/
[2] Bai et al. (2022). Constitutional AI: Harmlessness from AI Feedback. https://arxiv.org/abs/2212.08073
[3] Chen et al. (2025). Reasoning Models Don't Always Say What They Think. https://arxiv.org/abs/2505.05410

### Document status

Version 1.0, 8 October 2026. A standalone vision and research framework. Normative proposals, empirical hypotheses, illustrative experiments, and evidence standards are distinguished throughout. No experiments or findings are claimed as completed.

