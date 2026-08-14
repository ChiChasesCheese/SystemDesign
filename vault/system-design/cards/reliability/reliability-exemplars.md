---
id: reliability-exemplars
node: reliability.observability
type: qa
---
## Q
You see a p99 latency spike on a dashboard and now need one concrete slow request to debug. What feature jumps you straight from the metric to a trace, and how does it work?

## A
**Exemplars**: when recording a latency observation into a histogram bucket, the metrics SDK attaches the current **trace ID** (a sampled reference request) to that bucket. The dashboard renders exemplars as clickable points on the latency chart — one click lands on a real trace from the slow bucket.

This closes the classic gap: metrics tell you *that/where* it's slow, traces tell you *why*, and exemplars are the join between them — no timestamp archaeology across systems. Requires trace context active where metrics are recorded (OpenTelemetry does this natively).
