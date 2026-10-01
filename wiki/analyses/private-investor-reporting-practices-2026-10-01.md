# How private financial systems report — best practice

Web research for redesigning MAS reporting. `Last-verified: 2026-10-01`. Related: [[mas-change-proposal-2026-09-27]],
[[functionality-map]], [[investing]].

## Converging practice
- **Policy first (IPS).** CFA's IPS for individuals: write targets, ranges and review rules; monitoring = checking the
  portfolio against the policy. Common: calendar review (annual/semi-annual) + threshold action (drift > 5 or 10 pp).
  Deviations from policy reported immediately; everything else waits for the scheduled review.
- **Cadence (family offices):** daily/weekly cash, liquidity and risk checks (automated); monthly consolidated net worth
  + performance; quarterly review pack; annual tax package. Less active portfolios: quarterly.
- **What the regular report holds:** net worth and its change, holdings at value/cost/tax basis, time-weighted return vs
  benchmark, attribution (what drove it), allocation vs target, income (dividends), realised gains for tax, risk
  (concentration, currency, liquidity), upcoming events.
- **Robo-advisors:** threshold-based rebalancing and daily tax-loss harvesting run silently; the user sees outcomes.
- **Trackers (Sharesight, getquin, Snowball, Stock Events):** performance + tax reports, dividend calendar, ex-div /
  earnings notifications for holdings, price-target alerts (Telegram/WhatsApp/push).
- **Alerting (Google SRE):** every alert urgent + actionable; if no action follows, the alert shouldn't exist. Noise
  audit: rules with < 30% actionable firings get retuned or removed.
- **Behavioural evidence:** checking more often → more observed losses → worse decisions (myopic loss aversion,
  Benartzi & Thaler; experiments by Gneezy & Potters, Haigh & List). Barber & Odean: households trail the market ~2 pp/yr,
  the most active quintile > 7 pp/yr; investors buy attention-grabbing (in-the-news) stocks, which don't outperform.

## Implication for MAS
MAS today = daily pushes of news-driven ideas about stocks Alex doesn't hold, no targets, no benchmark/allocation view —
the pattern the evidence warns against. Redesign direction: IPS-lite (targets, bands, concentration limit incl. ORCL RSUs,
currency) → silent daily checks with exception alerts → monthly report (net worth, return vs benchmark, allocation vs
target, income, realised gains for PIT-38) → quarterly review with on-demand research → annual tax pack.
Status: research only; nothing changed.
