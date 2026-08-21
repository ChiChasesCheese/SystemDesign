---
id: quality-validate-boundary
node: quality.errors
type: qa
---
## Q
"Validate at the boundary" — what does it mean structurally, and how do value objects make re-validation unnecessary?

## A
Structurally: all input crosses **one checkpoint** (API handler, command constructor) where it's checked and **converted into types that can't hold invalid data**. Inside that boundary, code trusts its inputs — no defensive re-checking scattered through every layer.

The mechanism is **"parse, don't validate"**: instead of passing a `String` plus the knowledge that someone once checked it, construct `Email.of(raw)` which **throws on bad input and cannot exist invalid**. The type system then carries the proof everywhere the value goes.

```java
record Email(String value) {
    Email { if (!value.matches(".+@.+")) throw new InvalidEmailException(value); }
}
```

Interview payoff: "invalid states are unrepresentable" — invariants live in constructors, not in every method that touches the data.

## Q zh
为什么在方法边界处验证输入很重要？

## A zh
边界验证是防御编程的首道防线。

**为什么在边界处**：
```java
public void setAge(int age) {
    if (age < 0) throw new IllegalArgumentException();
    this.age = age;  // 现在我们知道 age >= 0
}
```

优势：
- **快速失败**：在进入之前发现错误
- **清晰的契约**：方法声明它期望什么
- **防止后续的 null 检查**：内部代码不需要防御
- **不变量维护**：确保对象始终处于有效状态

何时验证：
- **公共方法**：总是（调用者是陌生人）
- **私有方法**：较少（内部调用者受信任）
- **参数**：始终
- **返回值**（如果可能）：验证结果有效

验证什么：
```java
public void setName(String name) {
    if (name == null) throw new NullPointerException("name required");
    if (name.trim().isEmpty()) throw new IllegalArgumentException("name empty");
    this.name = name;
}
```

不验证是什么时候：
- 对性能敏感且已验证
- 内部代码路径已被充分测试
