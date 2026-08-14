---
id: reliability-bulkhead-vs-shedding
node: reliability.resilience
type: qa
---
## Q
Bulkheads vs load shedding — which failure does each contain, and when do you need both?

## A
- **Bulkheads** partition resources (connection pools, thread pools, instances) per dependency or tenant, so one slow dependency exhausts only its own pool — contains **cross-contamination**.
- **Load shedding** rejects excess work (by priority, early, cheaply — e.g. 429 at the front door) so the work you do accept finishes within SLO — contains **overload**.

You need both when a multi-tenant service faces both noisy neighbors and traffic spikes: bulkheads isolate who hurts, shedding caps how much total hurt is accepted.
