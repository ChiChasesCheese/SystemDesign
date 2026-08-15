---
id: ai-retrieve-then-rerank
node: ai.rag
type: qa
---
## Q
Why do production RAG systems use two stages — a fast retriever pulling top-100 and then a reranker cutting to top-5 — instead of one better retriever?

## A
It's the classic **candidate-generation + ranking** split from search/recsys, forced by a precompute trade-off:

- **Retriever (bi-encoder)**: embeds documents **ahead of time**; query time is one embed + ANN lookup over millions of vectors. Cheap and scalable, but the query and document never "see" each other — scoring is coarse. Optimize for **recall**.
- **Reranker (cross-encoder)**: scores each (query, document) **pair jointly** — far more accurate, but nothing can be precomputed, so it only affordably runs over ~100 candidates. Optimize for **precision**.

Result: recall from the cheap stage, precision from the expensive one, latency bounded by reranking a fixed small set. Feed the reranker from hybrid (BM25 + vector) retrieval for best coverage.
