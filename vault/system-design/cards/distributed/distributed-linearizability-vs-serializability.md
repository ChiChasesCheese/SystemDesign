---
id: distributed-linearizability-vs-serializability
node: distributed.consistency
type: qa
---
## Q
Linearizability vs serializability — what does each guarantee, over what unit, and what do you call their combination?

## A
- **Linearizability**: a *single-object, real-time* guarantee — every read/write appears to take effect atomically at some instant between its start and end, so a read after a completed write must see it. A recency/ordering contract; no notion of multi-object transactions.
- **Serializability**: a *multi-object transaction isolation* guarantee — the outcome equals **some** serial order of transactions. That order may disagree with real time: a serializable system may legally execute yesterday's-snapshot reads.

Together (transactions serialized in an order consistent with real time) = **strict serializability** — what Spanner provides. Classic trap: "serializable" alone does not imply "you read the latest committed data".

## Q zh
线性一致性和可序列化的区别是什么？

## A zh
**线性一致性（Linearizability）**：单对象一致性，保证操作的实时顺序（wall-clock order）。但事务跨对象可能违反因果关系。

**可序列化（Serializability）**：事务一致性，保证并发事务的结果等价于某个串行执行。可以违反实时顺序，但保证逻辑一致性。

**例子**：转账 A→B 100，B→A 50。线性一致但不可序列化：A 先减 100，B 加 100（中间读可能看到转账中状态）。可序列化但不线性一致：根据事务逻辑顺序（可能与实时不同）确定结果。

权衡：线性一致性严格但成本高，可序列化灵活但复杂。
