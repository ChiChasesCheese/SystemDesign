---
id: caching-negative-caching
node: caching.strategies
type: qa
---
## Q
Lookups for keys that *don't exist* miss the cache every time and hit the DB. What's the fix, and its two risks?

## A
**Negative caching**: on a DB miss, store a "not found" marker under the key with a short TTL — repeated lookups (dead links, scrapers, id enumeration) get absorbed instead of each costing a DB query.

- **Create-after-miss invisibility**: an item created while its negative entry lives is hidden until the TTL expires → explicitly delete the negative entry on create.
- **Junk-key growth**: attackers can fill the cache with markers for random keys → keep negative TTLs short and let eviction handle volume.

DNS bakes the same idea in natively — [[networking-dns-negative-caching]].
