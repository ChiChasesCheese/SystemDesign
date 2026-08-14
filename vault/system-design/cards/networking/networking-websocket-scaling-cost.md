---
id: networking-websocket-scaling-cost
node: networking.realtime
type: qa
---
## Q
What makes a WebSocket fleet fundamentally harder to scale than a stateless HTTP fleet? Name the three concrete problems.

## A
**Connection state lives on a specific server.**

- **Routing**: to push to user X you must find *which* server holds X's socket → needs a connection registry (e.g. Redis) or a pub/sub layer every server subscribes to.
- **Deploys/drains**: restarting a server drops every connection it holds; clients must reconnect and resync missed state.
- **Reconnect storms**: an LB or server failure makes tens of thousands of clients reconnect at once — require jittered exponential backoff clientside.
