---
id: structure-state-transition-table
node: structure.state-machines
type: qa
---
## Q
Where should "can an order go from PAID to CANCELLED?" live, and how does the entity change state without exposing a setter?

## A
In **one declarative transition table**, not in scattered `if`s:

```java
static final Map<State, Set<State>> ALLOWED = Map.of(
    CREATED,  Set.of(PAID, CANCELLED),
    PAID,     Set.of(SHIPPED, CANCELLED),
    SHIPPED,  Set.of(DELIVERED));

private void transitionTo(State next) {
    if (!ALLOWED.getOrDefault(state, Set.of()).contains(next))
        throw new IllegalStateException(state + " -> " + next);
    state = next;
}
```

Public methods are **named events** (`pay()`, `ship()`, `cancel()`) that call `transitionTo` — never a public `setState`. Changing the lifecycle = editing the table, and the guard makes every illegal path fail loudly.
