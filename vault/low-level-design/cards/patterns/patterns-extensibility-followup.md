---
id: patterns-extensibility-followup
node: patterns.selection
type: qa
---
## Q
The classic LLD follow-up: "now add a new payment method / notification channel / pricing rule without touching existing code." What's the standard two-pattern answer, and what remains that you must still edit?

## A
**Strategy + factory (registry)** — the bread-and-butter OCP combo:

1. The varying behavior sits behind an interface (`PaymentMethod.charge()`); core flow depends only on it — closed for modification.
2. A **registry-based factory** maps a key to a `Supplier<PaymentMethod>`; adding UPI = one new class + one `register()` line (or an annotation/config entry).

Honest caveat to state: something must still change — the registration line and the composition root. OCP means changes are **additive and localized**, not zero. If variants also need new *data* fields end-to-end (request parsing, storage), no pattern hides that; say so.

## Q zh
设计说「通过 Plugin 扩展系统」。Plugin 是什么模式，你为它准备什么接口合同？

## A zh
Plugin 是**工厂模式 + 反射/发现**的应用。系统定义一个接口（如 `PluginProvider`），然后：

```java
interface PluginProvider { 
    String name();
    Component create(Config);
}
```

**合同**：
- 每个 plugin 必须声明它的**依赖和版本兼容性**。
- Plugin 只能改变它自己的行为；不能改变系统核心接口或其他 plugin 的行为。
- 系统通过**显式发现**（注解扫描、配置文件列表）而不是**类路径扫描**来加载 plugin（可预测）。
- 版本冲突、加载顺序和配置冲突有显式错误处理。
