---
id: foundations-latency-vs-throughput
node: foundations.tradeoffs
type: qa
---
## Q
Batching writes raises throughput but hurts which metric, and why? Name the general trade-off.

## A
**Latency vs throughput.** Batching amortizes fixed per-request costs (syscalls, network frames, fsyncs) across many items — throughput up — but each item now waits for its batch to fill or a flush timer, so per-item latency rises.

The lever appears everywhere: Kafka `linger.ms`, group commit in databases, Nagle's algorithm. Choose by whether the path is user-facing (latency wins) or bulk/async (throughput wins).
