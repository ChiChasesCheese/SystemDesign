---
id: reliability-untested-failover
node: reliability.multi-region
type: qa
---
## Q
Why does an untested regional failover "not exist," and what two practices make failover real?

## A
Failover paths rot silently: the standby region drifts (missing config, stale capacity quotas, expired secrets, un-replicated new dependencies), and the first execution under pressure discovers all of it at once. A DR plan that has never run is a hypothesis, not a capability.

- **Regular game days / DR drills**: fail over real (or shadow) traffic on a schedule and measure actual RTO/RPO against the objectives.
- **Continuous validation**: standby capacity provisioned and health-checked, runbooks executable by automation, ideally routine traffic served from the secondary so drift surfaces immediately.
