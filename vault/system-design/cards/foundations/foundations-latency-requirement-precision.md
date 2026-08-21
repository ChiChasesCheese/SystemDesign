---
id: foundations-latency-requirement-precision
node: foundations.method
type: qa
---
## Q
"It should be fast" — turn that into an engineering requirement. What elements make a response-time requirement precise enough to design against?

## A
- **Metric**: response time **measured at the client** (includes queueing + network), not server service time.
- **Percentiles**: a median *and* a tail target (e.g. p99) — never the mean, which no actual user experiences.
- **Threshold + window**: "p99 < 1 s over rolling 10-min windows".
- **Load assumption**: the requirement holds *at* a stated load (e.g. 1,000 RPS peak) — latency without load is meaningless.

Sample: "median < 200 ms, p99 < 1 s, client-measured, at peak 1k RPS."


## Q zh
面试官："做这个快一点。"你问什么？

## A zh
**哪个百分位？**"快"对 p50 和 p99 不同。p50 优化廉价；p99 改变架构。

**对谁快？**用户延迟（端到端）vs API 延迟 vs 处理时间 — 它们相差数量级。不同消费者有不同的需求。

**相比什么？**相比现在状态？相比竞争对手？相比用户舒适度？每个推动不同的估算。

**在什么条件下？**p99 @ 平均负载 vs 峰值负载是截然不同的设计。
