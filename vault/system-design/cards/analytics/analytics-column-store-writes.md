---
id: analytics-column-store-writes
node: analytics.olap
type: qa
---
## Q
Compressed sorted columns can't be updated in place. How do column stores accept writes anyway?

## A
The LSM move: writes land in a small **row-oriented (or unsorted) in-memory delta store**, and queries transparently merge the delta with the immutable, compressed column files. Background jobs periodically **rewrite/merge** deltas into new sorted column segments.

Consequences to know:
- Single-row updates/deletes are expensive relative to appends — column stores want **bulk, append-mostly** ingestion.
- A query is only fast again after merges keep the delta small; heavy trickle updates degrade scan performance.

Same amplification triangle as [[storage-amplification-triangle]], applied to analytics.
