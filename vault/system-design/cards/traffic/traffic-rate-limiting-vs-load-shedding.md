---
id: traffic-rate-limiting-vs-load-shedding
node: traffic.rate-limiting
type: qa
---
## Q
Rate limiting vs load shedding — different triggers, different fairness. Draw the distinction and say why you need both.

## A
- **Rate limiting**: a *per-client contract* (quota), enforced even at 10% utilization — protects tenants from each other and makes cost predictable.
- **Load shedding**: *self-protection under actual overload*, triggered by health signals (queue depth, CPU, latency), dropping traffic regardless of anyone's quota — protects the service itself.

Shedding is priority-ordered: drop unauthenticated, background, and retry traffic before paid interactive requests; never shed health checks.

You need both because every client staying within quota can still sum to more than the system can serve.
