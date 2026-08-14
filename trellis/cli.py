"""CLI. Layout convention (one repo, many domains):

    skeleton/<domain>.yaml      the mind map
    vault/<domain>/             Obsidian content for that domain
    vault/<domain>/cards/       cards (leaves)
    vault/<domain>/readings/    long-form notes, multi-node
    vault/<domain>/drills/      design/coding exercises, multi-node
    dist/<domain>.apkg          build output

Open vault/ itself as the Obsidian vault so wikilinks work across domains.
--domain is optional while the repo has one skeleton; --all runs
validate/sync/build/stats/path over every domain.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from .build import build_package
from .cards import Card, load_cards
from .drills import Drill, load_drills
from .path import study_path
from .readings import Reading, load_readings
from .scaffold import import_cards, scaffold_prompt
from .skeleton import Skeleton, SkeletonError, load_skeleton
from .sync import _write_managed, sync
from .validate import validate


def _fail(msg: str) -> "sys.NoReturn":
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(1)


@dataclass
class Project:
    skeleton: Skeleton
    cards: list[Card] = field(default_factory=list)
    card_errors: list[str] = field(default_factory=list)
    readings: list[Reading] = field(default_factory=list)
    reading_errors: list[str] = field(default_factory=list)
    drills: list[Drill] = field(default_factory=list)
    drill_errors: list[str] = field(default_factory=list)

    def report(self):
        return validate(self.skeleton, self.cards, self.card_errors,
                        self.readings, self.reading_errors,
                        self.drills, self.drill_errors)

    def vault(self, root: Path) -> Path:
        return root / "vault" / self.skeleton.domain


def _domains(root: Path) -> list[str]:
    return [f.stem for f in sorted((root / "skeleton").glob("*.yaml"))]


def _resolve_domains(root: Path, args) -> list[str]:
    available = _domains(root)
    if not available:
        _fail(f"no skeleton files in {root / 'skeleton'}")
    if getattr(args, "all", False):
        return available
    if args.domain:
        if args.domain not in available:
            _fail(f"no skeleton/{args.domain}.yaml")
        return [args.domain]
    if len(available) > 1:
        _fail("multiple domains found, pass --domain or --all: "
              + ", ".join(available))
    return available


def _load(root: Path, domain: str) -> Project:
    try:
        skeleton = load_skeleton(root / "skeleton" / f"{domain}.yaml")
    except SkeletonError as exc:
        _fail(str(exc))
    project = Project(skeleton=skeleton)
    vault = project.vault(root)
    if (vault / "cards").exists():
        project.cards, project.card_errors = load_cards(vault / "cards")
    if (vault / "readings").exists():
        project.readings, project.reading_errors = load_readings(vault / "readings")
    if (vault / "drills").exists():
        project.drills, project.drill_errors = load_drills(vault / "drills")
    return project


def _print_report(report) -> None:
    for w in report.warnings:
        print(f"warning: {w}")
    for e in report.errors:
        print(f"error: {e}", file=sys.stderr)


def _checked(project: Project, action: str) -> None:
    report = project.report()
    if not report.ok:
        _print_report(report)
        _fail(f"fix validation errors before {action}")


def cmd_validate(args, project: Project) -> int:
    report = project.report()
    _print_report(report)
    s = project.skeleton
    print(f"{s.title}: {len(s.walk())} nodes, {len(project.cards)} cards, "
          f"{len(project.readings)} readings, {len(project.drills)} drills, "
          f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 0 if report.ok else 1


def cmd_sync(args, project: Project) -> int:
    _checked(project, "syncing")
    result = sync(project.skeleton, project.cards, project.vault(args.root),
                  project.readings, project.drills)
    print(f"{project.skeleton.domain}: updated {len(result['written'])} note(s)")
    for orphan in result["orphans"]:
        print(f"warning: orphan map note (node no longer in skeleton): {orphan}")
    return 0


def cmd_build(args, project: Project) -> int:
    _checked(project, "building")
    if not project.cards:
        _fail(f"{project.skeleton.domain}: no cards to build")
    out = args.output or args.root / "dist" / f"{project.skeleton.domain}.apkg"
    result = build_package(project.skeleton, project.cards, out)
    print(f"wrote {result['path']}: {result['notes']} notes in {result['decks']} decks")
    return 0


def cmd_stats(args, project: Project) -> int:
    s = project.skeleton
    per_node = Counter(c.node for c in project.cards)
    print(f"{s.title} — {len(project.cards)} cards, {len(project.readings)} readings, "
          f"{len(project.drills)} drills, {len(project.card_errors)} unparseable")
    for root_node in s.roots:
        subtree = [root_node] + [n for n in s.walk()
                                 if n.id.startswith(root_node.id + ".")]
        total = sum(per_node.get(n.id, 0) for n in subtree)
        leaves = [n for n in subtree if n.is_leaf]
        covered = sum(1 for n in leaves if per_node.get(n.id))
        print(f"  {root_node.title:<28} {total:>4} cards   "
              f"{covered}/{len(leaves)} leaves covered")
    return 0


def cmd_path(args, project: Project) -> int:
    _checked(project, "generating the path")
    body = study_path(project.skeleton, project.cards, weeks=args.weeks)
    out = project.vault(args.root) / "Study Path.md"
    changed = _write_managed(out, body)
    print(f"{'updated' if changed else 'unchanged'}: {out}")
    return 0


def cmd_scaffold(args, project: Project) -> int:
    if args.node not in project.skeleton.by_id:
        _fail(f"unknown node {args.node!r}")
    prompt = scaffold_prompt(project.skeleton, args.node, project.cards,
                             count=args.count)
    if args.output:
        Path(args.output).write_text(prompt, encoding="utf-8")
        print(f"wrote {args.output}")
    else:
        print(prompt)
    return 0


def cmd_import(args, project: Project) -> int:
    if project.card_errors:
        for e in project.card_errors:
            print(f"error: {e}", file=sys.stderr)
        _fail("fix existing card errors before importing")
    written, errors = import_cards(
        project.skeleton, project.cards, args.file,
        project.vault(args.root) / "cards",
    )
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        _fail("nothing imported")
    for path in written:
        print(f"wrote {path}")
    print(f"imported {len(written)} card(s); run `trellis sync` to refresh map notes")
    return 0


HANDLERS = {
    "validate": cmd_validate,
    "sync": cmd_sync,
    "build": cmd_build,
    "stats": cmd_stats,
    "path": cmd_path,
    "scaffold": cmd_scaffold,
    "import": cmd_import,
}
SINGLE_DOMAIN_ONLY = {"scaffold", "import"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="trellis",
        description="Skeleton-constrained knowledge cards: Obsidian in, Anki out.",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(),
                        help="project root (default: cwd)")
    parser.add_argument("--domain", help="domain slug (default: the only skeleton)")
    parser.add_argument("--all", action="store_true",
                        help="run over every domain in skeleton/")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="check skeleton, cards, readings, drills")
    sub.add_parser("sync", help="regenerate Obsidian map notes from the skeleton")
    p_build = sub.add_parser("build", help="compile vault into an Anki .apkg")
    p_build.add_argument("-o", "--output", type=Path)
    sub.add_parser("stats", help="card counts and leaf coverage per branch")
    p_path = sub.add_parser("path", help="write the linear study path into the vault")
    p_path.add_argument("--weeks", type=int)
    p_scaffold = sub.add_parser("scaffold", help="emit an LLM prompt for a node")
    p_scaffold.add_argument("node")
    p_scaffold.add_argument("-n", "--count", type=int, default=8)
    p_scaffold.add_argument("-o", "--output", type=Path)
    p_import = sub.add_parser("import", help="import LLM-generated JSON as cards")
    p_import.add_argument("file", type=Path)

    args = parser.parse_args(argv)
    if args.all and args.command in SINGLE_DOMAIN_ONLY:
        _fail(f"{args.command} needs a single domain")
    if args.all and args.command == "build" and args.output:
        _fail("build --all uses dist/<domain>.apkg; drop -o")

    exit_code = 0
    for domain in _resolve_domains(args.root, args):
        project = _load(args.root, domain)
        exit_code = max(exit_code, HANDLERS[args.command](args, project))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
