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
