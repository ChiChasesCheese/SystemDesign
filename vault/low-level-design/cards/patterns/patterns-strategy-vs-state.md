---
id: patterns-strategy-vs-state
node: patterns.behavioral
type: qa
---
## Q
Strategy and state have the same UML — context delegates to a swappable interface. What are the two behavioral differences?

## A
- **Who switches, and when**: with **strategy**, the *client* picks one algorithm up front (pricing rule, sort order) and it rarely changes mid-flight; strategies don't know about each other. With **state**, the *states themselves* (or the context) drive transitions at runtime — `PaidState` decides the order moves to `ShippedState` — so states know their successors.
- **What the abstraction means**: strategies are **interchangeable ways to do the same thing** (any one is valid); states make the object **behave differently per lifecycle phase**, and most transitions between them are illegal.

Tell: requirements say "support multiple X algorithms" → strategy; "an order/elevator/game can be in phases with different allowed actions" → state.
