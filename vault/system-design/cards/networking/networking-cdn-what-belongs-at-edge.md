---
id: networking-cdn-what-belongs-at-edge
node: networking.cdn
type: qa
---
## Q
Beyond static files, what can a modern CDN edge absorb — and what technique protects the origin even for cache misses?

## A
- **Cacheable dynamic responses**: API GETs with short TTLs (even 1–5 s absorbs a viral spike), personalized pages split so the shared shell caches.
- **Terminating work**: TLS, compression, WAF/bot filtering, edge functions for redirects/auth checks.

Miss protection: **origin shield / tiered caching** — all edge misses funnel through one mid-tier cache plus **request coalescing**, so a global miss becomes one origin fetch instead of hundreds.
