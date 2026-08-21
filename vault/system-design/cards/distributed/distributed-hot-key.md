---
id: distributed-hot-key
node: distributed.partitioning.skew
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

## Q zh
热 key 是什么，会导致什么问题？

## A zh
**热 key**：某个 key 被访问频率远高于平均，如明星用户、热点新闻的阅读量。

**问题**：
- **分片过载**：该 key 所在分片的 CPU 和网络流量爆炸，成为性能瓶颈。
- **缓存失效**：缓存一旦过期，大量并发请求打到存储→缓存击穿。
- **副本不堪一击**：若热 key 所在副本故障，无其他副本承载该 key。

**根本原因**：分片键选择不当，或业务自身的幂律分布（某些用户/内容远比其他受欢迎）。
