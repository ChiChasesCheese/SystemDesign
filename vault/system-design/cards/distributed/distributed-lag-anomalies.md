---
id: distributed-lag-anomalies
node: distributed.replication
type: qa
---
## Q
Name the two classic read anomalies replication lag causes besides missing your own writes, and the guarantee that fixes each.

## A
- **Going backwards in time**: successive reads hit differently-lagged replicas, so data you already saw disappears. Fix: **monotonic reads** — pin a session to one replica (or track a min-version the serving replica must have).
- **Seeing effects before causes**: an answer replicates faster than the question it references. Fix: **consistent prefix / causal reads** — expose writes only in an order that preserves causality (per-partition ordering, causal tokens).

Both are session/ordering guarantees — far cheaper than making all reads linearizable, which is the sledgehammer answer.
