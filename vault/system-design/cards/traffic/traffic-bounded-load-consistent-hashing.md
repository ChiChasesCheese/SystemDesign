---
id: traffic-bounded-load-consistent-hashing
node: traffic.load-balancing
type: qa
---
## Q
Consistent hashing at the LB gives cache affinity, but plain consistent hashing has a load problem. What is it, and how does bounded-load CH fix it?

## A
Random ring placement plus skewed key popularity means some backends receive far more than the mean — affinity and balance fight each other, and a hot key can bury its home node.

**Bounded-load consistent hashing**: cap every server at `c × average load` (e.g. c = 1.25); when a key's home server is at its cap, spill to the next server around the ring. You keep ~affinity for most keys with a hard guarantee that no server exceeds the bound. Shipped in HAProxy (`hash-balance-factor`) and used for Google's and Vimeo's cache-affine routing.
