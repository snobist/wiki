# Jira workflow (Oracle)

`Last-verified: 2026-08-31` (bundle). Source: `raw/codex-memories/jira-bug-template-global.md`, `rr-note-template-global.md`.

## Bug ticket template (use for ANY bug creation)
Sections, in Jira markup: *Description* (narrative) · *Pre-conditions* (optional) · *Steps to reproduce* (numbered) ·
*Actual Result* · *Expected Result* (with reasoning: requirement / previous prod behaviour) ·
*Regression from version (not reproducible on):* <version> (set Regression=Yes + Broken build if confirmed) ·
*Automation Test Failed:* (optional). Never assume project/team/component — discover required fields at creation time
and ask only for missing mandatory ones.

## RR note template (`@RR@`)
*Note type: @RR@* then: Description (opt) · Workaround (opt) · **Root Cause** · **Change Description** ·
**Automated Testing** (mandatory for customer bug fixes; link MRs; cover Feature ON and OFF) · Testing Hints
(mandatory for Gaps) · Side effects (opt) · Definition of Done (opt). Delete optional sections only in the final note.
Write in Alex's voice ([[humanizer-alex]]).

## Tooling
- `cli-ticket-create` / `cli-ticket-update` wrappers (bundle `tools/bin`) + skill `cli-ticket-creator`: one issue per
  run, required-field discovery, routing fields like "To Scrum Team". Auth: `JIRA_URL`, `JIRA_PERSONAL_TOKEN`
  (see [[access]]).
- MR reviews: skill `mr-review-risk` → risk score 1–5, changes, blast radius, perf impact.
