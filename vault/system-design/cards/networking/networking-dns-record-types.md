---
id: networking-dns-record-types
node: networking.dns
type: qa
---
## Q
A vs CNAME vs ALIAS/ANAME: which do you use at a zone apex pointing to a load balancer's changing IPs, and why?

## A
- **A/AAAA**: name → IP. Breaks when the LB's IPs change.
- **CNAME**: name → another name. Correct for `www`, but **forbidden at the apex** (`example.com`) because the apex must also hold SOA/NS records.
- **ALIAS/ANAME** (provider extension, e.g. Route 53 alias): apex-safe — the DNS provider resolves the target name and serves fresh A records itself.

Answer: ALIAS at the apex, CNAME everywhere else.
