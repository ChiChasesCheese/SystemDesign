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


TRANSLATED = """---
id: my-card
node: alpha.one
type: qa
---
## Q
What is X?

## A
X is **Y**.

## Q zh
X 是什么？

## A zh
X 是 **Y**。
"""

CLOZE_TRANSLATED = """---
id: my-cloze
node: alpha.one
type: cloze
---
The formula is {{c1::W + R > N}}.

## zh
公式是 {{c1::W + R > N}}。
"""


def test_translation_sits_beside_the_english_never_replacing_it(tmp_path):
    card = parse_card(write(tmp_path, "my-card.md", TRANSLATED))
    assert card.question == "What is X?"          # English is untouched
    assert card.render() == ("What is X?", "X is **Y**.")
    assert card.render("zh") == ("X 是什么？", "X 是 **Y**。")


def test_a_card_without_the_language_falls_back_to_english(tmp_path):
    card = parse_card(write(tmp_path, "my-card.md", QA))
    assert card.render("zh") == ("What is X?", "X is **Y**.")


def test_cloze_translation_keeps_its_deletion(tmp_path):
    card = parse_card(write(tmp_path, "my-cloze.md", CLOZE_TRANSLATED))
    assert card.render("zh")[0] == "公式是 {{c1::W + R > N}}。"


@pytest.mark.parametrize("mutation, fragment", [
    (TRANSLATED.replace("## A zh\nX 是 **Y**。\n", ""), "missing \\['answer'\\]"),
    (CLOZE_TRANSLATED.replace("{{c1::W + R > N}}。", "W + R > N。"), "no \\{\\{c1"),
    (TRANSLATED.replace("## Q zh", "## Notes"), "unknown section"),
])
def test_half_a_translation_is_rejected(tmp_path, mutation, fragment):
    with pytest.raises(CardError, match=fragment):
        parse_card(write(tmp_path, "bad.md", mutation))


def test_language_does_not_change_a_cards_identity(tmp_path):
    """The same card in two languages is one card: same id, so re-importing
    a translated build replaces the text in place and review history lives."""
    import genanki
    en = parse_card(write(tmp_path, "my-card.md", QA))
    zh = parse_card(write(tmp_path, "my-card.md", TRANSLATED))
    assert genanki.guid_for(f"trellis:{en.id}") == genanki.guid_for(f"trellis:{zh.id}")
