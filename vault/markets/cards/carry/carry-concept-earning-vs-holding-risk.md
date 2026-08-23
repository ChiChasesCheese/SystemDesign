---
id: carry-concept-earning-vs-holding-risk
node: carry.concept
type: qa
---
## Q
A strategy shows a Sharpe ratio of 2.5, near-zero drawdowns, and positive
returns in nearly every month for three straight years. Why should this
track record make you suspicious rather than impressed, and what question
should you ask before trusting it?

## A
**Because that exact shape — smooth, high Sharpe, almost no drawdown — is
the signature of a position that is quietly short volatility or short tail
risk the whole time, not evidence that the risk isn't there.** A carry-like
strategy's "safety" over any given three-year window reflects only that the
specific tail event it's exposed to hasn't happened yet in that window, not
that the position has been engineered to avoid it. The steadiness is a
by-product of collecting a risk premium continuously; it says nothing about
the size of the payout the strategy owes if the risk does materialize.

The distinction that matters is between **earning carry** — collecting a
persistent risk premium as fair compensation for a risk you are prepared to
absorb — and **being paid for a risk you have not actually priced or sized**
for the day it shows up. The honest diagnostic question for any track record
like this is: "what insurance is this position implicitly selling, and what
does the payout day look like?" If you can't answer that — what the tail
event is, roughly how large the loss would be, and whether the strategy's
current leverage could survive it — a suspiciously smooth curve is not
confidence-inspiring, it is simply a tail that hasn't been paid yet.

## Q zh
一个策略连续三年展示出 2.5 的夏普比率、接近零的回撤,几乎每个月都是正收
益。为什么这份业绩记录应该让你起疑,而不是让你印象深刻?在信任它之前应该
问什么问题?

## A zh
**因为这种"平滑、高夏普、几乎没有回撤"的形状,恰恰是一个头寸一直在悄悄做
空波动率或做空尾部风险的标志,而不是这个风险不存在的证据。** 一个类 carry
策略在任何一个给定的三年窗口里表现出的"安全",反映的只是它所暴露的那个特
定尾部事件在这个窗口里恰好没有发生,而不是这个头寸被设计成能够避开它。这
份平稳只是持续收取一份风险溢价的副产品;它完全没有告诉你,如果这个风险真
的发生了,这个策略要偿还多大的赔付。

这里真正重要的区别在于**赚取 carry**——作为对一个你已经准备好去承担的风险
的合理补偿,持续收取一份风险溢价——和**为一个你其实并没有真正定价或量化风
险规模的东西被支付报酬**,直到它真的出现的那一天。对任何这样的业绩记录,
诚实的诊断问题是:"这个头寸隐含地在卖什么保险?赔付发生的那天会是什么样
子?"如果你答不上来——尾部事件是什么、亏损大致有多大、以及策略当前的杠杆
能不能扛过去——一条可疑地平滑的收益曲线并不能让人放心,它只是一个还没有兑
付的尾部而已。
