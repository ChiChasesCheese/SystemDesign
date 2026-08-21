---
id: distributed-causal-vs-eventual
node: distributed.consistency
type: qa
---
## Q
Under plain eventual consistency, a user sees the reply "No it isn't" before the question it answers. What guarantee prevents this, and what does it deliberately not order?

## A
**Causal consistency**: if write B was made after seeing write A (same session, or read-then-write), every node must apply/expose A before B. Implemented with version vectors or by tracking each write's causal dependencies and delaying delivery until they're satisfied.

It deliberately does **not** order concurrent writes — updates with no causal path between them may be seen in different orders by different nodes. That's why it's cheaper than linearizability: it's the strongest model that stays available during partitions.

## Q zh
因果一致性和最终一致性有什么区别？

## A zh
**因果一致性**：保证因果关系中的操作被正确有序地观察。如果 A 的写依赖于 B 的写，那么所有客户端都会看到 B 的写先于 A 的写（使用 version vector 或 timestamp）。

**最终一致性**：没有顺序保证，只保证最终所有副本收敛到同一状态。中间过程可能出现任意顺序的视图。

因果一致性强于最终一致性，弱于强一致性。
