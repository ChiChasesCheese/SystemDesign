"""Links: every card should lead somewhere deeper.

A card counts as linked when its body carries an inline markdown link, or
when its node (or any ancestor) has readings with URLs — those readings
are rendered as a clickable "Sources" footer on the Anki card. Coverage
of that property is a first-class metric: the project's job is to be the
authoritative index, so a card without a road onward is a gap.
"""

from __future__ import annotations

import re

from .cards import Card
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


def coverage(skeleton: Skeleton, cards: list[Card],
             readings: list[Reading]) -> tuple[int, int]:
    """(linked_cards, total_cards)."""
    linked = sum(
        1 for c in cards
        if has_inline_link(c) or sources_for(skeleton, readings, c.node)
    )
    return linked, len(cards)
