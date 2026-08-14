"""Cards: Obsidian-native markdown files that compile to Anki notes.

A card lives anywhere under vault/cards/ and looks like:

    ---
    id: cap-theorem
    node: consistency.cap
    type: qa            # qa (default) | cloze
    tags: [tradeoffs]   # optional extra Anki tags
    source: primer      # optional attribution key
    ---
    ## Q
    What does the CAP theorem state?
    ## A
    During a network partition, a distributed system must choose ...

Cloze cards have no Q/A sections; the body holds Anki cloze syntax:

    ---
    id: quorum-formula
    node: storage.replication
    type: cloze
    ---
    A quorum needs {{c1::W + R > N}} to guarantee read-your-writes.

The card `id` is the Anki GUID: rename it and Anki treats the card as new;
keep it and edits update the existing card in place.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_CLOZE_RE = re.compile(r"\{\{c\d+::")
CARD_TYPES = ("qa", "cloze")


class CardError(ValueError):
    """Raised for a card file that violates the format."""


@dataclass
class Card:
    id: str
    node: str
    type: str
    path: Path
    question: str = ""
    answer: str = ""
    text: str = ""  # cloze body
    tags: list[str] = field(default_factory=list)
    source: str = ""


def _split_frontmatter(raw: str, path: Path) -> tuple[dict, str]:
    if not raw.startswith("---\n"):
        raise CardError(f"{path}: missing YAML frontmatter")
    try:
        _, fm, body = raw.split("---\n", 2)
    except ValueError:
        raise CardError(f"{path}: unterminated frontmatter") from None
    meta = yaml.safe_load(fm)
    if not isinstance(meta, dict):
        raise CardError(f"{path}: frontmatter must be a mapping")
    return meta, body.strip()


def _split_qa(body: str, path: Path) -> tuple[str, str]:
    match = re.match(r"^##\s*Q\s*\n(.*?)\n##\s*A\s*\n(.*)$", body, re.DOTALL)
    if not match:
        raise CardError(f"{path}: qa card body must be '## Q' section then '## A' section")
    question, answer = match.group(1).strip(), match.group(2).strip()
    if not question or not answer:
        raise CardError(f"{path}: empty question or answer")
    return question, answer


def parse_card(path: str | Path) -> Card:
    path = Path(path)
    meta, body = _split_frontmatter(path.read_text(encoding="utf-8"), path)

    card_id = meta.get("id")
    if not isinstance(card_id, str) or not _ID_RE.match(card_id):
        raise CardError(f"{path}: invalid id {card_id!r} (want lowercase-hyphenated slug)")
    node = meta.get("node")
    if not isinstance(node, str) or not node:
        raise CardError(f"{path}: missing node")
    card_type = meta.get("type", "qa")
    if card_type not in CARD_TYPES:
        raise CardError(f"{path}: type must be one of {CARD_TYPES}, got {card_type!r}")
    tags = meta.get("tags", []) or []
    if not (isinstance(tags, list) and all(isinstance(t, str) for t in tags)):
        raise CardError(f"{path}: tags must be a list of strings")
    unknown = set(meta) - {"id", "node", "type", "tags", "source"}
    if unknown:
        raise CardError(f"{path}: unknown frontmatter keys {sorted(unknown)}")

    card = Card(
        id=card_id,
        node=node,
        type=card_type,
        path=path,
        tags=list(tags),
        source=str(meta.get("source", "") or ""),
    )
    if card_type == "qa":
        card.question, card.answer = _split_qa(body, path)
    else:
        if not body:
            raise CardError(f"{path}: empty cloze body")
        if not _CLOZE_RE.search(body):
            raise CardError(f"{path}: cloze card has no {{{{c1::...}}}} deletion")
        card.text = body
    return card


def load_cards(cards_dir: str | Path) -> tuple[list[Card], list[str]]:
    """Parse every .md file under cards_dir. Returns (cards, errors) —
    one bad file never hides the rest."""
    cards: list[Card] = []
    errors: list[str] = []
    for path in sorted(Path(cards_dir).rglob("*.md")):
        try:
            cards.append(parse_card(path))
        except CardError as exc:
            errors.append(str(exc))
    return cards, errors
