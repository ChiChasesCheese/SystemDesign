---
id: caching-layer-absorption
node: caching.placement
type: qa
---
## Q
Traffic doubles on a page that is 90% identical for all users and 10% personalized. Which cache layers absorb which part, and why can't the CDN take it all?

## A
- **CDN/edge** absorbs the shared 90%: static assets and any response whose cache key is URL-derivable and user-independent.
- The personalized 10% must be served behind auth, so it lands on **application-level caches** (Redis keyed by user/segment) or client-side caching.

CDN caching keyed on `Cookie`/`Authorization` fragments the cache into per-user entries — hit rate collapses to ~0 and you risk serving one user's data to another if the key is wrong. Common pattern: cache the shell at the edge, fetch personalization via a small API call.
