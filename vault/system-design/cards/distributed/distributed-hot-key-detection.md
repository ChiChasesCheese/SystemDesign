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
