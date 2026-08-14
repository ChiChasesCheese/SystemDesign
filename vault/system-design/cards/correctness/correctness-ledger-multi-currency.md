---
id: correctness-ledger-multi-currency
node: correctness.ledger
type: qa
---
## Q
How does a double-entry ledger handle a customer paying EUR 100 for a USD 108 charge — what does "entries sum to zero" mean with two currencies?

## A
The zero-sum invariant holds **per currency, never across currencies** — summing EUR against USD is meaningless. An FX conversion is modeled as **two balanced legs through conversion/nostro accounts**:

- EUR leg: customer −100 EUR → EUR conversion account +100 EUR (sums to 0 in EUR)
- USD leg: USD conversion account −108 USD → merchant +108 USD (sums to 0 in USD)

The conversion accounts absorb the position; revaluing them at market rate yields **FX gain/loss**, posted as its own entries. Store the **rate and both amounts** on the transaction, as integer **minor units with per-currency exponent** (JPY has 0 decimals, BHD 3) — never floats, never a single "converted amount" that loses the original.
