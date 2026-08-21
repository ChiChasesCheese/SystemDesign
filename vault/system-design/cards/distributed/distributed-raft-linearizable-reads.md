---
id: distributed-raft-linearizable-reads
node: distributed.consensus
type: qa
---
## Q
Why can't a Raft leader serve linearizable reads from its local state without extra work, and what are the two standard fixes?

## A
The leader may be **deposed and not know it** (partitioned away, long GC pause): a new leader is already committing writes elsewhere, so the old one's local read returns stale data as authoritative — a phantom-leader read.

- **Read index**: leader records its current commit index, **confirms leadership with a heartbeat round to a majority**, waits until its state machine has applied up to that index, then serves the read. Linearizable, costs one quorum round-trip per read batch.
- **Lease reads**: after a successful heartbeat, the leader assumes leadership for ~an election timeout and serves reads locally within that window. Nearly free, but safety now depends on **bounded clock drift** across nodes — a fast clock lets a deposed leader serve stale reads.

etcd exposes exactly this choice (linearizable vs serializable reads).

## Q zh
Raft 默认如何处理读取？为什么它可能违反线性一致性？

## A zh
天真的 Raft：领导者直接从状态机读取，不需要日志条目。问题：分割的旧领导者可能错误地认为它是领导者并返回过时的数据。

**线性一致性解决方案**：
- **读索引** — 在读时确认你是当前领导者（从多数获取心跳）。
- **租赁** — 领导者等待确认说没有其他领导者被选出。
- **查询（应用到所有副本）** — 通过日志发送读，确保任何副本看到相同的 happens-before 顺序。

成本：Raft 为强一致读付出复杂性。
