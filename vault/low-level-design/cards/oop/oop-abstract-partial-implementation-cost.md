---
id: oop-abstract-partial-implementation-cost
node: oop.interfaces
type: qa
---
## Q
You put shared logic in an abstract base class with `protected` hooks (template method). What are you paying for that reuse, and what's the alternative shape?

## A
Costs:

- **You spend the single inheritance slot** — the subclass can never extend anything else.
- **`protected` members are public API to subclasses**: you can't rename or reorder them later without breaking every child, and the base's call order becomes a contract.
- The base is **hard to test alone** (needs a fake subclass), and subclasses can't be tested without dragging the base's behavior in.

Alternative: **interface + a composed helper** — the algorithm lives in a collaborator that takes the varying step as a strategy object. Java's compromise is the *skeletal implementation* pattern: publish the interface, offer `AbstractFoo` as an optional convenience so implementers who need their own hierarchy can forward to it instead.
