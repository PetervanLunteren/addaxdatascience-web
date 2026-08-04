# Conventions

How a page in this repo is built. The AddaxAI page (`pages/addaxai/`) is the
reference implementation; `pages/_template/` is the starting point for new
pages.

## One page, one directory, one file

Each page lives in `pages/<name>/` and is a single `index.html`: markup plus
one inline `<style>` block. No build step, no framework, no JavaScript except
unavoidable third-party embeds (e.g. the Stripe buy button). The file renders
standalone in a browser for previewing; WordPress supplies its own `<head>`,
header and footer around the pasted snippet.

`scripts/build.py` generates `<name>.wordpress.html` from it — the snippet
pasted into a WordPress custom HTML block. The generated file is committed so
the exact markup that went live is in history, but it is never edited by hand.

## Paste markers

The publishable region sits between two comment markers:

```html
<!-- ================= PASTE FROM HERE ================= -->
...one <style> block, then one wrapper <div>...
<!-- ================= PASTE TO HERE ================= -->
```

Everything outside them is local-preview scaffolding (`<head>`, a body-margin
reset). Each marker must appear exactly once; build.py enforces this.

## CSS scoping

Every page has a short prefix (AddaxAI: `aai`) used three ways:

- a wrapper class on the outermost div: `.aai-lp`
- a class prefix on every element: `.aai-hero`, `.aai-section`, `.aai-btnSolid`
- a custom-property prefix: `--aai-primary`, `--aai-shadow-sm`

Every selector starts with the wrapper class (`.aai-lp .aai-hero { ... }`), so
the WordPress theme cannot style the page and the page cannot style the rest
of the site. The wrapper also carries defensive resets (headings, links,
lists, images) and a full-bleed rule (`width: 100vw; margin-left: calc(50% -
50vw)`) that breaks out of a theme container capping content width — delete
that rule if the page template is already full width.

Colours, fonts and shadows are defined once as custom properties on the
wrapper; rules reference the variables.

## Fonts

Pages embed Lexend (the AddaxAI brand face, the wordmark's font) as a base64
data URI in an `@font-face` block, latin subset only, ~39 KB raw / ~53 KB
encoded. The original woff2 lives in `shared/fonts/`.

Embedded rather than linked on purpose:

- WordPress blocks `.woff2` uploads to the media library by default.
- A Google Fonts `<link>` would put a third-party request on a page whose
  main claim is that your photos never leave your machine, and it drags in
  the cookie-consent question for an EU company.

To fall back to system fonts, delete the `@font-face` block and the two
`--<pfx>-font` variables.

## Images

- Format: WebP, sized for the web; keep a `_thumb` variant when a small
  version appears in a grid. Originals (e.g. `hero-detection.jpg`) may sit
  next to the WebP for reference.
- Live in `pages/<name>/assets/`, referenced with relative `assets/...`
  paths so the standalone preview works offline.
- `urls.json` maps local paths to live URLs at build time — normally a single
  prefix rule pointing at jsDelivr, which serves files straight from this
  repo on GitHub (`cdn.jsdelivr.net/gh/PetervanLunteren/addaxdatascience-web
  @main/pages/<name>/assets/...`). Publishing an image = commit, push,
  rebuild the snippet. `@main` follows the branch with ~12 h cache lag; don't
  rename or move published assets casually, and pin a commit sha in the URL
  if one must never move.
- Below-the-fold images get `loading="lazy"`; decorative images get
  `alt=""` and icons `aria-hidden="true"`.

## Markup details

- External links: `target="_blank" rel="noopener"`.
- Docs links use `https://docs.addaxai.com/` as the base — keep them
  consistent so one find-and-replace covers a docs move.
- Small inline SVGs and emoji (e.g. the model-zoo flags) are embedded as
  base64 SVG background images on classed spans, not as emoji characters, so
  they render identically on every platform.
- Keep the snippet self-contained: no external CSS, no external JS beyond
  vetted embeds, no fetches. The ~150 KB snippet size (mostly the font) is
  accepted cost.

## Starting a new page

1. Copy `pages/_template/` to `pages/<name>/`.
2. Pick a prefix and find-and-replace `xxx` in `index.html` (e.g. `con` for
   AddaxAI Connect). Set the palette variables for the page's branding.
3. Update the path in `urls.json` (replace `NAME`).
4. Build sections inside the wrapper div, images into `assets/`.
5. `python3 scripts/build.py <name>`, then follow the publishing steps in
   README.md.

**Repo conventions:**
1. **Crash early and loudly** - Fail hard in development so bugs cannot hide. Never allow silent failures.
2. **Explicit configuration** - No defaults. If something is missing, stop and surface it immediately.
3. **Type hints everywhere** - Make expectations clear and support safe refactoring.
4. **Short and clear documentation** - Keep explanations concise without losing clarity.
5. **Open source friendly** - Never commit secrets or anything that should not be public.
7. **Prefer simple solutions** - Use straightforward approaches that follow the conventions. Avoid cleverness when simplicity works.
8. **Follow the established conventions** - Keep structure predictable so the codebase stays readable and easy to maintain. 
9. **No quick fixes** - Fix issues in a way that holds for all future deployments, not only the current device.
10. **GitHub** - Always commit manually. Never commit automatically. 
11. **Clean repo** - Value simplicity and cleanliness. No redundant MD files. 
12. **No Title Case** - Use natural English capitalisation. That means only capitalising the first word of sentences and proper nouns (like "Peter van Lunteren", "Utrecht", "MegaDetector", "SpeciesNet", "Today, I was walking in the park.",  "Things I love about Amsterdam.", "Cities visited"). Do capitalize the first letter of headers (e.g., "Detections per 100 trap-days", "Species selection", "Observations"). 
13. **Use built in features if possible** - Always check whether the required functionality is already available through built-in features. If so, prefer that over writing custom code. If a built-in option is close but does not fully meet the requirement, stop and discuss the pros and cons before proceeding.
14. **No em dashes** - Never use em dashes (—) or double hyphens (--) in text. Use commas, colons, semicolons, or separate sentences instead.
15. **Write like a person, not an LLM** - Avoid filler phrases like "it's important to note that", "let's", "dive into", "in order to", "leverage", "streamline", "it should be noted", or "please note that". Just say the thing directly. Keep text natural and to the point.
* Follow the KISS principle. Keep things as simple as possible.                                                                       
* Follow the DRY principle (Don't Repeat Yourself). Avoid duplication and maintain a single source of truth.                          
* Follow the YAGNI principle (You Aren't Gonna Need It). Do not build functionality until it is actually needed. 
* Use shared helpers if possible. I do not want drift and maintain different code sets. Also, shared halpers make sure the UI looks and feels the same, and possible bugs are fixed sooner. 
* ALways ask before opening a new branch. Prefer to work on main, except for very large tasks or rewrites. If preferable to have a separate branch, ask permission first. 



Return all your explanations, answers, reports, and investigations with a few sentence summary in plain English at the bottom of your response. Keep it simple. 



## Writing
* **Short and clear documentation** - Keep explanations concise without losing clarity.
* **No Title Case** - Use natural English capitalisation. That means only capitalising the first word of sentences and proper nouns (like "Peter van Lunteren", "Utrecht", "MegaDetector", "SpeciesNet", "Today, I was walking in the park.",  "Things I love about Amsterdam.", "Cities visited"). Do capitalize the first letter of headers (e.g., "Detections per 100 trap-days", "Species selection", "Observations"). 
* **No em dashes** - Never use em dashes (—) or double hyphens (--) in text. Use commas, colons, semicolons, or separate sentences instead.
* **Write like a person, not an LLM** - Avoid filler phrases like "it's important to note that", "let's", "dive into", "in order to", "leverage", "streamline", "it should be noted", or "please note that". Just say the thing directly. Keep text natural and to the point.
* **Write like a non-English person** - Use simple, direct sentence structures. Avoid complex grammar, idioms, or overly polished phrasing. It should sound natural but slightly imperfect, like a fluent non-native speaker.
* **Direct and honest communication** - Say what you mean, without softening or filler. If something is a bad idea, say so and explain why in a few precise sentences. No sugar coating. 
* **Short and clear documentation** - Keep explanations concise without losing clarity.
* **Focus on the user** - Write from the user's perspective and focus on their goal, not the system.
* **Lead with the answer** - Put the most important information first.
* **Offer a solution** - Don't just describe a problem, explain how to fix it.
* **Use plain language** - Prefer simple words over technical or formal language.
* **Speak simply** - Aim for language that a typical 11 to 12 year old can understand.
* **Keep sentences short** - Prefer 5 to 15 words per sentence when practical.
* **One idea per sentence** - Split complex thoughts into multiple sentences.
* **Short beats clever** - Clarity is more important than sounding smart.
* **No Title Case** - Use natural English capitalisation. Capitalise only the first word of sentences, headers, and proper nouns.
* **No em dashes** - Never use em dashes (—) or double hyphens (--). Use commas, colons, semicolons, or separate sentences instead.
* **Write like a person, not an LLM** - Avoid filler, buzzwords, and corporate language.
* **Write like a fluent non-native English speaker** - Use simple, direct sentence structures and avoid unnecessary complexity.
* **Direct and honest communication** - Say what you mean. Do not sugar coat.
* **Sound conversational** - Write as if you are explaining something to a colleague.
* **Use contractions naturally** - Use "don't", "can't", and "won't" when they sound natural.
* **Avoid marketing language** - Do not use words like "powerful", "seamless", "robust", or "cutting-edge".
* **Avoid AI phrases** - Never write phrases like "It's important to note", "Let's dive in", or "Please note".
* **Be consistent** - Follow established terminology and writing patterns.
* **One concept, one name** - Use the same term everywhere for the same thing.
* **One source of truth** - Do not describe the same concept differently in different places.
* **Write globally** - Avoid culture-specific references, slang, and local expressions.
* **Make translation easy** - Avoid ambiguous wording, idioms, and unnecessary pronouns.
* **Avoid gerunds when possible** - Prefer simple verbs over verb-noun constructions.
* **Include everyone** - Use language that works across cultures, ages, and backgrounds.
* **Do not rely on visual cues** - Never refer only to colour, position, or appearance.
* **Be positive** - Tell users what they can do, not only what they cannot do.
* **Describe limits clearly** - State constraints without sounding negative.
* **Avoid system-centric language** - Users care about outcomes, not implementation details.
* **Do not expose internal details** - Explain only what users need to know.
* **Remove repetition** - Say things once unless repetition improves clarity.
* **Do not repeat product names unnecessarily** - Readers already know where they are.
* **Respect the reader's time** - Remove anything that does not help the reader.
* **Examples beat explanations** - Show an example when it explains faster.
* **Accuracy beats completeness** - Leave something out rather than guessing.
* **Be explicit when uncertain** - Clearly state assumptions, risks, or unknowns.
* **Avoid unnecessary adjectives** - Most adjectives add noise, not value.
* **Prefer active voice** - "You can export data" is better than "Data can be exported".
* **Use specific language** - Replace vague words with concrete terms.
* **Avoid filler words** - Remove words that do not change meaning.
* **Check for ambiguity** - Make sure every sentence has only one reasonable interpretation.
* **Check for scannability** - Use headings, lists, and structure to improve readability.
* **Assume intelligent readers** - Explain unfamiliar concepts without being patronising.
* **Do not over-explain obvious things** - Skip information the audience already knows.
* **Every word must earn its place** - If removing a word does not change meaning, remove it.
* **Read it out loud** - If it sounds unnatural when spoken, rewrite it.
* **Write first, edit second** - Get the idea down, then simplify aggressively.
* **Review for brevity** - After writing, make it shorter.
* **Review for clarity** - After shortening, make sure meaning is still clear.
* **Final test** - Ask: Can this be shorter, simpler, clearer, or more useful?