# financial-research-mas — project index

Async multi-agent system generating investment signals from news, earnings and portfolio monitoring.
`Last-verified: 2026-08-09`. Migrated 2026-09-12 from `~/Documents/ClaudeProjects/financial-research-mas-wiki`.

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
