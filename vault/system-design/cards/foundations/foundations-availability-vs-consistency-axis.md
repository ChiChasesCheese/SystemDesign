---
id: foundations-availability-vs-consistency-axis
node: foundations.tradeoffs
type: qa
---
## Q
For each, pick availability-first or consistency-first and justify in one line: (a) shopping-cart adds, (b) inventory decrement at checkout, (c) social-feed reads.

## A
- **(a) Cart adds — availability**: losing a sale to an error page costs more than merging a cart later (conflicts resolvable).
- **(b) Inventory at checkout — consistency**: overselling stock creates real-world cost; better to fail the request.
- **(c) Feed reads — availability**: a slightly stale feed is invisible to users; freshness is not a contract.

Pattern: choose per **operation**, not per system — the same product mixes both.
