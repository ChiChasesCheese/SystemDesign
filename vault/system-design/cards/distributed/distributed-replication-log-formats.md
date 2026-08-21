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

## Q zh
分布式系统中复制日志的常见格式是什么？

## A zh
- **语句日志** — 记录原始 SQL（INSERT ...）。小但不确定（NOW()、RAND() 在副本上不同）。
- **行日志** — 记录行级变化（旧值和新值）。更大但确定性。
- **WAL（预写日志）** — 底层存储格式的物理日志（字节位置的更改）。最小但不可读。
- **基于操作的** — 高级操作（increment counter）。小且表达力强但设计复杂。

权衡：大小 vs 确定性 vs 可读性。大多数现代系统使用行日志或 WAL。
