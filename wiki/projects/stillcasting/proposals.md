# Proposals Register

Purpose: every change proposal from the session, its intent, and status.
Last-verified: 2026-08-09. Full docs live in `../` (ClaudeProjects root) and `sources/`.

## Shipped
### Title indexability (indexing exception + Person schema enrichment)
- Source: `stillcasting_seo_change_proposal_2026-06-06.md`.
- The "popularity exception" for zero-death high-demand titles shipped as **Phase 2** of
  `title_is_indexable` (floor 20, verified ≥10). Person JSON-LD already enriched in template
  (`description`, `nationality`; `gender`/`alternateName` proposed). See [[seo-indexing]].

### Person soft-404 gate
- Source: `stillcasting_proposal_person_soft404_2026-06-21.md`.
- `person_is_indexable` + `Person.indexable` wired into page + sitemap. Fixed ~12,500 soft-404s.
  Verified live. Open: `MIN_CREDITS` value; whether filmography-alone (no life data) qualifies. See [[seo-indexing]].

### Status-aware person headline
- Source: `stillcasting_proposal_deceased_headline_2026-06-06.md`.
- `personHeadline()` shared by `<h1>` and `<title>`: deceased+cause → "How Did {Name} Die?";
  deceased no-cause → "When Did {Name} Die?"; else "Is {Name} Still Alive?". Live in `persons/[slug]/page.tsx`.

## Approved (logic), blocked on design
### Title-page "How Many … Still Alive?" headline
- Source: `stillcasting_proposal_title_headline_2026-06-06.md` (v2, two review rounds).
- Data-aware `titleHeadline()`: deaths>0 → "How Many {Name} ({Year}) Cast Members Are Still Alive?";
  all-living (`unverified==0`) → "Where Is the Cast of {Name} ({Year}) Now?"; else neutral.
  Fixes baked in: R1 year kept for disambiguation (note: `year` var already includes parens — don't double-wrap);
  R2 all-living gated on `unverified==0` to avoid over-claiming; R3 short-title guard
  (`AMBIGUOUS_ONE_WORD_TITLES` stoplist → reorder to "Cast Members of {Name}" for "It"/"Her"/…).
- **Only remaining blocker: a design mockup** (H1 grows ~9→~54 chars; eyebrow pattern, mobile+desktop).
  Optional zero-maintenance alternative: always use the "of {Name}" ordering (loses a little keyword adjacency).

## Proposed (not started)
### Pipeline science upgrades
- See [[pipeline-science]] — actuarial survival modeling, Bayesian death fusion, record linkage,
  survival-analysis content, hazard-based scan scheduling, anomaly guard.

## Working conventions established this session
- Proposals are written as standalone Markdown in ClaudeProjects root (outside the git repo) so the repo's
  **auto-commit hook** doesn't pick them up. Each carries: problem, evidence, exact diff, alternatives-rejected,
  risk/rollback, GSC validation, open decisions.
- The repo (`stillcasting/`, branch `develop`) has an **auto-commit hook** (commits show as "claude: <timestamp>").
  A trial implementation was made and reverted once via `git reset --hard` to the pushed commit.
- Deploy policy: dev/staging auto-deploy OK; prod only on explicit instruction.
