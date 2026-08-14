---
id: networking-anycast-vs-geodns
node: networking.dns
type: qa
---
## Q
Anycast vs GeoDNS for steering users to the nearest site — mechanism and weakness of each?

## A
- **Anycast**: the *same* IP announced via BGP from many sites; the network routes each client to the topologically closest. Failover is instant (withdraw the route) and DNS-invisible — but you don't control the mapping (BGP does), and a route flap can shift mid-connection, so it favors short flows and UDP (DNS roots, CDN edges).
- **GeoDNS/GSLB**: the authoritative server returns *different* IPs based on where the query comes from. Fine-grained control and weighted splits — but it sees the **resolver's** location, not the client's (public resolvers mislocate; EDNS Client Subnet only partially fixes it), and every change is TTL-bound.

Big CDNs use both: GeoDNS to pick a region, anycast within it.
