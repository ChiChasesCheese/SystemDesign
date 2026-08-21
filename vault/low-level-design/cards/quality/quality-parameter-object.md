---
id: quality-parameter-object
node: quality.refactoring
type: qa
---
## Q
Introduce parameter object: beyond shortening signatures, what two design payoffs justify it — and what's the anti-pattern version?

## A
```java
book(String from, String to, LocalDate out, LocalDate in, int guests)
→ book(Route route, StayPeriod period, int guests)
```

Payoffs beyond brevity:

- **A home for validation and behavior**: `StayPeriod` enforces `out < in` once in its constructor and grows methods like `nights()` — logic that was duplicated at every call site.
- **A stable seam**: adding a field changes the object, not every signature in the chain (kills a shotgun-surgery vector).

Anti-pattern: the grab-bag `RequestContext`/`Options` object that bundles *unrelated* params just to shorten a signature — that's a data clump faked, coupling every caller to every field. Group only what forms a real concept.

## Q zh
什么时候引入参数对象来简化签名？

## A zh
参数对象聚集相关的参数到一个对象中。

**触发器**：
```java
// 坏：长列表
createOrder(customerId, orderId, quantity, price, discount, taxRate,
            shippingAddress, billingAddress, paymentMethod);

// 好：参数对象
createOrder(order, customer, address, payment);
```

何时使用：
- 多个参数一起传递（它们相关）
- 多个方法使用相同的参数集
- 参数列表有 3+ 个相关参数

创建参数对象：
```java
class OrderDetails {
    int quantity;
    double price;
    double discount;
    double taxRate;
}

// 使用
createOrder(details, customer, payment);
```

优势：
- 更短的签名
- 参数的含义更清晰
- 易于添加新参数
- 可以向对象添加行为
