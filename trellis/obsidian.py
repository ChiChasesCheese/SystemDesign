"""Obsidian URI construction.

`obsidian://open?vault=<name>&file=<vault-relative path>` opens a note in
the Obsidian app — desktop and mobile alike. Anki hands any non-HTTP link
to the OS URL handler (desktop: QDesktopServices; AnkiMobile: documented
support for opening other apps by scheme), so this is what makes a card
open its archived reading inside Obsidian instead of a browser.

The vault name is the name Obsidian shows for the vault, which is the
vault directory's own name — `vault/` here. It must match on every device
the deck is used from, because the URI travels with the card.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote

# [[target]], [[target|alias]], [[target#heading]], ![[embed]]
_WIKILINK_RE = re.compile(r"\[\[([^\]|#^]+)")


def vault_name(vault_dir: str | Path) -> str:
    return Path(vault_dir).resolve().name


def note_names(vault_dir: str | Path) -> Counter:
    """How many files a wikilink target can mean, across the whole vault.

    Wikilinks resolve by name over the entire vault — that is what lets a
    low-level-design drill link a system-design topic — so the index spans
    every domain, and a name held by two notes is ambiguous for Obsidian
    and for us. Two names reach one file: the bare stem and the full
    filename (`[[paper-clip]]`, `![[paper-clip.pdf]]`). A markdown note
    shadows an attachment of the same stem, which is how a clipped PDF and
    the note embedding it live side by side.
    """
    vault = Path(vault_dir)
    if not vault.exists():
        return Counter()
    files = [p for p in vault.rglob("*") if p.is_file()]
    names = Counter(p.stem for p in files if p.suffix == ".md")
    names.update(p.name for p in files)
    for p in files:
        if p.suffix != ".md" and p.stem not in names:
            names[p.stem] += 1
    return names


def wikilink_targets(text: str) -> list[str]:
    """Bare note names a body links to, in order, duplicates kept."""
    return [m.strip() for m in _WIKILINK_RE.findall(text) if m.strip()]


def open_uri(vault: str, note_path: str | Path) -> str:
    """URI opening `note_path` (vault-relative, extension optional)."""
    rel = str(note_path)
    if rel.endswith(".md"):
        rel = rel[: -len(".md")]
    return (
        "obsidian://open?vault="
        + quote(vault, safe="")
        + "&file="
        + quote(rel, safe="")
    )
