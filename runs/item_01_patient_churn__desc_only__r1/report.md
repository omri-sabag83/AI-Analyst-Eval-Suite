# Patient Churn: Assessment, Drivers, and Next Steps

## Bottom line
1. **This data can't show whether churn is getting worse.** The export is a single snapshot taken on 2026-01-20, with one row per patient and one churn flag. There is no churn history to compare against. The slices that look like a time trend (see below) don't support "getting worse", and they can't be read as a trend either way.
2. **The `Churned` label shouldn't be trusted as it stands.** It flags **68.4%** of patients as churned, which is not a believable rate for an outpatient provider. It also marks **46 of the 77 patients (60%) seen in the last 30 days** as churned. Several other fields in the export contradict each other (details below). Any churn rate taken from this file, including the 68%, should not be quoted to leadership.
3. **Within the data, the strongest drivers are experience and access:** low overall satisfaction, low wait-time satisfaction, billing issues, not using the portal, distance to the facility, out-of-pocket cost, missed appointments and short tenure. State, specialty, insurance type and gender have no meaningful independent effect. All of these effects are modest. The best model only separates churners from non-churners with an AUC of about 0.65, so the drivers are directional, not decisive.
4. **Recommendation:** first fix how churn is defined and set up monthly tracking (without that, "is it getting worse" can't be answered). Then pilot actions on the experience and access levers, with a control group.

## Data and assumptions
- 2,000 patients, 21 columns, no missing values. The patients are spread evenly across 10 states, 7 specialties and 4 insurance types.
- **Snapshot date:** `Last_Interaction_Date + Days_Since_Last_Visit` equals 2026-01-20 for every row. I assume that is the extract date, and that "last interaction" means the last visit.
- I used `Churned` as the business provided it, because no definition was supplied. Every driver finding below inherits the problems with that label.

## 1. Is churn getting worse?
The question needs churn rates for successive periods, for example the share of patients active at the start of each quarter who were lost by the end of it. The file only has the current flag, so that can't be calculated.

There are two slices that might be mistaken for a trend:

| Last interaction quarter | 2024Q1 | 2024Q2 | 2024Q3 | 2024Q4 | 2025Q1 | 2025Q2 | 2025Q3 | 2025Q4 |
|---|---|---|---|---|---|---|---|---|
| % flagged churned | 76% | 67% | 75% | 70% | 70% | 67% | 58% | 65% |

| Tenure (months) | 0–12 | 12–24 | 24–48 | 48–72 | 72–96 | 96–120 |
|---|---|---|---|---|---|---|
| % flagged churned | 76% | 68% | 74% | 68% | 66% | 63% |

- The first table drifts downward. However, it groups patients by how recently they were seen, not by when they churned. Patients seen recently would be expected to be flagged less often, so this is a recency effect, not a trend over time.
- The second table shows newer patients churning somewhat more. That points to **early-tenure risk** (onboarding), but a single snapshot can't tell this apart from "recent intake cohorts are worse".
- **Conclusion:** the data neither supports nor refutes leadership's belief. If anything, the only time-related slice moves the other way.

## 2. Data quality problems (read before using any numbers)
| Check | Result |
|---|---|
| Overall churn rate | 68.4%, implausibly high |
| Churned despite a visit in the last 30 days | 46 of 77 (60%) |
| Churn rate by days since last visit | 60–66% for patients seen within a year, 72–73% beyond a year. Recency barely moves the label. |
| Last visit more than 365 days ago but `Visits_Last_Year` > 0 | 940 of 996 patients. These fields contradict each other. |
| `Visits_Last_Year` = 0 but seen within the last 365 days | 63 patients |
| Last visit before the patient's tenure began | 191 patients |
| Satisfaction sub-scores (overall, wait, staff, provider) | Almost uncorrelated with each other (\|r\| ≤ 0.04), which is unusual for survey data |

These patterns suggest the fields come from different systems or reference dates, or that the churn flag measures something other than "stopped coming". Whoever owns the export needs to confirm what each field means.

## 3. What is associated with churn
I fitted a multivariable logistic regression on all fields, so each effect is adjusted for the others. "Odds ×" is how much the odds of being flagged churned change for the stated difference.

| Factor | Raw churn contrast | Adjusted odds × (95% CI) |
|---|---|---|
| Overall satisfaction (per +1 point) | 78% for scores ≤2.0 vs 52% for scores >4.5 | **0.71** (0.64–0.78) |
| Billing issue (yes vs no) | 77% vs 68% | **1.62** (1.08–2.43) |
| Portal user (yes vs no) | 62% vs 70% | **0.66** (0.52–0.84) |
| Wait-time satisfaction (per +1 point) | — | **0.83** (0.75–0.92) |
| Distance (per +10 miles) | 64% within 10 mi vs 73% at 40–50 mi | **1.14** (1.06–1.22) |
| Out-of-pocket cost (per +$100) | 66% under $300 vs 73% at $1,500+ | **1.03** (1.01–1.05), about 1.6× from $300 to $2,000 |
| Missed appointments (per missed visit) | 66% at 0 vs 74% at 5 | **1.08** (1.02–1.15) |
| Provider rating (per +1 point) | — | 0.86 (0.75–0.99) |
| Tenure (per +12 months) | 76% at 0–12 mo vs 63% at 96–120 mo | 0.94 (0.91–0.98) |
| Referrals made (per referral) | — | 0.91 (0.83–1.00) |
| State, specialty, insurance, gender, staff satisfaction | Range of 64–72% across groups | No independent effect (all p > 0.1) |

How far these findings can be taken:
- **They are associations, not proven causes.** For example, portal users may simply be more engaged patients to begin with.
- **The effects are small.** The model explains little (pseudo-R² 0.07, cross-validated AUC 0.65 for logistic regression and 0.63 for gradient boosting). Most of the variation in the label is unexplained, which fits the label quality concerns above.
- Billing issues carry the largest effect per patient, but they affect only 157 patients (8%). Satisfaction and distance affect everyone, so they matter more across the whole population.

## 4. Recommendations
1. **Define churn properly and measure it over time (do this first).** Agree a definition, for example "no completed visit or scheduled appointment within N months of the expected next visit". Adjust N by specialty, since a pediatrics or cardiology follow-up cycle differs from orthopedics. Rebuild the flag from visit and appointment history, then report it every month or quarter by the cohort of patients active at the start of the period. Only then can leadership answer "is it getting worse?" Also fix the field conflicts listed in section 2.
2. **Billing:** route every billing issue to fast resolution with follow-up. This is a small group with the largest risk per patient, so it's cheap to target.
3. **Portal adoption:** push enrollment at check-in and for new patients. Run it as an A/B test or staggered rollout, since the link to retention may reflect selection rather than effect.
4. **Wait times and overall experience:** follow up when a patient gives low satisfaction scores (for example, overall ≤2.5, about 29% of patients), and work on scheduling and wait times.
5. **Access and cost:** for patients who live more than 30 miles away or have high out-of-pocket costs, offer telehealth, reminders, financial counseling and payment plans. Contact patients after missed appointments.
6. **Onboarding:** add a first-year retention touchpoint, because patients in their first 12 months show the highest flagged rate.
7. **Test before scaling.** Pilot each action with a holdout group and measure the effect on the corrected churn metric. The current associations are too weak and the label too uncertain to justify large spending on their own.

*Method: Python (pandas/statsmodels/scikit-learn). Logistic regression with all fields; 5-fold cross-validated AUC. Raw rates are shares of patients flagged `Churned` = 1 within each group.*
