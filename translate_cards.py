#!/usr/bin/env python3
"""
Translate flashcard files from English to Chinese.
Follows translation-spec.md rules strictly.
"""

import os
import re
import yaml
from pathlib import Path

# Map of card IDs to Chinese translations
TRANSLATIONS = {
    # PRINCIPLES - COHESION AND COUPLING
    "principles-cohesion-signal": {
        "type": "qa",
        "q": "单个类内部低内聚的表现是什么，标准的重构方法是什么？",
        "a": """信号：
- 字段聚集成不相交的组，每组被不同的方法子集使用
- 名字需要加上 "Manager"、"Util" 或 "Helper" 来涵盖所有东西
- 方法之间既不相互调用，也不共享状态

重构：沿着字段使用的聚类进行 **提取类（Extract Class）**，让每个类的方法使用大部分的字段。类内部的高内聚是使类之间的低耦合成为可能的前提。"""
    },
    "principles-delegation-boilerplate": {
        "type": "qa",
        "q": "什么时候你会看到委托而不是继承，什么时候 Extract Class 会引入样板代码？",
        "a": """当 A 委托给 B 时——B 的公共接口完全被 A "代理" 到那些委托方法中。这不是组合，而是代理对象，通常是因为继承会带来不必要的复杂性或紧耦合。

Extract Class 可能会导致样板代码，当：
- 新类只是持有从原始类转移的字段，但没有实现新的行为
- 原始类需要获取器和设置器来访问新类的字段
"""
    },
    "principles-demeter-train-wreck": {
        "type": "qa",
        "q": "什么是 Demeter 法则的违反？为什么 train wreck 是个名字？",
        "a": """Demeter 法则说你只应该和你的 "朋友" 交流——方法只应该调用：
- 它自己的类中的方法
- 参数对象的方法
- 本地创建或获取的对象的方法

Train wreck（火车碰撞）是因为每个点像一节火车车厢：`a.getB().getC().getD().doIt()`。每个点都是一个对象，链在一起像是无控制地滑动。这暴露了中间对象的内部结构。"""
    },
    "principles-di-seam": {
        "type": "qa",
        "q": "依赖注入如何充当一个接缝？它与工厂或服务定位器有什么区别？",
        "a": """DI 是一个接缝，因为它让你在不改变代码的情况下在真实和测试依赖之间切换。调用者在构造函数中接收依赖，而不是创建它们，所以测试可以传入模拟对象。

区别：
- 工厂：调用者仍然要求工厂创建依赖。仍然是隐式的依赖。
- 服务定位器：调用者要求定位器查找依赖。同样隐式。
- DI：调用者接收它需要的东西。依赖是显式的，在构造函数签名中可见。"""
    },
    "principles-dip-trigger": {
        "type": "qa",
        "q": "什么时候你知道有些代码需要依赖反转？",
        "a": """触发器：
- 你看到一个高级模块（业务逻辑）导入一个低级模块（基础设施、框架）
- 所有的变化都强制改变依赖于它的所有东西
- 你在测试中需要做很多工作来隔离一个类：创建真实的数据库连接、调用外部 API 等。
"""
    },
    "principles-dry-limit": {
        "type": "qa",
        "q": "什么时候应该因为代码重复而不是因为不是 DRY 而违反 DRY 原则？",
        "a": """两个代码片段看起来相似，但：
- 它们由于不同的原因而改变（它们有不同的 "为什么")
- 它们会在不同的时间演变成不同的方向
- 将它们提取到单个位置会创建一个虚假的抽象，实际上约束了它们各自的演变

一个常见的例子：两个不同的验证规则可能从相同的条件开始，但由于业务需求，它们最终会分支出去。"湿" 代码在这里会更好。"""
    },
    "principles-hierarchy-explosion": {
        "type": "qa",
        "q": "当你在继承中添加第二维变化时会发生什么，为什么是个问题？",
        "a": """你最终得到类爆炸：
```
Animal
  ├─ Dog
  │  ├─ ServiceDog (does service work)
  │  └─ PetDog (doesn't do service work)
  └─ Cat
     ├─ ServiceCat
     └─ PetCat
```

问题：
- N 维变化导致 M^N 个类
- 每个新概念都强制修改层次结构
- 违反开-闭原则：要添加新的维度，你必须修改现有的类

解决方案：使用组合或特性而不是继承的额外级别。"""
    },
    "principles-isp-trigger": {
        "type": "qa",
        "q": "什么时候你知道你的接口违反了接口分离原则？",
        "a": """触发器：
- 实现者强制实现它们不使用的方法
- 调用者只调用接口的一部分
- 接口名中有多个概念："Read-Write-Lock"、"Serializable-Comparable"
- 一个类有多个客户端需要不同的操作子集

症状：
- 模拟或存根会伪造不用的方法
- 测试中对实现者不相关的方法进行设置"""
    },
    "principles-lsp-signals": {
        "type": "qa",
        "q": "什么时候你知道一个子类违反了 Liskov 替换原则？",
        "a": """信号：
- 调用者必须检查运行时类型才能安全调用方法：`if (x instanceof Circle) ...`
- 子类抛出基类不抛出的异常
- 子类削弱前置条件或强化后置条件（相对于基类）
- 子类中的方法对调用者的期望没有满足（比如缓存的实现阻止重新计算，但调用者期望新值）
"""
    },
    "principles-mixins-vs-delegation": {
        "type": "qa",
        "q": "什么时候使用 mixin 而不是委托？它们的权衡是什么？",
        "a": """Mixin（通过继承或组合混入行为）：
- 优势：不需要显式委托调用；方法自动可用
- 劣势：创建隐含的依赖；多个 mixin 可能会冲突；难以测试隔离

委托（显式转发）：
- 优势：清晰明了哪些调用被转发；易于单独测试；灵活替换
- 劣势：需要显式转发方法（样板代码）

经验法则：如果你是在组织行为（多个概念），使用委托。如果你只是混入一个通用的、独立的功能，可以考虑 mixin。"""
    },
    "principles-ocp-trigger": {
        "type": "qa",
        "q": "什么时候你知道你的代码对修改不是开放的？",
        "a": """触发器：
- 每次添加新的变化（新的支付方式、新的报告类型、新的日志级别），你都修改现有的类
- 一个 if-else 或 switch 在分派新类型，每种类型都需要修改
- 测试新功能需要修改现有代码，这意味着回归风险

解决方案通常涉及：
- 多态性：让子类实现扩展点
- 策略模式：注入新的行为对象
- 尽可能让变化通过参数或配置进行，而不是代码"""
    },
    "principles-shallow-abstraction-test": {
        "type": "qa",
        "q": "一个抽象何时太浅了？如何测试抽象是否有价值？",
        "a": """一个抽象太浅了，当它：
- 只是为一个实现提供一个不同的名称（例如：`interface Logger { void log(String msg); }` 对 `System.out.println` 的 15 行包装）
- 没有隐藏任何复杂性或做任何有趣的事情
- 实现是微不足道的，抽象不能处理变化

测试抽象是否有价值：
1. 你能实现 2-3 个不同的、有意义的版本吗？（如果不能，太浅了）
2. 能否在不更改调用者的情况下切换实现？
3. 它是否降低了调用者代码的复杂性或提高了理解性？"""
    },
    "principles-speculative-generality": {
        "type": "qa",
        "q": "什么是投机泛化，为什么它是问题？",
        "a": """投机泛化是添加一个你认为将来可能需要的功能，但现在不需要。看起来像：
- 一个接口有操作，但只有一个实现者
- 一个参数存在但从未被使用
- 抽象层数比实际需要的多
- "我们可能想要这个"代码在 util 类中

问题：
- 增加复杂性，没有立即的益处
- 你猜测错了；需要的功能与你抽象的不一样
- 难以测试和维护过度工程的代码

解决方案：YAGNI（你不需要它）。等到有第二个实现者或实际的需求才进行抽象。"""
    },
    "principles-stable-dependencies": {
        "type": "cloze",
        "zh": "耦合有方向。**传入耦合（Afferent Coupling）** Ca = {{c1::依赖这个组件的类}}（传入的，难以改变）；**传出耦合（Efferent Coupling）** Ce = {{c2::这个组件依赖的类}}（传出的，易于改变）。不稳定性 I = {{c3::Ce / (Ca + Ce)}}，所以 I = 0 是最大稳定，I = 1 是最大不稳定。**稳定依赖原则**：依赖应该指向{{c4::更稳定的组件}}——易变代码可以依赖稳定代码，但反之不行。当箭头必须反向时，修复方法是{{c5::由依赖者（更高层）一方定义接口}}，这样易变的细节依赖于它。"
    },
    "principles-stack-extends-arraylist": {
        "type": "qa",
        "q": "为什么 Stack 扩展 ArrayList 是一个设计错误？",
        "a": """因为 Stack 是一个 LIFO（后进先出）数据结构，但 ArrayList 是一个 indexed、可随机访问的列表。

如果 Stack 扩展 ArrayList：
- 调用者可以调用 `get(0)`、`add(0, item)` 或 `remove(5)`
- 这违反了 Liskov 替换原则：Stack 的调用者期望 LIFO 行为，但可以进行不尊重 LIFO 的操作
- Stack 继承了所有不相关的方法：`indexOf`、`replaceAll` 等。

正确的设计：Stack 组合 ArrayList 或 LinkedList，只暴露 push、pop、peek 方法。这是组合而不是继承。"""
    },
    "principles-temporal-coupling": {
        "type": "qa",
        "q": "什么是时间耦合，为什么它是个问题？",
        "a": """时间耦合发生在方法必须以特定顺序调用时，但代码没有强制这个顺序。

例子：
```
user.setEmail(new_email);  // 必须在 validate 之前
user.validate();
user.save();
```

问题：
- 顺序对调用者来说不是显而易见的
- 没有编译时检查；错误直到运行时才显现
- 难以重构或并行化

解决方案：
- 创建一个方法强制顺序：`user.updateAndValidateAndSave(new_email)`
- 使用生成器（Builder）分阶段进行
- 使用返回"下一步"对象的 API 指导调用者"""
    },
    "principles-unwinding-wrong-abstraction": {
        "type": "qa",
        "q": "当你意识到一个抽象是错误的，为什么解开它而不是改进它？",
        "a": """当一个抽象错误时，尝试改进它通常会导致更多的复杂性。更好的方法：

1. 复制代码回到每个调用者（是的，重新引入重复）
2. 现在在隔离的上下文中优化每个版本
3. 一旦它们稳定并且真正的模式出现，提取正确的抽象

这违反了 DRY，但：
- 一个坏的抽象比重复更糟
- 重复暴露了真正的差异
- 改进一个坏的抽象很难；更好地开始就是正确的

这来自 Sandi Metz 的 "All the Little Things" 演讲。"""
    },
    "principles-when-inherit": {
        "type": "qa",
        "q": "什么时候继承是正确的选择？",
        "a": """继承合适的场景：
- IS-A 关系是真实的且稳定：`Dog IS-A Animal`
- 子类需要重写行为（模板方法、策略模式风格）
- 框架要求它（如 JUnit 的 TestCase）

继承不适合：
- 代码重用；使用组合
- 不同的对象类型（如 ArrayList 和 Stack）
- 你只想从一个类中获取一些方法

经验法则：如果你不能用一句话解释"为什么 B 是 A"，那就使用组合。"""
    },
    "principles-yagni-in-round": {
        "type": "qa",
        "q": "在迭代开发中应用 YAGNI 是什么样子？",
        "a": """YAGNI（你不需要它）意味着不要添加你现在不需要的功能。在迭代中：

第一次迭代：
- 实现最小的东西来传递测试
- 不要"预计"分支、扩展、配置

第二次迭代：
- 需要第二个实现者或变化吗？现在进行抽象
- 发现重复的代码吗？现在提取它

这与投机泛化相反。结果代码更简单、更易理解、更快交付。反讽刺的是，YAGNI 导致比过度工程的代码更长久的架构。"""
    },

    # CONCURRENCY
    "concurrency-bounded-queue-invariants": {
        "type": "qa",
        "q": "有界队列在并发中的不变量是什么？关键的临界区是什么？",
        "a": """不变量：
- `size >= 0` 且 `size <= capacity`
- 如果 `size == 0`，消费者会阻塞
- 如果 `size == capacity`，生产者会阻塞

关键的临界区：
- 锁保护：`size`、`head`、`tail` 指针（或数组索引）
- 入队操作：增加大小，获取下一个写位置
- 出队操作：减少大小，获取下一个读位置

条件变量：
- `notEmpty`：当大小从 0 变为 1 时发出信号（通知等待的消费者）
- `notFull`：当大小从 capacity 变为 capacity-1 时发出信号（通知等待的生产者）"""
    },
    "concurrency-cas-aba": {
        "type": "qa",
        "q": "什么是 ABA 问题，为什么它在 CAS 中很危险？",
        "a": """ABA 问题：
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
- 垃圾收集语言有较少的 ABA 风险"""
    },
    "concurrency-check-then-act": {
        "type": "qa",
        "q": "什么是 check-then-act 竞态条件，如何修复它？",
        "a": """模式：
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
3. **CAS 循环**：在检查失败时重试"""
    },
    "concurrency-condvar-wait-loop": {
        "type": "qa",
        "q": "为什么条件变量 wait 必须在循环中？虚假唤醒是什么？",
        "a": """条件变量 wait 必须在循环中（Spurious Wakeups）：

```java
while (!condition) {
    condVar.wait();  // 不要 if (condition)
}
```

原因：
1. **虚假唤醒**：OS 有时在没有相应的 notify 时唤醒线程
2. **竞态条件**：另一个线程可能在 notify 和 wait 方法返回之间改变条件
3. **多个消费者**：一个 notify 可能唤醒多个等待线程，但只有一个应该继续

例子：
```
消费者 1 等待
消费者 2 等待
生产者发送一个项目，notify 一个
消费者 1 唤醒，但... 队列仍然是空的！（消费者 2 已经取走了它）
```

所以总是检查条件后唤醒。"""
    },
    "concurrency-data-race-definition": {
        "type": "cloze",
        "zh": "**数据竞赛**（Data Race）需要{{c1::两个线程访问同一个内存位置，至少一个访问是写操作，且访问之间没有同步}}。不同于竞态条件（Race Condition），后者是程序的行为取决于事件时序。数据竞赛是低级概念；竞态条件是高级错误。修复所有数据竞赛不一定能消除竞态条件。"
    },
    "concurrency-deadlock-detect-vs-prevent": {
        "type": "qa",
        "q": "Deadlock 检测和预防之间有什么权衡？",
        "a": """**Deadlock 预防**（在死锁发生前阻止）：
- 打破四个必要条件之一（锁定顺序、超时等）
- 成本：开销（超时检查）、性能（严格的锁定规则）
- 优势：避免死锁开销

**Deadlock 检测**（等待并响应）：
- 让死锁发生，然后检测
- 成本：等待时间，然后恢复（通常重启或回滚）
- 优势：允许更灵活的锁定模式

实践中：
- 大多数应用使用预防（超时、一致的锁定顺序）
- 数据库系统常使用检测和事务回滚"""
    },
    "concurrency-deadlock-four-conditions": {
        "type": "cloze",
        "zh": "死锁需要 **所有四个** Coffman 条件：{{c1::互斥}}（资源不可共享）、{{c2::保持和等待}}（一个线程持有一个锁同时等待另一个）、{{c3::无抢占}}（锁不能被强制夺走）、{{c4::循环等待}}（线程等待的循环链）。打破任何一个都能防止死锁——**全局锁获取顺序**打破{{c5::循环等待}}，这就是为什么锁定顺序是标准的面试解决方案；带超时的 `tryLock` 打破保持-等待。"
    },
    "concurrency-double-checked-locking": {
        "type": "qa",
        "q": "什么是双重检查锁定，为什么它在单线程中很危险？",
        "a": """模式：
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

一般来说：避免这个模式。改用 eager 初始化、类初始化器或 holder 模式。"""
    },
    "concurrency-happens-before-edges": {
        "type": "cloze",
        "zh": "实际采访中用到的 happens-before 边：释放 mutex → 稍后{{c1::锁定同一 mutex}}；volatile 写 → 稍后{{c2::读相同的 volatile 变量}}；`Thread.start()` 之前的所有东西 → {{c3::启动的线程的第一个动作}}；线程的最后一个动作 → {{c4::`join()` 在等待线程中返回}}。如果两个访问没有被这样的链连接，读取可能看到陈旧或损坏的值。"
    },
    "concurrency-livelock-vs-starvation": {
        "type": "qa",
        "q": "livelock 和 starvation 之间有什么区别？",
        "a": """**Starvation**（饥饿）：
- 一个线程永远无法获得它需要的资源
- 例子：高优先级线程不断运行，低优先级线程从不获得 CPU 时间
- 线程被阻塞，等待变得可用的东西

**Livelock**（活锁）：
- 线程不断改变状态，但没有取得进展
- 例子：两个线程交替放弃资源尝试，进入无限重试循环
```
线程 1：检查资源，它忙，退出
线程 2：检查资源，它忙，退出
线程 1：重试...
```
- 线程在运行，但没有做有用的工作

相似之处：两者都导致缺乏进展。
区别：starvation 是被动等待；livelock 是活跃的无用工作。"""
    },
    "concurrency-lock-free-trap": {
        "type": "qa",
        "q": "为什么无锁代码陷阱会导致竞态条件？",
        "a": """无锁代码的常见错误：

```java
// 错误：两个原子操作不是原子的
if (queue.isEmpty()) {      // CAS 或原子检查
    queue.add(item);        // 单独的 CAS —— 在两者之间窗口！
}
```

竞态条件：
- 线程 1 检查 isEmpty() = true
- 线程 2 添加一个项目
- 线程 1 仍然添加 —— 队列现在有 2 个项目

修复：
- 使用原子的组合操作：`putIfAbsent`、`offer`
- 或在循环中进行 CAS 重试
- 或使用适当的同步

无锁代码看起来更快，但需要深入理解内存顺序。通常不值得。"""
    },
    "concurrency-lock-ordering-transfer": {
        "type": "qa",
        "q": "锁定顺序如何防止死锁？什么是锁定转移？",
        "a": """**锁定顺序**（Consistent Lock Ordering）：
- 所有线程以相同的顺序获取锁
```
线程 1：获取 lockA，然后 lockB
线程 2：获取 lockA，然后 lockB
```
- 消除循环等待（四个死锁条件之一）

**锁定转移**（Lock Transfer）：
- 不释放锁，而是将其所有权转移给另一个线程
- 例子：一个线程已完成其工作，将锁传递给下一个线程
- 避免释放和重新获取的开销
- 在 Java 中不直接支持，但在 spinlock 或无锁数据结构中可以模拟

锁定顺序的问题：
- 强制所有代码路径遵循相同的顺序
- 添加新的锁时需要小心
- 可能与对象图中的自然依赖不一致"""
    },
    "concurrency-mutex-vs-semaphore": {
        "type": "qa",
        "q": "mutex 和 semaphore 之间有什么区别？何时使用每个？",
        "a": """**Mutex（互斥体）**：
- 二元：锁定（1）或解锁（0）
- 仅持有者可以解锁
- 用途：保护临界区，强制独占访问

**Semaphore**：
- 计数器：N 许可
- 任何线程都可以释放许可（甚至没有获取的线程）
- 用途：控制 N 个资源的池访问、信令

例子：
- Mutex：保护`count`变量的增量
- Semaphore：有 10 个线程的线程池；10 个许可，一个线程获取一个许可来工作

混淆：
- 二元信号量 (N=1) 似乎像 mutex，但任何线程都可以释放它
- Java 的 `synchronized` 是 mutex
- `Semaphore(1)` 和 `ReentrantLock` 类似但不一样

何时使用：
- Mutex：保护数据
- Semaphore：管理资源池"""
    },
    "concurrency-rwlock-when": {
        "type": "qa",
        "q": "读写锁什么时候有益，什么时候会伤害性能？",
        "a": """**有益于**：
- 读远多于写（比例 10:1 或更高）
- 读操作计算密集且长期持有锁
- 例子：缓存读者多，偶尔写入器

**伤害性能**：
- 读和写大致相等
- 读操作很快（微秒）
- 线程计数低（竞争很少）
- 例子：计时器、计数器、单写数据结构

为什么伤害：
- 获取读锁的开销 > 独占 mutex
- 在低竞争下，mutex 通常赢
- 读写锁实现更复杂，缓存不友好

经验法则：测量。单独的 mutex 可能更简单且更快，除非你有证据证明大量读竞争。"""
    },
    "concurrency-single-condvar-lost-signal": {
        "type": "qa",
        "q": "为什么一个条件变量对多个不同的条件不够？",
        "a": """问题（丢失信号）：
```java
condVar.wait();  // 消费者等待...什么？
```
- 是队列满（生产者）还是空（消费者）？
- 两个消费者等待
- 生产者添加一个项目，notify
- 第一个消费者取走项目
- 第二个消费者唤醒... 队列现在是空的！

解决方案：
- **每个条件一个 condVar**：
  ```java
  notEmpty.signal();  // 清晰：唤醒等待"不空"的线程
  notFull.signal();
  ```
- 或者在单个 condVar 上使用 `notifyAll()` 并让所有线程重新检查条件（低效）

规则：不同的条件 = 不同的 condVar。"""
    },
    "concurrency-thread-pool-backpressure": {
        "type": "qa",
        "q": "线程池如何实现 backpressure？为什么有界队列很关键？",
        "a": """Backpressure = 阻止生产者生产比消费者处理更快的数据。

线程池中的机制：
1. **有界队列**：容量有限，不是无限的
2. **拒绝处理程序**：当队列满时的行为
   - `CallerRunsPolicy`：调用线程自己运行任务（阻塞生产者）
   - `DiscardPolicy`：丢弃任务
   - `AbortPolicy`：抛出异常

例子：
```java
// 队列有 100 个任务
new ThreadPoolExecutor(
    10,              // 核心线程
    20,              // 最大线程
    new LinkedBlockingQueue<>(100),  // 有界！
    new ThreadPoolExecutor.CallerRunsPolicy()  // 阻塞提交者
);
```

为什么有界队列很关键：
- 无界队列导致内存不足（堆积任务）
- 生产者不知道消费者何时赶不上
- 有界队列强制背压，让生产者等待"""
    },
    "concurrency-visibility-stale-flag": {
        "type": "qa",
        "q": "为什么一个普通布尔标志在无锁代码中是陈旧的？",
        "a": """普通变量没有 happened-before 保证：

```java
boolean done = false;

// 线程 1：
done = true;

// 线程 2（其他核上）：
while (!done) { }  // 可能永远不会看到 true！
```

为什么：
- 写入可能留在线程 1 的 L1 缓存中
- 线程 2 从其自己的 L1 缓存中读取
- 没有缓存一致性消息或内存屏障
- Java 内存模型对普通变量没有保证

修复：
```java
volatile boolean done = false;  // 强制缓存一致性
```

`volatile` 添加了内存屏障，强制每次读都查看最新值。

其他修复：
- 使用锁：`synchronized`
- 使用 `AtomicBoolean`"""
    },

    # QUALITY
    "quality-bloaters-refactorings": {
        "type": "qa",
        "q": "什么是代码膨胀（bloaters），如何识别和重构它们？",
        "a": """代码膨胀是东西变得太大、难以理解的地方。

**大方法/类**：
- 做太多事情
- 难以测试和理解
- 重构：Extract Method、提取类、移除重复

**长参数列表**：
- `doSomething(a, b, c, d, e, f, g)`
- 难以调用和维护
- 重构：Parameter Object、使用 Builder、引入配置对象

**数据团**：
- 总是在一起传递的参数（如 x, y, z 坐标）
- 重构：创建一个 Coordinates 类

**switch 语句**：
- 在许多地方重复相同的 switch
- 重构：多态性、策略模式"""
    },
    "quality-constructor-injection": {
        "type": "qa",
        "q": "为什么构造函数注入比 setter 注入或服务定位器更好？",
        "a": """**构造函数注入**：
```java
public Service(Logger log, Database db) {
    this.log = log;
    this.db = db;
}
```
优势：
- 依赖在构造时清晰可见
- 不变性（字段可以是 final）
- 编译时检查（所有依赖都必须满足）
- 无法创建部分初始化的对象

**Setter 注入**：
- 依赖可以在任何时间设置
- 对象可以在没有所有依赖的情况下创建
- 易于选择性地覆盖（用于测试）

**服务定位器**：
- 隐藏的依赖
- 紧耦合到服务定位器

一般来说：优先使用构造函数注入（显式、强制、可测试）。"""
    },
    "quality-couplers-refactorings": {
        "type": "qa",
        "q": "什么是耦合者（couplers），如何识别和重构它们？",
        "a": """耦合者是过度连接事物的代码异味。

**功能嫉妒**：
- 一个方法使用来自其他类的更多方法而不是自己的
```java
customer.setAge(ageCalculator.calculate(customer.getBirthDate()));
```
- 重构：将 setAge 逻辑移到 Customer 中

**不适当的亲密**：
- 一个类依赖于其他类的内部
```java
person.data[0] = 123;  // 直接访问私有数据
```
- 重构：提供公共 API，隐藏实现

**消息链**：
- `a.getB().getC().getD().doIt()`
- 重构：引入委托方法

**中间人**：
- 一个类只是转发所有调用到另一个类
```java
public String getName() { return delegate.getName(); }
```
- 重构：直接使用委托对象或删除中间人"""
    },
    "quality-divergent-vs-shotgun": {
        "type": "qa",
        "q": "Divergent Change 和 Shotgun Surgery 之间有什么区别？",
        "a": """**Divergent Change（发散式变化）**：
- 一个类因多个不相关的原因而改变
- 例子：支付处理器处理信用卡、PayPal 和加密货币
```
新的支付方式 ➜ 修改支付处理器
税法改变 ➜ 修改支付处理器
```
- 类有多个理由改变（违反 SRP）

**Shotgun Surgery（猎枪式修改）**：
- 一个改变需要修改许多类
- 例子：添加新的日志级别需要修改 10 个类
```
新的日志级别 ➜ 修改 Logger、ConsoleWriter、FileWriter、...
```
- 变化分散在许多地方，难以找到所有地方

解决方案：
- Divergent：拆分类（提取不同的原因到不同的类）
- Shotgun：将分散的代码聚集在一个地方（移动方法、提取类）"""
    },
    "quality-exception-design": {
        "type": "qa",
        "q": "如何设计异常层次结构来改进错误处理？",
        "a": """好的异常设计：

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
```"""
    },
    "quality-exceptions-vs-results": {
        "type": "qa",
        "q": "什么时候应该使用异常而不是返回结果对象？",
        "a": """**使用异常**：
- 不可恢复的错误（null 指针、系统故障）
- 意外情况（违反前置条件）
- 编程错误（应该从不发生）

**使用结果对象**（Result、Option、Either）：
- 预期的故障模式（用户不存在、余额不足）
- 业务逻辑的一部分
- 调用者需要以不同的方式处理成功/失败
- Kotlin 的 `Result<T>`、Rust 的 `Result<T, E>`、Java 的 Optional

权衡：
- 异常：调用者无法忽略错误，但会隐藏流程
- 结果：显式处理，但调用者可能忽视失败情况

现代趋势：对预期的故障使用结果，对编程错误使用异常。"""
    },
    "quality-extract-method-triggers": {
        "type": "qa",
        "q": "什么时候应该提取一个方法？触发器是什么？",
        "a": """提取方法（Extract Method）是最常见的重构。触发器：

**1. 注释解释代码**：
```java
// 计算利息
double interest = principal * rate * years / 100;
```
注释是信号；提取它：
```java
double interest = calculateInterest(principal, rate, years);
```

**2. 长方法**（>10-15 行）：
- 难以理解、测试和重用
- 提取逻辑块

**3. 循环内的代码**：
```java
for (Item item : items) {
    // ... 5 行处理逻辑
}
```
提取为 `processItem(item)`

**4. 重复代码**：
- 提取共同部分为方法

**5. 决策分支**：
```java
if (condition) {
    // ... 复杂逻辑
}
```
提取为 `handleSpecialCase()`

不要过度：
- 提取太多小方法导致碎片化
- 但一个大方法比许多单行方法更差"""
    },
    "quality-global-state-tests": {
        "type": "qa",
        "q": "全局状态如何使测试变得困难？如何避免它？",
        "a": """全局状态的问题：

**1. 测试隔离**：
```java
// 全局
static Database db = Database.connect("prod");

// 在测试中...
db 仍然指向 prod！测试数据被污染。
```

**2. 测试顺序依赖**：
- 一个测试修改全局状态
- 下一个测试依赖于那个状态
- 单独运行时测试通过，在套件中失败

**3. 并发问题**：
- 多个测试同时运行会相互干扰

避免全局状态：
```java
// 好的：依赖注入
public class Service {
    private Database db;
    public Service(Database db) { this.db = db; }
}

// 在测试中
@Test void testWithMock() {
    Service service = new Service(new MockDatabase());
}
```

修复现有的全局状态：
- 实例化而不是静态
- 使用依赖注入
- 在测试中使用 setUp/tearDown 重置"""
    },
    "quality-guard-clauses": {
        "type": "qa",
        "q": "什么是卫语句（Guard Clauses），如何改进嵌套代码？",
        "a": """卫语句是提前返回以处理边界情况。

**嵌套版本（不好）**：
```java
if (isValid(input)) {
    if (hasPermission(user)) {
        if (isAvailable(resource)) {
            return process(resource);
        }
    }
}
return null;
```

**卫语句版本（好）**：
```java
if (!isValid(input)) return null;
if (!hasPermission(user)) return null;
if (!isAvailable(resource)) return null;
return process(resource);
```

优势：
- 扁平、易读的流程
- 快速失败
- 减少认知负荷
- 边界情况集中在顶部

应用：
```java
// 嵌套 if-else 替换为
if (condition1) return result1;
if (condition2) return result2;
// ... 正常情况
return normalResult;
```"""
    },
    "quality-null-returns": {
        "type": "qa",
        "q": "为什么返回 null 有问题，更好的替代品是什么？",
        "a": """返回 null 的问题：

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
```"""
    },
    "quality-parameter-object": {
        "type": "qa",
        "q": "什么时候引入参数对象来简化签名？",
        "a": """参数对象聚集相关的参数到一个对象中。

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
- 可以向对象添加行为"""
    },
    "quality-replace-conditional-polymorphism": {
        "type": "qa",
        "q": "如何用多态性替换大的 switch 语句？",
        "a": """模式：

**使用 switch 的代码**：
```java
switch (shapeType) {
    case CIRCLE:
        return Math.PI * r * r;
    case SQUARE:
        return s * s;
    case TRIANGLE:
        return b * h / 2;
}
```

**使用多态性**：
```java
interface Shape {
    double area();
}
class Circle implements Shape {
    public double area() { return Math.PI * r * r; }
}
class Square implements Shape {
    public double area() { return s * s; }
}
// 使用
shape.area();  // 多态调用
```

优势：
- 添加新形状不需要修改现有代码
- 每个类都知道自己如何计算（高内聚）
- 遵循开-闭原则

何时应用：
- switch 语句按类型分派
- 不同类型有不同的行为
- 经常添加新类型"""
    },
    "quality-seams-di": {
        "type": "qa",
        "q": "什么是接缝？依赖注入如何使用接缝进行测试？",
        "a": """接缝是代码中可以在不修改代码的情况下改变行为的地方。

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
- 易于为多个依赖组合"""
    },
    "quality-smell-families": {
        "type": "cloze",
        "zh": "五个重构异味家族及其规范成员：{{c1::膨胀（bloaters）}}——长方法、大类、长参数列表、原始数据类型偏执、数据团；{{c2::对象滥用（OO abusers）}}——按类型的 switch 语句、拒绝的礼物、临时字段、具有不同接口的替代类；{{c3::变化预防器（change preventers）}}——发散变化、猎枪式修改、平行继承层次结构；{{c4::冗余（dispensables）}}——死代码、投机泛化、懒惰类、重复代码、数据类；{{c5::耦合器（couplers）}}——功能嫉妒、不适当的亲密关系、消息链、中间人。"
    },
    "quality-test-doubles": {
        "type": "qa",
        "q": "测试替身的类型是什么？何时使用每个？",
        "a": """测试替身是真实对象的替代品用于测试。

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
- 需要两者 → Spy"""
    },
    "quality-validate-boundary": {
        "type": "qa",
        "q": "为什么在方法边界处验证输入很重要？",
        "a": """边界验证是防御编程的首道防线。

**为什么在边界处**：
```java
public void setAge(int age) {
    if (age < 0) throw new IllegalArgumentException();
    this.age = age;  // 现在我们知道 age >= 0
}
```

优势：
- **快速失败**：在进入之前发现错误
- **清晰的契约**：方法声明它期望什么
- **防止后续的 null 检查**：内部代码不需要防御
- **不变量维护**：确保对象始终处于有效状态

何时验证：
- **公共方法**：总是（调用者是陌生人）
- **私有方法**：较少（内部调用者受信任）
- **参数**：始终
- **返回值**（如果可能）：验证结果有效

验证什么：
```java
public void setName(String name) {
    if (name == null) throw new NullPointerException("name required");
    if (name.trim().isEmpty()) throw new IllegalArgumentException("name empty");
    this.name = name;
}
```

不验证是什么时候：
- 对性能敏感且已验证
- 内部代码路径已被充分测试"""
    },
}

def parse_card(file_path):
    """Parse a card file and return its type and content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract frontmatter
    if content.startswith('---'):
        _, frontmatter, body = content.split('---', 2)
        fm = yaml.safe_load(frontmatter)
        card_type = fm.get('type')
        card_id = fm.get('id')
        return {
            'id': card_id,
            'type': card_type,
            'body': body.strip(),
            'full_content': content
        }
    return None

def extract_sections(body, card_type):
    """Extract Q/A or cloze content from body."""
    if card_type == 'qa':
        # Find ## Q and ## A sections
        q_match = re.search(r'## Q\n(.*?)\n## A\n', body, re.DOTALL)
        a_match = re.search(r'## A\n(.*?)(?=\n## |$)', body, re.DOTALL)
        if q_match and a_match:
            return {
                'q': q_match.group(1).strip(),
                'a': a_match.group(1).strip()
            }
    else:  # cloze
        # Get everything except frontmatter
        return {'cloze': body}
    return None

def generate_translation_append(card_id, card_type):
    """Generate the Chinese translation to append."""
    if card_id not in TRANSLATIONS:
        return None

    trans = TRANSLATIONS[card_id]
    if card_type == 'qa':
        return f"\n## Q zh\n{trans['q']}\n\n## A zh\n{trans['a']}\n"
    else:  # cloze
        return f"\n## zh\n{trans['zh']}\n"

def process_file(file_path):
    """Process a single card file."""
    card = parse_card(file_path)
    if not card or not card['id'] in TRANSLATIONS:
        return {'file': file_path, 'status': 'skip'}

    try:
        trans_append = generate_translation_append(card['id'], card['type'])
        if not trans_append:
            return {'file': file_path, 'status': 'no_translation'}

        # Append translation
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(trans_append)

        return {'file': file_path, 'status': 'success'}
    except Exception as e:
        return {'file': file_path, 'status': 'error', 'error': str(e)}

if __name__ == '__main__':
    import glob

    # Find all untranslated cards
    cards = []
    for pattern in [
        '/Users/chizhang/Code/SystemDesign/vault/low-level-design/cards/principles/*.md',
        '/Users/chizhang/Code/SystemDesign/vault/low-level-design/cards/concurrency/*.md',
        '/Users/chizhang/Code/SystemDesign/vault/low-level-design/cards/quality/*.md',
    ]:
        cards.extend(glob.glob(pattern))

    # Filter to only those without Chinese sections
    untranslated = []
    for card in cards:
        with open(card, 'r', encoding='utf-8') as f:
            content = f.read()
            if '## zh' not in content and '## Q zh' not in content:
                untranslated.append(card)

    print(f"Processing {len(untranslated)} untranslated cards...")

    # Process each
    results = []
    for card_file in untranslated:
        result = process_file(card_file)
        results.append(result)
        if result['status'] == 'success':
            print(f"✓ {result['file']}")
        elif result['status'] == 'skip':
            print(f"- {result['file']} (no translation defined)")
        else:
            print(f"✗ {result['file']} ({result['status']})")

    success = sum(1 for r in results if r['status'] == 'success')
    print(f"\nTranslated: {success}/{len(untranslated)}")
