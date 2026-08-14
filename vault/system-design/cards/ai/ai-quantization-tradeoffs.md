---
id: ai-quantization-tradeoffs
node: ai.inference
type: qa
---
## Q
Weight-only INT4/INT8 vs FP8 (weights + activations) vs KV-cache quantization: which serving bottleneck does each attack, and where are the quality cliffs?

## A
- **Weight-only (INT8/INT4, e.g. AWQ/GPTQ)**: shrinks weight streaming — attacks **memory-bandwidth-bound decode** and lets bigger models fit per GPU. Compute still runs in higher precision after dequant.
- **FP8 weights + activations**: engages the GPU's low-precision tensor cores — attacks **compute-bound prefill** too; needs hardware support (H100-class on).
- **KV-cache quantization (8/4-bit)**: attacks the **capacity ceiling on concurrency** — more sequences resident per GPU ([[ai-kv-cache]]).

Quality: 8-bit is near-lossless; **4-bit is where cliffs appear** — degradation is task-dependent (reasoning and long-context suffer first) and invisible to perplexity alone, so gate rollouts on your own task evals, not benchmark deltas.
