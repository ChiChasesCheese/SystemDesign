---
id: quality-test-doubles
node: quality.testability
type: qa
---
## Q
Stub vs mock vs fake — separate the three doubles people actually confuse, by what the test asserts on.

## A
- **Stub**: returns canned answers so the code under test can run (`stubRates.get("EUR") → 1.1`). The test asserts on the **system's output/state** — the stub is scenery.
- **Mock**: records calls and the test **asserts on the interaction itself** — "`emailSender.send()` was called once with X." Use only when the side effect *is* the requirement; over-mocking welds tests to implementation details.
- **Fake**: a real, working, lightweight implementation (in-memory repository, embedded queue). Behaves properly across many calls, so it suits whole-flow tests without a DB.

(Remaining taxonomy: **dummy** — passed but never used; **spy** — a stub that also records, letting you assert afterward instead of setting expectations upfront.)

## Q zh
测试替身的类型是什么？何时使用每个？

## A zh
测试替身是真实对象的替代品用于测试。

**Stub（存根）**：
- 返回预配置的值
- 用途：测试在不同数据下的行为
```java
stub.getUserById(1).thenReturn(new User("Bob"));
```

**Mock（模拟）**：
- 验证调用（是否被调用，参数是什么）
- 用途：测试对象与其依赖的交互
```java
verify(logger).log("message");
```

**Fake（假）**：
- 真实实现，但简化（如内存数据库）
```java
new InMemoryDatabase()  // 真实的 DB，但在内存中
```

**Spy（探针）**：
- 包装真实对象，记录调用
- 用途：测试真实行为加上交互验证

什么时候用什么：
- 需要控制返回值 → Stub
- 需要验证交互 → Mock
- 需要实现 → Fake
- 需要两者 → Spy
