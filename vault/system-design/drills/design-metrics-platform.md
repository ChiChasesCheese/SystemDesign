---
nodes: [reliability.observability, reliability.slo, analytics.olap, async.streaming, storage.internals]
tags: [flagship, operations]
---
# Drill: Design a metrics and alerting platform

Ingest telemetry from 50,000 hosts, answer dashboard queries in under a
second, and page a human when — and only when — something is actually
wrong. The half nobody prepares for is the second half.

**Constraints to state and honor**
- 20M samples/second ingest; 13 months retention, with older data downsampled.
- Dashboard queries over a week of data return in under a second.
- Alerting must survive the failure it is alerting about — a shared dependency outage cannot silence the pager.
- Cardinality is user-controlled: someone will put a request id in a label.

**Grading points**
- Metrics, logs, and traces separated by what each one costs and answers, rather than merged into "observability" ([[reliability-logs-metrics-traces]], [[reliability-red-vs-use]]).
- Cardinality treated as the platform's central scaling limit, with an enforced budget and a rejection path ([[reliability-metric-cardinality]]).
- A time-series storage layout argued from the write pattern: append-heavy, LSM-shaped, with compaction and the amplification it trades ([[storage-btree-vs-lsm]], [[storage-compaction-strategies]], [[storage-amplification-triangle]]).
- Columnar layout and compression for the query path, with the reason a row store loses here ([[analytics-row-vs-column-layout]], [[analytics-columnar-compression]], [[analytics-vectorized-execution]]).
- Pre-aggregation and downsampling as derived views with an explicit refresh strategy, not a cron nobody owns ([[async-materialized-view-refresh]], [[analytics-column-store-writes]]).
- Streaming aggregation with event time and watermarks, and a stated policy for late samples ([[async-event-time-watermarks]], [[async-stale-event-ordering]]).
- Percentiles never averaged across hosts; histograms aggregated instead ([[reliability-percentile-aggregation]], [[reliability-percentiles-over-averages]]).
- SLIs defined as a ratio of good events to valid events, with alerts on burn rate rather than on a threshold crossing ([[reliability-latency-sli-form]], [[reliability-burn-rate-alerting]], [[reliability-symptom-vs-cause-alerts]]).
- Traces sampled with a policy that keeps the interesting ones, and exemplars linking a metric spike to a trace ([[reliability-trace-sampling]], [[reliability-exemplars]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
