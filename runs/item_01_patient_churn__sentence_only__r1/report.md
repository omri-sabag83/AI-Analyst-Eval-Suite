# Patient Churn: Is It Getting Worse, and What Drives It?

**Data:** `patients.csv`, 2,000 patients, 21 fields, no missing values. It is a single snapshot. `Last_Interaction_Date + Days_Since_Last_Visit` equals **2026-01-20** for every row, so that is the "as-of" date.

## Bottom line

1. **This data can't show whether churn is getting worse.** The export is one snapshot with a yes/no churn flag. It has no churn date, so we can't build a churn-rate time series. The two time proxies that are available point in opposite directions, and both are biased by how they're built. Neither supports the belief that churn is getting worse.
2. **The `Churned` flag needs checking before anyone acts on it.** It marks **68%** of patients as churned, including **66% of patients seen in the last 90 days**. Other fields contradict each other too (details below). Until the business confirms how "churned" is defined, treat every number here as provisional.
3. **Taking the flag at face value, the drivers are mostly about patient experience and access, not demographics.** Overall satisfaction, wait-time satisfaction, billing problems, not using the patient portal, out-of-pocket cost, distance to the facility, missed appointments and shorter tenure are each linked to churn after adjusting for the other factors. State, specialty, insurance type and gender are not. Even so, the factors together predict churn only weakly (cross-validated AUC about 0.65), so most of the variation is unexplained.

## 1. Is churn getting worse?

The data contains no churn date, so the question can't be answered directly. I checked two proxies:

| Proxy | What it shows | Why it's unreliable |
|---|---|---|
| Churn rate by quarter of **last interaction** | 2024Q1 76% → 2025Q4 65%. That is a *decline* (logit slope −0.32 per year, p<0.001) | Mechanically biased. Patients whose last contact was long ago are more likely to be labelled churned anyway, so this shows recency, not a trend over time. |
| Churn rate by **join cohort** (as-of date minus tenure) | 2017–18 cohorts about 58–61%; 2022–25 cohorts about 68–77%. That is a *rise* (p<0.001) | Mixed up with tenure. Newer patients churn more at any point in time, which is a known early-tenure risk. A snapshot can't separate "newer cohorts are worse" from "new patients are always riskier". |

**Conclusion:** the data neither supports nor rules out the "getting worse" belief. The join-cohort pattern hints that patients acquired recently are retained worse, and that is worth checking with proper data (see recommendations).

## 2. Data-quality concerns about the outcome

- **The churn rate is implausibly high.** 1,367 of 2,000 patients (68.4%) are flagged, which is very high for an outpatient provider.
- **The flag barely depends on recency.** Churn is 66% among patients seen ≤90 days ago and 71–73% among those not seen for more than a year. A recency-based definition would give a much sharper split.
- **The visit fields contradict each other.** 47% of patients have `Days_Since_Last_Visit` > 365 but `Visits_Last_Year` > 0. Churned patients also show slightly *more* visits last year than retained ones (7.8 vs 7.3).
- **The Pediatrics data doesn't fit.** All 284 Pediatrics patients are 18 or older (minimum age in the whole file is 18).
- **The data looks synthetic.** Categorical variables are evenly spread and the satisfaction sub-scores are almost uncorrelated with each other (|r| ≤ 0.04), which is unusual for real survey data.

Taken together, `Churned` may be a forward-looking prediction, a label with a different meaning, or partly noise. It should not be read as "left the practice".

## 3. What is associated with churn (flag taken at face value)

I fitted a multivariable logistic regression on all fields. The table shows the average marginal effect on churn probability; overall base rate is 68%.

| Factor | Effect on churn probability | p |
|---|---|---|
| Overall satisfaction | −6.9 pp per point (1 point ≈ 1 SD); bottom quintile 77% vs top quintile 57% | <0.001 |
| Billing issue reported | +9.9 pp (77% vs 68% raw) | 0.02 |
| Patient-portal user | −7.7 pp (62% vs 70% raw) | 0.001 |
| Wait-time satisfaction | −3.8 pp per point | <0.001 |
| Out-of-pocket cost | about +0.7 pp per $100 (≈ +4 pp per SD of $590) | 0.002 |
| Distance to facility | +2.5 pp per 10 miles | <0.001 |
| Tenure | −1.0 pp per year of tenure (−3.5 pp per SD) | 0.001 |
| Missed appointments | +2.0 pp per missed appointment | 0.01 |
| Provider rating | −2.8 pp per point | 0.03 |
| Referrals made | −2.0 pp per referral | 0.04 |
| Age | −1.4 pp per decade | 0.02 |
| **Not significant:** State (64–72%), Specialty (64–70%), Insurance type (67–71%), Gender, Staff satisfaction, Visits last year | — | >0.1 |

**Caveats on these drivers**
- **These are associations, not proven causes.** For example, portal users may simply be more engaged patients.
- **The model explains little.** Cross-validated AUC is 0.65 for logistic regression and 0.63 for gradient boosting, so it can't reliably pick out individual patients at risk.
- **Every effect is modest.** No single factor moves churn by more than about 10 pp.

## Recommendations

1. **Fix the measurement first.** This step is cheap and comes before any spending.
   - Get the exact business definition of `Churned` and the date each patient churned.
   - Reconcile `Visits_Last_Year` against `Days_Since_Last_Visit`, and the Pediatrics ages.
   - Adopt one operational definition, for example "no visit or scheduled appointment in 12 or 18 months", and compute it from visit-level records.
2. **Track churn properly over time.** Build a monthly or quarterly churn-rate series, and retention curves by join cohort, from visit history. That is the only way to answer "is it getting worse?". It would also confirm or refute the signal that recent cohorts retain worse.
3. **Pilot the levers the data points to, measured with a control group.** Satisfaction and billing are the strongest candidates.
   - **Billing.** Run a billing-issue resolution and follow-up workflow; the gap is about 10 pp.
   - **Portal.** Push portal enrolment at intake.
   - **Wait times and satisfaction.** Run service recovery for patients reporting low overall or wait-time satisfaction.
   - **Cost and access.** Offer cost transparency or payment plans for high out-of-pocket patients, and telehealth for distant patients.
   - **Missed appointments.** Use reminders and outreach to cut missed appointments.
   - **New patients.** Onboard them in their first two years.
   - Run these as randomized or staggered pilots so their effect can be measured. Don't roll them out based on these correlations alone.
4. **Don't target by state, specialty or insurance type.** None of them show meaningful differences.

## Assumptions

- The as-of date is 2026-01-20, derived from the data.
- Join date is approximated as the as-of date minus `Tenure_Months` × 30.44 days.
- `Churned` was analysed as provided, despite the concerns above.
