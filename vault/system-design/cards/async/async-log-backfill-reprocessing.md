---
id: async-log-backfill-reprocessing
node: async.log
type: qa
---
## Q
You need to rebuild a derived store by reprocessing 90 days of a Kafka topic. What makes this operationally safe, and what two limits do you hit?

## A
Start a **new consumer group** at the earliest offset (or a timestamp via offset-for-time lookup) — offsets are per-group, so production consumers are untouched, and the rebuild writes to a *new* target that you cut over atomically ([[async-materialized-view-refresh]]).

Limits:
- **Retention**: the data must still exist — long replay windows are why **tiered storage** (old segments offloaded to object storage) matters; replay reads then pull from S3, slower but without bloating broker disks.
- **Read throughput**: a backfill can saturate broker I/O and page caches used by live consumers — throttle it (quotas) or read from tiered/offloaded segments.

Also ensure historical events are still *decodable*: schema-registry compatibility is what makes 90-day-old bytes readable by today's code.
