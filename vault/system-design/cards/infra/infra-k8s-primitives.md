---
id: infra-k8s-primitives
node: infra.containers
type: qa
---
## Q
At design-conversation depth: what do a Kubernetes Pod, Deployment, Service, and HPA each abstract?

## A
- **Pod**: smallest schedulable unit — one or more containers sharing network and storage. Mortal by design; its IP is ephemeral.
- **Deployment**: a declared desired state ("N replicas of image X"); a controller continuously reconciles reality toward it — that reconciliation loop is what gives self-healing and rolling updates.
- **Service**: a stable virtual IP/DNS name load-balancing over whichever pods are currently healthy — the answer to "pods die and change IPs".
- **HPA** (horizontal pod autoscaler): adjusts replica count to hold a metric at a target (e.g. 70% of requested CPU). It's reactive — scrape interval plus pod boot time means it lags spikes, so it can't replace headroom.
