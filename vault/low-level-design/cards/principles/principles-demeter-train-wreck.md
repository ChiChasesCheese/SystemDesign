---
id: principles-demeter-train-wreck
node: principles.coupling
type: qa
---
## Q
```java
order.getCustomer().getWallet().debit(total);
```
Name the smell, the fix, and one chained-call style that is NOT a violation.

## A
**Law of Demeter violation** (train wreck): the caller is coupled to the internal structure of `Order`, `Customer`, *and* `Wallet` — reshaping any of them breaks distant code.

Fix: tell, don't ask — `customer.charge(total)`; the traversal moves inside the owner.

Not a violation: fluent builders and streams — each link returns the builder itself or a fresh value, not a reached-into internal.
