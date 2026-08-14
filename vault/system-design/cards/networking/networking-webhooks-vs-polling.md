---
id: networking-webhooks-vs-polling
node: networking.api-styles
type: qa
---
## Q
Exposing events to third-party integrators: webhooks vs letting them poll. What must a webhook provider build that polling gives for free?

## A
Delivery machinery, because consumer endpoints are down or slow constantly:

- **Retries with backoff + dead-letter handling** — and since retries reorder and duplicate, consumers need event ids and idempotent handlers.
- **Authentication of pushes**: HMAC-signed payloads so receivers can verify origin.
- **A replay/list API anyway** — consumers must recover after missing deliveries.

Polling is simpler and consumer-paced, but latency = poll interval and most polls return nothing. Robust pattern: webhook as a "something changed" ping; consumer fetches truth via the API.
