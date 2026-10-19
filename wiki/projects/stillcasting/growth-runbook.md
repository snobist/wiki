# stillcasting — growth run (scheduled every 2 days)

Purpose: the procedure the scheduled Claude task `stillcasting-growth` follows. Fresh session each run; everything it needs is here.
Owner: Alex. `Last-verified: 2026-10-06`. Reports land in `wiki/analyses/stillcasting-growth/YYYY-MM-DD.md`; summary line in [[log]].

## 0. Ground rules (hard)
- Read [[index]] → [[overview]] → [[conventions]] → [[stillcasting-index]] → [[gsc-performance]] → the previous report in
  `wiki/analyses/stillcasting-growth/` before doing anything.
- **One change per run at most**, small (≈ ≤150 changed lines), from the ALLOWED list; **no change is a valid outcome** — report only.
- ALLOWED: SEO metadata/structured data, internal linking, hub-page content, sitemap composition (`title_service.get_curated_sitemap_titles`,
  `frontend/src/app/sitemap.ts`), `robots.ts` (incl. Crawl-delay for AI bots), frontend rendering/performance bugs, accessibility, analytics tagging.
- FORBIDDEN: production DB writes (no UPDATE/DELETE/INSERT), Caddyfile / compose / nginx / server config, deleting files on the box,
  auth or security code, the image/download pipeline, payments/ads, the Wikipedia deaths checker, anything touching persons' death data.
- Deploy only if the backend suite AND the frontend build pass on the box (step 4).
- Production data: the only allowed write is queueing a rescan for a flagged false death (section 2b); it uses the normal pipeline. Production images install with plain `pip` from
  pyproject (no lock file), so a new upstream release can break a deploy on its own — the test run is the only guard (SQLAlchemy 2.1 did this on 2026-10-06). Never deploy when the site is unhealthy (step 2).
- Auto mode may refuse a remote write: do not work around it; record "needed Alex" in the report and stop that step.
- Secrets: GSC/GA4 key at `.secrets/gsc-ga4-service-account.json`, OCI key `~/.ssh/oci-mas.key` (see [[access]]). Never print them.

## 1. Pull data (read-only)
```bash
OUT=/tmp/growth-$(date +%F); mkdir -p $OUT
python3 -W ignore ~/Documents/wiki/bin/gsc-ga4-pull.py $OUT          # GSC daily/pages/queries/sitemaps, GA4 channels/sources
```
Then URL-inspect (API `urlInspection/index:inspect`, siteUrl `sc-domain:stillcasting.app`) these 19: `/`, `/legends`, `/milestones`,
`/recently-deceased`, `/statistics`, `/cause`, `/cause/cancer`, `/spanning-generations`, `/died-this-week`, `/deaths/<current year>`,
`/born-in/1950`, and titles `the-godfather-1972-movie`, `star-wars-1977-movie`, `12-angry-men-1957-movie`, `psycho-1960-movie`,
`the-terminator-1984-movie`, `alien-1979-movie`, `the-good-the-bad-and-the-ugly-1966-movie`, `high-noon-1952-movie`.
Record coverageState + lastCrawlTime for each. Quota is 2,000/day; stay under 100.

## 2. Server health (read-only, over SSH; use `</dev/null` on docker exec, never `docker compose exec -T` inside `bash -s`)
`df -h /data` (alarm ≥ 80 %), `docker ps` (all stillcasting-* Up, postgres healthy), `uptime`, `curl -s -o /dev/null -w %{http_code} https://stillcasting.app/api/health`,
image worker outcomes `docker logs --since 48h stillcasting-worker-images-1 | grep -o "not_indexable\|'ok': True, 'path'\|no_free_photo_found" | sort | uniq -c`,
Caddy top user agents + top /16 networks (bots: ClaudeBot, PerplexityBot, GPTBot; scrapers: many IPs, Chrome UA, no `/_next/static` fetches).
If health fails → report only, no deploy.

## 2b. False-death audit (read-only, every run) — added 2026-10-18 after the Gal Gadot case
```bash
python3 ~/Documents/wiki/bin/stillcasting-false-death-check.py --days 14 --json /tmp/growth-$(date +%F)/false-deaths.json
```
Verdicts: `TMDB_RETRACTED` (TMDb dropped a death only TMDb ever gave us, Wikidata has none → vandalism), `WIKIDATA_MISMATCH` /
`TMDB_MISMATCH` (our date differs from the source), `NAME_TWIN` (same name died within 3 days on two records → one death, two records),
`UNCONFIRMED` (TMDb-only, Wikidata item exists but no death — fine for obscure people, suspect when popularity ≥ 5), `OK`.
What the run may do about it (this is the ONE exception to "no production writes", because it goes through the normal pipeline):
- `TMDB_RETRACTED`, `WIKIDATA_MISMATCH`, `TMDB_MISMATCH` → queue a rescan: on the box
  `docker exec stillcasting-worker-1 python -c "from stillcasting_worker.tasks import scan_person_task; scan_person_task.apply_async(args=[ID], queue='scans')" </dev/null`.
  The scanner (v1.267.53+) reverts retracted TMDb-only deaths and refreshes dates itself. Re-check after 60 s and report before/after.
- `NAME_TWIN` and popular `UNCONFIRMED` → report with both records' slugs for Alex; never change status or dates directly (no SQL, no PATCH).
- Also report anything with `date_of_death` in the future. Put a "False-death audit" table in the report even when everything is OK.

## 3. Assess (write the report first, then decide)
Metrics table, this run vs previous report: GSC impressions & clicks (last 7 days), avg position, pages with impressions; inspection sample:
indexed / crawled-not-indexed / unknown, URLs re-crawled since last run; GA4 **human** users (exclude channel Direct from China/Hong Kong/Singapore
and sessions with 0 s duration), organic by engine (Google/Bing/Yahoo/DDG), bot share; disk %, media growth; crawler request rates.
Then pick at most one improvement with a clear mechanism (e.g. hub never crawled → link it from a page Google does crawl; description duplicates;
missing JSON-LD; Crawl-delay for an AI bot exceeding ~5k req/h; a curated-set rule that admits junk). Write the rationale into the report.

## 4. Implement, test, deploy (only if a change was chosen)
Repo `~/Documents/Private_Projects/stillcasting`, branch `develop`; `git pull` first. Add/adjust a test. Then on the box, in self-cleaning
containers (clone `develop` to `/home/ubuntu/predeploy-test`, run backend `pytest` against throwaway `postgres:16-alpine` + `redis:7-alpine`
on a throwaway network with `TEST_DATABASE_URL=postgresql://postgres:postgres@postgres:5432/stillcasting_test REDIS_URL=redis://redis:6379/0
ADMIN_USERNAME=admin ADMIN_PASSWORD=testpassword123 JWT_SECRET_KEY=test-secret-key`, then `npm ci && npm run build` in `node:20` with
`NEXT_PUBLIC_BACKEND_URL=https://stillcasting.app/api`; `trap cleanup EXIT` removes containers, network, both images and the clone).
Green → `git checkout main && git merge --ff-only develop && git push`, tag `v1.267.<N+1>` (`git tag --sort=-creatordate | head -1`), push the tag.
Wait for prod HEAD to equal the tag and `/api/health` = 200 (≤ 20 min). Then `docker image prune -f; docker builder prune -af` on the box
(the hourly cron only prunes at ≥70 %). Verify the change live (curl as Googlebot smartphone UA). Red → do not deploy; leave the commit on
`develop` and describe the failure in the report.
Harness gotchas (2026-10-12): the backend tests import `stillcasting_worker`, so mount the whole clone and `pip install /repo/worker ".[test]"`
in `python:3.11-slim` (else every test errors at setup); containers write root-owned files, so `cleanup` must delete the clone via
`docker run --rm -v /home/ubuntu:/h python:3.11-slim rm -rf /h/predeploy-test` before removing the images; wait on `pg_isready`, not a fixed sleep.

More gotchas (2026-10-19): run the harness ssh with `-o ServerAliveInterval=20 -o ServerAliveCountMax=30` (an idle pytest phase dropped the connection once); full `npx jest` is green since v1.267.55 (run all suites, not a subset); Caddy is restarted not recreated by the deploy, so check `State.StartedAt`; scraper ranges blocked at Caddy: 202.46/16, 43.172/16, 43.173/16; GA4 human filter uses avg duration < 1 s (bots show 0.0x s).

More gotchas (2026-10-15): nothing after the image name in `docker run … postgres:16-alpine` (it becomes the postgres command → DB never starts, all tests error);
pre-pull images with `docker pull -q` so pull noise doesn't push the pytest summary out of `tail`; the deploy Action does `git reset --hard <tag>` ~3 min before
containers are recreated, so wait on the frontend container's `CreatedAt`, not `git describe`, and prune only after recreation.

## 5. Record
`wiki/analyses/stillcasting-growth/YYYY-MM-DD.md` (metrics table with deltas, findings, the change or "no change" + why, deploy tag, open items,
anything that "needed Alex"); add the page to [[index]] under Analyses on first creation; one `## YYYY-MM-DD — growth | …` entry in [[log]];
update [[proposals]] if a proposal shipped. `bin/sync.sh`. Finish with a 5-line summary for the notification.

## Known state 2026-10-06 (starting point)
- Google deindexed the site ~2026-07-15; curated sitemap live since 2026-09-24 (v1.267.37); Google re-crawled only `/` since. GSC ≈ 0–3 impressions/day.
- 2026-10-08: Alex manually requested indexing for `/statistics`, `/cause`, `/spanning-generations`, `/legends`, `/died-this-week` —
  next runs: check their lastCrawlTime/coverageState moved. Sitemap children show "Temporary processing error" / 0 discovered in GSC (files valid).
- (Gone as of 2026-10-06) GSC still lists a broken submission `sitemap.xml.` (trailing dot, 1 error) — Alex must delete it in the UI.
- Scrapers: 202.46.0.0/16 blocked at Caddy 2026-09-28; a rotating-IP Chinese scraper (≈850 fake GA "users"/day) and a residential-proxy
  HTML scraper remain; PerplexityBot ≈ 12k req/h, ClaudeBot bursts ≈ 20k req/h. Candidate first change: `Crawl-delay` for AI bots in robots.ts.
- Human traffic ≈ 5–10 sessions/day (Bing/Yahoo/DDG + a few from chatgpt.com).
