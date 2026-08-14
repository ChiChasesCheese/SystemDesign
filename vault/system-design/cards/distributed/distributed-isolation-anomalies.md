---
id: distributed-isolation-anomalies
node: distributed.transactions
type: qa
---
## Q
Map the standard isolation levels to the anomaly each one newly prevents, and name the anomaly snapshot isolation still allows.

## A
| Level | Newly prevents |
|---|---|
| Read committed | Dirty reads/writes |
| Repeatable read / **Snapshot isolation** | Non-repeatable (fuzzy) reads; SI gives a consistent point-in-time snapshot |
| Serializable | Everything, incl. **write skew** and phantoms |

**Snapshot isolation still allows write skew**: two transactions read the same snapshot, make disjoint writes based on it, and jointly violate an invariant. Practical notes: Postgres defaults to read committed; Postgres "repeatable read" *is* SI; its serializable is SSI (optimistic, aborts instead of locking).
