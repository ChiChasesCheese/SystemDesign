---
id: networking-heartbeats-idle-timeouts
node: networking.realtime
type: qa
---
## Q
Why do long-lived connections need application-level ping/pong when TCP already has keepalive?

## A
A dead peer with no traffic is pure silence — indistinguishable from idle. TCP keepalive defaults to **2 hours**, is often disabled by middleboxes, and says nothing about whether the *application* is alive.

App-level heartbeats every ~30 s do two jobs:

- **Detect half-open connections** (peer crashed, network path gone) within seconds — miss N pongs → close and reclaim the socket, registry entry, and queues.
- **Refresh idle timers** in NATs, LBs, and proxies, which commonly kill connections idle for ~60 s.

Heartbeat interval must therefore be shorter than the smallest idle timeout on the path.
