---
id: networking-realtime-transport-choice
node: networking.realtime
type: qa
---
## Q
Long polling vs SSE vs WebSockets — give the one-line selection rule and a canonical example for each.

## A
Choose by **directionality and frequency**:

- **Long polling**: rare updates, maximum compatibility, no infra changes — e.g. legacy notification checks.
- **SSE**: server→client only, over plain HTTP — e.g. live scores, LLM token streaming, dashboards.
- **WebSockets**: genuinely **bidirectional** and frequent — e.g. chat, collaborative editing, multiplayer games.

Default to the weakest tool that fits: SSE beats WebSockets when the client never needs to push.
