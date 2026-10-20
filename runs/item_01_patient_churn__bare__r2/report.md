# Patient Churn Assessment

**Data:** `patients.csv`, 2,000 patients, 21 fields, no missing values. The export is a single snapshot. For every row, `Last_Interaction_Date + Days_Since_Last_Visit` equals **2026-01-20**, so that is the "as-of" date.

## Bottom line

1. **This data can't tell us whether churn is getting worse.** It is a single snapshot with no churn date and no history of past churn rates. None of the time cuts I could build shows a worsening trend, and the most direct cut shows the opposite.
2. **The `Churned` flag needs checking before anyone relies on it.** It marks 68% of patients as churned, which is implausibly high for an active outpatient panel. It also doesn't line up with visit behavior (details below).
3. **Taking the flag at face value, churn is linked to many small factors, and no single one dominates.** The strongest are overall and wait-time satisfaction, portal use, billing problems, distance, out-of-pocket cost, missed appointments and short tenure. Even together they predict churn only weakly: cross-validated AUC is 0.65, where 0.5 is a coin flip.
4. **Recommendation:** first fix how churn is defined and tracked over time, then test interventions on the few factors the organization can control.

---

## 1. Is churn getting worse?

The file has no churn event date and no earlier snapshots, so we can't measure a churn *rate over time*. I tried the two time-like cuts available:

| Cut | Result |
|---|---|
| By year of last interaction | 2024: 72.0% churned · 2025: 65.1% · Jan 2026: 65.4% |
| By join cohort (as-of date minus tenure) | 2016: 68% · 2017: 58% · 2018: 61% · 2019: 71% · 2020: 66% · 2021: 70% · 2022: 77% · 2023: 71% · 2024: 68% · 2025: 76%. Bumpy, no steady upward trend. |

- **Last-interaction year:** the flagged churn rate is *lower* for recent interactions. That is also partly circular, because patients who last appeared long ago are more likely to be called churned.
- **Join cohort:** newer patients churn somewhat more. This is the normal pattern where churn risk falls with tenure (about −0.1 percentage points per month, p<0.001). It describes where patients are in their lifecycle, not a worsening trend. Each cohort also had a different amount of time to churn.

**Conclusion:** the belief that churn is worsening is **not supported by this data**, though the data can't rule it out either. Answering it properly needs churn measured the same way at several points in time, for example the monthly share of active patients who leave within 12 months.

## 2. Data-quality concerns about the outcome field

- **The rate is implausibly high:** 68.4% churned (1,367 of 2,000).
- **The flag barely tracks recency of visits:**
  - Patients seen in the last 90 days: 65.9% flagged as churned (164 patients).
  - Patients not seen for 630–730 days: 71.5% flagged as churned.
  - 275 patients with no visit in over a year are flagged as *not* churned.
- **Internal inconsistencies in the visit fields:**
  - 940 of the 996 patients whose last visit was over 365 days ago still show `Visits_Last_Year` > 0.
  - 191 patients have a last visit that predates the start of their tenure.

The business needs to confirm what `Churned` means before acting on it. Possible meanings include "left", "at risk", "did not rebook" and "transferred records", and each window would give a different rate. Until then, treat every driver estimate below as provisional.

## 3. What is associated with churn (taking the flag at face value)

**Method:** a logistic regression of churn on all available fields. The table shows how much each factor shifts the probability of churn, holding the other factors constant.

| Factor | Effect on churn probability | p |
|---|---|---|
| Overall satisfaction | −6.9 pts per 1-point increase (1–5 scale) | <0.001 |
| Billing issue present | +9.9 pts | 0.014 |
| Patient portal user | −7.7 pts | 0.001 |
| Wait-time satisfaction | −3.8 pts per point | <0.001 |
| Provider rating | −2.8 pts per point | 0.04 |
| Missed appointments | +2.0 pts per missed appointment | 0.001 |
| Distance to facility | +2.5 pts per 10 miles | <0.001 |
| Out-of-pocket cost | +0.6 pts per $100 | 0.001 |
| Tenure | −1.2 pts per year | 0.001 |
| Days since last visit | +1.8 pts per 100 days | <0.001 |
| Age | −1.4 pts per 10 years | 0.02 |
| Referrals made | −1.9 pts per referral | 0.03 |

**Raw churn rates for the same factors:**

| Comparison | Churn rate |
|---|---|
| Overall satisfaction ≤2.0 vs ≥4.5 | 78% vs 52% |
| Billing issue vs none | 77% vs 68% |
| Portal user vs non-user | 62% vs 70% |
| Farthest fifth vs closest fifth by distance (>30 mi vs ≤10.7 mi) | 72–73% vs 65% |
| Highest-cost 40% vs the rest | 72% vs 64–67% |

**No meaningful difference** (no factor clearly significant once the others are accounted for):

- State: 64–72%
- Specialty: 64–70%
- Insurance type: 67–71%
- Gender: 68% vs 69%
- Staff satisfaction

**How much the model explains:**

- Cross-validated AUC is 0.65 for logistic regression and 0.63 for gradient boosting.
- Pseudo-R² is 0.07.
- So these fields explain only a small part of who is flagged as churned. Either the flag is noisy (see section 2), or the real drivers aren't captured in this export.

**Caveat:** these are associations in observational data, not proven causes. Satisfaction and portal use, for example, may reflect patient engagement rather than cause retention.

## 4. Recommendations

1. **Fix the measurement first (highest priority).**
   - Agree a written churn definition, e.g. "no completed visit for 12+ months and no future appointment" or "records transferred".
   - Recompute the flag from visit-level data.
   - Report it monthly or quarterly so the "getting worse" question can actually be answered.
   - Reconcile the visit fields: `Visits_Last_Year` vs `Days_Since_Last_Visit`, and tenure vs last visit.
2. **Target the levers the organization controls, as small controlled pilots.** Prove each effect before scaling up.
   - **Billing:** resolve billing issues quickly and follow up with affected patients (largest single-factor effect; 157 patients affected).
   - **Portal:** drive portal enrollment, e.g. at check-in. Run this as a randomized test, because current portal users may simply be more engaged.
   - **Waits and experience:** reduce wait times and close the loop with low-satisfaction patients. A post-visit survey score of ≤2.5 should trigger outreach.
   - **Missed appointments:** reminders and easy rescheduling.
   - **Cost and distance:** offer cost estimates and payment plans to high out-of-pocket patients, and telehealth to patients more than 30 miles away.
3. **Focus retention outreach on new patients (first 12–24 months) and younger adults.** These groups show the highest flagged churn: 76% in the first year and 74% for ages 18–38.
4. **Don't reorganize by state, specialty or insurance type.** The data shows no meaningful differences across them.

## Assumptions

- The as-of date is 2026-01-20, derived from the date fields.
- Join date was estimated as the as-of date minus `Tenure_Months` × 30.44 days.
- The `Churned` field was used as provided for the driver analysis, despite the concerns in section 2.
