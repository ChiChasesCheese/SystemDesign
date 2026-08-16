"""Drill coverage and the wikilink resolution that keeps drills honest."""

from pathlib import Path

import pytest

from trellis.drills import (
    branches_without_drill, drill_coverage, drill_title, drilled_leaves,
    load_drills,
)
from trellis.obsidian import note_names, wikilink_targets
from trellis.skeleton import load_skeleton
from trellis.validate import validate

SKELETON = """
domain: demo
title: Demo
nodes:
  - id: alpha
    title: Alpha
    children:
      - id: alpha.one
        title: One
      - id: alpha.two
        title: Two
  - id: beta
    title: Beta
    children:
      - id: beta.one
        title: One B
"""

DRILL = """---
nodes: [{nodes}]
---
# Drill: {title}
Body {links}
"""


@pytest.fixture
def skeleton(tmp_path):
    path = tmp_path / "demo.yaml"
    path.write_text(SKELETON, encoding="utf-8")
    return load_skeleton(path)


def _drills(tmp_path, **specs):
    directory = tmp_path / "drills"
    directory.mkdir(exist_ok=True)
    for name, (nodes, links) in specs.items():
        (directory / f"{name}.md").write_text(
            DRILL.format(nodes=", ".join(nodes), title=name, links=links),
            encoding="utf-8",
        )
    drills, errors = load_drills(directory)
    assert errors == []
    return drills


def test_naming_an_inner_node_claims_its_subtree(tmp_path, skeleton):
    """A question about "alpha" is a question about each probe under it."""
    drills = _drills(tmp_path, whole=(["alpha"], ""))
    assert drilled_leaves(skeleton, drills) == {"alpha.one", "alpha.two"}
    assert drill_coverage(skeleton, drills) == (2, 3)
    assert branches_without_drill(skeleton, drills) == ["beta"]


def test_leaf_level_drill_covers_only_that_leaf(tmp_path, skeleton):
    drills = _drills(tmp_path, one=(["alpha.one", "beta.one"], ""))
    assert drilled_leaves(skeleton, drills) == {"alpha.one", "beta.one"}
    assert branches_without_drill(skeleton, drills) == []


def test_unknown_node_never_counts_as_coverage(tmp_path, skeleton):
    drills = _drills(tmp_path, ghost=(["nope"], ""))
    assert drill_coverage(skeleton, drills) == (0, 3)


def test_drill_title_drops_the_prefix_the_h1_carries(tmp_path):
    drill, = _drills(tmp_path, thing=(["alpha"], ""))
    assert drill.title == "Drill: thing"
    assert drill_title(drill) == "thing"


def test_wikilink_targets_ignores_alias_heading_and_block():
    text = "[[a|Alias]] ![[b.pdf]] [[c#Section]] [[d^block]] [[ e ]]"
    assert wikilink_targets(text) == ["a", "b.pdf", "c", "d", "e"]


def test_note_names_shadows_an_attachment_with_its_wrapper_note(tmp_path):
    """A clipped PDF is a .pdf plus the .md that embeds it. Obsidian
    resolves the bare name to the note, so that pair is not ambiguous —
    but two markdown notes of one name are."""
    vault = tmp_path / "vault"
    (vault / "clippings").mkdir(parents=True)
    (vault / "clippings" / "paper-clip.pdf").write_bytes(b"%PDF-")
    (vault / "clippings" / "paper-clip.md").write_text("![[paper-clip.pdf]]")
    (vault / "twin.md").write_text("x")
    (vault / "clippings" / "twin.md").write_text("x")

    names = note_names(vault)
    assert names["paper-clip"] == 1
    assert names["paper-clip.pdf"] == 1
    assert names["twin"] == 2


def test_dead_and_ambiguous_wikilinks_are_errors(tmp_path, skeleton):
    drills = _drills(tmp_path, good=(["alpha"], "[[real-note]] [[twin]] [[ghost]]"))
    notes = {"real-note": 1, "twin": 2}
    report = validate(skeleton, [], [], [], [], drills, [], notes=notes)
    assert any("[[ghost]] resolves to no note" in e for e in report.errors)
    assert any("[[twin]] is ambiguous" in e for e in report.errors)
    assert not any("real-note" in e for e in report.errors)


def test_undrilled_branch_is_a_warning_not_an_error(tmp_path, skeleton):
    drills = _drills(tmp_path, partial=(["alpha.one"], ""))
    report = validate(skeleton, [], [], [], [], drills, [])
    assert report.ok
    assert any("no drill" in w and "beta" in w for w in report.warnings)
    assert any("drill coverage 1/3" in w for w in report.warnings)


def test_a_domain_with_no_drills_is_all_warning(skeleton):
    """Not being nagged would be the bug: cards alone are recall, and the
    warning is how a domain's missing half stays visible."""
    report = validate(skeleton, [], [], [], [], [], [])
    assert report.ok
    assert any("alpha, beta" in w for w in report.warnings)
    assert any("drill coverage 0/3" in w for w in report.warnings)
