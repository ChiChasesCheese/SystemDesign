---
id: quality-test-doubles
node: quality.testability
type: qa
---
## Q
Stub vs mock vs fake — separate the three doubles people actually confuse, by what the test asserts on.

## A
- **Stub**: returns canned answers so the code under test can run (`stubRates.get("EUR") → 1.1`). The test asserts on the **system's output/state** — the stub is scenery.
- **Mock**: records calls and the test **asserts on the interaction itself** — "`emailSender.send()` was called once with X." Use only when the side effect *is* the requirement; over-mocking welds tests to implementation details.
- **Fake**: a real, working, lightweight implementation (in-memory repository, embedded queue). Behaves properly across many calls, so it suits whole-flow tests without a DB.

(Remaining taxonomy: **dummy** — passed but never used; **spy** — a stub that also records, letting you assert afterward instead of setting expectations upfront.)
