---
id: reliability-deadline-propagation
node: reliability.resilience.retries
type: qa
---
## Q
Service A (1s timeout) calls B, which calls C. C responds in 2s. What goes wrong with naive per-hop timeouts, and what is the fix?

## A
B and C keep doing work for a caller that has **already given up** — wasted capacity, and A may have retried, doubling load. Worse, if inner timeouts are longer than outer ones, errors always surface at the outermost layer, hiding the real culprit.

Fix: **deadline propagation** — the client's remaining budget travels with the request (e.g. gRPC deadlines); each hop subtracts elapsed time and cancels work the moment the deadline is exceeded.
