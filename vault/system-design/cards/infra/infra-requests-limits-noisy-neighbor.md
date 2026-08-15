---
id: infra-requests-limits-noisy-neighbor
node: infra.containers
type: qa
---
## Q
On a shared Kubernetes node, what do resource *requests* vs *limits* actually do — and why do CPU and memory overruns fail differently?

## A
- **Requests** = what the scheduler reserves when bin-packing pods onto nodes; your guaranteed share under contention. **Limits** = a hard runtime cap.
- **CPU is compressible**: hitting the limit means **throttling** — no crash, just mysterious p99 latency spikes.
- **Memory is incompressible**: hitting the limit is an **OOM-kill**.
- Noisy neighbors appear when pods set requests below real usage: the scheduler overcommits the node and co-tenants steal cycles or trigger evictions. For latency-critical pods, set requests = limits (Guaranteed QoS) to opt out of the fight.
