---
id: distributed-read-your-writes
node: distributed.consistency
type: qa
---
## Q
A user saves their profile, refreshes, and sees the old version (read hit a lagging replica). Name the missing guarantee and three ways to provide it without making all reads strong.

## A
**Read-your-writes (read-after-write) consistency** — a session-level guarantee, weaker than linearizability.

- **Route the writer's reads to the leader** for data they may have modified (or for N seconds after their last write).
- **Session token / monotonic timestamp**: client carries the LSN/version of its last write; a replica serves the read only if it has caught up to it (else wait or forward).
- **Client-side echo**: update local/app cache with the written value and serve the user's own view from it.

Scope it to the session — other users seeing the update a second late is usually fine.

## Q zh
什么是 read-your-writes 一致性？为什么分布式系统需要它？

## A zh
**Read-your-writes**：事务中的读看到同一事务中的写入。例如，提交后，后续查询看到更改。

为什么需要：用户期望他们的操作立即可见。如果您更新个人资料照片，刷新后应该看到新照片，而不是旧的。

分布式中的挑战：副本可能不同步。如果写入打到一个副本，读从另一个落后副本读取，它不会看到更改。解决：版本向量（客户端追踪最新看到的版本），混合逻辑时钟，或路由读到包含写的副本。
