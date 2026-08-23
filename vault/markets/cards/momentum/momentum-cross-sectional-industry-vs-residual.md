---
id: momentum-cross-sectional-industry-vs-residual
node: momentum.cross-sectional
type: qa
---
## Q
Moskowitz and Grinblatt found that momentum built purely at the industry
level — buying the strongest-performing industries and shorting the
weakest — captures much of the profit usually attributed to individual-stock
momentum. What does "residual momentum" try to fix about this, and why isn't
it automatically the better version of the trade?

## A
**Industry momentum shows that a large share of "stock momentum" is really
just industries drifting** — an oil stock rallying with the whole energy
sector looks like stock-level momentum but is mostly a common, industry-wide
effect, not something specific to that company.

**Residual (idiosyncratic) momentum** tries to purify the signal: regress
each stock's return on market, industry, and other common factor exposures,
and rank stocks on their *residual* (stock-specific) cumulative return rather
than their raw return. In principle this isolates the part of momentum that
is truly about that company rather than about riding a factor or sector tide,
and it can dampen crash risk somewhat since much of the crash-prone loser
leg's damage traces to shared high-beta exposure rather than idiosyncratic
drift.

In practice it is not automatically better: stripping out common exposures
via regression can leave a signal that is mostly repackaged residual beta
rather than a distinct source of return, and its statistical significance can
be fragile once measured with proper multiple-testing discipline (a
deflated Sharpe ratio) — "purified" is not the same as "more real." The
question to ask of any residual-momentum construction is whether what is
left over is genuinely idiosyncratic information diffusion, or just a
different-looking repackaging of the same factor exposures it claimed to
remove.

## Q zh
Moskowitz 和 Grinblatt 发现,纯粹在行业层面构造的动量——买表现最强的行业、
空表现最弱的行业——能解释很大一部分通常被归功于个股动量的收益。"残差动量
(residual momentum)"想解决这里的什么问题?为什么它不会自动就是这个交易
更优的版本?

## A zh
**行业动量说明,很大一部分"个股动量"其实只是行业在漂移**——一只石油股跟着
整个能源板块上涨,看起来像是个股层面的动量,但其实主要是一个共同的、行业
层面的效应,而不是这家公司特有的东西。

**残差(特质)动量**试图把信号"提纯":把每只股票的收益对市场、行业和其他
共同因子暴露做回归,然后按**残差(股票特有)**累计收益而不是原始收益来排序。
原则上这能剥离出动量中真正属于这家公司本身、而不是搭上某个因子或板块顺风
车的那部分,而且因为崩盘风险较大的输家腿的伤害很大程度上来自共同的高 beta
暴露而非特质性漂移,它在一定程度上也能压低崩盘风险。

但实际上它并不会自动更优:通过回归剥离共同暴露之后,剩下的信号很可能大部分
是换了个皮的残差 beta,而不是一个真正独立的收益来源,而且一旦用恰当的多重
检验纪律(deflated Sharpe ratio)去衡量,它的统计显著性可能很脆弱——"提纯
过"不等于"更真实"。对任何一个残差动量构造都该问的问题是:剩下的到底是真
正的特质性信息扩散,还是同一批因子暴露换了个样子的重新包装。
