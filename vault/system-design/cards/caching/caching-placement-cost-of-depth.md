---
id: caching-placement-cost-of-depth
node: caching.placement
type: cloze
---
Each cache layer sits closer to the client than the last, and the trade moves the same direction every step: pushing a cache toward the client (browser → CDN → gateway → app → DB) buys {{c1::lower latency and more offloaded backend traffic}} at the price of {{c2::weaker control over freshness/invalidation and less request context (no auth, no per-user data) available at that layer}}.

## zh
每个缓存层比最后一个更靠近客户端，权衡在每个步骤中朝相同方向移动：将缓存推向客户端（browser → CDN → gateway → app → DB）以 {{c1::lower latency and more offloaded backend traffic}} 为代价购买 {{c2::weaker control over freshness/invalidation and less request context (no auth, no per-user data) available at that layer}}。
