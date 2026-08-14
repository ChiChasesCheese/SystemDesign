---
id: quality-global-state-tests
node: quality.testability
type: qa
---
## Q
Name the two distinct ways static/global state breaks tests, and the standard fix for nondeterministic dependencies like time.

## A
Two failure modes:

- **No substitution point**: `Payment.process()` as a static call (or `Singleton.getInstance()`) can't be replaced — every test drags the real implementation along.
- **State leaks between tests**: a mutable global survives across test methods, so tests pass alone and fail in suite (or in parallel) depending on **order** — the worst kind of flake.

Fix for time (the canonical case): never call `LocalDateTime.now()` in domain logic — inject a `Clock`; tests pass `Clock.fixed(...)` and can step time deterministically. Same recipe for randomness (`Random` seed/interface) and UUIDs (injected `IdGenerator`). Legacy escape hatch: wrap the static in an instance class you can inject — then migrate.
