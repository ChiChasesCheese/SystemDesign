---
id: quality-exception-design
node: quality.errors
type: qa
---
## Q
Designing exceptions in an LLD round: what makes a good domain exception, and what are the two handling sins interviewers flag?

## A
A good domain exception:

- Is **specific and semantic** — `SeatAlreadyLockedException(seatId)`, not `RuntimeException("error")`; it names the business rule violated and carries the data needed to react (retry? pick another seat?).
- Extends a small hierarchy (e.g. `BookingException`) so callers can catch at the granularity they care about.

The two sins:

- **Swallowing**: `catch (Exception e) {}` (or log-and-continue) — the system limps on in a corrupt state and the failure surfaces far from its cause.
- **Catch-and-rethrow bare**: wrapping without adding context, or catching just to log then rethrowing — the same error gets logged three times at three layers. Handle where you can act; otherwise let it propagate, translating only at layer boundaries (with the cause chained).

## Q zh
如何设计异常层次结构来改进错误处理？

## A zh
好的异常设计：

**1. 有意义的层次结构**：
```
Exception
├─ BusinessException
│  ├─ InsufficientFundsException
│  └─ UserNotFoundException
└─ TechnicalException
   ├─ DatabaseException
   └─ NetworkException
```

**2. 按恢复能力分类**：
- 可恢复的异常（重试、降级）
- 无法恢复的异常（快速失败、日志）

**3. 包含上下文**：
```java
new InsufficientFundsException(
    "Need $100 but have $50",
    accountId,
    required,
    available
);
```

**4. 避免过度异常**：
- 不要每个场景都有一个异常类
- 相关的异常应该共享一个基类

**5. 不要使用异常控制流**：
```java
// 错误
try {
    return list.get(index);
} catch (IndexOutOfBoundsException) {
    return null;
}
// 正确
if (index < list.size()) return list.get(index);
```
