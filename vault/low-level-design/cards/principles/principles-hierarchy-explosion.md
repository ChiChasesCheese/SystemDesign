---
id: principles-hierarchy-explosion
node: principles.composition
type: qa
---
## Q
Coffee add-ons modeled as subclasses: `CoffeeWithMilk`, `CoffeeWithMilkAndSugar`, `CoffeeWithSoyMilkAndSugar`... Why does this hierarchy rot, and what's the composition fix?

## A
- **Combinatorial explosion**: n independent add-ons ⇒ up to 2^n subclasses, because inheritance forces all variation axes into one tree.
- Every base change ripples through the tree (fragile base class).

Fix: make the varying dimension a composed object — decorators wrapping a `Beverage`, or a list of `AddOn` components. Composition lets independent axes vary independently.
