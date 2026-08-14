---
id: networking-grpc-streaming-modes
node: networking.api-styles
type: qa
---
## Q
gRPC's four call types — match each to its use, and name the operational caveat long-lived streams create.

## A
- **Unary**: ordinary request/response — the default.
- **Server-streaming**: subscriptions and feeds — replaces client polling with pushed increments.
- **Client-streaming**: uploads and telemetry — batch many messages into one call, single response.
- **Bidirectional**: chat, sync protocols, interactive sessions.

Caveat: a stream lives on one HTTP/2 connection, so it **pins to one backend** for its lifetime — draining and rebalancing need max-connection-age or app-level reconnects ([[traffic-http2-connection-pinning]]).
