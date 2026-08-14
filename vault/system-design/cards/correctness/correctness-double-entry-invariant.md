---
id: correctness-double-entry-invariant
node: correctness.ledger
type: qa
---
## Q
Why do payment systems store money as double-entry ledger entries instead of a `balance` column, and what invariant does every transaction maintain?

## A
Every transaction posts **two or more entries that sum to zero** (each debit matched by credits) — money is never created or destroyed, only moved between accounts, and external money movements are posted against internal counterpart accounts (e.g. a processor clearing account).

What this buys over a mutable balance column:
- **Auditability**: the balance is *derivable* from history; a bare column can't explain itself or be audited.
- **Error detection**: any bug that loses or invents money breaks the zero-sum invariant and is mechanically detectable.
- **Concurrency**: appending entries avoids read-modify-write races on a single balance row.
