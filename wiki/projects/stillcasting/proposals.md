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

## Built, awaiting prod deploy
### Curated sitemap (2026-09-24, Alex's brief) — `develop` a15dce3 + 163c4f8
- Google deindexed the site ~2026-07-15 (see [[gsc-performance]]). Sitemap now = `/sitemap/0.xml` (home, hubs, 15 cause pages,
  `/deaths/{year}` with ≥25 deaths, `/born-in/{year}` with ≥50 indexable actors, 1900..today) + `/sitemap/1.xml` = top 1,500 movies by
  TMDb popularity with complete cast, ≥5 verified, ≥50 % deceased, poster present, not adult. Persons and the long tail stay
  "index, follow" but are not submitted. Backend: `/titles/sitemap/curated` (Redis 6 h), `/homepage/sitemap-years`; `Title.adult`
  (migration 0029) from TMDb on import.
- Meta validated on the set: 0 exact duplicates, 13 remake names → description now carries the year; 30 live pages sampled: all
  distinct titles/descriptions, index-follow. Titles are 66–148 chars (the approved "How Many … Are Still Alive?" pattern; long but distinct).
- After deploy (manual, GSC UI): resubmit `sitemap.xml`; URL-inspect → "Request indexing" for the hubs; watch Pages report weekly.
- Not in the set: TV series (cast rarely "mostly gone"); consider a series variant later. TMDb `adult` flag is rarely set on softcore
  Category-III style titles (e.g. Erotic Ghost Story III at rank 12) — a name/genre filter would be needed to drop those.

### Homepage "Careers Across Generations" — sort by actor popularity (requested 2026-09-14)
- Alex: "this guy has 2 appearances, so why should I care, while Mickey Rooney was really in a few famous movies".
  Example: Stan Alexander (Bambi 1942 → Once Upon a Studio 2023, 2 credits) ranks next to Mickey Rooney.
- Intent: order the section by actor notability (tmdb_popularity and/or credit count / known-for strength), not by span
  alone; consider a minimum-credits floor so archive-footage / cameo-only spans don't qualify. Backend: `homepage.py`
  spanning-generations query (commit a1d1869 already restricted it to "iconic films and real actors").
- Status: backlog for next iteration; not part of the 2026-09-14 bug-fix pass ([[stillcasting-bug-audit-2026-09-14]]).

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
