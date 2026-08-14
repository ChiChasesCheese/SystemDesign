---
id: traffic-timeout-budget-propagation
node: traffic.gateways
type: qa
---
## Q
The gateway times out at 10 s, but a service it calls uses a 15 s timeout on its own downstream call. What goes wrong, and what discipline fixes it?

## A
After 10 s the gateway returns 504 and the client may retry — while the abandoned request **keeps computing downstream** for 5 more seconds. Under overload this wasted work compounds: the system burns capacity on answers nobody will receive, stacked under fresh retries.

Fix: **deadline propagation** — attach the remaining budget to the request (gRPC deadlines, a budget header); every hop sets its timeout to ≤ what remains minus its own work, and cancels downstream calls when its caller gives up.

Rule: timeouts must strictly shrink as you go deeper in the call tree.
