---
id: networking-sse-mechanics
node: networking.realtime
type: qa
---
## Q
Two built-in SSE features that you'd otherwise hand-build on raw WebSockets?

## A
- **Automatic reconnection with resume**: browsers reconnect on drop and send the last received event id in `Last-Event-ID`, so the server can replay what was missed.
- **Plain HTTP transport**: works through proxies, LBs, and HTTP/2 multiplexing with normal auth headers — no protocol upgrade, no special infra.

Limits to state alongside: one direction only (server→client), text frames only.
