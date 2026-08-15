---
id: patterns-visitor-tradeoff
node: patterns.behavioral
type: qa
---
## Q
Visitor makes one thing easy and one thing hard. Which, and what property of the class hierarchy must hold before you use it?

## A
Visitor flips the extension axis:

- **Easy: adding operations.** A new operation over the hierarchy (type-check, pretty-print, evaluate over an AST) is one new visitor class — no touching the element classes.
- **Hard: adding element types.** A new element forces a new `visit` method on **every existing visitor** — it's the exact mirror of adding a method to every subclass.

Precondition: the element hierarchy is **stable** and the set of operations keeps growing (compilers, document models). If new element types arrive often, visitor is the wrong trade — use plain polymorphic methods. Mechanism worth naming: `element.accept(visitor)` → `visitor.visit(this)` is **double dispatch**, selecting behavior on both runtime types.
