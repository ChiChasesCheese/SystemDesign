---
id: distributed-linearizability-when-needed
node: distributed.consistency
type: qa
---
## Q
Which concrete features genuinely require linearizability (not just causal or session guarantees), and why?

## A
Anything where **two nodes agreeing on one current value** is the point:

- **Locks and leader election**: all nodes must agree who holds the lock — a stale view means two leaders.
- **Uniqueness constraints**: usernames, one-seat-one-buyer, balance-can't-go-negative — concurrent claims must serialize on a single answer (this is a compare-and-set).
- **Cross-channel dependencies**: service A writes storage then sends a message via a queue; the consumer's read must see the write, or it processes stale data — the side channel outruns replication.

Everything else (feeds, profiles, counters) usually needs only session/causal guarantees, which don't require coordination.

## Q zh
什么时候必须要线性一致性？

## A zh
**需要**：
- **互斥锁**：必须确保只有一个持有人。
- **金融转账**：必须确保钱不会凭空出现或消失。
- **主键约束**：数据库必须拒绝重复的主键。
- **基于当前值的原子更新**（如 CAS）。

**不需要**：
- **最终一致存储**（缓存、文档数据库）。
- **只读查询**。
- **日志系统**（log append-only，通常用时间戳而非线性一致）。

权衡：评估业务是否真的需要线性一致（成本高），很多系统用最终一致已足够。
