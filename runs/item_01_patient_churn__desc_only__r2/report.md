# Patient Churn Assessment

## Bottom line

1. **This data can't show whether churn is getting worse.** The export is a single snapshot taken on one day (every record's `Last_Interaction_Date + Days_Since_Last_Visit` = **2026-01-20**). It has no churn date and no earlier snapshots, so there's no time series of churn to look at. The proxies we do have don't show churn worsening. If anything, they point slightly the other way.
2. **The `Churned` flag shouldn't be trusted as it stands.** It marks **68% of patients** (1,367 of 2,000) as churned. That includes **66% of patients seen in the last 90 days**. Several other fields contradict each other too (details below). Before any churn number goes to leadership, the business needs to say how this flag is defined.
3. **The drivers that do show up are modest and consistent.** Within this flag, churn is higher with low overall satisfaction, low wait-time satisfaction, longer distance to the facility, billing issues, not using the portal, higher out-of-pocket cost, more missed appointments, shorter tenure and younger age. State, specialty, insurance type and gender make no meaningful difference. Taken together these factors predict churn only weakly (cross-validated AUC ≈ 0.65), so most of what the flag captures isn't explained by this data.

**Recommendation:** First fix the definition of churn and start tracking it over time. In parallel, run low-cost, measurable pilots on the levers that recur in the data: satisfaction and wait times, billing problems, and portal adoption.

---

## 1. Is churn getting worse?

**What the data is.** There are 2,000 patients, one row each, and no missing values. Last interaction dates run from 2024-01-21 to 2026-01-19, and every record's "days since last visit" counts back to the same export date, 2026-01-20. So we have one cross-section. We don't have a churn event date or a churn rate measured at different points in time.

**Proxies tried. None shows churn worsening:**

| Proxy | Result |
|---|---|
| Churn rate by year of last interaction | 2024: 72.0% (n=946) · 2025: 65.1% (n=1,002) · Jan 2026: 65.4% (n=52) |
| By quarter of last interaction | 76% in 2024Q1, falling to 58–65% in 2025Q3–2026Q1 (differences are statistically significant, p<0.001) |
| By year the patient joined (from tenure) | Recent cohorts are higher: 2022–2025 joiners at 68–77% vs 2016–2018 joiners at 58–68% |

**How to read these:**
- The last-interaction trend shows lower churn for recent dates. That's mostly what you'd expect by construction: patients seen recently have had less time to be labelled churned. So this isn't evidence that churn is improving, and it's certainly not evidence that it's getting worse.
- Recent joiners churning more could mean newer cohorts are worse. It's equally explained by new patients always churning more than established ones (tenure effect). With one snapshot the two explanations can't be separated.

**Conclusion:** Leadership's belief can't be confirmed or refuted with this export. Showing a trend needs churn measured the same way at several points in time (for example, the 12-month retention rate of each quarterly cohort).

## 2. Data quality: the `Churned` label is questionable

| Check | Finding |
|---|---|
| Base rate | 68.4% flagged churned. That's implausibly high for an outpatient provider that is still operating. |
| Recency vs. label | Patients seen in the **last 90 days** are 66% churned. Patients not seen in **1–2 years** are 72% churned. Recency barely separates the groups. |
| Visits vs. recency | 940 patients report ≥1 visit in the last year but a last visit more than 365 days ago. These can't both be true. |
| Tenure vs. recency | 191 patients have a "days since last visit" longer than their entire tenure. |

**Assumption:** I analyzed `Churned` as provided. Every driver finding below describes this flag, which may not match true patient loss. The flag might mean something narrower or broader, such as "at risk", "didn't rebook within X days" or "switched primary provider". The contradictions above suggest that some fields (`Visits_Last_Year`, `Days_Since_Last_Visit`, `Tenure_Months`) were generated or joined inconsistently.

## 3. What is associated with churn

I used a multivariable logistic regression on all fields, so each factor's effect is estimated with the others held constant. Below are the raw churn rates for the factors that remained significant in the model (p<0.05):

| Factor | Low group → high group churn rate | Direction |
|---|---|---|
| Overall satisfaction (quintiles) | 77% (≤2.2) → 57% (>4.3) | Strongest single factor |
| Wait-time satisfaction | 74% (≤2.3) → 63% (>4.3) | Independent of overall satisfaction (correlation 0.04) |
| Both overall and wait-time satisfaction <2.9 | **81%** (n=297) vs 61% when both ≥4 (n=203) | Combined high-risk group |
| Distance to facility | 65% (<11 mi) → 72% (>30 mi) | |
| Billing issue | 68% without → **77%** with (n=157) | |
| Patient portal use | 70% non-users → **62%** users (n=412) | |
| Out-of-pocket cost | 64–67% (<$978) → 72% (>$978) | |
| Missed appointments | 63–66% (0–1) → 74% (5) | |
| Tenure | 76% (≤12 months) → 63% (8–10 years) | |
| Age | 74% (18–38) → 64–69% (49+) | |
| Provider rating, referrals made | Small protective effects | |

**Not drivers:** state, specialty, insurance type and gender. None of them are significant once the other factors are controlled for, and the raw rates fall in a narrow 64–72% band. Staff satisfaction and visit count are also not significant.

**Strength of evidence:** the full model's cross-validated AUC is 0.65 (0.63 for gradient boosting). These factors shift churn risk by roughly 10–20 percentage points between extreme groups. They are not strong enough to identify individual churners reliably. All of this is correlation from a single snapshot. Low satisfaction might, for example, be measured *after* patients had already disengaged, so these are candidate levers to test, not proven causes.

## 4. Recommendations

1. **Define churn before acting on it (highest priority).** Agree on an operational definition, for example "no completed visit and no future appointment within 12 months of the last visit, excluding deceased, moved and discharged patients". Recompute the flag on that definition, and reconcile the inconsistent visit, recency and tenure fields at the source.
2. **Build a trend measure.** Keep monthly snapshots, or reconstruct visit histories, so retention can be tracked by join cohort and by quarter. Only then can "is it getting worse?" be answered. Compare first-year retention across cohorts to separate genuine deterioration from the normal pattern of new patients leaving more often.
3. **Pilot the levers the data points to. Each pilot is cheap and can be tested against a control group:**
   - **Wait times and service recovery:** follow up with patients who give low overall or wait-time satisfaction scores. The group with both scores low (≈15% of patients) churns at 81%.
   - **Billing:** resolve billing issues quickly and proactively, and be upfront about cost estimates for patients paying more than about $1,000 out of pocket.
   - **Portal adoption:** encourage enrolment, with reminders and self-scheduling. Users churn about 8 points less, though part of this is probably self-selection, so test it with a randomized rollout.
   - **Access:** offer telehealth or reminder outreach to patients more than 30 miles from a facility and to those with repeated missed appointments.
   - **Onboarding:** first-year patients have the highest churn, so a structured follow-up after the first visit is worth testing.
4. **Don't target by state, specialty or insurance.** The data gives no basis for it.

*Method notes: pandas/statsmodels/scikit-learn. Logistic regression included all 19 predictors (categoricals dummy-coded). Cross-validated AUC uses 5 folds. Rates are unadjusted percentages; significance comes from the multivariable model.*
