---
id: networking-rest-as-default
node: networking.api-styles
type: qa
---
## Q
Why does REST over JSON remain the default for public APIs in 2026, despite gRPC and GraphQL?

## A
Because a public API's clients are **unknown and uncontrolled**, and REST maximizes what strangers get for free:

- Works from any HTTP client, browser, or `curl` — zero codegen or SDK required.
- **HTTP-native caching** (GET + Cache-Control + ETags) works through CDNs and proxies.
- Uniform semantics (verbs, status codes) that every tool — gateways, monitors, WAFs — already understands.

Pick gRPC/GraphQL when you control the clients; pick REST when you don't.
