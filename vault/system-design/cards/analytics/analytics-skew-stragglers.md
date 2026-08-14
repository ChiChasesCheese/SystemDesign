---
id: analytics-skew-stragglers
node: analytics.batch
type: qa
---
## Q
A 1000-task stage finishes in 5 minutes except one task still running after an hour. Give the two distinct causes and the fix for each.

## A
- **Data skew (hot key)**: hash partitioning sent one giant key (the null key, the whale customer) to one reducer. Fixes: **salt the key** (split it into `key#0..N` subkeys, aggregate twice), map-side pre-aggregation, or the engine's skew-join handling (e.g. Spark AQE splits oversized partitions).
- **Slow node (straggler)**: same data volume, sick machine (failing disk, noisy neighbor). Fix: **speculative execution** — run a duplicate of the slow task elsewhere, take the first finisher.

Diagnose by task input size: huge input = skew; normal input, slow progress = straggler. Speculation does nothing for skew — the duplicate gets the same giant key.
