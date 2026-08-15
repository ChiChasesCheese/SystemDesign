---
id: quality-guard-clauses
node: quality.refactoring
type: qa
---
## Q
Replace nested conditionals with guard clauses — show the transformation and state the rule about when arrow-code is a symptom of something else.

## A
```java
// before: happy path buried 3 levels deep
if (user != null) { if (user.isActive()) { if (order.isPaid()) { ship(order); } } }

// after: reject early, happy path flat at the bottom
if (user == null)      return;            // or throw
if (!user.isActive())  throw new InactiveUserException(user.id());
if (!order.isPaid())   throw new UnpaidOrderException(order.id());
ship(order);
```

Rule: guards handle the **abnormal** cases and exit immediately; the main flow reads unindented top-to-bottom. Multiple returns are fine — the single-exit rule predates garbage collection.

Symptom check: if the "guards" are checking the object's *lifecycle phase* (`if (status == PLACED) ... else if (status == SHIPPED)`), the real fix is the **state pattern**, not prettier conditionals.
