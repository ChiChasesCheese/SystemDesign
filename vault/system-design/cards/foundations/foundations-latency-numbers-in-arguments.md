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


## Q zh
你说"这会很快"。面试官要数字。这个故事的要点是什么？

## A zh
延迟数字让你论证选择。说"缓存很快"不能区分 memcached（~100 µs）vs 本地内存（~100 ns）vs SSD 落回（~100 µs）— 但区别决定了架构。

数字还会揭示假设：说"本地查询很快，所以用多个数据库"，但如果"快"是 50 ms，而 TTL-based 缓存能做 10 ms，你刚刚高估了分布式的收益。

规则：如果你不能为它说出数字或测量，它就不能驱动设计。
