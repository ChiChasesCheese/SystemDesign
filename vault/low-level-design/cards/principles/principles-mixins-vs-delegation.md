---
id: principles-mixins-vs-delegation
node: principles.composition
type: qa
---
## Q
Mixins/traits (Java default methods, Scala/Rust traits, Python mixins, Go embedding) promise reuse without forwarding code. What do they actually cost?

## A
They are **inheritance with a wider slot** — the fragility mostly stays:

- **Java default methods**: no instance state, and the same-signature diamond forces an explicit `X.super.m()` override.
- **Python mixins**: reuse comes with the **MRO** — which sibling's method runs depends on the class's linearization order, so a base-class edit can silently reroute behavior.
- **Go embedding**: forwarding is automatic, but there is no virtual dispatch back to the outer type — the SELF problem in full.
- All of them still expose the mixin's members as part of your public surface.

Rule: use a trait/mixin for a **stateless capability** with no per-user variation (`Comparable`, `Serializable`-style). Anything with state or a lifecycle → delegate to a collaborator.

## Q zh
什么时候使用 mixin 而不是委托？它们的权衡是什么？

## A zh
Mixin（通过继承或组合混入行为）：
- 优势：不需要显式委托调用；方法自动可用
- 劣势：创建隐含的依赖；多个 mixin 可能会冲突；难以测试隔离

委托（显式转发）：
- 优势：清晰明了哪些调用被转发；易于单独测试；灵活替换
- 劣势：需要显式转发方法（样板代码）

经验法则：如果你是在组织行为（多个概念），使用委托。如果你只是混入一个通用的、独立的功能，可以考虑 mixin。
