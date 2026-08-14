---
id: correctness-ledger-immutability
node: correctness.ledger
type: qa
---
## Q
A posted ledger entry turns out to be wrong (wrong amount, wrong account). What does a payments-grade ledger do, and what is banned?

## A
**Banned**: `UPDATE` or `DELETE` on posted entries. The ledger is append-only; history that auditors and past reports saw must never change.

Correct move: post a **reversal entry** (equal and opposite) and then the corrected entry — three entries total, all preserved, each linking to the original for traceability. The current balance is right *and* the mistake remains visible.

Enforce it structurally: no update/delete grants on the entries table, and corrections go through the same posting API (idempotent, zero-sum-checked) as normal transactions.
