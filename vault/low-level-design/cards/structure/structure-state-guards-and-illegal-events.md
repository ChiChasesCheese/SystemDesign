---
id: structure-state-guards-and-illegal-events
node: structure.state-machines
type: qa
---
## Q
"An order may ship from PAID only if every line item is in stock." Why can't a state→state table express this, and how should the illegal case be reported?

## A
Legality is a triple **(current state, event, guard)** — not a pair of states. Model transitions keyed by *event* and attach a predicate:

```java
record Transition(State from, Event on, Predicate<Order> guard, State to) {}
```
`state × event` picks the row; the guard decides. Otherwise the stock check leaks back into the caller, which is what the table was supposed to prevent.

Reporting the rejection — choose by what the caller can do:
- **Throw** when it's a programming error (`SHIPPED → PAID`): unreachable if callers are correct.
- **Return a typed failure** when it's expected business flow ("out of stock") — the caller retries or messages the user; exceptions for control flow here are noise.
- **No-op** for idempotent repeats (`cancel()` on a CANCELLED order) — but only if repeat is genuinely harmless.
