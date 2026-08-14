---
id: distributed-rebalancing
node: distributed.partitioning
type: qa
---
## Q
How do you resplit/rebalance a sharded store without downtime, and what is the classic mistake in choosing partition count?

## A
Live migration recipe: (1) start copying the moving range to the new shard while (2) **dual-writing or streaming changes** (CDC) to keep it in sync, (3) when caught up, flip routing metadata atomically (router/config service), (4) drain and delete the old copy. Reads cut over per-range; writes must never be accepted in two places for the same range.

Classic mistake: `mod N` routing baked into clients, or too few fixed partitions. Standard designs: **many fixed logical partitions** mapped to fewer nodes (move whole partitions, never rehash), or **dynamic range splitting** (HBase/CockroachDB) that splits when a range grows hot or large.
