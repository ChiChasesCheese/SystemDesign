---
id: ai-temperature-sampling
node: ai.foundations
type: qa
---
## Q
What does the `temperature` parameter actually control on an LLM request, and when do you set it low vs high?

## A
The model outputs a **probability distribution over next tokens**; the sampler picks one. Temperature reshapes that distribution: **0 ≈ always pick the most likely token** (near-deterministic — not guaranteed identical across runs), **higher values flatten it** so unlikely tokens get picked more, giving variety and more derailments. `top_p` is a sibling knob that cuts off the improbable tail.

- **Low (0–0.3)**: extraction, classification, code, tool calls, evals — anything you validate or compare.
- **Higher (0.7–1)**: brainstorming, creative drafts, generating diverse candidates.

It is a dial on the **sampler**, not the model — no request-time setting makes the model "know" more.
