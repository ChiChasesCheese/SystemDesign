---
id: concurrency-check-then-act
node: concurrency.model
type: qa
---
## Q
```java
if (!map.containsKey(key)) {
    map.put(key, createExpensive(key));
}
```
`map` is a `ConcurrentHashMap`, so every call is thread-safe. What's the bug, and what fixes it?

## A
**Check-then-act race**: two threads both pass the check before either puts, so both create the value and one overwrites the other. A *composite* operation is not atomic just because each step is.

- Fix: one atomic operation — `computeIfAbsent(key, k -> createExpensive(k))` (or `putIfAbsent`).
- Or hold one lock across **both** the check and the act.

`volatile` cannot help here — it fixes visibility, not atomicity.

## Q zh
什么是 check-then-act 竞态条件，如何修复它？

## A zh
模式：
```
if (cache.containsKey(key)) {        // 线程 1：检查
    // ... 线程 2 现在删除了 key
    return cache.get(key);            // 线程 1：行动 —— 获取 null！
}
```

TOCTOU 漏洞（检查时间到使用时间）：检查和使用之间有一个窗口。

修复：
1. **原子操作**：在一次锁定中检查和行动
   ```java
   synchronized(cache) {
       if (cache.containsKey(key)) {
           return cache.get(key);
       }
   }
   ```
2. **使用原子方法**：`putIfAbsent`, `getOrDefault` 等
3. **CAS 循环**：在检查失败时重试
