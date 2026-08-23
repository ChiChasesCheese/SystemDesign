---
id: carry-concept-cross-asset-unification
node: carry.concept
type: qa
---
## Q
Koijen, Moskowitz, Pedersen, and Vrugt (2018) show that the same
"unchanged-price return" definition of carry, computed purely off each asset
class's own curve, predicts future returns not just in FX but in equities,
global bonds, and commodities as well. What does this generality actually
buy you as a portfolio construction argument, and what does it explicitly
not buy you?

## A
**It buys the argument that carry is a genuine, general phenomenon rather
than an FX-specific quirk of interest-rate differentials.** Equity carry
(roughly the dividend yield minus the real risk-free rate), bond carry
(the yield curve's slope/roll-down), and commodity carry (the futures
curve's backwardation or contango) are all computed the same way — the
return you'd earn with the price frozen — and all of them separately predict
which asset will do better going forward. That commonality means carry
strategies can be built and combined across very different asset classes
using one unified signal, rather than needing a bespoke theory for every
market.

**It does not buy you diversification of the underlying risk.** Because
every one of these carry positions is compensation for bearing some version
of a risk that shows up in a broad, correlated risk-off event — currency
devaluation, credit/liquidity stress, demand collapse — combining carry
across asset classes smooths day-to-day noise (the individual sources of
carry are not perfectly correlated in normal times) but does not remove the
shared tail exposure. In a systemic deleveraging event, FX carry, bond
carry, and commodity carry have historically been hit at the same time,
because "risk appetite falls sharply" is the common trigger behind all of
them — the unification is real, and so is the shared crash.

## Q zh
Koijen、Moskowitz、Pedersen 和 Vrugt(2018)证明,同一个"价格不变时的收
益"carry 定义,只要单纯从每个资产类别自身的曲线算出来,不仅能预测 FX 的未
来收益,也能预测股票、全球债券和商品的未来收益。这种普遍性作为一个组合构
建的论据,到底能带来什么?它明确又不能带来什么?

## A zh
**它带来的论据是:carry 是一个真正普遍存在的现象,而不是利率差在 FX 市场
里的一个特有小把戏。** 股票 carry(大致是股息收益率减去实际无风险利率)、
债券 carry(收益率曲线的斜率/roll-down)、商品 carry(期货曲线的
backwardation 或 contango),都是用同一种方式算出来的——把价格冻结时能赚
到的收益——而且它们各自都能分别预测哪个资产未来表现会更好。这种共通性意
味着,carry 策略可以用同一个统一的信号在非常不同的资产类别之间构建和组
合,而不需要为每个市场单独设计一套理论。

**它不能带来的是对底层风险的分散。** 因为这里的每一个 carry 头寸,都是在
为承担某种版本的、会在一次广泛的、相关性趋同的风险规避事件中同时出现的风
险(货币贬值、信用/流动性压力、需求崩溃)收取补偿,把不同资产类别的 carry
组合在一起,能平滑掉日常噪音(正常时期这些 carry 的来源并非完全相关),但
无法消除共同的尾部暴露。在一次系统性去杠杆事件中,FX carry、债券 carry 和
商品 carry 历史上都是同时被打击的,因为"风险偏好骤降"正是它们背后共同的
触发因素——这种统一性是真实的,同样真实的还有它们共同的崩溃。
