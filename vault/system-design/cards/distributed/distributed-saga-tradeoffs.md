---
id: distributed-saga-tradeoffs
node: distributed.transactions.distributed
type: qa
---
## Q
A saga replaces a distributed transaction with local transactions plus compensations. Precisely which ACID property do you lose, and what do you do about it?

## A
You keep **atomicity in the eventual sense** (every step either completes or is compensated) and lose **isolation**: each local step commits immediately, so other transactions can **read intermediate state** — an order that exists while payment is still pending, an inventory reservation that will be released 3 seconds from now. Classic hazards are *dirty reads* of half-done sagas and *lost updates* when another saga writes the same row mid-flight.

Countermeasures (the "semantic lock" toolkit):

- **Semantic lock**: a status flag (`PENDING`) that other workflows must respect; the saga clears it at the end.
- **Commutative updates**: model as `credit/debit` deltas rather than absolute set, so ordering stops mattering.
- **Reread value / version check** before compensating, so you don't undo someone else's newer write.

Also non-negotiable: every step and compensation must be **idempotent and retryable** (they will be re-delivered), and compensation must be *semantically* possible — you can refund a charge, but you cannot un-send an email, so put irreversible steps **last**. If the invariant truly cannot tolerate a visible intermediate state (balance must never go negative), don't use a saga — co-locate the data in one transactional store.

## Q zh
Saga（无协调分布式事务）相对于两阶段提交的权衡是什么？

## A zh
**优势**：
- 无阻塞 — 各个服务立即提交，不等待全局协调。
- 容错 — 一个失败不会锁定所有参与者。
- 灵活 — 支持长期运行的事务。

**缺点**：
- 没有原子性 — 中间状态在某个事务失败时可见。
- 复杂补偿 — 必须写撤销步骤（解除预订）；这些本身可能失败。
- 最终一致 — 不是立即一致。

使用于：跨越多个独立服务的业务工作流，其中短期不一致是可接受的。避免用于需要强原子性保证的操作。
