---
id: distributed-causal-vs-eventual
node: distributed.consistency
type: qa
---
## Q
Under plain eventual consistency, a user sees the reply "No it isn't" before the question it answers. What guarantee prevents this, and what does it deliberately not order?

## A
**Causal consistency**: if write B was made after seeing write A (same session, or read-then-write), every node must apply/expose A before B. Implemented with version vectors or by tracking each write's causal dependencies and delaying delivery until they're satisfied.

It deliberately does **not** order concurrent writes — updates with no causal path between them may be seen in different orders by different nodes. That's why it's cheaper than linearizability: it's the strongest model that stays available during partitions.
