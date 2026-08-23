---
id: data-bars-vwap-eligible-trades
node: data.market-data.bars
type: qa
---
## Q
You compute an intraday VWAP (volume-weighted average price) benchmark by summing `price * size` over every trade message in the raw tape for the day and dividing by total size — no filtering. Why does this produce a benchmark that doesn't match what a broker's VWAP algo actually reports for the same stock and day?

## A
**Not every trade message on the tape is "real" volume in the sense a VWAP benchmark should count, and unfiltered inclusion double-counts or misweights several categories.** Standard VWAP calculation conventions exclude, via trade condition codes, at least: **odd-lot trades** (fewer than a round lot, historically excluded or handled separately from consolidated volume in the US until relatively recent SIP changes broadened odd-lot reporting), **derivatively-priced trades** (executions priced off a reference like the NBBO midpoint rather than through genuine price discovery, e.g. some retail wholesaler internalization), trades explicitly marked as **not eligible for last-sale or volume-weighted calculations**, and any trade later **cancelled or corrected**. Each of these either represents volume that traded away from the price-discovery process VWAP is meant to summarize, or is a print that no longer exists once corrected — including it either dilutes the average toward an off-market reference price or bakes in a since-retracted number.

The consequence is concrete: a naive VWAP computed from raw, unfiltered ticks will disagree with a broker's or exchange's official VWAP by an amount that scales with how much odd-lot and off-exchange-reference volume traded that day — often small for a liquid large-cap on a quiet day, but large enough on names with heavy retail/wholesaler internalization to make the benchmark unusable for execution-quality comparison. The fix mirrors the busted-print case: filter trades by their condition codes to the vendor- or venue-defined "eligible" set before computing any volume-weighted statistic, and never assume "every row in the tape counts."

## Q zh
你通过对当天原始行情里的每一笔成交报文求和 `price * size`（不做任何过滤）、再除以总成交量，来计算日内 VWAP（成交量加权平均价）基准。为什么这样算出来的基准和券商 VWAP 算法对同一只股票同一天实际报告的结果对不上？

## A zh
**并不是行情带上的每一笔成交报文都算作 VWAP 基准应当计入的"真实"成交量，不加过滤地全部纳入会导致重复计算或权重错配。** 标准 VWAP 计算惯例会通过成交状态码至少排除以下几类：**零股成交（odd-lot trades）**（少于一个整手，在美国历史上曾被从合并成交量中排除或单独处理，直到相对较近的 SIP 改革才扩大了零股上报范围）、**衍生定价成交**（按照某个参考价，例如 NBBO 中点价定价，而非真实价格发现产生的成交，例如某些零售批发商的内部化撮合）、明确标记为**不计入最新成交价或成交量加权计算**的成交，以及任何后续被**取消或更正**的成交。这些成交要么代表着偏离 VWAP 本应概括的价格发现过程的成交量，要么是一笔一旦被更正就不复存在的报价——纳入它们要么把均值稀释向一个偏离市场的参考价，要么把一个已经被撤回的数字烘焙进结果里。

后果是具体的：一个从原始、未过滤的逐笔数据朴素算出的 VWAP，与券商或交易所的官方 VWAP 之间的差异，会随着当天零股成交和场外参考定价成交的占比而变化——对一只流动性好的大盘股在平静的一天里，差异往往很小，但对零售/批发商内部化撮合较重的标的，差异会大到让这个基准无法用于执行质量对比。修正方法和作废成交那道题的思路一致：在计算任何成交量加权统计量之前，先按供应商或场所定义的"合格"集合对成交进行状态码过滤，永远不要假设"行情带上的每一行都算数"。
