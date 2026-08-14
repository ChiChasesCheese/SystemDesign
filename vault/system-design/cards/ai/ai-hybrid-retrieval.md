---
id: ai-hybrid-retrieval
node: ai.vector-search
type: qa
---
## Q
Pure vector retrieval in a RAG system misses queries for "error `AUTH-4012`" and part numbers. Why, and what is the standard fix?

## A
Embeddings capture **semantic similarity** but blur exact tokens — rare identifiers, SKUs, names, and negations land poorly in embedding space, while lexical search (BM25) nails them but misses paraphrases.

Fix: **hybrid retrieval** — run BM25 and vector search in parallel and merge, typically with **Reciprocal Rank Fusion** (score by rank positions, so no score-scale calibration needed), then optionally a **cross-encoder reranker** over the fused top-k for precision where it matters.
