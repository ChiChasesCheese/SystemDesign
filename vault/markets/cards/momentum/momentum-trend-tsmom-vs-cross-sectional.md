---
id: momentum-trend-tsmom-vs-cross-sectional
node: momentum.trend
type: qa
---
## Q
Cross-sectional momentum ranks a basket of assets against each other and, by
construction, ends up roughly market-neutral (equal dollars long the top
decile, short the bottom decile). Time-series momentum (TSMOM) is built
differently — each asset's sign(past 12-month return) sets its own long or
short, scaled inversely by that asset's volatility, summed across dozens of
futures markets. Why does this difference in construction mean TSMOM is not
just "momentum applied one asset at a time," and what does it give up on
being market-neutral in exchange for?

## A
**TSMOM never compares assets to each other — each asset is judged only
against its own history**, so there is no ranking step forcing longs and
shorts to offset. If every asset in the universe happens to be trending down
at once — equities, credit, commodities all falling in a global risk-off
move — TSMOM goes short essentially everything simultaneously. Cross-
sectional momentum cannot do this: it always has a long side and a short
side of roughly equal size, because "strongest relative to the others" and
"weakest relative to the others" both exist in any basket no matter what the
whole market is doing.

That means TSMOM's aggregate exposure is not pinned near zero the way
cross-sectional momentum's is — the portfolio can be net long or net short
the market as a whole, and it is precisely this **directional, potentially
concentrated exposure** across asset classes that gives TSMOM the ability to
profit from a broad, sustained market decline rather than only from relative
winners beating relative losers. The trade-off is that TSMOM carries real
directional market risk when trends align across assets (a global trend
reversal hits many positions at once), whereas cross-sectional momentum's
market-neutral construction insulates it from the market's overall level,
at the cost of never being able to make money from a broad market move in
either direction.

## Q zh
横截面动量把一篮子资产互相比较,按构造方式大致做到市场中性(等额做多最强的
一档、做空最弱的一档)。时序动量(TSMOM)的构造方式不同——每个资产按自己
过去 12 个月收益的符号来定多空,并按该资产自身波动率反向缩放仓位,再汇总到
几十个期货市场上。这种构造上的差异为什么意味着 TSMOM 不只是"把动量逐个资
产地套用一遍",它用放弃市场中性换来了什么?

## A zh
**TSMOM 从不把资产互相比较——每个资产只和自己的历史比**,所以没有一个排序
步骤强迫多空互相抵消。如果整个资产池里所有资产恰好同时在下跌——股票、信
用、商品在一次全球风险规避行情中一起跌——TSMOM 会几乎在所有市场上同时做
空。横截面动量做不到这一点:无论整个市场在干什么,篮子里总会同时存在"相
对最强"和"相对最弱"的资产,所以它总有一个规模大致相当的多头端和空头端。

这意味着 TSMOM 的整体敞口不会像横截面动量那样被钉在接近零的位置——组合可
以整体净多头或净空头整个市场,正是这种**跨资产类别的方向性、有可能高度集
中的敞口**,让 TSMOM 有能力从一次广泛、持续的市场下跌中获利,而不只是从"相
对赢家跑赢相对输家"中获利。代价是当趋势在各资产间同向排列时,TSMOM 承担
真实的方向性市场风险(一次全球性趋势反转会同时打击多个仓位);而横截面动
量的市场中性构造让它不受市场整体水平的影响,代价是它永远无法从市场朝任一
方向的整体移动中赚钱。
