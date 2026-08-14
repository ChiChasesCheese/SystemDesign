---
id: reliability-logs-metrics-traces
node: reliability.observability
type: qa
---
## Q
Logs, metrics, traces: which one answers "is it broken?", "where is it broken?", and "why is this request broken?" — and what does each cost at scale?

## A
- **Metrics** → "is it broken?": pre-aggregated time series; cheap to store and alert on, but you can only ask questions you pre-declared.
- **Traces** → "where?": follow one request across services, showing which hop ate the latency; cost controlled by sampling.
- **Logs** → "why?": arbitrary per-event detail for the specific failing case; the most expensive per event — volume scales with traffic, so structured + sampled or they dominate infra cost.
