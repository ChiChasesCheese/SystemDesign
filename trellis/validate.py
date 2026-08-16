"""Cross-validation: every card and reading must hang off the skeleton
correctly."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from .cards import Card
from .obsidian import wikilink_targets
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
    drills: list[Reading] | None = None,
    drill_errors: list[str] | None = None,
    clippings: dict | None = None,
    notes: Counter | None = None,
) -> Report:
    report = Report(
        errors=list(card_errors) + list(reading_errors or []) + list(drill_errors or [])
    )

    for note in list(readings or []) + list(drills or []):
        for node_id in note.nodes:
            if node_id not in skeleton.by_id:
                report.errors.append(
                    f"{note.path}: node {node_id!r} not in skeleton"
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

    if cards and clippings is not None:
        from .links import leaves_without_readable_source
        hunting = leaves_without_readable_source(skeleton, readings or [], clippings)
        if hunting:
            report.warnings.append(
                f"{len(hunting)} leaf/leaves have no archived, readable source — "
                "their cards point at a book or an index: " + ", ".join(hunting[:8])
                + (" …" if len(hunting) > 8 else "")
            )

    if cards:
        from .links import LINK_COVERAGE_TARGET, coverage
        linked, total = coverage(skeleton, cards, readings or [])
        if linked / total < LINK_COVERAGE_TARGET:
            report.warnings.append(
                f"link coverage {linked}/{total} ({linked / total:.0%}) is below the "
                f"{LINK_COVERAGE_TARGET:.0%} target — attach readings with URLs to "
                "the uncovered nodes"
            )

    if drills is not None:
        from .drills import (
            DRILL_COVERAGE_TARGET, branches_without_drill, drill_coverage,
        )
        undrilled = branches_without_drill(skeleton, drills)
        if undrilled:
            report.warnings.append(
                f"{len(undrilled)} branch(es) have no drill — nothing there trains "
                "producing an answer, only recalling one: " + ", ".join(undrilled)
            )
        done, total = drill_coverage(skeleton, drills)
        if total and done / total < DRILL_COVERAGE_TARGET:
            report.warnings.append(
                f"drill coverage {done}/{total} ({done / total:.0%}) is below the "
                f"{DRILL_COVERAGE_TARGET:.0%} target — write drills spanning the "
                "leaves you have only read about"
            )

    if notes:
        report.errors += _dead_wikilinks(cards, list(readings or []),
                                         list(drills or []), notes)
    return report


def _dead_wikilinks(
    cards: list[Card], readings: list[Reading], drills: list[Reading],
    notes: Counter,
) -> list[str]:
    """Wikilinks that Obsidian would leave unresolved.

    A drill's grading points are wikilinks into the cards that answer them,
    and a reading points at the cards it feeds; when a card is renamed, the
    reference has to break loudly here rather than quietly in the vault.
    Names are resolved across the whole vault, so cross-domain links are
    fine — an ambiguous name is not, since Obsidian then picks for you.
    """
    errors: list[str] = []
    bodies = [(c.path, c.question + "\n" + c.answer + "\n" + c.text) for c in cards]
    bodies += [(n.path, n.body) for n in readings + drills]
    for path, text in bodies:
        for target in dict.fromkeys(wikilink_targets(text)):
            found = notes.get(target, 0)
            if not found:
                errors.append(f"{path}: wikilink [[{target}]] resolves to no note")
            elif found > 1:
                errors.append(
                    f"{path}: wikilink [[{target}]] is ambiguous — {found} notes "
                    "share that name"
                )
    return errors
