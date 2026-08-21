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

## Q zh
哈希分片和范围分片各有什么优缺点？

## A zh
**哈希分片**（hash(key) % n）：优点：分布均匀（热 key 分散）。缺点：范围查询无法批量定位（"age > 20" 要扫所有分片），range scan 变成 scatter-gather。

**范围分片**（key 范围如 A-M 在分片 1，N-Z 在分片 2）：优点：范围查询只需访问几个分片，顺序扫描高效。缺点：容易出现热 key（某个范围有大量写入）。

权衡：有大量范围查询选范围分片（付出热 key 代价），有热 key 写入选哈希分片（付出 scatter-gather 代价）。也可以混合或二级索引。
