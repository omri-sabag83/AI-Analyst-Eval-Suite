# Patient Churn: Is It Getting Worse, What Drives It, What to Do

## Bottom line

1. **This export can't show whether churn is getting worse.** It is a single snapshot: every record lines up to one "as-of" date, 20 Jan 2026. There is no churn date and no history. A trend needs churn rates measured at several points in time, and this file doesn't have them. The few time-based views it does allow show **no worsening**. If anything, they lean the other way.
2. **The `Churned` label looks unreliable, so treat any churn rate from this file with caution.** 68.4% of patients (1,367 of 2,000) are flagged as churned. That is far above normal for an outpatient provider. **66% of patients seen in the last 90 days are also flagged churned.** The visit fields also contradict each other (details below).
3. **Within the data, the factors linked to churn are weak, but they all point the same way:** low overall satisfaction, low wait-time satisfaction, no portal use, billing problems, greater distance, higher out-of-pocket cost, more missed appointments, and shorter tenure. Together they predict churn only modestly (cross-validated AUC ≈ 0.65, where 0.5 is a coin flip). These are associations, not proven causes.
4. **Recommendation:** first fix how churn is defined and measured. Do that before funding a churn program or reporting a trend. Low-cost actions that target the strongest signals (satisfaction, wait times, billing, portal adoption) are reasonable to pilot meanwhile, as long as they are tested properly.

---

## 1. Is churn getting worse?

**What the data is:** 2,000 patients, one row each. For every row, `Last_Interaction_Date` + `Days_Since_Last_Visit` = **2026‑01‑20**. So this is one extract taken on one day, not a time series.

**Proxy views (none of them is a true trend):**

| Proxy view | Result |
|---|---|
| Churn flag by quarter of last interaction | 2024 Q1 76%, Q2 67%, Q3 75%, Q4 70%; 2025 Q1 70%, Q2 67%, Q3 58%, Q4 65%; 2026 Q1 65% (n=52) |
| Last interaction in past 6 months vs earlier | 62.6% (n=521) vs 70.4% (n=1,479) |
| Churn flag by year patients joined (from tenure) | 2016 68%, 2017 58%, 2018 61%, 2019 71%, 2020 66%, 2021 70%, 2022 77%, 2023 71%, 2024 68%, 2025 76%. Noisy, with no clear trend |

- None of these views shows churn rising over time. Patients active more recently are flagged churned *less* often. That fits churn being partly about inactivity, so it isn't evidence of improvement either.
- Newer joiners churn somewhat more. That is a tenure effect (new patients leave more readily) mixed with survivorship (long-tenure patients still on the books are, by definition, the ones who stayed). It is not evidence that things are getting worse over time.
- **Conclusion:** the belief that churn is worsening is **neither supported nor refuted** by this file. Settling it needs monthly or quarterly churn rates, each calculated the same way.

## 2. Data quality: why the churn label is in doubt

| Check | Finding |
|---|---|
| Overall churn rate | 68.4%, which is implausibly high for a functioning outpatient practice |
| Recently seen patients | 66% of patients with a visit in the last 90 days are flagged churned (n=249) |
| Churn vs. recency | Churn rises only modestly with days since last visit (≈60–66% under 1 year vs ≈71–73% over 1 year). If the label meant "stopped coming", this relationship should be much stronger |
| Visit fields disagree | 940 patients have >365 days since their last visit but report ≥1 visit in the last year. 63 report 0 visits last year but had a visit within 365 days |
| Tenure vs. recency | 191 patients have a last visit that predates their tenure start |
| Specialty vs. age | Pediatrics patients have a median age of 54 (range 18–86) |

**Assumption:** `Churned` is used as provided, because there is no definition to check it against. The business should confirm what it means: no visit in X months? A formal transfer of care? Account closure? Some of the issues above (pediatrics ages, conflicting visit counts) suggest the export may be test data, joined incorrectly, or built from fields with different definitions than their names imply.

## 3. What's associated with churn

Method: a multivariable logistic regression on all fields, with each factor adjusted for the others. I also compared simple churn rates across groups. Effects are reported as odds ratios (OR), where >1 means more churn and <1 means less.

| Factor (adjusted) | Effect | Simple churn rates |
|---|---|---|
| Overall satisfaction | OR 0.71 per point (p<0.001), the strongest single signal | 77% in the lowest fifth vs 57% in the highest |
| Portal usage | OR 0.66 (p<0.001) | 62% for users vs 70% for non-users |
| Billing issue | OR 1.62 (p=0.02) | 77% vs 68% (only 157 patients have billing issues) |
| Wait-time satisfaction | OR 0.83 per point (p<0.001) | 74% vs 63% (lowest vs highest fifth) |
| Distance to facility | OR 1.13 per 10 miles (p<0.001) | 65% under 20 mi vs 72–73% over 30 mi |
| Out-of-pocket cost | OR 1.38 per $1,000 (p=0.002) | 64–67% under $978 vs 72% above |
| Missed appointments | OR 1.08 per missed appointment (p=0.01) | 63–66% at 0–1 vs 74% at 5 |
| Tenure | OR 0.94 per year (p<0.001) | 76% in the first year vs 63% at 8–10 years |
| Provider rating, referrals, age | Small protective effects (p 0.02–0.04) | |
| State, specialty, insurance, gender, staff satisfaction | No meaningful differences | All within ≈64–72% |

**How much to trust these:**
- **The overall signal is weak.** The full model's cross-validated AUC is 0.65. A gradient-boosted model scores 0.63, so the weakness isn't because the model is too simple. Most of the variation in the label is unexplained, which fits a noisy or poorly defined outcome.
- **These are associations from observational data.** For example, portal users may simply be more engaged patients to begin with. Turning on the portal for someone won't necessarily keep them.
- The four satisfaction and rating measures barely correlate with each other (|r| ≤ 0.04). Real survey scores usually move together, which adds to the doubt about data quality.
- No single location, specialty or payer stands out, so I found no "hot spot" to target.

## 4. Recommendations

1. **Define churn and rebuild the measure (do this first).** Agree on one operational definition, such as "no completed visit in 18 months and no future appointment" or "records transferred". Recalculate the flag from the source scheduling and EHR systems, and reconcile it with the visit fields that currently conflict.
2. **Build a real trend.** Produce monthly churn-rate snapshots for at least the last 2–3 years under that definition, split by state, specialty and payer. Only then can anyone answer whether churn is getting worse.
3. **Fix the data issues listed in Section 2** (visit counts, tenure dates, specialty coding) before any churn model or dashboard is put into use.
4. **Meanwhile, run low-cost pilots on the consistent signals, tested properly** (randomized or staggered rollout, so the effect can be measured):
   - Follow up on billing issues and resolve them quickly.
   - Push portal enrollment at check-in.
   - Reduce wait times and send wait-time updates.
   - Contact patients after a missed appointment.
   - Run cost-transparency and payment-plan outreach for high out-of-pocket patients.
   - Prioritize patients in their first year and those who live more than 30 miles away (telehealth options).
5. **Don't** put large retention spending behind the belief that churn is worsening, and don't use the current model to score patients. Its predictive power is too weak, and the label it learns from is unverified.

---
*Assumptions: the as-of date is 2026‑01‑20 (worked out from the data). `Churned` is used as provided. Tenure-based join years are approximate (tenure months × 30.44 days). All figures come from `patients.csv` (n=2,000).*
