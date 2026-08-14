---
id: networking-cdn-cache-key
node: networking.cdn
type: qa
---
## Q
Your CDN hit rate is mysteriously low for static assets. What cache-key mistakes cause this, and what's the fix?

## A
The cache key is (by default) the full URL plus any `Vary` headers — anything that varies fragments the cache:

- **Irrelevant query params** (tracking params, random ordering) → normalize: strip/sort params in the CDN config.
- **`Vary` on high-cardinality headers** (Cookie, full User-Agent) → drop cookies for static paths, vary only on what changes the response (e.g. `Accept-Encoding`).

Rule: put every byte that changes the response in the key, and **nothing else**.
