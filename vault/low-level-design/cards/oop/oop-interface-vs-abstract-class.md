---
id: oop-interface-vs-abstract-class
node: oop.interfaces
type: qa
---
## Q
Interface or abstract class — what's the decision rule? One example of each from a machine-coding problem.

## A
- **Interface**: a capability contract across otherwise-unrelated types; a class can hold many — `FareStrategy`, `Notifiable`.
- **Abstract class**: a family sharing **state and a partial implementation** — chess `Piece` holding position with abstract `possibleMoves()`.

Rule of thumb: no shared fields → interface; shared fields/protected helpers → abstract class. When torn, start with the interface — it's the weaker, easier-to-revise commitment.
