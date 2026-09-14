# Environment — machines, paths, tooling

`Last-verified: 2026-09-12`

## Machines
- **Current Mac**: `alexs-macbook-pro-local`, macOS arm64, user `alexgrtsenko`. Home: `/Users/alexgrtsenko`.
- **Old Mac** (retired ~2026-08-31): user `oleksandrgrytsenko`. Any path starting `/Users/oleksandrgrytsenko/` in
  raw sources is stale and must be re-mapped (lint item).
- **OCI VPS** — hosts stillcasting prod/staging, financial-research-mas (prod+staging), Kasm. `/data` volume is
  74 GB and chronically full (see [[infra-deploys]], stillcasting log 2026-08-26/28).

## Where sessions run
- Claude Cowork: cloud container + a Linux VM on the Mac (`device_bash`). Mounted folders appear under
  `$HOME/mnt/<folder>`. Only granted folders are visible; `Documents` is the one to grant (wiki lives there).
- Claude Code / Codex: run natively on the Mac.

## Folders on the Mac (`~/Documents`)
- `wiki/` — this knowledge base.
- `OFS_REPOS/` — Oracle Field Service repos: app_server, content-delivery, daily-extract, daily-extract-scheduler,
  db-maintenance, db-updater, mobile-data-interface, platform-lcm, web. Several have `README.md`/`AGENTS.md`.
- `ClaudeProjects/` — frozen per-project wikis (superseded) + a Claude transcript.
- `Private_Projects/` — non-Oracle repo checkouts: `stillcasting/` (cloned 2026-09-14 from GitHub, branch `develop`;
  replaces the old-Mac `~/Documents/ClaudeProjects/stillcasting`).
- `Codex/` — dated Codex work dirs (2026-08-27 … ), `Codex/bin`.
- `Codex_Restored_2026-08-31/` — migration bundle from the old Mac: chat history, redacted config, skills
  (cli-ticket-creator, confluence-browser-access, grill-me, humanizer-alex, mr-review-risk, slack-browser-access),
  tools, automations. Secrets deliberately excluded.
- `LeetCode/` — interview prep scripts (arrays, linkedlist, tree, mock).
- Loose meeting transcripts: `meeting_01-09.txt`, `notes_04.09`, `meetingnotes09-09.txt`, `meeting10-09.txt`,
  `APIAPpcahe method.txt` — candidates for `raw/meetings/` ingestion.

## Git from the Cowork VM — gotcha
The VM cannot unlink files in mounted folders unless delete permission was granted for the session, so any git write
leaves `.git/*.lock` and `tmp_obj_*` behind and the next git call fails. Rule: sessions only edit markdown; the Mac
LaunchAgent syncs. If a lock is found: `find .git -name '*.lock' -delete` after requesting delete permission.

## Tooling
- Mac: git 2.34 (in the Cowork VM), no `gh`. Obsidian: not detected (optional — open `~/Documents/wiki` as a vault).
- Codex skills/automations exist but are not registered on this Mac yet (see bundle README).
