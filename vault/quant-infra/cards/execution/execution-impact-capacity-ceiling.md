---
id: execution-impact-capacity-ceiling
node: execution.impact
type: qa
---
## Q
A strategy has a stable gross alpha of 15 bps per round trip and trades a single stock with $2B ADV. At $10M AUM its impact cost is negligible; the fund grows the strategy to $2B AUM in that same name. Using the square-root law's shape (impact rises with the square root of size, not linearly), explain why this strategy has a capacity ceiling even though it never runs out of alpha, and where that ceiling actually sits.

## A
**The ceiling isn't a hard wall where alpha vanishes — it's the AUM at which impact cost, which keeps rising (just sub-linearly) with size, catches up to and then exceeds a fixed per-trade alpha, and every dollar past that point is destructive rather than merely lower-margin.**

Because impact scales as `k · σ · √(order size / ADV)`, doubling AUM does not double cost — but it does keep increasing it, just more slowly than size grows. At $10M against a $2B ADV name (0.5% participation), impact might be a fraction of a bp — negligible next to 15 bps of alpha, so the strategy looks scale-free. Push AUM toward a meaningful fraction of ADV — participation rates of 10%, 20%, 50% — and impact per round trip climbs toward, and eventually past, the fixed 15 bps of gross alpha, because gross alpha per trade is roughly constant while impact cost keeps climbing with size (just concavely). The **capacity ceiling** is exactly the AUM where marginal impact cost equals marginal alpha — beyond it, incremental capital doesn't merely earn a lower return, it earns a *negative* one, because the sub-linear-but-still-increasing cost curve has crossed the flat alpha line.

The practical consequence: a strategy's true capacity is not "however much capital I can raise" but a specific number set by the ratio of its alpha to the liquidity (ADV, volatility) of what it trades — which is exactly why capacity estimation belongs next to alpha estimation in any serious strategy write-up, and why a strategy that looked scale-free at $10M can quietly become unprofitable well before the fund intends to stop growing it, unless someone is explicitly tracking where the impact curve crosses the alpha line.

## Q zh
某策略每次往返交易稳定获取 15 个基点的毛 alpha，交易的是一只日成交额 20 亿美元的单一股票。在 1000 万美元管理规模下，它的冲击成本可以忽略不计；基金把这个策略在同一只股票上扩大到 20 亿美元管理规模。利用平方根冲击律的形状（冲击随规模的平方根上升，而不是线性上升），解释为什么这个策略存在容量上限（capacity ceiling），尽管它的 alpha 从未枯竭？这个上限具体在哪里？

## A zh
**这个上限不是 alpha 突然消失的一堵硬墙——而是随着规模增大不断上升（只是次线性地上升）的冲击成本，追上并最终超过一个固定的单笔 alpha 的那个管理规模；超过这个点之后，每多投入一美元不再只是回报更低，而是纯粹的破坏。**

因为冲击按 `k · σ · √(订单规模 / ADV)` 缩放，管理规模翻倍并不会让成本翻倍——但成本确实会持续上升，只是比规模增长得慢。在 1000 万美元对上 20 亿美元 ADV（0.5% 参与率）的情况下，冲击可能只有零点几个基点——相对 15 个基点的 alpha 微不足道，所以这个策略看起来"规模无关"。但把管理规模推到 ADV 一个可观的比例——参与率 10%、20%、50%——每次往返的冲击就会不断逼近、最终超过固定的 15 个基点毛 alpha，因为每笔交易的毛 alpha 大致恒定，而冲击成本会随规模持续攀升（只是以凹函数的方式）。**容量上限**恰恰就是边际冲击成本等于边际 alpha 的那个管理规模——超过它之后，增量资本不只是赚得更少，而是赚**负的**，因为这条次线性但持续上升的成本曲线已经穿过了那条平坦的 alpha 线。

实际后果是：一个策略真正的容量，不是"我能募到多少资本"，而是由它的 alpha 相对于它所交易标的的流动性（ADV、波动率）之比决定的一个具体数字——这正是为什么容量估算应该和 alpha 估算一起出现在任何认真的策略说明里，也是为什么一个在 1000 万美元时看起来规模无关的策略，如果没有人明确追踪冲击曲线什么时候穿过 alpha 线，可能在基金打算停止扩张它之前很久，就已经悄悄变得不再盈利。
