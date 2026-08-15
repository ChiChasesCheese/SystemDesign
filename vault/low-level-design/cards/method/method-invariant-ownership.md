---
id: method-invariant-ownership
node: method.modeling
type: qa
---
## Q
Requirement: "a spot holds at most one vehicle." Which class enforces this invariant — and why not the `ParkingService` that calls it?

## A
The owner of the state: `Spot.park(vehicle)` fails if already occupied. Enforcing it in the service means every current and future call path can corrupt the spot — the invariant holds only by convention.

Rule: **entities protect their own invariants; services orchestrate**. Enforcement at the data owner makes the illegal state unreachable from any caller.
