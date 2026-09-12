# OFS automations (Codex) — to re-register on the new Mac

`Status: not registered on current Mac` · `Last-verified: 2026-08-31`. Source: bundle `configuration/automations/`.
Definitions: `cli-ticket-create`, `cli-ticket-update`, `grafana-loki-query`, `kh05-queue-report`, `customers-ticket-report`,
`overall-tickets-overview`, `repo-check-daily-repot`, `run-db-scan-approvals`, `slack-activity-tracker-update`,
`standup-summary` (some with `-c39766180f54` variants). Inputs live in bundle `automation-dependencies/` (customer ticket
Excel exports, activity tracker, Slack scanner, 10 OFS repo working copies). Old working dir `~/Documents/OrgAnalytics/web`
was missing at export — needs fresh checkout. All absolute paths need `/Users/oleksandrgrytsenko` → `/Users/alexgrtsenko`.
Related: [[oracle-ofs-index]], [[environment]].
