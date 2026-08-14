---
id: traffic-gateway-buffering
node: traffic.gateways
type: qa
---
## Q
Reverse-proxy request/response buffering — what does it protect upstream from, and when must you turn it off?

## A
The proxy absorbs a slow client's upload fully, then forwards to the upstream at LAN speed; responses likewise: upstream hands off the full response in milliseconds and the proxy drip-feeds it. Upstream workers stop being held hostage by slow or malicious clients (slowloris-style connection exhaustion).

Turn it off when incremental delivery *is* the product:

- **SSE / streamed responses** — buffering holds events until the response completes (`X-Accel-Buffering: no` / `proxy_buffering off`).
- **Large uploads** — buffering doubles them into proxy disk/memory.
- WebSockets bypass buffering after the upgrade anyway.
