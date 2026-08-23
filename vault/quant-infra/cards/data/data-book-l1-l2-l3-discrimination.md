---
id: data-book-l1-l2-l3-discrimination
node: data.market-data.book
type: qa
---
## Q
You need to build a market-impact model that estimates how much a 5,000-share order would move the price by walking the visible order book. Level 1 data is cheapest, Level 2 next, Level 3 most expensive. Which level is the minimum you actually need, and what does each level structurally omit that the next level adds?

## A
**You need at least Level 2 — walking a book to estimate impact requires depth, which L1 does not have.**
- **Level 1 (top of book)**: best bid, best ask, and their sizes only — plus last trade. It tells you the current spread and the size available at the very best price, but nothing about how much liquidity sits one, two, or ten price levels away. Sufficient for a last-price feed or a simple spread monitor, useless for impact estimation past the first fill.
- **Level 2 (market-by-price, or "depth")**: aggregated size at each price level away from the top, usually to some configurable depth. This is what lets you "walk the book" — sum available size level by level until you've accounted for your order's full quantity, and read off the worst price you'd touch. What it omits is *who* is at each level and in what order: L2 gives you the total size at $50.02, not the five individual orders that compose it or which one is first in the queue.
- **Level 3 (market-by-order, full order book)**: every individual resting order, with its own id, size, and price, in the exchange's actual matching priority. This is required for anything that depends on **queue position** — e.g. modeling the probability a specific resting limit order gets filled before it's cancelled, or reconstructing exactly which of several orders at the same price level executes first — L2's aggregated-by-price view cannot answer that because it has already summed away individual order identity.

So: impact modeling via walking the book needs L2; anything about limit-order fill probability or queue dynamics needs L3.

## Q zh
你需要构建一个市场冲击模型，通过遍历盘口来估计一笔 5,000 股的委托会把价格推动多少。一档（L1）数据最便宜，二档（L2）次之，三档（L3）最贵。你实际至少需要哪一档？每一档相对下一档结构性地缺失了什么？

## A zh
**你至少需要二档（L2）——遍历盘口估算冲击需要深度信息，而一档没有这个信息。**
- **一档（Level 1，最优盘口）**：只有最优买价、最优卖价及其数量，再加最新成交价。它告诉你当前的点差以及最优价位上有多少数量，但完全不知道再往外一档、两档、十档还有多少流动性。对于一个最新价行情源或简单的点差监控足够，但一旦超过第一档成交就毫无用处。
- **二档（Level 2，按价格市场深度，或"深度"）**：顶部之外每个价位上的聚合数量，通常到某个可配置的深度。这才是让你能"遍历盘口"的数据——逐档累加可用数量，直到覆盖你委托的全部数量，并读出你会触及的最差价格。它缺失的是**每一档上究竟是谁、按什么顺序**：L2 只告诉你 50.02 美元这一档总共有多少数量，不告诉你构成这个数量的五笔独立委托，也不告诉你队列里谁排在第一。
- **三档（Level 3，逐笔委托全深度）**：每一笔独立的挂单，带有自己的 id、数量、价格，按交易所真实的撮合优先级排列。任何依赖**队列位置（queue position）**的分析都需要它——例如为某个特定挂单在被取消前成交的概率建模，或精确还原同一价位上几笔委托里哪一笔先成交——L2 按价格聚合的视图已经把单笔委托的身份汇总掉了，回答不了这类问题。

所以：通过遍历盘口做冲击建模需要 L2；任何涉及限价单成交概率或队列动态的问题需要 L3。
