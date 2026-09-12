# Log

Chronological, append-only. Newest at top. Per `schema.md`.

## 2026-08-26 — Infra incident: /data 100% full → Kasm down + workers down
`/data` (Docker data-root, 74GB) hit 100%. Cause breakdown: media 29GB (stillcasting_media_data) +
unrotated logs ~17GB (caddy 8.5 + backend 4.9) + financial-mas images 11.7GB (prod+staging) + staging
media 6.5GB. Effects: kasm_db/api crash-looped (Kasm down → Chromium can't launch); stillcasting-worker-1
& worker-images-1 EXITED 08-25 21:51 (data pipeline stalled ~14h). Fixes: truncated logs (freed 17GB→80%),
restarted kasm control plane (all healthy) + workers (processing again). OPEN: (1) no Docker log rotation →
will refill; (2) Kasm has NO workspace registered (registry NaN/empty) → still need to add registry +
install kasmweb/chromium:1.15.0; (3) staging-media 6.5GB + financial-mas 2-copy 11.7GB reclaimable.

## 2026-08-28 — PROD DB OUTAGE: /data refilled to 100% → postgres death-spiral
Symptom: site DB-backed pages 404, backend "database system is not yet accepting connections".
Cause: /data (74GB) hit 100% again (~2h after prior cleanup). At 100%, postgres can't write → spams
errors into its own json.log at ~4GB/hr → keeps disk pinned → can't recover. Trigger: restarted workers
churning 14h backlog (media downloads + activity) + unrotated logs. Stabilized: truncated logs (freed
~5GB, 98%), STOPPED workers (worker/worker-images/backfill/beat) → postgres back accepting connections,
logging ~0 now (confirmed log_statement=none; the 4GB/hr was pure disk-full spiral). ROOT: 74GB volume
chronically full — 68GB all real data (media 35GB, in-use images 20GB incl. financial-mas ×2 = 11.7GB,
chromium 2.6GB, DB 3GB); nothing prunable. Only ~1.9GB free. WORKERS LEFT STOPPED (data updates paused).
DECISIONS PENDING (asked user): (1) EXPAND OCI /data volume [real fix]; (2) interim ~9GB reclaim = clear
staging media 6.5GB + rm chromium image 2.6GB; (3) Docker log rotation (needs daemon restart); (4) does
financial-mas staging need this box. Do NOT resume workers until headroom exists.

## 2026-08-26 — Tim Curry death recorded + Bob Caudle date fixed
Tim Curry: user reported death; VERIFIED real (Wikidata P570=2026-08-25 Q52392 + Wikipedia Deaths_in_2026
+ THR). Ran check_wikipedia_deaths_task → now deceased 2026-08-25 (id 10996). (Post-cutoff event; verified
via sources not memory — correct process vs asserting.) Bob Caudle (id 467000): TMDb deathday=2026-11-16
(future, wrong YEAR); real = 2025-11-16 age 95 (Wikidata 2025-11 + web). Corrected → 2025-11-16. Future-
dated deaths now = 0. Death caches flushed. 3rd TMDb bad-date (Marinos, Caudle) — scanner future-date guard
would auto-catch but BLOCKED by broken deploy pipeline (see below).

## 2026-08-26 — Kasm FIXED + content fixes + DEPLOY PIPELINE BLOCKER
KASM: root cause = Chromium workspace WAS registered (kasm images table, enabled/available) but its Docker
image was missing (couldn't pull on full disk) + control plane crash-looped. Fixed: freed disk, restarted
control plane (healthy), `docker pull kasmweb/chromium:1.15.0` (2.64GB). Should launch now.
CONTENT (visible fixes, prod, no deploy): Marinos widget cleared (recreated prod frontend → dropped stale
ISR); Bertín Osborne 1923 credit deleted (span fixed, earliest now 1963).
⚠️ DEPLOY PIPELINE BROKEN: dev.stillcasting.app (runs `develop`) serves 200/**0 bytes** → develop is NOT
safe to deploy to prod. This BLOCKS all durable code fixes (scanner future-date guard, display guard,
force-dynamic, and the needed career-span plausibility guard). Systemic content issues remain unfixable
until the pipeline is repaired: 32,041 impossible credits across 23,423 persons (credit predates birth);
48k unverified wiki photos. Disk now 85% and climbing (chromium pull) — log rotation still unconfigured.

## 2026-08-26 — Data bug: impossible career spans ("Careers Across Generations")
Bertín Osborne (id 38019, DOB 1954, living) shown with "103-year career" — record has junk TMDb credits
predating birth (M'Lord of the White Road 1923, Psycho 1960, etc.). "103 YEARS" = span earliest→latest
credit. Also Fredrick Lewis "88 years" (1922→2010). Root: feature has NO plausibility guard + TMDb junk
credits (same-name conflation). Fix: (quick) exclude credits where title.year < birth_year + cap span to a
lifespan; (root) credit validation (§3). Same data-integrity family as Marinos date / Franke photo.

## 2026-08-09 — Wrong wiki photo (visitor report) + 48k exposure
Visitor Lynn: `/persons/anthony-franke` showed Anthony Franciosa's photo. Confirmed DIFFERENT people
(Franke = obscure Blob-1958 actor, no photo on TMDb; Franciosa = famous 1928–2006). Wiki-photo scanner
name-matched to wrong entity (no wikidata verification). Fixed on prod: cleared `wiki_profile_path_local`
for id 220688 (reversible). Systemic: 48,009 persons have a wiki photo but no wikidata_id (unverified
matches, not all wrong). Root = §3 record-linkage gap. → [[wiki/pipeline-science]] §3. Reply drafted for Lynn
(NOT sent — needs user to send). Open: add entity-verification to wiki-photo scanner; audit the 48k high-risk subset.

## 2026-08-09 — FIX shipped (develop): future-deathday guard in TMDb scanner
`scanner_service.py`: reject `detail.deathday > date.today()` (log + ignore) so an impossible/future
TMDb deathday can't flip a person to DECEASED. Added logger + 2 tests (test_sc1203) — all 16 pass.
NOT yet: (a) existing bad rows still need a data fix (`UPDATE persons SET date_of_death='2026-03-10'
WHERE slug='giorgos-marinos'`; `SELECT ... WHERE date_of_death > CURRENT_DATE` to find others — guard
doesn't heal existing rows); (b) prod deploy of this + display guard 05820b9 (deploy policy = manual);
(c) same guard on worker Wikidata/Wikipedia death paths (defense-in-depth); (d) §2 reconciliation.

## 2026-08-09 — Giorgos Marinos wrong date: SOURCE TRACED to TMDb
Confirmed origin of `2026-10-03`: **TMDb `deathday` field** for person 1455489 = a DD/MM↔MM/DD
transposition of the real 2026-03-10 (TMDb's own bio prose says "March 10, 2026"). `scanner_service.py:95`
ingests TMDb `deathday` verbatim → DECEASED. **No swap bug in our code**; bad upstream TMDb data.
Wikidata `P570 = 2026-03-10` (correct) — sources disagreed, nothing reconciled them. NOT the Wikipedia
death page; death data is multi-source (TMDb primary). Real fixes: §6 future-date guard + §2 cross-source
reconciliation. Corrects user assumption of "one source = wiki death page". → [[wiki/pipeline-science]] Case 2.

## 2026-08-09 — Data bug: future death date (Giorgos Marinos) + ROOT CAUSE
`/persons/giorgos-marinos` stored `date_of_death = 2026-10-03` (future) → marked Deceased, top of
"Remembered This Week". Root cause traced (two layers):
(1) DISPLAY: `died-this-week` guard `<= CURRENT_DATE` exists on develop since commit 05820b9
    (2026-07-09) but is **NOT deployed to prod** → prod widget + /died-this-week still leak it (confirmed live).
(2) DATA: 05820b9 patched the query only, not ingestion. Record still wrong; person page shows
    "How Did Giorgos Marinos Die?". No guard rejects future dates at write. Bad source or DD/MM↔MM/DD swap.
Fixes: deploy develop→prod (quick); §6 anomaly guard at ingestion (root); `count(*) where date_of_death
> CURRENT_DATE` to size. Team is patching symptoms not root — reinforces [[wiki/pipeline-science]] §2/§6.

## 2026-08-09 — Wiki seeded
Created the StillCasting wiki (Karpathy LLM-Wiki pattern) from the 2026-06-06 → 2026-08-09 SEO session.
Entries: `seo-indexing`, `gsc-performance`, `proposals`, `pipeline-science`. Sources catalogued.

## 2026-08-09 — GSC: mid-July impression drop investigated
9-week data: 6.66k impr, 21 clicks, CTR 0.3%, avg position 50. Daily impressions collapsed ~2026-07-14
(~300 → ~10–30/day), sustained. Live-site health check: PASS (no robots block; homepage/hub/person/title
all 200 + content + `index`; sitemap grew to ~162,591). Conclusion: not a breakage; lost impressions were
low-value (clicks held, position improved). Likely = cleanup + possibly dev deindex + honeymoon correction.
Unconfirmed — needs GSC Pages before/after diff + "what deployed ~07-14". → [[wiki/gsc-performance]]

## ~2026-07 — dev.stillcasting.app exposure found
`dev.*` publicly indexed ("indexed without content"): 200/0-byte/no-auth/no-noindex/serves sitemap.
Recommended Caddy basic-auth + `X-Robots-Tag: noindex`. Domain property means dev affects prod's reports. OPEN.

## ~2026-06-21 → 2026-08 — Person soft-404 fix shipped & verified
~12,500 person pages were Soft 404 (thin: 125–161 words, no filmography/bio). Proposed + shipped
`person_is_indexable` gate; verified live (thin → `noindex`+desitemapped; Stallone → `index`). GSC
Soft-404 validation started (12,500→9,894). Duplicate-canonical 260 = stale numeric-ID URLs, self-resolving.

## ~2026-06 — GSC property added; baseline diagnosis
Domain property `sc-domain:stillcasting.app`. Established: avg position ~51 = page 5–6 → 0.2–0.3% CTR is
on-curve (position problem, not snippet). Winnable intent = hubs + cast pages (`/legends` grew 41→102 WoW).

## 2026-06-06/07 — Indexing + headline proposals
Title indexing "popularity exception" → shipped as `title_is_indexable` Phase 2 (floor 20). Person headline
`personHeadline()` shipped. Title "How Many…" headline approved (v2, 2 reviews) but blocked on design mockup.
Trial impl of title indexing was auto-committed by the repo hook, then reverted via `git reset --hard`.

## 2026-06-05 — SEO audit
Full audit (`stillcasting_seo_audit_2026-06-05.pdf`). Health ~83–90/100. Strong technical baseline; main
debt = programmatic thin-content on title (then person) pages.
