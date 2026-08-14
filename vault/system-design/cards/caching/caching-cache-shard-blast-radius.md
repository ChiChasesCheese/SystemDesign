---
id: caching-cache-shard-blast-radius
node: caching.placement
type: qa
---
## Q
Clients shard keys across 10 cache nodes. Why consistent hashing instead of `hash(key) % 10`, and what is the blast radius when one node dies?

## A
With modulo, any membership change remaps nearly **all** keys — adding or losing a node is an effective cluster-wide flush, and the resulting miss storm lands on the DB. Consistent hashing moves only ~1/N of the keyspace per membership change.

Blast radius of one dead node: ~1/N of reads become misses — so node count N is a sizing lever: the DB must absorb 1/N of cache read load (plus warming) without falling over ([[caching-hit-rate-outage-math]]).
