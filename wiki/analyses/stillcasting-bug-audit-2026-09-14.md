# stillcasting.app — bug audit 2026-09-14

Purpose: findings from a full assessment (live probes, prod DB/log queries via SSH, code review of `develop` @ f5a0f60).
Status: FIXES MERGED to `develop` 2026-09-14 (commit cc49224, branch `fix/audit-2026-09-14`) → staging auto-deploy; prod NOT deployed (needs a tag push). Prod data cleanup pending — see bottom. `Last-verified: 2026-09-14`. Raw diag: `raw/docs/stillcasting-diag-2026-09-14.txt`.
Hub: [[stillcasting-index]]. Related: [[pipeline-science]] (record linkage), [[seo-indexing]].

## A. Confirmed data-integrity bug — false deaths from the Wikipedia deaths checker (HIGH, recurring)
**Symptom** (Alex saw it on the homepage): two "Jeremy Thomas" entries in Remembered This Week.
- `/persons/jeremy-thomas` = id 321670, tmdb 2391998, no DOB, 1 credit, **death 2026-09-12** — a FALSE death on an obscure shell record.
- `/persons/jeremy-thomas-2` = id 326787, tmdb 3056, DOB 1949-07-26, Q1365966, death 2026-09-11 — the real producer (correct; marked by TMDb scan 2026-09-12 18:30Z).

**Root cause** — `worker/src/stillcasting_worker/tasks.py` `_find_or_create_person_from_wiki_entry` (~L1590-1720):
1. DB match is name-only (`name ILIKE` + also_known_as), filtered to LIVING/UNVERIFIED, unordered, first candidate wins.
2. The ±1-year birth-year gate is **skipped when the candidate has no DOB** → empty shells always pass. The producer (DOB 1949, in DB since 2026-06-10) lost to the shell.
3. TMDb fallback accepts first exact-name hit unverified when Wikipedia gives no age.
4. Prod log 2026-09-12 12:15:04Z: `Wikipedia deaths: marked Jeremy Thomas (id=321670) deceased dod=2026-09-12`.

**Why the dates differ**: Wikipedia revision history — entry added under `===12===` at 12:10Z, our hourly checker ran at 12:15Z, Wikipedia moved it to `===11===` at 17:28Z. Corrections never propagate because the snapshot key `wp_deaths_snapshot:{year}` is written *before* matching, so an article is never re-examined (also means unmatched entries are never retried, contrary to the code comment).

**Collateral**: name-based Wikipedia photo fallback (`download_wiki_photo_task` → `fetch_wikipedia_photo_by_name`, incl. OpenSearch fuzzy match) gave the shell the producer's photo (`Jeremy_Thomas_TIFF09-portrait.jpg`) — same mechanism as the Anthony Franke/Franciosa incident. SEO gate then flipped the shell to `indexable=True` (death date counts as a biographical anchor).

**Scale**: same pattern confirmed for Terence Donovan (shell id 31948, 1 credit, wiki-checker 2026-07-19; real one id 68771 b.1942 marked by TMDb 2026-07-20). In the last 90 days the checker wrote 254 deaths, **48 onto persons with no DOB**; ~10 of those have a same-name person with a DOB in the DB (tony-scott-2, john-douglas-2, dave-marsh-2, johnny-young-2, jeff-olson/jeff-olson-3, ricardo-pachon, barry-mitchell…). Query used:
`persons p where status='deceased' and date_of_death >= current_date-90 and date_of_birth is null and exists(status_provenance source_type='wikipedia_deaths_page')`.

**Fix direction**: require positive evidence (DOB within ±1y, or wikidata/imdb id); if only DOB-less candidates exist, fetch TMDb detail for them and gate; if >1 survivor, skip and log for review; drop the LIVING/UNVERIFIED filter (short-circuit "already deceased same DOD"); add snapshot only after a confident match; re-parse DOD for seen articles and update when Wikipedia corrects; photo fallback only via wikidata/wikipedia_url, never by bare name. Admin PATCH to `living` must also null death fields and recompute indexability (today it doesn't — `services/person_service.py`).

## B. SEO / crawl bugs (verified live)
1. **Titles sitemap is one file with 138,834 URLs** (`/sitemap/1.xml`, 26 MB) — protocol limit is 50,000 URLs/file. `frontend/src/app/sitemap.ts` chunks persons at 45k but puts all titles in id 1. Google will reject it.
2. **`public/robots.txt` shadows `app/robots.ts`**: lists only `/sitemap/0..4.xml` (index now has 0..8), never ships `Disallow: /import`, and `Disallow: /api/` blocks Googlebot from all images (`/api/media/...` is og:image + JSON-LD image). `next.config.js` persons-N rewrites hardcode 6 chunks; there are 7.
3. Duplicate brand in `<title>` (`… — StillCasting | StillCasting`) on deaths/[year], born-in/[year], cause, terms, privacy, not-found fallbacks.
4. og:url/og:title inherited from root on deaths/[year], born-in/[year], cause, search.
5. Sitemap omits `/deaths/{year}` and `/born-in/{year}`.
6. Titles marked dead via wiki-checker or IMDb sync **never get titles re-flagged indexable** (`tasks.py` ~L145-153 only recomputes when the status changed inside that scan) — news-traffic pages stay noindex.
7. `dev.stillcasting.app` on :443 still answers 200/0 B with no X-Robots-Tag (Caddy has only a `:8081` block for it) — known open item.

## C. Frontend bugs
1. `(main)/layout.tsx` awaits three fetches with no try/catch → any backend blip 500s every page incl. static ones.
2. Title pages with >100 cast SSR **zero cast rows** (`TitleCastWrapper.tsx`) while still shipping the full cast in the RSC payload (verified on doctor-who-1963-series: 1194 rows, 0 rendered).
3. Broken links: homepage `/titles`; `Nav.tsx` `/nationality/{slug}` (no route), years hardcoded 2020–2025.
4. Day-shift on client date formatting (`BornInYearClient.fmtDeathDate`, client `calcAge` in CastSection/NewSearch) for negative-UTC visitors; possible hydration mismatch.
5. `BornInYearClient` localStorage year overrides deep links to `/born-in/{year}`.
6. Title bio prints "(null)" when year is null; cast total omits presumed_deceased.
7. "How Did X Die?" answer not in SSR HTML when a bio exists (`PersonTabs` mounts only active tab).
8. Heavy polling: `DeathInfoSection` and `TitleCastWrapper` poll full person/title payloads (same class as fixed PR-08).
9. og:image is 185 px while declared 500×750.

## D. Backend / worker
1. `POST /import-jobs` unauthenticated, no dedup → queue flooding; re-import of a TV title can duplicate cast rows (credit dedup keyed on primary-role credit_id).
2. Cache-key flooding: unbounded `offset`, free-text nationality/cause, any `year`, unbounded search `q`; hard TTL up to 6 days.
3. `recover_orphaned_jobs` (every minute, 90 s window) + no claim step in `run_import_job` → same job can run twice; second run flips DONE→FAILED and skips post-import work.
4. Wikidata year-precision dates stored as 1 January (`raw[:10]`) → fake "died on this day" every Jan 1.
5. Person indexability not recomputed after credit inserts / `death_year` writes.
6. `import-filmography` resolves titles by natural slug, not tmdb_id → credits can land on a same-name/year title.
7. TMDb changes window advanced even when pagination failed.
8. `GET /search` writes to DB; concurrent identical queries can 500 on unique index.
9. Wiki re-scan churn: 45,361 deceased persons have `wikipedia_extract NULL` after a scan and are re-dispatched forever (3,782 in the last day; tmdb 2391998 queried 7× on 2026-09-14 within 2 h).
10. `docs/bugs/high.md` says SEC-04 fixed, but `import-filmography` is still unauthenticated by design comment.

## E. Infra state 2026-09-14
- `/data` 74 GB at **92 % (5.7 GB free)**; `/` 40 %. Workers ARE running (all prod + staging containers up 3 days; beat schedule active; cron: hourly disk cleanup, 5-min cache warm, hourly death_check.sh).
- Prod checkout has untracked stray files (`routers/scanner_service.py`, `routers/search_service.py`, `routers/tmdb.py`, `services/persons.py`, `connectors/persons.py`, root `Dockerfile`) — not in git; verify they are dead before the next deploy.
- `/sitemap.xml` returns 200 (the earlier 404 report from Cowork was the proxy).

## Suggested order
1. A (wiki-checker matching + snapshot + photo-by-name) and clean the ~10 wrong shells (set living, null death fields, drop wrong photo).
2. B1 (chunk titles sitemap) + B2 (delete `public/robots.txt`, fix rewrites) + B6.
3. C1, C2, D1, D3. Then the rest.

## Fix status (2026-09-14, same day)
Merged into `develop` (staging auto-deploys on push). Verified on the OCI box in throwaway containers: backend 349 passed,
worker 8 passed, `next build` OK. Prod deploy = tag push (`git tag vX && git push origin vX`) — not done.

Fixed: A (Wikidata-id resolution + evidence-gated name match + snapshot-after-match + date corrections + no name-based
photo + PATCH→living clears death fields + indexability recompute on wiki-checker/IMDb deaths), B1 (titles sitemap chunked,
new `/titles/sitemap?chunk=` + `/titles/sitemap/count`; ids now 0=static, 1..T titles, T+1.. persons), B2 (`public/robots.txt`
deleted, `robots.ts` allows `/api/media/`), B3, B4, B6, C1, C2, C3, C4, C6, C7 (utils.calcAge on date parts), C8, C9 (og:image
w500 + wording), D1 (import-jobs dedup + allowlist), D2 (offset/year/q caps), D3 (row lock + 15-min orphan window), D4, D5,
D6, D7, D11.
NOT fixed (next iteration): B5 (deaths/born-in years in sitemap), B7 dev.stillcasting.app :443 (Caddy change on the box),
C10 (death story not in SSR when bio exists), C11 (age-in-year sort), C12 (DeathInfoSection/TitleCastWrapper heavy polling),
C15 a11y, D8/D13 (search writes race), D9 (wiki re-scan churn), D10 (docs/bugs SEC-04 wording), E stray prod files, /data 92 %.

**Prod data cleanup — PENDING Alex's approval** (Claude Code's auto mode refused the remote write). Script:
`bin/stillcasting-revert-false-deaths.sh` — reverts the 5 shells verified against Wikidata (TMDb id of the real person differs):
jeremy-thomas 321670 (real 3056), virginio-gazzolo 368825 (real 103104, NOT in DB), dave-kendall 401991 (real 101826, NOT in DB),
jeff-olson 28721 (real 1426772 = jeff-olson-3), terence-donovan 31948 (real 75394 = terence-donovan-1942); creates the two missing
real persons as deceased with the Wikipedia date and queues their pipeline; deletes the two wrong portraits; refreshes caches.
Verdicts for all 48 suspects: `raw/docs/stillcasting-shell-verdicts-2026-09-14.json` (4 "shell is correct", 5 false, rest unverifiable).
Also to do on the box: `rm -rf /home/ubuntu/audit-test` (test clone) and `DROP DATABASE stillcasting_test` on the staging Postgres.
