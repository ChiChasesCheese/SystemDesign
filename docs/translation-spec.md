# Translating cards

A card is written in English and keeps that English forever. A translation is
**added beside it**, never in place of it, so a bad translation is always one
deletion away from being undone and the deck still builds if a card was missed.

## Where the translation goes

**qa card** — append two sections after `## A`:

```markdown
## Q
A hot key expires and 10k requests hit the database at once. Name the failure
and two mitigations.

## A
**Cache stampede.** Request coalescing (one recomputes, rest wait) or
jittered/early refresh so keys never expire under full load.

## Q zh
一个热点 key 过期，1 万个请求同时打到数据库。这个故障叫什么，两种缓解手段是什么？

## A zh
**缓存击穿（cache stampede）。** 请求合并（只让一个请求回源重算，其余等待或读旧值），
或者给 TTL 加抖动、提前刷新，让 key 不会在满负载下同时过期。
```

**cloze card** — append one section at the end:

```markdown
Leaderless replication needs {{c1::W + R > N}} to guarantee read-your-writes.

## zh
无主复制要保证 read-your-writes，需要 {{c1::W + R > N}}。
```

## Rules

1. **Never touch the frontmatter or the English sections.** Append only.
2. **Keep the cloze deletions byte-identical** — `{{c1::...}}` including what is
   inside it. Translate the prose around them. The deletion is the answer being
   tested; changing it changes the card.
3. **Technical terms stay in English.** Write natural Chinese around them:
   quorum、write skew、idempotency key、LSM-tree、outbox、backpressure、
   implementation shortfall. On a term's first appearance in a card you may
   gloss it once — 缓存击穿（cache stampede）— but do not invent Chinese
   equivalents for terms the field uses in English.
4. **Code, identifiers, formulas, numbers, and product names are untouched**:
   `SELECT ... FOR UPDATE SKIP LOCKED`, `W + R > N`, `p99`, Kafka, Postgres,
   DynamoDB, `principles.coupling`.
5. **Keep the markdown structure** — the same bullets, the same bold, the same
   code fences, in the same order. If the English answer is three bullets, the
   Chinese answer is the same three bullets.
6. **Translate the meaning, not the words.** These are interview flashcards read
   under time pressure: write the Chinese a senior engineer would actually say.
   Awkward literal translation is worse than English.
7. **Skip nothing.** Every card in your batch gets its translation.

## Verify

```bash
cd /Users/chizhang/Code/SystemDesign && trellis --all validate
```

Zero errors. The parser rejects a translation that is missing half a qa pair or
that dropped a cloze deletion, so a clean validate means the structure survived.
