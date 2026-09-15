# financial-research-mas — project index

Async multi-agent system generating investment signals from news, earnings and portfolio monitoring.
`Last-verified: 2026-08-09`. Migrated 2026-09-12 from `~/Documents/ClaudeProjects/financial-research-mas-wiki`.

**Repo**: `git@github.com:snobist/mas.git` (private). Local clone `~/Documents/Private_Projects/financial-research-mas`
(cloned 2026-09-15). `main` is the live branch; `develop` had been stale since 2026-06 and was fast-forwarded to `main`
on 2026-09-15. Delivery = GitHub Actions: push `develop` → staging (`deploy-staging.yml`), push tag `v*` → prod
(`deploy-prod.yml`); both rsync code (excluding `.env`) and rebuild. Old `deploy.sh` needs `mas_key.pem` and still
has a hardcoded Serper API key in git — rotate it.

**Models** (`Last-verified: 2026-09-15`): every role runs `deepseek/deepseek-v4.1-flash` via `AGENT_MODEL` in
`app/config.py` (it overrides any `AGENT_{FAST,MID,STRONG,PREMIUM}_MODEL`, blank it to route per role). V4.1 Flash reasons
by default at high effort and reasoning tokens count toward `max_tokens`, so `get_llm` sends `reasoning.enabled` per call,
on only for `AGENT_REASONING_ROLES` (default `strong`). Merged to `develop` 2026-09-15 (commit efc2332); prod not tagged.

**Stack**: Python 3.12, LangGraph orchestration, OpenRouter LLM routing, IBKR Client Portal API, Telegram output,
FastAPI+HTMX dashboard on :8080, Langfuse prompts, Docker on OCI (prod + staging; images ~11.7 GB — see stillcasting infra).

## Pages
- [[signal-quality]] — realised track records, DB-native calibration, rejected-candidate contamination fix, walk-forward lessons.
- [[earnings-scoring]] — decision-aware grading, reaction baseline, direction/BUY gates, beats-don't-predict-direction.
- [[infra-deploys]] — OCI/Docker/deploy gotchas (SSH drops, container conflicts, Langfuse prompt override, .env overwrite).

## State as of 2026-08-09
- Shipped: `news_research_rejected` VIEW split; decision-aware earnings grading + re-grade; reaction baseline (15/29 = 52%);
  direction gate on WATCH; expectations-framed direction prompt.
- Proposed: numeric calibrated P(up) as primary signal; CI on dashboard accuracy; store bmo/amc report hour.
- Posture: everything is paper-trading grade (bar for action-trust: n≥50, positive median AR, hit >50%).
- Open: does the new prompt lift direction accuracy >50%? why does Static Research's 5d edge vanish by 10d? is the news critic inverted?
Related: [[investing]], [[access]].
