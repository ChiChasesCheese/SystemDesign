---
id: distributed-multi-leader-topologies
node: distributed.replication.multi-leader
type: qa
---
## Q
Circular, star, and all-to-all multi-leader topologies — what does each risk, and what extra metadata does every one of them need?

## A
- **Circular / star**: each write forwards along a fixed path. One node down **breaks the chain** until reconfigured, and every write pays multiple hops. MySQL's classic ring replication is this.
- **All-to-all**: every leader ships to every other. No single-node chokepoint, but messages can **overtake each other** — an `UPDATE` can arrive at a leader before the `INSERT` it depends on, and naive timestamps won't order them.

All topologies need a **replication path tag** on each write (list of node ids it has passed through) so a leader drops writes it has already applied and the write stops circulating. All-to-all additionally needs **causal ordering** — version vectors, not wall clocks — which is exactly the bug most hand-rolled multi-master setups ship with.

## Q zh
多主复制的三种拓扑是什么？每种的优缺点？

## A zh
- **星形** — 一个主充当枢纽，中转其他主的更新。简单但枢纽是单点故障。
- **环形** — 每个主转发给下一个；转发失败可能阻断链。
- **全连接** — 每个主向所有其他主发送更新。最灵活但消息数 O(n²)；需要版本向量或时间戳来检测重复。

实际上：大多数系统默认全连接（更简单）或星形（降低复杂性）。
