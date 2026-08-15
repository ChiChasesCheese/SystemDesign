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

from pathlib import Path
from urllib.parse import quote


def vault_name(vault_dir: str | Path) -> str:
    return Path(vault_dir).resolve().name


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
