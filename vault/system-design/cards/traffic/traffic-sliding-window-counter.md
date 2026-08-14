---
id: traffic-sliding-window-counter
node: traffic.rate-limiting
type: cloze
---
The sliding-window **counter** (the production approximation, e.g. Cloudflare): keep one counter for the current fixed window and one for the previous; estimated rate = {{c1::current count + previous count × the fraction of the sliding window overlapping the previous window}}. Memory is {{c2::O(1) per key — two counters}}, versus a sliding **log** storing every request timestamp; the price is assuming requests were {{c3::evenly distributed across the previous window}}, so the boundary-burst error is small and bounded.
