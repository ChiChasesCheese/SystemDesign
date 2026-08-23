---
id: backtest-dsr-psr-skew-kurtosis
node: backtest.overfitting.deflated-sharpe
type: qa
---
## Q
Two strategies both report an annualized Sharpe of 1.5 over the same 5-year backtest. Strategy A's returns are close to normal (skew ≈ 0, excess kurtosis ≈ 0). Strategy B looks like a short-volatility strategy — frequent small gains, rare large losses (skew ≈ -2, excess kurtosis ≈ 6). Why doesn't the identical Sharpe mean the identical amount of trustworthy edge, and what does the Probabilistic Sharpe Ratio (PSR) do about it?

## A
**The Sharpe ratio is a mean-over-standard-deviation statistic, and it is only a sufficient description of risk if returns are close to i.i.d. normal.** Strategy B's shape — many small wins funding rare large losses — is exactly what negative skew and excess kurtosis describe: a standard deviation computed mostly from small, quiet moves understates the size of the tail loss that hasn't shown up yet in a 5-year sample, so the same Sharpe hides much more downside risk than Strategy A's. Separately, fat tails and skew also inflate the *sampling variance of the Sharpe estimator itself*, so the same observed 1.5 is a noisier, less reliable estimate for B than for A even setting aside the true risk difference.

PSR builds both effects directly into a confidence statement instead of leaving Sharpe as a bare number:

PSR(SR*) = Φ[ (ŜR − SR*)·√(n−1) / √(1 − γ₃·ŜR + ((γ₄−1)/4)·ŜR²) ]

where γ₃, γ₄ are the sample skew and kurtosis, SR* is a benchmark Sharpe (often 0), and n is the number of observations. For Strategy B, γ₃ < 0 makes `−γ₃·ŜR` positive (adding to the denominator) and γ₄ > 3 (excess kurtosis > 0) also inflates the denominator — both push PSR *down* relative to Strategy A's, whose γ₃ ≈ 0 and γ₄ ≈ 3 leave the denominator near its normal-returns baseline. So two funds with an identical 1.5 headline Sharpe can produce meaningfully different PSRs — B's confidence that its true Sharpe exceeds the benchmark comes out lower, correctly flagging that its return shape makes the same number less trustworthy, not just riskier in a way variance alone would show.

## Q zh
两个策略在同样的 5 年回测窗口上都报告年化 Sharpe 1.5。策略 A 的收益接近正态分布（偏度 ≈ 0，超额峰度 ≈ 0）。策略 B 看起来像一个卖波动率策略——频繁的小额盈利，偶尔的大额亏损（偏度 ≈ -2，超额峰度 ≈ 6）。为什么相同的 Sharpe 不代表相同程度的可信 edge？Probabilistic Sharpe Ratio（PSR）对此做了什么？

## A zh
**Sharpe 比率本质上是"均值 / 标准差"这样一个统计量，只有在收益近似独立同分布的正态分布时，它才足以描述风险。** 策略 B 的形态——大量小额盈利支撑起偶尔的大额亏损——恰恰就是负偏度和超额峰度所描述的：一个主要由小幅、平静波动算出来的标准差，会低估那笔在 5 年样本里还没出现过的尾部损失的真实大小，所以同样的 Sharpe 在 B 身上掩盖的下行风险，比在 A 身上多得多。另外，肥尾和偏度还会放大 **Sharpe 估计量本身的抽样方差**，所以即便撇开真实风险的差异不谈，同样观测到的 1.5，对 B 而言也是一个噪音更大、更不可靠的估计。

PSR 把这两个效应直接内建进一个置信度陈述里，而不是让 Sharpe 停留在一个孤立的数字上：

PSR(SR*) = Φ[ (ŜR − SR*)·√(n−1) / √(1 − γ₃·ŜR + ((γ₄−1)/4)·ŜR²) ]

其中 γ₃、γ₄ 是样本偏度和峰度，SR* 是基准 Sharpe（常取 0），n 是观测数。对策略 B 而言，γ₃ < 0 使得 `−γ₃·ŜR` 为正（加大分母），γ₄ > 3（超额峰度 > 0）同样会放大分母——两者都把 PSR 相对策略 A **往下拉**；而 A 的 γ₃ ≈ 0、γ₄ ≈ 3 让分母基本停留在正态收益的基线水平。于是两只头条 Sharpe 同样是 1.5 的基金，PSR 可以有意义地不同——B 的"真实 Sharpe 超过基准"的置信度更低，正确地标记出：它的收益形态让同一个数字更不可信，而不只是用方差就能看出来的"风险更高"。
