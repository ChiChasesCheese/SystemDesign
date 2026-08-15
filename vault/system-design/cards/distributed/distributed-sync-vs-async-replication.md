---
id: distributed-sync-vs-async-replication
node: distributed.replication.leader
type: qa
---
## Q
Leader-follower: synchronous vs asynchronous replication — what does each risk, and what's the standard compromise?

## A
- **Async**: leader acks before followers confirm. Risk: leader dies → **acknowledged writes are lost** on failover (the new leader never received them). Fast, and lag is unbounded under load.
- **Sync**: leader waits for follower confirmation. Zero-loss failover to that follower, but one slow/dead follower **stalls all writes**.

Compromise: **semi-synchronous** — exactly one (any one) follower must confirm, rest async; or quorum-ack (e.g. Kafka `acks=all` with `min.insync.replicas=2`). Interview framing: this is your RPO decision — async RPO > 0, sync/semi-sync RPO = 0.
