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

## Q zh
动态分片分裂和合并是什么时候触发的？

## A zh
**分裂**：当分片大小或请求负载超过阈值（e.g., > 100GB 或 > 10k QPS），分裂成两个较小的分片。新分片从中间的 key 范围切分。

**合并**：当两个相邻分片的总大小或负载都很低（e.g., < 10GB），合并成一个分片。

**触发策略**：定期检查：后台线程周期性扫描分片。监控：监听大小/负载指标，超过阈值自动触发。

**成本**：数据迁移（从旧分片拷贝到新分片）、数据放大、短期不可用。需要平衡分片数量和迁移成本。
