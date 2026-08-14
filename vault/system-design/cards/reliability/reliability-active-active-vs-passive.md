---
id: reliability-active-active-vs-passive
node: reliability.multi-region
type: qa
---
## Q
When is active-passive the right multi-region design over active-active, given that active-active looks strictly better on paper?

## A
Choose **active-passive** when writes must stay strongly consistent and single-homed: one region owns all writes, so there are no cross-region write conflicts and no conflict-resolution logic — at the cost of higher write latency for far users and a real failover event.

**Active-active** serves writes in every region (great latency, region loss is a non-event) but forces you to handle **concurrent conflicting writes** — CRDTs, last-writer-wins, or partitioning users to a home region. If your domain can't tolerate merge semantics (payments, inventory), active-active on the write path is the wrong call.
