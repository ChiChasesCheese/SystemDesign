---
id: oop-encapsulation-anemic-model
node: oop.pillars
type: qa
---
## Q
```java
ticket.setStatus(PAID);
ticket.setPaidAt(now);
wallet.setBalance(wallet.getBalance() - fee);
```
Name the smell and the refactor.

## A
**Anemic domain model** — encapsulation broken by getter/setter pairs: the invariants (paid ⇒ `paidAt` set; balance never negative) must be re-implemented by every caller.

Refactor to tell-don't-ask: `ticket.markPaid(now)`, `wallet.debit(fee)`. The operation moves to the data owner, which validates the transition once and can reject illegal states.
