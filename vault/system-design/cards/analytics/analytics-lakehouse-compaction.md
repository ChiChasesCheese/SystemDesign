---
id: analytics-lakehouse-compaction
node: analytics.warehouse
type: qa
---
## Q
A streaming pipeline commits to an Iceberg/Delta table every minute. What degrades over time, and what's the maintenance answer?

## A
**Small-file buildup**: each commit writes tiny Parquet files, so queries pay per-file overhead — metadata/footer reads, one object-store GET each (~tens of ms first-byte), poor compression, less effective min/max pruning. Thousands of small files can dominate query time.

Answer: background **compaction** (`OPTIMIZE` / rewrite-data-files) merges small files into large ones (target ~128MB–1GB), optionally clustering/sorting by common filter keys; plus expiring old snapshots so dead files get deleted.

Same compaction tax as LSM-trees — moved to the lakehouse layer, and it's your job to schedule it.
