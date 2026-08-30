# The digestion pipeline

How a body of source material — a freely published book, a company
engineering blog — becomes skeleton growth, readings, clippings, and
bilingual cards, in a way that can be stopped at any point and resumed.
This is the procedure the DDIA-deepening pass followed; reuse it verbatim
for the next corpus.

## Stages

1. **Register** the source.
   - A book gets a row in `sources/books.yaml`. Its `license` decides
     whether the text may be downloaded; a commercial book (DDIA itself)
     is registry-only — the entry documents the digestion plan and points
     at freely published companion material, and cards are written from
     understanding, never copied from the text.
   - Blog posts need no registry: they become ordinary readings, and
     `trellis clip` archives them like any other page.
2. **Ingest** what may be fetched:
   `python3 scripts/ingest_book.py <id>` downloads chapter by chapter into
   `sources/archive/<id>/`, checkpointing after each chapter. Re-running
   resumes; `--retry` re-attempts failures.
3. **Expand the skeleton first, in one place.** Decide the new leaves and
   splits *before* fanning out card writers, so every writer targets final
   node ids and only one editor ever touches `skeleton/<domain>.yaml`.
   Re-point existing cards the same commit; `trellis validate` must pass
   before stage 4 starts.
4. **Digest with at most three agents at once**, each owning disjoint
   files:
   - split by card directory (`cards/storage` vs `cards/distributed` vs
     `cards/correctness`…) so parallel writers can never collide;
   - exactly one agent owns `readings/` and `clippings/`;
   - each agent reads the existing card fronts for its leaves before
     writing, to avoid duplicates;
   - each agent maintains `pipeline/state/agent-<name>.json` — the leaves
     it owns, each marked `todo`/`done` with the card ids written —
     updating it after **every leaf**, so a run cut off by a rate limit
     resumes from the checkpoint, not from zero.
5. **Card rules** (enforced by review, then by `trellis validate`):
   - bilingual: English `## Q`/`## A` plus `## Q zh`/`## A zh` per
     `docs/translation-spec.md` (terms of art stay English, glossed once);
   - self-contained: the question carries its own context and the answer
     defines every term it uses — the card must teach without opening
     Obsidian;
   - one retrievable fact/mechanism/trade-off per card, ≤ ~6 cards per
     leaf before considering a split (`README.md` granularity policy).
6. **Merge and verify**: a dedupe pass over new card fronts, then
   `trellis --all validate && trellis --domain <d> sync && trellis --all
   build && trellis --domain <d> build --lang zh && pytest -q`.
7. **Ship**: commit (checkpoints included), push, PR, merge. Import the
   fresh `.apkg` or `trellis anki-push`; after a skeleton restructure run
   `trellis anki-align` (see README).

## Checkpoint conventions

Everything under `pipeline/state/` is committed, one JSON per unit of
resumable work:

| file | written by | resume action |
|---|---|---|
| `book-<id>.json` | `scripts/ingest_book.py` | re-run the same command |
| `agent-<name>.json` | a digest agent (stage 4) | relaunch the agent with the same brief; it skips leaves marked `done` |

A fresh session resumes the whole pipeline by reading this directory:
any `todo` leaf or `failed` chapter is the remaining work, and the git
history holds the last consistent state of everything else.
