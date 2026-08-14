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
