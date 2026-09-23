# MAS functionality map

What the system does, how each piece is triggered, and how much it is actually used.
`Last-verified: 2026-09-23` (code at `v1.2.0`; usage from prod `run_log`). Hub: [[financial-research-mas-index]].

One container runs three things: APScheduler jobs, the Telegram bot (`@alex_fin_agent_bot`), and the
FastAPI+HTMX dashboard (`portfolioview.stillcasting.app`, basic auth).

## Pipelines (run_log counts: all-time / last 30d / hand-triggered all-time, last hand-triggered)
| Pipeline | Trigger | Runs | Manual |
|---|---|---|---|
| News research — headlines → clusters → ToC supply-chain chains → candidates → critic → price levels | 09:00 daily, 15:00 daily, `/news_research` | 291 / 63 | 55, last 2026-09-16 |
| Portfolio monitor — per-position news + analyst + PM rating (HOLD/REDUCE…) + stop/target/trim | 08:00 Mon–Fri, 15:00 daily, `/research_portfolio` | 223 / 54 | 38, last 2026-09-16 |
| Earnings watch — top 5/day, next 3 business days; BUY/WATCH/SKIP + direction call | 07:15 Mon–Fri, `/earnings` | 68 / 22 | 5, last 2026-07-02 |
| Static research — your active prompts → planner → search → analyst → PM ranking | Mon 06:30, `/research` | 64 / 5 | 27, last 2026-06-22 |
| Hypothesis — cross-domain ideas + internet verification | `/hypothesis` only | 5 / 0 | 5, last 2026-06-19 |
| Portfolio delta (afternoon changed-only monitor) | retired 2026-06-23 | 38 / 0 | — |
"Manual" = run started off the exact minute (scheduled jobs fire at hh:mm:00.00x).

## Background jobs (no Telegram output)
- 18:00 daily: signal forward returns → `signal_outcomes`, calibration map rebuilt from DB, earnings outcomes, Sheets retrospective.
- Hourly 09–22 Mon–Fri: earnings score/freeze — locks the post-report reaction price per exchange.
- Every 15 min / 10 min: news accumulator broad sweep + gap-fill (on in prod via `ACCUMULATOR_ENABLED`; default off).
- 07:30 daily: event calendar refresh (IPO/dividend/split; on in prod via `EVENT_CALENDAR_ENABLED`).

## Telegram commands
`/start` `/status` `/research` `/news_research` `/research_portfolio` `/earnings` `/hypothesis` `/retrospective`
(forward returns + IC report) · portfolio: `/portfolio` (list + inline toggle/delete), `/update_portfolio` or just send a
`.csv` (IBKR Flex lot CSV; replaces IBKR lots only) · prompts: `/prompts` (inline toggle/delete), `/add_prompt`,
`/remove_prompt` · `/context` + send a `.txt` (supply-chain context docs) · `/reset_recent` (clear ticker suppression).

## Dashboard pages
Overview `/` · Signals `/signals` (+ detail) · Advice `/advice` · Runs `/runs` · Performance `/performance` ·
Calibration `/calibration` · Monitor `/monitor` · Portfolio `/portfolio` (Investments + Equity Compensation) ·
Earnings `/earnings` (paginated, 30/page) · News `/news` · Prompts `/prompts` (the only editable page).

## Data (2026-09-23)
1,009 earnings predictions · 3,356 signal outcomes · 2,680 PM decisions (494 in 30d) · 1,019 news signals ·
38 lots (35 IBKR, 3 ORCL RSU at Fidelity) · 50 watchlist · 4/4 prompts active · 123 critic scout requests.

## Dead / unwired code
- `add_manual_lot()` (database.py) — only writer for RSU/Equity Compensation lots; no command or page calls it.
- AgentMail inbox (`tools/agentmail.py`, `agents/research/email_reader.py`) — no caller; config vars still present.
- `delta_mode` in the portfolio PM — always False since the 15:00 job switched to the full monitor.
- Caddy has no access log for portfolioview, so dashboard page usage cannot be measured.
