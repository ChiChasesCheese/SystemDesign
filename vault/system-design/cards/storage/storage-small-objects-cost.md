---
id: storage-small-objects-cost
node: storage.object
type: qa
---
## Q
Storing 1 billion 4KB objects in S3 costs far more than the same 4TB as large objects. Where does the money and latency go, and what's the fix?

## A
Object storage prices and performs **per request, not per byte**:

- **Requests dominate**: writing a billion objects ≈ $5k in PUTs alone; every read is a full GET round-trip (~tens of ms) for 4KB; LISTing returns 1,000 keys per call — a full enumeration is a million paged calls.
- Lifecycle transitions and archive tiers also bill per object, and archive tiers have per-object minimum sizes/durations.

Fix: **pack small records into large objects** (Parquet/ORC files, tar-style bundles, or a log-structured layout with an index), targeting ~100MB+ per object, and read records back with ranged GETs — see [[storage-multipart-ranged-io]] and [[analytics-lakehouse-compaction]].
