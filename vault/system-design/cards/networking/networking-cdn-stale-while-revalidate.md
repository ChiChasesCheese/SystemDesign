---
id: networking-cdn-stale-while-revalidate
node: networking.cdn
type: qa
---
## Q
`Cache-Control: stale-while-revalidate` and `stale-if-error` — what does each authorize a CDN to do, and what do you buy?

## A
- **stale-while-revalidate=N**: for N seconds after TTL expiry, serve the stale copy *immediately* while refetching in the background — popular keys never make a user pay origin latency, and staleness stays bounded by the window.
- **stale-if-error=N**: if the origin errors or is unreachable, keep serving the expired copy for up to N — availability from cache through an origin outage.

Both trade strict freshness for latency and availability — the right default for content where seconds-old is indistinguishable from fresh.
