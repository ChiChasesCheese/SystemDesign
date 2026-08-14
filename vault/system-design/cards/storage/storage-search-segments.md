---
id: storage-search-segments
node: storage.search
type: qa
---
## Q
Lucene segments are immutable. What do update and delete actually do, and what background process pays the bill?

## A
- **Delete**: the doc is only *marked* in a per-segment deletion bitmap; it still occupies space and is filtered out at query time.
- **Update**: delete-mark the old version + index a full new document into a fresh segment — there is no in-place field update.

**Segment merging** pays the bill: background merges combine small segments into larger ones, physically dropping deleted docs. It's Lucene's compaction — same trade as [[storage-amplification-triangle]]: merge I/O competes with queries, and an update-heavy index carries growing "deleted but not merged" overhead (watch `docs.deleted`). Per-query cost also scales with segment count, which is why merging matters for latency, not just space.
