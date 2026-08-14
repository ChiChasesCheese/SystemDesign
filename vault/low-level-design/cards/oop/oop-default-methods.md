---
id: oop-default-methods
node: oop.interfaces
type: qa
---
## Q
What problem do interface default methods solve, and which two limits keep them from replacing abstract classes?

## A
They let a published interface **grow without breaking existing implementations** — add the method with a sensible default, implementers override at leisure.

Limits:
- **No instance state** — a default can only compute over the interface's own methods.
- **Diamond conflicts**: inherit the same default from two interfaces and the class must override explicitly (`InterfaceName.super.method()` to pick one).
