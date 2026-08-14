---
id: analytics-shuffle-mechanics
node: analytics.batch
type: qa
---
## Q
Walk through what a shuffle actually does in Spark/MapReduce, and why it's the step that dominates job cost.

## A
1. Each map task **partitions its output by hash of the key** (one bucket per reducer) and spills sorted bucket files to local disk.
2. Every reduce task then **fetches its bucket from every map task** over the network and merges the sorted runs, so all records with the same key land on one machine.

It dominates because it's an **all-to-all barrier**: M×R network transfers, full materialization to disk, and downstream stages can't start until it completes. Wide operations (`groupByKey`, joins, `repartition`) trigger it; the core optimization in any batch job is shuffling **fewer bytes, fewer times** (pre-aggregate map-side, broadcast small tables).
