---
id: quality-couplers-refactorings
node: quality.smells
type: qa
---
## Q
Diagnose and fix each coupler: feature envy, message chains, inappropriate intimacy, middle man.

## A
- **Feature envy** — a method uses another object's data more than its own (`order.getCustomer().getAddress().format()` logic living in `InvoicePrinter`). Fix: **move method** to where the data lives; behavior belongs with state.
- **Message chains** — `a.getB().getC().doIt()` couples the caller to the whole navigation path (Law of Demeter violation). Fix: **hide delegate** — ask the first object to do it (`a.doIt()`).
- **Inappropriate intimacy** — two classes poke each other's internals. Fix: move method/field to concentrate the interaction in one class, or extract the shared part.
- **Middle man** — a class that only forwards calls. Fix: **remove middle man**, talk to the target directly. (Note: it's the *over-applied* cure for message chains — the two smells pull in opposite directions, so aim between.)
