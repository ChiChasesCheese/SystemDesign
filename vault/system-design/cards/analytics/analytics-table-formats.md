---
id: analytics-table-formats
node: analytics.warehouse
type: qa
---
## Q
Iceberg/Delta are "just metadata over Parquet files." What do they actually add that a directory of Parquet files lacks?

## A
- **Atomic commits / snapshots**: a table version is a metadata file listing exactly which data files belong; readers never see half-written jobs (no more `_SUCCESS`-flag conventions).
- **Schema evolution by column ID**: add/rename/drop columns safely without rewriting data files.
- **Hidden partitioning + file-level stats**: queries prune partitions and skip files by min/max column stats without listing directories or knowing the partition scheme.
- **Time travel**: query any retained snapshot; roll back a bad write by re-pointing.

In short: they turn files into a **transactional table abstraction** any engine can share.
