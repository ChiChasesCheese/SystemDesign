---
id: distributed-read-repair-anti-entropy
node: distributed.replication.leaderless
type: qa
---
## Q
In leaderless stores, read repair vs anti-entropy — how does each catch replicas up, and why do you need both?

## A
- **Read repair**: on a quorum read, the coordinator compares versions across replicas and writes the newest value back to any stale ones — repairs happen on the read path, so only **frequently-read** keys benefit.
- **Anti-entropy**: a background process diffs whole datasets between replicas (Merkle trees make the comparison cheap) and copies missing writes — covers **cold, never-read** data, but with no ordering and no freshness bound.

You need both because read repair alone leaves rarely-read data stale indefinitely — a *durability* hole: a value existing on only 1 of 3 replicas quietly waits for that replica's disk to die. (Hinted handoff is the third leg: replaying writes parked on stand-in nodes after a fault, see [[distributed-quorum-math]].)
