# Environment — machines, paths, tooling

`Last-verified: 2026-09-12`

## Machines
- **Current Mac**: `alexs-macbook-pro-local`, macOS arm64, user `alexgrtsenko`. Home: `/Users/alexgrtsenko`.
- **Old Mac** (retired ~2026-08-31): user `oleksandrgrytsenko`. Any path starting `/Users/oleksandrgrytsenko/` in
  raw sources is stale and must be re-mapped (lint item).
- **OCI VPS** — hosts stillcasting prod/staging, financial-research-mas (prod+staging), Kasm.
  Specs (2026-10-08): `VM.Standard.A1.Flex`, eu-frankfurt-1 AD-3, created 2026-03-18 — 4 OCPU ARM Neoverse-N1
  (aarch64), 24 GB RAM + 2 GB swap, no GPU, 4 Gbps network; disks: / 45 GB (44% used), /data 74 GB (66%, ~+0.3 GB/day);
  Ubuntu 20.04.6 LTS (out of standard support since 2025-05), kernel 5.15.0-1081-oracle; Docker 28.1.1, Compose 2.35.1;
  22 containers. Public ports (verified from outside): 22, 80, 443, 8081 (Caddy → dev.stillcasting.app staging),
  8443 (Caddy → Kasm). 8080 (MAS dashboard) is published by Docker but filtered by the OCI security list — reached via
  portfolioview (443). Docker-published ports bypass ufw. Stale ufw allows with nothing listening: 3000, 5000, 8000,
  12414, 18789. CUPS (631) + rpcbind (111) run but are firewalled.
  **Kasm broken since ~2026-09-17**: kasm_db exited, kasm_api/share/manager in restart loops (24–29k restarts) →
  dockerd ~100% of one core, load avg up to ~3.8, I/O wait spikes. Decision pending: remove Kasm or repair kasm_db. `/data` volume is
  74 GB and chronically full (see [[infra-deploys]], stillcasting log 2026-08-26/28). 2026-09-17: hit 100 % (outage); after log truncation + staging teardown 90 %, 7 GB free. Log rotation 50m×3 now set on all prod containers. Docker root is `/data/docker`.

## Where sessions run
- Claude Cowork: cloud container + a Linux VM on the Mac (`device_bash`). Mounted folders appear under
  `$HOME/mnt/<folder>`. Only granted folders are visible; `Documents` is the one to grant (wiki lives there).
- Claude Code / Codex: run natively on the Mac.

## Folders on the Mac (`~/Documents`)
- `wiki/` — this knowledge base.
- `OFS_REPOS/` — Oracle Field Service repos: app_server, content-delivery, daily-extract, daily-extract-scheduler,
  db-maintenance, db-updater, mobile-data-interface, platform-lcm, web. Several have `README.md`/`AGENTS.md`.
- `ClaudeProjects/` — frozen per-project wikis (superseded) + a Claude transcript.
- `Private_Projects/` — non-Oracle repo checkouts: `financial-research-mas/` (cloned 2026-09-15 from `snobist/mas`), `stillcasting/` (cloned 2026-09-14 from GitHub, branch `develop`;
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
