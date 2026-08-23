---
id: backtest-pbo-degradation-plot
node: backtest.overfitting.pbo
type: qa
---
## Q
CSCV output includes a "degradation" plot: in-sample performance (rank or Sharpe) on one axis, the corresponding out-of-sample performance on the other, for every configuration across every split, with a fitted regression line. What does a strongly negative slope on that line tell you that the single PBO number doesn't, and why might a strategy family show a low PBO but still have a clearly negative-sloped degradation trend?

## A
**PBO only looks at where one configuration — the in-sample winner — lands out-of-sample, split by split; it's silent on everything the rest of the candidate set is doing.** The degradation plot regresses OOS performance against IS performance across *every* configuration and *every* split, not just the winner, so its slope answers a different question: as configurations get progressively better in-sample, do they get better or worse out-of-sample? A strongly negative slope means configurations that look *more* impressive in-sample are systematically the ones that do *worse* out-of-sample — in-sample performance isn't merely uninformative here, it's actively anti-correlated with real performance past some point, which is the signature of a search that's climbing a noise surface (the harder a configuration is pushed to fit the IS data, the more that fit is pure overfit, and the worse it reverses OOS).

A family can post a moderate-to-low PBO (the single IS-best configuration doesn't fall below the OOS median in most splits) while still showing this negative trend, because PBO only samples the extreme point of the distribution — the winner — while the slope captures the *entire* IS-vs-OOS relationship across the whole candidate set. A family where the top handful of configurations are all reasonably close and none catastrophically overfit can still show a real negative slope driven by the weaker, more aggressively tuned configurations further down the ranking; PBO, by construction, can be blind to that because it never looks past the single best-performing entry per split.

## Q zh
CSCV 的输出里包含一张"退化（degradation）"图：一个轴是样本内表现（排名或 Sharpe），另一个轴是每个配置、每次切分对应的样本外表现，并配有一条拟合回归线。这条线明显为负的斜率，能告诉你哪些单纯一个 PBO 数字告诉不了的信息？为什么一个策略家族可能 PBO 较低，却仍然呈现出明显负斜率的退化趋势？

## A zh
**PBO 只看一个配置——样本内赢家——在每次切分中的样本外落点；它对候选集合里其余配置的表现完全不置一词。** 退化图对**每一个**配置、**每一次**切分的样本外表现相对样本内表现做回归，而不仅仅是赢家，所以它的斜率回答的是另一个问题：随着配置在样本内表现变得越来越好，它们在样本外是变好还是变差？明显为负的斜率意味着，那些在样本内看起来**更亮眼**的配置，系统性地是样本外表现**更差**的那些——样本内表现在这里不只是没有信息量，而是过了某个点之后与真实表现**主动负相关**，这正是一个搜索正在攀爬噪音曲面的标志（一个配置被推得越努力去拟合样本内数据，这种拟合就越纯粹是过拟合，样本外反转就越严重）。

一个策略家族可能呈现中等偏低的 PBO（单一样本内最优配置在大多数切分中不会落到样本外中位数以下），却仍然表现出这种负向趋势，因为 PBO 只采样了分布里的一个极端点——赢家——而斜率捕捉的是**整个候选集合**上完整的样本内-样本外关系。一个头部若干配置都相当接近、没有哪个灾难性过拟合的家族，仍然可能因为排名更靠后、被更激进调参的那些较弱配置，而呈现真实的负斜率；PBO 从构造上就可能对此视而不见，因为它每次切分都只看单一表现最好的那一条。
