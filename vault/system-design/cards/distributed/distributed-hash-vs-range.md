---
id: distributed-hash-vs-range
node: distributed.partitioning.schemes
type: qa
---
## Q
Hash partitioning vs range partitioning: what does each optimize, and what workload wrecks each?

## A
- **Hash**: uniform key spread → even load, no planning. Wrecked by **range queries** — "last hour of events" scatters across every shard (scatter-gather).
- **Range**: adjacent keys co-located → efficient range scans, and shards can split where data actually is. Wrecked by **monotonically increasing keys** (timestamps, sequential IDs) — all inserts hammer the last shard (hot tail).

Standard hybrid: **hash a prefix, range the rest** — e.g. partition by `hash(user_id)`, sort by `timestamp` within the partition (DynamoDB's PK/SK, Cassandra's partition + clustering keys): even spread across users, cheap time-range scans per user.
