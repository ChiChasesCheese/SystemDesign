---
id: ai-index-maintenance
node: ai.vector-search
type: qa
---
## Q
Your vector index takes constant upserts and deletes. Why does incremental maintenance degrade HNSW over time, and when do you pay for a full rebuild?

## A
HNSW handles inserts well, but **deletes are tombstones**: the graph node is marked dead, not removed, so searches still traverse it — as the deleted fraction grows, latency rises and recall drops (dead nodes were routing shortcuts). IVF degrades differently: **centroids go stale** as the data distribution drifts, unbalancing lists and hurting recall.

Practice:

- Engines compact continuously (segment merges that drop tombstones, à la Lucene) — know your engine's mechanism.
- Trigger a **full rebuild** when tombstone ratio or recall-benchmark drift crosses a threshold, built **blue-green**: construct the new index alongside, backfill, dual-write during the build, cut reads over, drop the old.

Same cutover machinery serves embedding-model upgrades ([[ai-corpus-freshness]]).
