---
id: structure-state-table-vs-state-pattern
node: structure.state-machines
type: qa
---
## Q
Transition table/enum vs the GoF State pattern (one class per state) — how do you choose in a timed machine-coding round?

## A
Decide by **where the complexity is**:

- **Table/enum** when the logic *is* the transitions and per-state behavior is trivial (order lifecycle, booking status). Far less code — the right default under time pressure.
- **State pattern** when each state carries **substantial distinct behavior** (elevator: MovingUp/DoorOpen/Idle each handle `requestFloor` differently) — behavior lives in the state class, and you delete the giant `switch` repeated across methods.

Say the trade-off out loud: State pattern = one class per state (more files, open for extension); table = one map (compact, but every event method still branches).
