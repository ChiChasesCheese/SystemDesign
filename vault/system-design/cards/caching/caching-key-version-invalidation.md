---
id: caching-key-version-invalidation
node: caching.invalidation
type: qa
---
## Q
You need to invalidate a whole *group* of cache entries at once (every page of a user's feed) without tracking each key. Pattern and costs?

## A
**Generation (versioned) keys**: embed a per-group version in every key — `feed:{user}:v42:page3`. To invalidate the group, bump the version; old entries become unreachable instantly and age out via LRU/TTL — no enumeration, no purge.

- An extra read for the current version on each access — keep it in the same cache (or a local copy).
- A bump makes the entire group cold at once — a deliberate miss spike, so pair with warming or size the backend for it.
