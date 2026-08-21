---
id: oop-entity-vs-value-object
node: oop.values
type: qa
---
## Q
`Ticket` vs `Money` in a parking-lot design: which is an entity, which a value object, and how does equality differ between them?

## A
- `Ticket`: **entity** — has an id and a lifecycle; two tickets with identical fields are still different tickets. Equality = identity (compare ids).
- `Money(amount, currency)`: **value object** — immutable, no id; equality = structural (all fields), so `equals`/`hashCode` over fields.

Test: if you'd track it over time, it's an entity; if its attributes fully describe it, it's a value.

## Q zh
`Ticket` vs `Money` 在停车场设计中：哪个是 entity，哪个是 value object，equality 如何不同？

## A zh
- `Ticket`：**entity** ——有一个 id 和生命周期；两张字段相同的票仍然是不同的票。Equality = identity（比较 id）。
- `Money(amount, currency)`：**value object** ——不可变，没有 id；equality = structural（所有字段），所以 `equals`/`hashCode` 遍历字段。

**测试**：如果你会随时间跟踪它，它是一个 entity；如果它的属性完全描述它，它是一个 value object。

**代码后果**：
```java
Ticket t1 = new Ticket("T123");
Ticket t2 = new Ticket("T123");
t1.equals(t2)  // false ——不同的 id

Money m1 = new Money(100, "USD");
Money m2 = new Money(100, "USD");
m1.equals(m2)  // true ——相同的值
```
