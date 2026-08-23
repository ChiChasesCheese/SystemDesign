# Writing cards

A card is one file under `vault/<domain>/cards/<branch>/<card-id>.md`, and the
filename equals the id.

```markdown
---
id: data-pit-restatement-leak
node: data.point-in-time.as-of
type: qa
---
## Q
Your loader filters `WHERE report_date <= t` against a fundamentals table that
the vendor restates. A backtest on it beats live trading by a wide margin.
What leaked, and what does the table need instead?

## A
**Restatements leak the future even though every row's `report_date` is in the
past.** A company files Q1 in April and revises it in July; the vendor
overwrites the April row. Filtering on `report_date` at a June simulation date
returns the *July* numbers — figures nobody could have had — so the strategy
trades on corrections it could not have seen, and the edge evaporates in
production where only the April figures exist.

The table needs a second time axis: **effective date** (the period the fact
describes) and **knowledge date** (when it became known). A point-in-time query
filters `knowledge_date <= t`, returning the April view in June and the July
view in August. A table with one date cannot express this, no matter how the
query is written.

## Q zh
（同一问题的中文翻译）

## A zh
（同一答案的中文翻译，术语保持英文）
```

Cloze cards drop the Q/A headings; the body carries `{{c1::…}}` deletions and a
`## zh` section holds the translation. See
[the translation spec](translation-spec.md) for the rules that apply there.

## What earns a card

**The vital few, not the complete list.** A leaf holds four to six cards, so
each one has to be a fact that pays rent: the mechanism that explains several
others, the number an interviewer actually probes, the failure that bites in
production. Exhaustive coverage of a topic is not the goal and actively hurts —
every marginal card is daily review time taken from a better one.

Ask of each candidate: *if I could only keep five facts from this leaf, is this
one of them?* If not, it does not get written.

## Every card stands alone

A card is met months later, in isolation, on a phone, out of order. It cannot
lean on the card next to it.

- **The question carries its own setup.** Name the scenario, the numbers, the
  code — enough that the question is answerable cold. Never "in the case above"
  or a bare "why?".
- **The answer explains the mechanism, not the label.** Say what happens, in
  what order, and what it causes. A reader who has never met the term should
  finish the card understanding *why* the answer is the answer.
- **Consequences belong on the card.** What breaks, what it costs, what you give
  up by choosing it. A trade-off without its price is trivia.
- **Terms of art get a clause.** The first time a card uses `write skew` or
  `hinted handoff`, one clause says what it is. Do not send the reader to
  another card.

Length follows from this rather than from a limit: as long as it needs to teach
the mechanism and its consequence, and not one sentence longer. Two short
paragraphs, or a lead sentence plus four or five bullets, is the usual shape.
Padding is as bad as omission — every sentence carries a fact, a cause, or a
cost.

## Rules

- `id`: lowercase-hyphenated, unique across the domain, prefixed with the
  top-level branch id. Filename = id + `.md`.
- `node`: exactly one leaf id from the skeleton.
- qa body: `## Q` then `## A`, both non-empty. Cloze body: no headings, at least
  one `{{c1::…}}`.
- Frontmatter keys: `id`, `node`, `type`, optional `tags`.
- Markdown is welcome — bold, small tables, fenced code. No images, no
  wikilinks.
- Every card ships with its `zh` translation, written at the same time by the
  same author. Technical terms stay in English; see the translation spec.

## Verify

```bash
trellis --domain <domain> validate    # 0 errors
```
