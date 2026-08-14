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
