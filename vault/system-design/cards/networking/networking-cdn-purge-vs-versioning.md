---
id: networking-cdn-purge-vs-versioning
node: networking.cdn
type: qa
---
## Q
Shipping a new asset build behind a CDN: purge/invalidate vs versioned URLs — compare, and what's the standard practice?

## A
- **Purge**: propagates across PoPs in seconds–minutes (eventual), is a per-URL operational step, and does nothing for copies already in *browser* caches.
- **Versioned (fingerprinted) URLs**: content hash in the name (`app.3f2a1c.js`) makes each asset immutable → `max-age=1yr, immutable`; "invalidation" is just deploying HTML that references new names — instant and atomic.

Standard: fingerprint everything referenced; keep the HTML entry point short-TTL/no-store as the mutable pointer. Purge is for emergencies (leaked or wrong content), not deploys.
