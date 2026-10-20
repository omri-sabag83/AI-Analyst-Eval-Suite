# Patient churn: is it getting worse, and what is driving it?

## Bottom line

1. **This export can't show whether churn is getting worse.** It is a single snapshot: all 2,000 patients are measured as of the same date, 2026-01-20. `Days_Since_Last_Visit` is exactly that date minus `Last_Interaction_Date` for every row. There is no churn date and no earlier snapshot, so we can't build a churn rate over time. The only split that looks like a trend actually points the other way. Patients whose last interaction was in 2024 are flagged churned 72% of the time, against 65% for 2025 (p = 0.004). But that split groups patients by how recently they were seen. It isn't a trend, and it doesn't support "getting worse".
2. **The `Churned` label itself looks unreliable, so treat every churn number here with caution.** It flags 68% of patients (1,367 of 2,000) as churned. That is implausibly high for an active patient panel. It also doesn't behave like churn:
   - 60% of patients seen in the **last 30 days** are flagged churned (46 of 77).
   - Churned patients had **more** visits last year than retained ones (7.8 vs 7.3).
   - About 275 patients flagged *retained* have not been seen for over a year.
   - Activity fields contradict each other. 940 of the 996 patients whose last visit was more than 365 days ago still show visits in `Visits_Last_Year`. Another 63 show zero visits last year despite a visit in the past 365 days.
3. **Several associations with the label are consistent, but weak.** They are dissatisfaction (overall and wait time), billing problems, not using the patient portal, distance to the facility, out-of-pocket cost, missed appointments, and being younger or newer. State, specialty, insurance type and gender show no meaningful difference. Taken together, all the fields explain little: cross-validated AUC is 0.65 (0.5 is a coin flip), and pseudo-R² is 0.07.

**Recommendation:** before acting on "churn is rising", agree on a written definition of churn (for example, no visit in 12 or 18 months with no future appointment booked). Then rebuild the label from visit history, with dates, and track it monthly. Meanwhile, the satisfaction, billing and portal findings are reasonable low-regret things to act on, but they need to be confirmed against the corrected label.

---

## 1. Data and assumptions

- `patients.csv` has 2,000 rows (one per patient) and 21 columns, with no missing values. It covers 10 states, 7 specialties and 4 insurance types.
- Last interaction dates run from 2024-01-21 to 2026-01-19. The snapshot date works out to 2026-01-20 for every row.
- **Assumption:** `Churned` is used as provided. We don't know its definition, how it was produced or when it was set.
- **Assumption:** we don't know when the satisfaction and cost fields were collected relative to churn. If the survey was taken after a patient decided to leave, the satisfaction link could partly run in reverse.

## 2. Is churn getting worse?

**The data can't answer this.** A trend needs churn measured at two or more points in time, or a dated churn event. This file has neither.

These are the time-like splits that are available, and why none of them answers the question:

| Split | Churn rate | Why it isn't a trend |
|---|---|---|
| Last interaction in 2024 (n=946) | 72.0% | Groups patients by how long ago they were last seen, not by when they churned |
| Last interaction in 2025 (n=1,002) | 65.1% | Same |
| Tenure ≤12 months (n=193) | 75.6% | Long-tenure patients are, by definition, the ones who stayed. That survivorship effect, plus the tenure effect itself, is mixed in with any cohort effect |
| Tenure 96–120 months (n=433) | 63.3% | Same |

If anything, the naive "by last interaction date" split shows *lower* churn among recently active patients. That is what you would expect, and it says nothing about direction over time.

## 3. Problems with the `Churned` label

| Check | Result | What you'd expect from a sound churn label |
|---|---|---|
| Overall rate | 68.4% | Usually well under 50% for an active panel |
| Churn rate, last visit ≤30 days | 59.7% (n=77) | Close to 0% |
| Churn rate, last visit ≤90 days vs 630–730 days | 65.9% vs 71.5% | A large gap |
| Mean visits last year, churned vs retained | 7.78 vs 7.26 | Churned patients visit less |
| Patients last seen >365 days ago but with visits in `Visits_Last_Year` | 940 of 996 | 0 |

The label barely tracks recency. Either it means something other than "stopped coming", such as a risk flag or a survey answer like "intends to switch", or the export has a data-quality problem. Either way, leadership's churn figure shouldn't be quoted until this is resolved.

## 4. What is associated with the label

I fit a multivariable logistic regression with all fields entered together, so each effect is adjusted for the others. I also compared raw rates across groups.

| Factor | Raw churn rate | Adjusted odds ratio (95% CI) |
|---|---|---|
| Overall satisfaction, per +1 point | 78% at ≤2.0 vs 52% at >4.5 | **0.71** (0.64–0.78) |
| Wait-time satisfaction, per +1 point | 72–78% at ≤2.5 vs ~65% at >3.0 | **0.83** (0.75–0.92) |
| Billing issue (yes vs no) | 77% vs 68% (n=157 with issue) | **1.62** (1.08–2.43) |
| Uses patient portal | 62% vs 70% | **0.66** (0.52–0.84) |
| Distance, per +10 miles | 64% at ≤10 mi vs 73% at 40–50 mi | **1.14** (1.06–1.22) |
| Out-of-pocket cost, per +$100 | 64–68% under $1,000 vs 72–73% over $1,000 | **1.03** (1.01–1.05) |
| Missed appointments, per +1 | 66% at 0 vs 74% at 5 | **1.08** (1.02–1.15) |
| Provider rating, per +1 | – | 0.86 (0.75–0.99) |
| Tenure, per +12 months | 76% in the first year vs 63% at 8–10 years | ~0.94 per year (p=0.001) |
| Age, per +10 years | 77% for ages 18–30 vs ~65% for 45+ | ~0.93 per decade (p=0.02) |
| State, specialty, insurance, gender, staff satisfaction | 64–72% across all groups | No significant effect |

**Robustness check:** I re-fit the model separately for patients seen within the last year and those not seen for over a year. The direction and approximate size of every effect above held in both groups. For example, the overall-satisfaction odds ratio was 0.66 in one group and 0.76 in the other, and for billing issues it was 1.54 and 1.72.

**Caveats:**
- These are associations with an unreliable label, not proven causes.
- Their predictive power is modest: cross-validated AUC is 0.65 for logistic regression and 0.63 for gradient boosting. No single field or segment explains churn.
- Because none of the fields are correlated with each other (all |r| < 0.35, and nearly all < 0.06), the effects really are separate. They are not the same signal counted several times.

## 5. Recommendations

1. **Fix the measurement first (highest priority).**
   - Get the written definition and the business logic behind `Churned`.
   - Redefine churn from visit and scheduling data. A suggested definition is no completed visit in 12 months and no future appointment booked, applied with a single dated cut-off.
   - Reconcile `Visits_Last_Year` with `Last_Interaction_Date`.
2. **Then answer the "getting worse" question properly.** Rebuild monthly or quarterly snapshots from historical visit records and track churn by when patients joined. Until then, don't report that churn is rising.
3. **Low-regret actions the current evidence supports.** These should be checked against the corrected label and tested as pilots with control groups, not rolled out across the board.
   - **Service experience:** reduce wait times and follow up on low overall-satisfaction scores. This is the strongest and most consistent association.
   - **Billing:** fast-track the resolution of billing problems. Only 8% of patients have one, but their odds of the label are about 1.6 times higher.
   - **Portal adoption:** encourage patients to use the portal. Users have about a third lower odds. This may partly reflect which patients choose to use it, so a randomized enrolment nudge would test whether it actually causes lower churn.
   - **Access:** offer telehealth or reminder outreach for patients more than 30 miles away and for those with repeated missed appointments.
   - **First-year patients:** focus onboarding and outreach on younger and newer patients.
4. **Don't target interventions by state, specialty or insurance type.** None of these segments stands out.
