#!/usr/bin/env python3
"""Render a page to a PNG with headless Chrome, for checking visual changes.

Usage:
  scripts/screenshot.py addaxai                    desktop, 1440 x 4600
  scripts/screenshot.py addaxai --width 390        mobile width
  scripts/screenshot.py addaxai --height 8000 --out preview/tall.png

Headless Chrome clamps the window to a 500 px minimum width. For narrower
widths this script wraps the page in an iframe of the requested width and
screenshots that instead, so mobile layouts render correctly.

Output goes to preview/ (gitignored) unless --out is given. Set the CHROME
env var if Chrome lives somewhere non-standard.
"""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
MIN_CHROME_WIDTH = 500


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("page", help="page name under pages/, or a path to an html file")
    p.add_argument("--width", type=int, default=1440)
    p.add_argument("--height", type=int, default=4600)
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    html = Path(args.page)
    if not html.suffix == ".html":
        html = ROOT / "pages" / args.page / "index.html"
    if not html.exists():
        sys.exit(f"not found: {html}")
    html = html.resolve()

    out = args.out or ROOT / "preview" / f"{html.parent.name}-{args.width}.png"
    out.parent.mkdir(parents=True, exist_ok=True)

    target = html
    wrapper = None
    if args.width < MIN_CHROME_WIDTH:
        # iframe of the requested width inside a window Chrome will accept
        wrapper = tempfile.NamedTemporaryFile(
            mode="w", suffix=".html", dir=html.parent, delete=False
        )
        wrapper.write(
            f'<!doctype html><body style="margin:0">'
            f'<iframe src="{html.name}" style="border:0;display:block;'
            f'width:{args.width}px;height:{args.height}px"></iframe>'
        )
        wrapper.close()
        target = Path(wrapper.name)

    try:
        subprocess.run(
            [
                CHROME,
                "--headless",
                "--disable-gpu",
                "--hide-scrollbars",
                "--allow-file-access-from-files",
                f"--screenshot={out}",
                f"--window-size={max(args.width, MIN_CHROME_WIDTH)},{args.height}",
                f"file://{target}",
            ],
            check=True,
            capture_output=True,
        )
    finally:
        if wrapper:
            os.unlink(wrapper.name)
    print(f"wrote {out.relative_to(Path.cwd()) if out.is_relative_to(Path.cwd()) else out}")


if __name__ == "__main__":
    main()
