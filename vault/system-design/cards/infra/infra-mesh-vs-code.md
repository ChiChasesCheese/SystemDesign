---
id: infra-mesh-vs-code
node: infra.mesh
type: qa
---
## Q
mTLS, retries, and traffic splitting can live in a shared library or in the mesh. When does the mesh win, and what does it inherently do worse than code?

## A
- Mesh wins on **polyglot fleets** (one proxy implementation vs a library per language), **upgrades without redeploying apps**, and **uniform enforcement** — security can guarantee mTLS everywhere without trusting every team.
- Code wins on **context**: the app knows which calls are idempotent and what a sensible fallback is. A mesh retry policy applies blindly per route — it can retry non-idempotent writes, and it can stack with app-level retries into a multiplicative retry storm.
- Working split: transport concerns (mTLS, telemetry, routing, splitting) to the mesh; semantic concerns (fallbacks, idempotency-aware retries, business timeouts) in code — and configure retries at **exactly one** layer.
