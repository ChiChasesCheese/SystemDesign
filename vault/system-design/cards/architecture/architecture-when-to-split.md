---
id: architecture-when-to-split
node: architecture.services
type: qa
---
## Q
What are legitimate triggers for splitting a monolith into services — and what is the default recommendation for a new system in 2026?

## A
Legitimate triggers (organizational and operational, not aesthetic):
- **Team scaling**: deploy trains and merge conflicts across many teams; you split so teams can ship independently (Conway alignment).
- **Divergent scaling/runtime needs**: one component needs 50x the instances, a different language, or isolation for a risky dependency.
- **Fault isolation** for a component whose failure must not take the core down.

Default for new systems: a **modular monolith** — enforced module boundaries in one deployable. You get boundary discipline without the distributed-systems tax, and clean modules are the extraction seams if a real trigger arrives. "Microservices for scale" alone is not a trigger; monoliths scale horizontally fine.
