---
id: oop-self-use-override-trap
node: oop.pillars
type: qa
---
## Q
```java
class CountingSet<E> extends HashSet<E> {
  int added = 0;
  public boolean add(E e) { added++; return super.add(e); }
  public boolean addAll(Collection<? extends E> c) { added += c.size(); return super.addAll(c); }
}
```
`addAll` of 3 elements reports 6. Why, and what does this teach about inheritance?

## A
`HashSet.addAll` is implemented by calling `this.add()` in a loop — **self-use**. The overridden `add` runs and counts again, so every element is counted twice.

The subclass broke because it depended on an *unspecified internal detail* of the base. Two consequences:

- A base class is only safely subclassable if it **documents its self-use** (Java's "@implSpec / this implementation calls…") — and that documentation then freezes the base's internals forever.
- The same trap in constructors: a base constructor calling an overridable method runs the override **before** the subclass fields are initialized.

Fix here: compose — wrap a `Set` and forward.

## Q zh
为什么从同一个类中调用可覆盖的方法是陷阱，如何避免？

## A zh
**陷阱**：
```java
class Parent {
    void work() {
        log("开始");
        doWork();
        log("结束");
    }
    
    void doWork() { /* 父类实现 */ }
    void log(String msg) { System.out.println(msg); }
}

class Child extends Parent {
    @Override
    void log(String msg) { 
        System.out.println("[CHILD] " + msg);  // 自定义日志
    }
}

child.work();  // 哦天啊，"开始" 没有 [CHILD] 前缀，因为 Parent.work() 调用 this.log()...
               // 等等，它应该调用子类的 log()！
```

实际上在 Java 中，这**确实**调用 `Child.log()`（因为多态），但代码有点混乱。

**真正的陷阱**：初始化顺序。
```java
class Parent {
    Parent() { init(); }
    void init() { /* ... */ }
}

class Child extends Parent {
    List<String> items;  // 字段
    Child() { items = new ArrayList<>(); }
    
    @Override
    void init() { items.add("foo"); }  // 空指针！items 尚未初始化
}
```

**避免**：
- **不要**从构造函数调用可覆盖的方法。
- 使用 `final` 方法用于内部自调用。
- 分离初始化逻辑（模板方法的 hook 应该简单且安全）。
