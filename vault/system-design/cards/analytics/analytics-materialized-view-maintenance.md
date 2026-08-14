---
id: analytics-materialized-view-maintenance
node: analytics.derived
type: qa
---
## Q
A materialized view is stale the moment its base table changes. Compare the two maintenance strategies and when each wins.

## A
- **Full recompute on a schedule** (the classic warehouse/batch approach): simple, self-healing — every run erases previous errors — but freshness = schedule interval, and cost grows with base-table size regardless of how little changed.
- **Incremental maintenance**: consume the base table's changelog (CDC) and apply each change's *delta* to the view — a stream processor keeping a running aggregate. Fresh within seconds and cost proportional to change volume, but you now own streaming infrastructure, and non-decomposable logic (e.g. exact distinct counts, complex joins) needs real operator state, not just add/subtract.

Common hybrid: incremental for freshness + periodic full recompute to heal drift.
