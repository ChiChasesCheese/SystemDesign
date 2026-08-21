---
id: distributed-local-first-limits
node: distributed.crdt
type: qa
---
## Q
A local-first app (Automerge/Yjs-style) writes to the local replica and syncs in the background. What does the server shrink to, and which requirements force real server-side logic back in?

## A
The server shrinks to a **dumb relay + durable store of encrypted ops/states** — it never resolves conflicts, because CRDT merge runs on every client; clients get zero-latency writes, offline operation, and multi-device sync for free ([[distributed-multi-leader-fit]]: this is multi-leader with merge by construction).

Forced back to a coordinating server (or consensus):

- **Global invariants**: unique usernames, seat sold once, balance ≥ 0 — CRDTs converge but can't enforce "at most one".
- **Authoritative side effects**: payments, emails — must happen exactly once, somewhere.
- **Metadata growth**: tombstones/edit history need compaction, and text CRDTs pay per-character metadata.

Interview line: CRDTs remove coordination from *data merging*, not from *invariants*.

## Q zh
本地优先（local-first）系统的局限是什么？

## A zh
**本地优先**：数据首先写到本地存储，后台同步到云或其他节点。好处是低延迟、离线可用。

**局限**：
1. **协作冲突**：多个用户/设备并发修改同一数据→冲突。需要 CRDT 或 OT 合并。
2. **强一致性**：难以实现——必须等所有节点达成共识才能确认写，这破坏了本地优先的意图。
3. **约束验证**：本地无法验证全局约束（如主键唯一性跨设备），后同步才发现冲突。
4. **大数据**：本地存储有限，无法存储整个数据集。

适用场景：协作编辑（Google Docs 风格）、笔记、待办事项。不适用：金融系统、库存。
