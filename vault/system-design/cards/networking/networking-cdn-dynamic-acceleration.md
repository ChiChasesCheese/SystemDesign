---
id: networking-cdn-dynamic-acceleration
node: networking.cdn
type: qa
---
## Q
Your API responses are fully personalized and uncacheable. What does routing them through a CDN still buy?

## A
- **Handshakes on a short path**: TCP/QUIC + TLS terminate at an edge ~10–20 ms away instead of 150 ms cross-continent — saving 1–2 RTTs where RTTs are cheap.
- **Warm pooled edge→origin connections**: no per-client handshake ever reaches the origin.
- **Private backbone routing**: edge-to-origin rides the provider's network, typically beating public-internet transit paths.
- **Edge absorption of hostile traffic**: WAF, bot filtering, DDoS soak before your infra.

Net effect: meaningfully lower cross-continent API latency with zero caching involved.
