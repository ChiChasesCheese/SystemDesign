---
id: ai-pipeline-tracing
node: ai.evals
type: qa
---
## Q
A user reports one bad answer from your RAG/agent pipeline (query rewrite → retrieve → rerank → generate → tool calls). What does AI-specific tracing capture, and what question must it answer?

## A
Same shape as distributed tracing — **one trace per request, a span per step** — but each span records the **full inputs and outputs** (prompts, retrieved chunks with scores, model responses), plus token counts, model version, latency, and cost.

The question it must answer: **which step failed?** Retrieval missed the doc vs reranker buried it vs the model ignored good context vs a tool call errored — each has a completely different fix, and without payloads in the trace they're indistinguishable.

Second job: traced failures become **new eval-set cases**, closing the loop between production and the offline suite. (OpenTelemetry has GenAI semantic conventions for exactly this.)
