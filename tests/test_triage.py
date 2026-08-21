import json

import pytest

from trellis.cases import load_cases
from trellis.codebases import CodebaseError, Harvest, artefacts, load_codebase
from trellis.skeleton import load_skeleton
from trellis.triage import accept, codebase_index, leaf_inventory, triage_prompt

SKELETON = """
domain: demo
title: Demo
nodes:
  - id: alpha
    order: 1
    title: Alpha
    children:
      - id: alpha.one
        title: One
        summary: The first thing.
"""

DECL = """
repo: owner/name
ref: main
harvest:
  - path: docs/adr/*.md
    kind: decisions
  - path: .importlinter
    kind: contracts
"""


@pytest.fixture
def project(tmp_path):
    (tmp_path / "skeleton").mkdir()
    (tmp_path / "skeleton" / "demo.yaml").write_text(SKELETON, encoding="utf-8")
    (tmp_path / "codebases").mkdir()
    (tmp_path / "codebases" / "cb.yaml").write_text(DECL, encoding="utf-8")
    cache = tmp_path / ".trellis" / "codebases" / "cb"
    (cache / "docs" / "adr").mkdir(parents=True)
    (cache / "docs" / "adr" / "0001-a-choice.md").write_text("# A choice\n", encoding="utf-8")
    (cache / ".importlinter").write_text("name = a rule\n", encoding="utf-8")
    (cache / "ignored.md").write_text("not declared\n", encoding="utf-8")
    return tmp_path


def _skeletons(project):
    return {"demo": load_skeleton(project / "skeleton" / "demo.yaml")}


def test_declaration_rejects_unknown_kind(tmp_path):
    (tmp_path / "bad.yaml").write_text(
        "repo: owner/name\nharvest:\n  - path: x\n    kind: nonsense\n", encoding="utf-8")
    with pytest.raises(CodebaseError, match="kind must be one of"):
        load_codebase(tmp_path / "bad.yaml")


def test_only_declared_paths_are_harvested(project):
    cb = load_codebase(project / "codebases" / "cb.yaml")
    found = artefacts(cb, project)
    assert [a.id for a in found] == ["decisions:0001-a-choice", "contracts:.importlinter"]
    assert not any("ignored" in a.rel for a in found)


def test_prompt_offers_every_leaf_and_names_the_commit(project):
    cb = load_codebase(project / "codebases" / "cb.yaml")
    prompt = triage_prompt(cb, "abc123def456789", artefacts(cb, project),
                           _skeletons(project), prefix="cb")
    assert "`alpha.one`" in prompt and "The first thing." in prompt
    assert "abc123def456" in prompt
    assert "decisions:0001-a-choice" in prompt


def _proposal(project, items):
    path = project / "p.json"
    path.write_text(json.dumps(
        {"codebase": "cb", "ref": "abc123", "items": items}), encoding="utf-8")
    return path


GOOD_CASE = {
    "artefact": "decisions:0001-a-choice", "verdict": "case", "lens": "demo",
    "nodes": ["alpha.one"], "slug": "cb-a-choice", "title": "A choice",
    "body": "The general mechanism, and what it costs.", "confidence": "high",
}


def test_accepted_case_is_written_with_its_provenance(project):
    written, errors, gaps = accept(
        _proposal(project, [GOOD_CASE]), project, _skeletons(project), set())
    assert errors == [] and gaps == [] and len(written) == 1
    case = load_cases(project / "vault" / "demo" / "cases")[0][0]
    assert case.nodes == ["alpha.one"]
    assert case.extra["codebase"] == "cb" and case.extra["ref"] == "abc123"
    assert case.extra["artefact"] == "decisions:0001-a-choice"


def test_a_bad_item_blocks_the_whole_proposal(project):
    bad = {**GOOD_CASE, "slug": "cb-other", "nodes": ["alpha.ghost"]}
    written, errors, _ = accept(
        _proposal(project, [GOOD_CASE, bad]), project, _skeletons(project), set())
    assert written == [] and any("no node" in e for e in errors)
    assert not (project / "vault" / "demo" / "cases").exists()


def test_slug_colliding_with_an_existing_note_is_refused(project):
    written, errors, _ = accept(
        _proposal(project, [GOOD_CASE]), project, _skeletons(project), {"cb-a-choice"})
    assert written == [] and any("already exists" in e for e in errors)


def test_gaps_are_reported_not_treated_as_errors(project):
    gap = {"artefact": "decisions:0001-a-choice", "verdict": "gap", "lens": "demo",
           "proposed_leaf": "alpha.two", "why": "nothing covers it"}
    skip = {"artefact": "contracts:.importlinter", "verdict": "skip", "why": "local"}
    written, errors, gaps = accept(
        _proposal(project, [gap, skip]), project, _skeletons(project), set())
    assert errors == [] and written == []
    assert [g["proposed_leaf"] for g in gaps] == ["alpha.two"]


def test_index_groups_a_codebases_harvest_by_lens(project):
    accept(_proposal(project, [GOOD_CASE]), project, _skeletons(project), set())
    index = codebase_index(project, "cb", ["demo"])
    assert "## demo" in index and "[[cb-a-choice|A choice]]" in index
    assert "1 case(s) accepted." in index
