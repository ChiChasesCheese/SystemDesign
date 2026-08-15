---
id: distributed-multi-leader-topologies
node: distributed.replication.multi-leader
type: qa
---
## Q
Circular, star, and all-to-all multi-leader topologies — what does each risk, and what extra metadata does every one of them need?

## A
- **Circular / star**: each write forwards along a fixed path. One node down **breaks the chain** until reconfigured, and every write pays multiple hops. MySQL's classic ring replication is this.
- **All-to-all**: every leader ships to every other. No single-node chokepoint, but messages can **overtake each other** — an `UPDATE` can arrive at a leader before the `INSERT` it depends on, and naive timestamps won't order them.

All topologies need a **replication path tag** on each write (list of node ids it has passed through) so a leader drops writes it has already applied and the write stops circulating. All-to-all additionally needs **causal ordering** — version vectors, not wall clocks — which is exactly the bug most hand-rolled multi-master setups ship with.
