---
id: quality-exception-design
node: quality.errors
type: qa
---
## Q
Designing exceptions in an LLD round: what makes a good domain exception, and what are the two handling sins interviewers flag?

## A
A good domain exception:

- Is **specific and semantic** — `SeatAlreadyLockedException(seatId)`, not `RuntimeException("error")`; it names the business rule violated and carries the data needed to react (retry? pick another seat?).
- Extends a small hierarchy (e.g. `BookingException`) so callers can catch at the granularity they care about.

The two sins:

- **Swallowing**: `catch (Exception e) {}` (or log-and-continue) — the system limps on in a corrupt state and the failure surfaces far from its cause.
- **Catch-and-rethrow bare**: wrapping without adding context, or catching just to log then rethrowing — the same error gets logged three times at three layers. Handle where you can act; otherwise let it propagate, translating only at layer boundaries (with the cause chained).
