---
id: principles-ocp-trigger
node: principles.solid
type: qa
---
## Q
Every new discount type means editing the same growing `if/else` in `PriceCalculator` — and re-testing it. Which principle, what refactor, and when should you NOT apply it?

## A
**OCP**: extend behavior by adding code, not by modifying tested code. Refactor: extract a `DiscountRule` interface; each discount is a new class; the calculator folds over an injected list of rules.

Don't apply speculatively: a conditional with two stable cases doesn't earn the abstraction. OCP triggers on the *second or third* variant of the same axis — that's evidence the axis really varies.
