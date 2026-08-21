---
id: oop-getter-collection-leak
node: oop.pillars
type: qa
---
## Q
```java
class Floor {
  private final List<Spot> spots;
  public List<Spot> getSpots() { return spots; }
}
```
The field is `private final`. Explain how encapsulation is still broken, and give the three fixes in order of preference.

## A
`final` protects the *reference*, not the contents — the caller holds the live list and can `add`/`clear` it, bypassing every rule `Floor` enforces. Same leak on the way **in**: a constructor storing a caller-supplied list lets the caller keep mutating it.

1. **Don't expose it** — add the operation instead: `floor.findFreeSpot(size)`.
2. Return an **unmodifiable view** (`List.copyOf` / `Collections.unmodifiableList`) and defensively copy in the constructor.
3. Expose a stream/iterator only if callers genuinely need arbitrary traversal.

Getters returning mutable internals (collections, `Date`, arrays) are the most common encapsulation leak in review.

## Q zh
从 getter 返回一个集合有什么危险，你如何防止？

## A zh
**危险**：调用者可以修改内部集合，破坏对象的不变量。

```java
class Document {
    List<Page> pages;
    List<Page> getPages() { return pages; }  // 危险！
}

Document doc = new Document();
doc.getPages().clear();  // 调用者刚刚删除了所有页面。文档现在不一致。
```

**防止**：

1. **返回不可修改的视图**：
   ```java
   List<Page> getPages() { return Collections.unmodifiableList(pages); }
   ```

2. **返回副本**：
   ```java
   List<Page> getPages() { return new ArrayList<>(pages); }
   ```

3. **返回迭代器**（没有 `remove()`）：
   ```java
   Iterator<Page> getPages() { return pages.iterator(); }
   ```

**权衡**：防守（不可修改）vs 便利（副本有内存成本）。不可修改通常是首选；如果调用者想要写访问，他们应该要求 add/remove 方法。
