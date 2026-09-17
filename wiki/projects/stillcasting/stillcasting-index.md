# stillcasting.app — project index

Cast-survivorship reference site (which movie/TV cast members are still alive). `Last-verified: 2026-08-28`.
Migrated 2026-09-12 from `~/Documents/ClaudeProjects/stillcasting-wiki` (frozen copy in `raw/project-wikis/`).

**Stack**: Next.js App Router (ISR) frontend, Python backend, PostgreSQL, Redis; data from TMDb + Wikidata/Wikipedia,
updated daily; Caddy/nginx; Docker on an OCI box. ~24.7k title pages + ~100k+ person pages (~162k sitemap URLs).
Built in ~3 weeks, spec-driven / vertical slices, with Claude Code. GSC domain property `sc-domain:stillcasting.app`.

**Repo**: `git@github.com:snobist/stillcasting.app.git` (private, SSH; see [[access]]). Local clone on the new Mac:
`~/Documents/Private_Projects/stillcasting`, branch `develop` (cloned 2026-09-14; HEAD f5a0f60 = main). Top level:
`backend/`, `frontend/`, `worker/`, `nginx/`, `Caddyfile`, `docker-compose.yml`, `docker-compose.staging.yml`, `Makefile`, `docs/`.

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

## Incident 2026-09-17 — /data full again (see log)
- Media 51 GB = TMDb JPEGs (posters w500 19 GB / w300 8 GB, profiles w342 8.6 GB / w185 3 GB, wiki portraits 5.4 GB); WebP display set 0.25 GB.
- Log rotation now on (prod override + compose files on develop). Staging stack is DOWN; deploy is manual (Actions → "Deploy → Staging").
- Decision pending: serve TMDb CDN instead of local JPEGs (frees ~46 GB, frontend already falls back) / expand volume.

## Audit 2026-09-14 (Claude Code, with server access)
- Full findings + fix status: [[stillcasting-bug-audit-2026-09-14]]. Fixes merged to `develop` 2026-09-14 (staging); prod not tagged;
  prod data cleanup script `bin/stillcasting-revert-false-deaths.sh` awaiting Alex. Workers confirmed RUNNING; `/data` at 92 %. Jeremy Thomas duplicate = false death
  from the Wikipedia deaths checker (name-only match, DOB-less shells skip the birth-year gate); recurring (Terence Donovan 07-19, ~10 more).

## External check 2026-09-14 (from Cowork; no server access)
- Site up; homepage stats: 283,564 titles / 1,154,852 cast / 72% alive / 87,090 deceased.
- Data is FRESH — "Remembered This Week" has deaths dated up to 2026-09-13 → workers are running again (contradicts
  the 2026-08-28 "workers stopped" state above; server-side confirmation still needed: /data headroom, worker status).
- robots.txt: Allow / (blocks /api/); citation bots allowed, training/SEO bots blocked; sitemaps at `/sitemap/0..4.xml`
  (`/sitemap.xml` and `/sitemap-0.xml` are NOT valid paths). `/sitemap/0.xml` = 28 static URLs, latest lastmod 2026-06-06.
- **Data-quality finding**: `/persons/jeremy-thomas` (1 credit, "Not Quite Hollywood" 2008, no bio, death 2026-09-12)
  vs `/persons/jeremy-thomas-2` (the producer, b. 1949-07-26, death 2026-09-11 Oxfordshire). Looks like a duplicate
  TMDb entity fused with the same death via name match, with a date off by one day — candidate for the record-linkage /
  false-death checks in [[pipeline-science]]. Both appear on /died-this-week.
- `dev.stillcasting.app` still resolves and serves something (binary/non-HTML response to the fetcher) — lock-down
  item remains open.
- Network note: stillcasting.app is blocked by the Cowork proxy (curl from both cloud and Mac VM → 403); only the
  WebFetch tool reaches it. SSH to the OCI box is impossible from Cowork — use Claude Code / Terminal on the Mac.
