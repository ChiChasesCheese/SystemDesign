import pytest

from trellis.skeleton import SkeletonError, load_skeleton

GOOD = """
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
        requires: [beta]
  - id: beta
    title: Beta
"""


def write(tmp_path, text):
    p = tmp_path / "s.yaml"
    p.write_text(text, encoding="utf-8")
    return p


def test_load_good(tmp_path):
    s = load_skeleton(write(tmp_path, GOOD))
    assert [n.id for n in s.walk()] == ["alpha", "alpha.one", "alpha.two", "beta"]
    assert [n.id for n in s.leaves()] == ["alpha.one", "alpha.two", "beta"]
    assert s.by_id["alpha.two"].requires == ["beta"]
    assert s.by_id["alpha.one"].parent is s.by_id["alpha"]


def test_deck_name_carries_study_order(tmp_path):
    s = load_skeleton(write(tmp_path, GOOD))
    assert s.deck_name(s.by_id["alpha.one"]) == "Demo::01 Alpha::One"
    assert s.deck_name(s.by_id["beta"]) == "Demo::02 Beta"


@pytest.mark.parametrize("mutation, fragment", [
    (GOOD.replace("id: beta", "id: alpha"), "duplicate node id"),
    (GOOD.replace("requires: [beta]", "requires: [ghost]"), "unknown node"),
    (GOOD.replace("id: alpha.one", "id: one"), "prefixed by its parent"),
    (GOOD.replace("title: One\n", "title: One\n        bogus: 1\n"), "unknown keys"),
    (GOOD + "  - id: gamma\n    title: G\n    requires: [gamma]\n", "requires itself"),
])
def test_rejects_bad_skeletons(tmp_path, mutation, fragment):
    with pytest.raises(SkeletonError, match=fragment):
        load_skeleton(write(tmp_path, mutation))


def test_rejects_requires_cycle(tmp_path):
    text = GOOD.replace("  - id: beta\n    title: Beta\n",
                        "  - id: beta\n    title: Beta\n    requires: [alpha.two]\n")
    with pytest.raises(SkeletonError, match="cycle"):
        load_skeleton(write(tmp_path, text))
