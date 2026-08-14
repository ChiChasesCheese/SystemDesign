---
id: reliability-trace-sampling
node: reliability.observability
type: qa
---
## Q
Head-based vs tail-based trace sampling — what does each decide on, and which one keeps the traces you actually want during an incident?

## A
- **Head-based**: sample decision made at the first hop (e.g. keep 1%), propagated via the trace context so all spans of a kept trace survive. Cheap and simple — but errors and slow requests are rare, so the interesting 1-in-10k trace is usually dropped.
- **Tail-based**: buffer all spans, decide after the trace completes — keep every error and p99-slow trace, sample the boring ones. Exactly what incidents need, at the cost of a buffering/collection tier that must see the whole trace.
