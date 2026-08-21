---
id: oop-equals-hashcode-contract
node: oop.values
type: qa
---
## Q
You override `equals` on `Money` but not `hashCode`. `set.add(new Money(5, USD))` then `set.contains(new Money(5, USD))` returns **false**. Explain, and state the contract that was broken.

## A
`HashSet` looks in the bucket chosen by `hashCode` first. Two equal objects with different identity hash codes land in different buckets, so `equals` is never even called.

Contract: **equal ⇒ equal hash codes** (the converse is not required — collisions are legal, just slower). Also required: reflexive, symmetric, transitive, consistent, and `x.equals(null) == false`.

Two practical consequences:
- **Symmetry with subclasses**: `instanceof` in a superclass `equals` lets `sub.equals(super)` disagree with `super.equals(sub)`; `getClass() !=` avoids that but forbids subclass equality entirely.
- Only fields that never change may participate — otherwise a mutation strands the object in the wrong bucket.

## Q zh
`equals()` 和 `hashCode()` 之间的合同是什么，打破它会发生什么？

## A zh
**合同**：
- 如果 `a.equals(b)` 为 true，则 `a.hashCode() == b.hashCode()` 必须为真。
- （反向**不**成立：`a.hashCode() == b.hashCode()` 不保证 `equals`。）

**为什么**：HashMaps 和 HashSets 使用 `hashCode()` 找到桶，然后使用 `equals()` 以找到确切的元素。

**打破它会发生什么**：
```java
class User {
    String name;
    // 只覆盖 equals，忘记 hashCode
    boolean equals(Object o) { return ((User)o).name.equals(name); }
}

Set<User> s = new HashSet<>();
s.add(new User("Alice"));
s.contains(new User("Alice"))  // false ——相同的值，不同的 hashCode，所以不同的桶
```

**修复**：
```java
public int hashCode() { return name.hashCode(); }
public boolean equals(Object o) { 
    if (!(o instanceof User)) return false;
    return name.equals(((User)o).name);
}
```

**记住**：`equals()` → 也实现 `hashCode()`。IDEs 会警告。
