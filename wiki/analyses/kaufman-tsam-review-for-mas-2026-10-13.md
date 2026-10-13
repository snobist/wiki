# Kaufman, *Trading Systems and Methods* (6th ed.) → MAS

Chapter-by-chapter review against MAS code + prod data. `Last-verified: 2026-10-13`.
Basis: official 24-chapter structure (Wiley 2019, 1,168 pp, ISBN 978-1-119-60539-3) + the book's well-known content —
NOT a page-level read (the link Alex sent was a pirated copy, not used; sub-section headings weren't publicly retrievable).
Related: [[mas-change-proposal-2026-09-27]], [[earnings-scoring]], [[private-investor-reporting-practices-2026-10-01]].

## MAS facts this is checked against
- Stops/targets are fixed %: research stop = max(−15%, 52w low+2%), target = analyst target or +25%; portfolio stop =
  max(−12% trail, −15% from cost), target +20% (`compute_mechanical_levels`). No ATR/volatility anywhere; no position
  sizing (only LLM `ai_units_to_sell`). Signals graded at fixed 5/21-day horizons, no exits. Never backtested; gates tuned
  on n≈30. Earnings ≈ always-down baseline; news picks trail SPY 68% at 21d.

## Chapter map (relevance → proposal)
- 1 Introduction — n/a.
- 2 Basic Concepts & Calculations — HIGH: add volatility (ATR, σ of returns) per ticker; express levels + alert thresholds in it.
- 3–4 Charting / Charting Systems — LOW (52w-low floor already used).
- 5 Event-Driven Trends (price swings/breakouts) — MED: rule-based breakout/breakdown alerts on holdings instead of LLM rating flips.
- 6 Regression — MED: slope + R² as trend-quality measure for holdings.
- 7–8 Time-based Trends / Trend Systems — MED: trend filter as a gate for long ideas — test first (above/below 200d MA showed no earnings effect).
- 9 Momentum & Oscillators — LOW–MED: features for testing only (momentum 43.8%, fade-run-up 55.8% on earnings).
- 10 Seasonality & Calendar — LOW for now.
- 11 Cycles — LOW.
- 12 Volume, OI, Breadth — MED: abnormal volume confirms news-driven moves; breadth for regime header.
- 13 Spreads & Arbitrage — LOW.
- 14 Behavioral Techniques (news/event trading, contrary opinion) — HIGH: trade the measured reaction with rules, time-boxed;
  test "fade MAS's own picks" as a contrary-opinion system.
- 15 Short-Term Patterns (gaps, reversal days) — MED–HIGH: earnings are gap events → gap-continue vs gap-fill rules (pairs with PEAD).
- 16 Day Trading — LOW.
- 17 Adaptive Techniques (Efficiency Ratio, adaptive MAs) — HIGH: Efficiency Ratio as noise filter for alerts; adaptive stops.
- 18 Price Distribution Systems (z-scores, skew, fat tails) — HIGH: alert when a move is > k σ for that ticker; stops/targets
  from the distribution, not fixed %; plan for fat tails (6% of earnings moves > 1.5× implied).
- 19 Multiple Time Frames — MED: confirm daily alerts with the weekly trend.
- 20 Advanced Techniques (ML/NN/GA) — caution: overfitting; keep LLM as feature extractor, decisions by simple tested rules.
- 21 System Testing — HIGHEST: build the harness — in/out-of-sample, walk-forward, parameter robustness, trade count,
  baselines (always-down, buy & hold, SPY). Gate every signal/alert.
- 22 Adding Reality — HIGH: costs, slippage, price shocks, execution timing, FX, 19% PL tax → evaluate net.
- 23 Risk Control — HIGH: volatility-based position risk, stops, max loss per position, drawdown rules, risk of ruin.
- 24 Diversification & Portfolio Allocation — HIGH for Alex: correlation, concentration (ORCL RSUs), allocation targets → IPS-lite.

## Top changes (order)
1. Ch 21–22 test harness with baselines + costs (prerequisite). 2. Ch 2/17/18 volatility units + Efficiency Ratio +
z-score alert thresholds (cuts noise). 3. Ch 23–24 portfolio risk layer (sizing, concentration, drawdown).
4. Ch 14–15 rule-based event trading in shadow (post-earnings gap rules, contrary test of MAS picks).
5. Ch 20: LLM reads, rules decide. Skip: 3–4, 10–11, 13, 16. Status: proposal.
For a page-level pass: legit copy via Wiley ebook, O'Reilly, Perlego/Everand trial — then read Ch 17, 18, 21–23 closely.
