---
id: networking-push-vs-pull-cdn
node: networking.cdn
type: qa
---
## Q
Push CDN vs pull CDN — how does each get content to the edge, and which fits (a) a video release dropping globally at midnight, (b) a long-tail image catalog?

## A
- **Pull** (the default): edge fetches from origin on first miss, then caches. Zero upload workflow; cost is a slow first request per edge and origin load on misses.
- **Push**: you upload content to the CDN ahead of time.

(a) **Push/pre-warm** — a synchronized global spike would stampede the origin on cold caches.
(b) **Pull** — pre-pushing millions of rarely-viewed files wastes edge storage; let demand decide what's cached.
