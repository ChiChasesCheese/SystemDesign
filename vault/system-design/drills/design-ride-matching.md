---
nodes: [distributed.partitioning.skew, storage.search, architecture.services, traffic.load-balancing, networking.realtime]
tags: [classic, flagship]
---
# Drill: Design ride matching

Match riders to nearby drivers in a city, in real time, while every driver
in that city reports a new location every four seconds. A geospatial
question wearing a hot-partition question underneath.

**Constraints to state and honor**
- 1M active drivers, location update every 4 seconds; matching decision within 5 seconds of a request.
- "Nearby" is a moving target: the index is written far more often than it is read.
- Demand is grossly uneven — a stadium at 22:00 is a single partition's worth of the world's traffic.
- A dropped match must be retried without ever assigning one driver to two riders.

**Grading points**
- Geospatial indexing chosen with its trade named — cell-based (geohash/S2/H3) buckets versus a tree — and why cells suit a write-heavy index ([[storage-inverted-index]], [[storage-search-not-sot]]).
- Location writes kept out of the durable store's hot path; the live index treated as regenerable state ([[storage-search-sync]], [[caching-local-vs-remote]]).
- Cell-level hotspots named as access skew, with the fix stated as splitting a cell rather than adding replicas ([[distributed-data-skew-vs-access-skew]], [[distributed-hot-key]], [[distributed-hot-key-detection]]).
- Tenant/region isolation limits acknowledged: one city's surge must not starve another ([[distributed-tenant-isolation-limits]], [[caching-cache-shard-blast-radius]]).
- Sticky routing for the driver's connection, and what happens to that connection when the gateway it landed on is redeployed ([[traffic-lb-algorithm-choice]], [[traffic-http2-connection-pinning]], [[networking-websocket-scaling-cost]]).
- Load balancing that follows partitions rather than fighting them, with bounded-load consistent hashing named ([[traffic-bounded-load-consistent-hashing]], [[traffic-lb-health-and-ha]]).
- Service boundaries drawn around data ownership — matching, pricing, trip, payments — instead of by team convenience ([[architecture-boundaries-data-ownership]], [[architecture-when-to-split]], [[architecture-distributed-monolith]]).
- The synchronous call chain through match → price → dispatch questioned before it becomes the availability ceiling ([[architecture-sync-call-chains]]).
- Real-time push to both apps with heartbeats, and offer expiry so a silent phone releases the driver ([[networking-realtime-transport-choice]], [[networking-heartbeats-idle-timeouts]]).

**Attempt log**
- [ ] Attempt 1 (date, 45 min, self-graded notes):
