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

## Q zh
全局二级索引的陈旧性问题是什么？怎样解决？

## A zh
**问题**：主表数据写入分片 A，二级索引在分片 B。数据到索引的更新是异步的（消息队列或后台进程）。查询时，索引可能还没更新→返回旧结果或遗漏新数据。

**解决方案**：
1. **强一致索引**：使用分布式事务（2PC 或 saga）确保表和索引同时更新。成本高。
2. **异步索引 + 版本检查**：索引记录版本号，查询时检查主表版本确认是否陈旧。
3. **异步索引 + 后台修复**：定期全量扫描主表重建索引。
4. **接受陈旧**：文档、缓存等场景接受最终一致。

权衡：一致性 vs 性能。
