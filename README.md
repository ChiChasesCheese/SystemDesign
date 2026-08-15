# Trellis

Skeleton-constrained knowledge base. One YAML mind map defines the topics, their
study order, and their prerequisite edges. Two kinds of content attach to its
nodes, both plain Obsidian markdown:

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

Ships with a **System Design** domain: a 66-node map (318 cards, 13 readings,
every leaf covered), structured against DDIA 2nd edition's chapter framework
and spanning the classic interview canon plus what the 2017-era resources
miss — consensus, CRDTs, encoding & schema evolution, delivery semantics,
idempotency/outbox/saga/ledger patterns, OLAP/lakehouse/batch/derived data,
SLOs, multi-region, and AI-serving infrastructure. The `ddia-2e` reading note
maps every DDIA chapter to its skeleton nodes.

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

Clippings are **gitignored on purpose**: they are verbatim copies of other
people's writing and this repo is public. They are personal and reproducible —
`trellis clip` rebuilds them anywhere. To read them on a phone, sync the vault
with Obsidian Sync or iCloud (a git clone won't carry ignored files); to commit
them instead, make the repo private first and drop the ignore rule.

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
