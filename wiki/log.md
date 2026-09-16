# Log

Append-only, newest at top. Format: `## YYYY-MM-DD — <op> | <title>`.

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
