---
id: distributed-avoiding-scatter-gather
node: distributed.partitioning.indexes
type: qa
---
## Q
You need a second access pattern on a sharded table and don't want scatter-gather. What are your options besides a built-in global index, and how do you choose?

## A
- **Query-shaped duplicate table** ("one table per query", Cassandra idiom): write the same fact twice, partitioned differently. You own the fanout on write and the consistency between copies; reads are single-partition and fast. Keep it correct with the **outbox/CDC pipeline**, not dual writes from app code.
- **Async materialized view from the change log**: consume CDC and build the derived table. Same result, one writer, replayable — and the lag is observable as consumer offset lag rather than invisible.
- **Composite key that serves both patterns**: partition by `hash(tenant)`, sort by `(status, created_at)` — a filter that's a prefix of the sort key needs no index at all.
- **Bound the fanout instead of removing it**: partition by a coarse bucket of the query attribute so a query touches 4 shards, not 400.

Choose by read/write ratio and staleness tolerance: read-heavy + tolerant of ~seconds of lag → derived table/view; write-heavy or must-be-consistent → local index and accept scatter-gather, or fix the partition key. Also check the **projection**: an index that doesn't carry the columns you select forces a second round trip to the base partition per matched item, which quietly reinstates the fanout.
