---
id: async-queue-backpressure
node: async.queues
type: qa
---
## Q
A queue's depth is growing without bound. Why is "the queue absorbs it" not an answer, and what are your options?

## A
An unbounded queue converts an overload failure into a *latency* failure: messages still get processed, but hours late, and the backlog hides that consumers can't keep up.

Options, in order of preference:
- **Scale consumers** until you hit the downstream bottleneck (often the DB, not the workers).
- **Bound the queue and push back**: reject/slow producers (backpressure) so callers fail fast instead of queuing stale work.
- **Shed load**: drop or downgrade low-value messages; route poison/expired work to a DLQ.
- Alert on **queue depth and consumer lag age**, not just error rate.
