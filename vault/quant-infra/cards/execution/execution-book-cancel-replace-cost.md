---
id: execution-book-cancel-replace-cost
node: execution.microstructure.book
type: qa
---
## Q
A market maker's resting limit order has been sitting at the best price for several minutes with hundreds of shares ahead of it filled and gone — it's now near the front of the queue. A momentary signal suggests nudging the price up by one tick would be marginally better. What actually happens to the order's economics if they cancel and resubmit at the new price, versus leaving it alone?

## A
**Cancel-replace does not move the order — it destroys the old order's queue position and creates a brand-new one at the back of a different queue.** Under price-time priority, an exchange has no notion of "the same order at a slightly different price"; a cancel is a full withdrawal, and the replacement is a new order stamped with the current timestamp. Even a one-tick improvement means giving up a position that took minutes of waiting (and possibly hundreds of shares of prior fills passing by) to earn, in exchange for landing at the very back of the new price's queue — often behind other market makers who have been quoting there all along.

The cost shows up three ways: **(1) forfeited fill probability** — the near-front order had a high chance of being filled by the next incoming marketable order; the new order at the back may not fill before the market moves again, meaning the "improvement" is never realized. **(2) round-trip latency exposure** — between the cancel acknowledgment and the new order's acceptance, the market can move, so the trader may end up chasing a price that has already left, repeating the cycle. **(3) many venues also reset priority on a size increase even at the *same* price** — so even "just adding more shares" to a resting order, not just moving its price, can cost the accumulated position. This is why sophisticated market makers treat every cancel-replace as a real economic decision, not a costless correction: the expected value of the marginal price improvement has to exceed the value of the queue position being surrendered.

## Q zh
一位做市商挂在最优价的限价单已经在盘口待了好几分钟，前面几百股的委托都已经成交离场了——它现在已经接近队列前段。这时一个瞬时信号显示，把价格往上挪一个 tick 会略微更好。如果他们撤单并以新价格重新挂单，相比不动它，订单的经济性实际会发生什么变化？

## A zh
**撤单重挂（cancel-replace）并不是"挪动"这笔委托——它是销毁旧委托积累的队列位置，然后在另一个队列的最末尾创建一笔全新的委托。** 在 price-time priority 下，交易所并不存在"同一笔委托、价格稍微变一下"这种概念；撤单就是完全撤回，重新提交的是一笔盖着当前时间戳的全新委托。哪怕只是改善一个 tick，也意味着放弃了一个花了几分钟等待（甚至看着前面几百股陆续成交离场）才赚到的位置，换来的是排在新价位队列的最末端——常常排在那些一直在那个价位持续报价的其他做市商后面。

这个代价体现在三方面：**（1）放弃的成交概率**——原本接近队首的委托，被下一笔来到的可成交单打中的概率很高；新挂在队尾的委托可能在市场再次变化之前都成交不了，也就是说这个"改善"根本没有机会兑现。**（2）往返延迟暴露**——从撤单确认到新委托被接受这段时间里，市场可能已经变了，交易者可能变成在追一个已经跑掉的价格，然后重复这个循环。**（3）很多交易所即便是在*同一个*价位上增加委托数量，也会重置优先权**——所以哪怕只是给挂单"加量"、并没有改价格，也可能付出已积累的位置作为代价。这正是为什么老练的做市商会把每一次撤单重挂都当成一个真实的经济决策，而不是免费的纠错：边际价格改善的期望价值，必须超过被放弃的队列位置的价值。
