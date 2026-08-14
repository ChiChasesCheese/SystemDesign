---
id: architecture-distributed-monolith
node: architecture.services
type: qa
---
## Q
Name the symptoms that reveal a "microservices" system is actually a distributed monolith, and the one-question test.

## A
Symptoms:

- Services must be **deployed together** or in a fixed order (lockstep releases, coordinated version matrices).
- **Shared database** or shared internal libraries that force simultaneous upgrades.
- One feature change touches **N repos**; chatty fine-grained synchronous calls ([[architecture-sync-call-chains]]).

Test: **"Can this team deploy its service alone, right now, without asking anyone?"** If not, you've kept the monolith's coupling and added network failures, latency, and operational overhead ([[architecture-microservices-tax]]) — strictly worse than either clean option. Fix by re-drawing boundaries around data ownership, or honestly merging back.
