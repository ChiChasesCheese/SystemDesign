---
id: infra-mesh-tax-ambient
node: infra.mesh
type: qa
---
## Q
What does a sidecar mesh cost in latency and operations, and how does the ambient/sidecarless model restructure that cost?

## A
- **Latency tax**: two extra proxy traversals per hop (caller's sidecar out, callee's sidecar in), roughly **0.5–2 ms at p99 per hop** — compounding across deep call chains.
- **Ops tax**: one proxy per pod (CPU/memory × every pod), proxy upgrades coupled to pod restarts, and one more layer in every debugging session.
- **Ambient** (e.g. Istio ambient mode) splits the proxy: a shared **per-node L4 tunnel** provides mTLS and telemetry with no per-pod sidecar, and optional **L7 waypoint proxies** are deployed only for services that need HTTP-level policy. You pay the L7 tax only on routes that use it.
