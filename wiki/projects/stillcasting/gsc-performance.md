# Search Performance (GSC) + Traffic/Revenue Model

Purpose: the Search Console metrics timeline, diagnosis, and the traffic/ad-revenue forecast.
Status: property is ~9 weeks old, low authority. Last-verified: 2026-08-09.

## Property
- `sc-domain:stillcasting.app` (Domain property → all subdomains incl. `dev.*`). Added ~2026-06-08.
- GSC does not backfill: data begins at verification. GSC API **not connected** (no credentials) — all
  page/query-level analysis is still blocked; repeatedly the recommended next step.

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
