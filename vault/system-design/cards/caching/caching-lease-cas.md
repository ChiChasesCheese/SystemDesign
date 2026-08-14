---
id: caching-lease-cas
node: caching.invalidation
type: qa
---
## Q
Even with delete-on-write, cache-aside has a residual stale-set race. How do memcached *leases* (Facebook) close it?

## A
The race: reader misses, reads the old value from the DB; a write commits and deletes the key; the reader then sets its stale value — wrong until TTL ([[caching-delete-not-update]]).

**Leases**: on a miss, the cache hands the reader a lease token; the reader may only set the key *with* that token. Any delete arriving in between **invalidates outstanding leases**, so the stale set is refused.

Bonus: leases throttle stampedes — only the current lease holder may repopulate; other missers briefly wait or serve the last stale value.
