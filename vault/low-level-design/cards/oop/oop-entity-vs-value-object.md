---
id: oop-entity-vs-value-object
node: oop.values
type: qa
---
## Q
`Ticket` vs `Money` in a parking-lot design: which is an entity, which a value object, and how does equality differ between them?

## A
- `Ticket`: **entity** — has an id and a lifecycle; two tickets with identical fields are still different tickets. Equality = identity (compare ids).
- `Money(amount, currency)`: **value object** — immutable, no id; equality = structural (all fields), so `equals`/`hashCode` over fields.

Test: if you'd track it over time, it's an entity; if its attributes fully describe it, it's a value.
