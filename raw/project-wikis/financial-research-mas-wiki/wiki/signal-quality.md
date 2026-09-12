# Signal Quality & Calibration

Purpose: what the pipelines' realised track records actually show, and how the
stats/calibration are kept honest.

**Status:** active · **Last-verified:** 2026-08-09 (data points dated inline)

## Data plumbing (how stats are computed)
- All performance/calibration stats come from SQLite (`signals` VIEW + `signal_outcomes`),
  never Google Sheets (user directive, 2026-06). `calibration_map` is wiped and rebuilt
  nightly by `update_calibration_map()` (DB-native, `app/tools/calibration.py`).
- The `signals` VIEW splits critic-rejected news candidates into pipeline
  **`news_research_rejected`** (2026-07-09 fix). Before that, 66% of "News Research"
  resolved stats were candidates never sent to Telegram, and the "News Research high"
  calibration bucket was 109/109 rejects (the critic labels confidence even on rejects).
  Same pattern as `hypothesis_rejected`. Do NOT re-blend them.
- Episode-dedup (7-day gap) collapses Portfolio Monitor/Delta daily re-ratings so one
  drawdown isn't counted N times (`_resolved_deduped`, `_episode_dedup`).

## Track record findings (2026-07, ~8 weeks of data)
- News Research (sent, n=61): hit5 39%, mean AR5 +2.4% but **median -2.1%** —
  a few outliers (WYFI +59%) carry many small losers. Decays by 10d/21d.
- News critic was **inverted**: rejected candidates hit 57% vs accepted 39% —
  rejected track kept as an A/B (`news_research_rejected`).
- Static Research (n=52): the only positive 5d pulse (64% hit, +4.4% mean, +0.5% median)
  but fully evaporates by day 10 → if used, mechanical ~5-day exit.
- Portfolio Monitor/Delta: ~zero alpha (as expected — they rate held positions).
- Hypothesis judge works directionally (9/9 accepted beat SPY; rejected -7.7%) but n tiny.
- Walk-forward backtests (2026-07): calibration gates reduce exposure but **cannot
  improve the win ratio** when the underlying signal is a coin flip. News numeric filter
  (p≥0.5) didn't help either (kept 37% vs dropped 43%, n small).

## Standing posture
Treat all discovery-pipeline output as paper-trading until a bucket earns credibility
(suggested bar: n≥50, positive median AR, hit rate meaningfully >50%). Nothing
qualified as of 2026-07.

Related: [[wiki/earnings-scoring]], [[wiki/infra-deploys]]
