---
id: reliability-correlated-failures
node: reliability.availability
type: qa
---
## Q
Two replicas at 99.9% "should" give six nines in parallel. Why do real systems get far less, and what restores some of the promised benefit?

## A
The parallel formula assumes **independent** failures; real faults are correlated:

- **Shared fate**: same rack/AZ/power, same load balancer, same cloud control plane.
- **Same software**: one bad deploy or config push takes out every replica simultaneously — the most common correlated fault.
- **Load coupling**: one replica's death shifts traffic and overloads the survivors (cascade).

Restore independence by spreading across **failure domains** (AZs/regions), staggering rollouts so versions never change everywhere at once, and removing shared hard dependencies from the redundant path. See [[reliability-serial-parallel-composition]].
