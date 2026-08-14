---
id: architecture-conways-law
node: architecture.services
type: qa
---
## Q
Conway's law says architecture copies org structure. How do mature orgs use it as a *design input* rather than a curse?

## A
**Inverse Conway maneuver**: since the system will mirror team communication paths anyway, design the *teams* to match the architecture you want — one long-lived team per service group, each owning its services end-to-end (build, run, on-call).

Practical consequences:

- A service boundary that **splits across two teams** will erode into chatty coupling and unclear ownership — redraw the boundary or merge the teams.
- **Team cognitive load caps service scope**: split when a team can no longer hold its domain, not at some ideal "microservice size."
- Interview signal: justify boundaries by *ownership and change patterns* ([[architecture-boundaries-data-ownership]]), not by technology layers.
