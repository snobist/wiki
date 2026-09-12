# stillcasting.app — project index

Cast-survivorship reference site (which movie/TV cast members are still alive). `Last-verified: 2026-08-28`.
Migrated 2026-09-12 from `~/Documents/ClaudeProjects/stillcasting-wiki` (frozen copy in `raw/project-wikis/`).

**Stack**: Next.js App Router (ISR) frontend, Python backend, PostgreSQL, Redis; data from TMDb + Wikidata/Wikipedia,
updated daily; Caddy/nginx; Docker on an OCI box. ~24.7k title pages + ~100k+ person pages (~162k sitemap URLs).
Built in ~3 weeks, spec-driven / vertical slices, with Claude Code. GSC domain property `sc-domain:stillcasting.app`.

## Pages
- [[seo-indexing]] — indexability gates, soft-404 fix, sitemap/robots, dev-subdomain exposure, canonicals.
- [[gsc-performance]] — Search Console metrics timeline, mid-July impression drop, traffic/ad-revenue model.
- [[proposals]] — every change proposal with status.
- [[pipeline-science]] — actuarial survival modelling, Bayesian death fusion, record linkage, false-death risk.

## State as of 2026-08-28 (from log)
- Shipped: title + person indexability gates, status-aware person headline.
- Approved not shipped: title-page "How Many … Still Alive?" headline (blocked on mockup).
- **Infra**: `/data` (74 GB) hit 100% twice (08-26, 08-28) → Postgres death-spiral. Workers STOPPED; data updates
  paused. Pending decisions: expand OCI volume (real fix), reclaim ~9 GB (staging media + chromium image), Docker log
  rotation, whether MAS staging needs this box. Do not resume workers without headroom.
- Deploy pipeline was broken (blocks scanner future-date guard).
- Open: GSC API keys; lock down `dev.stillcasting.app`; backlinks; Marjane Satrapi false-death check; `MIN_CREDITS`.

Full history: `raw/project-wikis/stillcasting-wiki/log.md`. Related: [[environment]], [[access]].
