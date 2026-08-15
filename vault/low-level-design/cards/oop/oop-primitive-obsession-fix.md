---
id: oop-primitive-obsession-fix
node: oop.values
type: qa
---
## Q
```java
Ticket issue(String plate, String spotId, double amount, long enteredAt)
```
Name the smell, the failure it enables, and the fix — plus when the fix isn't worth it.

## A
**Primitive obsession.** Two same-typed parameters mean `issue(spotId, plate, ...)` compiles and fails silently at runtime; `double` for money invites rounding drift; validation ("plates are 7 chars") is re-done at every call site or nowhere.

Fix: small value types — `record Plate(String value)`, `Money`, `Instant` — validating in the constructor. Now the compiler rejects swapped arguments, the rule lives in one place, and the type name documents the unit (`Money`, not "amount in cents… probably").

Not worth it for a scalar used in one local computation, or a loop index. Trigger: the primitive **crosses a boundary** or carries a rule.
