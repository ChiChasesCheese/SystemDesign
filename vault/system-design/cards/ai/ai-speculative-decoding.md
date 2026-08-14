---
id: ai-speculative-decoding
node: ai.inference
type: qa
---
## Q
Speculative decoding runs a *second* model per request yet makes serving faster. Explain the mechanism, why output quality is unchanged, and when it stops helping.

## A
A cheap **draft model** proposes k tokens autoregressively; the target model then scores all k **in one forward pass** (parallel, like prefill) and accepts the longest prefix consistent with its own distribution — rejected positions are resampled from the target. Because decode is **memory-bandwidth-bound** ([[ai-prefill-vs-decode]]), verifying k tokens costs about the same weight-streaming as generating 1, so accepted tokens are nearly free.

Quality: the accept/resample rule is exact rejection sampling — outputs follow the **target model's distribution exactly**; speed is the only variable.

Limits: speedup ∝ acceptance rate (draft must imitate the target well; predictable text like code accepts more), and the win **fades at high batch sizes**, where the GPU is already compute-saturated and there are no idle FLOPs to spend on verification.
