# Trellis

Skeleton-constrained knowledge cards. One YAML mind map defines the topics, their
study order, and their prerequisite edges; flashcards are Obsidian-native markdown
files attached to the map's leaves; the build compiles everything into an Anki
`.apkg` you can re-import forever without duplicates.

Ships with a **System Design** domain: a 59-node map covering the classic
interview canon plus what the 2017-era resources miss — consensus, delivery
semantics, idempotency/outbox/saga/ledger patterns, SLOs, multi-region, and
AI-serving infrastructure.

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
trellis validate          # skeleton + all cards, structural checks
trellis build             # -> dist/system-design.apkg, import into Anki
trellis sync              # regenerate Obsidian map notes
trellis stats             # coverage per branch
```

- **Anki**: import `dist/system-design.apkg`. After editing or adding cards,
  rebuild and re-import — note GUIDs are stable, so edits update in place and
  your review history survives.
- **Obsidian**: open `vault/system-design/` as a vault. `map/` holds the
  generated topic notes (your own text outside the `%% trellis %%` markers is
  preserved); `cards/` holds the cards. The graph view is the mind map.

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
`{{c1::W + R > N}}`.

## Growing content with an LLM

```bash
trellis scaffold distributed.consensus -n 8   # emit a fenced, context-rich prompt
# paste into any LLM, save its JSON answer:
trellis import batch.json                     # all-or-nothing validation, then files
trellis sync && trellis build
```

## Adding a domain

Drop `skeleton/<domain>.yaml` (same shape as `system-design.yaml`), put cards
under `vault/<domain>/cards/`, and pass `--domain <domain>`. Nothing else
changes.

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
