---
nodes: [async.streaming, async.delivery.exactly-once, analytics.batch, analytics.warehouse, analytics.derived]
tags: [flagship, data]
---
# Drill: Design ad click aggregation

Count clicks — per ad, per minute, per hour — for a stream that pays the
bills. Advertisers are billed from these numbers, so "roughly right" is
not a design goal, and the stream never stops to let you fix it.

**Constraints to state and honor**
- 1M clicks/second peak; dashboards must show the last minute within a minute.
- Billing totals must be reproducible: the same day recomputed tomorrow gives the same number.
- Clicks arrive late — a mobile SDK can buffer for hours — and some arrive twice.
- Fraud filtering runs later and retroactively invalidates clicks already counted.

**Grading points**
- Event time versus processing time separated on the first diagram, with watermarks and an explicit allowed-lateness policy ([[async-event-time-watermarks]], [[async-stale-event-ordering]]).
- Effectively-once framed as an end-to-end property of the boundary — idempotent producer, transactional read-process-write, deterministic sink ([[async-exactly-once-myth]], [[async-eos-boundary-choice]], [[async-kafka-transactions-eos]]).
- Idempotent producers and the reordering that a naive retry causes ([[async-idempotent-producer]], [[async-producer-retry-reordering]]).
- Sink determinism confronted: what it takes for a re-run to overwrite rather than double-count ([[async-eos-sink-determinism]], [[analytics-idempotent-reruns]]).
- The lambda-shaped answer justified or rejected on its merits: a fast streaming path for dashboards, a batch recomputation as the billing source of truth ([[analytics-batch-vs-stream]], [[analytics-derived-data-framing]]).
- Aggregates modelled as derived data with a version, so a fraud-corrected recomputation can replace a published view atomically ([[analytics-derived-view-versioning]], [[analytics-materialized-view-maintenance]]).
- Warehouse or lakehouse table format chosen for snapshot isolation and time travel, so a reader never sees a half-written partition ([[analytics-table-formats]], [[analytics-lakehouse-snapshot-isolation]], [[analytics-time-travel-retention]]).
- Skew handled: one viral ad is a hot key in every shuffle ([[analytics-skew-stragglers]], [[analytics-shuffle-mechanics]], [[distributed-hot-key]]).
- Backfill after a bad deploy described as a normal operation, not an incident ([[async-log-backfill-reprocessing]], [[analytics-backfill-cdc]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
