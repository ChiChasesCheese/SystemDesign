---
id: reliability-three-region-quorum
node: reliability.multi-region
type: qa
---
## Q
Why does surviving a full region loss with zero data loss require three regions, not two — and what is the cheap third-region trick?

## A
Synchronous consensus/quorum replication needs a **majority**. With 2 regions, any split or region loss leaves at most half the replicas — no majority, so you either stall (unavailable) or fail over asynchronously (lose data). With replicas spread across **3 regions**, losing any one still leaves 2/3 — writes continue, RPO stays 0.

Cost trick: make the third region a **witness/tiebreaker** — it stores only quorum votes/log metadata, not full data or serving capacity.

Price: every commit waits for the **nearest other region's RTT**, so region choice (two close + one far) sets your write latency floor.
