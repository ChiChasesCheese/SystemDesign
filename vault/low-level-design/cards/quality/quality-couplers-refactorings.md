---
id: quality-couplers-refactorings
node: quality.smells
type: qa
---
## Q
Diagnose and fix each coupler: feature envy, message chains, inappropriate intimacy, middle man.

## A
- **Feature envy** — a method uses another object's data more than its own (`order.getCustomer().getAddress().format()` logic living in `InvoicePrinter`). Fix: **move method** to where the data lives; behavior belongs with state.
- **Message chains** — `a.getB().getC().doIt()` couples the caller to the whole navigation path (Law of Demeter violation). Fix: **hide delegate** — ask the first object to do it (`a.doIt()`).
- **Inappropriate intimacy** — two classes poke each other's internals. Fix: move method/field to concentrate the interaction in one class, or extract the shared part.
- **Middle man** — a class that only forwards calls. Fix: **remove middle man**, talk to the target directly. (Note: it's the *over-applied* cure for message chains — the two smells pull in opposite directions, so aim between.)

## Q zh
什么是耦合者（couplers），如何识别和重构它们？

## A zh
耦合者是过度连接事物的代码异味。

**功能嫉妒**：
- 一个方法使用来自其他类的更多方法而不是自己的
```java
customer.setAge(ageCalculator.calculate(customer.getBirthDate()));
```
- 重构：将 setAge 逻辑移到 Customer 中

**不适当的亲密**：
- 一个类依赖于其他类的内部
```java
person.data[0] = 123;  // 直接访问私有数据
```
- 重构：提供公共 API，隐藏实现

**消息链**：
- `a.getB().getC().getD().doIt()`
- 重构：引入委托方法

**中间人**：
- 一个类只是转发所有调用到另一个类
```java
public String getName() { return delegate.getName(); }
```
- 重构：直接使用委托对象或删除中间人
