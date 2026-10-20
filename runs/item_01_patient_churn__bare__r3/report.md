# Patient Churn Assessment

## Bottom line

1. **This export can't tell us whether churn is getting worse.** It is a single snapshot: one row per patient, all measured as of 20 Jan 2026. It has no churn date and no history of past churn rates, so there is no valid time series of churn. None of the time-based cuts I tried shows churn rising. If anything they point slightly the other way, but they are biased by how the data was built and should not be read as a trend either way.
2. **The `Churned` flag needs to be defined before anyone acts on it.** 68% of patients (1,367 of 2,000) are flagged as churned. That includes 66% of patients who had a visit in the last 90 days. That is not believable as an annual churn rate for an outpatient provider, and it suggests the flag means something other than "the patient left".
3. **Taking the flag at face value, churn is linked to patient experience, cost and access, not to which market or service line a patient is in.** The most consistent associations are low overall satisfaction, low wait-time satisfaction, billing problems, higher out-of-pocket cost, longer distance to the facility, not using the patient portal, missed appointments and short tenure. State, specialty, insurance type and gender show no meaningful differences. Even together, these factors predict churn only weakly (cross-validated AUC ≈ 0.65), so most of what drives the flag is not in this file.

## Data and assumptions

- `patients.csv` has 2,000 patients, 21 columns and no missing values. It covers 10 states, 7 specialties and 4 insurance types.
- For every row, `Last_Interaction_Date` + `Days_Since_Last_Visit` = **2026-01-20**. I treat that date as the snapshot date. Last interactions range from Jan 2024 to Jan 2026.
- I assume `Churned` is a status as of the snapshot date. The file doesn't say how it is defined or what time window it covers.

## 1. Is churn getting worse?

There is no field showing *when* a patient churned, so a churn rate over time can't be built. I tried the two time-based cuts the file allows:

| Cut | Result | Why it isn't a trend |
|---|---|---|
| Churn rate by quarter of last interaction | 76% (2024 Q1) → 65–66% (2025 Q4 / 2026 Q1); the general drift is **downward** | Patients whose last contact was long ago are more likely to have been labelled as churned. This measures how recently patients were seen, not churn over time. |
| Churn rate by year the patient joined (snapshot minus tenure) | 58%–77% with no steady direction (2016: 68%, 2019: 71%, 2022: 77%, 2025: 76%) | Newer patients churn more in every business, because tenure effects are mixed in with the cohorts. Older cohorts also only include people who stayed long enough to still be on the books. |

**Conclusion:** the data neither supports nor disproves leadership's view that churn is worsening. The overall rate of 68% is high, but nothing in the file can be used as a baseline for comparison.

## 2. Data quality issues to fix before acting

- **The churn flag doesn't match visit recency.** Patients seen in the last 90 days are flagged as churned 66% of the time. For patients not seen in 1–2 years, the figure is 71–73%. If "churned" meant "stopped coming", those numbers would be far apart.
- **Visit fields contradict each other.**
  - 940 patients had no visit in over 365 days but show `Visits_Last_Year` > 0.
  - 63 patients had a visit in the last year but show `Visits_Last_Year` = 0.
- **191 patients** have a last visit that falls *before* their tenure start date.
- The variables are almost uncorrelated with each other. For example, missed appointments and billing issues don't move with satisfaction, and cost doesn't vary by insurance type in any meaningful way. Real patient data usually shows these relationships. This suggests the export may be assembled or simulated, so I'd treat the findings below as directional only.

## 3. What is associated with churn?

**Method:** a multivariable logistic regression with all fields included. Odds ratios (OR) for numeric variables are per one standard deviation. OR above 1 means higher churn odds, below 1 means lower.

| Factor | Churn rate by group (raw) | Adjusted OR (95% CI) |
|---|---|---|
| Overall satisfaction (per 1 SD ≈ 1 point) | 78% at ≤2.0 vs 52% at 4.5–5.0 | **0.71** (0.64–0.78) |
| Billing issue reported | 77% vs 68% | **1.62** (1.08–2.43) |
| Uses patient portal | 62% vs 70% | **0.66** (0.52–0.84) |
| Days since last visit (per ~213 days) | 60–66% (<1 yr) vs 71–73% (>1 yr) | 1.21 (1.10–1.34) |
| Out-of-pocket cost (per ~$590) | 66% (<$800) vs 73% (>$1,600) | 1.21 (1.07–1.37) |
| Distance to facility (per ~14 miles) | 64% (<10 mi) vs 73% (>40 mi) | 1.20 (1.09–1.32) |
| Missed appointments (per ~1.7) | 63–66% (0–1) vs 74% (5) | 1.15 (1.03–1.28) |
| Tenure (per ~35 months) | 76% (≤1 yr) vs 63% (>7.5 yrs) | 0.85 (0.77–0.93) |
| Wait-time satisfaction | — | 0.83 (0.75–0.92) |
| Age (per ~16 yrs) | 77% (18–30) vs 65% (45+) | 0.89 (0.81–0.98) |
| Provider rating, referrals made | — | 0.90 each (borderline, p ≈ 0.03–0.04) |
| Staff satisfaction, visit volume | — | not significant |
| State, specialty, insurance, gender | 64%–72% across groups | none significant |

**How strong are these factors?** Each effect is modest. Together they explain little of the variation: pseudo-R² is 0.07, and cross-validated AUC is 0.65 for logistic regression and 0.63 for gradient boosting. A churn-risk score built from this file would only rank patients a little better than chance. These are also associations from cross-sectional data, not proven causes. For example, low satisfaction could be partly a *result* of a patient already disengaging.

## Recommendations

1. **Fix the churn definition first.** Agree on a written definition, for example "no completed visit in the 12–18 months after the last expected visit, and not deceased or transferred out", and re-derive the flag from scheduling and visit records. Find out why 66% of recently seen patients are flagged as churned.
2. **Build the data needed to answer the trend question.** Pull visit-level history, or monthly status snapshots, so churn can be measured as *active patients at the start of a period who were lost during it*. Report it monthly or quarterly by state and specialty. Only then can "getting worse" be confirmed or ruled out.
3. **Fix the data quality issues listed in section 2** (`Visits_Last_Year` vs `Days_Since_Last_Visit`, tenure vs last visit) at the source system.
4. **In the meantime, put modest effort into the levers that look most promising.** They line up with the signals above and are worth doing for other reasons as well:
   - **Billing:** resolve billing issues quickly and run price-transparency or payment-plan outreach for patients with high out-of-pocket costs.
   - **Portal:** drive portal enrollment and use it for reminders and self-scheduling. This should help with missed appointments too.
   - **Wait times and overall experience:** follow up on low satisfaction scores (≤2.5) within days.
   - **Access for distant patients:** offer telehealth or satellite options for patients more than 30 miles away.
   - **Onboarding:** focus on new (first-year) and younger patients.
5. **Test these with controlled pilots** (holdout groups) instead of rolling them out everywhere, because this data shows associations, not causes. Don't target by state, specialty or insurance: the data shows no difference there.
