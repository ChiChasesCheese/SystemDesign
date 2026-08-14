---
id: ai-ann-tradeoff
node: ai.vector-search
type: cloze
---
Exact nearest-neighbor search over embeddings is a linear scan — O(N·d) per query — so vector databases use **ANN** indexes, which trade {{c1::perfect recall (they may miss some true neighbors)}} for {{c2::sublinear query time}}. Recall vs latency is tunable at query time (e.g. HNSW `efSearch`, IVF `nprobe`), so you benchmark recall@k on your own data instead of trusting defaults.
