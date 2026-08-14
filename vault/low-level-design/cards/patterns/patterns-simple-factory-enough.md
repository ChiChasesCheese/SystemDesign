---
id: patterns-simple-factory-enough
node: patterns.creational
type: qa
---
## Q
In a machine-coding round you need to create the right `Vehicle` subtype from an input string. Do you reach for factory method, or something simpler?

## A
A **simple (static) factory** — one function with the type switch — is the right first move:

```java
static Vehicle of(String type) {
    return switch (type) {
        case "car"  -> new Car();
        case "bike" -> new Bike();
        default -> throw new IllegalArgumentException(type);
    };
}
```

- It centralizes the only `switch` on type in one place; callers stay decoupled from concretes.
- Upgrade to a **registry map** (`Map<String, Supplier<Vehicle>>`) when new types must be added without editing the switch, and to **factory method** only when *creation itself* must vary per subclass of the creator.
- Saying "simple factory now, registry if types grow" scores better than pattern-dropping GoF names.
