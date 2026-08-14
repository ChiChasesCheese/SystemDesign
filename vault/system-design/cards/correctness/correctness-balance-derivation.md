---
id: correctness-balance-derivation
node: correctness.ledger
type: qa
---
## Q
If balance = SUM(entries), how do you make balance reads fast AND enforce "no overdraft" under concurrent spends?

## A
- **Fast reads**: periodic **snapshots/checkpoints** — persist balance as of entry N; current balance = snapshot + entries since N. The snapshot is a cache, always rebuildable from entries.
- **Overdraft enforcement** needs the check and the append to be atomic per account:
  - serialize per account (row lock on an account record, or single-writer per account partition), or
  - maintain a materialized balance updated **in the same transaction** as the entry insert, with a `CHECK (balance >= 0)` constraint.
- Distinguish **available vs posted** balance: holds/authorizations reduce available immediately, posted only on capture — most "double spend" bugs are really available-balance bugs.
