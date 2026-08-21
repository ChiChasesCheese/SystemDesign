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

## Q zh
令牌桶 vs 滑动窗口用于速率限制 — 每个保证什么，哪个允许突发？

## A zh
- **令牌桶**：令牌以速率 r 重填，桶保持最多 b；请求消费一个令牌。**允许最多 b 的突发**同时用 r 限制长期平均值 — 通常客户端实际想要。O(1) 状态：(count、timestamp)。
- **滑动窗口**（日志或计数器近似）：在任何尾部窗口限制请求 — **平滑、在上限之外没有突发允许**；固定窗口边界双突发缺陷的修复。

选择令牌桶用于友好的突发容忍；滑动窗口用于严格"每分钟永不超过 N"合约。

令牌桶 vs 滑动窗口用于速率限制 — 每个保证什么，哪个允许突发？

- **令牌桶**：令牌以速率 r 补充，桶保持最多 b；请求花费一个令牌。**允许最多 b 的突发**同时限制长期平均为 r — 通常是客户端真正想要的。O(1) 状态：(计数、时间戳)。
- **滑动窗口**（日志或计数器近似）：上限任何尾随窗口中的请求 — **平滑，没有超过上限的突发余量**；固定窗口边界双突发缺陷的修复。

为友好的突发容错选择令牌桶；为严格的"每分钟永不超过 N"契约选择滑动窗口。
