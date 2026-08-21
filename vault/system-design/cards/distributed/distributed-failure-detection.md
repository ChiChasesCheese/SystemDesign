---
id: distributed-failure-detection
node: distributed.time
type: qa
---
## Q
Why can no timeout prove a remote node is dead, and how do real systems pick and use timeouts anyway?

## A
In an asynchronous network you can't distinguish **crashed** from **slow / partitioned / GC-paused**: no reply within T is consistent with all of them, and the node may resume and keep acting (why fencing exists).

Practice:
- Pick T from **observed latency distributions** (e.g. p999 × margin), not a folklore constant; adaptive detectors like **phi-accrual** (Cassandra/Akka) output a suspicion level from the heartbeat history instead of a binary verdict.
- Make the *reaction* safe rather than the detection perfect: quorum-agreed membership, leases that must expire before takeover, fencing on the resource.

Trade-off to state: short timeout = fast failover but false positives (flapping, duplicate leaders' work); long timeout = slow recovery.

## Q zh
分布式系统中如何检测节点故障？

## A zh
**心跳（heartbeat）**：节点周期性发送 "我还活着" 消息。接收方如果在超时时间内未收到，认定该节点故障。

优点：简单。缺点：无法区分节点故障和网络延迟（可能误杀健康节点）。

**适应式超时（adaptive timeout）**：根据网络延迟历史动态调整超时，减少误报。

**Phi Accrual Failure Detector**：不是二分（活/死），而是计算怀疑度（phi 值），超过阈值才认定故障，增加容错。

**分布式投票**：多个节点投票判断一个节点是否故障，一票否决（多数派同意才宣布故障）。
