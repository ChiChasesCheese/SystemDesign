---
id: foundations-latency-numbers-in-arguments
node: foundations.numbers
type: qa
---
## Q
A p99 budget is 200 ms and each service hop costs ~0.5 ms of same-DC RTT plus its own work. What design smell do the latency numbers expose in a 10-microservice synchronous call chain?

## A
Network RTT itself is cheap (~5 ms for 10 hops) — the real costs are **per-hop p99 amplification** (the slowest of many hops dominates; tail latencies compound) and any hop that touches disk (~10 ms) or crosses a region (~100 ms).

Rule: budget in orders of magnitude — one cross-region call can outweigh dozens of in-DC hops.
