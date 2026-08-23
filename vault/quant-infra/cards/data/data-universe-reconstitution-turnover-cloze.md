---
id: data-universe-reconstitution-turnover-cloze
node: data.point-in-time.universe
type: cloze
---
A point-in-time universe table must be keyed on {{c1::(date, instrument)}} rather than just instrument, because membership is a function of time: the S&P 500 alone sees on the order of {{c2::20-30}} constituent changes a year from quarterly rebalances plus ad hoc removals (M&A, bankruptcy, index-eligibility loss), so over a {{c3::15-year}} backtest window roughly {{c4::300-450}} membership events have occurred — meaning a universe query for any single historical date must reproduce that date's exact roster, not derive it by filtering today's roster backward.

## zh
一张点时（point-in-time）股票池表必须以 {{c1::(日期, 标的)}} 为键，而不能只以标的为键，因为成分资格是时间的函数：仅标普 500 一个指数，每年就会因季度调仓加上临时调出（并购、破产、丧失指数资格）产生大约 {{c2::20-30}} 次成分股变动，因此在一个 {{c3::15 年}}的回测窗口里，累计大约发生了 {{c4::300-450}} 次成分变动事件——这意味着对任意一个历史日期的股票池查询，必须还原出该日期确切的成分股名单，而不能靠把今天的名单往回过滤得到。
