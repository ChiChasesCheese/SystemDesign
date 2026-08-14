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
