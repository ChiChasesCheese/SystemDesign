---
id: distributed-scatter-gather-fanout-math
node: distributed.partitioning.indexes
type: qa
---
## Q
A scatter-gather query fans out to 100 shards, each with a p99 of 10 ms. What is the query's latency distribution, and what do you do about it?

## A
The query finishes when the **slowest** shard replies, so you need *all* 100 under 10 ms: `0.99^100 ≈ 0.37`. About **63% of queries exceed 10 ms** — the per-shard p99 has become roughly the query's *median*. Generalize: fanout S turns the per-shard p(1−q) into a query-level exceedance of `1 − (1−q)^S`, so tail latency is amplified, not averaged.

Levers, in order of effectiveness:

- **Reduce S** — route on a key so the query hits 1 shard (the real fix; a global index or a query-shaped denormalized table).
- **Hedged/backup requests**: re-issue to a replica after the 95th percentile delay; costs a few % extra load and cuts the tail dramatically (Google's tail-at-scale result).
- **Partial results with a deadline**: return the shards that answered, flag incompleteness — acceptable for search/analytics, not for billing.

## Q zh
Scatter-gather 和 fanout 在分布式系统中如何工作？延迟是什么样的？

## A zh
**Scatter-gather** — 客户端向所有 N 个分片发送查询（scatter），等待所有响应（gather）。延迟 = max(分片延迟)。

如果分片延迟是 p50=10ms, p99=100ms，聚合 p50 ≈ 10ms（快），但 p99 ≈ 100ms（由慢分片主导）。

缓解：
- **超时** — 返回部分结果。
- **副本** — 查询副本，使用先返回的。
- **分片排序** — 优先查询快的分片。

**Fanout** — 单个查询分散到多个路径（如 MapReduce）。尾部延迟变成系统的敌人。
