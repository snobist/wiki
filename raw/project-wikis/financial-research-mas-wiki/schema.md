# Schema — financial-research-mas Wiki

This wiki follows Karpathy's "LLM Wiki" pattern: a persistent, AI-maintained
knowledge base that compiles knowledge once instead of re-deriving it each session.
Source pattern: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Layers
1. **sources/** — raw inputs (DB query outputs, backtest results, diagnosis scripts). Not rewritten, only cited.
2. **wiki/** — compiled, de-duplicated knowledge entries. One topic per file. This is the durable artifact.
3. **schema.md + index.md** — configuration and the navigable map.

## Operations
- **ingest** — take a new source (a backtest, a deploy, a decision, a calibration reading) → update the relevant wiki entry, add a `log.md` line, cross-link.
- **query** — answer a question from `wiki/` + `index.md` without re-querying the DB or re-deriving from code.
- **lint** — health check: stale facts, unresolved contradictions, broken `[[links]]`, entries missing a `Status`/`Last-verified` line.

## Entry conventions
Each `wiki/*.md` entry has:
- A one-line **purpose** under the title.
- **Status** and **Last-verified** (date) near the top where facts can go stale.
- Dated metric series are **appended, never overwritten**. Contradictions get both
  values dated, not a silent overwrite.
- Cross-links as `[[wiki/entry-name]]`.

## Log conventions
`log.md` is chronological, append-only, **newest at top**. One short block per event
(a deploy, a finding, a decision), ending with a link to the updated entry.
