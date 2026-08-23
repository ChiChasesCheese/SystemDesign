---
id: execution-book-tif-taxonomy-cloze
node: execution.microstructure.book
type: cloze
---
An order's **time-in-force (TIF)** governs how long it stays live, independent of its price type. {{c1::Immediate-or-cancel (IOC)}} executes whatever quantity is immediately available at the limit price or better and cancels any unfilled remainder instead of resting — used to take liquidity without leaving an order exposed on the book. {{c2::Fill-or-kill (FOK)}} is stricter: it requires the *entire* quantity to execute immediately or the whole order is cancelled, with no partial fill accepted — used when a partial fill would leave an unwanted, unhedgeable residual position. {{c3::Good-till-cancelled (GTC)}} rests on the book, accumulating queue position, until explicitly cancelled or filled — the standard choice for a patient, passive order. A {{c4::peg order}}, most often pegged to the {{c5::midpoint}} of the NBBO, automatically re-quotes as the reference price moves, giving passive execution without the trader manually cancelling and replacing (and therefore without repeatedly losing queue position) every time the market ticks.

## zh
一笔委托的 **time-in-force (TIF)** 决定它存活多久，这与它的价格类型是两回事。{{c1::立即成交或取消（IOC）}}会立刻按限价或更优价格成交当下可用的数量，未成交的剩余部分直接撤销，而不是挂在盘口——用于在不暴露挂单的情况下吃掉流动性。{{c2::全部成交或取消（FOK）}}更严格：要求*全部*数量立即成交，否则整笔委托作废，不接受部分成交——用于部分成交会留下一个不想要、也无法对冲的残余仓位的场景。{{c3::撤销前有效（GTC）}}会挂在盘口上，不断积累队列位置，直到被明确撤销或成交——是耐心、被动委托的标准选择。{{c4::盯盘单（peg order）}}最常见的是挂在 NBBO 的{{c5::中点（midpoint）}}上，会随参考价的变动自动重新报价，从而实现被动成交，而无需交易者在每次行情变动时手动撤单重挂（因而也不会每次都损失队列位置）。
