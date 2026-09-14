# Access — services, auth routes, credential pointers

Where every credential lives and how each service is reached. **Pointers only — never values.**
`Last-verified: 2026-09-12` — most rows are imported from the 2026-08-31 Codex bundle (old Mac) and need
re-verification on the current Mac (`alexgrtsenko`). Status column says what is known.

| Service | Reach | Auth | Credential pointer | Status |
| --- | --- | --- | --- | --- |
| Wiki git remote (private) `github.com/snobist/wiki` | `bin/sync.sh`; LaunchAgent `com.alex.wiki-sync` every 15 min | SSH key `wiki-sync` | `~/.ssh/id_ed25519_wiki` (Host github.com in `~/.ssh/config`); `.secrets/git-remote` holds the URL | verified 2026-09-14; `/bin/bash` has Full Disk Access for the agent |
| Oracle Confluence | `confluence.oraclecorp.com` via Codex MCP `confluence` (`https://emcp.oracle.com/atlassian/centralconfluence/v2`, OAuth) or browser-authenticated Chrome fallback | OAuth / browser session | none stored; OAuth in Codex, session in Chrome | recovery cookbook: [[confluence-access]] |
| Oracle Jira | CLI wrappers `cli-ticket-create` / `cli-ticket-update` (Codex bundle `tools/bin`) | personal token | env `JIRA_URL`, `JIRA_PERSONAL_TOKEN`; fallback `~/.codex/config.toml` | token was excluded from bundle — re-create; see [[jira-workflow]] |
| Slack (Oracle workspace) | browser-derived auth script (Codex skill `slack-browser-access`) | `xoxc` token + `d`/`x` cookies decrypted from Chrome via Keychain | Keychain: browser "Safe Storage" item; script path in bundle | needs port to new Mac paths; see [[slack-access]] |
| Grafana / Loki (`oc1.octo.oraclecloud.com/grafana`) | `grafana-loki-query` wrapper | Chrome cookie `picauth_0` (Profile 2) via Keychain `Chrome Safe Storage` | Keychain item `Chrome Safe Storage` / account `Chrome` | old Mac paths; see [[grafana-access]] |
| OraHub (Oracle GitLab) — OFS repos | local checkouts `~/Documents/OFS_REPOS/*` | git creds | whatever git uses on the Mac (Keychain via osxkeychain helper) | unverified |
| OCI (stillcasting + MAS host) `130.61.219.74`, user `ubuntu` | `ssh -o ServerAliveInterval=15 -i <key> ubuntu@130.61.219.74` (from the Mac; Cowork VM cannot open SSH) | SSH key (1675 B, RSA PEM) | Backup: `~/Library/CloudStorage/OneDrive-OracleCorporation/private_folder/stillcasting/ssh-key-2026-03-18.key` (+ `INSTRUCTIONS.md` recovery notes, + `claude-export-2026-08-29/` with old wikis & transcript). File is OneDrive **cloud-only** — must be downloaded ("Always keep on this device") before use; `chmod 600`. Local working copy: `~/.ssh/oci-mas.key` (recommended; unconfirmed) | pointer verified 2026-09-14; connection not yet re-tested from new Mac; see [[infra-deploys]] |
| stillcasting.app prod | Docker on OCI box, Caddy/nginx, Postgres | SSH | as above | see [[stillcasting-index]] |
| Google Search Console (stillcasting) | Domain property `sc-domain:stillcasting.app`, UI only | Google account | no API keys yet (2026-08-09) | see [[seo-indexing]] |
| IBKR | Client Portal API (planned for MAS) | IBKR login | not stored | see [[investing]] |
| OpenRouter, Telegram bot, Langfuse (MAS) | `.env` on the OCI box | API keys | `.env` in the MAS deploy dir on the box (never copied here) | see [[infra-deploys]] |
| Anthropic / Claude | Cowork desktop app, Claude Code | account | n/a | — |

## Rules for sessions
1. Look here before asking Alex "where is the key for X".
2. If a route is marked *unverified*, verify it once, then update the row and `Last-verified`.
3. A new service → add a row *before* finishing the task.
4. From a Cowork session the shell is a Linux VM: it can read files in mounted folders (`$HOME/mnt/Documents/…`)
   but **cannot** read macOS Keychain. For Keychain-backed routes use a macOS-side script (Codex / Terminal)
   or ask Alex to export into `.secrets/`.
