---
id: analytics-backfill-cdc
node: analytics.derived
type: qa
---
## Q
You're standing up a new derived view (search index, feature store) from a database that already holds years of data. Why do you need two pipelines, and how do you stitch them without gaps or double-processing?

## A
CDC alone can't help: the log doesn't retain history back to the beginning, so you need a **backfill** (bulk load from a snapshot) *plus* the **CDC tail** for ongoing changes.

Stitching: take a consistent snapshot whose **log position is known** (e.g. Debezium's initial snapshot records the binlog offset; or a backup annotated with its LSN), bulk-load it, then start CDC **exactly at that offset**. Overlap is tolerated by making applies idempotent/upserts — replaying a change you already have converges to the same state.

Gap = missed updates forever; that's why "snapshot with known offset" is the load-bearing detail.
