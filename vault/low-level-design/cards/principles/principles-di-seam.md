---
id: principles-di-seam
node: principles.coupling
type: qa
---
## Q
What exactly does constructor injection buy over `new`-ing the collaborator inside the class — and does it require a framework?

## A
It creates a **seam**: the class sees only the interface, so tests substitute fakes and "swap MySQL for in-memory" becomes a wiring change instead of an edit. It also makes the dependency graph explicit — hidden `new`s are invisible coupling.

No framework needed: plain constructor parameters wired by hand in `main()` is complete DI. Spring/Guice only automate the wiring — worth saying explicitly in an interview.
