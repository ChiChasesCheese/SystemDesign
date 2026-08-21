---
id: distributed-raft-guarantees
node: distributed.consensus
type: qa
---
## Q
What does Raft actually guarantee about leaders and logs, and what mechanism enforces each guarantee?

## A
- **Election safety**: ≤1 leader per term — each node votes once per term, and a candidate needs a **majority**; two majorities always intersect.
- **Leader completeness**: an elected leader already holds every committed entry — voters **refuse candidates whose log is less up-to-date** than theirs (compare last term, then length), so a majority-committed entry exists on at least one voter of any winning majority.
- **Log matching / state machine safety**: if two logs agree on an entry's index+term, they agree on everything before it (AppendEntries consistency check), so all nodes apply the same commands in the same order.

Consequence worth stating: entries flow only leader → follower; a new leader never overwrites committed entries, only uncommitted divergence.

## Q zh
Raft 保证什么？为什么它在实践中有效？

## A zh
**Raft 保证**：
1. 选举安全 — 任何任期最多一个领导者。
2. 领导者追加-只 — 领导者只追加日志，从不覆盖/删除。
3. 日志匹配 — 如果两个日志在相同索引和任期有条目，它们在该点之前相同。
4. 领导者完整性 — 新领导者拥有所有已提交的条目。
5. 状态机安全 — 如果日志条目被应用到一个服务器，没有其他服务器会在相同索引应用不同条目。

这使得 Raft 对于可靠地复制有限状态机很有效。
