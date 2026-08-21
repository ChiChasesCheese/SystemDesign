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

## Q zh
Anemic model 是什么陷阱，它如何违反 encapsulation？

## A zh
**Anemic model**：类只有数据（getters/setters）和没有业务逻辑。逻辑住在「Service」类中。

```java
class Order {
    int quantity; double price;
    int getQuantity() { return quantity; }
    void setQuantity(int q) { quantity = q; }
}
class OrderService {
    double calculateTotal(Order o) { return o.getQuantity() * o.getPrice(); }
}
```

**为什么这是贫血**：
- `Order` 知道计算自己的总数；`OrderService` 不应该。
- Getters/setters 暴露内部，无法保证不变量。例：`order.setQuantity(-5)` 不检查。
- 逻辑散落在许多 Services 中；难以维护。

**修复**（Rich model）：
```java
class Order {
    int quantity; double price;
    double getTotal() { return quantity * price; }
    void setQuantity(int q) { 
        if (q < 0) throw new IllegalArgumentException();
        this.quantity = q;
    }
}
```

**Encapsulation** = 数据 + 操纵它的逻辑，一起，保护不变量。
