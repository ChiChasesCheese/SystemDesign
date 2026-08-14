---
id: distributed-lww-danger
node: distributed.time
type: qa
---
## Q
Why is last-write-wins by wall-clock timestamp a data-loss mechanism, not a conflict resolution strategy?

## A
Wall clocks on different nodes disagree: NTP sync leaves ms–100s of ms of skew, clocks **step backwards** on correction, and VMs pause. So "last" is decided by whichever node's clock runs fast — a genuinely later write can carry an *earlier* timestamp and be **silently discarded**. Cassandra-style LWW drops concurrent writes with no error and no trace.

Acceptable only when losing one of two concurrent updates is fine (e.g. idempotent "current status" values). Otherwise: version vectors to *detect* concurrency and merge, CRDTs, or route conflicting writes through a single leader. Hybrid: TrueTime-style bounded clocks (Spanner) make timestamp ordering safe by waiting out the uncertainty.
