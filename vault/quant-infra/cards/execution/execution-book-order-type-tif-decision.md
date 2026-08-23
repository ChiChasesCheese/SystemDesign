---
id: execution-book-order-type-tif-decision
node: execution.microstructure.book
type: qa
---
## Q
You need to buy 500 shares of a liquid stock right now because your signal decays in seconds, and separately you need to buy 500 shares of a different name where you have no urgency and want the best price you can get over the next hour. Which order type and time-in-force fits each, and what do you give up with each choice?

## A
**The urgent order takes liquidity; the patient order supplies it, and the trade-off is certainty of execution versus certainty of price.**

- **Urgent leg → marketable order, immediate-or-cancel (IOC).** A plain market order guarantees a fill but not a price — in a fast-moving or thin book it can walk several levels and pay far more than the last quote. A **limit IOC** (limit price at or through the current offer) caps the worst price you'll pay while still executing whatever quantity is available *right now*; any unfilled remainder is cancelled instead of resting exposed. You pay the spread and any impact from consuming displayed size, but you get the fill before your signal decays.
- **Patient leg → resting limit order, good-till-cancelled (GTC) or day.** You quote inside or at the touch and wait for someone else to cross the spread to you. You avoid paying the spread and may earn a maker rebate, but you take on **non-execution risk** (price runs away and you never fill) and **adverse-selection risk** (you only get filled when the market is moving against you, since informed flow is exactly what crosses to hit a stale-looking limit price).

A third option worth knowing: a **peg order** (e.g., pegged to the midpoint) behaves like a patient limit order that automatically re-quotes as the market moves, so you don't have to manually cancel-replace to stay at the touch — useful for the patient leg when you want passive execution without babysitting the order, at the cost of revealing (to anyone who can detect the pattern) that a pegged order is present.

## Q zh
你需要立刻买入 500 股某只流动性好的股票，因为你的信号几秒钟内就会衰减；同时你还需要买入另一只股票 500 股，这次不着急，希望在接下来一小时内争取到最好的价格。这两种情形分别该用什么订单类型和 time-in-force？各自放弃了什么？

## A zh
**紧急单是"吃"流动性，耐心单是"供给"流动性，二者的权衡是成交确定性 vs 价格确定性。**

- **紧急那一单 → 可成交单 + 立即成交或取消（IOC）。** 普通市价单能保证成交但不保证价格——在行情快或盘口薄的时候可能扫过好几档、付出远高于最新报价的成本。**限价 IOC**（限价设在当前对手价或以内）能锁死你愿意付的最差价格，同时立刻吃掉当下可用的数量；没成交的剩余部分直接撤销，而不是挂在盘口暴露。你付出了价差和吃掉挂单数量带来的冲击，但换来了在信号衰减前的成交。
- **不急那一单 → 挂在盘口的限价单，good-till-cancelled（GTC）或当日有效。** 你在盘口内侧或最优价挂单，等别人来穿过价差成交给你。你省下了价差、可能还赚到做市返佣，但要承担**不成交风险**（价格跑掉了、你始终没成交）和**逆向选择风险**（你只有在市场朝对你不利方向走时才会被成交，因为恰恰是知情单流会去吃这个看起来"过时"的限价）。

还有第三种值得了解的选项：**盯盘单（peg order）**（比如挂在中点上）表现得像一个会随行情自动重新报价的耐心限价单，让你不用手动撤单重挂就能一直贴在最优价——适合想要被动成交又不想盯盘的耐心那一单，代价是（对能识别这种模式的人而言）暴露了这里有一个盯盘单存在。
