# Patient Churn Assessment

**Data:** `patients.csv`, 2,000 patients, 21 fields, no missing values. Every record is a snapshot taken on **2026‑01‑20** (`Last_Interaction_Date + Days_Since_Last_Visit` comes to that date for all 2,000 rows).

## Bottom line

1. **This data cannot show whether churn is getting worse, and the trend proxies that do exist do not support the claim.** The export is a single snapshot with no churn date. Patients whose last interaction was more recent are *less* likely to be flagged as churned, not more.
2. **The `Churned` label is not reliable enough to act on yet.** It flags 68% of patients as churned, including 66% of patients seen in the last 90 days. The activity fields also contradict each other for about half of the records.
3. **Patient experience and access issues are linked to higher churn, but only weakly.** The clearest signals are overall satisfaction, wait‑time satisfaction, portal use, distance, out‑of‑pocket cost and billing issues. Demographics, state, specialty and insurance type add almost nothing. Even all of these together separate churners from non‑churners only modestly (cross‑validated AUC ≈ 0.65).
4. **Recommendation:** fix the churn definition and set up time‑stamped tracking before deciding on a "churn is worsening" response. In the meantime, run low‑cost pilots on the experience levers listed in Section 4.

## 1. Is churn getting worse?

**Why the data can't answer this directly.** To measure a trend, we need churn *events* with dates, or repeated snapshots over time. This file has neither: it shows each patient's status on one day. Any "trend" we see is a cross‑sectional proxy.

**Proxy A: churn rate by date of last interaction.**

| Last interaction | 2024 Q1 | Q2 | Q3 | Q4 | 2025 Q1 | Q2 | Q3 | Q4 | 2026 Q1* |
|---|---|---|---|---|---|---|---|---|---|
| Churn rate | 76% | 67% | 75% | 70% | 70% | 67% | 58% | 65% | 65% |
| n | 218 | 231 | 256 | 241 | 220 | 276 | 254 | 252 | 52 |

*Up to 19 Jan 2026 only.

The rate is falling: the odds of being flagged churned drop by about 27% for each year‑later last interaction (OR 0.73 per year, 95% CI 0.62–0.85, p<0.001). This is mostly what you'd expect, since patients you saw recently are less likely to have left. But it is the opposite of evidence for worsening churn.

**Proxy B: churn rate by joining cohort (snapshot date minus tenure).** Recent joiners churn a little more (OR 1.06 per cohort‑year). The pattern is noisy (58%–77% across years, not monotonic). It is also the same effect as "shorter tenure → more churn": older cohorts have survived longer by definition. It does not show the organization getting worse over time.

**Supporting drivers don't show deterioration either.** Average overall satisfaction by last‑interaction year was 3.22 → 3.28 → 3.31 (2024, 2025, 2026). The billing‑issue rate was 8.6% → 7.1% → 9.6% (the 2026 figure rests on only 52 patients).

**Conclusion:** there is no evidence in this export that churn is getting worse. If leadership's belief comes from another source, such as monthly active‑patient counts, that source should be brought into the analysis.

## 2. Data quality: the outcome field needs validation

- **The label doesn't match activity.** 66% of patients seen within the last 90 days are flagged `Churned = 1`, against 72% of those not seen for 1.5–2 years. Under any usual definition (e.g., no visit in 12–18 months), recent visitors would almost all be retained. Recency barely separates the two groups: median days since last visit is 311 for retained patients and 384 for churned ones.
- **The activity fields contradict each other.**
  - 940 patients (47%) have `Visits_Last_Year > 0` but `Days_Since_Last_Visit > 365`.
  - 63 have zero visits last year but a visit within 365 days.
  - 191 have a last visit dated before they joined (`Days_Since_Last_Visit` exceeds their tenure).
- **The headline rate is implausible.** A 68% churn rate for an established outpatient panel is extremely high. It suggests the flag may mean something other than "left the organization", for example "at risk", "lapsed for one specialty", or a flag that is set and never cleared.

**Assumption:** I analysed `Churned` as given, because that is the business's outcome field, but every driver finding below inherits this uncertainty. I re‑ran the key model on only the 947 internally consistent records. The direction of the main effects held: satisfaction, wait time, portal use, distance and cost stayed significant. Billing issues and tenure lost significance.

## 3. What is associated with churn

Multivariable logistic regression on all fields. Odds ratios are per 1 standard deviation for continuous variables:

| Factor | Odds ratio (95% CI) | Churn rate, low vs high group |
|---|---|---|
| Overall satisfaction (+1 SD) | **0.71** (0.64–0.78) | 78% at ≤2.0 vs 52% at >4.5 |
| Wait‑time satisfaction (+1 SD) | 0.83 (0.75–0.92) | 72–73% at ≤3 vs 65% at >3 |
| Patient portal user | 0.66 (0.52–0.84) | 70% non‑users vs 62% users |
| Billing issue reported | 1.62 (1.08–2.43) | 68% none vs 77% with issue |
| Distance to facility (+1 SD ≈ 14 mi) | 1.20 (1.09–1.32) | 64% at <20 mi vs 73% at >30 mi |
| Out‑of‑pocket cost (+1 SD ≈ $590) | 1.21 (1.07–1.37) | 64–67% below $978 vs 72% above |
| Missed appointments (+1 SD) | 1.15 (1.03–1.28) | 63–66% at 0–1 vs 74% at 5 |
| Tenure (+1 SD ≈ 35 months) | 0.85 (0.77–0.93) | 76% in first year vs 63% at 8+ years |
| Age (+1 SD) | 0.89 (0.81–0.98) | 77% at 18–30 vs 65% at 45+ |

**No meaningful effect:** gender, state, specialty, insurance type, staff satisfaction and visit count. All p > 0.1. State rates range from 64% to 72%, and specialty rates from 64% to 70%.

**How strong this is:** together, these factors explain little (pseudo‑R² 0.07, cross‑validated AUC 0.65 for logistic regression and 0.63 for gradient boosting). These are associations from observational data, not proven causes. They point to where to look, but they are not enough for precise patient‑level targeting.

## 4. Recommendations

1. **Define and audit churn first (weeks, not months).** Agree a written definition, e.g. "no completed visit in 18 months and not deceased or transferred". Recompute the flag from visit data. Reconcile `Visits_Last_Year`, `Days_Since_Last_Visit` and tenure in the source system. Hand‑check a sample of recent visitors who are flagged as churned.
2. **Build the data needed to answer "is it getting worse?"** Get monthly snapshots, or visit‑level history with churn dates. Then track a monthly or quarterly churn rate (patients lost ÷ active patients at the start of the period) by state and specialty, ideally for at least 8 quarters back.
3. **Pilot the experience levers with controls,** since they are the most consistent signals and cheap to test:
   - shorter waits and better wait communication;
   - portal enrolment at check‑in;
   - fast billing‑issue resolution;
   - cost transparency and payment plans for high out‑of‑pocket patients;
   - missed‑appointment follow‑up and reminders;
   - telehealth or closer‑site options for patients more than 30 miles away.

   Randomise or stagger the rollout so that real impact can be measured, because portal users, for example, may simply be more engaged patients to begin with.
4. **Focus early retention on new and younger patients.** First‑year and 18–30‑year‑old patients have the highest churn rates (about 76–77%).
5. **Don't spend on state‑ or specialty‑specific programmes on the basis of this data.** Those differences are within noise.

Once the churn label is validated, the driver analysis should be re‑run. The effect sizes above could change substantially.
