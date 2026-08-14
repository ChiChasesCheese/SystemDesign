---
id: caching-hit-rate-outage-math
node: caching.placement
type: cloze
---
Second-order dependency math: at a 99% hit rate, losing the cache multiplies database read load by {{c1::100× (1 ÷ miss rate)}} — so either the DB is provisioned for full miss-storm traffic (almost never) or the cache is a **hard dependency** that needs {{c2::HA (replication/failover) plus warmed, gradual recovery — never a cold restart into live traffic}}. The trap: every hit-rate improvement quietly shrinks DB headroom, until a "cache" the database cannot survive without is really {{c3::a serving tier, not an optimization}}.
