---
id: networking-dns-ttl-failover
node: networking.dns
type: qa
---
## Q
Why is DNS a blunt instrument for failover, and what two things do teams do about it?

## A
Because you can't force clients to forget: cached records live until **TTL expires**, and some resolvers/apps ignore TTLs or pin connections — so after a DNS switch, traffic bleeds to the dead endpoint for minutes.

- **Pre-drop TTL** (e.g. 60 s) on records you may need to move — accepting more resolver load.
- **Fail over below DNS instead**: anycast IPs or a load balancer VIP, so the IP stays the same and rerouting is instant.
