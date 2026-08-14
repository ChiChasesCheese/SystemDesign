---
id: networking-dns-negative-caching
node: networking.dns
type: qa
---
## Q
You delete a DNS record by mistake and resolvers start returning NXDOMAIN. You fix the zone — but clients keep failing. Why?

## A
**Negative caching**: resolvers cache NXDOMAIN/NODATA answers too, for the negative TTL — min(SOA MINIMUM field, SOA record's own TTL). Your fix only takes effect as those cached denials expire, so a misconfiguration outage outlives its correction.

Ops takeaways: keep the negative TTL modest (minutes, not hours), and remember the mechanism exists *for* a reason — it shields authoritative servers from repeated lookups of nonexistent names (typo storms, misconfigured clients).
