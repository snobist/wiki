# MAS change proposal — prioritised

Consolidates [[mas-pruning-review-2026-09-23]], [[mas-news-collector-review-2026-09-23]], [[jev-laya-for-mas-2026-09-23]].
`Last-verified: 2026-09-27` (prod unchanged since v1.2.0; portfolio still 2026-07-20). Status: proposal, awaiting Alex.

## P0 — stop being misled (now)
1. Re-import the portfolio (IBKR Flex CSV via /update_portfolio) — Alex, no code.
2. performance_cache: rebuild from signal_outcomes (DB), stop reading Sheets. Today it tells the agents the Monitor averages
   +687 excess return; feeds rank/critic/rerank/monitor prompts + frame rejection.
3. News Research → shadow (log, don't send to Telegram) until the critic is fixed. Picks beat SPY 32–33% at 21d, median
   −5.6 to −5.9%; the critic's rejects do better (44%, −1.7%).

## P1 — cut waste (release v1.3.0, low risk)
4. Schedule: weekdays only; remove 15:00 job; collector every 30 min 06–22; remove gap-fill + scout loop. ~−54% LLM calls.
5. Collector: pipelines read cache (no re-fetch); drop LLM relevance filter (passes 71%); drop CNBC Earnings (dead since
   2026-09-17); store RSS dates as ISO.
6. Delete dead code (AgentMail, news_meta, Track A directives, delta_mode, 10 DB fns, 5 dead settings, duplicate prompt
   builders, redis stub, push_prompts_to_hub.py, deploy.sh). Alex rotates the Serper key.

## P2 — improve signals (v1.4.0, all in shadow first, judge after 3–4 weeks)
7. Critic: flip/retune; replace high/medium/low labels with calibration_map p_up.
8. Clustering: merge same story (title near-dup + shared entities); require a 2nd source for Energy Storage News,
   SpaceNews, Utility Dive, Resource World candidates.
9. Earnings = the product that works (58%, rising 55→63%; down calls 63%, up calls 47%). Publish down calls, treat up
   calls as info-only; run the Laya-on-earnings-history experiment.

## P3 — tidy
10. /add_rsu + /rsu + /remove_rsu, or delete add_manual_lot. 11. Retire Sheets fully after DB columns for research/Track C
stop-target levels. 12. Log strings naming old models. 13. EDGAR: broaden to all material 8-K items or drop.

## Decisions needed from Alex
News Research → shadow? · RSU command or delete? · Keep Sheets writes for now? · Go for v1.3.0 (P0.2 + P1)?
