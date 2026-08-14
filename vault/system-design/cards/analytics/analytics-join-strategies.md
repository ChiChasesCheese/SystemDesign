---
id: analytics-join-strategies
node: analytics.batch
type: qa
---
## Q
Distributed join of a 10TB fact table with a 200MB dimension table: sort-merge join or broadcast hash join, and why?

## A
**Broadcast hash join**: ship the 200MB table to every executor, build an in-memory hash table, and stream the 10TB side through it — the big table never shuffles, and no sort is needed.

**Sort-merge join** is the fallback when *both* sides are large: shuffle both tables by join key so matching keys co-locate, sort each side, then merge. Cost: two full shuffles.

Rule: broadcast whenever one side fits comfortably in executor memory (engines auto-pick below a size threshold); if the "small" side is misestimated and doesn't fit, the join OOMs — a classic production failure.
