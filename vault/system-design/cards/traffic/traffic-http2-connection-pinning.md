---
id: traffic-http2-connection-pinning
node: traffic.load-balancing
type: qa
---
## Q
You put gRPC services behind an L4 load balancer; one backend runs hot while new instances sit idle. Why, and what are the fixes?

## A
L4 balances **connections**, and gRPC/HTTP-2 clients open one long-lived multiplexed connection — every request from a client pins to whichever backend won the initial pick. Scale-outs get nothing: existing connections never move.

- **L7 proxy** (Envoy/ALB) balancing per-request/per-stream instead of per-connection.
- **Client-side load balancing**: client resolves the backend set and picks per request (often over a subset).
- Blunt backstop: server-enforced `max-connection-age` forcing periodic reconnect and re-pick.
