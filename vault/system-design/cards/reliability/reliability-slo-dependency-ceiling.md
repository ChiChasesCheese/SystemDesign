---
id: reliability-slo-dependency-ceiling
node: reliability.slo
type: cloze
---
A service's achievable SLO is capped by its **hard dependencies**: if you call a 99.9% service synchronously on every request, you cannot credibly promise more than {{c1::~99.9% (minus your own failures — hard dependencies multiply in)}}. To offer a *higher* SLO than a dependency you must {{c2::take it off the critical path — cache its data, degrade gracefully without it, or make the call async}}. Rule of thumb: your critical dependencies should each be about one nine *more* reliable than the SLO you sell.
