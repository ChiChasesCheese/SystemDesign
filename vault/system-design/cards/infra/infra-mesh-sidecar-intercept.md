---
id: infra-mesh-sidecar-intercept
node: infra.mesh
type: qa
---
## Q
Mechanically, what does a service-mesh sidecar do to a pod's traffic — and why does intercepting at that point enable every mesh feature?

## A
At pod startup, iptables rules are installed that transparently **redirect all inbound and outbound TCP through an L7 proxy (Envoy) running in the same pod**. The application is unmodified and unaware — it thinks it's talking to the network.

Because every byte now crosses a proxy on both ends of a call, the mesh can: terminate/originate **mTLS**, parse HTTP/gRPC for **per-request metrics and traces**, enforce **retries, timeouts, and authz policy**, and route by header or percentage — all pushed from a control plane as config, with zero application code.
