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
import json
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from .build import build_package
from .cards import Card, load_cards
from .clippings import (
    CLIPPINGS_DIRNAME,
    Clipping,
    ClipError,
    canonical_url,
    fetch_page,
    load_clippings,
    write_clipping,
)
from .cases import CASES_DIRNAME, load_cases
from .codebases import CodebaseError, artefacts, fetch, load_codebase
from .drills import Drill, load_drills
from .obsidian import vault_name
from .path import study_path
from .readings import Reading, load_readings
from .scaffold import import_cards, scaffold_prompt
from .skeleton import Skeleton, SkeletonError, load_skeleton
from .sync import sync, write_managed
from .triage import accept, codebase_index, triage_prompt
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
    cases: list[Reading] = field(default_factory=list)
    case_errors: list[str] = field(default_factory=list)
    clippings: dict[str, Clipping] = field(default_factory=dict)

    def report(self):
        return validate(self.skeleton, self.cards, self.card_errors,
                        self.readings, self.reading_errors,
                        self.drills, self.drill_errors, self.clippings,
                        self.cases, self.case_errors)

    def content_dir(self, root: Path) -> Path:
        """This domain's folder inside the Obsidian vault. Not the vault
        itself — `vault/` is one Obsidian vault holding every domain."""
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
    vault = project.content_dir(root)
    if (vault / "cards").exists():
        project.cards, project.card_errors = load_cards(vault / "cards")
    if (vault / "readings").exists():
        project.readings, project.reading_errors = load_readings(vault / "readings")
    if (vault / "drills").exists():
        project.drills, project.drill_errors = load_drills(vault / "drills")
    if (vault / CASES_DIRNAME).exists():
        project.cases, project.case_errors = load_cases(vault / CASES_DIRNAME)
    if (vault / CLIPPINGS_DIRNAME).exists():
        project.clippings = load_clippings(vault / CLIPPINGS_DIRNAME)
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
          f"{len(project.cases)} cases, "
          f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 0 if report.ok else 1


def cmd_sync(args, project: Project) -> int:
    _checked(project, "syncing")
    result = sync(project.skeleton, project.cards, project.content_dir(args.root),
                  project.readings, project.drills, project.cases,
                  project.clippings)
    print(f"{project.skeleton.domain}: updated {len(result['written'])} note(s)")
    for orphan in result["orphans"]:
        print(f"warning: orphan map note (node no longer in skeleton): {orphan}")
    return 0


def cmd_build(args, project: Project) -> int:
    _checked(project, "building")
    if not project.cards:
        # A skeleton with no cards yet is the normal early state of a new
        # domain, not an error: the map and its sources are authored first
        # and cards are grown branch by branch.
        if getattr(args, "all", False):
            print(f"{project.skeleton.domain}: skeleton only, no cards to build yet")
            return 0
        _fail(f"{project.skeleton.domain}: no cards to build")
    out = args.output or args.root / "dist" / f"{project.skeleton.domain}.apkg"
    result = build_package(
        project.skeleton, project.cards, out, project.readings,
        vault=args.vault_name or vault_name(args.root / "vault"),
        clippings=project.clippings,
        cases=project.cases,
        lang=args.lang,
    )
    print(f"wrote {result['path']}: {result['notes']} notes in {result['decks']} decks")
    return 0


def cmd_stats(args, project: Project) -> int:
    from .links import coverage, leaves_without_readable_source
    s = project.skeleton
    per_node = Counter(c.node for c in project.cards)
    linked_all, total_all = coverage(s, project.cards, project.readings)
    pct = f"{linked_all / total_all:.0%}" if total_all else "n/a"
    hunting = leaves_without_readable_source(s, project.readings, project.clippings)
    readable = len(s.leaves()) - len(hunting)
    print(f"{s.title} — {len(project.cards)} cards, {len(project.readings)} readings, "
          f"{len(project.drills)} drills, link coverage {pct}, "
          f"readable sources {readable}/{len(s.leaves())} leaves, "
          f"{len(project.card_errors)} unparseable")
    langs = Counter(lang for c in project.cards for lang in c.tr)
    for lang, n in sorted(langs.items()):
        print(f"  translated into {lang}: {n}/{len(project.cards)} cards "
              f"({n / len(project.cards):.0%})")
    for root_node in s.roots:
        subtree = [root_node] + [n for n in s.walk()
                                 if n.id.startswith(root_node.id + ".")]
        branch_cards = [c for c in project.cards
                        if c.node in {n.id for n in subtree}]
        leaves = [n for n in subtree if n.is_leaf]
        covered = sum(1 for n in leaves if per_node.get(n.id))
        linked, total = coverage(s, branch_cards, project.readings)
        link_pct = f"{linked / total:>4.0%}" if total else " n/a"
        print(f"  {root_node.title:<28} {total:>4} cards   "
              f"{covered:>2}/{len(leaves):<2} leaves   links {link_pct}")
    return 0


def cmd_path(args, project: Project) -> int:
    _checked(project, "generating the path")
    body = study_path(project.skeleton, project.cards, weeks=args.weeks)
    out = project.content_dir(args.root) / "Study Path.md"
    changed = write_managed(out, body)
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
        project.content_dir(args.root) / "cards",
    )
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        _fail("nothing imported")
    for path in written:
        print(f"wrote {path}")
    print(f"imported {len(written)} card(s); run `trellis sync` to refresh map notes")
    return 0


def cmd_clip(args, project: Project) -> int:
    """Archive readings' pages into the vault so they can be read in
    Obsidian offline. Already-clipped readings are skipped, so this is
    safe to re-run; pages the Web Clipper saved are recognised too."""
    from datetime import date

    dest = project.content_dir(args.root) / CLIPPINGS_DIRNAME
    today = date.today().isoformat()
    todo = [
        r for r in project.readings
        if r.url and canonical_url(r.url) not in project.clippings
    ]
    if args.node:
        todo = [r for r in todo if any(n.startswith(args.node) for n in r.nodes)]
    if not todo:
        print(f"{project.skeleton.domain}: every reading is already clipped")
        return 0

    clipped, failed = 0, []
    for reading in todo:
        try:
            page = fetch_page(reading.url)
        except ClipError as exc:
            failed.append((reading.path.stem, str(exc)))
            continue
        if not page.title:
            page.title = reading.title
        path = write_clipping(dest, reading.path.stem, reading.url, page, today)
        print(f"clipped {path.name}  <- {reading.url}")
        clipped += 1
    print(f"{project.skeleton.domain}: {clipped} clipped, {len(failed)} skipped")
    for slug, why in failed:
        print(f"  skipped {slug}: {why}")
    return 0


def cmd_anki_align(args, project: Project) -> int:
    from .anki import AnkiConnectError, align
    try:
        result = align(project.skeleton, url=args.anki_url)
    except AnkiConnectError as exc:
        _fail(str(exc))
    print(f"{project.skeleton.domain}: moved {result['moved']} card(s), "
          f"deleted {len(result['deleted'])} stale deck(s)")
    for name in result["deleted"]:
        print(f"  deleted: {name}")
    return 0


def _all_skeletons(root: Path) -> dict:
    return {d: _load(root, d).skeleton for d in _domains(root)}


def _vault_note_names(root: Path) -> set[str]:
    """Every note name in the vault. Names must stay unique because card
    links resolve a note by name, not by path."""
    return {p.stem for p in (root / "vault").rglob("*.md")}


def cmd_triage(args) -> int:
    try:
        codebase = load_codebase(args.root / "codebases" / f"{args.codebase}.yaml")
    except CodebaseError as exc:
        _fail(str(exc))
    print(f"fetching {codebase.repo}@{codebase.ref} ...", file=sys.stderr)
    try:
        sha = fetch(codebase, args.root)
    except CodebaseError as exc:
        _fail(str(exc))
    found = artefacts(codebase, args.root)
    if args.kinds:
        wanted = set(args.kinds.split(","))
        found = [a for a in found if a.kind in wanted]
    if not found:
        _fail("no artefacts matched")
    skeletons = _all_skeletons(args.root)
    if args.lens:
        skeletons = {k: v for k, v in skeletons.items() if k in args.lens.split(",")}
    prompt = triage_prompt(codebase, sha, found, skeletons, prefix=args.prefix)
    out = args.output or args.root / "proposals" / f"{codebase.name}.prompt.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(prompt, encoding="utf-8")
    print(f"{len(found)} artefact(s) at {sha[:12]} -> {out}")
    return 0


def cmd_accept(args) -> int:
    skeletons = _all_skeletons(args.root)
    written, errors, gaps = accept(
        args.file, args.root, skeletons, _vault_note_names(args.root)
    )
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        _fail("nothing accepted")
    for path in written:
        print(f"wrote {path}")
    for gap in gaps:
        print(f"gap: {gap.get('lens')} needs {gap.get('proposed_leaf')!r} "
              f"— {gap.get('why', '')}")
    if written:
        name = json.loads(Path(args.file).read_text(encoding="utf-8"))["codebase"]
        index = args.root / "vault" / "Codebases" / f"{name}.md"
        index.parent.mkdir(parents=True, exist_ok=True)
        write_managed(index, codebase_index(args.root, name, _domains(args.root)))
        print(f"index: {index}")
    print(f"accepted {len(written)} case(s), {len(gaps)} skeleton gap(s) proposed")
    return 0


CROSS_DOMAIN = {"triage": cmd_triage, "accept": cmd_accept}

HANDLERS = {
    "clip": cmd_clip,
    "anki-align": cmd_anki_align,
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
    p_build.add_argument(
        "--lang", default="",
        help="render cards in this language where a translation exists "
             "(e.g. zh); card ids are unchanged, so re-importing swaps the "
             "text in place and keeps review history",
    )
    p_build.add_argument(
        "--vault-name",
        help="Obsidian vault name used in obsidian:// links "
             "(default: the vault directory's name)",
    )
    p_clip = sub.add_parser(
        "clip",
        help="archive readings' pages as markdown in the vault, so cards can "
             "open them in Obsidian instead of a browser",
    )
    p_clip.add_argument("--node", help="only readings under this node id")
    sub.add_parser("stats", help="card counts and leaf coverage per branch")
    p_path = sub.add_parser("path", help="write the linear study path into the vault")
    p_path.add_argument("--weeks", type=int)
    p_scaffold = sub.add_parser("scaffold", help="emit an LLM prompt for a node")
    p_scaffold.add_argument("node")
    p_scaffold.add_argument("-n", "--count", type=int, default=8)
    p_scaffold.add_argument("-o", "--output", type=Path)
    p_triage = sub.add_parser(
        "triage",
        help="prepare a triage prompt for a declared codebase "
             "(codebases/<name>.yaml)",
    )
    p_triage.add_argument("codebase")
    p_triage.add_argument("--kinds", help="only these harvest kinds, comma separated")
    p_triage.add_argument("--lens", help="only offer these lenses, comma separated")
    p_triage.add_argument("--prefix", default="", help="slug prefix for proposals")
    p_triage.add_argument("-o", "--output", type=Path)
    p_accept = sub.add_parser(
        "accept", help="validate a triage proposal and write the cases it accepts")
    p_accept.add_argument("file", type=Path)
    p_import = sub.add_parser("import", help="import LLM-generated JSON as cards")
    p_import.add_argument("file", type=Path)
    p_align = sub.add_parser(
        "anki-align",
        help="move cards in a live Anki collection to the decks the current "
             "skeleton defines, and delete stale empty decks (run after "
             "importing the new .apkg; needs desktop Anki + AnkiConnect)",
    )
    p_align.add_argument("--anki-url", default="http://127.0.0.1:8765")

    args = parser.parse_args(argv)
    if args.all and args.command in SINGLE_DOMAIN_ONLY:
        _fail(f"{args.command} needs a single domain")
    if args.all and args.command == "build" and args.output:
        _fail("build --all uses dist/<domain>.apkg; drop -o")

    if args.command in CROSS_DOMAIN:
        return CROSS_DOMAIN[args.command](args)

    exit_code = 0
    for domain in _resolve_domains(args.root, args):
        project = _load(args.root, domain)
        exit_code = max(exit_code, HANDLERS[args.command](args, project))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
