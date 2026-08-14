---
id: correctness-outbox-relay-lag
node: correctness.outbox
type: qa
---
## Q
The outbox relay dies for 2 hours. What is the failure mode for the system, and what do you monitor to catch it?

## A
Writes keep succeeding — the outbox insert is in the local transaction — so the system stays **available**; events are delayed, not lost, and downstream views go **stale** silently. That's the pattern's point (broker/relay outage decoupled from the write path) and its trap: nothing user-facing errors.

Monitor:
- **Oldest-unpublished-row age** (SELECT min(created_at) WHERE unsent) — the true staleness signal; alert on seconds/minutes per your freshness SLO.
- Unsent **row count** growth rate, and relay publish error rate.

On recovery the relay drains the backlog in order — expect a duplicate/late-event burst downstream, which consumer dedup ([[correctness-outbox-mechanism]]) must absorb.
