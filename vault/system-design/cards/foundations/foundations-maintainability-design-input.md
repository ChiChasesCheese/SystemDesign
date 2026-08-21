---
id: foundations-maintainability-design-input
node: foundations.method
type: qa
---
## Q
DDIA's three maintainability goals — name them, and where does each show up in a design interview answer?

## A
- **Operability** — make life easy for ops: metrics, runbooks, sane defaults, no manual toil. Show it: say how you deploy, monitor, and migrate the thing you just drew.
- **Simplicity** — remove *accidental* complexity with good abstractions. Show it: refuse components a number doesn't justify.
- **Evolvability** — cheap to change later. Show it: schema evolution plan, versioned APIs, reversible decisions.

Most software cost is maintenance, not initial build — treating these as requirements (not virtues) is a senior signal.


## Q zh
"可维护性"是非功能需求。它如何改变设计？

## A zh
可维护性说的是：工程师能在需要改变时多快改变系统。

它驱动：
- **API 边界清晰** — 隐藏实现细节，所以改变内部不会传播。
- **自动化测试覆盖** — 一个改变不会无声地破坏东西。
- **可观察性** — 当它破裂时诊断快速。
- **避免单一故障点** — 一个人知道一切意味着他们离开时知识就离开了。

一个"快速"的系统最终变得无法维护，速度优先的设计则相反。
