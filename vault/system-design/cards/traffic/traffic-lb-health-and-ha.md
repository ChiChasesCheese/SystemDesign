---
id: traffic-lb-health-and-ha
node: traffic.load-balancing
type: qa
---
## Q
The load balancer is itself a single point of failure. How is the LB tier made highly available, and what health-check subtlety prevents it from making outages worse?

## A
HA: **redundant LB pairs sharing a virtual IP** (VRRP/keepalived failover), or **anycast/ECMP** spreading one IP across an LB fleet; DNS with multiple records as the coarse outer layer.

Health-check subtlety: distinguish **"this instance is down" from "everything is down."** If all backends fail checks (e.g. a shared dependency blips), removing them all serves 100% errors — use fail-open thresholds ("if >50% unhealthy, keep routing to all") and checks that test the process, not its dependencies.
