---
id: ai-retrieval-eval
node: ai.vector-search
type: qa
---
## Q
You want to change chunk size and swap the embedding model in your RAG system. How do offline and online evaluation divide the work of proving it's an improvement?

## A
- **Offline**: a **golden set** of real queries with labeled relevant docs; measure recall@k, MRR/nDCG per candidate config in minutes. This *gates* changes — cheap, reproducible, runs in CI — but only as good as the label set, which drifts from live traffic.
- **Online**: ship behind an experiment; measure end-task metrics — answer quality (thumbs, LLM-as-judge on grounded-ness), deflection/click-through, "no-answer" rate. This *validates* what offline can't see (query drift, latency effects on abandonment), but is slow and noisy.

Discipline: offline eval to kill bad candidates fast, online to confirm the survivor; continuously **harvest failed prod queries back into the golden set** so offline stays honest.
