---
id: backtest-mt-trials-discipline
node: backtest.overfitting.multiple-testing
type: qa
---
## Q
You want a research process where a reported Sharpe can be trusted without having to trust the researcher's memory of what they tried. Name three concrete mechanisms that make this mechanical rather than a matter of self-discipline, and what failure each one specifically blocks.

## A
**Pre-registration** — commit to the strategy specification (universe, signal definition, parameters, evaluation window) in writing *before* touching the evaluation data. This blocks post-hoc rationalization: without it, a researcher can always describe whatever survived as "the hypothesis," making every result look like a single confirmed prediction instead of the one that happened to work.

**A trials log / ledger** — a system that mechanically records every backtest run against a given return stream or strategy family, and accumulates the count across sessions and researchers rather than resetting per run. This blocks undercounting: the researcher doesn't get to decide what counts as a "real" trial versus a quick check — every run that touched the data is logged, and the cumulative count (not just the current session's) is what feeds `n_trials` in a deflated-Sharpe-style gate, so trying something on Monday and something similar on Friday doesn't quietly reset the search size to zero.

**A holdout that literally cannot be queried during search** — data that either didn't exist yet when the search happened (true forward/out-of-sample-in-time validation) or is walled off by infrastructure so no query against it is possible until a final, single, logged decision point. This blocks the reusable-holdout leak: a holdout you *can* look at, you eventually will, and each look is a trial by another name (see the reusable-holdout problem) — the only way to guarantee zero adaptive contamination is to make it physically impossible to query early.

Together these turn "did you overfit by searching" from a question about the researcher's honesty into a question the infrastructure answers on its own.

## Q zh
你希望建立一套研究流程，让报告出来的 Sharpe 值得信任，而不必依赖研究者对自己试过什么的记忆。请说出三个具体机制，让这件事变成机制性的、而不是靠自觉——并说明每个机制分别堵住了哪种具体的失败方式。

## A zh
**预注册（pre-registration）**——在接触评估数据**之前**，就以书面形式确定策略规格（股票池、信号定义、参数、评估窗口）。这堵住了事后合理化：没有它，研究者总能把最终存活下来的那个描述成"原本的假设"，让每个结果看起来都像是一次被验证的预测，而不是碰巧奏效的那一个。

**试验记录 / 账本（trials log / ledger）**——一个机制性记录针对某个收益序列或策略家族进行的每一次回测运行的系统，且跨会话、跨研究者累计计数，而不是每次运行都清零。这堵住了漏记：研究者不能自己决定什么算"正式"试验、什么算"随手看看"——每一次接触过数据的运行都会被记录，而喂进 deflated-Sharpe 式闸门里的 `n_trials` 是**累计**计数（而不只是当前会话的计数），所以周一试了一个、周五又试了个类似的，搜索规模不会被悄悄清零重来。

**一份在搜索期间物理上无法被查询的留出集**——要么是搜索发生时根本还不存在的数据（真正的 forward / 出设计期验证），要么由基础设施隔离，使得在一个最终、单一、被记录的决策点之前，任何对它的查询都不可能发生。这堵住了可重用留出集式的信息泄漏：一份你**可以**看的留出集，你迟早会看，而每一次看都是换了个名字的一次试验（见可重用留出集问题）——唯一能保证零自适应污染的办法，就是让提前查询在物理上不可能发生。

三者合在一起，把"你是不是靠搜索过拟合了"从一个关于研究者是否诚实的问题，变成了一个基础设施自己就能回答的问题。
