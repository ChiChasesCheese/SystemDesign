---
id: distributed-global-index-staleness
node: distributed.partitioning.indexes
type: qa
---
## Q
A global (term-partitioned) secondary index is updated asynchronously. Name the two failure modes this creates for application logic, and the operational gotcha nobody expects.

## A
- **Read-your-writes is gone on the index path**: you write an item and immediately query the index — the item is missing (usually sub-second, but unbounded when the index is throttled or backlogged). Any UI that writes then re-queries by the indexed attribute will look broken.
- **Read-modify-write off the index is unsafe**: the index can return a *stale version* of an item, or an item that no longer matches the predicate. Treat a global index as a **lookup of candidate keys**, then re-read the base row for authoritative values before acting on it.

Operational gotcha: the index has **its own capacity**, and back-pressure flows backwards. In DynamoDB, if a GSI can't absorb the write rate, **writes to the base table are throttled** — an under-provisioned index takes down the table it was meant to accelerate. Also, a deleted/unmatched item requires a *delete* in the index partition, so backlogs surface as ghost entries, not just missing ones.
