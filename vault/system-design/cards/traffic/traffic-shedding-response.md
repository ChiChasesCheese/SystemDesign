---
id: traffic-shedding-response
node: traffic.rate-limiting
type: qa
---
## Q
When a rate limiter rejects a request, what exactly should the response contain — and why does the wrong response amplify load?

## A
- **HTTP 429 Too Many Requests** (or 503 for server-wide shedding) — a distinct code so clients and dashboards can tell throttling from errors.
- **`Retry-After`** header — tells well-behaved clients when to come back, spreading the retry wave.
- **`RateLimit-*` headers** (limit / remaining / reset) — lets clients self-pace before hitting the wall.

Wrong response (generic 500, no Retry-After): clients treat it as transient failure and **retry immediately**, turning shed load into a self-inflicted retry storm.
