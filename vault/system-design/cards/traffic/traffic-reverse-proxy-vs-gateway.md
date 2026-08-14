---
id: traffic-reverse-proxy-vs-gateway
node: traffic.gateways
type: qa
---
## Q
Reverse proxy vs API gateway — same box or different? Draw the line.

## A
Same mechanical position (server-side intermediary terminating client requests), different altitude:

- **Reverse proxy** (nginx, Envoy) is the *mechanism*: forwarding, TLS, buffering, compression, caching, basic routing.
- **API gateway** is a reverse proxy plus **API-level policy**: per-client auth, quotas/billing, version routing, request/response transformation, developer-facing API management.

In practice gateways are built *on* reverse proxies. If you only need "route and terminate TLS," a plain reverse proxy is less machinery to operate.
