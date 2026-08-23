---
id: backtest-dsr-mintrl
node: backtest.overfitting.deflated-sharpe
type: qa
---
## Q
A strategy has been live for 8 months (~170 trading days) with an annualized Sharpe of 1.2. A risk manager asks whether it's ready to size up. What question does Minimum Track Record Length (MinTRL) actually answer, and why might the honest answer be "wait another two to three years" even though the point estimate already looks good?

## A
**MinTRL inverts the PSR question.** PSR asks "given n observations, how confident am I the true Sharpe exceeds a benchmark?" MinTRL asks the reverse: "given this *observed* Sharpe (and its skew/kurtosis), how many observations n would I need before I could reject 'true Sharpe ≤ benchmark' at a chosen confidence level, say 95%?" In plain terms, it answers exactly: **how long does this track record need to run before I could tell it apart from luck?**

n* ≈ 1 + [1 − γ₃·ŜR + ((γ₄−1)/4)·ŜR²] · [Z⁻¹(confidence) / (ŜR − SR*)]²

The required n scales with 1/(ŜR − benchmark)² — so it grows fast as the observed edge shrinks toward the benchmark — and is inflated further by negative skew or excess kurtosis in the return stream, both of which widen the estimator's effective noise. With only ~170 daily observations and a Sharpe of 1.2, this formula can easily require several **years**, not months, of further data before 95% confidence is reached, because a Sharpe estimated from 8 months of daily returns has a very wide sampling distribution — the point estimate "1.2" is compatible with a wide range of true Sharpes, including numbers near zero. Sizing up on the point estimate alone means sizing up on a number whose confidence interval still plausibly contains zero; MinTRL is what turns "it looks good" into an actual answer for "for how long has it looked good enough."

## Q zh
一个策略已经实盘运行了 8 个月（约 170 个交易日），年化 Sharpe 为 1.2。风控经理问这是否已经可以加大仓位。Minimum Track Record Length（MinTRL，最小业绩记录长度）实际回答的是什么问题？为什么即便当前的点估计已经"看起来不错"，诚实的答案也可能是"再等两三年"？

## A zh
**MinTRL 把 PSR 的问题反过来问。** PSR 问的是"给定 n 个观测，我有多大信心认为真实 Sharpe 超过某个基准？" MinTRL 问的是反问题："给定这个**观测到**的 Sharpe（及其偏度/峰度），我需要多少观测 n，才能在某个选定的置信水平（比如 95%）下拒绝'真实 Sharpe ≤ 基准'？"说白了，它回答的正是：**这份业绩记录需要跑多久，我才能把它和运气区分开？**

n* ≈ 1 + [1 − γ₃·ŜR + ((γ₄−1)/4)·ŜR²] · [Z⁻¹(置信度) / (ŜR − SR*)]²

所需的 n 随 1/(ŜR − 基准)² 增长——所以当观测到的 edge 越接近基准，n 就增长得越快——而收益序列中的负偏度或超额峰度会进一步放大它，两者都会拉宽估计量的有效噪音。只有约 170 个日频观测、Sharpe 1.2 的情况下，这个公式很容易要求再等**数年**而非数月的数据，才能达到 95% 置信度，因为用 8 个月日频收益估计出来的 Sharpe，其抽样分布相当宽——点估计"1.2"其实和一大片真实 Sharpe 值都相容，其中包括接近零的数字。仅凭点估计就加仓，等于在一个置信区间很可能仍然包含零的数字上加仓；MinTRL 做的，就是把"看起来不错"变成对"它已经好到足以确认了多久"这个问题的真正回答。
