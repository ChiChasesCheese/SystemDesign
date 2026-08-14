---
id: correctness-saga-isolation
node: correctness.saga
type: qa
---
## Q
Sagas have ACD but no I. What anomalies does the missing isolation cause, and name the standard countermeasures.

## A
Each step commits locally, so **intermediate state is visible** before the saga's fate is known:

- **Dirty read**: another flow sees "payment captured" and ships — then the saga compensates. The world acted on state that got undone.
- **Lost update**: a concurrent writer modifies the row between a step and its compensation; the compensation stomps it.

Countermeasures (Garcia-Molina lineage):
- **Semantic lock**: write a `PENDING` marker; other transactions must skip/wait/reject pending resources.
- **Commutative updates** (± deltas) so interleavings don't matter.
- **Version check / reread** before compensating — compensate only what you actually did.
- **Reordering**: put the riskiest, non-compensatable step last (the pivot, [[correctness-saga-compensation-limits]]).
