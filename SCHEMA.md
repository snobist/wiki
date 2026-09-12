# SCHEMA — Alex's LLM Wiki

Pattern: Karpathy's "LLM Wiki" (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
One persistent, compounding knowledge base that every AI session (Claude Cowork, Claude Code, Codex, …)
reads at start and maintains as it works. Nothing in it has to be re-explained per session.

## Location
- macOS path: `/Users/alexgrtsenko/Documents/wiki`
- From a Cowork session shell (Linux VM with Documents mounted): `$HOME/mnt/Documents/wiki`
- Remote: private git repo (see `wiki/access.md` → "wiki repo"). Synced by `bin/sync.sh`.

## Layers
1. `raw/` — immutable inputs. Never edited, only cited. Subfolders per source type
   (`codex-memories/`, `project-wikis/`, `meetings/`, `docs/`, `assets/`).
2. `wiki/` — the compiled knowledge. LLM-owned. One topic per file, kebab-case slugs.
3. `SCHEMA.md` (this file) + `wiki/conventions.md` — the contract. Co-evolved by Alex and the LLM.
4. `.secrets/` — gitignored, chmod 700. Local credential files. The wiki only ever stores
   **pointers** to these (`wiki/access.md`), never the values.

## Map of wiki/
- `index.md` — catalog of every page with a one-liner. Read this FIRST in every session.
- `log.md` — append-only, newest at top: `## YYYY-MM-DD — <op> | <title>`.
- `overview.md` — who Alex is, what is going on, current priorities. Read SECOND.
- `conventions.md` — house rules (how Alex likes things done). Read THIRD.
- `access.md` — every service/tool Alex uses: how to reach it, which auth, where the credential lives (pointer).
- `environment.md` — machines, paths, installed tooling, folders, what runs where (Mac vs VM vs cloud).
- `projects/<name>/` — one folder per project, with its own `index.md` when > 2 pages.
- `entities/` — people, teams, orgs, tools/services as things (not how-to).
- `concepts/` — methods, frameworks, patterns Alex uses or is learning.
- `analyses/` — comparisons, syntheses, answers to queries that were worth keeping.
- `personal/` — non-work: travel, gear, hobbies. Keep it factual; nothing sensitive.

## Session protocol (what every session does)
**Start:** read `wiki/index.md` → `wiki/overview.md` → `wiki/conventions.md`. Then only the pages the task
needs. If the task touches a service, read its row in `wiki/access.md` before asking Alex for anything.

**During:** when you learn something durable (a decision, a fact, a path, a gotcha, a new access route),
write it into the right page immediately — don't wait for the end. Cross-link with `[[slug]]`.

**End of session (if anything changed):**
1. update `wiki/index.md` if pages were added/removed/renamed,
2. append a `wiki/log.md` entry,
3. run `bin/sync.sh` (commit + push). Never leave the wiki unsynced after edits.

## Operations
- **ingest** — Alex drops a source into `raw/` (or points at a file/folder/URL) and says "ingest".
  Read it fully → discuss key takeaways → write/update pages (a source can touch 5–15 pages) →
  update index → log entry → sync.
- **query** — answer from `wiki/` first; cite pages. Re-read raw sources only when the wiki is silent or
  contradicts itself. If the answer was hard-won, file it under `analyses/`.
- **lint** — health check: contradictions (quote both sentences), stale `Last-verified` (> 90 days),
  orphan pages (no inbound links), missing cross-refs, broken `[[links]]`, secrets accidentally in
  plaintext, old paths (`/Users/oleksandrgrytsenko/…` is the OLD Mac — flag any that remain).
  Write findings to `analyses/lint-YYYY-MM-DD.md` and log it.

## Page conventions
- Title line, then one-line purpose, then `Status:` / `Last-verified: YYYY-MM-DD` where facts can go stale.
- Facts that are time-sensitive carry an absolute date. Never "today"/"recently" in durable text.
- Contradictions are recorded, dated, and the current one is marked — never silently overwritten.
- Computed/live values (SHAs, counts, metrics) are stored as *pointers* to where they can be re-read,
  or quoted with the date they were read.
- Sources cited inline as `(src: raw/…)` or a URL.

## Secrets rule (hard)
- No tokens, cookies, passwords, private keys in `wiki/`, `raw/`, or git — ever. Including in log entries.
- `wiki/access.md` maps *service → auth method → pointer* (`.secrets/<file>`, Keychain item name, env var).
- Credential files live in `.secrets/` (gitignored) or wherever `access.md` says.
- When a session uses a secret: read it from the pointer, keep it in memory/env, never echo it.

## Roles
- Alex: curates sources, decides, sets priorities, points sessions at new material.
- LLM: reads, distills, cross-links, flags contradictions/staleness, keeps index/log, syncs.
