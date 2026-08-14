---
id: oop-polymorphism-vs-switch
node: oop.pillars
type: qa
---
## Q
When do you replace a switch-on-type with polymorphism — and when is keeping the switch the better design?

## A
- **Replace** when the same type-switch recurs in several places and new variants keep arriving: one class per variant localizes each addition to one file (this is OCP in action).
- **Keep** a single exhaustive switch over a closed enum in one place: the compiler flags missing cases, and class-per-variant there is speculative generality.

Count the switch sites and the expected variants before reaching for the hierarchy.
