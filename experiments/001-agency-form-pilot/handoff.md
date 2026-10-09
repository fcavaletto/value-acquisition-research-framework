# Handoff

## Task

The Phase 2 review package is drafted. The next task is owner review. Do not start Phase 3, do not write a training corpus, and do not write a held-out set until the owner records decisions.

## Relevant documents

- [Research charter](../../docs/research_framework.md). This study addresses teaching form (H1). It does not establish H2 or H3.
- [Decision log](../../docs/decisions.md). The approved choice is the first study and the six-phase sequence. The protocol's recommendations are listed there as proposals, not as decisions.
- [Proposed protocol](protocol.md).
- [Phase 1 protocol](phase1_protocol.md) and [Phase 1 results](results.md).
- [Teaching examples](../../data/development/001-agency-form-pilot/teaching_examples.md) and [evaluation scenarios](../../data/development/001-agency-form-pilot/evaluation_examples.md).

## Inputs

- MLX artifact `mlx-community/Qwen3-4B-Instruct-2507-4bit`, revision `50d427756c6b1b2fe0c0a10f67fbda1fc8e82c1b`, from `Qwen/Qwen3-4B-Instruct-2507` revision `cdbee75f17c01a7cc42f958dc650907174af0554`. Quantization in the downloaded config: 4-bit, group size 64.
- Token counts on the four draft documents, measured with that tokenizer.
- Confirmation data are out of bounds. None exist.

## Allowed changes

The owner may revise the proposed protocol and record choices in the decision log. Implementation work may edit the draft to match those choices. It may not treat the draft as approval to train, and it may not treat Phase 1's loss drop as evidence of value acquisition. It may not edit the charter.

## Completed work

Phase 1 was run and reported. The proposed protocol, two illustrative teaching pairs, worked evaluation scenarios, a decision table, an assumed compute and review budget, Phase 2 completion criteria, and a Phase 3 task list are written. No research training and no held-out evaluation were run for this package.

## Commands actually run

Phase 1 commands are listed in [results.md](results.md). For this package, the only model-related command was a tokenizer count of the four draft documents, using `TextDataset.process` on the pinned snapshot. It did not load the weights for training and did not generate research outputs.

## Findings

The four drafts, including the end-of-sequence token the trainer would append, measure 623, 612, 587, and 579 tokens. Pair gaps are 11 and 8 tokens. Loss offset was 0. That measurement does not show that a 768-token update will fit in memory. Phase 1's 35-token run remains the only training measurement.

The Phase 1 restaurant answer, "No one may choose the restaurant," is addressed by separating a comprehension question (Sam may choose) from the executed booking. Those scenarios are development material.

## Unresolved decisions

Every row in the protocol's decision table. In particular, the owner still needs to judge:

- Whether the pilot includes a benign training adapter.
- Which agency boundaries are in the battery and which are deferred.
- Whether the primary outcome is the executed action, as proposed.
- Whether one seed and eight families are the right exploratory size.
- The document-length cap and the hardware check before any corpus is trained.

## Next task

Owner review of [protocol.md](protocol.md). Record accepted, revised, or rejected choices in the decision log. Do not treat this handoff as permission to begin the Phase 3 task list.
