---
id: reliability-latency-sli-form
node: reliability.slo
type: qa
---
## Q
Why do SRE teams define a latency SLI as "% of requests faster than 300ms" instead of "p99 < 300ms"?

## A
The threshold form turns latency into a **good-event / total-event ratio**, which:

- Plugs directly into **error-budget math** — each slow request spends budget, same as an error.
- **Aggregates cleanly** across shards, regions, and time windows (counts add; percentiles don't — [[reliability-percentile-aggregation]]).
- Reflects users: it counts *how many* requests were slow, while a p99 target says nothing about how bad the worst 1% was or how many users it hit.

Also specify **where** it's measured (load balancer vs client) — client-side includes network reality but adds noise you don't control.
