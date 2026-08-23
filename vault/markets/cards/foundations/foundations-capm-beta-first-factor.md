---
id: foundations-capm-beta-first-factor
node: foundations.capm
type: qa
---
## Q
In what specific sense is CAPM described as a "one-factor model," and why is market beta called "the first factor" — what did every subsequent multi-factor model do with it rather than replace it?

## A
**CAPM is one-factor because it claims there is exactly one source of systematic (undiversifiable) risk that markets price — sensitivity to the return of the market portfolio itself — and every asset's expected excess return is fully explained by its beta (sensitivity) to that single factor.** Idiosyncratic, firm-specific risk earns no premium under CAPM because a diversified investor can eliminate it for free by holding many assets, so only the risk that can't be diversified away (market-wide risk) deserves compensation.

Market beta is called "the first factor" because it was the original systematic risk exposure, both historically (CAPM predates the factor models that followed by roughly two decades) and structurally: Fama-French's three-factor model (1993) added size (SMB) and value (HML) *alongside* market beta rather than discarding it; their five-factor extension (2015) added profitability and investment the same way; arbitrage pricing theory (APT) generalizes to an arbitrary number of factors but still typically includes a market-like factor. Every later model treats market beta as the baseline systematic exposure every asset carries and asks what *additional* factors explain the returns beta leaves unexplained — none of them zero out beta's role, they layer on top of it.

## Q zh
CAPM 为什么被称为"单因子模型"？具体在什么意义上？市场 beta 为什么被称为"第一个因子"？后来出现的每一个多因子模型，对它做了什么，而不是把它扔掉？

## A zh
**CAPM 是单因子的，因为它主张市场只会给恰好一种系统性（无法分散掉的）风险定价——即对市场组合本身收益的敏感度——而每项资产的预期超额收益，完全由它相对这唯一一个因子的 beta（敏感度）来解释。** 在 CAPM 下，特异的、公司层面的风险不会带来任何溢价，因为一个分散化的投资者可以通过持有大量资产免费消除这种风险，所以只有无法被分散掉的风险（全市场层面的风险）才值得被补偿。

市场 beta 被称为"第一个因子"，是因为它无论在历史上（CAPM 比后来的因子模型早了大约二十年）还是在结构上，都是最原始的系统性风险敞口：Fama-French 三因子模型（1993）是在市场 beta**之外**加上了规模因子（SMB）和价值因子（HML），而不是把 beta 丢弃；他们的五因子扩展（2015）同样是在此基础上加上了盈利能力和投资因子；套利定价理论（APT）虽然可以推广到任意多个因子，但通常仍然包含一个类似市场因子的东西。后来的每一个模型，都把市场 beta 当作每项资产都携带的基准系统性敞口，然后去问：还有哪些**额外**的因子能解释 beta 解释不了的那部分收益——没有一个模型把 beta 的作用清零，它们都是在 beta 之上叠加，而不是取代它。
