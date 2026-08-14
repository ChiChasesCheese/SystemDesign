---
id: correctness-ledger-hot-accounts
node: correctness.ledger
type: qa
---
## Q
A platform fee account appears in every transaction — millions of entries/day against one ledger account. Why does it melt down, and how do you design around it?

## A
If posting maintains a materialized balance row, every transaction serializes on that **one row lock** — the fee account becomes a global throughput ceiling.

- **Don't maintain a synchronous balance** for it: append entries lock-free; derive the balance **asynchronously** (projection / snapshot + delta, [[correctness-balance-derivation]]). Legit because internal omnibus/fee accounts have no overdraft rule to enforce at write time.
- If a balance constraint IS required: **shard into sub-accounts** (fee-01..fee-32, hash-routed), each with its own serialization; report SUM across shards.
- Reserve synchronous check-and-post for accounts where overdraft actually matters (customer wallets).

Interview line: hot accounts are why "row-lock the balance" doesn't survive scale — pick per-account strategy by its invariant.
