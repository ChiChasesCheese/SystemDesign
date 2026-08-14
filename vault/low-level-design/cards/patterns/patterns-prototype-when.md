---
id: patterns-prototype-when
node: patterns.creational
type: qa
---
## Q
When does Prototype (clone-based creation) beat constructing from scratch? Name its classic trap.

## A
Use it when new objects are **mostly copies of a configured exemplar**:

- Construction is expensive or requires context you no longer have (parsed config, loaded resources).
- You want a **registry of pre-configured prototypes** — `registry.get("premium-invoice").copy()` — so new variants are added as data, not subclasses.
- The concrete class isn't known to the copier — `shape.clone()` works polymorphically without a `switch`.

Trap: **shallow vs deep copy** — a shallow clone shares mutable sub-objects, so two "independent" copies mutate each other. Prefer copy constructors / explicit `copy()` methods over Java's broken `Cloneable`.
