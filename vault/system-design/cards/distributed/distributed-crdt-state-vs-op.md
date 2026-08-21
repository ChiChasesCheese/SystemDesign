---
id: distributed-crdt-state-vs-op
node: distributed.crdt
type: qa
---
## Q
State-based vs operation-based CRDTs — what does each ship over the network, and what does each demand from the delivery channel?

## A
- **State-based (CvRDT)**: ship the whole state (or a **delta**) and merge. Demands almost nothing from the network — duplicates, reordering, and lost messages are all fine (idempotent merge + gossip retries) — but full states get big, hence delta-CRDTs.
- **Operation-based (CmRDT)**: ship each operation once; concurrent ops must commute. Cheaper on the wire but demands **reliable, exactly-once, causally ordered delivery** — a duplicated increment double-counts, a remove arriving before its add corrupts state — so you need a causal broadcast layer per replica pair.

Rule of thumb: gossip/edge sync with flaky links → state/delta-based; a sync engine already maintaining ordered per-peer logs (Automerge, Yjs-style) → op-based.

## Q zh
状态型 CRDT 和操作型 CRDT 有什么区别？

## A zh
**状态型（State-based）**：副本定期或按需交换完整状态，接收方合并状态后同步最新值。带宽高（要传状态），但简单。

**操作型（Operation-based）**：副本只广播操作（"递增 by 1"、"删除元素 x"），接收方在本地重放。带宽低（操作小），但要保证因果序列和幂等性。

权衡：state-based 简单但重，operation-based 轻量但复杂。
