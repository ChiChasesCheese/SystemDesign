---
id: correctness-ledger-three-way-recon
node: correctness.ledger
type: qa
---
## Q
Payments teams reconcile three-way — internal ledger vs processor report vs bank statement. What does each pairwise match catch that two-way misses, and how are breaks classified?

## A
- **Ledger ↔ processor**: did every charge/refund we recorded happen, at the right amount/state? Catches lost webhooks, timeout-ambiguity bugs.
- **Processor ↔ bank**: did the processor's promised payouts (net of fees, chargebacks, reserves) actually **arrive as cash**? Two-way recon against the processor alone trusts their report — a processor error or insolvency shows up only at the bank.
- **Ledger ↔ bank**: closes the triangle so cash movements have ledger entries (fees, FX spreads you never booked).

Breaks are bucketed **timing** (in-flight, self-clears within a settlement window — age it, don't page) vs **true break** (investigate, then post an explicit **correcting entry**, never edit). Metrics: match rate and oldest unresolved break age ([[correctness-reconciliation]]).
