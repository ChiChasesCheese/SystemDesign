---
id: execution-book-price-time-vs-pro-rata
node: execution.microstructure.book
type: qa
---
## Q
Most US equity venues match orders at the same price by arrival time (price-time priority). CME's interest-rate futures options and some other derivatives venues instead allocate fills at a price proportionally to order size (pro-rata). If you were designing a market-making strategy for each venue, what would you optimize for, and why does the matching rule change the answer?

## A
**Price-time priority rewards being first; pro-rata rewards being big — so the same strategy that wins on one venue is suboptimal on the other.**

- **Price-time (FIFO):** at a given price level, orders queue strictly by arrival time — the order that has been resting longest fills first, in full, before the next order in the queue gets anything. A market maker here optimizes for **speed and being at the front of a fresh price level**: the moment a new best price opens up, whoever posts first captures the entire queue priority at that price, and everyone who posts a millisecond later inherits a worse position no matter how large their order is. This is why price-time venues are latency arms races — priority is a race, not an auction.
- **Pro-rata:** at a given price level, each resting order receives a fill proportional to its share of the total size resting at that price, regardless of when it arrived (some venues blend in a small time-priority allocation for the first order, but the bulk is proportional). A market maker here optimizes for **quoting large size**, because doubling your resting quantity roughly doubles your fill share — being first buys you little, since a late but large order still gets a proportional cut. This discourages pure speed racing and instead rewards capital commitment and quote size.

The consequence for strategy design: a price-time market maker invests in co-location and fast requoting to win the race for queue position; a pro-rata market maker invests in being willing to hold larger resting size at a price, because size — not speed — is what buys fill share.

## Q zh
美股大多数交易所对同一价位的委托按到达时间撮合（price-time priority）。而 CME 的利率期货期权等部分衍生品市场则按委托数量比例分配同一价位的成交（pro-rata）。如果你要为这两个市场分别设计一个做市策略，你会分别优化什么？为什么撮合规则不同会改变答案？

## A zh
**Price-time priority 奖励"先到"，pro-rata 奖励"够大"——所以在一个市场上赢的策略，搬到另一个市场就未必是最优的。**

- **Price-time（先进先出）：** 在同一价位，委托严格按到达时间排队——排在最前面的委托先全额成交，后面的委托要等它成交完才轮到自己，无论后面这笔委托有多大。做市商在这种规则下要优化的是**速度和抢占新价位队首**：一旦某个新的最优价位刚出现，谁先挂单谁就拿到该价位的全部队列优先权，哪怕只晚了一毫秒挂单，无论你的单有多大，位置都更差。这正是 price-time 市场演变成延迟军备竞赛的原因——优先权是一场竞速，不是一场拍卖。
- **Pro-rata（按比例）：** 在同一价位，每笔挂单按其占该价位总挂单量的比例分到成交（有些市场会给排在最前的那笔委托一点点时间优先权，但大头仍按比例分配），跟到达时间基本无关。做市商在这种规则下要优化的是**挂大单**，因为把挂单量翻倍大致就能把成交份额翻倍；先到几乎没什么用，因为一笔虽然晚到但更大的委托依然能分到相应比例。这抑制了纯粹的速度竞赛，转而奖励资本投入和挂单量。

对策略设计的后果是：price-time 的做市商要投入 co-location（机房共址）和快速重新报价，去抢队列位置这场竞速；pro-rata 的做市商则要愿意在某个价位挂更大的量，因为买到成交份额靠的是量，不是速度。
