---
id: ai-generation-loop
node: ai.foundations
type: qa
---
## Q
In backend terms: what does an LLM server actually do with a request, and why does the response stream out token-by-token instead of arriving at once?

## A
Two phases:

- **Prefill**: the whole prompt is read in one parallel pass — this sets **time-to-first-token**.
- **Decode**: a loop — predict the next token, append it to the input, repeat until a stop condition. Each token depends on everything before it, so generation is **inherently sequential**; there is no "compute the whole answer in parallel".

Consequences: latency scales with **output length**, streaming APIs exist because tokens genuinely become available one at a time, and the API is **stateless** — the server keeps no conversation memory; the client resends history every call.
