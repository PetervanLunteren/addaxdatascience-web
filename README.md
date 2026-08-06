# addaxdatascience-web

Source for hand-built pages on [addaxdatascience.com](https://addaxdatascience.com),
which runs WordPress. Each page is one self-contained HTML file — markup plus
an inline `<style>` block, no build step and no framework — pasted into a
WordPress custom HTML block as a generated snippet.

| path | what it is |
| --- | --- |
| `pages/addaxai/index.html` | the AddaxAI landing page (https://addaxdatascience.com/addaxai/) — edit this |
| `pages/addaxai-connect/index.html` | the AddaxAI Connect landing page (https://addaxdatascience.com/addaxai-connect/) |
| `pages/<name>/<name>.wordpress.html` | generated paste snippets — never edit by hand |
| `pages/<name>/urls.json` | local asset path → live URL rewrites used by the build |
| `pages/<name>/assets/` | images for that page, served to the live site via jsDelivr |
| `pages/addaxai-connect/mockup/` | source for the hero's phone mockup, with re-render instructions |
| `pages/_template/` | boilerplate for starting the next page |
| `shared/fonts/` | original woff2 files; pages embed them as base64 |
| `scripts/build.py` | source → snippet: extract, rewrite URLs, validate |
| `scripts/screenshot.py` | render a page to PNG with headless Chrome |
| `CONVENTIONS.md` | how a page is structured (scoping, fonts, images, markers) |
| `TODO.md` | backlog |

## Workflow

```sh
open pages/addaxai/index.html          # preview: renders standalone in a browser
python3 scripts/build.py               # regenerate the WordPress snippet(s)
python3 scripts/build.py --check       # verify committed snippets are current
python3 scripts/screenshot.py addaxai              # desktop PNG → preview/
python3 scripts/screenshot.py addaxai --width 390  # mobile PNG (iframe trick)
```

The source file uses relative `assets/...` image paths so the preview works
offline. `build.py` extracts everything between the `PASTE FROM HERE` /
`PASTE TO HERE` markers, swaps those paths for live URLs per `urls.json`, and
refuses to build if local paths or `TODO` markers would ship.

The mobile flag exists because headless Chrome clamps the viewport to a
500 px minimum; the script wraps the page in an iframe of the requested width
and screenshots that.

## How assets go live

Images are served by [jsDelivr](https://www.jsdelivr.com/) directly from this
repo on GitHub:

```
https://cdn.jsdelivr.net/gh/PetervanLunteren/addaxdatascience-web@main/pages/addaxai/assets/...
```

So publishing an image is: commit it, push to `main`, rebuild the snippet.
Nothing is uploaded to the WordPress media library. Two consequences:

- `@main` follows the branch with roughly a 12-hour CDN cache, so renaming or
  moving a committed asset breaks the live page until the re-built snippet is
  re-pasted. Prefer adding files over renaming published ones; pin a commit
  sha in `urls.json` if a URL must never move.
- The snippet on the live site references the paths as they were when it was
  pasted. After any repo restructuring, re-paste promptly.

## Publishing

1. Edit `pages/<name>/index.html`, preview it, run `python3 scripts/build.py`.
2. Commit and push, so jsDelivr can serve any new/changed assets.
3. Copy the full contents of `pages/<name>/<name>.wordpress.html`.
4. Paste into the single custom HTML block on a **draft** page, check it
   inside the real theme, then move it to the live page.
5. Purge the cache.

Pushing through the REST API instead of pasting needs an application password
(Users → Profile → Application Passwords) and a `POST` to
`/wp-json/wp/v2/pages/<id>`.

### Gotchas

- Some setups strip `<style>` from post content when the user lacks
  `unfiltered_html`. If that happens, move the CSS to a custom CSS plugin.
- Security plugins sometimes disable the REST API or block application
  passwords.
- Docs links point at `https://docs.addaxai.com/`, which changes if the docs
  move during the v7 repo migration. One find-and-replace covers all of them.

## Where the AddaxAI page content comes from

- Copy, screenshots and structure: the Docusaurus marketing homepage in the
  AddaxAI-WebUI repo (`docs/marketing-homepage/`), converted from React to
  plain HTML. Feature tiles, species models, user map, stats, forum, honesty
  box and partners were carried over from the old live page.
- The species-model list is generated from `models.json` in the AddaxAI-WebUI
  repo. Older duplicate model versions (Deepfaune v1.1–v1.3) are left out on
  purpose.
- The hero photo is a Grevy's zebra from the iWildCam 2022 dataset on LILA
  BC, © Wildlife Conservation Society, used under CDLA-Permissive-1.0; credit
  and links sit under the image. The detection box and label are drawn on
  with ImageMagick from the real detection stored in the app database, at the
  real coordinates and confidence (0.97).
- The embedded font is Lexend, the same face as the AddaxAI wordmark.
