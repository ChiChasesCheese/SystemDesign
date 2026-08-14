---
id: distributed-linearizability-vs-serializability
node: distributed.consistency
type: qa
---
## Q
Linearizability vs serializability — what does each guarantee, over what unit, and what do you call their combination?

## A
- **Linearizability**: a *single-object, real-time* guarantee — every read/write appears to take effect atomically at some instant between its start and end, so a read after a completed write must see it. A recency/ordering contract; no notion of multi-object transactions.
- **Serializability**: a *multi-object transaction isolation* guarantee — the outcome equals **some** serial order of transactions. That order may disagree with real time: a serializable system may legally execute yesterday's-snapshot reads.

Together (transactions serialized in an order consistent with real time) = **strict serializability** — what Spanner provides. Classic trap: "serializable" alone does not imply "you read the latest committed data".
