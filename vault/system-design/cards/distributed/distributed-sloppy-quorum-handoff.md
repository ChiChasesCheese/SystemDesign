---
id: distributed-sloppy-quorum-handoff
node: distributed.replication.leaderless
type: qa
---
## Q
Trace a write under a sloppy quorum with hinted handoff: where does it land, when does it get home, and what are the two ways it never gets there?

## A
The key's N home replicas are decided by the ring. If some are unreachable, the coordinator writes to the **first N reachable nodes instead**, and a stand-in stores the value in a separate **hint** — a durable record tagged "this belongs to node 7". When node 7 is seen alive again (gossip), the stand-in **replays the hints to it** and deletes them.

It never gets home when:

- **The hint window expires** — hints are only retained for a bounded time (Cassandra's `max_hint_window`, hours by default); after that they are dropped and only anti-entropy repair can fix the replica.
- **The stand-in dies** before replaying, taking the only copy of the hint with it.

Hence the guarantee downgrade: a sloppy write is a **durability/availability boost, not a quorum** — the R read replicas need not intersect the nodes that actually took the write, so `W + R > N` no longer implies you read it back.

## Q zh
什么是 sloppy quorum？它如何在节点故障下保持可用性？

## A zh
传统 quorum：写必须达到 N 个副本中的 W 个，这些是**首选的**副本。如果 W 个首选副本不可用，写失败。

**Sloppy quorum**（提示移交）：如果首选副本不可用，写入**任何** W 个可用节点，包括临时节点。临时节点标记写入为"为节点 X"。当节点 X 恢复时，临时节点将数据移交回去。

好处：在节点失败中写可用性。缺点：持久性降低（临时节点本身可能失败，数据丢失）。权衡：可用性 vs 持久性。
