"""Study path: flatten the skeleton DAG into a linear curriculum.

Tree order is already a valid topological order (validation guarantees
requires edges never point forward), so the path is the leaf walk with
card counts; --weeks splits it into balanced chunks by card volume.

Drills ride along on the same line: each one lands under the last leaf it
spans, the first point in the walk where you know enough to attempt it. A
drill scheduled any earlier is a drill you fail for the wrong reason.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict

from .cards import Card
from .drills import Drill, drill_title, drilled_leaves
from .skeleton import Skeleton


def _drills_by_unlock(
    skeleton: Skeleton, drills: list[Drill], order: dict[str, int]
) -> dict[int, list[Drill]]:
    """Drill -> position of the last leaf it spans."""
    out: dict[int, list[Drill]] = defaultdict(list)
    for drill in sorted(drills, key=lambda d: d.title):
        covered = [order[leaf] for leaf in drilled_leaves(skeleton, [drill])
                   if leaf in order]
        if covered:
            out[max(covered)].append(drill)
    return out


def study_path(skeleton: Skeleton, cards: list[Card], weeks: int | None = None,
               drills: list[Drill] | None = None) -> str:
    per_node = Counter(c.node for c in cards)
    leaves = skeleton.leaves()
    total = sum(per_node.get(n.id, 0) for n in leaves)

    week_of: dict[str, int] = {}
    if weeks:
        target = total / weeks
        acc, week = 0, 1
        for leaf in leaves:
            # close the week once it has reached its share (never exceed
            # the requested number of weeks)
            if acc >= target * week and week < weeks:
                week += 1
            acc += per_node.get(leaf.id, 0)
            week_of[leaf.id] = week

    order = {leaf.id: i for i, leaf in enumerate(leaves)}
    unlocks = _drills_by_unlock(skeleton, drills or [], order)

    lines = [f"# {skeleton.title} — study path", ""]
    if weeks:
        lines.append(f"{total} cards over {weeks} weeks ≈ "
                     f"{math.ceil(total / (weeks * 7))} new cards/day"
                     + (f", plus {sum(len(v) for v in unlocks.values())} drills."
                        if unlocks else "."))
        lines.append("")

    current_branch = None
    current_week = None
    for position, leaf in enumerate(leaves):
        if weeks and week_of[leaf.id] != current_week:
            current_week = week_of[leaf.id]
            lines += [f"## Week {current_week}", ""]
            current_branch = None
        branch = leaf.path()[0]
        if branch.id != current_branch:
            current_branch = branch.id
            lines.append(f"**{branch.title}**")
        count = per_node.get(leaf.id, 0)
        extras = [f"{count} cards"]
        if leaf.requires:
            needs = ", ".join(skeleton.by_id[r].title for r in leaf.requires)
            extras.append(f"needs: {needs}")
        lines.append(f"- [ ] [[{leaf.id}|{leaf.title}]] — {'; '.join(extras)}")
        for drill in unlocks.get(position, []):
            lines.append(
                f"    - [ ] **Drill:** [[{drill.link_target}|{drill_title(drill)}]]"
            )
    return "\n".join(lines)
