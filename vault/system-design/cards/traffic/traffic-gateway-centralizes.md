---
id: traffic-gateway-centralizes
node: traffic.gateways
type: qa
---
## Q
An API gateway sits in front of 30 microservices. Which cross-cutting concerns does it centralize that would otherwise be reimplemented 30 times?

## A
- **TLS termination** — one place holding certs.
- **Authentication** — validate the JWT/session once, forward trusted identity headers; services skip auth logic.
- **Routing & versioning** — path → service mapping, canary splits.
- **Protection** — rate limits, quotas, request size caps, WAF.

Plus observability chokepoint: uniform access logs, metrics, and trace-id injection for every request entering the system.
