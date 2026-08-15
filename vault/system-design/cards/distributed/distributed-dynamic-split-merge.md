---
id: distributed-dynamic-split-merge
node: distributed.partitioning.rebalancing
type: qa
---
## Q
How does dynamic (split/merge) partitioning work, what triggers each operation, and what's the pitfall on an empty database?

## A
Ranges are split when a partition exceeds a size or load threshold — HBase regions (~10 GB), CockroachDB ranges (~512 MiB), DynamoDB partitions (10 GB or when throughput demands it). The split is a **metadata operation first**: the range is cut at a chosen mid-key into two ranges owned by the same node, and only then may one half be *moved* to another node. Merges run the other way when adjacent ranges shrink (after mass deletes), to stop metadata from fragmenting.

Pitfall: a **fresh database starts as one partition on one node** — all writes hit a single machine until the first split completes, so a load test or a bulk load looks catastrophically slow. Fix: **pre-split** at creation using known key boundaries (HBase pre-splitting, Cockroach split points, DynamoDB's older parallel-load guidance). Advantage over fixed counts: the partition count tracks data volume automatically, so it works from 1 GB to 100 TB.
