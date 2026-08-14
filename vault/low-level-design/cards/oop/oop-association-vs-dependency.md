---
id: oop-association-vs-dependency
node: oop.relationships
type: qa
---
## Q
`NotificationService` appears as a constructor-injected field of `OrderService` in one design, and as a parameter of `checkout(cart, notifier)` in another. Name each relationship and what the choice signals.

## A
- **Field** → association: structural, long-lived — "OrderService *has* a notifier."
- **Parameter/local** → dependency: transient uses-a, the weakest coupling in UML.

Signal: keep it a dependency while only one operation needs it; promote to an association when most methods do. Weakest workable relationship wins — it minimizes what a change can break.
