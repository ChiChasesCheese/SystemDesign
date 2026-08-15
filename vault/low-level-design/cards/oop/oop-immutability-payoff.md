---
id: oop-immutability-payoff
node: oop.values
type: qa
---
## Q
Name three concrete bug classes that making a type immutable eliminates.

## A
- **Aliasing bugs**: instances can be shared and returned freely — no defensive copies.
- **Corrupted collections**: safe as `HashMap`/`HashSet` keys, since `hashCode` cannot drift after insertion.
- **Data races**: read-only sharing across threads needs no synchronization.

"Mutation" becomes `money.plus(x)` returning a new instance — every invariant is checked once, in the constructor.
