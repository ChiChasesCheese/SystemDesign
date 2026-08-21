---
id: distributed-secondary-index-partitioning
node: distributed.partitioning.indexes
type: qa
---
## Q
Local (document-partitioned) vs global (term-partitioned) secondary indexes on a sharded store — who pays, the writer or the reader?

## A
- **Local index**: each partition indexes only its own rows. Writes touch one partition (cheap, transactional with the row), but a query on the indexed field must **scatter-gather across every partition** — tail latency is the max over all shards.
- **Global index**: the index itself is partitioned by the indexed value (term), so a query hits one index partition. But one row update may touch **several index partitions**, so updates are typically **asynchronous** — the index lags the base data (DynamoDB GSIs work exactly like this, with their own provisioned throughput and eventual consistency).

Rule: write-heavy with occasional filtered reads → local; read-heavy queries on the secondary key → global, and accept the lag.

## Q zh
二级索引如何在分布式系统中分区？权衡是什么？

## A zh
给定表在主键上分片，如何在辅助属性（如用户名）上进行查询？

**全局二级索引** — 索引本身也按索引键分片。查询快速（直接去索引分片）。但更新分布式且缓慢（主分片 → 索引分片）。

**本地二级索引** — 每个分片维护其自己的数据的索引。写入本地且快速。但查询需要 scatter-gather 所有分片。

权衡：write-local-read-global（全局索引）vs read-local-write-global（本地索引）。选择取决于工作负载。
