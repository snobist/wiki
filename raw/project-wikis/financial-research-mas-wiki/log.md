# Log

Chronological, append-only. Newest at top. Per `schema.md`.

## 2026-08-28 — CPU-torch images shipped; staging hazards found & fixed
Both images rebuilt on the CPU torch index: 5.96GB → **1.96GB each, layers shared;
11.72GB pruned** (disk 40%→40%, images now ~2GB of the box total). FinBERT verified
(torch 2.13.0+cpu). Side-discoveries while rebuilding staging: its compose named the
container `financial-research-mas` (prod's name — recreate collided, Docker's conflict
check protected prod) and its .env lacked TELEGRAM_ENABLED=false (defaults True → was
polling with the prod bot token). Both fixed; staging verified in silent mode.
→ [[wiki/infra-deploys]]

## 2026-08-09 — Docker image bloat diagnosed & fixed
MAS images were ~6GB each (2 images = 11.7GB = 73% of all image space on the box);
5.65GB was the pip layer, of which nvidia/ 2.9GB + triton 0.65GB — GPU libs pulled by
default aarch64 torch wheels on a GPU-less server. Dockerfile now installs torch from
the CPU-only index (expected ~2.4GB images). HF cache confirmed volume-mounted (clean).
→ [[wiki/infra-deploys]]

## 2026-08-09 — Wiki seeded
Created the financial-research-mas wiki (Karpathy LLM-Wiki pattern, same layout as the
StillCasting wiki). Entries: `signal-quality`, `earnings-scoring`, `infra-deploys`.

## 2026-07-20± — Earnings measurement corrected, history re-graded
Reaction baseline (`_pre_report_close`) replaced stale prediction-time ref; 20% of old
grades had the wrong sign (C: -4.7% "LOSS" was actually +0.7% up). 65 rows re-measured,
21 grades changed symmetrically (fake wins removed too: APOG, GS). Honest record
15/29 = 52%. Direction prompt reframed to expectations/positioning (beats predict
direction at 49%). → [[wiki/earnings-scoring]]

## 2026-07-15 — Direction gate shipped
WATCH direction calls suppressed (⊘) when the raw-direction bucket calibrates <50%
(up bucket was 36%, n=11 at the time). `raw_direction` column added so learning
continues on suppressed calls. → [[wiki/earnings-scoring]]

## 2026-07-14 — Decision-aware grading shipped
SKIP decisions and |move|<1% no longer graded; 20 historical rows unscored (15 SKIPs
incl. freebie wins like CNXC -20%, 5 noise-moves like SLP -0.1%). → [[wiki/earnings-scoring]]

## 2026-07-09 — Calibration contamination fix
`signals` VIEW splits critic-rejected news candidates into `news_research_rejected`.
"News Research high" calibration bucket had been 109/109 rejects. Clean rebuild left
one bucket: News Research medium n=38 @ 42%. Honest per-pipeline stats: nothing
credible; critic inverted (rejects beat accepts). → [[wiki/signal-quality]]

## 2026-06 → 07 — Context (pre-wiki)
DB-native calibration replaced Google Sheets (user directive). Broker/RSU portfolio
split, tooltip saga, WON/LOSS badges, EV-based BUY gate — see repo history and
memory files for detail.
