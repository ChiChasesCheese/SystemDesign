---
id: oop-primitive-obsession-fix
node: oop.values
type: qa
---
## Q
```java
Ticket issue(String plate, String spotId, double amount, long enteredAt)
```
Name the smell, the failure it enables, and the fix — plus when the fix isn't worth it.

## A
**Primitive obsession.** Two same-typed parameters mean `issue(spotId, plate, ...)` compiles and fails silently at runtime; `double` for money invites rounding drift; validation ("plates are 7 chars") is re-done at every call site or nowhere.

Fix: small value types — `record Plate(String value)`, `Money`, `Instant` — validating in the constructor. Now the compiler rejects swapped arguments, the rule lives in one place, and the type name documents the unit (`Money`, not "amount in cents… probably").

Not worth it for a scalar used in one local computation, or a loop index. Trigger: the primitive **crosses a boundary** or carries a rule.

## Q zh
Primitive obsession 是什么代码气味，你如何修复它？

## A zh
**代码气味**：过度使用基本类型（int、String、double）表示域概念。

```java
class User {
    String email;  // 仅仅是一个 String？
    int age;       // 仅仅是一个 int？
    double salary; // 仅仅是一个 double？
}

// 到处都是验证：
if (email.contains("@")) { ... }
if (age > 18 && age < 65) { ... }
```

**修复**：将基本类型包装在值对象中：
```java
class Email {
    String value;
    Email(String v) {
        if (!v.contains("@")) throw new InvalidEmail();
        this.value = v;
    }
}
class Age {
    int value;
    Age(int a) { 
        if (a < 0 || a > 150) throw new InvalidAge();
        this.value = a;
    }
}

class User {
    Email email;
    Age age;
    // 验证已发生；不变量得到保证
}
```

**好处**：
- **自我验证对象**；无法创建无效的 Email。
- **清晰的意图**：`Email` 比 `String` 更清晰。
- **可重用的验证**。

**成本**：更多的类。但对大型域模型来说是值得的。
