---
id: carry-commodities-backwardation-contango-roll-yield
node: carry.commodities
type: qa
---
## Q
A long-only commodity index has to sell its expiring near-month future and
buy the next-dated contract every month to stay invested. If the curve is in
steep contango, what does this monthly roll do to returns even if the spot
price is flat, and why is this exactly the opposite outcome from a
backwardated curve?

## A
**In contango, the roll is a structural loss even with a flat spot price.**
The expiring contract is being sold at a lower (near-month) price, and the
replacement contract has to be bought at a higher (further-dated) price —
that's what contango means, the curve rising with maturity. Rolling
month after month means systematically selling low and buying high on the
curve itself, which drags on returns regardless of what the spot price does
— this is why long-only commodity index products and ETFs (the standard
example being oil products like USO during 2020's deep contango) can lose
significant value through roll even while the underlying spot price is
roughly unchanged or only modestly down.

**Backwardation produces the mirror-image, favorable outcome.** There, the
expiring near-month contract is priced above the further-dated replacement,
so rolling means selling high and buying low — a positive roll yield added
on top of any spot price change. This is why "carry" for a long commodity
futures position is not the same question as "will the spot price go up" —
a trader can be right about spot direction and still lose money to a
sufficiently negative roll in deep contango, or be flat on spot and still
profit from a strongly backwardated curve.

## Q zh
一个纯多头的商品指数每个月都需要卖出即将到期的近月合约、买入下一份远月合
约以维持持仓。如果曲线处于深度 contango,即便现货价格持平,这个每月展期
的动作会对收益造成什么影响?这为什么和一条 backwardation 曲线的结果正好相
反?

## A zh
**在 contango 下,即使现货价格持平,展期本身在结构上就是一种亏损。** 到期
合约是以较低的(近月)价格卖出的,而替换合约必须以较高的(远月)价格买
入——这正是 contango 的含义,曲线随期限延长而上升。一个月接一个月地展期,
意味着在曲线本身上系统性地低卖高买,无论现货价格怎么走,这都会拖累收
益——这正是为什么纯多头的商品指数产品和 ETF(标准例子是 2020 年深度
contango 时期的原油产品如 USO)即便标的现货价格大致持平甚至只是小幅下跌,
也可能因为展期而损失可观的价值。

**Backwardation 则产生镜像的、有利的结果。** 在那种情况下,即将到期的近月
合约价格高于将要替换它的远月合约,所以展期意味着高卖低买——在任何现货价格
变动之上再叠加一份正的展期收益。这就是为什么对一个多头商品期货头寸而言,
"carry"和"现货价格会不会涨"根本不是同一个问题——一个交易者可以在现货方
向上判断正确,却仍然因为深度 contango 下足够负的展期收益而亏钱;也可以在
现货上完全持平,却仍然因为一条强烈 backwardation 的曲线而获利。
