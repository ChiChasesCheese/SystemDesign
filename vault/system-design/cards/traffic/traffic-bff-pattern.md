---
id: traffic-bff-pattern
node: traffic.gateways
type: qa
---
## Q
Backend-for-Frontend: what failure of the single shared API gateway does it address, and at what cost?

## A
A single gateway serving web, mobile, and partners accretes conflicting per-client logic — payload shaping, aggregation, feature quirks — owned by no one (the god-box problem, [[traffic-gateway-risks]]).

**BFF**: one thin edge service per client type, owned by that client's team — the mobile BFF aggregates and trims for constrained devices; the web BFF evolves independently.

Cost: more deployables and the temptation to duplicate cross-cutting policy — so auth, rate limiting, and TLS stay in a shared gateway layer *beneath* the BFFs; BFFs hold only per-client shaping.
