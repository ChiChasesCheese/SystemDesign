---
id: reliability-fault-vs-failure
node: reliability.availability
type: qa
---
## Q
Fault vs failure (DDIA framing): what is the difference, and what does that make "fault tolerance" mean in practice?

## A
- **Fault**: one component deviates from spec (a disk dies, a node returns garbage, a network link drops packets).
- **Failure**: the *system as a whole* stops providing its service to the user.

Fault tolerance = designing so faults do **not** escalate into failures — you cannot reduce fault probability to zero, so you contain faults instead. Corollary: deliberately *inducing* faults (killing processes, injecting latency) is how you prove the containment machinery works — see [[reliability-chaos-hypothesis]].
