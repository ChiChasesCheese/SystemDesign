---
id: async-cdc-mechanism
node: async.streaming
type: qa
---
## Q
How does log-based CDC (e.g. Debezium) capture changes, and why is it preferred over the application publishing events itself or polling the table?

## A
It **tails the database's replication log** (WAL/binlog) and emits every committed row change, in commit order per key, into a stream.

- vs **app publishes**: CDC can't miss or invent events — it sees exactly what committed, even writes from other code paths, migrations, or manual fixes.
- vs **polling**: no missed intermediate states, no `updated_at` race, deletes are captured, and latency is sub-second instead of poll-interval.

Cost: events are row-level and schema-shaped, not intent-shaped — you often re-derive domain meaning downstream (or use the outbox pattern for intent events).
