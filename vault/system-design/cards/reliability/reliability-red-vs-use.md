---
id: reliability-red-vs-use
node: reliability.observability
type: qa
---
## Q
RED method vs USE method: what does each one measure, and which do you apply to a payment service vs a database host?

## A
- **RED** — for every *request-driven service*: **R**ate (req/s), **E**rrors (failed req/s), **D**uration (latency distribution). This is the user's view; the payment service gets RED dashboards, and RED metrics feed SLIs.
- **USE** — for every *resource* (CPU, memory, disk I/O, connection pool, GPU): **U**tilization (% busy), **S**aturation (queue depth / wait), **E**rrors. This is the capacity view; the database host gets USE.

Key discrimination: **saturation, not utilization, predicts trouble** — a resource can be 70% utilized with a growing queue. Standard practice: RED to detect user impact, USE to explain it.
