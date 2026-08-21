---
id: oop-default-methods
node: oop.interfaces
type: qa
---
## Q
What problem do interface default methods solve, and which two limits keep them from replacing abstract classes?

## A
They let a published interface **grow without breaking existing implementations** — add the method with a sensible default, implementers override at leisure.

Limits:
- **No instance state** — a default can only compute over the interface's own methods.
- **Diamond conflicts**: inherit the same default from two interfaces and the class must override explicitly (`InterfaceName.super.method()` to pick one).

## Q zh
Java 中的 default methods in interfaces（Java 8+）是什么，何时使用它们，何时避免？

## A zh
**Default methods**：接口中有实现的方法。所有实现者继承它，除非覆盖。

```java
interface Logger {
    void log(String msg);  // 必须实现
    default void info(String msg) { log("[INFO] " + msg); }  // 可选
}
```

**何时使用**：
- **添加新功能到现有接口**而不破坏实现者。例：`List` 获得 `sort()`、`removeIf()` 在 Java 8 中而不重写每个 ArrayList。
- **便利方法**：通用实现，可以覆盖以优化。

**何时避免**：
- **复杂逻辑**：接口不是基类。Default methods 应该简单、少数。
- **状态**：接口没有字段（除了常数）；default method 无法维护状态。
- **增加混淆**：太多 defaults 使继承链难以跟踪。

**经验法则**：default method 是一个**最后手段**，用于向后兼容性或简单便利。对于真正的共享逻辑，使用基类或组合。
