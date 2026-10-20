# Patient Churn: Assessment of `patients.csv`

## Bottom line

1. **This export can't tell us whether churn is getting worse.** It is one snapshot of 2,000 patients, all taken on the same date (2026-01-20). It has no history of churn rates over time. The only date field is each patient's *last interaction*. If I group patients by that date, the "trend" points the other way (more recent groups churn *less*), and that pattern is built into how the data is constructed. It is not evidence of improvement either.
2. **The `Churned` flag is undefined and doesn't look trustworthy as delivered.** 68.4% of patients are flagged as churned. That is far above any plausible annual attrition rate for an outpatient provider. Also, 60% of patients seen in the **last 30 days** are flagged as churned. Whatever rule produced this flag, it isn't "the patient stopped coming".
3. **The data has several internal contradictions** (below). These make me treat every driver finding as provisional.
4. **The driver signals that do exist are weak but consistent:** low overall satisfaction, low wait-time satisfaction, not using the portal, billing issues, distance to the facility, out-of-pocket cost and short tenure. A model using all the fields only reaches AUC ≈ 0.64 (0.5 is a coin flip). So the data explains little about who is flagged as churned.

**Recommendation:** before taking action on churn, define churn properly and rebuild the dataset as monthly or quarterly snapshots. In the meantime, the low-cost actions below are reasonable regardless of how the label question is resolved.

---

## 1. Is churn getting worse?

**Not answerable from this data.**

- Each patient's `Last_Interaction_Date` + `Days_Since_Last_Visit` adds up to exactly 2026-01-20 for all 2,000 rows. This is a single point-in-time extract with no churn history.
- Grouping by half-year of last interaction:

| Last interaction | Churn flag rate | n |
|---|---|---|
| 2024 H1 | 71.3% | 449 |
| 2024 H2 | 72.6% | 497 |
| 2025 H1 | 68.5% | 496 |
| 2025 H2 | 61.7% | 506 |
| 2026 (Jan) | 65.4% | 52 |

  The downward slope is statistically significant (logit p < 0.001). But it doesn't measure churn over time. Patients whose last contact was long ago are, by construction, more likely to be labelled lost. So this slope is a recency effect, not a trend, and **it doesn't support leadership's belief either way.**
- Grouping by tenure (as a rough proxy for when patients joined) shows no clear time pattern. Newer patients churn slightly more (≈ 75% at 0–12 months vs ≈ 60% at 84–108 months). That is a standard tenure effect, not evidence that things are deteriorating.

**What would answer the question:** churn rates (on a fixed definition) for each period, e.g. the share of patients active at the start of each quarter who had no visit in the following 12 months, tracked over 8+ quarters.

## 2. Data quality issues (read before using any finding)

| Issue | Evidence |
|---|---|
| Churn rate implausibly high | 68.4% flagged (1,367/2,000) |
| Label conflicts with recency | 46 of 77 patients seen in the last 30 days are flagged as churned (60%). Churn is only modestly higher for patients unseen for >1 year (≈ 72%) than for those seen in the last 90 days (≈ 66%) |
| Visits vs recency contradict | 940 of 996 patients with no visit for over 365 days still show `Visits_Last_Year` > 0 |
| Tenure vs recency contradict | 191 patients have a last visit that predates their stated tenure |
| Pediatrics has no children | All 284 Pediatrics patients are aged 18+ |
| Medicare ages | 385 of 516 Medicare patients are under 65 (some is legitimate via disability, but 75% is implausible) |
| Out-of-pocket costs | Median out-of-pocket cost for Medicaid ($1,059) is the same as for Private ($1,056), which is implausible. Only Medicare is lower ($276) |
| Satisfaction sub-scores unrelated | Overall, wait-time, staff and provider scores are almost uncorrelated with each other (|r| ≤ 0.04), which is unusual for real survey data |

These issues suggest the export was assembled or simulated in a way that doesn't reflect real patient journeys, or that fields were joined incorrectly. **I recommend confirming with the data owner how `Churned` was defined and how the extract was built.**

## 3. What is associated with the churn flag?

Method: churn-flag rates by group, plus a multivariable logistic regression on all fields (n = 2,000). I treat these as associations with the flag as provided, not causal effects.

| Factor | Churn-flag rate | Independent effect (logit, all other fields held constant) |
|---|---|---|
| Overall satisfaction, bottom vs top quartile | 76.5% vs 58.3% | Strongest: −0.34 log-odds per point, p < 0.001 |
| Wait-time satisfaction, bottom vs top quartile | 73.7% vs 63.9% | −0.18 per point, p < 0.001 |
| Portal use (yes vs no) | 61.7% vs 70.1% | −0.41, p < 0.001 |
| Billing issue (yes vs no) | 77.1% vs 67.6% (n = 157 with an issue) | +0.48, p = 0.02 |
| Distance, >37 mi vs <13 mi | 72.9% vs 63.1% | +0.013 per mile, p < 0.001 |
| Out-of-pocket cost, top vs bottom quartile | 71.8% vs 67.1% | +0.03 per $100, p = 0.002 |
| Missed appointments, 5 vs 0 | 74.4% vs 66.3% | +0.08 per missed appointment, p = 0.01 |
| Tenure, 0–12 vs 96–108 months | 75.6% vs 58.2% | −0.06 per year, p < 0.001 |
| Provider rating, referrals made, age | small | small negative effects, p 0.02–0.04 |

**Not associated:** state, specialty, insurance type, gender (all within ~6 points of the average, no significant effect) and staff satisfaction.

**How much do these explain?** Not much. Pseudo-R² = 0.07, and cross-validated AUC = 0.65 (logistic regression) and 0.63 (gradient boosting). Removing days-since-last-visit hardly changes the AUC (0.64), which again suggests the label isn't a recency-based definition. No single segment or region is "the problem". The differences are gradual and spread across the whole patient base.

## 4. Recommendations

**First, fix the measurement (prerequisite):**
1. **Write down a churn definition**, for example "no completed visit in 12 months among patients who were active at the start of the period, excluding deaths, moves and planned discharges". Recompute the flag from visit records rather than using the current field.
2. **Rebuild the extract as repeated snapshots** (monthly or quarterly) so churn can be trended. Only then can "getting worse" be tested.
3. **Fix the source inconsistencies** listed in section 2 (visit counts, tenure, pediatric ages, payer fields).

**Then, actions that are justified now (low cost, consistent signals, worth piloting with a control group):**
4. **Wait times and overall experience:** these are the strongest, most consistent levers in this data.
5. **Portal adoption:** portal users have an ~8-point lower churn-flag rate. Note that self-selection is likely (engaged patients adopt the portal), so measure this with a randomised enrolment push, not a before/after comparison.
6. **Billing-issue resolution and cost transparency:** a small group (8% of patients), but the highest flag rate.
7. **Outreach to patients after missed appointments, to new patients in their first year, and to patients living more than 35 miles away** (e.g. telehealth options).

**Don't do:** reallocate budget by state, specialty or payer based on this data. There are no meaningful differences between them.

## Assumptions and limitations
- I took `Churned` as provided because I had no definition. All driver findings are associations with that flag and may not hold under a proper definition.
- The snapshot date (2026-01-20) is inferred from the arithmetic of the date and recency fields.
- The data is cross-sectional, so no causal claims are made. Effects of portal use and satisfaction may partly reflect patients who were already disengaged.
