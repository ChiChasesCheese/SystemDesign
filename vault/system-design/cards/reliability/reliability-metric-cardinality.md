---
id: reliability-metric-cardinality
node: reliability.observability
type: qa
---
## Q
An engineer adds `user_id` as a label on a request-latency metric. Why does this melt the metrics system, and where does that data belong instead?

## A
Time-series stores keep **one series per unique label combination**. An unbounded label (user id, request id, URL with ids) multiplies cardinality into millions of series — memory, ingest, and query cost all scale with series count, not sample count.

Rule: metric labels must be **low-cardinality and bounded** (endpoint, status class, region). Per-user/per-request detail belongs in **structured logs or trace attributes**, which are built for high-cardinality search.
