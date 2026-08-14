---
id: networking-dns-resolution-path
node: networking.dns
type: qa
---
## Q
Trace an uncached lookup of `api.example.com` from the browser to an answer. Where do caches sit in that path?

## A
Client stub resolver → **recursive resolver** (ISP or 8.8.8.8) which walks: **root** servers ("ask `.com`") → **TLD** servers ("ask example.com's nameservers") → **authoritative** server (returns the A/AAAA record).

Caches at every layer — browser, OS, recursive resolver — each honoring the record's **TTL**. In practice most lookups never leave the recursive resolver's cache, which is why DNS is fast and also why changes propagate slowly.
