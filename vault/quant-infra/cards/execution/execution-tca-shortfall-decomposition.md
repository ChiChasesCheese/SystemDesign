---
id: execution-tca-shortfall-decomposition
node: execution.tca
type: qa
---
## Q
A PM decides to buy 100,000 shares at $50.00 (the arrival price). The order isn't sent for 10 minutes, by which point the price has drifted to $50.05. Execution then takes an hour and fills 90,000 shares at an average price of $50.12; the remaining 10,000 shares are cancelled when the price is $50.20. Decompose this into the four components of implementation shortfall.

## A
**Implementation shortfall is the full gap between the paper P&L of trading instantly at the decision price and what actually happened, split into delay, execution (impact + timing), and opportunity cost — each measuring a different phase or a different fate of the shares.**

- **Delay cost**: the price move between the *decision* ($50.00) and the moment the order actually starts working ($50.05), applied to the full 100,000 shares — `($50.05 − $50.00) × 100,000 = $5,000`. This is the cost of the gap between deciding and acting, before a single share trades.
- **Execution cost** (often further split into impact and market timing): the difference between the price when the order started ($50.05) and the actual average fill price on the shares that traded ($50.12), applied to the 90,000 filled shares — `($50.12 − $50.05) × 90,000 = $6,300`. This is what most people mean by "trading cost" — the combination of the algo's own footprint (impact) and any adverse drift during the execution window that wasn't caused by the order itself (timing).
- **Opportunity cost**: for the 10,000 shares never filled, the cost is measured from the *decision* price to the price at the point the order was abandoned ($50.20) — `($50.20 − $50.00) × 10,000 = $2,000`. This captures the real economic cost of the shares the fund wanted but never got, which a P&L statement that only looks at executed trades would silently omit entirely.

Total implementation shortfall = $5,000 + $6,300 + $2,000 = **$13,300**, against a decision-price notional of $5,000,000 — about 27 bps. The point of the decomposition is that a single blended "cost" number can't tell you whether the problem was slow desk handoff (delay), a bad algo (execution), or an algo that gave up too early on hard-to-fill shares (opportunity cost) — three completely different fixes.

## Q zh
基金经理决定以 50.00 美元（到达价）买入 10 万股。订单在 10 分钟后才发出，此时价格已经漂到 50.05 美元。执行花了一个小时，成交了 9 万股，平均成交价 50.12 美元；剩下的 1 万股在价格到 50.20 美元时被取消了。请把这笔交易分解成实现盈亏差（implementation shortfall）的四个组成部分。

## A zh
**实现盈亏差是"立刻按决策价格成交"的账面盈亏与实际发生结果之间的全部差距，拆分为延迟成本、执行成本（冲击+时机）、以及机会成本——每一部分衡量的是不同阶段、或不同命运的那部分股份。**

- **延迟成本（delay cost）**：*决策*那一刻（50.00 美元）与订单真正开始执行那一刻（50.05 美元）之间的价格变动，作用在全部 10 万股上——`(50.05 − 50.00) × 100,000 = 5,000 美元`。这是"决策"和"行动"之间那段时间差的成本，此时一股都还没成交。
- **执行成本（execution cost，通常再拆分成冲击和时机）**：订单开始执行时的价格（50.05 美元）与实际成交股份的平均成交价（50.12 美元）之间的差，作用在成交的 9 万股上——`(50.12 − 50.05) × 90,000 = 6,300 美元`。这是大多数人所说的"交易成本"——算法自身足迹带来的冲击，加上执行窗口内并非由订单本身造成的不利漂移（时机）的组合。
- **机会成本（opportunity cost）**：对于始终没成交的 1 万股，成本是从*决策*价格到订单被放弃那一刻的价格（50.20 美元）来衡量的——`(50.20 − 50.00) × 10,000 = 2,000 美元`。这捕捉到了基金想要却始终没拿到的那部分股份的真实经济成本——一份只看已成交交易的盈亏报表，会悄无声息地把这部分完全遗漏掉。

总实现盈亏差 = 5,000 + 6,300 + 2,000 = **13,300 美元**，相对 500 万美元的决策价格名义金额，约合 27 个基点。这个分解的意义在于：一个单一的混合"成本"数字，无法告诉你问题出在交易台交接太慢（延迟）、算法本身不好（执行），还是算法对难成交的股份放弃得太早（机会成本）——这是三种完全不同的修复方向。
