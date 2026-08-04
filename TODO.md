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
- [x] Update the screenshot for "Count by event, not by photo".
      `docs.addaxai.com/img/counts-event.webp` was indeed the film strip
      shot; cropped to the modal interior and saved as
      `assets/screenshots/countsEvent.webp`. The old grid shot
      (`counts.webp`) is removed; the docs site still hosts a copy as
      `project-counts.webp`.
- [x] Add a section with external AddaxAI references. The forum panel is now
      a three-card "Docs, community and code" resources section linking the
      docs, the forum invite, and the GitHub repo.
- [x] Deleted the unused `inter-latin-var.woff2` and
      `space-grotesk-latin-var.woff2` from `shared/fonts/` (leftovers from an
      earlier design pass; git history keeps them). Only the embedded Lexend
      remains.

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
