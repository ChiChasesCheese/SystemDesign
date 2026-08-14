---
id: ai-continuous-batching
node: ai.inference
type: qa
---
## Q
Why does LLM serving batch requests at the token level (continuous batching) instead of batching whole requests?

## A
GPUs are only efficient when work is batched, but LLM outputs have wildly different lengths. With **static batching**, the whole batch waits for its longest sequence — finished slots sit idle and new requests queue.

**Continuous (in-flight) batching** schedules per decode step: the moment a sequence emits its stop token, its slot is refilled with a waiting request. Utilization stays high regardless of length skew — the core scheduling idea behind vLLM/TGI-class servers and typically several-fold throughput over static batching.
