---
id: concurrency-cas-aba
node: concurrency.primitives
type: qa
---
## Q
A lock-free stack pops by `compareAndSet(top, A, A.next)`. The CAS succeeds — yet the stack is corrupted. What happened, and what's the fix?

## A
**ABA problem**: between reading `top == A` and the CAS, another thread popped A, popped B, and pushed A back (or a *recycled* node at A's address). The CAS sees "still A" and succeeds, but `A.next` now points at a node that's no longer in the stack.

- Fix: pair the pointer with a **version stamp** bumped on every update (`AtomicStampedReference`, tagged pointers) — the stale version fails the CAS.
- In GC languages the classic node-reuse variant is rarer (a reachable A can't be reallocated), but logical ABA on values still bites.

## Q zh
什么是 ABA 问题，为什么它在 CAS 中很危险？

## A zh
ABA 问题：
1. 线程读取值 A
2. 线程执行一些工作
3. 另一个线程将值改为 B，然后改回 A
4. 第一个线程的 CAS 成功，尽管发生了中间改变

例子（栈）：
```
Head -> [A] -> [B]
线程 1 想弹出 A，读取 head = A
线程 2 弹出 A，然后 push A 回来
线程 1 的 CAS(head, A, B) 成功
```

危险：
- 链表节点可能被重用或释放
- 计数器可能溢出
- 数据结构不变量被破坏

解决方案：
- 版本数：配对值和版本号（Versioned Reference）
- 垃圾收集语言有较少的 ABA 风险
