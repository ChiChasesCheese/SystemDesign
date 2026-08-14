---
id: traffic-gateway-risks
node: traffic.gateways
type: qa
---
## Q
What risks does putting an API gateway in front of everything create, and how is each mitigated?

## A
- **Single point of failure**: gateway down = whole product down → run it as a **stateless horizontally-scaled fleet** behind an L4 LB; config from a replicated store.
- **Latency tax**: one extra hop plus any auth/transform work on *every* request → keep per-request logic lean; ~ms budget.
- **Team bottleneck / god-box**: all routing and policy changes funnel through one component → self-serve declarative config (per-team route ownership, GitOps) instead of a central gatekeeper team.
