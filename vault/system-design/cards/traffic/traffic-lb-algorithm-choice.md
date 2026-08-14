---
id: traffic-lb-algorithm-choice
node: traffic.load-balancing
type: qa
---
## Q
Round robin vs least-connections vs consistent hashing — match each to the workload it exists for.

## A
- **Round robin** (weighted): requests are cheap and uniform, backends identical — the simple default.
- **Least connections** (or least outstanding requests): request costs **vary widely** — stops slow requests piling onto one backend; the usual production default.
- **Consistent hashing** (on user/session/key): the backend holds **per-key state** — local cache, WebSocket sessions — so the same key must land on the same node, with minimal reshuffling when nodes change.
