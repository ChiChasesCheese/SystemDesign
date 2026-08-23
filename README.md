# Trellis

Skeleton-constrained knowledge base. One YAML mind map defines the topics, their
study order, and their prerequisite edges. Two kinds of content attach to its
nodes, both plain Obsidian markdown:

- **Cases** — decisions taken from a real codebase, rewritten in a lens's
  vocabulary and attached to the leaf whose principle they instantiate. Evidence
  for cards, never cards themselves. See [Studying a codebase](#studying-a-codebase).
- **Cards** — atomic Q&A / cloze fragments for spare-time review; the build
  compiles them into an Anki `.apkg` you can re-import forever without duplicates.
- **Readings** — long-form, authoritative material (papers, engineering-blog
  essays, book chapters) for systematic study; a reading can span several nodes.
- **Drills** — output practice: design questions and exercises with constraints,
  grading points, and an attempt log. Cards recall, readings feed in, drills
  train the 40-minute performance.

Cards and readings reference each other with ordinary wikilinks, and every node's
generated map note lists both — so the Obsidian graph connects topic ↔ reading ↔
card.

Ships with two domains. **System Design** — a 92-node map (391 cards, 72
readings) structured against DDIA 2nd edition and spanning the interview canon
plus what the 2017-era resources miss: consensus, CRDTs, encoding and schema
evolution, delivery semantics, idempotency/outbox/saga/ledger, OLAP and
lakehouse, SLOs, multi-region, AI serving. **Low-Level Design** — a 33-node map
(125 cards) covering the machine-coding round: object modelling, SOLID as
refactoring triggers, the GoF catalogue by intent, code smells, concurrency,
and program structure. Every leaf in both is covered.

## Why a skeleton

Every existing markdown→Anki tool treats cards as a flat bag. Trellis inverts
that: the skeleton is the source of truth, and everything is derived from it —

- **Anki deck hierarchy and ordering** (`System Design::06 Distributed Data::Consensus`)
  follow the map, so new cards always arrive in prerequisite order.
- **Obsidian graph** mirrors the map: `trellis sync` generates one linked note
  per node (breadcrumbs, prerequisites, what each topic unlocks, its cards).
- **LLM generation is fenced in**: prompts are scaffolded per-node with the
  node's scope, siblings marked out-of-scope, and existing cards to avoid
  duplicating; the LLM's JSON is validated against the skeleton before a single
  file is written.
- **Validation is structural**: a card pointing at a dead topic, a duplicate id,
  or an uncovered leaf is a build error or warning, not silent rot.

## Quickstart

```bash
pip install -e .
trellis validate          # skeleton + cards/readings/drills, structural checks
trellis build             # -> dist/system-design.apkg, import into Anki
trellis sync              # regenerate Obsidian map notes
trellis path --weeks 8    # write a week-by-week study plan into the vault
trellis stats             # coverage per branch
```

Validation also guarantees the study order is coherent: a node can never
appear before one of its `requires` prerequisites — tree order in the
skeleton is checked against the edges.

## Links are the product

The vault is meant to be the definitive index: for every topic, the one
authoritative, approachable resource — so studying never starts with a search.
Mechanically:

- Readings with a `url` become a clickable **"Go deeper"** footer on every Anki
  card under their node (ancestors included — a branch-level reading covers the
  whole branch).
- `trellis stats` reports **link coverage** (cards with a road onward) per
  branch; `trellis validate` warns when a domain drops below the 70% target.
- A source only counts as **readable** when it is archived in the vault, has
  real prose, and is not tagged `book` or `index`. Preference order, highest
  first: an engineering-blog deep dive, a company write-up, a paper, or a
  single section of a knowledge base — then anything else on the web — then
  books and indexes, which rank last however cleanly their homepage happens to
  archive. Tag a genuine full chapter `canonical`, not `book`. `validate`
  names every leaf still stuck with a pointer, so this cannot regress quietly.
- `python3 scripts/check_links.py` verifies every archived URL still resolves
  (run manually; network-bound).

### One app to read in

A reading is a pointer; a **clipping** is the page itself, saved as markdown in
the vault. Every card's footer links to its reading note with
`obsidian://open?...` — tapping it in Anki opens that note *in Obsidian*, where
`trellis sync` has embedded the clipped article, so you read with your own
typography, highlights and backlinks, online or not. The web original stays one
↗ away. See [ADR 0001](docs/adr/0001-obsidian-as-the-reader.md).

Links name the note rather than its path, so the same card works on a laptop
whose vault root is `vault/` and a phone whose git client cloned the whole
repo. That requires unique names, which is why clippings are stored as
`<reading>-clip`.

```bash
trellis --all clip          # fetch every unclipped reading into vault/<domain>/clippings/
trellis --all build         # footers now point at the local copies
```

Clippings are matched to readings by URL — the same `source:` property
[Obsidian Web Clipper](https://obsidian.md/clipper) writes — so anything you clip
by hand with the extension (point it at `<domain>/clippings/`) is picked up
identically. Pages that are the resource itself (videos) or that hide behind
JavaScript are skipped with a reason and stay web links.

Clippings **are committed**, because this repository is private and a clone is
how the archive reaches a phone. They remain other people's writing: making the
repository public again means removing them first (`git rm -r --cached
vault/*/clippings` and restoring the ignore rule that is kept, commented, in
`.gitignore`). They are reproducible either way — `trellis clip` rebuilds them
anywhere.

- **Anki**: import `dist/system-design.apkg`. After editing or adding cards,
  rebuild and re-import — note GUIDs are stable, so edits update in place and
  your review history survives.
- **After a skeleton restructure** (renamed/split/reordered nodes): Anki never
  moves existing cards between decks on import, so stale deck names linger with
  the old cards inside. Fix in one step on desktop Anki (with the
  [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on installed):
  import the new `.apkg` first, then `trellis anki-align`, then sync to
  AnkiWeb. Cards are matched by their stable node tags, moved to the decks the
  current skeleton defines, and emptied stale decks are deleted. Top-level
  branches carry an explicit `order:` in the skeleton, so their deck numbers
  never shift when new branches are inserted.

### Publishing to the phone

`build` produces a file; `anki-push` is that file reaching the phone. It runs
the four steps in the order that makes them safe, against desktop Anki with the
[AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on:

```bash
trellis --domain system-design anki-push --lang zh
#   built 391 notes in 71 decks
#   pulled from AnkiWeb        <- the phone's reviews land first
#   imported system-design.zh.apkg
#   moved 12 card(s), removed 2 stale deck(s)
#   pushed to AnkiWeb          <- the phone gets the new cards
```

It builds the package itself rather than trusting whatever sits in `dist/`,
because **Anki updates a note only when the incoming one is newer**. Re-importing
a package built before the collection last changed leaves those notes silently
stale — which is exactly what happens when you switch languages and push the old
file again. Building inside the command removes the trap.

Switching language is a push, not a migration: card ids and therefore note GUIDs
do not depend on language, so `anki-push --lang zh` rewrites the text of the
cards already in the collection and every review history survives.

Syncing **before** the import is the point: it puts the package on top of
current scheduling rather than a stale collection, so nothing reviewed on the
phone is lost. Aligning between import and the final sync means decks renamed or
split since the last push are reconciled in the same trip.

### Granularity policy

A leaf is **one interview probe** — a topic narrow enough that "I'm weak here"
points at something specific to drill or generate more cards for. Split a leaf
when it accumulates more than ~6 cards or you can't name the single skill it
trains. Splits are cheap: edit the skeleton, re-point the affected cards'
`node:` lines, `trellis sync && trellis build`, and `trellis anki-align` makes
the live collection follow.
- **Obsidian**: open `vault/` as the vault (not a single domain folder), so
  wikilinks work across domains. Each domain's `map/` holds the generated topic
  notes (your own text outside the `%% trellis %%` markers is preserved). The
  graph view is the mind map.

## Languages

A card is written in English and keeps it. A translation is **appended**, never
substituted, so nothing is lost if one is wrong or missing:

```markdown
## Q
A hot key expires and 10k requests hit the database at once…

## A
**Cache stampede.** Request coalescing, or jittered TTLs…

## Q zh
一个热点 key 过期，1 万个请求同时打到数据库……

## A zh
**缓存击穿（cache stampede）。** 请求合并，或给 TTL 加抖动……
```

A cloze card takes a single `## zh` section instead, with its `{{c1::…}}`
deletions kept byte-identical — the deletion is the answer being tested.

```bash
trellis build --lang zh     # cards render in Chinese where a translation exists
```

**Switching language is not a new deck.** Card ids — and therefore Anki note
GUIDs — do not depend on language, so re-importing a translated build swaps the
text in place and your review history survives. Technical terms stay in English
by policy; see [the translation spec](docs/translation-spec.md). `trellis stats`
reports translation coverage per language.

## Card format

One file per card under `vault/<domain>/cards/<branch>/`, filename = card id:

```markdown
---
id: caching-stampede-protection
node: caching.invalidation
type: qa            # qa | cloze
---
## Q
A hot key expires and 10k requests hit the database at once. Name the failure
and two mitigations.

## A
**Cache stampede.** Request coalescing (one recomputes, rest wait) or
jittered/early refresh so keys never expire under full load.
```

Cloze cards drop the Q/A sections and use Anki syntax in the body:
`{{c1::W + R > N}}`. Wikilinks are allowed and render as styled plain text in
Anki.

## Reading format

One file per reading under `vault/<domain>/readings/`; `nodes` may list several
topics:

```markdown
---
nodes: [async.log, async.streaming]
url: https://engineering.linkedin.com/...
---
# The Log: What every software engineer should know
Why read, what to extract, and wikilinks to related cards.
```

## Growing content with an LLM

```bash
trellis scaffold distributed.consensus -n 8   # emit a fenced, context-rich prompt
# paste into any LLM, save its JSON answer:
trellis import batch.json                     # all-or-nothing validation, then files
trellis sync && trellis build
```

## Drill format

One file per drill under `vault/<domain>/drills/`; same frontmatter as
readings (`nodes` lists every topic the exercise exercises). Body: prompt,
constraints, grading points, attempt log. Node map notes list their drills.

## Studying a codebase

A repository can be ingested as a learning target. It is *declared*, not
discovered — the sharpest decisions in a real codebase are rarely where a
heuristic would look (in the first one ingested, nine architecture rules with
their rationale live in a lint config):

```yaml
# codebases/quant-stroller.yaml
repo: ChiChasesCheese/Quant-Stroller
ref: main
harvest:
  - path: .importlinter        # architecture rules -> Case
    kind: contracts
  - path: docs/adr/*.md        # decision records  -> Case
    kind: decisions
  - path: docs/concepts/*.md   # subject matter    -> reading + clipping
    kind: subject
    lens: quant-infra
```

```bash
trellis triage quant-stroller --kinds decisions,contracts --lens system-design,low-level-design
# hand proposals/quant-stroller.prompt.md to an LLM, save its JSON answer
trellis accept proposals/quant-stroller.json
```

`triage` shallow-clones into a gitignored cache, pins the commit, and writes a
prompt listing every artefact beside every leaf it could attach to. The LLM
answers with a proposal; `accept` validates it against the skeletons and writes
files all-or-nothing — the LLM never touches the vault.

**A decision becomes a [Case](CONTEXT.md)**: rewritten in the lens's vocabulary,
attached to the leaf whose principle it instantiates, frozen at the commit it
was read from. Cases are evidence for cards, never cards themselves — a card
asking "what did we decide about X" tests recall of your own conclusion and is
worthless in an interview.

**An artefact that fits no leaf is a `gap`**, not an error: it proposes growing
the skeleton. That is why skeletons are authored from the field first and
codebases are mapped onto them afterwards — see
[ADR 0002](docs/adr/0002-skeletons-are-authored-from-the-field.md) and
[ADR 0003](docs/adr/0003-a-codebase-enters-as-cases-and-subject-material.md).

## Adding a domain

Drop `skeleton/<domain>.yaml` (same shape as `system-design.yaml`), put content
under `vault/<domain>/`, and pass `--domain <domain>` — or `--all` to run any
command across every domain (CI builds all decks). Nothing else changes.
Keep low-level design, domain knowledge, etc. as separate domains; bridge them
with cross-domain wikilinks, which work because `vault/` is one Obsidian vault.

## Development

```bash
pip install -e .[dev]
pytest -q
```

CI validates the skeleton, runs the tests, and uploads a fresh `.apkg` on every
push.

## Credits

Topic coverage informed by
[system-design-primer](https://github.com/donnemartin/system-design-primer)
(CC BY 4.0) and *Designing Data-Intensive Applications*. Card text is original.
`.apkg` packaging via [genanki](https://github.com/kerrickstaley/genanki).
