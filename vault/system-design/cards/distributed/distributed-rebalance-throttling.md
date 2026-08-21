---
id: distributed-rebalance-throttling
node: distributed.partitioning.rebalancing
type: qa
---
## Q
Why is fully automatic, unthrottled rebalancing a well-known way to turn a small failure into an outage — and what are the standard guards?

## A
Rebalancing consumes exactly the resources you are short of: disk IO, network, and page cache, **at the moment the cluster is already degraded**. The cascade: a node is falsely declared dead (GC pause, slow disk) → the cluster starts re-replicating its data → the extra load slows *other* nodes past the failure detector's threshold → they're declared dead too → more rebalancing. This death spiral has taken down real clusters that never lost a machine.

Guards:

- **Rate limits**: cap stream throughput and concurrent recoveries (Cassandra `stream_throughput_outbound`, Elasticsearch `cluster.routing.allocation.node_concurrent_recoveries` and the recovery byte budget).
- **Delay before acting**: don't move data until the node has been gone for N minutes (Elasticsearch `index.unassigned.node_left.delayed_timeout`, default 1m) — most node absences are restarts.
- **Human in the loop**: automatic *proposal*, operator-approved *execution*, for the largest moves.

## Q zh
分布式系统在重新平衡分片时如何避免响应时间峰值？

## A zh
重新平衡（移动分片副本）竞争 I/O 和网络带宽，拖累查询。缓解：
- **限流** — 限制同时传输的字节数或分片数。
- **背压** — 监测延迟；如果延迟上升，减速。
- **优先队列** — 优先考虑热分片或关键分片。
- **离峰** — 在低流量窗口重新平衡。

权衡：更快的重新平衡（如果节点死了）vs 更低的峰值延迟。实践中：关键的分片限流避免用户可感知的脉冲。
