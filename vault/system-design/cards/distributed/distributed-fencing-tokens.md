---
id: distributed-fencing-tokens
node: distributed.consensus
type: qa
---
## Q
A client holds a distributed-lock lease, pauses for a 20s GC, then resumes and writes — but its lease expired and another client took the lock. How do fencing tokens prevent the corruption, and why can't the client fix this itself?

## A
The lock service issues a **monotonically increasing token** with every lock grant. The *protected resource* (storage) records the highest token it has seen and **rejects writes carrying a lower token** — so the paused client's stale-token write bounces.

The client can't fix it alone: it cannot atomically "check lease still valid, then write" — arbitrary pauses (GC, page fault, network delay) can strike **between** the check and the write. Safety must be enforced at the resource. Corollary: a lock/lease without downstream fencing checks is only advisory, never a safety mechanism.

## Q zh
隔离令牌（fencing token）是什么，怎样防止脑裂？

## A zh
**隔离令牌**：一个单调递增的数字或版本号，新领导者当选时得到递增的令牌。客户端持有令牌，发送请求时带上令牌。

**防止脑裂**：新主库当选时获得令牌 v2，旧主库仍持有 v1。存储层（如锁服务）记录最后接受的最大令牌。旧主库的请求带 v1 会被拒绝（v1 < v2），新主库的请求带 v2 被接受。这样即使旧主库还活着，也无法修改数据或获得锁。

**关键**：存储层必须检验令牌的单调性，不能让更小的令牌改变状态。
