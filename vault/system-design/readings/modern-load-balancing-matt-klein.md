---
nodes: [traffic.load-balancing]
url: https://blog.envoyproxy.io/introduction-to-modern-network-load-balancing-and-proxying-91ef79a71c8a
tags: [canonical]
---
# Introduction to Modern Network Load Balancing and Proxying (Matt Klein)

Written by Envoy's creator, this is the one essay that covers the entire
load-balancing landscape — L4 vs L7, algorithms, health checking, DNS/middle/
sidecar topologies — with production judgment behind every claim.

**Extract on read:**
- Why L4 breaks down for multiplexed protocols (HTTP/2, gRPC) and L7 fixes it.
- Algorithms in practice: round robin vs least-request vs power-of-two-choices.
- LB high availability itself: DNS, anycast, and consistent-hash ECMP at the edge.
