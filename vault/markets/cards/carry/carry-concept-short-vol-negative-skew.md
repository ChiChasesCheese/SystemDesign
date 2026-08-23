---
id: carry-concept-short-vol-negative-skew
node: carry.concept
type: qa
---
## Q
"Carry works until it doesn't" is the standard one-liner for carry
strategies. Describe the shape of the return distribution this refers to,
and explain precisely why it is structurally the same payoff as being short
an option.

## A
**The distribution is a long run of small, steady positive returns punctuated
by rare, large negative ones** — carry harvested month after month while the
underlying risk that's being compensated for doesn't materialize, followed
by a sudden, sharp loss when it finally does (a currency devaluation, a
curve-steepening shock, a commodity demand collapse, a default wave). This
is negative skew: the mean can look attractive and the volatility can look
low precisely because the tail event is rare, not because it's absent.

It is structurally the same as being short an option because a short option
position has exactly this shape by construction — collect a small, steady
premium regularly for selling insurance, and owe a large, lumpy payout only
on the rare occasion the option finishes in the money. Carry positions are
economically doing the same thing even without any option contract in sight:
the small periodic income is compensation collected for continuously
bearing a risk that usually doesn't show up but occasionally does in full
force, all at once. The popular image for this is "picking up pennies in
front of a steamroller" — the pennies are real and collectible for a long
time, but the steamroller is always somewhere on the road.

## Q zh
"Carry works until it doesn't"是描述 carry 策略最常见的一句话。请描述这句
话指的是什么样的收益分布形状,并精确说明为什么这在结构上和做空一份期权是
同一种payoff。

## A zh
**这个分布是长期一连串小额、稳定的正收益,被少数几次大额负收益打断**——
carry 一个月接一个月地被收获,而被补偿的那个底层风险始终没有发生,直到它
突然、剧烈地发生(一次货币贬值、一次曲线陡峭化冲击、一次商品需求崩溃、一
波违约潮)。这就是负偏(negative skew):均值看起来很吸引人、波动率看起来
很低,恰恰是因为尾部事件很罕见,而不是因为它不存在。

它在结构上和做空一份期权完全一样,是因为一个空头期权仓位按构造就是这个形
状——通过卖保险定期收取一笔小额、稳定的权利金,只有在期权极少数情况下变为
实值时才需要支付一笔庞大、笨重的赔付。即使眼前没有任何期权合约,carry 头
寸在经济实质上做的是同一件事:那笔小额的周期性收入,是为持续承担一个通常
不会出现、但偶尔会全力爆发的风险所收取的补偿。形容这个的通俗说法是"在压
路机前面捡硬币"——硬币是真实的,可以捡很长时间,但压路机始终在路上某处逼
近。
