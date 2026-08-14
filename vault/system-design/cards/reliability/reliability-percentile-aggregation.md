---
id: reliability-percentile-aggregation
node: reliability.observability
type: qa
---
## Q
Each of 50 hosts reports its own p99 latency. Why can't you average (or max) them to get the service p99, and what should hosts export instead?

## A
**Percentiles don't compose** — a percentile is a point on a distribution, and you can't reconstruct the merged distribution from per-host points. Averaging p99s systematically understates the true p99 (traffic is uneven; the worst host's tail dominates), and max overstates it.

Fix: hosts export **histograms** (fixed buckets or mergeable sketches like DDSketch/t-digest); buckets are just counters that **sum across hosts and time windows**, and the backend computes any percentile from the merged histogram at query time. Same reason latency SLIs use threshold-ratio form — [[reliability-latency-sli-form]].
