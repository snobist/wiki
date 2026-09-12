# Sources

Raw inputs the `wiki/` entries were compiled from. Not rewritten — cited. Per `../schema.md`.

## Documents (ClaudeProjects root, `../../`)
- `stillcasting_seo_audit_2026-06-05.pdf` — original full SEO audit.
- `stillcasting_seo_change_proposal_2026-06-06.md` — title indexing exception + Person schema.
- `stillcasting_proposal_deceased_headline_2026-06-06.md` — person status-aware headline (shipped).
- `stillcasting_proposal_title_headline_2026-06-06.md` — title "How Many…" headline v2 (approved, blocked on mockup).
- `stillcasting_proposal_person_soft404_2026-06-21.md` — person indexability gate (shipped).

## Codebase (`../../stillcasting/`, branch `develop`)
- `backend/src/stillcasting_api/services/seo_service.py` — `title_is_indexable` (Phase 1+2), `recompute_title_indexable`.
- `backend/src/stillcasting_api/routers/persons.py` — sitemap endpoints; `get_person`.
- `backend/src/stillcasting_api/models/` — `Title.indexable`, `Person.indexable`, person columns.
- `frontend/src/app/(main)/titles/[slug]/page.tsx` — title page + `generateMetadata` gate.
- `frontend/src/app/(main)/persons/[slug]/page.tsx` — person page + `personHeadline()` + JSON-LD.
- `frontend/src/app/sitemap.ts`, `sitemap.xml/route.ts`, `robots.ts` — sitemap/robots.

## Live-site probes (curl, 2026-08-09) — captured in wiki entries
- robots.txt, sitemap counts (~162,591 URLs), homepage/hub/person/title HTTP+robots checks.
- Numeric-ID person URLs 308→slug. dev.stillcasting.app: 200/0-byte/no-auth/serves sitemap.

## GSC observations (screenshots relayed by user; no API export)
- Metrics series → `[[wiki/gsc-performance]]` table. Page-indexing report (Soft 404 12,500→9,894;
  Duplicate-canonical 260 = numeric IDs; Crawled-not-indexed 1,850; dev "indexed without content").
  `/legends` top page 41→102 impr WoW.

## External method reference
- Karpathy "LLM Wiki" pattern: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  (the pattern this wiki implements).

## Not yet available
- GSC API (no credentials) → no page/query-level position data. `sc-domain:stillcasting.app`.
- Backlink data (none configured). PageSpeed/CrUX field data (no API key).
