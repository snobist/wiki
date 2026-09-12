# Earnings Prediction Scoring

Purpose: how earnings direction calls are graded, why the rules are what they are,
and the empirical findings behind them.

**Status:** active · **Last-verified:** 2026-08-09

## Grading rules (`app/tools/earnings_research.py`)
- **Decision-aware** (`_grade_direction`): SKIP never graded (its ▲/▼ was a forced
  convention); |move| < 1% (`_SCORE_FLAT_PCT`) never graded (noise). `correct` = NULL
  for unscored rows; all stats/calibration filter `correct IS NOT NULL`.
- **Reaction baseline** (2026-07 fix): outcome = `_pre_report_close` (last close
  on/before report_date) → `_post_report_price` (~30 min after first post-report open).
  The old scheme graded vs prediction-time `ref_price` (days early): **20% of grades
  had the wrong sign from pre-report drift** (C scored -4.7% LOSS when the true
  reaction was +0.7% up). All 65 historical rows re-measured 2026-07; record moved
  from apparent 39–47% to honest **15/29 = 52%**. BMO reporters collapse into the
  flat band (no bmo/amc hour stored — storing it would unlock same-day grading).
- **Direction gate** (`_gate_directions`): WATCH candidates lose the published
  direction (stored '', shown ⊘) when their raw-direction bucket's shrunk P(correct)
  < 0.50 (K=12, min_n=10, prior 0.52). `raw_direction` keeps the model's lean so
  calibration keeps learning from suppressed calls.
- **BUY gate** (`_calibrate_and_gate`): EV-based demotion BUY→WATCH; asymmetric on
  purpose (wrong BUY = realised loss; wrong WATCH = opportunity cost). One-way only —
  no promote path; with buckets below prior it would demote further anyway.

## Key empirical findings (2026-07, n≈60 measured)
- **~84% of companies beat consensus; of beats only 44% rose. "Will they beat?"
  predicts "will the stock rise?" at 49% — zero directional information.**
  The `_DECISION_SYSTEM` prompt was reframed (2026-07) to force expectations/
  positioning reasoning (run-up, implied move, revision direction). Whether that
  lifts accuracy above 50% is unproven — watch the scoreboard.
- Sell-the-news cases: AZZ, C — beat on numbers, stock fell; the model kept
  answering the beat question. Regime note: ~60% of reactions in the window were down.
- "Reaction history" (fell after last N beats) tested WEAK — skip as a feature.
- Small-n honesty: n≈30 cannot distinguish 47% from a coin flip (binomial p≈0.4).
  Proposed-but-not-built: numeric calibrated P(up) as the primary signal; CI display
  on the dashboard accuracy stat.

## Frozen-history policy
Grades are frozen once measured — EXCEPT when the grading rules themselves change;
then history is re-graded symmetrically (removes fake losses AND fake wins), as done
2026-07 for the SKIP/flat rules and the reaction baseline.

Related: [[signal-quality]], [[infra-deploys]]
