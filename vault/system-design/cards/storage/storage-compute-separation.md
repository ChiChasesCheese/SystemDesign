---
id: storage-compute-separation
node: storage.object
type: qa
---
## Q
Storage–compute separation (Snowflake, BigQuery, modern lakehouses): what does putting the data in object storage buy, and what latency problem does it create?

## A
Buys **independent scaling and elasticity**: spin compute to zero or burst to hundreds of nodes without moving data; multiple engines (SQL, Spark, ML) read the same files; storage is cheap, durable, and effectively infinite.

Creates a latency problem: object-store reads are **tens of ms first-byte over the network** vs local NVMe µs — so every serious engine adds **local SSD/memory caching of hot data** and columnar formats + metadata pruning to read as few bytes as possible. It fits analytics; OLTP still wants storage next to compute.
