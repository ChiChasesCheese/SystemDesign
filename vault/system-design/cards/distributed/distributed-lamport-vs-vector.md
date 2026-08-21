---
id: distributed-lamport-vs-vector
node: distributed.time
type: qa
---
## Q
Lamport timestamps vs vector clocks: what question can a vector clock answer that a Lamport clock cannot, and what does that cost?

## A
**"Were these two events concurrent?"** Lamport clocks (single counter: bump on local event, take max+1 on receive) guarantee only one direction: A happened-before B ⇒ L(A) < L(B). The converse fails — L(A) < L(B) tells you nothing; the events may be concurrent.

Vector clocks (one counter per node) capture causality exactly: A → B iff V(A) ≤ V(B) elementwise; **incomparable vectors = concurrent** — which is what Dynamo-style stores need to detect conflicting siblings instead of silently ordering them.

Cost: O(number of nodes) per timestamp, carried on every message, and pruning entries of departed nodes is awkward. Use Lamport when you just need *some* total order; vectors when you must *detect* conflicts.

## Q zh
Lamport 时钟和向量时钟有什么区别？

## A zh
**Lamport 时钟**：单个整数，每次事件递增 1，接收消息时取 max(本地, 消息)。单调但无法判断因果关系。

**缺点**：两个不同的事件可能有相同的 Lamport 时间戳（无法确定先后）。

**向量时钟**：长度 = 进程数的向量 [a, b, c, ...]，每个进程维护自己的计数。事件 E1 发生在 E2 之前 ⟺ E1 的向量在 E2 的向量中逐元素 ≤ 且至少一个 <。

**优点**：可以判断因果关系和并发事件（向量无偏序关系 = 并发）。

**缺点**：向量大小随进程数增长，数据结构复杂。混合方案如 interval tree clock 减少开销。
