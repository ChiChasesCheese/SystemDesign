---
id: oop-program-to-interface-scope
node: oop.interfaces
type: qa
---
## Q
"Program to an interface" — where does it pay off in a machine coding round, and where does it become interface bloat?

## A
- **Pays** at variation points and boundaries: pricing/allocation strategies, notification channels, storage — so extension probes are additive and tests can inject fakes.
- **Bloat**: an interface per class with one implementation and no seam need — pure ceremony (speculative generality).

Extract the interface when the second implementation or the test seam actually arrives; requirements hinting at variants ("support multiple pricing schemes") count as arrival.

## Q zh
「Program to interfaces, not implementations」——这何时应用，什么是陷阱？

## A zh
**意思**：将变量、参数、返回类型声明为接口而不是具体类。

```java
// 不好
ArrayList<User> users = new ArrayList<>();
HashMap<String, User> cache = new HashMap<>();

// 好
List<User> users = new ArrayList<>();
Map<String, User> cache = new HashMap<>();
```

**好处**：
- 解耦；你可以交换实现（LinkedList、TreeMap）而不改变调用代码。
- 易于测试；模拟接口。

**陷阱**：
- **过度应用**。对于内部变量或不可能被交换的东西，具体类很好。
- **接口无法表达所有需求**。例：`List` 接口，但你需要 `LinkedList.getFirst()` 的 O(1) 性能。你无法在接口中表达这个。
- **接口膨胀**。为每个具体类创建一个接口是过度工程。

**平衡**：
- 公共 API / 交换点 → 接口。
- 内部实现 → 具体类可以。
- 一个实现 → 接口可能是多余的。

**现代实践**：Java 8+ 接口可以有默认方法，使它们更像轻量级基类。
