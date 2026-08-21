---
id: distributed-sync-vs-async-replication
node: distributed.replication.leader
type: qa
---
## Q
Leader-follower: synchronous vs asynchronous replication — what does each risk, and what's the standard compromise?

## A
- **Async**: leader acks before followers confirm. Risk: leader dies → **acknowledged writes are lost** on failover (the new leader never received them). Fast, and lag is unbounded under load.
- **Sync**: leader waits for follower confirmation. Zero-loss failover to that follower, but one slow/dead follower **stalls all writes**.

Compromise: **semi-synchronous** — exactly one (any one) follower must confirm, rest async; or quorum-ack (e.g. Kafka `acks=all` with `min.insync.replicas=2`). Interview framing: this is your RPO decision — async RPO > 0, sync/semi-sync RPO = 0.

## Q zh
同步和异步复制有什么区别？各自的权衡是什么？

## A zh
**同步复制**：主等待至少一个副本确认写入后才向客户端返回。
- 优点：耐久性 — 如果主故障，副本有数据。
- 缺点：延迟 — 缓慢（等待网络往返）。如果副本缓慢/离线，主被阻塞。

**异步复制**：主立即向客户端返回，副本在后台追赶。
- 优点：延迟 — 快速（无等待）。
- 缺点：丢失风险 — 如果主故障但副本还没追上，数据丢失。

现代折衷：半同步 — 主等待副本 *开始* 处理（不一定完成）。
