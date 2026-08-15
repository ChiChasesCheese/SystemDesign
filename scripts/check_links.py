#!/usr/bin/env python3
"""Check every reading/drill URL responds. Run manually (network-bound,
so not part of CI): python3 scripts/check_links.py"""

import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from trellis.readings import load_readings  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; trellis-link-check)"}


def check(url: str) -> tuple[bool, str]:
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                return resp.status < 400, str(resp.status)
        except Exception as exc:  # noqa: BLE001 — try GET after HEAD failures
            reason = str(exc)
    return False, reason


def main() -> int:
    urls: dict[str, list[str]] = {}
    for sub in ("readings", "drills"):
        for path in (ROOT / "vault").glob(f"*/{sub}"):
            items, _ = load_readings(path)
            for item in items:
                if item.url:
                    urls.setdefault(item.url, []).append(str(item.path))
    bad = blocked = 0
    for url, files in sorted(urls.items()):
        ok, status = check(url)
        # Bot walls (403, connection resets) and hosts our proxy can't
        # reach are not dead links — flag but don't fail on them.
        is_blocked = not ok and (
            "403" in status or "reset" in status.lower()
            or "web.archive.org" in url
        )
        if ok:
            print(f"ok   {status:>3} {url}")
        elif is_blocked:
            blocked += 1
            print(f"BLKD {status:>3} {url}  (bot wall / proxy — verify in a browser once)")
        else:
            bad += 1
            print(f"BAD  {status:>3} {url}  <- {', '.join(files)}")
    print(f"\n{len(urls)} urls, {bad} broken, {blocked} blocked")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
