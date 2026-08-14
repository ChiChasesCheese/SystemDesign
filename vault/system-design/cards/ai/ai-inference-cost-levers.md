---
id: ai-inference-cost-levers
node: ai.inference
type: qa
---
## Q
Latency on an LLM endpoint feels fine but the GPU bill is too high. Name four levers that cut cost per token without swapping hardware.

## A
- **Quantization** (weights and/or KV cache to 8- or 4-bit): shrinks memory and bandwidth needs → bigger batches per GPU, minor quality cost.
- **Right-size the model**: route easy requests to a small/distilled model, escalate hard ones (model cascade/router).
- **Prompt/prefix caching**: stop re-prefilling the shared system prompt on every call.
- **Speculative decoding**: a draft model proposes several tokens, the big model verifies them in one pass — more tokens per weight-load, same output distribution.

(Streaming, by contrast, is a perceived-latency lever — it doesn't reduce cost.)
