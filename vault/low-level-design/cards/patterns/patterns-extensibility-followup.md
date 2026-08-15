---
id: patterns-extensibility-followup
node: patterns.selection
type: qa
---
## Q
The classic LLD follow-up: "now add a new payment method / notification channel / pricing rule without touching existing code." What's the standard two-pattern answer, and what remains that you must still edit?

## A
**Strategy + factory (registry)** — the bread-and-butter OCP combo:

1. The varying behavior sits behind an interface (`PaymentMethod.charge()`); core flow depends only on it — closed for modification.
2. A **registry-based factory** maps a key to a `Supplier<PaymentMethod>`; adding UPI = one new class + one `register()` line (or an annotation/config entry).

Honest caveat to state: something must still change — the registration line and the composition root. OCP means changes are **additive and localized**, not zero. If variants also need new *data* fields end-to-end (request parsing, storage), no pattern hides that; say so.
