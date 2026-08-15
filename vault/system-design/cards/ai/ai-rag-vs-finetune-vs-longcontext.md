---
id: ai-rag-vs-finetune-vs-longcontext
node: ai.rag
type: qa
---
## Q
To make an LLM answer from your company's data you can: RAG it, fine-tune on it, or stuff it all into the context window. When does each win?

## A
- **RAG**: default for **knowledge**. Wins when the corpus is large, changes often (update = re-index one doc, no retraining), needs **per-user access control** at retrieval time, or answers must cite sources.
- **Fine-tuning**: for **behavior, not facts** — style, format, domain jargon, tool-use patterns. Bad at knowledge: expensive to refresh, can't do permissions, can't cite, and facts get blended, not stored.
- **Long context**: fine when the corpus is small (fits comfortably), stable, and needed whole — but you pay its token cost and prefill latency **on every request**, and attention quality degrades over very long inputs.

Common production answer: RAG for facts, light fine-tune (or just prompting) for behavior.
