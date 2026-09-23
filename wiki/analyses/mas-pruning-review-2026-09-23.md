# MAS pruning review — what to cut, fix, keep

Fresh look at code + prod data. `Last-verified: 2026-09-23` (code `v1.2.0`; prod DB; logs since 2026-09-22 10:08).
Related: [[functionality-map]], [[signal-quality]], [[earnings-scoring]]. Status: proposal, nothing changed yet.

## Evidence (prod)
- Signal edge (signals view ⨝ signal_outcomes, beat-SPY rate / median abnormal return):
  - news_research WATCH n=467: 5d 42% / −1.5%, 21d 32% / −5.9%. BUY n=49: 21d 33% / −5.6%.
  - news_research_rejected WATCH n=530: 21d 44% / −1.7% → the critic's rejects beat its picks (critic inverted).
  - portfolio_monitor HOLD n=1,525: 21d 43% / −0.2% (neutral). REDUCE n=193: 5d 34% beat (i.e. REDUCE right ~66%).
  - research (weekly) and hypothesis: n ≤ 53 — too small to judge.
- Calibration map: News Research medium p_up 0.37 (n=251) vs low 0.57 (n=162) → confidence labels run backwards.
- Earnings: 201 graded, 58.2% overall; by month 55→58→63%. WATCH down 63% (n=144), WATCH up 47% (n=55).
- News research: 88/124 runs in 60d had zero signals (71%); 15:00 run 43/61 zero.
- Monitor: rating changed in 70/1,037 decisions (6.7%); weekends 9.6% vs weekdays ~5% → weekend changes are model noise.
- Weekend runs in 60d: news 36, monitor 18.
- Cost per run (60d avg LLM calls): earnings 57.7, research 51.3, news 17.9, monitor 17.7.
- Accumulator (29h of logs): broad sweep 116×, 42,176 fetched → 953 new, ~1 LLM filter call per sweep (~96/day, outside
  run budgets). Gap-fill 175×, 350 targets → 1 ingested. Scout requests: 2 fulfilled of 125.
- performance_cache (built by performance.py from Google Sheets `signals_data`) shows Portfolio Monitor avg_ar5 = 687.85
  — garbage; and it feeds prompts (rank/gate/rerank/critic, monitor context) + dynamic frame rejection.

## Remove (dead code, no behaviour change)
AgentMail (`tools/agentmail.py`, `agents/research/email_reader.py`, `agentmail` dep, `AGENTMAIL_*`); `tools/news_meta.py`
+ `upsert_news_meta` (disabled 2026-06-23); Track A `generate_news_directives` + `NEWS_DIRECTIVE_SYSTEM`; portfolio
`delta_mode` branches; 10 dead DB functions (incl. `add_manual_lot` unless the RSU command is built); dead config
(`planner_max_calls`, `reflection_max_rounds`, `pm_max_calls`, `tavily_results_per_query`, `search_request_timeout`);
`planner_system`/`build_commodity_analyst_system` duplicates; redis limiter stub; `scripts/push_prompts_to_hub.py`
(LangSmith, old-Mac path); `deploy.sh` (CI replaced it; hardcoded Serper key); earnings `_DECISION_ROLE` TRIAL note.

## Stop (runs with no payoff)
Weekend news + monitor runs; 15:00 afternoon job (news + full monitor); accumulator gap-fill + scout-request loop.

## Fix
performance_cache → compute from signal_outcomes, stop reading Sheets (then Sheets writes can go once research/Track C
stop-target levels get DB columns); invert/retune news critic; confidence labels; stale portfolio (last import 2026-07-20).

## Proposed schedule (CET) — ~54% fewer scheduled LLM calls (~1,470 → ~680/week)
Mon–Fri: 07:15 earnings watch · 07:30 event calendar · 08:00 portfolio monitor · 09:00 news research ·
hourly 09–22 earnings score (no LLM) · 18:00 outcomes + calibration · accumulator broad sweep every 30 min 06:00–22:00.
Weekly: Mon 06:30 static research. On demand: all Telegram commands incl. /hypothesis. Nothing on weekends.
