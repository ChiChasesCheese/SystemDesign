---
id: principles-stack-extends-arraylist
node: principles.composition
type: qa
---
## Q
```java
class Stack<T> extends ArrayList<T> {
  void push(T t) { add(t); }
  T pop() { return remove(size() - 1); }
}
```
What's wrong, and the refactor?

## A
Inheritance-for-reuse: `Stack` publicly inherits ~30 `List` methods (`add(i, e)`, `get(i)`, `clear()`) that let any caller break the LIFO invariant, and it permanently advertises is-a-List.

Refactor to composition: hold a private `ArrayDeque`/`ArrayList`, expose only `push`/`pop`/`peek`. Inherit an interface only when you mean to honor its *entire* contract.
