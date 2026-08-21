---
id: distributed-read-repair-anti-entropy
node: distributed.replication.leaderless
type: qa
---
## Q
In leaderless stores, read repair vs anti-entropy — how does each catch replicas up, and why do you need both?

## A
- **Read repair**: on a quorum read, the coordinator compares versions across replicas and writes the newest value back to any stale ones — repairs happen on the read path, so only **frequently-read** keys benefit.
- **Anti-entropy**: a background process diffs whole datasets between replicas (Merkle trees make the comparison cheap) and copies missing writes — covers **cold, never-read** data, but with no ordering and no freshness bound.

You need both because read repair alone leaves rarely-read data stale indefinitely — a *durability* hole: a value existing on only 1 of 3 replicas quietly waits for that replica's disk to die. (Hinted handoff is the third leg: replaying writes parked on stand-in nodes after a fault, see [[distributed-quorum-math]].)

## Q zh
什么是读修复和反熵？它们如何让无主复制最终一致？

## A zh
**读修复**：当读 quorum 的副本有不同版本时，返回最新的并在后台修复过时的副本。快速但不能捕获从不读取的数据的不一致。

**反熵**：后台进程定期比较所有副本（通过 Merkle 树）并修复分歧。缓慢但完整。

两者结合：读修复快速修复热数据，反熵最终修复一切。结果：最终一致 — 所有副本最终收敛到相同状态，但没有强保证在任何时刻的一致性。
