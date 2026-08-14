---
id: foundations-coordinated-omission
node: foundations.numbers
type: qa
---
## Q
Your load-test harness sends a request, waits for the response, then sends the next. Name the measurement error and the fix.

## A
**Coordinated omission**: by waiting, the harness backs off *exactly when the system is slow*, so queueing delay vanishes from the data — you measured service time, not response time, and high percentiles come out wildly optimistic.

Fix: generate load on a **fixed schedule independent of responses**, and clock each request from its *scheduled* send time, so time spent waiting behind a stall is counted. Measure at the client, where users actually wait.
