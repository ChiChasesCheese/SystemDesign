---
id: distributed-cp-partition-behavior
node: distributed.cap
type: qa
---
## Q
A 5-node CP system (e.g. etcd/ZooKeeper) is partitioned 2 | 3. What can each side do, and what would break if the minority side kept serving?

## A
- **Majority side (3)**: elects/keeps a leader and serves both reads and writes — it can still reach quorum.
- **Minority side (2)**: cannot commit writes, and must not serve reads it claims are current; clients there see unavailability.

If the minority also served: **split brain** — two leaders accepting conflicting writes, or the minority returning stale data as authoritative (breaking linearizability). Quorum intersection (any two majorities of 5 share a node) is exactly what prevents two sides from both thinking they're current.

## Q zh
CP 系统在网络分区时如何表现？

## A zh
CP 系统选择**一致性**而非**可用性**。分区发生时：
- 少数派分区：无法获得多数仲裁→拒绝所有请求（返回错误或超时），等待分区愈合。
- 多数派分区：可以继续操作并保持一致。

例子：Consul、Etcd（强一致模式）、Zookeeper。代价是可用性下降：发生分区时，系统部分不可用。
