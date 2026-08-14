---
id: traffic-l4-vs-l7
node: traffic.load-balancing
type: qa
---
## Q
L4 vs L7 load balancer — what does each see, and when is L4 the right choice despite L7's flexibility?

## A
- **L4** sees only IP+port: forwards TCP/UDP flows, no payload inspection. Extremely fast, millions of connections, protocol-agnostic.
- **L7** terminates the connection and sees the request: path/header routing, TLS termination, retries, per-route policies.

Choose **L4** for raw throughput or non-HTTP traffic (databases, MQTT, game servers, WebSocket passthrough at huge scale) — or as the resilient tier **in front of** the L7 fleet, which is the common stacked pattern.
