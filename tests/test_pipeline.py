"""End-to-end tests over a tiny fixture project, plus a guard that the
real repo content always validates and builds."""

import json
import sqlite3
import zipfile
from pathlib import Path

import pytest

from trellis.build import build_package
from trellis.cards import load_cards
from trellis.scaffold import import_cards, scaffold_prompt
from trellis.skeleton import load_skeleton
from trellis.sync import BEGIN, END, sync
from trellis.validate import validate

REPO = Path(__file__).resolve().parent.parent

SKELETON = """
domain: demo
title: Demo
nodes:
  - id: alpha
    title: Alpha
    children:
      - id: alpha.one
        title: One
        summary: First topic.
      - id: alpha.two
        title: Two
        requires: [beta]
  - id: beta
    title: Beta
"""

CARD = """---
id: alpha-sample
node: alpha.one
type: qa
---
## Q
What is X?

## A
`X` is **Y**.
"""


@pytest.fixture
def project(tmp_path):
    (tmp_path / "skeleton").mkdir()
    (tmp_path / "skeleton" / "demo.yaml").write_text(SKELETON, encoding="utf-8")
    cards_dir = tmp_path / "vault" / "demo" / "cards" / "alpha"
    cards_dir.mkdir(parents=True)
    (cards_dir / "alpha-sample.md").write_text(CARD, encoding="utf-8")
    return tmp_path


def load(project):
    skeleton = load_skeleton(project / "skeleton" / "demo.yaml")
    cards, errors = load_cards(project / "vault" / "demo" / "cards")
    return skeleton, cards, errors


def test_validate_flags_unknown_node_and_filename_mismatch(project):
    skeleton, cards, errors = load(project)
    assert validate(skeleton, cards, errors).ok
    bad = project / "vault" / "demo" / "cards" / "alpha" / "wrong-name.md"
    bad.write_text(CARD.replace("alpha-sample", "other-id")
                       .replace("alpha.one", "ghost.node"), encoding="utf-8")
    report = validate(*load(project))
    assert any("not in skeleton" in e for e in report.errors)
    assert any("filename must equal card id" in e for e in report.errors)


def test_sync_is_idempotent_and_preserves_user_text(project):
    skeleton, cards, _ = load(project)
    vault = project / "vault" / "demo"
    first = sync(skeleton, cards, vault)
    assert (vault / "Demo MOC.md").exists()
    node_note = vault / "map" / "alpha.one.md"
    body = node_note.read_text(encoding="utf-8")
    assert BEGIN in body and END in body and "First topic." in body
    assert "[[alpha-sample]]" in body

    node_note.write_text(body + "\nmy own notes\n", encoding="utf-8")
    second = sync(skeleton, cards, vault)
    assert second["written"] == []  # nothing changed -> nothing rewritten
    assert "my own notes" in node_note.read_text(encoding="utf-8")


def test_build_produces_apkg_with_stable_guid(project):
    skeleton, cards, _ = load(project)
    out = project / "dist" / "demo.apkg"
    result = build_package(skeleton, cards, out)
    assert result["notes"] == 1
    with zipfile.ZipFile(out) as z, open(project / "c.db", "wb") as f:
        f.write(z.read("collection.anki2"))
    db = sqlite3.connect(project / "c.db")
    guids = [r[0] for r in db.execute("select guid from notes")]
    decks = json.loads(db.execute("select decks from col").fetchone()[0])
    names = {d["name"] for d in decks.values()}
    assert len(guids) == 1
    assert "Demo::01 Alpha::One" in names
    # rebuild -> same guid (safe re-import)
    build_package(skeleton, cards, out)
    with zipfile.ZipFile(out) as z, open(project / "c2.db", "wb") as f:
        f.write(z.read("collection.anki2"))
    guids2 = [r[0] for r in sqlite3.connect(project / "c2.db").execute("select guid from notes")]
    assert guids == guids2


def test_scaffold_prompt_carries_context(project):
    skeleton, cards, _ = load(project)
    prompt = scaffold_prompt(skeleton, "alpha.two", cards)
    assert "Beta" in prompt            # prerequisite surfaced
    assert "One" in prompt             # sibling marked out of scope
    assert '"node": "alpha.two"' in prompt


def test_import_is_all_or_nothing(project):
    skeleton, cards, _ = load(project)
    cards_dir = project / "vault" / "demo" / "cards"
    good = {"id": "alpha-new", "node": "alpha.two", "type": "qa", "q": "Q?", "a": "A."}
    bad = {"id": "alpha-sample", "node": "alpha.two", "type": "qa", "q": "Q?", "a": "A."}

    batch = project / "batch.json"
    batch.write_text(json.dumps([good, bad]), encoding="utf-8")
    written, errors = import_cards(skeleton, cards, batch, cards_dir)
    assert written == [] and any("already exists" in e for e in errors)
    assert not (cards_dir / "alpha" / "alpha-new.md").exists()

    batch.write_text("```json\n" + json.dumps([good]) + "\n```", encoding="utf-8")
    written, errors = import_cards(skeleton, cards, batch, cards_dir)
    assert errors == [] and len(written) == 1
    reloaded, parse_errors = load_cards(cards_dir)
    assert parse_errors == []
    assert {c.id for c in reloaded} == {"alpha-sample", "alpha-new"}


def test_real_repo_content_validates_and_builds(tmp_path):
    skeleton = load_skeleton(REPO / "skeleton" / "system-design.yaml")
    cards, errors = load_cards(REPO / "vault" / "system-design" / "cards")
    report = validate(skeleton, cards, errors)
    assert report.errors == []
    assert len(cards) >= 50
    result = build_package(skeleton, cards, tmp_path / "out.apkg")
    assert result["notes"] == len(cards)
