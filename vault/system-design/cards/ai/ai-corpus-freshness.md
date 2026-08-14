---
id: ai-corpus-freshness
node: ai.vector-search
type: qa
---
## Q
How do you keep a RAG corpus fresh as source documents change, and why does upgrading the embedding model force a special migration?

## A
Freshness: drive the index from the source of truth via **CDC or an event stream** — on document update, re-chunk, re-embed, and upsert; on delete, remove vectors (deletes are easy to forget and leak stale or unauthorized content into answers).

Model upgrades: embeddings from different models live in **incompatible spaces** — you cannot query old vectors with new-model query embeddings. Upgrading means **re-embedding the entire corpus**, usually into a parallel index with a cutover, which is why embedding-model choice is sticky and re-embed cost belongs in the design.
