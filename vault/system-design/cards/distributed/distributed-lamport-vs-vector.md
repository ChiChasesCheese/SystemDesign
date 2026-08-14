---
id: distributed-lamport-vs-vector
node: distributed.time
type: qa
---
## Q
Lamport timestamps vs vector clocks: what question can a vector clock answer that a Lamport clock cannot, and what does that cost?

## A
**"Were these two events concurrent?"** Lamport clocks (single counter: bump on local event, take max+1 on receive) guarantee only one direction: A happened-before B ⇒ L(A) < L(B). The converse fails — L(A) < L(B) tells you nothing; the events may be concurrent.

Vector clocks (one counter per node) capture causality exactly: A → B iff V(A) ≤ V(B) elementwise; **incomparable vectors = concurrent** — which is what Dynamo-style stores need to detect conflicting siblings instead of silently ordering them.

Cost: O(number of nodes) per timestamp, carried on every message, and pruning entries of departed nodes is awkward. Use Lamport when you just need *some* total order; vectors when you must *detect* conflicts.
