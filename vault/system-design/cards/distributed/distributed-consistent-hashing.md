---
id: distributed-consistent-hashing
node: distributed.partitioning.schemes
type: qa
---
## Q
In consistent hashing, what fraction of keys moves when a node joins an N-node ring, why is that the whole point, and what problem do virtual nodes solve?

## A
Only ~**K/N** of K keys move — the keys between the new node and its predecessor on the ring. With naive `hash(key) mod N`, changing N remaps **almost every key**, which would flush caches or trigger a full data reshuffle; consistent hashing makes membership change cheap.

**Virtual nodes** (each physical node owns many ring positions, e.g. 100–256) fix two issues: with few positions, random placement makes ownership arcs **wildly uneven**, and a leaving node dumps its entire range onto **one successor**. Vnodes even out load and spread a departed node's data across the whole cluster.
