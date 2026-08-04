#!/usr/bin/env python3
"""Build WordPress snippets from page sources.

For every page directory (pages/<name>/ containing an index.html), this:

  1. extracts the content between the PASTE FROM HERE / PASTE TO HERE markers,
  2. applies the string replacements in that page's urls.json (typically one
     prefix rule that maps local asset paths to their live CDN URLs),
  3. validates the result (no leftover local asset paths, no TODO markers),
  4. writes pages/<name>/<name>.wordpress.html — the snippet to paste into
     the WordPress custom HTML block.

The generated file is committed so the exact snippet that went live is in git
history. Never edit it by hand; edit index.html and rerun this script.

Usage:
  scripts/build.py            build every page
  scripts/build.py addaxai    build one page
  scripts/build.py --check    build to memory and fail if any committed
                              snippet is out of date (no files written)
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "pages"
MARK_FROM = "PASTE FROM HERE"
MARK_TO = "PASTE TO HERE"

# a local asset reference that survived URL rewriting, e.g. src="assets/x.webp"
# in markup or url('assets/x.webp') in inline CSS
LOCAL_REF = re.compile(r"""(?:src="|href="|url\(["']?)(assets/[^"')]+)""")


def list_pages():
    return sorted(
        d.name
        for d in PAGES.iterdir()
        if d.is_dir() and not d.name.startswith("_") and (d / "index.html").exists()
    )


def extract_snippet(source_html, page):
    starts = source_html.count(MARK_FROM)
    ends = source_html.count(MARK_TO)
    if starts != 1 or ends != 1:
        raise SystemExit(
            f"{page}: expected exactly one {MARK_FROM!r} and one {MARK_TO!r} "
            f"marker, found {starts} and {ends}"
        )
    i = source_html.index("\n", source_html.index(MARK_FROM)) + 1
    j = source_html.rindex("\n", 0, source_html.index(MARK_TO)) + 1
    return source_html[i:j]


def apply_urlmap(snippet, page_dir):
    urlmap_path = page_dir / "urls.json"
    if not urlmap_path.exists():
        return snippet
    urlmap = json.loads(urlmap_path.read_text())
    # longest key first so an exact-file override beats a prefix rule
    for local in sorted(urlmap, key=len, reverse=True):
        if local.startswith("_"):
            continue  # comment keys
        live = urlmap[local]
        if not isinstance(live, str) or not live.startswith("https://"):
            raise SystemExit(f"{page_dir.name}: urls.json entry {local!r} is not a live https URL")
        snippet = snippet.replace(local, live)
    return snippet


def validate(snippet, page):
    errors = []
    leftover = sorted({m.group(1) for m in LOCAL_REF.finditer(snippet)})
    if leftover:
        errors.append(
            "local asset paths not covered by urls.json:\n    " + "\n    ".join(leftover)
        )
    todos = [
        line.strip()[:100]
        for line in snippet.splitlines()
        if "TODO" in line and "base64," not in line
    ]
    if todos:
        errors.append("TODO markers still in snippet:\n    " + "\n    ".join(todos))
    if errors:
        raise SystemExit(f"{page}: not publishable:\n  " + "\n  ".join(errors))


def build(page, check_only):
    page_dir = PAGES / page
    source = (page_dir / "index.html").read_text()
    snippet = apply_urlmap(extract_snippet(source, page), page_dir)
    validate(snippet, page)
    out = page_dir / f"{page}.wordpress.html"
    size_kb = len(snippet.encode()) / 1024
    if check_only:
        if not out.exists() or out.read_text() != snippet:
            print(f"{page}: {out.relative_to(ROOT)} is OUT OF DATE — run scripts/build.py")
            return False
        print(f"{page}: up to date ({size_kb:.0f} KB)")
        return True
    out.write_text(snippet)
    print(f"{page}: wrote {out.relative_to(ROOT)} ({size_kb:.0f} KB)")
    return True


def main(argv):
    check_only = "--check" in argv
    names = [a for a in argv if not a.startswith("-")] or list_pages()
    for name in names:
        if not (PAGES / name / "index.html").exists():
            raise SystemExit(f"no such page: pages/{name}/index.html")
    ok = all([build(name, check_only) for name in names])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
