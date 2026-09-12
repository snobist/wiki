# Schema — StillCasting Wiki

This wiki follows Karpathy's "LLM Wiki" pattern: a persistent, AI-maintained
knowledge base that compiles knowledge once instead of re-deriving it each session.
Source pattern: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Layers
1. **sources/** — raw inputs (GSC observations, the SEO audit PDF, proposal docs, live-site probes). Not rewritten, only cited.
2. **wiki/** — compiled, de-duplicated knowledge entries. One topic per file. This is the durable artifact.
3. **schema.md + index.md** — configuration and the navigable map.

## Operations
- **ingest** — take a new source (a GSC screenshot, a deploy, a decision) → update the relevant wiki entry, add a `log.md` line, cross-link.
- **query** — answer a question from `wiki/` + `index.md` without re-crawling the site or re-reading raw sources.
- **lint** — health check: stale facts, unresolved contradictions, broken `[[links]]`, entries missing a `Status`/`Last-verified` line.

## Entry conventions
Each `wiki/*.md` entry has:
- A one-line **purpose** under the title.
- **Status** and **Last-verified** (date) near the top where facts can go stale.
- **Cross-links** as `[[wiki/other-entry]]`.
- **Sources** cited inline as `(src: …)`.
- Facts stated as of a date when they are time-sensitive (GSC metrics, deploy state).

## Contradiction rule
When a new source contradicts an existing fact, do **not** silently overwrite.
Record both, date them, and mark which is current (e.g., "was X on 2026-06-06;
now Y on 2026-06-21"). The GSC metrics timeline in `[[wiki/gsc-performance]]` is
kept as a dated series for this reason.

## Human vs LLM roles
- Human (Oleksandr): curates sources, makes product/editorial/deploy decisions, sets thresholds.
- LLM: maintains cross-references, distills sources into entries, flags contradictions and staleness, keeps `log.md`.

## Naming
- Slugs kebab-case. Entries are nouns/topics, not tasks.
- Dates ISO `YYYY-MM-DD`. "Today" is never used in durable text — always an absolute date.
