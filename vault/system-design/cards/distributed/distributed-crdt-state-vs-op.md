---
id: distributed-crdt-state-vs-op
node: distributed.crdt
type: qa
---
## Q
State-based vs operation-based CRDTs — what does each ship over the network, and what does each demand from the delivery channel?

## A
- **State-based (CvRDT)**: ship the whole state (or a **delta**) and merge. Demands almost nothing from the network — duplicates, reordering, and lost messages are all fine (idempotent merge + gossip retries) — but full states get big, hence delta-CRDTs.
- **Operation-based (CmRDT)**: ship each operation once; concurrent ops must commute. Cheaper on the wire but demands **reliable, exactly-once, causally ordered delivery** — a duplicated increment double-counts, a remove arriving before its add corrupts state — so you need a causal broadcast layer per replica pair.

Rule of thumb: gossip/edge sync with flaky links → state/delta-based; a sync engine already maintaining ordered per-peer logs (Automerge, Yjs-style) → op-based.
