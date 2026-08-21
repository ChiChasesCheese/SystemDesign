---
id: distributed-rebalancing
node: distributed.partitioning.rebalancing
type: qa
---
## Q
How do you resplit/rebalance a sharded store without downtime, and what is the classic mistake in choosing partition count?

## A
Live migration recipe: (1) start copying the moving range to the new shard while (2) **dual-writing or streaming changes** (CDC) to keep it in sync, (3) when caught up, flip routing metadata atomically (router/config service), (4) drain and delete the old copy. Reads cut over per-range; writes must never be accepted in two places for the same range.

Classic mistake: `mod N` routing baked into clients, or too few fixed partitions. Standard designs: **many fixed logical partitions** mapped to fewer nodes (move whole partitions, never rehash), or **dynamic range splitting** (HBase/CockroachDB) that splits when a range grows hot or large.

## Q zh
什么是分布式系统中的重新平衡？何时触发？

## A zh
**重新平衡**：在节点加入/离开时重新分配分片副本（和数据）。

触发：
- 新节点加入 — 将分片副本分配给它以利用容量。
- 节点离开/失败 — 将其副本移动到健康节点以保持复制因子。
- 不平衡 — 某些节点拥有太多分片/数据；重新分配以平衡。

挑战：重新平衡 I/O 和网络密集；它与 foreground 查询竞争资源。缓解：限流、背压监测、优先考虑重要分片。
