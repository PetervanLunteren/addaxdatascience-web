# Backlog

- [ ] Publish the AddaxAI Connect page: commit and push, create the draft
      WordPress page (slug `addaxai-connect`, same full-width template as the
      AddaxAI page), paste `pages/addaxai-connect/addaxai-connect.wordpress.html`,
      check, publish, purge cache. Then phase 2 placements: cross-link block
      on the AddaxAI page, nav dropdown under ADDAXAI, homepage software
      section, footer link to the new page.
- [ ] Maintenance: the Connect page's deploy command, server spec ($48/mo
      example) and camera models mirror connect.addaxai.com/deployment/ and
      /camera-requirements/. If those docs change, update the "what you'll
      need", costs and FAQ sections to match.
- [ ] Optional: replace the Connect app screenshots (map, cameras, images,
      settings, users) with fresh captures from demo.addaxai.com. The current
      ones were lifted from the early-warning-systems page and match the demo,
      but a new capture would let us pick the framing.
- [ ] Unrelated, spotted while reviewing the live site: the `cdla.io` link on
      the AddaxAI page now redirects to `cdla.dev` (the Connect page already
      uses the new domain); the leftover theme demo posts and `/sandbox/` are
      live and in the sitemap; the homepage and service pages show flat grey
      hero bands where an image may be missing.

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
