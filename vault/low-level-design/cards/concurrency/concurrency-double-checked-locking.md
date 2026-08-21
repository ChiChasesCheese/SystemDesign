---
id: concurrency-double-checked-locking
node: concurrency.patterns
type: qa
---
## Q
```java
if (instance == null) {
    synchronized (Lock.class) {
        if (instance == null) instance = new Expensive();
    }
}
return instance;
```
What's still wrong with this double-checked locking, and what are two correct alternatives?

## A
Without `volatile`, the write `instance = new Expensive()` can be **reordered**: the reference is published before the constructor finishes. The *first* (unlocked) check can then see non-null and return a **partially constructed object**.

- Fix: declare `instance` **`volatile`** (volatile write→read forbids that reordering).
- Better in Java: the **holder-class idiom** (`static class H { static final Expensive I = new Expensive(); }`) — the classloader gives lazy init + safety with no locking code. An `enum` singleton works too.

## Q zh
什么是双重检查锁定，为什么它在单线程中很危险？

## A zh
模式：
```java
if (instance == null) {           // 第一次检查（无锁）
    synchronized(lock) {
        if (instance == null) {   // 第二次检查（有锁）
            instance = new Foo();
        }
    }
}
return instance;
```

目标：避免在 singleton 初始化后每次都获取锁。

危险：
- 在 Java 5 之前，`instance` 必须是 `volatile`，否则另一个线程可能看到部分初始化的对象
- 构造函数可能尚未完成，但 `instance != null` 已经为真
- 编译器重新排序可能会暴露这个

在现代 Java 中（5+）有效，如果：
- 字段是 `volatile`
- 或者使用更简单的方法（类初始化器、枚举）

一般来说：避免这个模式。改用 eager 初始化、类初始化器或 holder 模式。
