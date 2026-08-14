---
id: patterns-builder-when
node: patterns.creational
type: qa
---
## Q
What two construction problems does Builder solve, and when is it over-engineering?

## A
- **Telescoping constructors**: many parameters, several optional — `new Pizza(12, true, false, null, true)` is unreadable and error-prone. Builder gives named, order-free steps.
- **Immutable objects built in stages**: collect values mutably, validate everything once in `build()`, emit an immutable result — no half-initialized object ever escapes.

Skip it when the class has ≤3 required params and no optionals — a plain constructor (or static factory with named intent) is clearer. The GoF "director" role is almost never needed in practice; the fluent-builder form is what interviews expect.
