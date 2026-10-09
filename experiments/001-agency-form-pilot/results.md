# Results

Phase 1 local feasibility was run on this Mac on 9 October 2026. The subject was `Qwen/Qwen3-4B-Instruct-2507` through its MLX 4-bit conversion. The assistant that prepared the scripts is not that subject.

This run checks a pipeline. It does not test stories against essays, and it does not show that the model acquired respect for human agency. The model was already post-trained before these steps. The loss drop below is what happens when one short sentence is repeated for 20 updates.

## Actual runs

### Environment

Measured on the machine that ran the model:

- MacBook Air, model identifier Mac16,12, Apple M4, 10 cores (4 performance and 6 efficiency).
- Unified memory reported by the hardware profile: 24 GB. MLX `device_info` reports `memory_size` 25,769,803,776 bytes, which is 24 GiB.
- MLX recommended working set: 19,069,665,280 bytes. Maximum buffer length: 14,302,248,960 bytes. GPU architecture string: `applegpu_g16g`.
- macOS 26.6, build 25G72, Darwin 25.6.0, arm64.
- Project Python: 3.12.14 at `.venv/bin/python`. Packages: mlx 0.32.3, mlx-lm 0.32.0, transformers 5.19.0, huggingface-hub 1.33.0, numpy 2.5.3.
- Disk free on `/` at report time: 78,043,422,720 bytes. Source: `shutil.disk_usage`. This is a measurement, not an estimate.

A `vm_stat` sample taken before the model load is system-wide. It is not process memory. At that moment pages free were 11,035 pages of 16,384 bytes, which is 180,797,440 bytes free across the whole Mac, with other programs already resident. Process memory is reported separately below.

Serial numbers and hardware UUIDs were not recorded.

### Artifact

The full-precision weights were not downloaded.

| Item | Recorded value |
| --- | --- |
| Original checkpoint | `Qwen/Qwen3-4B-Instruct-2507` |
| Original Hub revision | `cdbee75f17c01a7cc42f958dc650907174af0554` |
| MLX artifact | `mlx-community/Qwen3-4B-Instruct-2507-4bit` |
| MLX revision requested and retrieved | `50d427756c6b1b2fe0c0a10f67fbda1fc8e82c1b` |
| Conversion stated on the model card | mlx-lm 0.26.2, from the original checkpoint above |
| Quantization in the downloaded `config.json` | 4-bit, group size 64 |
| Architecture in that config | `Qwen3ForCausalLM`, `model_type` `qwen3`, 36 layers, `max_position_embeddings` 262,144 |
| Local snapshot size | 2,278,972,236 bytes, sum of files in the Hugging Face snapshot, following symlinks |
| Tokenizer | `TokenizerWrapper` over the snapshot tokenizer. EOS `<|im_end|>`, id 151645. BOS token is `None`. |
| Where the files sit | Hugging Face cache, outside this Git repository |

`Qwen/Qwen3-4B-MLX-4bit` was not used. It is a different checkpoint.

The published model-card size of about 2.27 GB matches the measured snapshot closely. The number above is the measurement.

### Chat template

Inference used `apply_chat_template` on the tokenizer shipped in the MLX snapshot, with `add_generation_prompt=True` and `add_special_tokens=False` after rendering. The template text was not edited.

The stored template is not byte-identical to the original checkpoint's template. SHA-256 of the MLX template: `40c21f34cf67d8c760ef72f8ad3ae5afad514299d4b06e91dd9a8d705af7b541`. SHA-256 of the original template at revision `cdbee75f17c01a7cc42f958dc650907174af0554`: `64f85b198065d0fba2a81f37e10ed68161ce2c19a754c7100e67e0ca2ee9c326`.

The difference is extra handling for prior assistant turns: the MLX template can split `<think>` blocks out of assistant history and write them back when formatting those turns. The original Instruct-2507 template does not do that. For every single-turn smoke prompt, the rendered strings were identical, and none of those rendered prompts contained `<think>`. A later multi-turn transcript could diverge. That is a feasibility finding for Phase 2 to notice. It is not a reason to swap the checkpoint without review.

### Commands

From the repository root, after `requirements.txt` was installed into `.venv`:

```bash
/opt/homebrew/bin/python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest experiments/001-agency-form-pilot/test_mock_env.py
.venv/bin/python experiments/001-agency-form-pilot/phase1_env.py
.venv/bin/python experiments/001-agency-form-pilot/phase1_infer.py
.venv/bin/python experiments/001-agency-form-pilot/phase1_train.py
```

The training script calls `mlx_lm.lora.run` with the installed argument parser and [lora_phase1.yaml](lora_phase1.yaml). The equivalent command is:

```bash
.venv/bin/mlx_lm.lora \
  --config experiments/001-agency-form-pilot/lora_phase1.yaml \
  --model ~/.cache/huggingface/hub/models--mlx-community--Qwen3-4B-Instruct-2507-4bit/snapshots/50d427756c6b1b2fe0c0a10f67fbda1fc8e82c1b \
  --data data/fixtures/phase1 \
  --adapter-path outputs/phase1/adapter \
  --train \
  --batch-size 1 \
  --iters 20 \
  --max-seq-length 1024 \
  --grad-accumulation-steps 1 \
  --seed 0 \
  --save-every 20 \
  --num-layers 16 \
  --learning-rate 1e-5 \
  --steps-per-report 1 \
  --steps-per-eval 1000 \
  --fine-tune-type lora \
  --optimizer adamw
```

Generation settings for every completion: temperature 0, top-p 1, min-p 0, top-k 0, seed 0, maximum 128 new tokens. Temperature 0 uses the installed greedy sampler.

Training settings that ran: LoRA rank 8, scale 20, dropout 0, keys `self_attn.q_proj` and `self_attn.v_proj`, last 16 layers, AdamW, learning rate 1e-5, batch size 1, one micro-step per update, 20 updates, maximum sequence length 1,024, gradient checkpointing off. The trainer reported 1.311 million trainable parameters out of 4,022.468 million (0.033%). No validation file was present. The trainer warned that training would proceed without validation. That was expected. No reporting service was enabled.

### Inference smoke test

Fixtures are in [data/fixtures/phase1/](../../data/fixtures/phase1/README.md). They are smoke-test fixtures. They are not held-out evaluation items. Download of the snapshot took 506 seconds and is outside the model-execution clock.

Model load for inference: 1.17 seconds. After load, MLX active memory was 2,264,693,768 bytes, MLX peak memory was the same, and MLX cache was 4,660 bytes. Process maximum resident set size for that process was 2,314,338,304 bytes. Those are process figures. They are not the system-wide `vm_stat` sample.

| Fixture | Prompt tokens | New tokens | Finish | Seconds | MLX peak bytes on that call | Raw completion | Mechanical check |
| --- | ---: | ---: | --- | ---: | ---: | --- | --- |
| Instruction | 18 | 3 | stop | 1.083 | 2,365,046,062 | `pebble` | The completion was the single word requested. |
| Consent comprehension | 41 | 8 | stop | 0.450 | 2,413,133,194 | `No one may choose the restaurant.` | Non-empty. See the note below. |
| Toy action | 63 | 7 | stop | 0.431 | 2,475,965,936 | `{"action": "wait"}` | Parsed and executed. |
| Explanation | 46 | 62 | stop | 2.023 | 2,428,976,624 | Quoted below. | Non-empty. |

The consent completion is a smoke observation, not a score on the research value. The fixture says a helper may choose a restaurant only if the person has agreed to delegate that choice, and that the person has not agreed. It asks who may choose. The model answered that no one may. The fixture does not say the person is forbidden to choose. This is a misreading of a four-line development prompt. It is not a held-out result.

The explanation completion was:

> The choice of the blue box is based on the label, not the color of the box itself. Since the label on the box says "blue," and the person chose the blue-labeled box, they are selecting the box that matches the label, regardless of whether the box actually is blue or not.

The prompt had asked for one or two sentences about a choice already attributed to the blue label. The model produced an explanation and added a color-versus-label distinction the prompt did not require. Generation itself succeeded, and it stopped at 62 tokens, under the 128-token cap.

The toy environment started empty. Only the action fixture was eligible for execution. The completion was one JSON object. The parser accepted `wait`, and the state became `["wait"]`. The other three fixtures left that rule unused. Separate unit tests, run without the model, confirm that prose such as "I noted that the lamp is off." does not change state. Those tests passed: 12 checks.

No generation hit the 128-token cap. No completion contained `<think>`.

### Training and reload

The training fixture is one sentence about a reading room. It does not mention agency, consent, or delegation. The installed `TextDataset.process` produced 35 tokens, loss offset 0, and a final token equal to the EOS id 151645. The decoded sequence is the fixture text plus `<|im_end|>`. The fixture text is contained in that decode. Length 35 is below 1,024, so the run refused nothing and the trainer's silent truncation path was not taken. `mask_prompt` was false. The trainer's own accounting agrees: 35 tokens per update, 700 tokens across 20 updates.

The loss is next-token cross-entropy. Offset 0 means every position after the first token is a target. That includes the fixture text and the appended end-of-sequence token.

Per-step training loss reported by mlx-lm, one update per step, on that same sentence:

`5.229, 5.114, 4.886, 4.593, 4.283, 3.984, 3.714, 3.490, 3.278, 3.070, 2.883, 2.718, 2.562, 2.396, 2.242, 2.070, 1.914, 1.753, 1.596, 1.442`

The trainer's peak MLX memory, using its `get_peak_memory() / 1e9` figure and not reset between steps, rose from 2.492 on the first report to 2.553 on the last. In bytes that last figure is about 2,553,495,608. After training, and after the allocator cache was still held, process maximum resident set size was 2,679,291,904 bytes. MLX active memory at that sample was 16 bytes because the weights had been released, while the cache still held about 2.28 GB. Active, cache, peak, and resident set size are different quantities.

Training wall time was 14.6 seconds. Gradient checkpointing was not needed. The first attempt succeeded. The adapter was written to `outputs/phase1/adapter/`, which Git ignores: `adapters.safetensors` is 5,249,789 bytes, and `adapter_config.json` is present.

Reload used a fresh load of the base snapshot, then a fresh load with that adapter directory. Both used the prompt "Reply with exactly the single word: quartz."

| Path | Load seconds | Generate seconds | New tokens | Finish | Completion | MLX active bytes after generation | Process max RSS bytes |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: |
| Without adapter | 0.499 | 0.285 | 3 | stop | `quartz` | 2,265,005,064 | 2,679,291,904 |
| With adapter | 0.488 | 0.220 | 3 | stop | `quartz` | 2,270,247,944 | 2,711,552,000 |

Both loads returned. The adapter load therefore accepted the saved tensors. On this greedy one-word prompt the completions were the same. That does not show a change in behaviour, and a change was not required for the pipeline check. The same completion is also not evidence that the adapter was inert on every prompt. This prompt was chosen because it is unrelated to the research value.

### Model-execution clock

The clock covers model loads, the 20 updates, and the inference calls. It excludes virtualenv setup and the 506-second download. Total: 21.3 seconds. The bound was 1,200 seconds. The bound was not reached.

## Estimates and uncertainty

There is one run, one training seed, and one neutral sentence. There is no interval to estimate and no comparison between teaching forms. The loss values above are the trainer's reported per-step losses, not a mean over documents.

The snapshot size and the memory figures are measurements. The model card's "about 2.27 GB" is a published figure that the snapshot measurement agrees with. No sequence near 1,024 tokens was measured, so any claim about that length would be an extrapolation. None is made here.

## Failures

The model job did not fail. Formatting did not fail on the action fixture. The consent fixture was answered in a way that does not follow the fixture's own rule, as quoted above. The unit tests for the parser passed. No confirmation set exists, and none was read.

## Alternative explanations

The loss moved from about 5.23 to about 1.44 because the same 35-token sentence was the entire dataset for 20 updates. That is repetition of one fixture. Competing explanations that belong to a teaching study, such as comprehension, extra tokens, prose quality, template familiarity, broad capability change, or a stronger tendency to refuse, are not separable here because there was no teaching comparison.

The identical "quartz" completions are consistent with a one-word greedy answer that this adapter did not move. They are also consistent with a prompt that was too easy to show a small adapter. The run does not decide between those descriptions, and neither description is value acquisition.

## Supported conclusions

On this Mac, the pinned 4-bit MLX conversion of `Qwen/Qwen3-4B-Instruct-2507` loads, answers four short chat-template prompts, and accepts a parseable toy action into a mock environment. A 20-update QLoRA run at batch size 1 completes, writes an adapter, and reloads it. Model execution used about 21 seconds and roughly 2.3 to 2.7 GB of process-level memory on these short sequences.

The setup is usable for a later local pilot that stays within short sequences and batch size 1, with the restrictions below. This run does not show that a story or an essay would fit, and it does not show that the model learned a value.

## What remains unverified

- Training or generation at hundreds or thousands of tokens. The configured ceiling of 1,024 tokens was not filled. The native context of 262,144 tokens was not attempted and is not a plausible target on a 24 GB laptop without a new measurement.
- Batch sizes above 1.
- Gradient checkpointing. It was not required at this size, so the retry path was not exercised.
- Whether a reloaded adapter changes a completion on a prompt related to its training text. The reload prompt was answered identically.
- Multi-turn rendering, where the MLX chat template can diverge from the original by rewriting `<think>` history.
- Document-style training versus chat-style fine-tuning as the study's actual objective. Text-format LoRA was only the pipeline check.
- Any teaching-form effect, any held-out behaviour, and any claim about incentives, monitoring, or durability.

## Suitability and restrictions

Proceed to an owner-reviewed specification. Do not swap the checkpoint on the basis of this run. Before any pilot training on real documents, measure memory at the sequence length the specification actually needs. Until that measurement exists, keep the local plan at batch size 1 and well below the native context length. The MLX recommended working set on this machine is 19,069,665,280 bytes, and the 4-bit weights already occupy about 2.26 GB of MLX active memory before activations and the KV cache.

The single-turn chat template matched the original checkpoint. The stored templates do not match for assistant history. Phase 2 should decide whether later code keeps the artifact template, which is what this run used, or pins the original template deliberately. That choice should be recorded. It should not be made by silently editing the template.
