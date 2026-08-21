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

## Q zh
什么时候 scatter-gather 是不可避免的？怎样避免它？

## A zh
当查询必须触及多个分片且无法路由到单个分片时，scatter-gather 是不可避免的（e.g., 聚合、全局排序、跨分片的范围查询）。

**避免方式**：
- **重新分片**：将频繁一起查询的数据放在同一分片（e.g., 按用户ID分片，查询该用户的所有订单）。
- **denormalize**：复制必要的数据到多个分片，这样每个分片可以独立处理查询（增加存储和写放大）。
- **分层索引**：用全局索引或 search cluster（Elasticsearch）来快速定位行，再精确取值。
- **接受 scatter-gather**：对于不频繁的重查询，直接 scatter-gather 可能比维护复杂分片策略更简单。
