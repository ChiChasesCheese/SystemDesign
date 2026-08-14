---
id: quality-constructor-injection
node: quality.testability
type: qa
---
## Q
Why is constructor injection preferred over setter/field injection — three concrete properties?

## A
- **No invalid intermediate state**: the object is fully usable the moment it exists; setter injection allows a constructed-but-unwired object, adding "was it initialized?" as a bug class.
- **Dependencies are honest and final**: `final` fields, visible in one signature — and a constructor demanding six collaborators is a *feature*: it makes the SRP violation impossible to ignore (field injection hides it).
- **Framework-free tests**: `new Service(fakeRepo, fixedClock)` — no DI container, no reflection in unit tests.

Setter injection's remaining niche: genuinely **optional** or cyclic dependencies — both rare, and a cycle is usually a design smell to break instead.
