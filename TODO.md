# Backlog

- [x] Make this repo a proper repo for Claude Code sessions: CLAUDE.md,
      README, CONVENTIONS.md, a build script for the WordPress snippet, and a
      `pages/<name>/` structure plus `pages/_template/` so future pages
      (e.g. AddaxAI Connect) work the same way.
- [ ] **Re-paste the snippet after the restructure lands on `main`.** Assets
      moved from `assets/` to `pages/addaxai/assets/`, so the jsDelivr URLs
      in the currently live snippet will 404 once the CDN cache refreshes
      (~12 h after push). Rebuilt snippet is ready in
      `pages/addaxai/addaxai.wordpress.html`.
- [ ] Update the screenshot for "Count by event, not by photo". Current
      image is the grid (`counts.webp`); better would be the modal with the
      film strip below it. `https://docs.addaxai.com/img/counts-event.webp`
      may be that shot — check it, otherwise make a new one.
- [ ] Consider a section with external AddaxAI references: the docs, the
      forum, the GitHub repo — what else?
- [ ] Decide whether the unused `shared/fonts/inter-latin-var.woff2` and
      `space-grotesk-latin-var.woff2` (left over from an earlier design pass;
      the page now embeds Lexend) should be deleted.

## Done / superseded

- ~~Replace the GitHub user-attachment image URLs with the downsampled
  `https://docs.addaxai.com/img/<name>.webp` versions.~~ Superseded: all
  images now live in the repo as WebP under `pages/addaxai/assets/` and are
  served via jsDelivr (see README). The docs site still hosts downsampled
  copies (app-home, project-dashboard, project-counts, counts-event,
  insights-map, insights-timeline, insights-confusion-matrix,
  folder-run-1-setup, …) if an alternative host is ever needed.
- ~~Fill in the donate link and the CamTrap Pro link.~~ Done on the page
  (Stripe buy button is live; the integration links all have real hrefs).
