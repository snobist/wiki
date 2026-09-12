# SEO Indexing System

Purpose: how StillCasting decides which pages Google should index, and the fixes applied.
Status: title gate shipped; person gate shipped. Last-verified: 2026-08-09 (live probes).

## Single source of truth
Indexability is a persisted boolean per entity, computed by a backend rule and read by
**both** the page template (`robots` meta) and the XML sitemap. No page is in the sitemap
that the template would `noindex`. Backend: `backend/src/stillcasting_api/services/seo_service.py`.

## Title indexability — `title_is_indexable` (SHIPPED)
Persisted `Title.indexable`; recomputed via `recompute_title_indexable` on cast/status change.
- **Phase 1:** index iff ≥1 deceased headline-cast member AND the title is released
  (`year <= current year`, or year unknown). Unreleased → never index.
- **Phase 2 (demand gate):** also index all-living, complete-cast titles from *past* years
  when `popularity >= POPULARITY_FLOOR (20.0)` and `verified >= MIN_VERIFIED (10)`.
  Floor = p90 of the 1,206-title all-living cohort, calibrated 2026-06-07 (~81 titles indexed;
  drop to 10 later → ~263). Current-year titles excluded (anticipation inflates popularity).
- Page gate: `titles/[slug]/page.tsx` → `...(!title.indexable ? { robots: { index:false, follow:true } } : {})`.
- History: Phase 2 originated as the "popularity exception" in [[proposals]] (indexing proposal).

## Person indexability — `person_is_indexable` (SHIPPED, fixes soft-404)
`Person.indexable` column pre-existed as an unwired stub; the session completed it.
- Rule (as proposed): index iff **biographical anchor** (DOB, death date/year, or Wikipedia bio)
  **AND** a synced non-empty filmography (`last_filmography_synced_at` set, `credits >= MIN_CREDITS`).
  The synced-filmography requirement also closes the `FilmographyAutoImport` empty-shell gap
  (client-side import means Googlebot otherwise saw an empty SSR page).
- `MIN_CREDITS` open decision (default 1; raise to 2–3 if thin pages persist).
- Verified live 2026-08-09: `shameer-khan`, `redin-kingsley`, `nidhi-arun`, `dimple-rose`,
  `sandy-j-christopher` → `noindex, follow` and removed from sitemap; `sylvester-stallone` → still `index`.

## Soft-404 incident (RESOLVED)
- Symptom: ~12,500 person pages reported **Soft 404** in GSC (HTTP 200 but ~empty: 125–161 words,
  no filmography, ~no bio fields). Cause: long-tail obscure persons with no data + no indexability gate.
- Fix: the person gate above (noindex + sitemap exclusion). GSC validation started; count fell 12,500 → 9,894.
- Expected motion: Soft 404 ↓, "Excluded by 'noindex'" ↑ (that row growing = fix completing, not a problem).

## Duplicate / canonical (NON-ISSUE)
- GSC "Duplicate, Google chose different canonical" (260) = **numeric-ID person URLs**
  (`/persons/29995` …). They now 308-redirect to the slug (`/persons/les-brandt`). Last crawled May,
  before the redirect existed → stale GSC data, self-resolving on re-crawl. Not a bug.
- Source of numeric URLs: internal links fall back to `person_id` when a person has no slug
  (`person_slug ?? person_id`). Shrinks as slugs backfill. Low-priority cleanup.

## robots.txt / crawler policy (STRONG)
- `Allow: /`, `Disallow: /api/`. Sitemap index with 5 children.
- Deliberately allows AI *citation* crawlers (ChatGPT-User, OAI-SearchBot, PerplexityBot, ClaudeBot)
  and blocks AI *training* crawlers (GPTBot, CCBot, anthropic-ai). `llms.txt` present and accurate.

## dev.stillcasting.app exposure (OPEN — action needed)
- `dev.stillcasting.app` is publicly reachable: HTTP 200, **0-byte body**, **no auth**, **no `X-Robots-Tag`**,
  empty robots.txt, and it **serves its own sitemap (200)**. Google indexed it → "Page indexed without content".
- Risk: the whole staging site can get indexed as duplicate content of prod. Because the GSC property is a
  **Domain property**, dev shows up in prod's reports — and dev deindexing would lower the aggregate impressions
  (candidate contributor to the mid-July drop — see [[gsc-performance]]).
- Fix (Caddy): HTTP Basic Auth on the dev block (best) + `header X-Robots-Tag "noindex, nofollow"` +
  stop serving the dev sitemap. Then GSC → Removals for the `dev.*` prefix.

## Live technical baseline (verified 2026-08-09)
Homepage + `/legends` + person/title/hub pages all HTTP 200, full server-rendered content, `index, follow`.
Sitemap total ~162,591 URLs (grew over the session). Security headers exemplary (CSP, HSTS preload,
X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy). Dynamic OG images.
Note: ISR cold-start can spike TTFB (~8.7s observed once; steady-state ~0.2s) → cache-warm follow-up.
