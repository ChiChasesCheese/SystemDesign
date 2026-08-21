---
id: distributed-crdt-convergence
node: distributed.crdt
type: qa
---
## Q
What algebraic properties must a CRDT's merge function have, and what operational freedoms do those properties buy?

## A
Merge must be **commutative** (order doesn't matter), **associative** (grouping doesn't matter), and **idempotent** (merging the same state twice is harmless) — formally, states form a join-semilattice and merge is the least-upper-bound.

That buys: replicas can accept writes **independently with no coordination**, sync **in any order, over any topology, with duplicated or re-sent messages**, and still provably converge to the same state once they've seen the same updates. Conflicts are resolved *by construction* rather than detected and escalated.

The catch: convergence ≠ correctness — the merged result is whatever the type's semantics say (e.g. add-wins), which may not be what the business rule wanted.

## Q zh
CRDT 是如何保证所有副本最终收敛的？

## A zh
**交换律、结合律、幂等性**：CRDT 操作满足交换律（顺序无关）和结合律（分组无关），任何两个副本只要应用了相同的操作集合（不论顺序），最终状态就相同。

**因果序列**：用版本向量或操作日志跟踪因果依赖，确保不重复应用操作。

**最终对账**：通过反熵（全量交换）或 merkle tree，定期校验并补齐缺失的操作。

关键：设计 CRDT 时操作必须天然具有幂等性和交换性。
