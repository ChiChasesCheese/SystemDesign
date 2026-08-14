---
id: distributed-quorum-not-linearizable
node: distributed.consistency
type: qa
---
## Q
Dynamo-style store, N=3, W=2, R=2 — strict quorums, no sloppiness. Why are reads still not linearizable?

## A
A write lands on replicas **one at a time**, and reads can interleave with the partial write: reader 1's quorum includes an updated replica and returns the new value; a *later* reader 2's quorum hits two not-yet-updated replicas and returns the **old** value — new-then-old violates linearizability even though both quorums were valid.

To fix it, a reader must **synchronously read-repair** the new value to a write quorum before returning, and writers must read the latest state before writing — expensive, and LWW conflict resolution breaks it anyway. That's why quorum overlap gives you "reads see *acknowledged* writes", not linearizability ([[distributed-quorum-math]]).
