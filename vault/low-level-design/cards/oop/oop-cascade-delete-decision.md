---
id: oop-cascade-delete-decision
node: oop.relationships
type: qa
---
## Q
`removeFloor(floor)` is called. How does the relationship type decide what happens to the objects the floor referenced, and what must you clean up regardless?

## A
- **Composition (owned parts)** — `Spot`s exist only inside that floor → **cascade**: delete them with the floor; nothing else may hold a reference.
- **Aggregation (shared parts)** — a `Vehicle` parked there outlives the floor → **never cascade**: either detach (`spot.release()`) or **refuse the delete** while a live reference exists, which is usually the right answer for occupied floors.

Regardless of type, delete must also remove the object from every **secondary index / back-pointer** you built (`spotById`, `ticketsByPlate`). In-memory designs don't have foreign keys, so a missed index entry becomes a stale object that stays reachable and reads as "deleted but still bookable."
