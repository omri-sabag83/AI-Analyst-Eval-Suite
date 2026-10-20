# Patient Churn Assessment

## Summary

1. **This data can't tell us whether churn is getting worse.** The export is a single snapshot: one row per patient, taken on about 20 Jan 2026. It has a churned yes/no flag but no date showing *when* a patient churned, and there are no earlier snapshots to compare against. Any trend line drawn from this file would be an artefact of how the file was built. The proxies that are available don't show a worsening trend either (see §2).
2. **The `Churned` label is suspect and needs to be defined before anyone acts on it.** 68% of patients are flagged as churned, including 66% of patients who visited in the last 90 days. The visit-history fields also contradict each other for about half the rows (§1).
3. **Taking the label at face value, the drivers are about patient experience and access, not demographics.** The strongest drivers are low overall and wait-time satisfaction, distance to the facility, not using the patient portal, billing issues, missed appointments, and short tenure. State, specialty, insurance type and gender make no significant difference. Even so, the drivers together explain churn only modestly (cross-validated AUC about 0.65).
4. **Recommendation:** first fix how churn is measured, so there is a dated churn definition and a monthly time series. In parallel, run low-cost, testable pilots on the drivers that can be acted on: wait times and satisfaction recovery, portal enrolment, billing-issue resolution, and missed-appointment follow-up.

---

## 1. Data and data-quality findings

- 2,000 patients, 21 fields, no missing values. They cover 10 states, 7 specialties and 4 insurance types.
- `Last_Interaction_Date + Days_Since_Last_Visit` comes to **2026-01-20 for every row**. So the export is a point-in-time snapshot, and "days since last visit" is measured from that date. Last interactions range from Jan 2024 to Jan 2026.
- **The churn rate is implausibly high: 68.4% overall.** For an outpatient provider that would mean most of the patient base has already been lost.
- **The label doesn't line up with patient activity:**
  - Patients who visited in the last 90 days are flagged churned 66% of the time (164 of 249).
  - Patients whose last visit was 630–730 days ago are flagged churned only 71% of the time.
  - Churn barely changes with recency: 60–66% under 270 days, 71–73% over 365 days. If `Churned` meant "stopped coming", recently active patients would rarely be flagged.
  - Patients with **0 visits last year churn *less* (60%)** than patients with 12–15 visits (71%).
- **The visit fields contradict each other:**
  - 940 patients (47%) have a last visit more than 365 days ago but report one or more visits in the last year.
  - 63 patients have a visit within 365 days but report 0 visits last year.
- **Specialty and age don't match:** every Pediatrics patient is an adult (ages 18–86, median 54).

**Assumption:** I treat `Churned` as given, as the question asks, but all findings below are conditional on it. Until someone confirms what the flag means (for example, a patient who didn't rebook? who transferred records? who hasn't visited in X months?), these results should be treated as directional.

## 2. Is churn getting worse?

**We can't tell from this data.** Measuring a trend needs churn events with dates, or repeated snapshots, and this file has neither. The two proxies available don't support the "getting worse" belief:

| Last interaction (quarter) | Churn rate | n |
|---|---|---|
| 2024 Q1 | 76% | 218 |
| 2024 Q2 | 67% | 231 |
| 2024 Q3 | 75% | 256 |
| 2024 Q4 | 70% | 241 |
| 2025 Q1 | 70% | 220 |
| 2025 Q2 | 67% | 276 |
| 2025 Q3 | 58% | 254 |
| 2025 Q4 | 65% | 252 |
| 2026 Q1 (partial) | 65% | 52 |

- **By last interaction date:** patients whose last contact was more recent are *less* often churned. That pattern is partly built in, because a recent interaction implies the patient is still active. So it isn't evidence of improvement, but it isn't evidence of deterioration either.
- **By joining cohort (tenure):**
  - The newest patients (12 months' tenure or less) churn at 76%. The longest-tenured (96–108 months) churn at 58%.
  - In a single snapshot, long-tenured patients are survivors, so this gap can't be read as "newer cohorts are worse".
  - Tenure buckets between 1 and 7 years move up and down (66–77%) with no clear direction.

## 3. What is associated with churn

**Single-factor churn rates (overall rate 68%):**

| Factor | Low-risk group | High-risk group |
|---|---|---|
| Overall satisfaction | 4.5–5: **52%** | ≤2: **78%** |
| Wait-time satisfaction | >3.5: 65% | 2–2.5: 78% |
| Distance to facility | ≤20 mi: 65% | >30 mi: 73% |
| Portal usage | uses portal: 62% | no portal: 70% |
| Billing issue | none: 68% | had issue: 77% |
| Missed appointments | 0–1: 63–66% | 5: 74% |
| Out-of-pocket cost | <$500: 64–68% | >$1,000: 72–73% |
| Age | 45+: 65–67% | 18–30: 77% |
| Tenure | 8–9 yrs: 58–61% | ≤1 yr: 76% |

**Multivariable logistic regression** (all fields together; p-values in parentheses):

- **Significant drivers that raise churn:**
  - billing issue: +0.48 log-odds (p=0.02)
  - missed appointments: +0.08 per appointment (p=0.01)
  - distance: +0.013 per mile, about +0.4 over 30 miles (p<0.001)
  - out-of-pocket cost: +0.0003 per dollar (p=0.002)
  - days since last visit (p<0.001)
- **Significant drivers that lower churn:**
  - overall satisfaction: −0.34 per point (p<0.001)
  - wait-time satisfaction: −0.18 per point (p<0.001)
  - portal usage: −0.41 (p<0.001)
  - provider rating: −0.15 per point (p=0.03)
  - referrals made: −0.09 each (p=0.04)
  - tenure: −0.005 per month (p<0.001)
  - age: −0.007 per year (p=0.02)
- **Not significant:** state, specialty, insurance type, gender, staff satisfaction, and visit count.

**Risk factors stack up.** I counted five actionable flags per patient: satisfaction ≤3, more than 30 miles away, no portal use, a billing issue, and 3 or more missed appointments.

| Risk flags | Churn rate | n |
|---|---|---|
| 0 | 49% | 80 |
| 1 | 57% | 453 |
| 2 | 68% | 799 |
| 3 | 77% | 523 |
| 4+ | 83% | 145 |

**Caveats:**
- Predictive power is modest: cross-validated AUC is 0.65 for logistic regression and 0.63 for gradient boosting. Most of the variation in the label isn't explained by these fields, which fits the label problems described in §1.
- These are associations, not proven causes. For example, low satisfaction might be a symptom of patients who were already leaving rather than the reason they left.

## 4. Recommendations

1. **Define and instrument churn (highest priority).**
   - Agree on an operational definition, for example "no completed visit or scheduled appointment in 12 months for a patient who isn't deceased, moved away or discharged."
   - Record a **churn date** and produce a monthly churn rate by state and specialty.
   - Without this, the question "is it getting worse?" can't be answered, and today's 68% figure shouldn't be reported to leadership.
2. **Fix the source data.**
   - Reconcile `Visits_Last_Year` with `Days_Since_Last_Visit`, which contradict each other for 47% of rows.
   - Check how Specialty is assigned (adult Pediatrics patients).
   - Confirm how the `Churned` flag is generated.
3. **Run pilots now on the drivers that can be acted on, each with a control group so impact can be measured:**
   - **Wait times and satisfaction recovery:** follow up on low satisfaction scores (≤3) within days. Satisfaction is the strongest single association, a 26-point spread between the lowest and highest groups.
   - **Portal enrolment** during visits. Portal users churn about 8 points less, and enrolment is cheap to push.
   - **Billing-issue resolution** with a named owner and a time limit.
   - **Missed-appointment outreach:** reminders, and proactive rebooking after a no-show.
   - **Access for distant patients (>30 miles):** telehealth options.
   - **Onboarding for patients in their first year,** who are the highest-churn tenure group.
4. **Don't target by state, specialty or insurance type.** Once the other factors are accounted for, those differences aren't significant.
5. **Once a reliable, dated churn label exists,** rebuild the risk model and use the risk-flag count above as a starting point for prioritising outreach.

*Method: Python (pandas, statsmodels, scikit-learn) on `patients.csv` only. Regression coefficients are log-odds from a logistic regression on all 2,000 patients; AUCs come from 5-fold cross-validation.*
