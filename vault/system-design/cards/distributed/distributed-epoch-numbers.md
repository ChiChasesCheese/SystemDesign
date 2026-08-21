---
id: distributed-epoch-numbers
node: distributed.consensus
type: qa
---
## Q
Every consensus protocol carries an epoch number (term/ballot/view) and runs two quorum checks. What problem do epochs solve, and how do the two quorums interact?

## A
Epochs solve "**which of two would-be leaders is current**" without relying on clocks: within one epoch there is at most one leader, and a **higher epoch always defeats a lower one**.

- **Quorum 1 — election**: a candidate collects majority votes for its epoch.
- **Quorum 2 — commit**: the leader gets majority acknowledgment for each value it proposes.

The safety trick is that the two quorums **must intersect**: if a new leader was elected, every commit quorum of the old leader contains at least one node that has seen the higher epoch and therefore **rejects the old leader's proposals**. So a deposed leader can't commit anything behind the new leader's back — the generic mechanism behind Raft terms, Paxos ballots, and Viewstamped Replication views ([[distributed-raft-guarantees]] is the Raft instantiation).

## Q zh
纪元号（epoch number）在分布式系统中的作用是什么？

## A zh
**作用**：标记系统状态的一个版本，用于检测过期的消息、检测新旧领导者的冲突。

**例子**：Raft 中的 term：每次选举产生新 term，新领导者会拒绝或覆盖旧 term 的消息。Dynamo 中的版本向量：包含纪元号和逻辑时钟，用于检测并发写。

**防止的问题**：旧领导者在网络恢复后继续发送消息→用 term 检测并丢弃。客户端从过期副本读到旧数据→检测 epoch 确认最新。

本质是用单调递增的数字将系统演化分阶段，阶段内操作有序，阶段间可以清晰界分。
