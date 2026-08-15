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
