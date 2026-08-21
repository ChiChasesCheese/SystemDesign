---
id: quality-guard-clauses
node: quality.refactoring
type: qa
---
## Q
Replace nested conditionals with guard clauses — show the transformation and state the rule about when arrow-code is a symptom of something else.

## A
```java
// before: happy path buried 3 levels deep
if (user != null) { if (user.isActive()) { if (order.isPaid()) { ship(order); } } }

// after: reject early, happy path flat at the bottom
if (user == null)      return;            // or throw
if (!user.isActive())  throw new InactiveUserException(user.id());
if (!order.isPaid())   throw new UnpaidOrderException(order.id());
ship(order);
```

Rule: guards handle the **abnormal** cases and exit immediately; the main flow reads unindented top-to-bottom. Multiple returns are fine — the single-exit rule predates garbage collection.

Symptom check: if the "guards" are checking the object's *lifecycle phase* (`if (status == PLACED) ... else if (status == SHIPPED)`), the real fix is the **state pattern**, not prettier conditionals.

## Q zh
什么是卫语句（Guard Clauses），如何改进嵌套代码？

## A zh
卫语句是提前返回以处理边界情况。

**嵌套版本（不好）**：
```java
if (isValid(input)) {
    if (hasPermission(user)) {
        if (isAvailable(resource)) {
            return process(resource);
        }
    }
}
return null;
```

**卫语句版本（好）**：
```java
if (!isValid(input)) return null;
if (!hasPermission(user)) return null;
if (!isAvailable(resource)) return null;
return process(resource);
```

优势：
- 扁平、易读的流程
- 快速失败
- 减少认知负荷
- 边界情况集中在顶部

应用：
```java
// 嵌套 if-else 替换为
if (condition1) return result1;
if (condition2) return result2;
// ... 正常情况
return normalResult;
```
