---
id: foundations-capm-pricing-model-vs-risk-control
node: foundations.capm
type: qa
---
## Q
CAPM is empirically rejected as a pricing model — value, momentum, quality, size, and the flat-SML anomaly all show returns beta alone cannot explain. Given that, why do practitioners still compute and use beta constantly in portfolio construction? Distinguish CAPM-as-pricing-model from beta-as-risk-control.

## A
**As a pricing model, CAPM's claim is that beta is the *only* characteristic that should command extra expected return — that claim is false**, since the anomalies above (value, momentum, quality, size, betting-against-beta itself) are statistically robust patterns in returns that a portfolio's beta alone does not explain, meaning CAPM systematically mis-prices many assets relative to what actually happens.

**As a risk-control tool, beta doesn't need CAPM's pricing claim to be true at all — it is simply a measured statistical sensitivity of an asset (or portfolio) to market-wide moves, useful regardless of whether that sensitivity is "correctly priced."** A portfolio manager uses beta to hedge unwanted market exposure (shorting an index future against a long stock book to isolate stock-specific bets), to size positions so that a strategy's realized risk matches a target, and to construct "beta-neutral" long-short portfolios that isolate a factor bet (such as value or momentum) from broad market direction. None of these uses requires believing beta fully explains expected returns — they only require that beta accurately measures market sensitivity, which remains true even after CAPM fails as a pricing theory. This is why beta survived decades of CAPM's empirical rejection as a pricing model: its role as a risk-measurement and risk-neutralization tool never depended on the pricing claim being correct.

## Q zh
CAPM 作为一个定价模型，在实证上已经被推翻——价值、动量、质量、规模因子，以及"证券市场线过平"这个异象，都显示出仅凭 beta 无法解释的收益。既然如此，为什么从业者在构建组合时还在不停地计算和使用 beta？请区分"作为定价模型的 CAPM"和"作为风险控制工具的 beta"。

## A zh
**作为定价模型，CAPM 的主张是 beta 是唯一应当带来额外预期收益的特征——这个主张是错的**，因为前面提到的那些异象（价值、动量、质量、规模，以及 betting-against-beta 本身）都是统计上稳健、仅凭组合的 beta 无法解释的收益规律，这意味着相对于实际发生的情况，CAPM 系统性地给很多资产定错了价。

**但作为风险控制工具，beta 根本不需要 CAPM 的定价主张为真——它只是一个衡量某项资产（或组合）对全市场变动的敏感度的统计量，不管这份敏感度是否被"正确定价"，它都有用。** 组合经理会用 beta 来对冲不想要的市场敞口（比如做空一份指数期货来对冲多头股票仓位，从而分离出纯粹的个股观点）、用它来做仓位大小的控制，让策略实现的风险匹配目标水平，以及构建"beta 中性"的多空组合，把某个因子观点（比如价值或动量）从大盘方向性敞口中隔离出来。这些用法都不需要相信 beta 能完全解释预期收益——它们只需要 beta 能准确衡量市场敏感度，而这一点即便在 CAPM 作为定价理论失败之后依然成立。这正是为什么 beta 能在 CAPM 作为定价模型被实证推翻几十年之后依然存活：它作为风险度量和风险中性化工具的角色，从来就不依赖于那个定价主张是否正确。
