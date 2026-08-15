---
id: structure-state-enum-vs-boolean-soup
node: structure.state-machines
type: qa
---
## Q
An `Order` has `isPaid`, `isShipped`, `isCancelled` booleans. Why does this rot as requirements grow, and what does replacing them with a state enum buy you concretely?

## A
Three booleans encode **2³ = 8 combinations** but only ~4 are legal — nothing stops `isShipped && isCancelled`, and every method starts with fragile flag-combination checks scattered everywhere.

A single `enum State { CREATED, PAID, SHIPPED, CANCELLED }` buys:
- **Illegal states are unrepresentable** — one field, one value.
- Transitions become **checkable in one place** instead of implied by flag flips.
- New states (REFUNDED) are an enum addition + transition entries, and `switch` exhaustiveness finds every spot to update.
