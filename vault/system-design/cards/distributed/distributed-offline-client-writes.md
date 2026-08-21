---
id: distributed-offline-client-writes
node: distributed.replication.multi-leader
type: qa
---
## Q
Why is an offline-capable mobile/desktop app a multi-leader system, and which two schema decisions does that force on you?

## A
Every device has a full local replica that **accepts writes while disconnected** and syncs later — that is exactly multi-leader, with the peculiar property that **replication lag is unbounded** (days, if the phone is in a drawer) and the "leader count" equals the user's device count.

Forced decisions:

- **Client-generated ids** (UUID/ULID, or `(device_id, local_seq)`) — server auto-increment ids can't be assigned offline, and two devices would mint the same one.
- **Mutations as intents, not absolute state** — store `add 2 to quantity` or a CRDT/OT operation rather than `quantity = 5`, so two devices' offline edits both survive the merge.

What stays impossible: **global invariants** (uniqueness, non-negative balance) cannot be checked offline, so those operations must be *provisional locally and confirmed by the server*, with a visible rollback path in the UI.

## Q zh
离线客户端如何处理写入而无需等待网络往返？后来的冲突如何解决？

## A zh
客户端在本地乐观应用写入（日历事件、笔记）到其本地副本。当在线时，与服务器同步：
- 如果没有冲突（版本向量或时间戳显示两个写都在同一条链），合并自动。
- 如果冲突（并发写），使用 CRDT、LWW 或应用逻辑（undo/redo、显示差异让用户选择）。

关键：客户端是**主数据源**对于本地更改，直到同步；服务器必须接受客户端版本或表达冲突。
