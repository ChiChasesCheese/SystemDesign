---
id: reliability-retry-storm
node: reliability.resilience.retries
type: qa
---
## Q
A service slows down, clients retry, and the service dies completely. Name the failure mode and three design rules that prevent it.

## A
**Retry storm** — retries multiply offered load exactly when capacity is lowest (3 layers each retrying 3x = 27x amplification).

- **Exponential backoff with jitter** so retries spread out instead of synchronizing.
- **Retry budgets** (e.g. retries ≤ 10% of requests) and retry only at one layer, not every hop.
- **Circuit breakers / load shedding** so callers fail fast instead of piling on — and only retry idempotent operations.
