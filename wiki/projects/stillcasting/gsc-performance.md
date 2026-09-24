# Search Performance (GSC) + Traffic/Revenue Model

Purpose: the Search Console metrics timeline, diagnosis, and the traffic/ad-revenue forecast.
Status: property is ~15 weeks old; **site is effectively deindexed by Google since 2026-07-15** (see 2026-09-24 analysis). Last-verified: 2026-09-24.
GA4 property id: `365602077`. API access: service account (see [[access]]); pull script `bin/gsc-ga4-pull.py OUT_DIR`.

## Property
- `sc-domain:stillcasting.app` (Domain property → all subdomains incl. `dev.*`). Added ~2026-06-08.
- GSC does not backfill: data begins at verification. **API connected 2026-09-24** (read-only service account, key in `.secrets/`).

## Metrics timeline (dated series — do not overwrite, append)
| As of | Window | Impressions | Clicks | Avg CTR | Avg position |
|---|---|---|---|---|---|
| ~2026-06-16 | week 1 | ~231/day | 1–3 | 0.2% | 51.5 |
| 2026-07-12 | 5 wks (cum.) | 6.18k | 18 | 0.3% | 51.5 |
| 2026-08-07 | 9 wks (cum.) | 6.66k | 21 | 0.3% | 50 |

Daily shape: impressions rose and *accelerated* to a peak ~380/day around 2026-07-08…12,
then **collapsed ~2026-07-14 to ~10–30/day** and stayed low through August. Clicks always
0–3/day (noise-level).

## Core diagnosis
- **CTR is a function of position, not snippets.** Avg position ~50–51 = page 5–6. Expected CTR
  at that depth is ~0.1–0.3%, so 0.2–0.3% is *on-curve* — there is **no snippet/title problem** to fix yet.
  Headline work ([[proposals]]) only pays once pages reach page 1.
- **Why (almost) no clicks:** (1) 2-month-old domain, ~zero authority → ranked deep; (2) competing with
  Wikipedia / IMDb / Google Knowledge Panel for person queries; (3) many "is X alive / how did X die"
  queries are **zero-click** (answered in the SERP). Individual obscure-person pages are zero-volume or
  zero-click; they are crawl-surface, not traffic.
- **Winnable, click-hungry intent:** hub/list pages (`/legends` "oldest living actors", `/died-this-week`,
  milestones) and "[movie] cast still alive / where are they now" title pages. `/legends` was the top
  page and grew 41 → 102 impressions WoW (+149%) — first proof the hub thesis is correct.

## The mid-July impression drop (analysis, unconfirmed)
Site verified **healthy** 2026-08-09 (no robots block, all key pages 200 + content + `index`, sitemap grew).
So the drop is demand/indexing-side, not a breakage. Signals: clicks did **not** fall (18→21) and position
**improved** (51.5→50) → the lost impressions were low-position, non-clicking **junk**. Most likely causes:
1. The thin-page/soft-404 **cleanup** taking effect (Google dropped noindexed pages) → their scattered deep
   impressions vanished. See [[seo-indexing]].
2. **dev.stillcasting.app** deindexing lowering the Domain-property aggregate (if locked mid-July).
3. Normal **new-site "honeymoon" correction** (initial over-showing settles to a true baseline).
To confirm: GSC → Pages, compare impressions before/after 2026-07-14, sort by biggest loss (dev.* → #2;
thin `/persons/*` → #1; broad/uniform → #3). And: what deployed ~2026-07-14? (open question)

## Traffic model (estimate, no GSC/authority data)
Power-law; a few thousand famous entities + hubs carry it. Scenarios (organic sessions/mo at maturity):
- Conservative (ramp): 15k–40k · Base (well-indexed): **80k–180k** · Optimistic (authority): 250k–450k.
- **Event-driven**: a single A-list death can drive 50k–300k searches in a week across the person + co-star
  + died-this-week cluster. Traffic is spiky; plan on annual average. Currently at the very start of the ramp.

## Ad-revenue model ("moderate ads")
- Session RPM by scale: AdSense ~$4–8 → Mediavine (≥50k) ~$8–15 → Raptive (≥100k PV) ~$12–20.
- Base traffic ≈ **$1k–3k/mo**; mature ≈ $3k–9k/mo. Discounts: **death-content brand safety** (−15–30%),
  international-traffic dilution, "moderate" density trade-off.
- Blocker: current **CSP** (`default-src 'self'`, script-src self+GTM/GA only) **blocks third-party ad tags** —
  monetizing requires deliberately loosening CSP.
- AI-citation reach monetizes poorly (zero-click) — display revenue tracks clicks, not citations.

## What to watch (not daily)
Average **position** trend (should fall from ~50 as winnable pages climb), impressions *composition*
(hubs vs long-tail), Soft-404 ↓ / Excluded-by-noindex ↑. Ignore day-level clicks/CTR — noise.

## 2026-09-24 — API analysis: the July drop is a deindexing, not a demand change
Data: `bin/gsc-ga4-pull.py` (raw JSON kept in the session scratchpad; re-pull any time).

**Timeline (web impressions/week):** 1,393 (Jun 8) → 1,605 (Jul 6) → 610 (Jul 13) → 86 (Jul 20) → 47–77 (Aug) → 14 / 10 / 3 (Sep).
Day-level: 300 on Jul 13, 196 on Jul 14, **40 on Jul 15**, ≤30 since. Clicks were never more than 0–3/day.

**What Google's index says (URL Inspection API, 83 URLs):**
| Sample | Indexed | Crawled – currently not indexed | Unknown to Google |
|---|---|---|---|
| Homepage | 1 | – | – |
| 11 hub/list pages (/legends, /milestones, /died-this-week, /deaths/*, /cause*, /statistics, /about…) | 0 | 5 | 6 |
| Top-14 pre-drop pages + top-8 current pages | 1 (piranha-3d) | 21 | 0 |
| Top-25 persons by TMDb popularity | 0 | 3 | **22** |
| Top-25 titles by popularity | 0 | 9 | **16** |
Last crawl of the demoted pages: June–early July (legends Jul 8, died-this-week Jul 10, godfather Jul 9, stallone Jul 29). Google stopped
crawling almost everything around the drop and has not returned; only the homepage is re-crawled (Sep 22). Hub pages like /statistics and
/cause were **never** crawled. Fetch state SUCCESSFUL, robots ALLOWED, canonicals fine → not a technical block: a **site-level quality
verdict** ("crawled – currently not indexed" at scale = programmatic pages judged not worth indexing on a domain with ~no authority).

**Composition of the lost impressions:** 89 % came from queries at position >30; before the drop 1,694 distinct queries / 1,384 pages,
after: 160 / 333, now: 12 / 57. Top loser was `/persons/roger-coggio` (pos 1 for "roger coggio death cause cancer", 266 → 35 → 0) and
"[film] cast" queries at position 80–90 (mummy, conjuring, high noon, wizard of oz…). Countries fell uniformly (USA 1,864 → 257).
Image/News/Video/Discover: ~zero throughout. Sitemap index: accepted, 0 errors, last downloaded 2026-09-18, but GSC reports no child counts.

**GA4 vs GSC — no contradiction, two different things:**
- "Organic Search" in GA4 (≈420 users since June) is **Bing 223, Yahoo 99, DuckDuckGo 51, Google 29**. Bing/Yahoo/DDG still index the site;
  Google barely does. Those are real, engaged visitors (avg 150–190 s).
- "Direct" (3,800 users) is **bots that execute JS**: Hong Kong/China/Singapore desktop Chrome, 0–1 s sessions, 3,526 distinct landing pages,
  2,338 in the week of Sep 21 alone. Real direct traffic is ~US/NL desktop, a few dozen users. GA4 "active users" is therefore ~90 % noise.
- Real human audience ≈ 5–8 sessions/day.

**Edge findings the same day:** ClaudeBot (allowed at the edge since v1.267.36) crawls at ~300 req/min (32k requests in 1.6 h, a third of
them /api/media images); load stayed < 3, backend fine. Real Googlebot: 3 requests in the same window. Backend container restarted cleanly
(exit 0, no OOM) at 2026-09-22 05:48Z — cause unknown, harmless.

**What would change the picture (proposal, not started):**
1. Stop asking Google to index 160k pages. Submit a curated sitemap: hubs + a few thousand titles/persons that have real unique content
   (deaths, bios, survivorship prose); leave the rest crawlable but out of the sitemap (or noindex). Google must see a small, high-quality site first.
2. Get the hubs discovered: internal links from the homepage to every hub (several are "unknown to Google"), and request indexing for them.
3. Authority: a handful of real backlinks/mentions; without any, "crawled – currently not indexed" will persist regardless of content.
4. Optional: throttle ClaudeBot (`Crawl-delay` in robots.txt; Caddy has no rate-limit module in the stock image) and drop JS-executing
   scrapers from GA4 (filter by country/engagement) so Analytics reflects humans.
