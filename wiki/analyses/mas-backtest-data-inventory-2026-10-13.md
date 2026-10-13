# Data available for MAS system testing

`Last-verified: 2026-10-13`. Related: [[kaufman-tsam-review-for-mas-2026-10-13]], [[earnings-scoring]], [[signal-quality]].

## Internal (prod SQLite, point-in-time — what MAS knew at decision time)
- Signals 2026-05-20 → 2026-10-13: portfolio_monitor 2,304 (≈35 independent episodes after dedup), news_research 790
  + news_research_rejected 976 (natural A/B), portfolio_delta 323, research 94, hypothesis 14.
- signal_outcomes 3,791 (573 tickers): 5d/10d ~all, 21d 3,310; measured through 2026-09-25.
- price_targets 2,878 (stops/targets at decision time) → exit-rule tests possible.
- Earnings: 1,191 predictions, 371 unique events, 237 graded; 88 dossier snapshots (price, fundamentals, implied move,
  beat history, sentiment, bmo/amc).
- News text NOT archived: macro_news_cache keeps 7 days (4,591 rows); news_signal_log has tickers/frames/source names only.
- events (dividends/splits/IPOs, Massive) 2003–2027; portfolio_lots 38.
- Not stored: model/prompt version per signal; feature snapshot for monitor/news decisions.

## External (verified 2026-10-13)
- yfinance: ORCL daily bars since 1986 (10,225); hourly ~2 years (from 2023-11); earnings dates with EPS estimate/actual/
  surprise back to 2014 (50 quarters).
- Massive news API (key): ticker-tagged history — dense back to at least 2023, sparse before (ORCL ≤2020-06 returned 2019 items).
- Finnhub (free tier): company-news returned 0 for 2023-06 and 2025-06 (recent only); earnings surprises 4 quarters only.
- EDGAR full 8-K history (free). Search APIs (Brave/Tavily/Serper) unusable for backtests (today's results = look-ahead).

## What can be tested how
- Historical backtest OK: price/volatility rules (ATR stops, Efficiency Ratio, trend/breakout), post-earnings gap/drift
  rules (2014+ daily, 2023+ hourly), news-volume + FinBERT reaction rules on Massive history (2023+).
- Forward/shadow only: anything an LLM decides (earnings direction, critic, monitor ratings) — the model has seen the
  future in training (look-ahead). MAS's 5 months are the only valid sample; one regime, overlapping signals.
## Gaps to close now
Archive news (stop 7-day delete; ISO publish dates), feature snapshot per decision, model/prompt version per signal,
bmo/amc + reaction for all calendar earnings (not just top-5), fix RSS dates.
