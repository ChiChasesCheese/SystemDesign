---
id: foundations-performance-vs-scalability
node: foundations.tradeoffs
type: qa
---
## Q
"The service is slow" — how do you tell a performance problem from a scalability problem, and why does the distinction matter?

## A
- **Performance problem**: slow for a *single* user even at low load — fix the code path (algorithms, queries, I/O).
- **Scalability problem**: fast when idle, degrades as *load grows* — fix the architecture (add nodes, remove shared bottlenecks, partition).

Matters because the fixes are disjoint: optimizing code won't save a system whose bottleneck is one shared database, and adding servers won't fix an O(n²) endpoint.


## Q zh
性能 vs 可扩展性：定义差异。

## A zh
- **性能**：系统在给定的工作下有多快。例如 p99 延迟 = 50 ms。
- **可扩展性**：当工作增加时，系统如何响应。例如：当 DAU 从 1M 翻倍到 2M 时会发生什么？

一个"快速"（性能）的系统可能在增加负载时无法扩展。一个"可扩展"的系统应该保持延迟稳定或可预测地降低。

关键：设计不是"我们会很快"，而是"我们以 N 倍的成本扩展到 kN 的负载。"
