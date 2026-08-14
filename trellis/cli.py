"""CLI. Layout convention (one repo, many domains):

    skeleton/<domain>.yaml      the mind map
    vault/<domain>/             Obsidian vault content for that domain
    vault/<domain>/cards/       card files (leaves)
    dist/<domain>.apkg          build output

--domain is optional while the repo has exactly one skeleton file.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

from .build import build_package
from .cards import load_cards
from .readings import load_readings
from .scaffold import import_cards, scaffold_prompt
from .skeleton import Skeleton, SkeletonError, load_skeleton
from .sync import sync
from .validate import validate


def _fail(msg: str) -> "sys.NoReturn":
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(1)


def _resolve_domain(root: Path, domain: str | None) -> str:
    skel_dir = root / "skeleton"
    files = sorted(skel_dir.glob("*.yaml"))
    if domain:
        if not (skel_dir / f"{domain}.yaml").exists():
            _fail(f"no skeleton/{domain}.yaml")
        return domain
    if not files:
        _fail(f"no skeleton files in {skel_dir}")
    if len(files) > 1:
        _fail("multiple domains found, pass --domain: "
              + ", ".join(f.stem for f in files))
    return files[0].stem


def _load(root: Path, domain: str):
    try:
        skeleton = load_skeleton(root / "skeleton" / f"{domain}.yaml")
    except SkeletonError as exc:
        _fail(str(exc))
    cards_dir = root / "vault" / domain / "cards"
    cards, card_errors = load_cards(cards_dir) if cards_dir.exists() else ([], [])
    readings_dir = root / "vault" / domain / "readings"
    readings, reading_errors = (
        load_readings(readings_dir) if readings_dir.exists() else ([], [])
    )
    return skeleton, cards, card_errors, readings, reading_errors


def _print_report(report) -> None:
    for w in report.warnings:
        print(f"warning: {w}")
    for e in report.errors:
        print(f"error: {e}", file=sys.stderr)


def cmd_validate(args) -> int:
    skeleton, cards, card_errors, readings, reading_errors = _load(args.root, args.domain)
    report = validate(skeleton, cards, card_errors, readings, reading_errors)
    _print_report(report)
    nodes = len(skeleton.walk())
    print(f"{skeleton.title}: {nodes} nodes, {len(cards)} cards, "
          f"{len(readings)} readings, "
          f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 0 if report.ok else 1


def cmd_sync(args) -> int:
    skeleton, cards, card_errors, readings, reading_errors = _load(args.root, args.domain)
    report = validate(skeleton, cards, card_errors, readings, reading_errors)
    if not report.ok:
        _print_report(report)
        _fail("fix validation errors before syncing")
    result = sync(skeleton, cards, args.root / "vault" / skeleton.domain, readings)
    print(f"updated {len(result['written'])} note(s)")
    for orphan in result["orphans"]:
        print(f"warning: orphan map note (node no longer in skeleton): {orphan}")
    return 0


def cmd_build(args) -> int:
    skeleton, cards, card_errors, readings, reading_errors = _load(args.root, args.domain)
    report = validate(skeleton, cards, card_errors, readings, reading_errors)
    if not report.ok:
        _print_report(report)
        _fail("fix validation errors before building")
    if not cards:
        _fail("no cards to build")
    out = args.output or args.root / "dist" / f"{skeleton.domain}.apkg"
    result = build_package(skeleton, cards, out)
    print(f"wrote {result['path']}: {result['notes']} notes in {result['decks']} decks")
    return 0


def cmd_stats(args) -> int:
    skeleton, cards, card_errors, readings, _ = _load(args.root, args.domain)
    per_node = Counter(c.node for c in cards)
    print(f"{skeleton.title} — {len(cards)} cards, {len(readings)} readings, "
          f"{len(card_errors)} unparseable")
    for root_node in skeleton.roots:
        subtree = [root_node] + [n for n in skeleton.walk()
                                 if n.id.startswith(root_node.id + ".")]
        total = sum(per_node.get(n.id, 0) for n in subtree)
        leaves = [n for n in subtree if n.is_leaf]
        covered = sum(1 for n in leaves if per_node.get(n.id))
        print(f"  {root_node.title:<28} {total:>4} cards   "
              f"{covered}/{len(leaves)} leaves covered")
    return 0


def cmd_scaffold(args) -> int:
    skeleton, cards, _, _, _ = _load(args.root, args.domain)
    if args.node not in skeleton.by_id:
        _fail(f"unknown node {args.node!r}")
    prompt = scaffold_prompt(skeleton, args.node, cards, count=args.count)
    if args.output:
        Path(args.output).write_text(prompt, encoding="utf-8")
        print(f"wrote {args.output}")
    else:
        print(prompt)
    return 0


def cmd_import(args) -> int:
    skeleton, cards, card_errors, _, _ = _load(args.root, args.domain)
    if card_errors:
        for e in card_errors:
            print(f"error: {e}", file=sys.stderr)
        _fail("fix existing card errors before importing")
    written, errors = import_cards(
        skeleton, cards, args.file, args.root / "vault" / skeleton.domain / "cards"
    )
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        _fail("nothing imported")
    for path in written:
        print(f"wrote {path}")
    print(f"imported {len(written)} card(s); run `trellis sync` to refresh map notes")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="trellis",
        description="Skeleton-constrained knowledge cards: Obsidian in, Anki out.",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(),
                        help="project root (default: cwd)")
    parser.add_argument("--domain", help="domain slug (default: the only skeleton)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="check skeleton and all cards")
    sub.add_parser("sync", help="regenerate Obsidian map notes from the skeleton")
    p_build = sub.add_parser("build", help="compile vault into an Anki .apkg")
    p_build.add_argument("-o", "--output", type=Path)
    sub.add_parser("stats", help="card counts and leaf coverage per branch")
    p_scaffold = sub.add_parser("scaffold", help="emit an LLM prompt for a node")
    p_scaffold.add_argument("node")
    p_scaffold.add_argument("-n", "--count", type=int, default=8)
    p_scaffold.add_argument("-o", "--output", type=Path)
    p_import = sub.add_parser("import", help="import LLM-generated JSON as cards")
    p_import.add_argument("file", type=Path)

    args = parser.parse_args(argv)
    args.domain = _resolve_domain(args.root, args.domain)
    handler = {
        "validate": cmd_validate,
        "sync": cmd_sync,
        "build": cmd_build,
        "stats": cmd_stats,
        "scaffold": cmd_scaffold,
        "import": cmd_import,
    }[args.command]
    return handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
