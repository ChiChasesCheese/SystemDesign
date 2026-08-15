---
id: method-cross-object-invariant
node: method.modeling
type: qa
---
## Q
"A vehicle may hold at most one active ticket." Neither `Vehicle` nor `Ticket` can enforce this alone. Where does the invariant go?

## A
An invariant spanning several objects belongs to the **smallest object that can see all of them** — here `ParkingLot` (the aggregate root), which owns ticket issuance and can check the existing-active-ticket index atomically.

Consequences worth saying out loud:
- `new Ticket(...)` must not be callable from outside; construction goes through `lot.issueTicket(vehicle)`.
- The root becomes the **transaction/lock boundary** if concurrency is added later.

Rule: if enforcement needs two objects' state, neither of them is the owner — find or introduce the one that contains both.
