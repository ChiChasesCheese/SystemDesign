---
id: storage-search-deep-pagination
node: storage.search
type: qa
---
## Q
Why does `from=99000, size=20` melt a sharded search cluster when page 1 is instant, and what's the correct pattern for deep result access?

## A
Results come from distributed top-K: **every shard** must compute and return its own top `from+size` (99,020) scored docs, and the coordinator merges all of them to pick 20 — cost grows linearly with depth **multiplied by shard count**, mostly to produce results it throws away. Elasticsearch caps `from+size` at 10,000 for this reason.

Correct patterns:
- **`search_after`**: cursor on the sort values of the last hit — each shard returns only 20 docs after that key; depth-independent. (With a point-in-time snapshot so pages stay consistent.)
- For full exports, don't paginate a search engine at all — scan the source of truth ([[storage-search-not-sot]]).
