---
id: foundations-capm-flat-empirical-sml-bab
node: foundations.capm
type: qa
---
## Q
If you sort US stocks into portfolios by beta and plot their realized average returns against beta over long historical samples, the resulting line is much flatter than the security market line CAPM predicts — high-beta stocks earn less than CAPM says they should, and low-beta stocks earn more. What is this finding, when was it first documented, and what trading strategy did it motivate?

## A
**The empirical security market line is flatter than CAPM's theoretical one — often close to flat, sometimes even downward-sloping among the highest-beta stocks — meaning realized returns barely rise with beta at all, contrary to the model's central prediction.** This was first documented by Black, Jensen, and Scholes (1972) using US stock portfolios sorted on beta, and has been replicated across markets and time periods since.

Frazzini and Pedersen (2014) formalized this into the "Betting Against Beta" (BAB) framework and strategy: a portfolio that goes long low-beta assets (leveraged up to match the market's overall risk level) and short high-beta assets (de-leveraged to match), designed to be beta-neutral while capturing the flat-slope anomaly as pure return. Their explanation is that many real-world investors face leverage constraints — they cannot borrow freely to lever up a low-risk portfolio to their desired return target, so instead they buy inherently high-beta, high-volatility ("lottery-like") stocks to reach for return without borrowing. That crowds up the price (and depresses the future return) of high-beta stocks specifically, and leaves low-beta stocks relatively cheap — flattening the empirical line exactly where CAPM predicts it should be steepest.

## Q zh
如果把美股按 beta 分组，用长期历史样本画出各组已实现平均收益相对 beta 的关系，得到的这条线会比 CAPM 预测的证券市场线（SML）平得多——高 beta 股票赚得比 CAPM 说的要少，低 beta 股票赚得比 CAPM 说的要多。这个发现是什么？最早是什么时候被记录下来的？它催生了什么交易策略？

## A zh
**实证的证券市场线比 CAPM 理论上的那条线要平得多——常常接近水平，在 beta 最高的那批股票里甚至会向下倾斜——也就是说，已实现收益几乎不随 beta 上升而上升，与模型的核心预测相悖。** 这一现象最早由 Black、Jensen 和 Scholes（1972）用按 beta 分组的美股组合记录下来，此后在不同市场、不同时期被反复验证。

Frazzini 和 Pedersen（2014）把这个现象系统化成了"Betting Against Beta"（BAB）框架和策略：做多低 beta 资产（加杠杆使其风险水平与市场整体匹配），做空高 beta 资产（去杠杆使其匹配），整个组合设计成 beta 中性，从而把这条"过平"的斜率异象本身，转化成纯粹的收益。他们给出的解释是：现实中很多投资者面临杠杆约束——他们无法自由借入资金，把一个低风险组合加杠杆做到自己想要的收益目标，于是转而直接买入天生高 beta、高波动率（"彩票型"）的股票，不靠借钱去够收益。这就把资金特别拥挤地推高了高 beta 股票的价格（压低了它未来的收益），同时让低 beta 股票相对便宜——正好在 CAPM 预测这条线应该最陡的地方，把它压平了。
