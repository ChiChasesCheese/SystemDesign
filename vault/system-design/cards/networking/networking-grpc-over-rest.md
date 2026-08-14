---
id: networking-grpc-over-rest
node: networking.api-styles
type: qa
---
## Q
When choose gRPC over REST for service-to-service calls — and what do you give up?

## A
Choose gRPC when **you own both ends**: internal microservices wanting compact binary payloads (protobuf), generated typed clients, low per-call overhead, and first-class **streaming** (client, server, bidi) over HTTP/2.

Give up: human-readable payloads, effortless browser support (needs gRPC-Web or a proxy), and HTTP-native caching/tooling. Public-facing APIs stay REST/JSON; gRPC is the internal default.
