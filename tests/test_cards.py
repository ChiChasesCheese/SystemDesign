import pytest

from trellis.cards import CardError, load_cards, parse_card

QA = """---
id: my-card
node: alpha.one
type: qa
tags: [core]
---
## Q
What is X?

## A
X is **Y**.
"""

CLOZE = """---
id: my-cloze
node: alpha.one
type: cloze
---
The formula is {{c1::W + R > N}}.
"""


def write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return p


def test_parse_qa(tmp_path):
    card = parse_card(write(tmp_path, "my-card.md", QA))
    assert card.id == "my-card"
    assert card.question == "What is X?"
    assert card.answer == "X is **Y**."
    assert card.tags == ["core"]


def test_parse_cloze(tmp_path):
    card = parse_card(write(tmp_path, "my-cloze.md", CLOZE))
    assert card.type == "cloze"
    assert "{{c1::" in card.text


@pytest.mark.parametrize("mutation, fragment", [
    (QA.replace("## A\n", ""), "'## Q' section then '## A'"),
    (QA.replace("id: my-card", "id: My Card"), "invalid id"),
    (QA.replace("node: alpha.one\n", ""), "missing node"),
    (QA.replace("type: qa", "type: basic"), "type must be one of"),
    (QA.replace("tags: [core]", "extra: 1"), "unknown frontmatter"),
    (CLOZE.replace("{{c1::", "(("), "no {{c1::"),
    ("no frontmatter at all", "missing YAML frontmatter"),
])
def test_rejects_bad_cards(tmp_path, mutation, fragment):
    with pytest.raises(CardError, match=fragment):
        parse_card(write(tmp_path, "bad.md", mutation))


def test_load_cards_collects_errors_without_hiding_good_files(tmp_path):
    write(tmp_path, "my-card.md", QA)
    write(tmp_path, "bad.md", "broken")
    cards, errors = load_cards(tmp_path)
    assert [c.id for c in cards] == ["my-card"]
    assert len(errors) == 1
