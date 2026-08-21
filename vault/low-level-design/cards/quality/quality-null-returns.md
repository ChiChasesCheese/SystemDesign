---
id: quality-null-returns
node: quality.errors
type: qa
---
## Q
Your repository's `findById` can miss. Rank the return-type options for "not found" and say when absence should be an exception instead.

## A
- **Best: `Optional<Order>`** — absence is in the signature; the compiler makes every caller decide (`orElseThrow`, `map`, default). For collections, return an **empty collection**, never null.
- **Acceptable: null object** (`GuestUser.ANONYMOUS`) — only when there's a genuinely sensible do-nothing/default behavior; a null object that silently absorbs real work hides bugs.
- **Worst: return `null`** — moves the check to every caller, and the NPE fires far from the cause.

Absence should **throw** when it violates an invariant — the caller holds an id the system itself issued (`getById` on a just-created order), so "missing" means corruption, not a normal outcome. Pattern: offer `findById → Optional` and `getById → throws NotFoundException`, and let callers state their expectation.

## Q zh
为什么返回 null 有问题，更好的替代品是什么？

## A zh
返回 null 的问题：

**1. NullPointerException**：
```java
User user = findUser(id);
user.getName();  // 如果 user 是 null，崩溃
```

**2. 意图不清楚**：
- 方法返回什么时 null 意味着什么？
- 调用者必须检查；容易忘记

**3. 级联检查**：
```java
if (user != null) {
    if (user.getAddress() != null) {
        if (user.getAddress().getCity() != null) {
            // ... 金字塔末日
        }
    }
}
```

替代品：

**1. Optional<T>**（Java）：
```java
Optional<User> user = findUser(id);
user.ifPresent(u -> System.out.println(u.getName()));
```

**2. 异常**（对真正的错误）：
```java
User user = findUserOrThrow(id);  // 不存在时抛出
```

**3. 默认值**：
```java
User user = findUser(id).orElse(new GuestUser());
```

**4. 空对象模式**：
```java
return new NullUser();  // 有空实现的用户对象
```
