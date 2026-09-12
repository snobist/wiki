# financial-research-mas Wiki — Index

Persistent knowledge base for **financial-research-mas** — an async multi-agent
system generating investment signals from news, earnings, and portfolio monitoring
(Python 3.12, Docker on OCI, Telegram output, FastAPI+HTMX dashboard on :8080).
Maintained per `schema.md`.

Seeded 2026-08-09 from a long working session (2026-06 → 2026-08) covering
calibration integrity, earnings scoring, and pipeline credibility.

## Topic map
- [[wiki/signal-quality]] — realised track records per pipeline, DB-native calibration, the rejected-candidate contamination fix, walk-forward backtest lessons.
- [[wiki/earnings-scoring]] — decision-aware grading, reaction baseline, direction/BUY gates, the beats-don't-predict-direction finding.
- [[wiki/infra-deploys]] — OCI/Docker/deploy gotchas (SSH drops, container conflicts, Langfuse prompt override, .env overwrite).

## Current state (as of 2026-08-09)
- **Shipped:** `news_research_rejected` VIEW split; decision-aware earnings grading
  (SKIP/flat unscored) + historical re-grade; reaction-baseline measurement + 65-row
  re-measure (honest record 15/29 = 52%); direction gate on WATCH calls
  (`raw_direction` learning); expectations-framed direction prompt.
- **Proposed, not built:** numeric calibrated P(up) as the primary signal (replacing
  categorical arrows); CI display on dashboard accuracy; store bmo/amc report hour
  for same-day BMO grading.
- **Standing posture:** all discovery pipelines are paper-trading grade — no bucket
  has earned action-trust (bar: n≥50, positive median AR, hit >50%).

## Top open questions
1. Does the expectations-framed prompt lift direction accuracy above 50%? (watch scoreboard as n grows past ~50)
2. Why does Static Research's 5d edge evaporate by 10d — and is a mechanical 5-day exit worth building?
3. Is the news critic still inverted after the prompt/context changes? (rejects 57% vs accepts 39% as of 2026-07)
