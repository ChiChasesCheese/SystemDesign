#!/usr/bin/env python3
"""Ingest a freely published book into sources/archive/, chapter by chapter.

The registry is sources/books.yaml. Only books whose author or publisher
gives the text away are downloaded — a commercial license stops the run
before any network I/O, because archiving someone's paid book is not
"studying" it. Commercial entries still earn their row in the registry:
they carry the digestion plan the card-writing stage follows without a
local copy of the text.

The run is checkpointed per chapter in pipeline/state/book-<id>.json and
written after every chapter, so a run killed mid-book (network, rate
limit, container reclaim) resumes exactly where it stopped:

    python3 scripts/ingest_book.py mixu-distsys           # start or resume
    python3 scripts/ingest_book.py mixu-distsys --retry   # also retry failures

Fetching and HTML→markdown extraction reuse trellis.clippings (trafilatura
underneath), so an archived chapter looks like any clipping and can later
be promoted to a reading + clipping with a file move.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from trellis.clippings import ClipError, fetch_page  # noqa: E402

REGISTRY = ROOT / "sources" / "books.yaml"
ARCHIVE = ROOT / "sources" / "archive"
STATE = ROOT / "pipeline" / "state"

# Licenses the pipeline may download. Anything else is registry-only.
FREE_LICENSES = {"free-online", "cc-by", "cc-by-nc", "cc-by-sa", "public-domain"}


def _slug(url: str) -> str:
    tail = url.rstrip("/").rsplit("/", 1)[-1]
    tail = re.sub(r"\.[a-z]+$", "", tail)
    return re.sub(r"[^a-z0-9-]+", "-", tail.lower()).strip("-") or "chapter"


def _load_book(book_id: str) -> dict:
    registry = yaml.safe_load(REGISTRY.read_text())
    for book in registry.get("books", []):
        if book["id"] == book_id:
            return book
    known = ", ".join(b["id"] for b in registry.get("books", []))
    sys.exit(f"error: unknown book {book_id!r} (registry has: {known})")


def _checkpoint_path(book_id: str) -> Path:
    return STATE / f"book-{book_id}.json"


def _load_checkpoint(book_id: str) -> dict:
    path = _checkpoint_path(book_id)
    if path.exists():
        return json.loads(path.read_text())
    return {"book": book_id, "chapters": {}}


def _save_checkpoint(book_id: str, cp: dict) -> None:
    cp["updated"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    path = _checkpoint_path(book_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cp, indent=2, sort_keys=True) + "\n")


def ingest(book_id: str, retry_failed: bool = False) -> int:
    book = _load_book(book_id)

    if book.get("license") not in FREE_LICENSES:
        print(
            f"{book['title']} is licensed {book.get('license')!r} — not freely "
            "published, so it is never downloaded. Its registry entry documents "
            "the digestion plan; write cards from understanding and archive only "
            "the freely published companion material (see the entry's notes)."
        )
        return 1

    chapters = book.get("chapters", [])
    if not chapters:
        sys.exit(f"error: {book_id} has no chapters listed in the registry")

    cp = _load_checkpoint(book_id)
    out_dir = ARCHIVE / book_id
    out_dir.mkdir(parents=True, exist_ok=True)

    done = skipped = failed = 0
    for i, url in enumerate(chapters, start=1):
        entry = cp["chapters"].get(url, {})
        dest = out_dir / f"{i:02d}-{_slug(url)}.md"
        if entry.get("status") == "done" and dest.exists() and not (
            retry_failed and entry.get("status") == "failed"
        ):
            skipped += 1
            continue
        if entry.get("status") == "failed" and not retry_failed:
            skipped += 1
            continue

        try:
            page = fetch_page(url)
        except ClipError as exc:
            cp["chapters"][url] = {"status": "failed", "error": str(exc)}
            _save_checkpoint(book_id, cp)
            print(f"  FAIL {url}: {exc}")
            failed += 1
            continue

        if page.is_pdf:
            dest = dest.with_suffix(".pdf")
            dest.write_bytes(page.pdf)
        else:
            front = {
                "title": page.title,
                "source": url,
                "book": book["title"],
                "license": book["license"],
                "fetched": dt.date.today().isoformat(),
            }
            body = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
            dest.write_text(f"---\n{body}---\n\n{page.markdown.strip()}\n")

        cp["chapters"][url] = {"status": "done", "file": str(dest.relative_to(ROOT))}
        _save_checkpoint(book_id, cp)
        print(f"  ok   {dest.name}")
        done += 1

    print(f"{book_id}: {done} fetched, {skipped} already done, {failed} failed")
    return 0 if failed == 0 else 2


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("book_id", help="id from sources/books.yaml")
    ap.add_argument("--retry", action="store_true", help="retry chapters marked failed")
    args = ap.parse_args()
    sys.exit(ingest(args.book_id, retry_failed=args.retry))


if __name__ == "__main__":
    main()
