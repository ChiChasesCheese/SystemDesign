---
id: quality-extract-method-triggers
node: quality.refactoring
type: qa
---
## Q
Extract method: what are the two classic triggers, and what does a well-composed method look like afterward?

## A
Triggers:

- **A comment announcing a block** — `// validate input` above six lines means the block wants to be `validateInput()`; the name replaces the comment.
- **A fragment you must study to see what it does** — or one you'd like to reuse or test in isolation.

Target shape (**composed method**): the body reads as a sequence of same-altitude, intention-named steps —

```java
void checkout(Cart c) {
    validate(c);
    var total = priceWithDiscounts(c);
    charge(c.customer(), total);
    emitReceipt(c, total);
}
```

Each step is one level of abstraction; details live one call down. When several extracted methods keep sharing the same parameters, that's the follow-on trigger for **extract class**.

## Q zh
什么时候应该提取一个方法？触发器是什么？

## A zh
提取方法（Extract Method）是最常见的重构。触发器：

**1. 注释解释代码**：
```java
// 计算利息
double interest = principal * rate * years / 100;
```
注释是信号；提取它：
```java
double interest = calculateInterest(principal, rate, years);
```

**2. 长方法**（>10-15 行）：
- 难以理解、测试和重用
- 提取逻辑块

**3. 循环内的代码**：
```java
for (Item item : items) {
    // ... 5 行处理逻辑
}
```
提取为 `processItem(item)`

**4. 重复代码**：
- 提取共同部分为方法

**5. 决策分支**：
```java
if (condition) {
    // ... 复杂逻辑
}
```
提取为 `handleSpecialCase()`

不要过度：
- 提取太多小方法导致碎片化
- 但一个大方法比许多单行方法更差
