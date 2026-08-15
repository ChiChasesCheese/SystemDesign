---
id: distributed-tenant-isolation-limits
node: distributed.partitioning.skew
type: qa
---
## Q
One tenant's runaway job saturates a shared shard and everyone on it gets timeouts. Which mechanisms contain the blast radius, and what does each actually bound?

## A
- **Per-key / per-tenant rate limits** (token bucket at the routing tier, keyed by tenant): bounds the *offender's* request rate, so the shard never saturates. Cheapest and first to reach for; needs a distributed counter (Redis or approximate local buckets with a global reconciliation).
- **Fair queueing / weighted admission** at the shard: bounds *share* rather than rate — under overload each tenant gets a slice instead of first-come-first-served, so a burst delays only its own owner.
- **Shuffle sharding**: assign each tenant a random *subset* of k nodes out of n. With n=8, k=2 there are 28 distinct pairs, so one abusive tenant fully overlaps with only ~1/28 of the others — the blast radius shrinks combinatorially without dedicated hardware per tenant.
- **Dedicated partitions** for the largest tenants: bounds everything, at the cost of capacity planning per tenant.

Escalation order: limit → fair-queue → shuffle-shard → isolate. Note limits must return a clean `429` with a retry hint, or clients turn the limit into a retry storm.
