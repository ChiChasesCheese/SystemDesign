---
id: quality-seams-di
node: quality.testability
type: qa
---
## Q
What is a "seam" in the testability sense, and why does `new` inside a method destroy one?

## A
A **seam** (Feathers): a place where you can **change the program's behavior without editing the code under test** — i.e. where a collaborator can be swapped.

```java
class OrderService {
    void place(Order o) {
        var gw = new StripeGateway();   // no seam: test MUST hit Stripe
        ...
```

`new` (like a static call) hard-wires the concrete class at the use site — there is no point of substitution. Fix: accept the dependency through the **constructor** as an interface; the test passes a fake, production wiring happens at the composition root.

Rule of thumb: a class may `new` its own **value objects and data structures**, but anything with I/O, time, randomness, or its own behavior worth faking arrives injected.

## Q zh
什么是接缝？依赖注入如何使用接缝进行测试？

## A zh
接缝是代码中可以在不修改代码的情况下改变行为的地方。

**示例**（Michael Feathers）：
```java
// 接缝：通过继承修改行为
class Database {
    public Connection getConnection() {
        return DriverManager.getConnection(...);
    }
}

// 在测试中
class TestDatabase extends Database {
    @Override
    public Connection getConnection() {
        return mockConnection;
    }
}
```

**DI 作为接缝**：
```java
// 接缝：通过注入改变依赖
class UserService {
    private Database db;
    public UserService(Database db) { this.db = db; }
}

// 在测试中
new UserService(new MockDatabase());
```

其他接缝类型：
- 继承：重写方法
- 参数化：通过参数改变行为
- 配置：外部配置文件
- 全局变量：修改全局状态

DI 接缝很好，因为：
- 清晰明显
- 不需要继承
- 易于为多个依赖组合
