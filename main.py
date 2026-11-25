#!/usr/bin/env python3
"""Worst Fix Ever entry: write one commit-message line to /output/entry.txt.

Stdlib only (os, pathlib). The entry is a single line, 1-100 chars.
"""

import os
from pathlib import Path

ENTRY = "fix: printer kept jamming, so I removed the printer; zero jams since Monday"


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 100:
        raise SystemExit(f"entry must be 1-100 chars, got {len(text)}")
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
