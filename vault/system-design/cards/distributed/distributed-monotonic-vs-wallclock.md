---
id: distributed-monotonic-vs-wallclock
node: distributed.time
type: qa
---
## Q
Time-of-day clock vs monotonic clock — which do you use for timeouts and elapsed-time measurement, and what goes wrong if you pick the other?

## A
**Monotonic** for all durations (timeouts, latency measurement, rate limiting): it only moves forward, at a steady rate. Its absolute value is meaningless and **not comparable across machines** — it's typically time since boot.

**Time-of-day** clocks are NTP-disciplined: they get **slewed** (rate-adjusted) for small errors but **stepped** — jumped, possibly *backwards* — for large ones, and they pause weirdly across VM migrations and leap-second smearing. Measuring an interval with wall-clock time can therefore yield negative or wildly wrong durations; classic bugs: request "timeouts" firing instantly after an NTP step, or negative latency metrics.

Rule: wall clock only for timestamps humans or other systems interpret as calendar time — and never for ordering writes ([[distributed-lww-danger]]).
