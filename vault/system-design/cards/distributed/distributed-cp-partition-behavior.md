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
