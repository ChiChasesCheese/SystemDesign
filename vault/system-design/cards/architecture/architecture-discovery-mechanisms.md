---
id: architecture-discovery-mechanisms
node: architecture.discovery
type: qa
---
## Q
Client-side vs server-side service discovery: how does each find healthy instances, and which does Kubernetes give you?

## A
- **Client-side**: caller queries a registry (Consul, Eureka) and load-balances across instances itself. Fewer hops and smart per-request balancing, but discovery logic lives in every client/language.
- **Server-side**: caller hits a stable virtual name; a load balancer/proxy resolves to instances. Dumb clients, but an extra hop and the LB is now critical infra.
- **Kubernetes**: server-side by default — a `Service` gives a stable DNS name/VIP; readiness probes gate which pods receive traffic. A service mesh (sidecar or ambient) moves balancing back client-side without app code.

Either way, the registry's real job is **health**: instances are registered on start and evicted on failed health checks/missed heartbeats — a registry of dead instances is worse than none.
