---
id: distributed-2pc-avoidance
node: distributed.transactions
type: qa
---
## Q
Why is two-phase commit avoided for cross-service transactions at scale, and what do systems do instead?

## A
2PC is a **blocking protocol with a single point of failure**: after voting "prepared", a participant must hold locks and cannot unilaterally commit or abort — if the coordinator dies, participants stay wedged (locks held, rows unavailable) until it recovers. Add: latency of two round-trips to the slowest participant, and every participant must be up (availability = product of all).

Instead: **avoid distributed transactions** — put co-mutating data in one shard/DB; or use **sagas** (local transactions + compensations) and the **outbox pattern** for atomic write-and-publish. Note: *within* one strongly-consistent database (Spanner/Cockroach), 2PC over Paxos/Raft groups is fine — the replicated coordinator removes the blocking failure mode.
