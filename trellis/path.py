"""Study path: flatten the skeleton DAG into a linear curriculum.

Tree order is already a valid topological order (validation guarantees
requires edges never point forward), so the path is the leaf walk with
card counts; --weeks splits it into balanced chunks by card volume.
"""

from __future__ import annotations

import math
from collections import Counter

from .cards import Card
from .skeleton import Skeleton


def study_path(skeleton: Skeleton, cards: list[Card], weeks: int | None = None) -> str:
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

    lines = [f"# {skeleton.title} — study path", ""]
    if weeks:
        lines.append(f"{total} cards over {weeks} weeks ≈ "
                     f"{math.ceil(total / (weeks * 7))} new cards/day.")
        lines.append("")

    current_branch = None
    current_week = None
    for leaf in leaves:
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
    return "\n".join(lines)
