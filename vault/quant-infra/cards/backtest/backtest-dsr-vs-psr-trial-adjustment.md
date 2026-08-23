---
id: backtest-dsr-vs-psr-trial-adjustment
node: backtest.overfitting.deflated-sharpe
type: qa
---
## Q
For a return series, PSR against a benchmark Sharpe of 0 comes back 0.98 (98% confidence the true Sharpe exceeds 0). The same strategy, evaluated as one of 300 parameter combinations that were searched to find it, has a Deflated Sharpe Ratio (DSR) of 0.31. Which number should drive a go/no-go decision, and what changed between the two calculations?

## A
**PSR and DSR run the exact same formula against different benchmarks.** PSR asks "is ŜR significantly above a chosen fixed benchmark SR*, given this sample's length, skew and kurtosis" — and 0.98 against SR*=0 just says the number is unlikely to be indistinguishable from zero skill *in isolation*. It says nothing about how that particular configuration was found. **DSR replaces the fixed benchmark SR* with SR*_N — the expected maximum Sharpe that N trials of pure noise would be expected to produce** (the same expected-max-Sharpe quantity from multiple-testing theory) — and then runs the identical PSR formula against that inflated bar instead of 0.

Going from PSR=0.98 (vs. 0) to DSR=0.31 (vs. SR*_300) means: this Sharpe comfortably clears "better than doing nothing," but does **not** clear "better than the best of 300 noise draws," which over a few years of data can itself sit well above 1. **DSR is the number that should drive the decision**, because PSR-against-zero is exactly the statistic multiple testing exploits — you can always find a result that beats a benchmark of 0 if you search hard enough, so a PSR computed without reference to N answers a question nobody asked (is this better than nothing) instead of the one that matters (is this better than what nothing-plus-N-guesses would produce). A DSR of 0.31 doesn't mean the strategy has zero real edge in an absolute sense; it means the observed number is statistically indistinguishable from what this search process would have handed you even with zero real edge.

## Q zh
针对一段收益序列，以基准 Sharpe = 0 计算的 PSR 是 0.98（即有 98% 的置信度认为真实 Sharpe 超过 0）。同一个策略，作为搜索出它的 300 组参数组合中的一个来评估时，Deflated Sharpe Ratio（DSR）是 0.31。哪个数字应该用来决定是否上线？这两次计算之间发生了什么变化？

## A zh
**PSR 和 DSR 用的是完全同一套公式，只是针对不同的基准。** PSR 问的是"给定样本长度、偏度、峰度，ŜR 是否显著高于某个选定的固定基准 SR*"——0.98（相对 SR*=0）只是说，**孤立地看**，这个数字不太可能和零 skill 无法区分。它对这个具体配置是怎么被找出来的完全没有回答。**DSR 则把固定基准 SR* 换成 SR*_N——N 次纯噪音试验本该产生的期望最大 Sharpe**（和多重检验理论里那个期望最大 Sharpe 是同一个量）——然后用同一套 PSR 公式去对这个被抬高的门槛做检验，而不是对 0。

从 PSR=0.98（相对 0）变成 DSR=0.31（相对 SR*_300）意味着：这个 Sharpe 轻松超过了"比什么都不做强"，但**没有**超过"比 300 次噪音抽样里最好的那次强"——而后者在几年数据上本身就可能远超过 1。**应该用 DSR 来做决策**，因为"相对 0 的 PSR"正是多重检验能钻的空子——只要搜得够多，你总能找到一个超过基准 0 的结果，所以一个不考虑 N 就算出来的 PSR，回答的是没人真正关心的问题（这比什么都不做强吗），而不是真正要紧的问题（这比"什么都不做外加搜了 N 次"强吗）。DSR 为 0.31 并不意味着这个策略绝对没有真实 edge；它意味着观测到的数字，在统计上和"这套搜索流程即便毫无真实 edge 也会给你的结果"没有区别。
