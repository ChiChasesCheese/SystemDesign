---
id: distributed-system-models
node: distributed.time
type: qa
---
## Q
Crash-stop vs crash-recovery vs Byzantine fault models — what does each assume, and which (plus which timing model) do mainstream datacenter systems design for?

## A
- **Crash-stop**: a faulty node halts and never returns — clean but unrealistic.
- **Crash-recovery**: nodes may crash and come back, keeping **stable storage** across the outage but losing memory — what Raft, Kafka, and databases actually assume.
- **Byzantine**: nodes may lie or act arbitrarily (bugs, compromise). Tolerating f liars needs **3f+1** nodes plus signed messages — the cost is why datacenter systems skip it and instead handle *weak* corruption with checksums, TLS, and input validation. BFT lives where participants distrust each other (blockchains, some aerospace).

Timing: **partial synchrony** — the network usually behaves, but delays are occasionally unbounded — which is why timeouts can trigger recovery but must never be the sole proof of death ([[distributed-failure-detection]]).

## Q zh
分布式系统中的主要网络和时间模型是什么？

## A zh
- **同步** — 消息在已知时间内递送，处理在已知时间内完成。不现实但容易分析。
- **部分同步** — 有界延迟，但边界未知；周期性达到同步。现实中很多系统。
- **异步** — 消息可能任意延迟，无关时序假设。最坏情况但最具防卫性。对于安全（不违反正确性）必要。

**故障模型**：
- **崩溃故障** — 节点停止但不发送垃圾。
- **拜占庭** — 节点可能撒谎/任意表现。需要 PBFT。

大多数设计假设异步 + 崩溃故障。
