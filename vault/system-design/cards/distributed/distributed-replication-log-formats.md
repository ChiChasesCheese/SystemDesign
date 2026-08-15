---
id: distributed-replication-log-formats
node: distributed.replication.leader
type: qa
---
## Q
Statement-based vs WAL shipping vs logical (row-based) replication — what breaks or binds with each, and which do modern systems default to?

## A
- **Statement-based** (ship the SQL): breaks on nondeterminism — `NOW()`, `RAND()`, auto-increments, triggers, concurrent-execution order. Requires rewriting statements to be deterministic; mostly abandoned as a default.
- **WAL shipping** (ship physical block changes): exact but **couples replicas to the storage-engine version and layout** — leader and follower must run compatible versions, blocking zero-downtime rolling upgrades across versions.
- **Logical (row-based)** (ship row insert/update/delete records): decoupled from engine internals — enables cross-version replication, and is the basis of **CDC** to external systems (Debezium reading Postgres logical decoding / MySQL binlog `ROW` format).

Default answer: logical/row-based for flexibility; WAL shipping inside a single homogeneous cluster.
