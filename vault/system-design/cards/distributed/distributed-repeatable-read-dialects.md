---
id: distributed-repeatable-read-dialects
node: distributed.transactions.isolation
type: qa
---
## Q
Postgres and MySQL/InnoDB both offer `REPEATABLE READ`. Name three behavioral differences that bite in production.

## A
- **Phantoms**: InnoDB RR blocks them for *locking* reads via next-key (gap) locks; Postgres RR is snapshot isolation — plain reads never see phantoms, but nothing prevents a concurrent insert from breaking an invariant you checked (write skew stays possible in both).
- **Write-write conflicts**: Postgres RR **aborts** the second transaction with `could not serialize access due to concurrent update` (SQLSTATE 40001) — your app *must* have a retry loop. InnoDB instead **blocks on the row lock** and proceeds with the newly committed row, so you get no error and a possibly wrong result.
- **Locking reads see a different world**: in InnoDB, `SELECT ... FOR UPDATE` reads the **latest committed** row, not the transaction's snapshot — so a plain `SELECT` and a `SELECT ... FOR UPDATE` in the same transaction can return different values for the same row. Postgres keeps the snapshot and errors instead.

Takeaway for design docs: "repeatable read" names a *level*, not a behavior — always state the engine, and always write the retry loop.
