---
id: traffic-lb-algorithm-choice
node: traffic.load-balancing
type: qa
---
## Q
Round robin vs least-connections vs consistent hashing — match each to the workload it exists for.

## A
- **Round robin** (weighted): requests are cheap and uniform, backends identical — the simple default.
- **Least connections** (or least outstanding requests): request costs **vary widely** — stops slow requests piling onto one backend; the usual production default.
- **Consistent hashing** (on user/session/key): the backend holds **per-key state** — local cache, WebSocket sessions — so the same key must land on the same node, with minimal reshuffling when nodes change.

## Q zh
轮询 vs 最少连接 vs 一致哈希 — 将每个匹配到它存在的工作负载。

## A zh
- **轮询**（加权）：请求很廉价且统一，后端相同 — 简单的默认。
- **最少连接**（或最少未完成请求）：请求成本**变化很大** — 停止缓慢请求堆积到一个后端；通常生产默认。
- **一致哈希**（在用户/会话/键上）：后端持有**每键状态** — 本地缓存、WebSocket 会话 — 所以相同的键必须着陆在相同的节点，当节点改变时最小重新洗牌。

轮询 vs 最少连接 vs 一致哈希 — 将每个与其存在的工作负载匹配。

- **轮询**（加权）：请求便宜且统一，后端相同 — 简单的默认值。
- **最少连接**（或最少未完成请求）：请求成本**差异很大** — 阻止缓慢请求堆积在一个后端；通常的生产默认值。
- **一致哈希**（在用户/会话/key）：后端持有**每 key 状态** — 本地缓存、WebSocket 会话 — 所以相同的 key 必须落在同一节点，节点变化时重新洗牌最少。
