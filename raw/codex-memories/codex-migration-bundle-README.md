# Codex migration bundle

Created on 2026-08-31 from the current Mac. This is a portable working backup, not an authentication transfer.

## Included

- `chat-history/` — 731 current and 288 archived session files at export time, attachments, session index, and consistent snapshots of desktop state/log databases.
- `configuration/` — redacted Codex configuration, rules, automations, and Codex memory.
- `skills/` — custom/user-installed skills, including HumanizerAlex, Slack browser access, Confluence browser access, Jira CLI ticket creator, BugDB operations, and repo reporting.
- `workspace-context/` — project `AGENTS.md`, AI Studio skill, local team/product-owner/ownership memory, and access notes.
- `tools/` — Jira ticket wrappers, Grafana Loki wrapper/scripts, and workspace-local ticket tooling.
- `automation-dependencies/` — all 10 automation definitions plus their local inputs: customer ticket Excel exports, the activity tracker and Slack scanner, and Git-working copies of the 10 OFS repositories used by the daily repo report.
- `inventory/` — plugin names/manifests and export counts.

## Deliberately excluded

- `auth.json`, Jira personal token, OAuth/session cookies, browser profiles, debugger profiles, keychain data, installation ID, caches, and local app/runtime binaries.
- Cached plugin payloads. Install current plugins on the destination Mac, then restore custom skills from this bundle.
- Live `.env`/`.env.local` files inside copied repositories. Recreate credentials from the destination Mac's secure configuration.

Chat history is unredacted user content and may include sensitive material pasted into prior conversations. Keep this entire bundle in encrypted storage and do not share it as a general-purpose archive.

## Restore on the new Mac

1. Install Codex/ChatGPT and sign in. Install or enable the plugins listed in `inventory/plugin-manifest-paths.txt`.
2. Copy the folders under `skills/` into `~/.codex/skills/`. Copy `workspace-context/.codex/` into the matching project checkout, then copy `tools/` into that checkout if desired.
3. Use `configuration/config.toml.redacted` as a reference only. Update all macOS paths and enter fresh secrets in the new Mac's secure configuration. Do not copy the redacted file over a newly generated config blindly.
4. Re-authenticate in Jira and in browser sessions. The Slack and Confluence skills contain the browser-debugger setup and scripts; launch a fresh remote-debug Chrome profile, sign in, then use the documented browser-backed workflow.
5. Keep `chat-history/` as a portable archive. Importing these database/session files into a fresh desktop installation is not guaranteed to be supported; preserve the original structure and consult the Codex version's supported import path before replacing any live state database.
6. Scheduled-task definitions are preserved at `configuration/automations/`, but they are not registered as live scheduled tasks on the new Mac. Recreate/re-enable them there and update the old absolute paths/project IDs in the definitions. Their copied local inputs are in `automation-dependencies/`. One old working directory, `~/Documents/OrgAnalytics/web`, was not present on this Mac during export and therefore needs a fresh checkout or an updated task directory.

## Verification

Run `sqlite3 chat-history/state_5.sqlite 'PRAGMA integrity_check;'` and the same command for `logs_2.sqlite`. Compare the session-count files in `inventory/` with the copied folders.
