---
id: storage-secondary-index-partitioning
node: storage.nosql
type: qa
---
## Q
In a partitioned store, secondary indexes can be local (document-partitioned) or global (term-partitioned). What does each cost, and which does DynamoDB's GSI use?

## A
- **Local**: each partition indexes only its own rows. Writes stay single-partition (index updated in the same operation), but a query on the indexed field must **scatter-gather across all partitions** — read latency = slowest partition, and cost grows with partition count.
- **Global**: the index itself is partitioned **by the indexed value**, so a query hits one partition. But one row's write now updates index partitions elsewhere — done **asynchronously**, so the index lags the base table.

DynamoDB GSIs are global: single-partition queries, eventually consistent, with their own provisioned capacity that can throttle base-table writes when hot.
