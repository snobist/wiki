# Log

Append-only, newest at top. Format: `## YYYY-MM-DD — <op> | <title>`.

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
