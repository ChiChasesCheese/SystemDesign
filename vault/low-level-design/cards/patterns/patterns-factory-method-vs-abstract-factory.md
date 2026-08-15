---
id: patterns-factory-method-vs-abstract-factory
node: patterns.creational
type: qa
---
## Q
Factory method vs abstract factory — what does each vary, and what's the tell for which one you need?

## A
- **Factory method** varies **one product** via an overridable creation step: subclasses (or a lambda/registry) decide which concrete class to instantiate. Tell: "callers shouldn't `new` the concrete type."
- **Abstract factory** varies a **family of related products** that must be used together (e.g. `Button` + `Checkbox` per UI theme, or connection + statement + transaction per DB vendor). Tell: "products must stay mutually consistent — never mix a Mac button with a Windows checkbox."
- An abstract factory is typically **implemented as** a set of factory methods; the pattern distinction is the *consistency-of-family* requirement, not the mechanics.
