# Patient Churn: Is It Getting Worse, and What Drives It?

**Data:** `patients.csv`, 2,000 patients, 21 fields, one row per patient. Nothing is missing. All `Last_Interaction_Date + Days_Since_Last_Visit` values land on the same date, **2026‑01‑20**, so I treat the export as a single snapshot taken that day.

## Bottom line

1. **This export can't show whether churn is getting worse.** It is one snapshot with no churn date and no history of the flag. The two time cuts it does allow point in opposite directions, and both are explained by how the data was built, not by a change in behaviour. Neither supports the claim that churn is getting worse. Neither rules it out.
2. **The `Churned` flag looks unreliable, so treat every number below with caution.** It marks **68% of patients as churned**, which is far too high for an outpatient provider. It also marks **66% of patients seen in the last 90 days** as churned, and the activity fields contradict each other (details below). Before anyone acts on a churn rate, someone needs to confirm what the flag means.
3. **Taking the flag at face value, the associations are modest but consistent.** Lower overall and wait-time satisfaction, billing issues, not using the portal, living farther away, missed appointments, higher out-of-pocket cost and shorter tenure all go with more churn. State, specialty, insurance type and gender don't matter. Even with every field included, a model separates churners from non-churners only weakly (cross-validated AUC 0.65), so most of what drives churn isn't in this data.

## 1. Data-quality problems (read first)

| Check | Result | Why it matters |
|---|---|---|
| Overall churn rate | 1,367 / 2,000 = **68.4%** | Not plausible as annual outpatient attrition. The flag probably means something broader, such as "ever lapsed". |
| Churn among patients seen in the last 90 days | **66%** (164 / 249); 46 of the 77 seen in the last 30 days | Patients who were just seen are labelled churned at almost the overall rate. |
| Last visit more than 365 days ago, yet `Visits_Last_Year` > 0 | **940 of 996** | The activity fields contradict each other: one of them has the wrong definition or the wrong window. |
| `Visits_Last_Year` = 0, yet last visit within 365 days | 63 | Same inconsistency in the other direction. |
| Tenure shorter than days since last visit | 191 | The patient's last visit would fall before they joined. |
| Patients not seen for more than a year | 275 of 996 are flagged **not** churned | If churn meant "inactive for 12 months", these would all be 1. |

**Assumption:** I analysed `Churned` exactly as supplied, as the brief asks. But churn barely rises with time since last visit (60–66% for visits under 9 months ago vs. 71–73% for visits over 12 months ago). That suggests the flag isn't a recency-based churn definition, and it may be partly noise.

## 2. Is churn getting worse?

There is no churn date and no earlier snapshot, so a true trend can't be measured. I tried the two possible proxies:

**a) Churn by quarter of last interaction.** This shows churn *falling*: 2024 = 72.0% (n=946), 2025 = 65.1% (n=1,002); by quarter, from 76% in 2024 Q1 to 58–65% in late 2025 (logit slope p<0.001). This is **not a trend in the churn rate**. Patients whose last contact was long ago are, unsurprisingly, more often flagged as churned. Sorting patients by last contact really sorts them by how recently they were active, not by when they churned.

**b) Churn by join cohort** (estimated from tenure). Recent joiners churn more: 75.6% in the first 12 months of tenure vs. 63.3% at 8–10 years (each extra year of tenure: log-odds −0.059, p<0.001). This **also doesn't show worsening**. Long-tenure patients who are still in the export are by definition the ones who stayed (survivorship). New patients churning more is normal in any year.

**Conclusion:** the data neither supports nor rules out "churn is getting worse". To answer that question, the organization needs the churn rate per period, calculated the same way each time (see Recommendations).

## 3. What is associated with churn

Univariate rates, followed by a multivariable logistic regression that includes all fields (n=2,000). These are **associations from a single snapshot, not proven causes.**

| Factor | Churn rate by group | Adjusted odds ratio (p) |
|---|---|---|
| Overall satisfaction | 77% (lowest fifth, ≤2.2) → 57% (highest fifth, >4.3) | 0.71 per point (p<0.001), the strongest factor |
| Wait-time satisfaction | lower → more churn | 0.83 per point (p<0.001) |
| Provider rating | lower → more churn | 0.86 per point (p=0.03) |
| Billing issue on record | 77% vs 68% (n=157 with an issue) | 1.62 (p=0.02) |
| Patient-portal use | 62% users vs 70% non-users | 0.66 (p<0.001) |
| Distance to facility | 64–65% (<20 mi) → 72–73% (>30 mi) | 1.13 per 10 mi (p<0.001) |
| Out-of-pocket cost | 67% (lowest quarter) → 72% (top quarter) | 1.03 per $100 (p=0.002) |
| Missed appointments | 63–66% (0–1) → 74% (5) | 1.08 per missed appt (p=0.01) |
| Tenure | 76% (<1 yr) → 63% (8–10 yrs) | 0.94 per year (p<0.001) |
| Referrals made, age | small protective effects | p≈0.02–0.04 |
| State, specialty, insurance, gender, staff satisfaction, visit count | no meaningful difference (e.g. state 64–72%, specialty 64–70%) | all p>0.1 |

**How much this explains:** cross-validated AUC is **0.65** for logistic regression and 0.63 for gradient boosting. Every effect is real but small, and together they explain little. That fits with the label being noisy, with the real drivers being absent from the export, or with both.

**Caveats:** portal use and referrals probably reflect engagement rather than cause retention. Pushing portal sign-ups won't necessarily cut churn. Satisfaction scores may have been recorded after the patient had already disengaged.

## 4. Recommendations

1. **Fix the measurement before treating churn as worsening.** Agree a written churn definition (for example, "no visit or scheduled appointment in 12 months and not discharged by plan of care"). Then recalculate the churn rate for each quarter over the last 2–3 years, applying the same definition each time. That is the only way to test leadership's belief.
2. **Have the data owner reconcile the activity fields.** In particular, `Visits_Last_Year` vs `Days_Since_Last_Visit`, and tenure vs last visit. Add a churn date to the export.
3. **Pilot changes on the levers the organization controls, as experiments (not company-wide rollouts):**
   - **Wait times and the overall experience**, the largest and most consistent signal.
   - **Fixing billing problems**: a targeted follow-up for the 8% of patients with a billing issue, who churn about 9 points more often.
   - **Access for patients far from a facility**: telehealth or reminder outreach for those over 30 miles away.
   - **Onboarding in the first year**, when churn is highest.
   - **No-show follow-up** after two or more missed appointments.

   Randomise or stagger each pilot so its effect can be measured. The associations above don't prove that any of these will work.
4. **Don't put money into state-, specialty- or insurance-specific retention programmes.** The data shows no difference there.
