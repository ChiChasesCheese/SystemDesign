---
id: backtest-mt-not-lookahead
node: backtest.overfitting.multiple-testing
type: qa
---
## Q
Your data pipeline is airtight — point-in-time fundamentals, purged and embargoed cross-validation, no feature ever computed with information from after the trade date. A strategy built on it shows a clean Sharpe of 1.8 in backtest and craters live. Given that lookahead has been ruled out, what else could explain the collapse, and why doesn't eliminating lookahead also eliminate this?

## A
**Multiple testing and lookahead are orthogonal failure modes** — a pipeline can be perfectly causal on every single run and still produce a fabricated Sharpe if many runs were compared and the best one reported. Lookahead is about whether *one* backtest, evaluated in isolation, secretly used information it couldn't have had at the time; multiple testing is about whether the 1.8 you're looking at is the max of, say, 500 equally causal, equally leakage-free backtests over different parameters or feature sets, in which case its size is explained by *how many honest draws you took*, not by any of them being individually cheating.

Nothing about purging or embargoing addresses this, because purging protects a single train/test boundary within one run — it says nothing about what happens when you run the causal, leakage-free pipeline 500 times and keep the best output. The fix is a different mechanism entirely: track `n_trials` (the number of causal-but-searched configurations) and discount the reported Sharpe through a deflated-Sharpe or similar trial-adjusted test, independent of and in addition to whatever leakage checks already passed. A strategy can pass every point-in-time and purging check and still be pure selection-on-noise.

## Q zh
你的数据管线无懈可击——基本面数据是 point-in-time 的，交叉验证做了 purge 和 embargo，没有任何特征在计算时用到过交易日之后的信息。基于它构建的策略在回测中显示出干净的 Sharpe 1.8，实盘却崩了。既然已经排除了前视（lookahead），还有什么能解释这次崩盘？为什么排除前视并不能同时排除这个问题？

## A zh
**多重检验和前视是两个正交的失败模式**——一条管线可以在每一次单独运行中都完全因果自洽，却仍然因为比较了很多次运行、只报告最好的那次，而产出一个虚构的 Sharpe。前视问的是**单次**回测本身是否偷偷用到了在那个时点不可能拥有的信息；多重检验问的是你看到的这个 1.8，是不是从比如说 500 个同样因果自洽、同样没有泄漏的回测（跨不同参数或特征集）里挑出来的最大值——如果是，它的大小是由**你抽了多少次诚实的样本**解释的，而不是任何一次抽样本身在作弊。

purge 或 embargo 对此完全无能为力，因为 purge 保护的是**单次运行内**的一条训练/测试边界——它对"把这条因果自洽、无泄漏的管线跑 500 次、只留最好的输出"这件事毫无约束。修复需要一个完全不同的机制：追踪 `n_trials`（搜索过的、因果自洽的配置数量），用 deflated Sharpe 或类似的、按试验数调整的检验去折扣报告出来的 Sharpe——这独立于、且要叠加在已经通过的任何泄漏检查之上。一个策略完全可以通过每一项 point-in-time 和 purging 检查，却依然是对噪音的纯粹选择。
