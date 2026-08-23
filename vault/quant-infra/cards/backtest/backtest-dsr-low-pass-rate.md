---
id: backtest-dsr-low-pass-rate
node: backtest.overfitting.deflated-sharpe
type: qa
---
## Q
A research pipeline runs 90 backtests across 44 strategy families and only 1 clears the deflated-Sharpe gate — a 2% pass rate. Several rejected strategies had raw Sharpes that look respectable in isolation (0.79, 0.65). Is a 2% pass rate evidence that the framework (or the researchers) are bad at finding edges, and what would a much higher pass rate actually indicate?

## A
**A low pass rate is exactly what a correctly calibrated deflation gate produces once it accounts for how many strategies and internal parameter variations were actually searched.** Raw Sharpes like 0.79 or 0.65 look fine as isolated numbers, but once dozens of families — each with its own internal parameter sweep — are counted honestly as trials, the expected-maximum-Sharpe-under-noise benchmark for that many trials can itself sit close to those values, so DSR correctly discounts them to statistically indistinguishable from luck. This matches the base rate found in the published academic literature: once multiple-testing corrections are applied to the thousands of factors ever proposed (Harvey, Liu & Zhu 2016), the majority don't hold up either.

A DSR failing on a specific strategy means "this Sharpe is not distinguishable from the best of the N trials this process actually searched" — it is not a claim that no edges exist in the data at all. The signal to actually worry about is the **opposite** one: a research process where most submissions pass is either undercounting its trials (not crediting every parameter sweep, every "quick check," every re-run to `n_trials`) or has its benchmark set too low — a high pass rate is the tell that the gate isn't doing its job, not that the researchers got unusually lucky at scale. A rare, hard-won pass under an honestly-counted gate is worth far more than a frequent one under a loose or miscounted gate.

## Q zh
一条研究管线在 44 个策略家族上跑了 90 次回测，只有 1 个过了 deflated-Sharpe 闸门——通过率 2%。几个被拒的策略单看原始 Sharpe 还算体面（0.79、0.65）。2% 的通过率是不是说明这个框架（或研究者）不擅长找 edge？一个高得多的通过率实际上又说明了什么？

## A zh
**一旦正确地把实际搜索过的策略数量和内部参数变体计入，一个校准正确的 deflation 闸门产出的正是这种低通过率。** 0.79、0.65 这样的原始 Sharpe，单独看还算体面，但一旦把几十个家族——每个又各自带内部参数扫描——都诚实地算作试验，这么多试验对应的、纯噪音下期望最大 Sharpe 的基准本身就可能接近这些数值，于是 DSR 正确地把它们折扣到"统计上和运气无法区分"。这与已发表学术文献中的基础比率是一致的：一旦对历史上被提出过的成千上万个因子应用多重检验校正（Harvey, Liu & Zhu 2016），大多数同样站不住脚。

某个策略 DSR 不过关，意味着"这个 Sharpe 和这套流程实际搜索过的 N 次试验里最好的那个没法区分"——它并不是在断言数据里根本不存在任何 edge。真正该警惕的信号方向是**相反**的：如果大多数提交都能通过，那要么是这个研究流程漏记了试验（没有把每一次参数扫描、每一次"随手一试"、每一次重跑都计入 `n_trials`），要么是基准定得太低——**高通过率是闸门没在起作用的迹象，而不是研究者大规模走运的证据**。在一个诚实计数的闸门下罕见、来之不易的通过，远比在一个宽松或漏记的闸门下频繁的通过更有价值。
