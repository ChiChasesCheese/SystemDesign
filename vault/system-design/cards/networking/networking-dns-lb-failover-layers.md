---
id: networking-dns-lb-failover-layers
node: networking.dns
type: qa
---
## Q
Health-checked DNS (e.g. Route 53) can drop a dead region from its answers. Why do you still need LB-level failover underneath — how is the labor divided?

## A
DNS failover operates at **minutes** granularity: health-check interval + record TTL + resolvers that ignore TTLs ([[networking-dns-ttl-failover]]). That's acceptable — and the only option — at *region/site* level, where the failing targets have different IPs.

*Instance* failure needs **seconds**: the load balancer's health checks eject a dead backend before the next request, behind the same VIP, with clients never involved.

Layered rule: GSLB/DNS chooses the region; the LB chooses the instance. Using DNS for instance failover means minutes of errors per dead host.
