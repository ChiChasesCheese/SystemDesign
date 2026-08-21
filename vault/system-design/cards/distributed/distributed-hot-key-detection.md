---
id: distributed-hot-key-detection
node: distributed.partitioning.skew
type: qa
---
## Q
You suspect a hot key but can't emit a metric per key (billions of them). How do you actually find it, and at which layer?

## A
Use a **heavy-hitters sketch**, not per-key metrics: a **count-min sketch** or **space-saving / top-K** structure keeps the top N keys by frequency in fixed memory (kilobytes) with bounded error, flushed every few seconds. Put it in the layer that sees the raw key **before** partition routing — the client library, proxy/routing tier, or cache tier — so you learn the key even when the shard is already saturated.

Complements:

- **Sampled request logs** (1:1000) aggregated offline — finds yesterday's hot keys, not this second's.
- **Per-partition metrics** as the alarm, per-key sketch as the diagnosis: partition-level p99 or throttle counts tell you *which shard*, the sketch tells you *which key*.
- Managed equivalents: DynamoDB **CloudWatch Contributor Insights** reports the most-accessed partition keys directly.

The output must feed something automatic (promote to cache, enable salting for that key) — a dashboard a human reads is too slow for a key that goes hot in seconds.

## Q zh
怎样检测和定位热 key（访问倾斜）？

## A zh
**检测方法**：
1. **计数器**：在代理或客户端维护最近 N 秒的访问计数，超过阈值的 key 为热 key。
2. **采样**：定期采样请求，统计 top-k 频繁的 key。
3. **指标监控**：监听分片级别的 QPS，QPS 不均匀表示有热 key。

**定位**：代理层或客户端直接记录。存储层上报热 key 清单给代理。

**处理**：多层缓存（本地缓存、中央缓存）。热 key 专用副本或热 key 缓存集群。请求合并（多个客户端请求同一热 key，只回源一次）。
