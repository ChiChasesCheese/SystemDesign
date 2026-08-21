---
id: distributed-tenant-isolation-limits
node: distributed.partitioning.skew
type: qa
---
## Q
One tenant's runaway job saturates a shared shard and everyone on it gets timeouts. Which mechanisms contain the blast radius, and what does each actually bound?

## A
- **Per-key / per-tenant rate limits** (token bucket at the routing tier, keyed by tenant): bounds the *offender's* request rate, so the shard never saturates. Cheapest and first to reach for; needs a distributed counter (Redis or approximate local buckets with a global reconciliation).
- **Fair queueing / weighted admission** at the shard: bounds *share* rather than rate — under overload each tenant gets a slice instead of first-come-first-served, so a burst delays only its own owner.
- **Shuffle sharding**: assign each tenant a random *subset* of k nodes out of n. With n=8, k=2 there are 28 distinct pairs, so one abusive tenant fully overlaps with only ~1/28 of the others — the blast radius shrinks combinatorially without dedicated hardware per tenant.
- **Dedicated partitions** for the largest tenants: bounds everything, at the cost of capacity planning per tenant.

Escalation order: limit → fair-queue → shuffle-shard → isolate. Note limits must return a clean `429` with a retry hint, or clients turn the limit into a retry storm.

## Q zh
多租户系统如何强制租户隔离和资源限制？

## A zh
- **数据隔离** — 每个租户的行由租户 ID 分区；查询检查权限。
- **连接限制** — 每个租户最多 N 个并发连接。
- **速率限制** — 最多 M 个请求/秒。
- **配额** — 最多存储 X 字节，最多 Y 行。
- **优先队列** — 低优先租户在繁忙时有不同的 QoS。

挑战：防止噪音邻居（一个租户的爆炸拖累其他人）。实现：线程池按租户、CPU 评估、I/O 权重。金融系统中严格；SaaS 中常见但有限。
