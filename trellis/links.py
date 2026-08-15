"""Links: every card should lead somewhere deeper.

A card counts as linked when its body carries an inline markdown link, or
when its node (or any ancestor) has readings with URLs — those readings
are rendered as a clickable "Sources" footer on the Anki card. Coverage
of that property is a first-class metric: the project's job is to be the
authoritative index, so a card without a road onward is a gap.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .cards import Card
from .clippings import Clipping, canonical_url
from .obsidian import open_uri
from .readings import Reading
from .skeleton import Skeleton

_INLINE_LINK_RE = re.compile(r"\[[^\]]+\]\(https?://")

LINK_COVERAGE_TARGET = 0.7


def has_inline_link(card: Card) -> bool:
    return bool(_INLINE_LINK_RE.search(card.question + card.answer + card.text))


def sources_for(skeleton: Skeleton, readings: list[Reading], node_id: str,
                limit: int = 3) -> list[Reading]:
    """Readings with URLs attached to the node or any ancestor, nearest
    first, deduped by URL."""
    node = skeleton.by_id.get(node_id)
    if node is None:
        return []
    lineage = [n.id for n in reversed(node.path())]
    out: list[Reading] = []
    seen: set[str] = set()
    for ancestor_id in lineage:
        for reading in readings:
            if ancestor_id in reading.nodes and reading.url and reading.url not in seen:
                seen.add(reading.url)
                out.append(reading)
    return out[:limit]


@dataclass
class GoDeeper:
    """One entry of a card's further-reading footer."""

    title: str
    href: str            # obsidian:// when a clipping exists, else the web URL
    web_href: str | None  # the original URL, kept as a fallback when href is local

    @property
    def is_local(self) -> bool:
        return self.href.startswith("obsidian://")


def go_deeper(
    skeleton: Skeleton,
    readings: list[Reading],
    node_id: str,
    vault: str | None = None,
) -> list[GoDeeper]:
    """Footer links for a card on `node_id`.

    The obsidian:// target is always the *reading note* — addressed by name
    alone, never by path. Two reasons: the note is committed, so it exists
    on every device, and a bare name resolves wherever the vault root
    happens to sit (the phone clones the whole repo; the desktop opens
    `vault/`). The clipped article rides along embedded inside that note.
    """
    out: list[GoDeeper] = []
    for reading in sources_for(skeleton, readings, node_id):
        if vault:
            out.append(
                GoDeeper(reading.title, open_uri(vault, reading.path.stem), reading.url)
            )
        else:
            out.append(GoDeeper(reading.title, reading.url, None))
    return out


def coverage(skeleton: Skeleton, cards: list[Card],
             readings: list[Reading]) -> tuple[int, int]:
    """(linked_cards, total_cards)."""
    linked = sum(
        1 for c in cards
        if has_inline_link(c) or sources_for(skeleton, readings, c.node)
    )
    return linked, len(cards)
