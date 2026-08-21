---
id: oop-enum-with-behavior
node: oop.values
type: qa
---
## Q
When does an enum with behavior (per-constant fields/methods) beat a class hierarchy for variants — and what signals you've outgrown the enum?

## A
- **Enum wins** for a small, closed variant set whose behavior is a pure function of the variant: `VehicleType.SUV.spotSize()` — constants and logic co-located, switches exhaustiveness-checked.
- **Outgrown** when variants need their own mutable state, substantially distinct logic, or open extension (new variants without editing the enum) → promote to interface + one class per variant (strategy).

## Q zh
Java enum 可以有方法。何时使用 enum with behavior，何时不应该？

## A zh
**Enum with behavior**：每个枚举常数可以有自己的实现。

```java
enum PaymentMethod {
    CREDIT {
        void charge(double amount) { /* 信用卡逻辑 */ }
    },
    BANK_TRANSFER {
        void charge(double amount) { /* 银行转账逻辑 */ }
    };
    abstract void charge(double amount);
}
```

**何时使用**：
- **小的、变体特定的行为**。例：每种支付方法的费用计算。
- **替代 switch/if 链**。清晰、类型安全。

**何时不应该**：
- **复杂逻辑**。Enum 不是为了包含方法的完整实现。
- **需要状态**。Enum 常数是共享的、不可变的；它们不能持有实例数据。
- **许多方法**。Enum 变得难以阅读。改用 Strategy pattern。

**经验法则**：≤2 个小方法 → enum behavior。更多 → strategy/polymorphism。
