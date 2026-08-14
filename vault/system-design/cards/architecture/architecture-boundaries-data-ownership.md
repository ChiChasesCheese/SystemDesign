---
id: architecture-boundaries-data-ownership
node: architecture.services
type: qa
---
## Q
What's the rule for drawing service boundaries, and why is a shared database between services considered the cardinal sin?

## A
Rule: a service **exclusively owns its data** — boundary drawn around a business capability (bounded context), and all access to that data goes through the service's API or its published events.

A shared database silently couples the services back together:
- Any **schema change breaks unknown readers** — you've recreated the monolith's coupling but without the compiler, tests, or atomic deploy that made it manageable.
- Ownership of invariants is ambiguous: two writers, no one accountable for consistency.

Consequence to say out loud: no cross-service joins or transactions — you get API composition, data replication via events, and eventual consistency instead. If two "services" constantly need each other's tables, they're one service.
