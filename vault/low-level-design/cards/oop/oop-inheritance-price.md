---
id: oop-inheritance-price
node: oop.pillars
type: qa
---
## Q
Inheritance buys polymorphism plus code reuse with one keyword. What price does it charge that composition doesn't?

## A
- **Strongest coupling available**: the subclass depends on base internals — base edits break children (fragile base class).
- **Fixed at compile time** and single-slot (one superclass); a composed collaborator is swappable at runtime and stackable.
- **Public is-a commitment**: every base contract now binds you (LSP), forever part of your API.

Hence: inherit for substitutable is-a, compose for reuse.
