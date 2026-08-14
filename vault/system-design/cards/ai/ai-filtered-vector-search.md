---
id: ai-filtered-vector-search
node: ai.vector-search
type: qa
---
## Q
"Top-10 similar docs WHERE tenant_id = 42": why does naive post-filtering break this query, and what do engines do instead?

## A
**Post-filter** (ANN top-k, then apply the predicate) fails when the filter is selective: if tenant 42 owns 0.1% of vectors, the top-50 ANN hits may contain **zero** matching docs — you return too few or garbage. Cranking k up to compensate destroys latency.

Alternatives:

- **Filter-aware traversal**: evaluate the predicate *during* HNSW/IVF search, only scoring passing vectors (Qdrant, pgvector w/ filtering, etc.) — works until the filter is so selective the graph becomes disconnected.
- **Partitioning**: one index (or namespace) per tenant/category — the right answer for multitenancy, which is also an **isolation** requirement, not just recall ([[ai-corpus-freshness]] notes the authorization-leak risk).
- **Brute-force fallback**: for tiny filtered sets, exact scan beats ANN.
