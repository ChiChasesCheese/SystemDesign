---
id: oop-bidirectional-association
node: oop.relationships
type: qa
---
## Q
`Order` holds `Customer`, and `Customer` holds `List<Order>`. What goes wrong with this bidirectional association, and what are the two disciplined options?

## A
Nothing keeps the two ends consistent: `order.setCustomer(c)` without `c.getOrders().add(order)` leaves a half-link, and every future mutation path must remember both. It also creates a **reference cycle** that breaks naive `equals`/`hashCode`/`toString` with infinite recursion.

- **Option A — one owning side**: only `Customer.addOrder(order)` exists; it sets the back-pointer itself and is the *only* mutator. `Order.setCustomer` is package-private or gone.
- **Option B — drop the back-pointer**: keep the single reference `Order → Customer` and answer "orders of a customer" from an index in the repository.

Default to B in a machine-coding round: a navigable link you can derive is cheaper than one you must maintain.
