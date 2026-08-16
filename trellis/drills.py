"""Drills: output practice attached to the same skeleton.

Cards recall knowledge, readings feed it in — drills train producing it:
a 40-minute design question, a coding exercise, a mock-interview scenario.
A drill lives under vault/<domain>/drills/, attaches to one or more nodes
(a real design question always spans several), and its body holds the
prompt, constraints, grading points, and your attempt log.

The file format is identical to readings (frontmatter: nodes, optional
title/url/tags), so the parser is shared.
"""

from __future__ import annotations

from pathlib import Path

from .readings import Reading as Drill, load_readings
from .skeleton import Skeleton

__all__ = [
    "DRILL_COVERAGE_TARGET",
    "Drill",
    "branches_without_drill",
    "drill_coverage",
    "drill_title",
    "drilled_leaves",
    "load_drills",
]

# Recall is measured by cards; this is the share of the map you have
# practised *producing* an answer for. Lower than the link target because
# one drill legitimately carries several leaves, and a domain in its first
# weeks has cards long before it has exercises.
DRILL_COVERAGE_TARGET = 0.6


def load_drills(drills_dir: str | Path) -> tuple[list[Drill], list[str]]:
    return load_readings(drills_dir)


def drill_title(drill: Drill) -> str:
    """The title without the "Drill:" the note's own H1 carries — every
    place we render one already says which it is."""
    return drill.title.removeprefix("Drill:").strip()


def drilled_leaves(skeleton: Skeleton, drills: list[Drill]) -> set[str]:
    """Leaves exercised by at least one drill.

    A drill names the nodes it spans; naming an inner node claims its whole
    subtree, because a question about "distributed transactions" is a
    question about each of its probes.
    """
    named = {n for d in drills for n in d.nodes if n in skeleton.by_id}
    return {
        leaf.id for leaf in skeleton.leaves()
        if any(n.id in named for n in leaf.path())
    }


def drill_coverage(skeleton: Skeleton, drills: list[Drill]) -> tuple[int, int]:
    """(drilled_leaves, total_leaves)."""
    leaves = skeleton.leaves()
    return len(drilled_leaves(skeleton, drills) & {n.id for n in leaves}), len(leaves)


def branches_without_drill(skeleton: Skeleton, drills: list[Drill]) -> list[str]:
    """Top-level branches no drill touches — whole areas you have only ever
    read about."""
    drilled = drilled_leaves(skeleton, drills)
    return [
        root.id for root in skeleton.roots
        if not any(leaf.id in drilled for leaf in skeleton.leaves()
                   if leaf.path()[0].id == root.id)
    ]
