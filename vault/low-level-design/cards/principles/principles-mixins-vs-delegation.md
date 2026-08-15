---
id: principles-mixins-vs-delegation
node: principles.composition
type: qa
---
## Q
Mixins/traits (Java default methods, Scala/Rust traits, Python mixins, Go embedding) promise reuse without forwarding code. What do they actually cost?

## A
They are **inheritance with a wider slot** — the fragility mostly stays:

- **Java default methods**: no instance state, and the same-signature diamond forces an explicit `X.super.m()` override.
- **Python mixins**: reuse comes with the **MRO** — which sibling's method runs depends on the class's linearization order, so a base-class edit can silently reroute behavior.
- **Go embedding**: forwarding is automatic, but there is no virtual dispatch back to the outer type — the SELF problem in full.
- All of them still expose the mixin's members as part of your public surface.

Rule: use a trait/mixin for a **stateless capability** with no per-user variation (`Comparable`, `Serializable`-style). Anything with state or a lifecycle → delegate to a collaborator.
