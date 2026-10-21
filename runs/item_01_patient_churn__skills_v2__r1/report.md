# Patient Churn Assessment

**Data:** `patients.csv`, 2,000 patients, 21 fields, no missing values. It is a single snapshot. Every row's `Last_Interaction_Date + Days_Since_Last_Visit` equals **2026-01-20**, so that is the as-of date. Last interactions run from 2024-01-21 to 2026-01-19.

## Bottom line

1. **This export can't show whether churn is getting worse.** It is one snapshot. It has no churn date and no history of past churn rates. The only date field, last interaction, is tied mechanically to the churn outcome, so it can't be used as a trend axis. Where I could make a rough comparison, nothing shows churn rising.
2. **The `Churned` label itself is suspect.** 68.4% of patients are flagged as churned, which is implausibly high for an outpatient provider. 60% of patients seen in the **last 30 days** are also flagged as churned. Until the definition is confirmed, every rate in this report is a rate of "whatever `Churned` means", not necessarily of patients who actually left.
3. **Taking the label as given, the drivers we can act on are modest but consistent:** low overall satisfaction and low wait-time satisfaction, billing problems, not using the patient portal, higher out-of-pocket cost, distance from the facility, missed appointments and shorter tenure. State, specialty, insurance type and gender have no independent effect. All the variables together predict churn only weakly (cross-validated AUC ≈ 0.65). Most of what drives the label is not in this data.

**Recommendation in one line:** fix the churn definition and start a monthly churn time series before acting on "churn is getting worse". In parallel, run low-cost pilots on billing-issue resolution, portal enrolment and wait times, because the evidence for those is consistent.

---

## 1. Is churn getting worse?

**Finding: we can't tell from this data. Nothing here supports "worse".**

- A trend needs churn rates measured at several points in time. This file has one status per patient as of 2026-01-20.
- Grouping by last-interaction date gives 72.0% churned for patients last seen in 2024 and 65.1% for 2025 (p = 0.001). The fall is not evidence of improvement. Patients last seen longer ago are more likely to be flagged as churned *by construction*, so this split mostly measures recency.
- Grouping by join year (estimated as the as-of date minus tenure) shows recent joiners (2022–2025) churning at about 73%, against about 66% for 2016–2021. That reflects **tenure**: long-tenured patients are, by definition, the ones who stayed. It is not a sign of deterioration over calendar time.
- **Assumption:** leadership's belief may come from other reports (for example, monthly attrition counts). Nothing in this file confirms or refutes those reports.

## 2. Data-quality issues (read before trusting any number)

| Issue | Evidence | Implication |
|---|---|---|
| Implausible base rate | 1,367 / 2,000 = **68.4%** churned | The label is probably not "patient permanently left". It may be a broad flag (for example "no visit within X", or a lapse in any service line) or a biased extract. |
| Recently seen patients flagged as churned | 46 of 77 patients (60%) seen in the last 30 days are `Churned = 1`. Churn varies only from 60% to 73% across recency bands. | If churn meant inactivity, recency would separate churners from non-churners sharply. It barely does. |
| Visit counts contradict recency | 940 patients have no visit in over 365 days but still record `Visits_Last_Year > 0` | Either "last year" uses a different window or the fields come from different systems or dates. |
| Pediatrics patients aged 18–86 | Median age in Pediatrics is 54 | The specialty field may be a referring or department code rather than the patient's own care line. Don't use it for segmenting until it is checked. |
| Satisfaction sub-scores are uncorrelated | Overall satisfaction correlates with wait-time, staff and provider scores at \|r\| ≤ 0.04 | This is unusual for survey data. Scores may come from different survey waves, or be imputed or defaulted. |

Because of these issues, the driver results below are **associations with the label as provided**. They are not proven causes of patients leaving.

## 3. What is associated with churn?

Method: a multivariable logistic regression on all patient attributes. I deliberately **excluded** `Days_Since_Last_Visit` and `Last_Interaction_Date`, because a recency-based label would make them circular. Odds ratios (OR) are adjusted for every other variable.

| Factor | Raw churn rates | Adjusted OR | p |
|---|---|---|---|
| Overall satisfaction (per +1 point) | 79% at <2 → 60% at ≥4 | **0.71** | <0.001 |
| Wait-time satisfaction (per +1) | 74% lowest quintile → 63% highest | 0.84 | 0.001 |
| Billing issue (yes vs no, n=157) | 77% vs 68% | **1.65** | 0.015 |
| Portal user (yes vs no, n=412) | 62% vs 70% | **0.66** | 0.001 |
| Distance (per +10 miles) | 64% at ≤20 mi → 73% at >30 mi | 1.14 | <0.001 |
| Out-of-pocket cost (per +$100) | 66% lowest two quintiles → 72% top two | 1.03 | 0.002 |
| Missed appointments (per missed visit) | 66% at 0 → 74% at 5 | 1.08 | 0.014 |
| Tenure (per +12 months) | 72–74% bottom two quintiles → 64–65% top two | 0.94 | 0.001 |
| Provider rating (per +1) | 71–72% → 65–67% | 0.86 | 0.034 |
| Referrals made (per +1) | 72% at 0 → 66% at 3 | 0.91 | 0.043 |
| Age (per +10 years) | small | 0.93 | 0.020 |
| State, specialty, insurance, gender, staff satisfaction | 64–72% spread | n.s. | >0.1 |

How strong this is:
- Model fit is weak: pseudo-R² = 0.06, and 5-fold cross-validated AUC is 0.65 (logistic) or 0.63 (gradient boosting). These factors shift churn by a few to about 20 percentage points, but they explain only a small part of who is flagged.
- These are cross-sectional associations. For example, portal users may simply be more engaged patients, so enrolling someone in the portal won't necessarily keep them. Treat each effect as a hypothesis to test.
- I have not estimated how many patients would be retained by any intervention. Converting ORs into "patients saved" would assume causation, which this data cannot support.

## 4. Recommendations

1. **Define churn before debating whether it is worsening (do this first).** Get the business rule behind `Churned`, and explain why 60% of patients seen this month carry the flag. Then adopt a clear, time-bound definition, for example "no completed visit within 18 months, excluding patients discharged or deceased".
2. **Build the trend properly.** Using the new definition, compute churn monthly or quarterly from historical visit data, as cohort-based retention curves by join month. That is the evidence that would answer leadership's question. One snapshot cannot.
3. **Fix the data issues in section 2:** the visit-count window, the specialty and age mismatch, and the source of the satisfaction scores.
4. **Pilot the actionable levers, with control groups, while that work is under way.**
   - *Billing:** proactively resolve billing issues (7.9% of patients, strongest single flag, OR 1.65).
   - *Portal:** enrol patients in the portal (only 20.6% use it now). Randomise outreach so the engagement effect can be separated from patient self-selection.
   - *Wait times and satisfaction:** follow up on low satisfaction scores (patients scoring under 3 overall churn at about 76%).
   - *Access:** offer telehealth or reminders for patients over 30 miles away and those with repeated missed appointments.
   - *Early tenure:** put first-year patients into an onboarding or follow-up programme.
5. **Don't reallocate resources by state, specialty or insurance type.** Once other factors are controlled for, none of them differ meaningfully.

## Assumptions
- The as-of date is 2026-01-20, derived from the data.
- `Churned` was analysed as delivered. Section 2 explains why its meaning is uncertain.
- Join year is approximated as the as-of date minus `Tenure_Months` × 30.44 days.
- Recency fields were excluded from the driver model to avoid circularity with a probable recency-based label.
