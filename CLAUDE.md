# CLAUDE.md

Source for hand-built pages on [addaxdatascience.com](https://addaxdatascience.com)
(WordPress). Each page is a single self-contained HTML file — markup plus one
inline `<style>` block. No build step, no framework, no JS beyond third-party
embeds (currently one Stripe buy button).

## Layout

```
pages/<name>/index.html            page source — THE file to edit
pages/<name>/urls.json             local path → live URL rewrites for publishing
pages/<name>/<name>.wordpress.html GENERATED snippet — never edit by hand
pages/<name>/assets/               images for that page
pages/_template/                   boilerplate for starting a new page
shared/fonts/                      original woff2 files (pages embed them as base64)
scripts/build.py                   source → WordPress snippet (extract, rewrite URLs, validate)
scripts/screenshot.py              render a page to PNG with headless Chrome
```

## Commands

```sh
python3 scripts/build.py              # regenerate all snippets (run after editing a page)
python3 scripts/build.py --check      # fail if any committed snippet is stale
python3 scripts/screenshot.py addaxai            # desktop render → preview/
python3 scripts/screenshot.py addaxai --width 390  # mobile render (iframe trick)
```

Preview = open `pages/<name>/index.html` in a browser; it renders standalone.

## Hard rules

- `*.wordpress.html` is generated output. Edit `index.html`, rerun build.py.
- Keep the `PASTE FROM HERE` / `PASTE TO HERE` markers intact — build.py
  extracts between them, and everything outside is local-preview scaffolding.
- Every CSS rule is scoped under the page's wrapper class (`.aai-lp` for the
  AddaxAI page). Never emit an unscoped selector; it would leak into the
  WordPress theme.
- Reference images with relative `assets/...` paths so the local preview
  works; `urls.json` maps them to live jsDelivr URLs at build time. An asset
  is published by committing it and pushing — jsDelivr serves this repo at
  `cdn.jsdelivr.net/gh/PetervanLunteren/addaxdatascience-web@main/...`.
  Consequence: renaming or moving a committed asset breaks the live page
  until the snippet is rebuilt and re-pasted (jsDelivr's `@main` cache lags
  ~12 h). Prefer adding new files over renaming published ones.
- Fonts are embedded in the CSS as base64 (Lexend, the brand face) — never a
  Google Fonts link or media-library upload. See CONVENTIONS.md for why.
- New pages start from `pages/_template/` — copy, pick a CSS prefix,
  find-and-replace `xxx`.

Page anatomy, naming, and styling conventions: `CONVENTIONS.md`.
Publishing workflow and WordPress gotchas: `README.md`.
Backlog: `TODO.md`.

## Context

- The AddaxAI page content derives from the Docusaurus marketing homepage in
  the AddaxAI-WebUI repo; the species-model list comes from `models.json`
  there. Docs links point at `https://docs.addaxai.com/` — if the docs move,
  one find-and-replace covers all of them.
- A likely future page: AddaxAI Connect
  (github.com/PetervanLunteren/AddaxAI-Connect), a self-hosted platform that
  auto-processes camera-trap imagery, built with Smart Parks.
