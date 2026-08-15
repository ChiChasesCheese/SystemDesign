---
id: oop-interface-width-by-client
node: oop.interfaces
type: qa
---
## Q
In a 90-minute design, how do you decide where to split an interface — and what makes a split *too* fine?

## A
Split by **client**, not by method count. If every caller of a 4-method interface uses all 4, it is cohesive and splitting it just multiplies files. Split when one client uses a strict subset, e.g. the pricing engine only ever `read`s the catalog while the admin flow `write`s it → `CatalogReader` + `CatalogWriter`, one class implementing both.

- **Too fine**: one-method interfaces per client of the *same* role, so a single implementation is declared `implements A, B, C, D` and every wiring site names four types.
- Signal that you split correctly: some client's constructor got **narrower**, and its test fake got shorter.

The purpose is shrinking what a client can depend on, not shrinking the interface.
