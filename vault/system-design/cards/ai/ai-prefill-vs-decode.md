---
id: ai-prefill-vs-decode
node: ai.inference
type: cloze
---
LLM inference has two phases with opposite bottlenecks: **prefill** (process the whole prompt, sets time-to-first-token) is {{c1::compute}}-bound and parallelizes across prompt tokens, while **decode** (one token per step, sets inter-token latency) is {{c2::memory-bandwidth}}-bound — each step streams the weights and KV cache. This is why servers batch aggressively during decode, and why disaggregated serving runs {{c3::prefill and decode on separate GPU pools}} so long prompts don't stall other users' token streams.
