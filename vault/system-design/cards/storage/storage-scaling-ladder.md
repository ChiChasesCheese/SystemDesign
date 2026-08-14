---
id: storage-scaling-ladder
node: storage.relational
type: qa
---
## Q
Your single Postgres is saturating. Give the escalation ladder in order, and the signal that forces each step.

## A
1. **Tune first**: indexes, query plans, caching, connection pooling — most "DB is slow" cases end here.
2. **Bigger box**: vertical scaling is boring and works to surprisingly large sizes (hundreds of GB RAM, NVMe).
3. **Read replicas**: when read QPS dominates and some staleness is tolerable — writes still bottleneck on the primary.
4. **Federation / functional split**: separate DBs per service or domain when unrelated workloads contend.
5. **Sharding**: only when *write* volume or dataset size exceeds one primary — it costs cross-shard queries, transactions, and rebalancing forever.

Interview point: a single well-tuned Postgres is the right answer far longer than candidates assume.
