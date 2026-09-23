# MAS news collector (accumulator) — how well it works

`Last-verified: 2026-09-23`. Data: prod `macro_news_cache` (7-day rolling), logs since 2026-09-22 10:08, `news_signal_log` ⨝
`signal_outcomes` (822 news signals incl. critic-rejected). Related: [[mas-pruning-review-2026-09-23]], [[functionality-map]].

## Works
- Reliable: 116 sweeps, 0 feed errors, 0 relevance-filter failures, 0 Massive rate-limit hits.
- Volume: ~650–730 new items per weekday, ~130–160 per weekend day; 4,310 items in the 7-day cache.
- Massive is the backbone: 1,627 of 4,310 items, freshest (avg 1.3 h from publish to fetch).

## Problems
- Relevance filter barely filters: 810/1,133 passed (71%); several feeds 100%. Real selection is BM25 vs the 4 active
  prompts + cluster scoring (8 of ~270 clusters researched per run). ~96 LLM calls/day for little.
- Pipelines re-fetch every source on each run ("356 fetched / 1 new") — the cache already has it all.
- Clustering doesn't group the same story: 300 items → 277 clusters. 902/1,031 news signals rest on one source.
  Corroboration helps only slightly (21d beat SPY 44% multi vs 42% single).
- CNBC Earnings RSS stopped publishing 2026-09-17 (source side). EDGAR 8-K keyword search: 9 filings/week, ~17.5 h late.
  Yahoo market news arrives ~14 h old.
- RSS `published_at` stored as raw RFC-822 text → can't sort or measure freshness for 18 of 21 sources (code orders by
  fetched_at, so nothing breaks).
- ~33% of items arrive 19:00–06:00 UTC; gap-fill ingested 1 of 350 targets.

## Source → signal outcome (21d beat-SPY rate, median abnormal return; includes critic-rejected)
Energy Storage News n=161 30% −7.1% · SpaceNews n=53 23% −6.8% · Utility Dive n=19 21% −4.0% · Resource World n=11 27% ·
Massive n=198 44% −1.2% · DatacenterDynamics n=74 43% −2.0% · Bloomberg n=113 52% +1.0% · Defense News n=34 68% +3.3% ·
Yahoo n=23 65% +2.9%. Likely sector drift (small-cap storage/space names fell), not source quality alone.

## Suggested
Pipelines read the cache instead of re-fetching; drop or replace the LLM relevance filter; drop CNBC Earnings; parse RSS
dates to ISO; merge same-story clusters (title near-dup + shared entities); down-weight or require corroboration for
Energy Storage News / SpaceNews / Utility Dive / Resource World candidates; broaden or drop EDGAR; sweep every 30 min
06:00–22:00 weekdays. Status: proposal.
