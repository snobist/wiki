# Index

Catalog of every page. One line each. Update on every ingest. (Wiki root: `~/Documents/wiki`; contract: `../SCHEMA.md`.)

## Core
- [[overview]] — who Alex is, active threads, current priorities. Read second.
- [[conventions]] — how Alex wants sessions to behave and how the wiki is kept. Read third.
- [[access]] — service → auth route → credential pointer table. Read before asking about keys.
- [[environment]] — machines (new Mac `alexgrtsenko`, old Mac paths are stale), folders, tooling, where sessions run.
- [[log]] — chronological record of operations.

## Projects
### Oracle Field Service (day job) — `projects/oracle-ofs/`
- [[oracle-ofs-index]] — hub: team, repos, Jira, Confluence/Slack/Grafana access, automations.
- [[ofs-repos]] — local OFS repo checkouts and owners.
- [[jira-workflow]] — bug template, @RR@ note template, CLI ticket tools, MR risk review.
- [[confluence-access]] — MCP config, OAuth recovery cookbook, browser fallback.
- [[slack-access]] — browser-derived Slack API auth.
- [[grafana-access]] — Loki queries via Chrome cookie.
- [[ofs-automations]] — 10 Codex automations awaiting re-registration.

### stillcasting.app — `projects/stillcasting/`
- [[stillcasting-index]] — hub + state as of 2026-08-28 (infra: /data full, workers stopped).
- [[seo-indexing]] — indexability system, soft-404 fix, sitemap/robots, canonicals.
- [[gsc-performance]] — Search Console timeline; 2026-09-24: site deindexed by Google since Jul 15 (API analysis), GA4 bot noise, proposal.
- [[proposals]] — change proposals with status.
- [[pipeline-science]] — survival modelling, death-data fusion, false-death risk.
- [[growth-runbook]] — procedure for the scheduled 2-day growth run (data pull, health, one safe change, test, deploy, report).
- [[backlinks-outreach]] — /last-survivors data page + fact-checked claims, ranked outreach targets, pitch templates (2026-10-15; nothing sent).

### financial-research-mas — `projects/financial-research-mas/`
- [[financial-research-mas-index]] — hub + state as of 2026-08-09.
- [[functionality-map]] — MAS pipelines, Telegram commands, jobs, dashboard pages, usage, dead code.
- [[signal-quality]] — track records, calibration, contamination fix.
- [[earnings-scoring]] — decision-aware grading, reaction baseline, direction gates.
- [[infra-deploys]] — OCI/Docker deploy gotchas.

### Other
- [[investing]] — IBKR, options overlays, UCITS bond ETFs, Polish tax.
- [[interview-prep]] — EM job targets, LeetCode practice, conference talk.

## Entities
- [[kh05-team]] — KH05 roster, roles, repo-ownership weights.

## Concepts
- [[humanizer-alex]] — Alex's work voice (skill to port).

## Analyses
- `analyses/stillcasting-growth/` — dated reports from the scheduled growth run (from 2026-10-06).
  - `stillcasting-growth/2026-10-29.md` — GSC 10 impr; nothing re-crawled; organic Bing/Yahoo/DDG 99 sessions; audit clean (adam-wolke checker FP); no change.
  - `stillcasting-growth/2026-10-27.md` — GSC 9 impr; nothing re-crawled; GA4 bot flood gone; audit clean; no change (on-site levers exhausted, scope question to Alex).
  - `stillcasting-growth/2026-10-25.md` — GSC 23 impr; nothing re-crawled; sitemap index fetched 10-24; audit clean; no change (7 foreign commits on develop).
  - `stillcasting-growth/2026-10-23.md` — GSC 20 impr; Google re-crawled `/` 10-23; Tencent 403s −93 %; audit clean; no change (develop holds 14 unreleased foreign commits).
  - `stillcasting-growth/2026-10-21.md` — flat GSC (17 impr); Godfather re-crawled 10-20; Tencent block cut GA4 Singapore junk to ~0; audit clean (Bracardi date refreshed); no change.
  - `stillcasting-growth/2026-10-19.md` — GSC 17 impr (deep pages back on 10-17); false-death audit clean; /last-survivors double period fixed (v1.267.54); Tencent scraper → GA4 199k-session spike.
  - `stillcasting-growth/2026-10-17.md` — flat; GA4 CN/SG bot surge; /born-in junk years (1025, 2084…) now noindex (v1.267.52, deployed unattended).
  - `stillcasting-growth/2026-10-15.md` — flat; homepage links /deaths/<year> + top /cause pages (v1.267.50, deployed unattended).
  - `stillcasting-growth/2026-10-13.md` — flat; /statistics links recent years to /deaths/<year> (v1.267.49, deployed on Alex's go).
  - `stillcasting-growth/2026-10-12.md` — flat metrics; /statistics cause rows now link /cause/* (v1.267.48); predeploy harness fixes.
  - `stillcasting-growth/2026-10-09.md` — 5 hubs re-crawled 10-08, still not indexed; /spanning-generations now SSRs 30 entries (v1.267.47).
  - `stillcasting-growth/2026-10-07.md` — no change; v1.267.39 verified live; GSC/inspection flat; openclaw + Kasm restart loops on the box.
  - `stillcasting-growth/2026-10-06.md` — first run: Google still 0 (only `/` re-crawled); fixed 404 default og:image/Organization logo (v1.267.39).
- [[mas-backtest-data-inventory-2026-10-13]] — what data MAS has for system testing; what's backtestable vs forward-only; gaps.
- [[kaufman-tsam-review-for-mas-2026-10-13]] — Kaufman Trading Systems and Methods, chapter-by-chapter vs MAS: test harness, volatility units, risk layer.
- [[private-investor-reporting-practices-2026-10-01]] — how private/family-office systems report: policy, cadence, exception alerts, behavioural evidence.
- [[mas-change-proposal-2026-09-27]] — MAS: prioritised change proposal P0–P3 + decisions needed.
- [[mas-news-collector-review-2026-09-23]] — MAS news collector: reliability, filter, clustering, per-source signal outcomes.
- [[mas-pruning-review-2026-09-23]] — MAS: dead code, runs with no payoff, broken perf stats, proposed schedule.
- [[jev-laya-for-mas-2026-09-23]] — Jev/Laya decision models vs MAS: where they fit, the Laya-on-earnings-history experiment.
- [[stillcasting-bug-audit-2026-09-14]] — full site/code/prod audit: false-death matcher bug (Jeremy Thomas), sitemap >50k URLs, robots.txt shadowing, 30+ findings.

## Personal
- [[tenerife-cruise-2027]] — Jan 2027 cruise dates and flight plan.
- [[transport]] — e-scooter.

## Raw sources (not pages)
- `raw/codex-memories/` — 2026-08-31 Codex bundle memory/access notes, templates, team JSONs, workspace AGENTS.md.
- `raw/project-wikis/` — frozen originals of the two per-project wikis (with their full logs).
