---
id: oop-interface-width-by-client
node: oop.interfaces
type: qa
---
## Q
In a 90-minute design, how do you decide where to split an interface — and what makes a split *too* fine?

## A
Split by **client**, not by method count. If every caller of a 4-method interface uses all 4, it is cohesive and splitting it just multiplies files. Split when one client uses a strict subset, e.g. the pricing engine only ever `read`s the catalog while the admin flow `write`s it → `CatalogReader` + `CatalogWriter`, one class implementing both.

- **Too fine**: one-method interfaces per client of the *same* role, so a single implementation is declared `implements A, B, C, D` and every wiring site names four types.
- Signal that you split correctly: some client's constructor got **narrower**, and its test fake got shorter.

The purpose is shrinking what a client can depend on, not shrinking the interface.

## Q zh
「interface 宽度应由客户端决定」是什么意思，你如何设计它？

## A zh
**意思**：不要创建一个拥有一切的大接口。设计小的、任务特定的接口，客户端**组合多个**来表达他们需要什么。

**不好**（宽接口）：
```java
interface PaymentGateway {
    void charge(Money);
    void refund(Money);
    void validateCard(String);
    void updateBillingAddress(Address);
    // ...20 多个方法
}
```

调用者需要 charge 和 refund；他们不应该被迫依赖 `validateCard` 或 `updateBillingAddress`。

**好**（瘦接口）：
```java
interface Charger { void charge(Money); }
interface Refundable { void refund(Money); }
interface Validator { void validate(String); }

class PayPal implements Charger, Refundable, Validator { }
```

调用者可以依赖**只**他们需要的：
```java
void processOrder(Order o, Charger c) { c.charge(o.total()); }
```

**好处**：
- 更少的耦合；更容易模拟测试。
- 更清晰的合同；每个接口有一个职责。
- 灵活的实现；对象可以选择性地实现角色。
