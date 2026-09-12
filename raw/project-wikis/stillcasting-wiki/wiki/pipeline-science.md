# Pipeline Science

Purpose: rigorous, named methods to upgrade the data pipeline from deterministic lookups to
probabilistic, demographically-informed inference. Status: all PROPOSED. Last-verified: 2026-08-09.

## Priority order
Start with §1 (cascades into 3 wins) and §2 (kills the worst error class).

## 1. Actuarial survival modeling
Problem: `presumed_deceased`/`unverified` are guesses; Legends ("oldest living actors") credibility
rests on this call.
- **Cohort life tables** (Human Mortality Database, mortality.org; SSA tables) → principled
  `P(alive | birth year, sex, nationality-cohort)`.
- **Gompertz–Makeham law** μ(x)=α·e^(βx)+λ to extrapolate beyond table ages (supercentenarians).
- Output: replace binary "presumed dead" with a **confidence score**; auto-flag `presumed_deceased`
  when P(alive) < ~1%. Feeds §5 scheduling and §4 content.

## 2. Bayesian multi-source death fusion
Problem: false-death flips (see Data-integrity risk below). Method: treat each source as evidence with
known reliability (sensitivity/specificity), combine via Bayes → posterior `P(deceased)`. Sources:
Wikidata `P570`, **Wikipedia "Living people" category removal** (fast, high-precision), TMDb `deathday`,
news. Flip to `deceased` only when posterior high **and** ≥2 independent sources agree; else hold in an
interim state.

## 3. Probabilistic record linkage (fixes `identity_unclear` + wrong wiki photos)
**Fellegi–Sunter model** (1969) — match weights from field agreement (name via **Jaro–Winkler**, birth
year, nationality, **filmography overlap**) with m/u probabilities and auto-link/review/reject thresholds.
Open-source: **Splink**. Replaces brittle exact-match heuristics.

### Confirmed instance — wrong wiki photo (visitor report, 2026-08-09)
- Visitor "Lynn" reported `/persons/anthony-franke` showed a photo of **Anthony Franciosa**.
- Diagnosis: **different people.** "Anthony Franke" = TMDb 1801645, obscure (1 credit, "Al" in *The Blob*
  1958, no dates, no TMDb photo). Anthony Franciosa (1928–2006) = famous, separate actor. The wiki-photo
  scanner matched the *name* "Anthony Franke" → Franciosa's Wikipedia article and pulled his portrait —
  **no entity verification** (person had wiki photo but empty `wikidata_id`).
- Fixed: `UPDATE persons SET wiki_profile_path_local = NULL WHERE id = 220688` (id-scoped, reversible;
  old value `media/profiles/1801645/wiki_w185.jpg`). Page now shows placeholder (correct — no valid photo).
- **Systemic exposure:** `SELECT count(*) FROM persons WHERE wiki_profile_path_local IS NOT NULL AND
  (wikidata_id IS NULL OR wikidata_id='')` = **48,009** — wiki photos with no Wikidata anchor (population
  at risk, NOT all wrong). Highest-risk subset: common name + no dates + no TMDb photo + few credits.
- Fix forward: only attach a wiki photo when the wiki entity is verified (Wikidata link, or agreement on
  birth year / filmography). Audit existing 48k by re-matching with verification; flag high-risk for review.
  Do NOT mass-delete (most are fine).

## 4. Survival analysis as content (unique, citable, brand-safe)
Ties to SEO moat + AI citation. Data enables analyses nobody else has:
- **Kaplan–Meier** survival curves per cohort (`lifelines`).
- **Standardized Mortality Ratio (SMR)** vs general-population life tables — "do actors outlive the public?"
  Literature: Redelmeier & Singh 2001 (Oscar winners, *Annals of Internal Medicine*).
- ⚠️ Methodological honesty: avoid **immortal time bias** (Sylvestre et al. 2006 correction); disclose
  **selection bias** (TMDb covers the notable, not the general public). Doing it right IS the differentiator.

## 5. Hazard-based scan scheduling (operations research)
The §1 survival model gives each living person a **hazard rate** (P(dies in next 30 days)). Schedule
Celery rescans by **hazard × page popularity** (expected value of information) → captures death-news
spikes faster at the same compute budget.

## 6. Anomaly-detection guard
Cheap ingest guards: impossible ages (DOD−DOB), **death date suspiciously recent** vs a still-"living"
Wikipedia category (the false-death signature), cross-field inconsistency → route to review, don't publish.

## Data-integrity risk — false / impossible death dates (OPEN, high stakes)
Two confirmed instances of the same class — a single bad source can flip a person to `deceased`,
publish it, and give it a "How Did X Die?" headline (see [[wiki/proposals]]).

### Case 1 — false death (2026-06)
- `/persons/marjane-satrapi` marked **Deceased** ("died in Paris, aged 56", dated ~2 days prior).
  Marjane Satrapi is a well-known **living** graphic novelist (Persepolis) → **false-death** signature.

### Case 2 — future death date (found 2026-08-09)
- `/persons/giorgos-marinos`: stored `date_of_death = 2026-10-03` (ISO) — **~2 months in the future**
  (today 2026-08-09), yet marked Deceased and shown at the TOP of the "Remembered This Week" widget.
- Two compounding bugs:
  1. **Impossible/future death date** — either a bad source value or a **DD/MM ↔ MM/DD swap** at ingestion
     (e.g., a real `2026-03-10` flipped to `2026-10-03`). If a swap, it is systematic, not one-off.
  2. **Recently-deceased query lacks an upper bound** — no `date_of_death <= today` filter, so future
     deaths leak in and sort to the top as "most recent".
- **Root cause found 2026-08-09 — two layers:**
  1. *Display:* the `<= CURRENT_DATE` guard on `died-this-week` was added in commit `05820b9`
     ("Fix died-this-week query including future-dated deaths", 2026-07-09) and is on `develop` (HEAD),
     but **NOT deployed to prod** (manual prod deploys). Confirmed: Giorgos still shows on prod
     `/died-this-week` + homepage widget; would be filtered if the guard were live. → deploy develop→prod.
  2. *Data (real bug):* `05820b9` patched the **query**, not **ingestion**. The record is still wrong
     (`date_of_death=2026-10-03`, `status=deceased`); the person page still renders "How Did … Die?".
     Nothing rejects a future date at write time. Root = bad source value or DD/MM↔MM/DD parse swap.
- **SOURCE TRACED 2026-08-09 — it's TMDb, not the wiki page, and NOT a code swap:**
  - TMDb person 1455489 `deathday` field = **2026-10-03** (its own bio prose says "March 10, 2026" — the
    structured field is a DD/MM↔MM/DD **transposition** entered by a TMDb contributor). `10/03` → `03/10`.
  - `scanner_service.py:93-95` takes `detail.deathday` verbatim → flips to DECEASED → stores `2026-10-03`.
    `date.fromisoformat` parsed a correct-looking-but-wrong ISO string, so **no swap bug in our code**.
  - **Wikidata `P570 = 2026-03-10` (correct, set 2026-07-03)** — our *second* source had it right; TMDb and
    Wikidata disagreed and nothing reconciled them. Death data is NOT single-source: TMDb `deathday`
    (primary trigger), Wikidata `P570`, and the Wikipedia Deaths_in_{year} parser all write `date_of_death`.
  - He DID die (2026-03-10) → wrong DATE, not a false death. Widget "age 87" matches the wrong Oct date (correct=86).
- Real defects = two missing guards (not a parser bug):
  (1) **§6 future-date guard** — `2026-10-03` was future at scan time → reject/hold. Catches it alone.
  (2) **§2 cross-source reconciliation** — TMDb vs Wikidata disagreed by a clean transposition → flag.
- Fixes: correct this record to `2026-03-10`; deploy develop→prod (stops widget leak); add §6 + §2 guards;
  `SELECT count(*) FROM persons WHERE date_of_death > CURRENT_DATE` to size other future-dated TMDb records.

### Action
Prioritize §2 (Bayesian death fusion) + §6 (anomaly guard). Verify both records; trace how `deceased`
was set (TMDb/Wikidata/manual); enforce future-date + recency guards before a person flips to `deceased`.
