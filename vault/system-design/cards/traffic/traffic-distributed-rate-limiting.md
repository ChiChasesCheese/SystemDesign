---
id: traffic-distributed-rate-limiting
node: traffic.rate-limiting
type: qa
---
## Q
Rate limit is 1,000 req/s per API key, enforced across 20 gateway instances. Compare the two enforcement designs and their failure trade-off.

## A
- **Centralized counters** (Redis, atomic Lua/INCR): exact global limit, but adds a network hop per request and the store becomes a hot dependency — decide **fail-open or fail-closed** when it's unreachable (usually fail-open: availability over strictness).
- **Local + async sync**: each node enforces ~limit/20 or a local bucket, reconciling counts in the background — zero added latency, survives store outages, but briefly over/under-admits as traffic skews across nodes.

Approximate local enforcement is the accepted norm; exactness is rarely worth a per-request round trip.
