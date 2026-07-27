# addaxdatascience-web

Source for hand-built pages on [addaxdatascience.com](https://addaxdatascience.com),
which runs WordPress. Each page is one self-contained HTML file: markup plus an
inline `<style>` block, no build step and no framework.

| file | what it is |
| --- | --- |
| `addaxai-bold.html` | current candidate for https://addaxdatascience.com/addaxai/ |
| `addaxai-soft.html` | earlier pass, borderless and airy, system fonts |
| `addaxai.html` | first conversion, bordered cards, kept for comparison |

All three have identical content and section order. They differ only in visual
treatment. Once one is picked, delete the other two.

## How a page is built

Everything is scoped under a single wrapper class (`.aai-lp` for the AddaxAI
page) so the WordPress theme cannot style the page and the page cannot style the
rest of the site. The wrapper also carries:

- the colour palette as CSS custom properties, so the brand teal is set once
- a font stack, since the theme's font would otherwise apply
- defensive resets for headings, links, lists and images
- a full-bleed rule (`width: 100vw`) that breaks out of a theme container that
  caps content width. Remove it if the page template is already full width.

## Fonts

`addaxai-bold.html` embeds two webfonts as base64 data URIs inside the CSS:
Inter for body text and Space Grotesk for headings, latin subsets only,
47 KB and 21 KB raw. The originals are in `assets/fonts/` for reference.

They are inlined rather than linked on purpose:

- WordPress blocks `.woff2` uploads to the media library by default, so a
  normal upload would fail without a MIME filter or a plugin.
- A Google Fonts `<link>` would put a third-party request on a page whose main
  claim is that your photos never leave your machine, and it drags in the
  cookie consent question for an EU company.

The cost is about 92 KB of base64 in the page source. To drop back to system
fonts, delete both `@font-face` blocks and the two `--aai-font` variables.

## Previewing

Open the file in a browser. It renders standalone.

To render it to an image:

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --hide-scrollbars --allow-file-access-from-files \
  --screenshot=out.png --window-size=1440,4600 \
  "file://$PWD/addaxai.html"
```

Headless Chrome clamps the viewport to a 500 px minimum, so a narrow
`--window-size` renders at 500 px and crops. To check the mobile layout, load
the page in an iframe of the width you want and screenshot that instead.

## Publishing

1. Upload the four files in `assets/` to the media library and swap the paths.
   They are listed in the comment at the top of the file, along with the two
   `TODO` markers that still need filling in (donate link, CamTrap Pro link).
2. Copy everything between the `PASTE FROM HERE` and `PASTE TO HERE` markers.
3. Paste into a single custom HTML block on a **draft** page, check it inside
   the real theme, then move it to the live page.
4. Purge the cache.

Pushing through the REST API instead of pasting needs an application password
(Users > Profile > Application Passwords) and a `POST` to
`/wp-json/wp/v2/pages/<id>`.

### Gotchas

- Some setups strip `<style>` from post content when the user lacks
  `unfiltered_html`. If that happens, move the CSS to a custom CSS plugin.
- Security plugins sometimes disable the REST API or block application
  passwords.
- Docs links point at `petervanlunteren.github.io/AddaxAI-WebUI/`, which changes
  if the docs move during the v7 repo migration. One find and replace covers all
  of them.

## Where the content comes from

- Copy, screenshots and structure: the Docusaurus marketing homepage.
- Feature tiles, species models, user map, stats, forum, honesty box and
  partners: carried over from the old live page, which is being replaced.
- The species model list is generated from `models.json` in the AddaxAI-WebUI
  repo, not from the old page, which was out of date. Older duplicate model
  versions (Deepfaune v1.1 to v1.3) are left out on purpose.
- The hero photo is a Grevy's zebra from the iWildCam 2022 dataset on LILA BC,
  © Wildlife Conservation Society, used under CDLA-Permissive-1.0. The credit
  and both links sit under the image in the hero. The detection box and its
  label are drawn on with ImageMagick from the real detection stored in the app
  database, at the real coordinates and confidence (0.97).

## Origin

`addaxai.html` started as the Docusaurus marketing homepage in the AddaxAI-WebUI
repo (`docs/marketing-homepage/`), converted from React and CSS modules to plain
HTML. That copy is kept there as a reference and is no longer the live page.
