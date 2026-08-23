---
id: backtest-mt-expected-max-sharpe-null
node: backtest.overfitting.multiple-testing
type: qa
---
## Q
A colleague reports "our search found a strategy with backtest Sharpe 1.8" over roughly 3 years of daily returns, and doesn't say how many parameter combinations were tried. Using the fact that under pure noise (zero true skill) the *expected* value of the best Sharpe out of N independent trials rises with N, is 1.8 believable evidence of skill if N=10? What about if N=2000?

## A
Under the null (true Sharpe = 0), the Sharpe of any one trial is a noisy draw with standard error roughly σ_SR ≈ 1/√(years of data) (ignoring skew/kurtosis, a simplification the exact formulas below relax). The **expected maximum** Sharpe across N independent such draws (Bailey & López de Prado) is

E[max SR_N] ≈ σ_SR · [(1-γ)·Z⁻¹(1 - 1/N) + γ·Z⁻¹(1 - 1/(Ne))]

where γ ≈ 0.5772 (Euler-Mascheroni) and Z⁻¹ is the standard normal quantile. This is monotonically increasing in N: the more noise draws you take the max over, the higher the max climbs, purely from sampling — no skill required.

Plugging in 3 years (σ_SR ≈ 1/√3 ≈ 0.577): at **N=10**, E[max SR_N] ≈ 0.91 — well below the reported 1.8, so 1.8 stands out as unusually good and is plausible evidence of real skill. At **N=2000** — a scale easily reached by a Bayesian hyperparameter search across a few hundred epochs and several parameters — E[max SR_N] ≈ **2.0**, *above* the reported 1.8. The identical headline number now means the opposite: 1.8 is *less* than what pure noise alone would be expected to produce at that search scale, so it is not evidence of skill at all. This is why the trial count, not the Sharpe, is the number that determines whether a backtest result means anything — and it is exactly the number that write-ups routinely omit, because nobody logs how many things they quietly tried before the one that looked good.

## Q zh
一位同事报告说"我们的搜索找到了一个回测 Sharpe 为 1.8 的策略"，数据大约是 3 年的日频收益，但没有说明搜索了多少组参数组合。已知在纯噪音（真实 skill 为零）下，N 次独立试验里**最优 Sharpe 的期望值**会随 N 增大而上升——如果 N=10，1.8 是不是可信的 skill 证据？如果 N=2000 呢？

## A zh
在零假设下（真实 Sharpe = 0），任意一次试验的 Sharpe 都是一个带噪音的抽样，标准误差大致为 σ_SR ≈ 1/√(数据年数)（忽略偏度/峰度，这是下面精确公式会放松的一个简化）。N 次独立这样的抽样中**最大 Sharpe 的期望值**（Bailey & López de Prado）是

E[max SR_N] ≈ σ_SR · [(1-γ)·Z⁻¹(1 - 1/N) + γ·Z⁻¹(1 - 1/(Ne))]

其中 γ ≈ 0.5772（Euler-Mascheroni 常数），Z⁻¹ 是标准正态分位函数。这个量随 N **单调递增**：你在越多噪音抽样上取 max，max 就会被纯抽样效应推得越高——不需要任何真实 skill。

代入 3 年数据（σ_SR ≈ 1/√3 ≈ 0.577）：当 **N=10** 时，E[max SR_N] ≈ 0.91——远低于报告的 1.8，所以 1.8 显得异常突出，可以合理地视为真实 skill 的证据。当 **N=2000**（一次贝叶斯超参搜索跑几百个 epoch、扫几个参数，很容易达到这个量级）时，E[max SR_N] ≈ **2.0**，*高于*报告的 1.8。同一个头条数字，现在意味着相反的结论：1.8 **低于**纯噪音在这个搜索规模下本就该产生的水平，所以完全不能算 skill 的证据。这就是为什么决定一个回测结果是否有意义的是试验次数，而不是 Sharpe 本身——而这恰恰是写报告时最常被省略的数字，因为没人会记录自己在得到那个"好看"的结果之前，悄悄试过多少次。
