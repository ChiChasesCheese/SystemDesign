---
id: distributed-hot-key
node: distributed.partitioning
type: qa
---
## Q
A celebrity account makes one partition take 100x the traffic of the rest. Why doesn't adding shards help, and what does?

## A
Adding shards rebalances *keys*, but all this load is on **one key** — it still lands on a single partition. Skew, not capacity, is the problem.

- **Reads**: cache the hot key in front (app/Redis tier, request coalescing) — reads are the easy half.
- **Writes**: **salt/split the key** — append a random suffix (`key#1..key#N`) to spread writes over N partitions; readers must fan out and merge, so apply only to detected hot keys.
- Isolate: move the hot key/tenant to its own dedicated partition or handling path.

Detection matters: per-key traffic metrics, because salting everything makes all reads scatter-gather.
