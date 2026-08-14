import pytest

from trellis.readings import ReadingError, parse_reading
from trellis.skeleton import load_skeleton
from trellis.validate import validate

READING = """---
nodes: [alpha.one, beta]
url: https://example.com/essay
---
# A Canonical Essay
Why read: it defines the vocabulary.
"""

SKELETON = """
domain: demo
title: Demo
nodes:
  - id: alpha
    title: Alpha
    children:
      - id: alpha.one
        title: One
  - id: beta
    title: Beta
"""


def write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return p


def test_parse_reading(tmp_path):
    r = parse_reading(write(tmp_path, "essay.md", READING))
    assert r.title == "A Canonical Essay"
    assert r.nodes == ["alpha.one", "beta"]
    assert r.url == "https://example.com/essay"
    assert r.link_target == "essay"


def test_single_node_string_allowed(tmp_path):
    r = parse_reading(write(tmp_path, "e.md", READING.replace("[alpha.one, beta]", "beta")))
    assert r.nodes == ["beta"]


@pytest.mark.parametrize("mutation, fragment", [
    (READING.replace("nodes: [alpha.one, beta]\n", ""), "'nodes' must be"),
    (READING.replace("url:", "link:"), "unknown frontmatter"),
    ("no frontmatter", "missing YAML frontmatter"),
])
def test_rejects_bad_readings(tmp_path, mutation, fragment):
    with pytest.raises(ReadingError, match=fragment):
        parse_reading(write(tmp_path, "bad.md", mutation))


def test_validate_rejects_unknown_reading_node(tmp_path):
    skeleton = load_skeleton(write(tmp_path, "s.yaml", SKELETON))
    reading = parse_reading(
        write(tmp_path, "e.md", READING.replace("beta]", "ghost]"))
    )
    report = validate(skeleton, [], [], [reading], [])
    assert any("ghost" in e for e in report.errors)
