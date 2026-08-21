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

## Q zh
为什么 quorum 读写不保证线性一致性？

## A zh
Quorum 保证 read-your-writes 和单调读，但不保证全局同步。问题：
- 两个并发写可以在不同的 quorum 中完成（都达到 W + R > N 但在不同时间）。
- 一个慢的读可能先返回旧值。

例如：W + R > N，但读 quorum 遗漏最新写的所有副本直到稍后才同步。写入被承认但读看不到。对于线性一致性，需要同步确认最新或使用 Raft/Paxos。
