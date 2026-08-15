---
id: infra-mesh-when-not
node: infra.mesh
type: qa
---
## Q
When is a service mesh not worth adopting?

## A
- **Few services or a single language**: a shared library plus an API gateway covers TLS, retries, and metrics with far less machinery.
- **Mostly north-south traffic**: meshes govern service-to-service (east-west) calls; if a gateway fronts a monolith or a couple of backends, there's little east-west to manage.
- **No platform team**: a mesh is a product you operate — control plane upgrades, proxy versioning, CRD sprawl.

It earns its keep with **many polyglot services**, a compliance mandate for uniform mTLS/authz, or cross-team traffic-policy needs (splits, mirroring) — i.e. when the alternative is N teams reimplementing the same guarantees.
