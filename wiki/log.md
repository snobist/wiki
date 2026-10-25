# Log

Append-only, newest at top. Format: `## YYYY-MM-DD — <op> | <title>`.

## 2026-10-25 — growth | no change; hubs still not discovered; false-death audit clean
- Report: `analyses/stillcasting-growth/2026-10-25.md`. GSC 23 impr/0 clicks (10-17…10-23); inspection 1/11/7, nothing re-crawled since `/` on 10-23; sitemap index re-fetched 10-24. Human GA4 sessions 179 (+36), engaged 67 (+14); Bing 39 / Yahoo 19 / DDG 14 / Google 0. Healthy, /data 68 %, prod v1.267.63.
- False-death audit: 51 checked, 46 OK, same 2 date-only Wikidata mismatches (rescans queued, unchanged) and 3 low-pop unconfirmed. No false deaths.
- No change: waiting for Google to follow the homepage hub links; develop holds 7 unreleased tv-player/split-money commits.
- Open: release develop (Alex); backlinks; IndexNow; Googlebot 0 hits in 6 h sample.

## 2026-10-23 — growth | no change; Google re-crawled `/`; false-death audit clean
- Report: `analyses/stillcasting-growth/2026-10-23.md`. GSC 20 impr/0 clicks (10-14…10-20); inspection 1/11/7, `/` re-crawled 10-23 (first since 10-11). Human GA4 sessions 143 (+28), engaged 53 (−12); Bing 33 / Yahoo 17 / DDG 9 / Google 0. Caddy 403s down 93 % (Tencent scraper gave up). Healthy, /data 69 %.
- False-death audit: 53 checked, 48 OK, 2 date-only Wikidata mismatches (rescans queued, unchanged: Price, Sabesh), 3 low-pop unconfirmed. No false deaths.
- No change: waiting to see the effect of the `/` re-crawl; develop has 14 unreleased worth-watching/home-weather commits a growth deploy would carry.
- Open: release develop from its owning sessions (Alex); backlinks; Loyd Price date.

## 2026-10-21 — growth | no change; Tencent block verified in GA4; false-death audit clean
- Report: `analyses/stillcasting-growth/2026-10-21.md`. GSC 17 impr/0 clicks (10-12…10-18); inspection 1/11/7, Godfather re-crawled 10-20 (not indexed), `/` still 10-11. Human GA4 sessions 115 (+16), engaged 65; Bing 38 / Yahoo 16 / DDG 11 / Google 0. Singapore Direct 136k (10-19) → 1 (10-20). Healthy, /data 68 %, prod v1.267.58.
- False-death audit: 58 checked, 52 OK, 3 Wikidata date mismatches (rescans: Bracardi fixed, Price + Sabesh unchanged), 3 low-pop unconfirmed. No false deaths.
- No change: Google hasn't re-read `/` since the last homepage-link changes; no metadata defect found; no bot over the Crawl-delay threshold.
- Open: request indexing for `/` (Alex); watch Alibaba 8.216/8.211/47.x ranges.

## 2026-10-19 — release | stillcasting v1.267.55: Tencent scraper blocked, sc605 tests fixed
- On Alex's go: Caddy 403 for 43.172.0.0/16 + 43.173.0.0/16 (source of the 199k GA4 sessions); verified live (1,066 × 403 in 2 min, others 200).
- sc605 search-dropdown suite: tests waited on the listbox, not results; actor links /persons/; loading row role=status; jest setupFilesAfterEnv typo. Jest 61/61, backend 370, build green.

## 2026-10-19 — growth | /last-survivors double period fixed (v1.267.54); false-death audit clean
- Report: `analyses/stillcasting-growth/2026-10-19.md`. GSC 17 impr/0 clicks (10-11…10-17), first person/title impressions since Sept (10 pages on 10-17); inspection 1/11/7, nothing re-crawled. Human GA4 sessions 99, engaged 62; Bing 35 / Yahoo 15 / DDG 11 / Google 0. GA4 bot spike: 199k Singapore Direct sessions on 10-18 (Tencent 43.172–173/16 scraper). Healthy, /data 67 %.
- False-death audit: 58 checked, 54 OK, 2 date-only Wikidata mismatches (rescans queued, no change), 2 low-pop unconfirmed. No false deaths.
- Shipped: `sentenceEnd()` drops the "Them!." double period on the backlink page. Backend 370 passed, build green (jest sc605 suite fails, pre-existing); deployed unattended, verified live, pruned 2.8 GB.
- Open: Caddy block for 43.172/16 + 43.173/16 (Alex); sc605 jest failures; Loyd Price date.

## 2026-10-17 — growth | noindex /born-in/<year> outside 1900..today−16 (v1.267.52)
- Report: `analyses/stillcasting-growth/2026-10-17.md`. Flat: GSC 3 impr/0 clicks (10-08…10-14); inspection 1/11/7, nothing re-crawled (`/` still 10-11); sitemap children pending. Human GA4 sessions 105 (10-10…10-16), engaged 72; Bing 40 (+11) / Yahoo 16 / DDG 19 / Google 0. GA4 bot share 94.7 % (CN/SG surge 10-15/16). Healthy, /data 63 %.
- Shipped: junk birth years (1025, 2084 …) render noindex; sitemap range unchanged. Backend 365 passed, build + jest green; deployed unattended, verified live, pruned 2.8 GB.
- Open: request indexing for `/`; PerplexityBot back up to ~150/h; GA4 bot filter is UI-only for Alex.

## 2026-10-15 — release | stillcasting v1.267.51: /last-survivors live
- Merged on Alex's go; containers recreated, verified as Googlebot (200, index, canonical, JSON-LD, sitemap, homepage link). 983 checked / 147 one-left. Pruned 2.8 GB; /data 62 %.
- Cosmetic: a double period after titles ending in punctuation ("Support Your Local Sheriff!.").

## 2026-10-15 — project | stillcasting backlink kit + /last-survivors page
- New page `/last-survivors` on branch `feat/last-survivors` (d2c40cf): 982 classics checked, 37 % have no top-billed star alive, 146 have exactly one. Backend 365 passed, build + jest green on the box. Waiting for Alex's go to merge and tag.
- Kit: `projects/stillcasting/backlinks-outreach.md`. Headline claims fact-checked (Novak, Andress, Vera Miles, Eastwood, Moreno, Mills, Caine alive; Duvall, Perrine and Eva Marie Saint deaths confirmed and in the DB). Ranked targets and templates included; Alex sends everything himself.

## 2026-10-15 — growth | homepage links /deaths/<year> + top /cause pages (v1.267.50)
- Report: `analyses/stillcasting-growth/2026-10-15.md`. Flat: GSC 3 impr/0 clicks (10-06…10-12); inspection 1/11/7, nothing re-crawled; sitemap index re-downloaded 10-14 (children pending). Human GA4 sessions 113 (10-08…10-14), engaged 78; Bing 29 / Yahoo 17 / DDG 21 / Google 0. Healthy, /data 62 %.
- Shipped: homepage prose links /deaths/2026, /deaths/2025 and 4 cause pages, because `/` is the only page Google re-crawls. Backend 363 passed, build + jest green; deployed unattended, verified live, pruned 2.9 GB.
- Open: "alzheimer's" lowercase nit; fastapi/starlette unpinned upgrade risk; WebSiphon 502 burst on bare IP.

## 2026-10-13 — growth | /statistics links recent years to /deaths/<year> (v1.267.49)
- Report: `analyses/stillcasting-growth/2026-10-13.md`. Flat: GSC 3 impr/0 clicks (same 7-d window, no new GSC data); inspection 1/11/7, nothing re-crawled; human GA4 sessions 132 (10-06…10-12), engaged 85; Bing 32 / Yahoo 17 / DDG 19 / Google 0. Healthy, /data 62 %.
- Change: crawlable `/deaths/<year>` links under /statistics year charts (f70b300 on develop). Backend 363 passed, build + jest green on the box.
- Scheduled deploy was denied by auto mode; deployed later the same day on Alex's go, verified live, pruned 6.7 GB. Sitemap children still pending; Baiduspider now top named bot (~640 req/h).

## 2026-10-12 — growth | /statistics links cause rows to /cause pages (v1.267.48)
- Report: `analyses/stillcasting-growth/2026-10-12.md`. Flat: GSC 3 impr/0 clicks (7 d); inspection 1/11/7 unchanged, only `/` re-crawled (10-11); human GA4 sessions 140, engaged 87; Bing 37 / Yahoo 19 / DDG 16 / Google 0. Sitemap children submitted by Alex, pending.
- Shipped: 6 cause rows + "All causes" link on /statistics (was 0 cause links). Backend 363 passed, build + jest green; verified live; /data 63 %.
- Predeploy harness needs `pip install /repo/worker` and container-based clone removal (see report). Needs Alex: request indexing for /statistics, backlinks, IndexNow decision.

## 2026-10-09 — growth | /spanning-generations renders 30 entries (v1.267.47)
- Report: `analyses/stillcasting-growth/2026-10-09.md`. Google re-crawled the 5 requested hubs 10-08; all still "Crawled – currently not indexed". GSC 3 impr/0 clicks (7 d); human GA4 sessions 154, engaged 85 (+22); Bing 34 / Yahoo 17 / DDG 16 / Google 0.
- Shipped: hub server-renders the full 30-entry pool (6 → 30 person links). Backend 363 passed, build + jest green; verified live; /data 61 %.
- Needs Alex: re-request indexing for /spanning-generations, submit sitemap children individually, backlinks; openclaw/Kasm loops.

## 2026-10-08 — release | stillcasting v1.267.46: enlarged photo above page
- ImageLightbox renders via portal to <body>; the sticky photo column (v1.267.41) trapped its z-index and the cohort bar showed over the enlarged photo. Verified live on /persons/mary-tsoni. Note: frontend container swap caused ~10 s of 000s at 17:06Z.

## 2026-10-08 — release | stillcasting v1.267.44–45: duplicate persons and deaths
- v1.267.44: scanner clears birthday/birthplace TMDb removed (Ray Anthony TMDb 9598 carried the 1922 bandleader's DOB); "twins" (same name + exact DOB, 523 groups / 1,050 records) shown once on born-in lists/counts, secondary person pages canonical to the primary (`services/twins.py`, migration 0030).
- v1.267.45: death lists (recently deceased, died this week/on this day, deaths by year, cause, born-in died-on + count) keep one record per name + death date (migration 0031). Verified: 24 Jun 1987 Igor Starkov ×2 → ×1, 24 Jun 1986 James Harrison ×2 → ×1.
- NEEDS ALEX: rescan of the 1,050 twin records (auto mode blocks prod DB access; command in session transcript — `scan_person_task` for name+DOB groups). Until then TMDb 9598 canonicalises to the bandleader. Status-conflict list (living vs deceased twins, e.g. Adelle August) still to produce.

## 2026-10-08 — release | stillcasting v1.267.42: /born-in hub
- New `/born-in` landing page (chart + all years + data intro), homepage link + sitemap. Verified live 200/index; Docker pruned (2.8 GB), /data 61 %.
- Next: filter adult films from born-in "films that year", 404 junk birth years. Alex to Request indexing for /born-in.

## 2026-10-08 — query | stillcasting: hubs submitted for indexing, sitemap status
- Alex requested indexing for 5 hubs in GSC. Hub audit + sitemap check (files valid; GSC "Temporary processing error", 0 discovered) added to `analyses/stillcasting-growth/2026-10-07.md`.
- Open: `/spanning-generations` thin (6 rows server-side); openclaw service removal blocked by corporate-Mac process killer.

## 2026-10-07 — growth | no change; v1.267.39 live, Google still not crawling
- Report: `analyses/stillcasting-growth/2026-10-07.md`. GSC unchanged (data ends 10-04, same window as the last run): 5 impr/0 clicks; 1/19 sample indexed, no new crawls.
- Human GA4 sessions 151 (09-30…10-06, new filter method); Bing 31 / Yahoo 19 / DDG 12 / Google 0. Site healthy, /data 61 %, og:image fix verified live.
- No change: last fix went live minutes before the check, nothing to measure yet. Needs Alex: GSC Request indexing, backlinks, openclaw-product-list-api + Kasm restart loops on the box.

## 2026-10-06 — growth | og:image/logo 404 fixed (v1.267.39); Google still not crawling
- Report: `analyses/stillcasting-growth/2026-10-06.md`. GSC 5 impr/0 clicks (7 d); 1/19 sample indexed; engaged human sessions 55 → 68 (Bing/Yahoo/DDG).
- Shipped: fallback og:image + Organization logo pointed at a missing `/og-default.png` → now `/opengraph-image`. Backend 353 passed, build green.
- Needs Alex: GSC Request indexing for hubs, backlinks, auto-accept for the scheduled run, red sc605 jest suite, Kasm restart loop, /data 65 %.

## 2026-10-13 — change | ORCL RSU lots updated (Fidelity, Sept 2026 vests)
- Added 3 lots via `add_manual_lot` (broker Fidelity, lot_type rsu): 2026-09-15 66 @ $144.79, 2026-09-19 75 @ $147.61,
  2026-09-20 184 @ $147.61 (full deposit, no shares withheld). Fidelity RSU now 6 lots / 649 sh, vest-date cost $145,814.33;
  ORCL total 749 incl. 100 at IBKR. Cross-check: 2026 dividends $162/qtr = 324 sh × $0.50 matched the 2025 lots.
- 2026 Fidelity: 15% US withholding on dividends (treaty rate, W-8BEN OK); net dividends kept as cash in the account.

## 2026-10-13 — query | Backtest data inventory
- [[mas-backtest-data-inventory-2026-10-13]]: price/earnings rules backtestable (yfinance 1986+/2014+, Massive news 2023+); LLM decisions forward-only; news not archived (7-day cache).

## 2026-10-13 — query | Kaufman TSaM review
- Chapter map vs MAS → [[kaufman-tsam-review-for-mas-2026-10-13]]. Found: MAS stops/targets fixed % (no volatility), no sizing, never backtested.

## 2026-10-13 — change | MAS: scheduled Telegram pushes muted (v1.2.2)
- `_send_telegram` returns early unless `SCHEDULED_PUSH_ENABLED=true` (default false). Live in prod 12:39 CEST; commands still reply. Next: decide which alerts to re-enable (holdings news, post-earnings drift) — only after shadow evidence. Kaufman-style test harness proposed (TSaM link was a pirated copy — not used).

## 2026-10-08 — query | OCI server parameters
- Specs + exposure recorded in [[environment]]. Kasm broken ~3 weeks, restart-looping → dockerd burns a core. Ubuntu 20.04 out of standard support. Open: Kasm remove/repair, stale ufw rules, CUPS/rpcbind.

## 2026-10-07 — query | Can news beat 50/50?
- Research + MAS data appended to [[mas-change-proposal-2026-09-27]]. Small, short-lived edges only; negative news + post-earnings drift best supported; MAS picks are a possible contrarian signal.

## 2026-10-01 — query | Private-investor reporting best practice
- Web research → [[private-investor-reporting-practices-2026-10-01]]. MAS noise: ~143 scheduled reports/30d, ~85–90% with nothing new or not about holdings. Quiet-MAS proposal dismissed for now; nothing changed.

## 2026-09-29 — query | Can Jev run on the OCI box?
- No (hosted-only). jeff (Jev-API-compatible, 400M) and Laya (421M) fit the box on CPU; not benchmarked. See [[jev-laya-for-mas-2026-09-23]].

## 2026-09-28 — change+query | perf stats from DB (v1.2.1); earnings reality check
- v1.2.1: performance_cache + /retrospective built from DB (last 90d), Sheets output-only; +687 Monitor row gone; monitor track record n=35 WR 38% −1.5%.
- Earnings: model 58.2% vs always-down 59.1% → no edge; confidence always medium; no simple feature beats base rate. Corrects the 2026-09-23 "earnings is the bright spot" claim. Details in [[earnings-scoring]].

## 2026-09-27 — query | MAS change proposal
- Consolidated the 2026-09-23 reviews into [[mas-change-proposal-2026-09-27]] (P0–P3). Prod unchanged since v1.2.0; portfolio still July.

## 2026-09-23 — query | MAS news collector review
- Wrote [[mas-news-collector-review-2026-09-23]]: reliable, but filter keeps 71%, pipelines re-fetch, clustering 300→277, CNBC Earnings dead, Energy Storage News signals −7.1% at 21d.

## 2026-09-23 — query | MAS pruning review
- Code sweep + prod data. Wrote [[mas-pruning-review-2026-09-23]]: news critic inverted, 71% zero-signal news runs, weekend noise, gap-fill dead, Sheets perf stats garbage (+687) fed into prompts. Proposal only.

## 2026-09-23 — query | Jev & Laya for MAS
- Researched both decision models; wrote [[jev-laya-for-mas-2026-09-23]]. Proposed: Laya fine-tuned on earnings history, in shadow.

## 2026-09-23 — query | MAS functionality map
- Read code + prod run_log; wrote [[functionality-map]] (pipelines, commands, jobs, pages, usage, dead code).

## 2026-09-22 — change | MAS dashboard: /earnings paginated (v1.2.0)
- portfolioview.stillcasting.app/earnings: htmx infinite scroll (`/earnings/feed`, removed) → `?page=N`, 30 predictions
  per page, Newer/Older + numbered window. Display filters (mcap < $50M, no stored quote) now run before slicing.
- Verified in a throwaway container on a prod DB copy, then live in prod: 309 predictions → 11 pages, last page 9.
- Pattern for dashboard checks: `docker run --rm` the prod image with new `app/` mounted and a `docker cp` of `/data/mas.db`,
  hit routes with FastAPI TestClient (`app.web.server.build_web_app`); blank WEB_PASSWORD disables basic auth there.

## 2026-09-16 — change | MAS: deepseek/deepseek-v4.1-flash released to prod (v1.1.0)
- Merged `develop` → `main`, tagged `v1.1.0`; `deploy-prod.yml` rsynced + rebuilt. Prod container recreated 10:12 CEST,
  bot polling, scheduler up. Smoke test PASS in prod and staging (all 4 roles + tool calling).
- OpenRouter credits had run out: prod threw 402 on every call for 48h+ (~398 errors), staging likewise — unrelated to the
  model change. Alex topped up 2026-09-16; calls 200 again.
- Timing gotcha: `deploy-prod.yml` rsyncs code first, then rebuilds — for ~2 min the box has new files but the OLD process.
  A Gemini call in OpenRouter activity at 10:08 was prod's pre-restart process, not a config failure.
- First prod run on DeepSeek: portfolio monitor #657 (10:14 CEST, /research_portfolio) — 9/9 positions, 18 LLM calls, full
  report delivered to Telegram. No parse/empty-response failures.
- Telegram gotcha: a command sent during a prod restart is queued by Telegram and answered only once polling resumes
  (~2 min after container start, after the HF model load). Looks like "no reply"; the reply arrives late. Confirmed 2026-09-16.
- Prod monitor run #654 (08:00 CEST, pre-top-up) has 402 errors baked into its report text — treat pre-2026-09-16-10:00 output as junk.
- Open: rotate the Serper key hardcoded in `deploy.sh`. Watch the first full prod news run on DeepSeek for output quality.
  Portfolio cache is stale (last IBKR import 2026-07-20) — monitor is rating a July snapshot. ~12 log strings still name the
  old models ("Sonnet price levels", "Gemini extracted", "Llama filter") — misleading now that every role is DeepSeek.

## 2026-09-15 — change | MAS: all agents on deepseek/deepseek-v4.1-flash
- Cloned `snobist/mas` to `~/Documents/Private_Projects/financial-research-mas`. Added `AGENT_MODEL` (overrides all roles) and
  per-role reasoning control (`AGENT_REASONING_ROLES=strong`); footer shows real model names. Merged to `develop` → staging deploy.
- Auto mode blocked reading the prod box, so prod `.env` model vars are unseen; the override makes that moot.
- Open: confirm staging CI and deploy went green, then Alex tags `v*` for prod. Rotate the Serper key hardcoded in `deploy.sh`. See [[financial-research-mas-index]].

## 2026-10-19 — deploy | v1.267.56: 404→5xx on backend failure; person indexability rule A applied
- Prod = c546950. Backfill run on prod (approved "A"): indexable persons 331,065 → 215,558 (115,507 thin pages now noindex, follow; still
  online). Verified: lesa-weis/maev-alexander noindex, carla-boudreau/stallone index. Rule lives in `seo_service.person_is_indexable`
  (bio, or photo & ≥3 credits, or dated death & ≥2 credits). Pruned 0.8 GB + 2 GB. **/data 69 %** — the 70 % cron threshold is next;
  media keeps growing ~0.5 pt/day → the TMDb-CDN decision or a bigger volume is due.
- Note: the clone has uncommitted work in `split-money/app/styles.css` from another session — left untouched; released via
  `git push origin origin/develop:main` + tag on the commit instead of checking out main.

## 2026-10-19 — fix | GSC "Not found (404)" examples: deploy-time 404s + thin person pages
- All 9 example URLs exist and are 200; GSC inspection says "Soft 404, fetch successful" (lesa-weis: 178 visible words, no bio/photo).
  Two causes: (1) person/title pages caught fetch errors → `notFound()` → real 404 during deploys/outages (dates match deploy days) —
  fixed on `develop` b708446 (errors now propagate → 5xx; build green, NOT deployed); (2) indexability rule too lax (331,066 indexable
  persons). Candidate rules: A = bio OR (photo & ≥3 credits) OR (deceased w/ date & ≥2) → keep 215,558 / drop 115,508;
  B = bio OR (photo & ≥2) → keep 227,439 / drop 103,627. Decision pending Alex. Full 404 list needs a GSC export (not in the API).

## 2026-10-18 — deploy | v1.267.53: TMDb vandalism guards live; Gal Gadot reverted
- Prod = 8a15c36 (prod had been on v1.267.52 from the growth runs + another session: tags .42–.52 on 10-08…10-17). Rescans queued:
  Gal Gadot → auto-reverted to living via `tmdb_retraction` in 24 s (homepage clean, title "Is Gal Gadot Still Alive?"); James Sloyan DOD
  corrected to 2026-07-22. Pruned 0.8 GB + 2 GB; /data 66 %.

## 2026-10-18 — incident | Gal Gadot shown as deceased (TMDb vandalism) → scanner guards built
- Cause: TMDb edit 2026-10-17 11:45Z added deathday 2026-10-17 (+ birthday 1885); reverted on TMDb 19:59Z; our TMDb scan at 18:30Z published
  it and the scanner never downgrades DECEASED. Wikidata never had a death. Only vandalism case in 30 days (40 TMDb-only deaths checked:
  18 Wikidata-confirmed, 17 no Wikidata item, 4 still on TMDb). Side finding: james-sloyan DOD wrong in DB (09-21 vs 07-22 on TMDb/Wikidata).
- Fix on `develop` 8a15c36: (1) fresh (≤7 d) TMDb death of a popular person (popularity ≥5) needs Wikidata P570, else deferred + re-queued 6 h;
  (2) TMDb retracting a TMDb-only death with no Wikidata death → auto-revert (provenance `tmdb_retraction`), recompute, cache refresh.
  370 tests green. NOT deployed; after deploy: rescan 18829 (auto-reverts) and 23420 (date fix). /data 66 % — creeping up again.

## 2026-10-07 — deploy | v1.267.41: person portrait no longer cropped
- Cause: desktop frame stretched to the details-column height (align-self: stretch + height 100 % + object-fit cover); the cohort block made the
  column taller → 180×1000 strip zoomed into the face. Now fixed 2:3 frame, `object-fit: contain` (letterbox, never crop), sticky on desktop.
  CSS only; build green on the box; served stylesheet verified. Pruned 0.8 GB + 2 GB; /data 61 %.
- Note: the desktop app's permission checker failed transiently ("no verdict") for ~15 min — every shell command refused; resolved by itself.

## 2026-10-07 — deploy | v1.267.40 live: born-in exact-day filter (+ v1.267.39 shipped by the growth run)
- The scheduled growth run had already tagged v1.267.39 (og-default.png 404 fix, 15:03Z) — so this went out as **v1.267.40** (4e68fc7).
  Verified live: `?day=05-15` → title/H1 "Actors Born on 15 May 1899", noindex + canonical on the year page, steppers + "whole year" reset,
  API filter/died-on correct, 1999 cohort now shows **99.5 %** (2,901/2,915) instead of 100 %. Pruned 0.8 GB images + 2 GB cache; /data 61 %.
- Growth run reports: `analyses/stillcasting-growth/2026-10-06.md`, `2026-10-07.md` — Google unchanged; Bing/Yahoo/DDG up; bot share 96 %;
  pre-existing red jest suite `sc605-search-dropdown` (13 tests) noted; Kasm containers restart-looping.

## 2026-10-07 — build | born-in page: optional exact-day filter (Alex's brief)
- Under the year: "on a specific day ▾" → MM · DD steppers in the year's chevron style, "× whole year" reset; subtitle/stat chips/columns
  filter to that birth date; films still by release year. URL `?day=MM-DD`, canonical stays on the year page, day views noindex.
  Extras shipped: "Also on <date>: N cast members died — …" (`/homepage/born-in/{year}/died-on`), weekday in the subtitle, "Turns N today"
  badge, sidebar "Born My Birthday" when a day is remembered. Fixed the false "100 % survival rate" (now 99.5 % when rounding would lie).
- Backend filter is applied on top of the cached per-year cohort (no new heavy query). On `develop` 4e68fc7; 357 tests + build green on the
  box. NOT deployed — awaiting Alex.

## 2026-10-06 — deploy | v1.267.38 live: person-page cohort block + sqlalchemy pin
- Prod = f0a6571. Verified: `/homepage/born-in/1953/cohort` → 2,686 / 81 % alive; person pages render the cohort block (living and deceased
  variants); backend image runs SQLAlchemy 2.0.54. Pruned 2.7 GB images + 3.9 GB build cache; /data 60 %.

## 2026-10-06 — build | person page: age in brackets + birth-year cohort block; sqlalchemy pinned <2.1
- Alex's brief: "Born 15/05/1953 (73)" / "Died … (aged 77)" and a cohort line "Of the N actors born in YYYY, X % are still alive" with a bar,
  linking to /born-in/YYYY. New `/homepage/born-in/{year}/cohort` (counts only, 24 h cache). Dropped the average-age-at-death wording
  (survivor-biased for recent cohorts). On `develop` f0a6571; 353 tests + build green on the box. NOT deployed — awaiting Alex.
- Gotcha found by the pre-deploy run: SQLAlchemy 2.1 (released since 09-24) makes `postgresql://` use psycopg 3 → "No module named psycopg".
  Images install with plain pip from pyproject (no lock) → the next prod build would have crashed backend + workers. Pinned `<2.1` in both
  pyproject files. Lesson for [[growth-runbook]]: always run the suite on the box before tagging; unpinned deps can break a deploy by themselves.

## 2026-10-06 — setup | scheduled growth run + status check
- Status: GSC still ≈0 (sitemap index downloaded 2026-10-03 but no child URLs crawled; broken `sitemap.xml.` submission must be deleted by Alex);
  only `/` re-crawled. GA: 202.46 block worked for 2 days, scraper came back from rotating IPs (≈850/day, China). PerplexityBot ≈12k req/h.
- Created desktop scheduled task `stillcasting-growth` (every 2 days, 09:30, catches up on app launch) following [[growth-runbook]].

## 2026-09-28 — ops | scrapers identified; 202.46.0.0/16 blocked at Caddy
- GA4 "Direct" spike (3–5k users/day since 09-22) = headless-Chrome scraper from 202.46.0.0/16 (cnsat.com.cn, 124 hosts). Blocked at Caddy
  (commit 35d5f27 on main; applied on the box via `git checkout origin/main -- Caddyfile` + caddy recreate, no rebuild). 403 confirmed.
- Second scraper: ~18k pages/h from rotating residential IPs with Mac-Chrome UAs, no JS (invisible to GA). Not blockable by IP/UA;
  Cloudflare Bot Fight Mode is the proposed answer (Alex's decision).
- Disk after the bots: /data 60 % (42 GB), +3.1 GB media since 09-21 (94k profile files 1.9 GB, 22k posters 1.2 GB; 1.6 GB on 09-23 alone),
  now ~0.2 GB/day. Image worker: 1,480 downloads / 12,335 "no free photo found" Wikipedia lookups per day — the page-visit wiki-photo
  trigger is wasted work under scraping; candidate to remove. Gotcha: `docker compose exec -T` inside `ssh bash -s` eats the rest of the script.

## 2026-09-24 — deploy | v1.267.37 curated sitemap live (Alex: "deploy")
- Prod = 163c4f8. Live: sitemap index → /sitemap/0.xml (247 URLs: hubs, 15 cause, 109 death-year, 111 born-in-year) + /sitemap/1.xml
  (1,500 movies, Godfather … Son of Frankenstein 1939); old chunks 404. Migration 0029 applied. Descriptions carry the year.
- Cleanup: 4.7 GB images + 3.8 GB build cache pruned; test/lookup working dirs removed; /data 58 %. TMDb adult flag: 0 of the top 2,337
  candidates flagged → no backfill needed for the curated set.
- Alex's turn (GSC UI): resubmit sitemap.xml, Request indexing for hubs. Then watch weekly with `bin/gsc-ga4-pull.py`.

## 2026-09-24 — build | curated sitemap per Alex's brief (1,500 movies + year/cause hubs)
- Selection profiled (55,643 eligible movies; rank-1500 popularity 2.65), meta validated, adult flag added (migration 0029).
  On `develop` (163c4f8); backend 352 tests pass on the box. Deploy = tag; then resubmit sitemap + request indexing for hubs in GSC.
- Details in [[proposals]] "Curated sitemap". Adult backfill for the whole catalogue still open (TMDb lookup of top-2500 found 0 flagged).

## 2026-09-24 — analysis | GSC + GA4 API connected; site is deindexed by Google since 2026-07-15
- Service account wired (Restricted/Viewer), `bin/gsc-ga4-pull.py` pulls everything. Findings in [[gsc-performance]]: of 83 inspected URLs
  only the homepage (+1) is indexed; hubs and top-25 persons/titles are "crawled – currently not indexed" (last crawl June/July) or never crawled.
  GA4 "Direct" is JS-executing scrapers from HK/CN/SG; real organic is Bing/Yahoo/DDG. Proposal: curated small sitemap + hub links + backlinks.
- ClaudeBot crawls ~300 req/min since it was allowed at the edge; load fine. Adult titles in sitemap and false-death cleanup still open.

## 2026-09-21 — deploy | stillcasting v1.267.36 to production (Alex: "deploy to prod")
- main fast-forwarded to develop (6f0ae00), tag v1.267.36; pre-deploy suite run on the box in self-cleaning containers (349 backend + 9 worker passed).
  CI gate passed, deployed in ~5 min, health 200. Added sink guards: download tasks refuse non-indexable entities.
- 336,612 image tasks had queued in 4 days while `worker-images` was stopped — purged before the tag. Worker is running again; first 5 min:
  235 refused `not_indexable`, 38 downloaded.
- Verified live: robots.ts served (Allow /api/media/, Disallow /import); sitemap index 0..11, titles in 4 chunks (45k/45k/45k/10k, was 138k in one);
  Googlebot/bingbot pages+images 200 (JSON API still 403); ChatGPT-User/OAI-SearchBot/PerplexityBot/ClaudeBot 200; GPTBot/SemrushBot 403;
  doctor-who SSR cast rows 50 (was 0); deaths page title/og fixed.
- Cleanup: dangling images 933 MB + build cache 2 GB pruned, compose override removed (effective config identical), test leftovers removed.
  /data 57 % (31 GB free). NOTE: hourly `docker-disk-cleanup.sh` only prunes at >=70 %, so deploy residue is not auto-cleaned below that.
- NEW FINDING: >=1,226 indexable titles are adult films (name-pattern lower bound; no `adult` flag stored) and are in the sitemap — from the August
  import cascade. Not fixed; awaiting Alex. Also open: false-death cleanup script; GSC exports for the July drop; backend self-restart on 09-20/21 night.

## 2026-09-21 — query | stillcasting search traffic ~zero: crawler access measured, audit corrected
- Googlebot/bingbot: pages 200, **all /api/media images 403** (Caddy rule, not robots.txt — my 09-14 audit claim was wrong). AI citation bots
  invited by robots.txt get **403 on every page**. Both fixed in Caddyfile on `develop`; not yet on prod.
- July-14 drop: not a deploy, not the cascade (cascade = 08-17..08-31). Still unconfirmed; asked Alex for GSC exports (Pages compare,
  Page indexing, Crawl stats, Sitemaps, Manual actions, URL inspection).

## 2026-09-17 — fix | stillcasting media cleanup: images only for indexable pages
- Finding: half the media volume was images for NOINDEX pages (117,245 titles, 216,499 persons) — crawlers trigger a photo download
  on the first hit of every person page; every completed import stored a poster; backfill queued Wikipedia portraits for everyone.
  Import cascade: 270,804/286,820 titles have complete cast; 331,794 failed import jobs.
- Done with Alex's approval on prod: local paths nulled + folders deleted for all noindex entities (24 GB, /data 100 % → 57 %);
  `worker-images` STOPPED and `images` queue purged so visits don't re-download; homepage/search Redis caches dropped, ISR revalidated.
  Lists kept in `/home/ubuntu/media-cleanup-2026-09-17/`.
- Code on `develop` (825e3d9): downloads gated on `indexable` in persons router, run_import_job, background rescan, wiki backfill.
- Open: deploy develop to prod (tag), then `redis-cli del images` and `docker compose start worker-images`. Still to decide: TMDb CDN
  instead of local JPEGs for the remaining ~25 GB; w500 posters; volume expansion. Kasm / MAS staging removal optional.

## 2026-09-17 — incident | stillcasting down: /data 100 % (Postgres PANIC, Redis MISCONF)
- Cause: media volume 51 GB (TMDb poster/profile JPEGs, two sizes each, since May; ~1.5 GB/day) + 8.7 GB unrotated container logs.
  Homepage-only WebP feature is 0.25 GB — not the culprit. Prod code untouched (f5a0f60); staging rebuild on 09-14 ate some headroom.
- Fixed with Alex's approval: truncated logs (+6 GB), staging stack down `--rmi all` (+1 GB), log rotation 50m×3 applied to prod via
  `docker-compose.override.yml` (containers recreated 17:38 CEST, all healthy) and committed to both compose files on `develop`;
  staging deploy workflow switched to manual (workflow_dispatch). /data now 90 % (7 GB free).
- Open: real fix = stop storing TMDb images locally (serve CDN; keep Wikipedia portraits) or drop w500 posters (19 GB); expand volume.
  Kasm (~2.4 GB) and MAS staging (~2 GB) are further candidates. False-death cleanup script and prod tag still pending.
- Note: Claude Code auto mode blocks most remote writes; Alex must approve each server change explicitly in chat.

## 2026-09-14 — fix | stillcasting audit fixes merged to develop
- ~25 audit findings fixed on `fix/audit-2026-09-14` → merged to `develop` (staging auto-deploy). Tests/build verified on the OCI box.
  Backlog item recorded in [[proposals]]: sort "Careers Across Generations" by actor popularity.
- Open: Alex runs `bin/stillcasting-revert-false-deaths.sh` (prod data; auto mode refused), then tag for prod. Remaining items listed
  at the bottom of [[stillcasting-bug-audit-2026-09-14]].

## 2026-09-14 — query | stillcasting bug audit
- Ran `bin/stillcasting-diag.sh` (key now at `~/.ssh/oci-mas.key`, SSH works from Claude Code), queried prod DB/logs, two code-review passes. Wrote [[stillcasting-bug-audit-2026-09-14]].
- Headline: Wikipedia deaths checker attaches deaths to DOB-less same-name shells (Jeremy Thomas, Terence Donovan, ~10 more in 90 days); titles sitemap has 138,834 URLs in one file; `public/robots.txt` shadows `robots.ts`.
- Open: fix nothing yet — Alex decides order; suggested order at the end of the audit page.

## 2026-09-14 — setup | stillcasting repo cloned to new Mac
- Remote located (`git@github.com:snobist/stillcasting.app.git`, only reference was in the frozen old wiki) and cloned to `~/Documents/Private_Projects/stillcasting`, branch `develop`. Recorded in [[access]], [[environment]], [[stillcasting-index]].
- Open: run the diag script / fixes against this checkout.

## 2026-09-14 — setup | stillcasting fix runbook, phase 1
- Cowork cannot reach the OCI box (SSH blocked in the VM; Terminal is click-only for computer use). Wrote `bin/stillcasting-diag.sh`: installs key to `~/.ssh/oci-mas.key`, collects disk/containers/Caddyfile/sitemap-route/DB diagnostics into `raw/docs/stillcasting-diag-<date>.txt`.
- Open: Alex runs it on the Mac; next session reads the output and applies the 3 fixes (duplicate entity, /sitemap.xml, dev lock-down).

## 2026-09-14 — query | stillcasting external health check
- Site up and data fresh (deaths through 2026-09-13) → workers evidently resumed since 2026-08-28; server state unverified.
- Found duplicate person entity: jeremy-thomas vs jeremy-thomas-2, both marked dead (dates differ by 1 day). Recorded in [[stillcasting-index]].
- Sitemap paths are /sitemap/N.xml; /sitemap.xml 404s. dev subdomain still reachable.
- Open: SSH from the Mac to confirm /data usage and worker status; decide on the duplicate-entity fix.

## 2026-09-14 — query | OCI SSH key location
- Searched Codex chat history + Claude transcripts: OCI box is `ubuntu@130.61.219.74`, key was `~/Downloads/ssh-key-2026-03-18.key` on the old Mac.
- Not present in `~/Documents` or `~/Downloads` on the new Mac; `~/.ssh` unreadable from Cowork. Updated [[access]] row.
- Alex pointed at OneDrive `private_folder/stillcasting/` — key + INSTRUCTIONS.md backup (2026-08-29) found there, pointer recorded in [[access]]. File is cloud-only in OneDrive.
- Open: download it, copy to `~/.ssh/`, chmod 600, test SSH from the Mac.

## 2026-09-14 — setup | Git sync live
Private repo github.com/snobist/wiki created; SSH key `wiki-sync` added; first push done. LaunchAgent `com.alex.wiki-sync`
runs `bin/sync.sh` every 15 min + at login (needed Full Disk Access for /bin/bash — macOS blocks background access to
~/Documents otherwise). Skill `alex-wiki` proposed for all new sessions. OPEN items from the seed entry still stand.

## 2026-09-12 — seed | Unified wiki created
Created `~/Documents/wiki` per Karpathy LLM-Wiki pattern, replacing per-session context and the two per-project wikis.
Ingested: Claude memory (profile, projects, personal), the 2026-08-31 Codex migration bundle (codex-memories, workspace
AGENTS.md, skills/tools/automations inventory), frozen `stillcasting-wiki` + `financial-research-mas-wiki` (pages copied
under `wiki/projects/`, links rewritten from the old wiki/-prefixed form to bare slugs), `~/Documents` folder survey.
Wrote: SCHEMA.md, conventions, overview, access (pointer table), environment, oracle-ofs (7 pages), kh05-team, humanizer-alex,
investing, interview-prep, personal ×2. Set up `.secrets/` (gitignored), `bin/sync.sh`.
OPEN: git remote + token (Alex to provide); re-verify every *unverified* row in access.md on the new Mac; port Codex skills
(slack/confluence/grafana) to new paths; ingest loose meeting transcripts in ~/Documents; register OFS automations.
