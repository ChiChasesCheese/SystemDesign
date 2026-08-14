---
id: distributed-write-skew
node: distributed.transactions
type: qa
---
## Q
On-call rule: at least one doctor must stay on shift. Two doctors, in concurrent transactions, each check "≥2 on call" and sign themselves off. Both commit under snapshot isolation. Name the anomaly and two fixes.

## A
**Write skew**: each transaction's read set was invalidated by the *other's* write, but since they wrote **different rows**, SI's write-write conflict detection sees nothing.

- **Serializable isolation** (e.g. Postgres SSI): tracks read-write dependencies and aborts one transaction — then retry.
- **Materialize the conflict / lock the invariant**: `SELECT ... FOR UPDATE` on the rows read (or a single row representing the shift), forcing the transactions to serialize on a common lock.

Pattern to recognize: *read a predicate, write based on it* — always suspect write skew under SI.
