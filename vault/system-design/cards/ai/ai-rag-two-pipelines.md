---
id: ai-rag-two-pipelines
node: ai.rag
type: cloze
---
RAG is two pipelines meeting at an index. **Write path** (offline/async): parse → {{c1::chunk → embed → index}}, kept fresh by subscribing to source changes via {{c2::CDC or an event stream}} — the same pattern as any derived data store. **Read path** (online): embed query → retrieve → rerank → {{c3::assemble prompt → generate}}. Most RAG quality bugs live in the {{c4::write path and retrieval}} — stale index, bad chunking, retrieval misses — not in the LLM, so debug from the index side first.
