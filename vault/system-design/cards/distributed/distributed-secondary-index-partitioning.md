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
