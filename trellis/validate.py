"""Cross-validation: every card and reading must hang off the skeleton
correctly."""

from __future__ import annotations

from dataclasses import dataclass, field

from .cards import Card
from .readings import Reading
from .skeleton import Skeleton


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate(
    skeleton: Skeleton,
    cards: list[Card],
    card_errors: list[str],
    readings: list[Reading] | None = None,
    reading_errors: list[str] | None = None,
) -> Report:
    report = Report(errors=list(card_errors) + list(reading_errors or []))

    for reading in readings or []:
        for node_id in reading.nodes:
            if node_id not in skeleton.by_id:
                report.errors.append(
                    f"{reading.path}: node {node_id!r} not in skeleton"
                )

    seen: dict[str, Card] = {}
    for card in cards:
        if card.path.stem != card.id:
            report.errors.append(
                f"{card.path}: filename must equal card id ({card.id}.md) — "
                "Obsidian wikilinks depend on it"
            )
        if card.id in seen:
            report.errors.append(
                f"duplicate card id {card.id!r}: {seen[card.id].path} and {card.path}"
            )
        else:
            seen[card.id] = card

        node = skeleton.by_id.get(card.node)
        if node is None:
            report.errors.append(f"{card.path}: node {card.node!r} not in skeleton")
        elif not node.is_leaf:
            report.warnings.append(
                f"{card.path}: attached to non-leaf node {card.node!r} "
                "(allowed, but prefer leaves)"
            )

    covered = {c.node for c in cards}
    bare = [n.id for n in skeleton.leaves() if n.id not in covered]
    if bare:
        report.warnings.append(
            f"{len(bare)} leaf node(s) have no cards yet: " + ", ".join(bare)
        )
    return report
