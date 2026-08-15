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
