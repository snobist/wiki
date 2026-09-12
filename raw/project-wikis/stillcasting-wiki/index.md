# StillCasting Wiki — Index

Persistent knowledge base for **stillcasting.app** — a cast-survivorship reference
site (which movie/TV cast members are still alive). Maintained per `schema.md`.

Seeded 2026-08-09 from a long SEO/indexing working session (2026-06-06 → 2026-08-09).

## Project one-liner
Programmatic reference site: ~24.7k title pages + ~100k+ person pages (~162k total
sitemap URLs). Next.js App Router (ISR) behind Caddy/nginx. Data from TMDb +
Wikidata/Wikipedia, updated daily. Strong technical SEO baseline (security headers,
`llms.txt`, AI-crawler robots policy). Google Search Console property added ~2026-06-08
as a **Domain property** (`sc-domain:stillcasting.app`, covers all subdomains).

## Topic map
- [[wiki/seo-indexing]] — indexability system (title + person gates), soft-404 fix, sitemap, robots, dev-subdomain exposure, canonical/duplicate handling.
- [[wiki/gsc-performance]] — Search Console metrics timeline, the mid-July impression drop, position/CTR diagnosis, why-no-clicks, traffic & ad-revenue model.
- [[wiki/proposals]] — every change proposal from the session, with status (shipped / approved / proposed / blocked).
- [[wiki/pipeline-science]] — scientific upgrades for the data pipeline (actuarial survival modeling, Bayesian death fusion, record linkage) + the false-death data-integrity risk.

## Current state (as of 2026-08-09)
- **Shipped:** title indexability (`title_is_indexable` Phase 1+2), person indexability gate (soft-404 fix), status-aware person headline.
- **Approved, not shipped:** title-page "How Many … Still Alive?" headline (blocked on a design mockup).
- **Open / recommended:** connect GSC API (no keys yet); lock down `dev.stillcasting.app`; start backlink acquisition + tracking; verify the Marjane Satrapi false-death record; decide `MIN_CREDITS` for person gate.

## Top open questions
1. What caused the ~14 July impression collapse? (site is healthy — likely cleanup + honeymoon correction; unconfirmed) → [[wiki/gsc-performance]]
2. Which pages sit at position 11–20 (striking distance)? → needs GSC API.
3. Is the Marjane Satrapi "deceased" record a false positive? → [[wiki/pipeline-science]]
