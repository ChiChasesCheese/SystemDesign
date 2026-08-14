---
id: traffic-token-bucket-vs-sliding-window
node: traffic.rate-limiting
type: qa
---
## Q
Token bucket vs sliding window for rate limiting — what does each guarantee, and which allows bursts?

## A
- **Token bucket**: tokens refill at rate r, bucket holds up to b; a request spends a token. **Allows bursts up to b** while capping the long-run average at r — usually what clients actually want. O(1) state: (count, timestamp).
- **Sliding window** (log or counter-approximation): caps requests in any trailing window — **smooth, no burst allowance** beyond the cap; the fix for fixed-window's double-burst-at-boundary flaw.

Pick token bucket for friendly burst tolerance; sliding window for strict "never more than N per minute" contracts.
