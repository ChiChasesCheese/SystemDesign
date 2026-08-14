---
id: distributed-cap-per-operation
node: distributed.cap
type: qa
---
## Q
Why is "is this system CP or AP?" the wrong granularity — and what is the right one? Give two real examples.

## A
The C/A trade is made **per operation**, not per system — the same store can serve some requests linearizably and others stale.

- **Cassandra/DynamoDB**: consistency level is chosen per read/write (`QUORUM` vs `ONE`; DynamoDB's `ConsistentRead` flag) — one table serves both CP-ish and AP-ish traffic.
- **ZooKeeper**: writes go through consensus, but reads are served **locally by any replica** (possibly stale) unless the client issues `sync` first — so even a "CP" system defaults to non-linearizable reads for speed.

Interview move: instead of labeling the system, state which *operations* need linearizability and pay for only those.
