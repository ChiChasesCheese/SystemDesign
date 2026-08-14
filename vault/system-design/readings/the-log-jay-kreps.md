---
nodes: [async.log, async.streaming]
url: https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
tags: [canonical]
---
# The Log: What every software engineer should know (Jay Kreps)

The single most influential essay behind Kafka, CDC, and stream processing.
Kreps (Kafka's creator) argues the append-only log is the unifying abstraction
for replication, messaging, and derived data.

**Extract on read:**
- Why a log subsumes both messaging and replication (state-machine replication).
- Logs as the source of truth; databases and caches as materialized views.
- How log compaction reconciles "infinite retention" with bounded storage.

Related cards: [[async-log-vs-queue]], [[async-consumer-groups-offsets]], [[async-cdc-mechanism]]
