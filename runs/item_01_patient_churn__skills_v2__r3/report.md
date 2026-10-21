# Patient Churn: Is It Getting Worse, What Drives It, What to Do Next

## Bottom line

1. **This data can't show whether churn is getting worse.** The export is one snapshot. Every record is as of the same date, **2026-01-20** (Last_Interaction_Date + Days_Since_Last_Visit gives that date for all 2,000 rows). It contains no churn history. The two time-like views I could build both suggest a trend, but each one is just another patient attribute (tenure or recency) relabelled as time. Neither tells us whether churn is rising.
2. **The `Churned` label needs to be checked before anyone acts on it.** It flags **68% of patients as churned**, which is not believable for an outpatient provider. It flags **60% of patients seen in the last 30 days** as churned. Several other fields also contradict each other (details below). Nobody has documented what "churned" means here.
3. **The drivers we can see are real but weak.** The strongest are low overall satisfaction, billing issues, not using the portal, low wait-time satisfaction, distance, missed appointments and out-of-pocket cost. Each one shifts the churn flag by about 3–11 percentage points. Together they explain little: a model using all fields reaches a cross-validated AUC of only about 0.63–0.65. **State, specialty, insurance type and gender make no detectable difference.**
4. **Recommendation:** first fix the measurement, then act on the drivers. Agree a written churn definition, rebuild the label from visit history, and start keeping monthly snapshots so a trend can actually be measured. In the meantime, the low-cost and low-regret steps are: follow up on billing problems, increase portal adoption, and follow up with patients who report low satisfaction.

---

## 1. The data and its quality problems (read this first)

- 2,000 patients, one row each. No missing values and no duplicate IDs.
- Patients come from 10 states, 7 specialties and 4 insurance types. Last interactions range from 2024-01-21 to 2026-01-19.

**Consistency problems I found:**

| Check | Result | Why it matters |
|---|---|---|
| Churn rate | 68.4% (1,367 / 2,000) | Far above any believable annual attrition for outpatient care. The label probably isn't "patient left" in the usual sense. |
| Patients seen ≤30 days ago flagged churned | 60% (46 / 77) | Someone seen last month is hard to call churned. |
| Churn rate by days since last visit | 66% (0–90 days) vs 71% (630–730 days) | Recency hardly changes the flag. That's unexpected if churn means "stopped coming". |
| Last visit >365 days ago but Visits_Last_Year > 0 | 94% of 996 such patients | These two fields can't both be true. |
| Days since last visit > tenure | 191 patients | The last visit falls before the patient joined. |
| Visits_Last_Year = 0 but a visit within the last 365 days | 63 patients | Another contradiction. |
| Correlations among behavioural fields | ~0 (e.g. Days_Since_Last_Visit vs Visits_Last_Year r = 0.02) | Real visit data would be strongly correlated. This suggests the fields come from different sources, different windows, or are partly synthetic. |

**Assumption:** I analysed `Churned` as the business supplied it. All the findings below describe what goes with *this flag*. They may not describe actual patient loss.

## 2. Is churn getting worse?

**Finding: we can't tell from this data. Nothing in it supports or contradicts the claim.**

To measure a trend, you need churn rates for the same population at two or more points in time. This file gives each patient's status at a single point in time. I tried the two available proxies:

- **By join cohort** (join date estimated as the snapshot date minus tenure): recently joined patients are flagged more often. The logistic slope is +0.06 log-odds per year (p < 0.001), about 76% for 2025 joiners versus about 58–68% for 2016–2018 joiners. However, join year is just tenure measured backwards. Long-tenure patients are by definition the ones who stayed. This is **survivorship**: established patients churn less than new ones. It is not a sign that the business is getting worse.
- **By quarter of last interaction**: churn is lower for recent quarters (about 76% in 2024Q1, about 58–65% in 2025Q3–2026Q1; p < 0.001). However, this proxy is identical to days since last visit (r = 1.0). It only says that recently seen patients are slightly less likely to be flagged. It points the opposite way from leadership's belief, and it is just as mechanical.

Neither proxy separates calendar time from patient attributes. **If leadership believes churn is worsening, that belief must come from a source outside this export. That source should be identified and checked against the definition issues in Section 1.**

## 3. What is associated with the churn flag

I used three methods: raw comparisons with 95% confidence intervals, a logistic regression including all fields, and average marginal effects. All three point to the same factors. The effects are associations measured at one point in time. They are not proven causes.

| Factor | Raw comparison (churn rate) | Adjusted effect* |
|---|---|---|
| Overall satisfaction | 78% at ≤2.0 vs 52% at 4.5–5.0; <2.5 vs rest: +11.1 pp ± 4.3 | −7.0 pp per 1 SD (p < 0.001), the strongest continuous factor |
| Billing issue (n = 157) | 77% vs 68%: +9.5 pp ± 6.9 | +9.9 pp (p = 0.01) |
| No portal use | 70% vs 62%: +8.4 pp ± 5.2 | −7.7 pp for portal users (p = 0.001) |
| Wait-time satisfaction <2.5 | 74% vs 67%: +7.1 pp ± 4.5 | −3.8 pp per SD (p < 0.001) |
| Distance >30 miles | 73% vs 66%: +7.1 pp ± 4.1 | +3.5 pp per SD (p < 0.001) |
| ≥3 missed appointments | 73% vs 66%: +6.9 pp ± 4.1 | +3.3 pp per SD (p = 0.001) |
| Out-of-pocket cost | top 2 quintiles about 72% vs about 66% | +3.4 pp per SD (p < 0.001) |
| Tenure | first 2 years 72% vs 68% (not significant raw) | −3.4 pp per SD (p < 0.001) |
| Age, provider rating, referrals | small | about −2 pp per SD each (p ≈ 0.02–0.04) |
| State, specialty, insurance, gender, staff satisfaction | rates fall between 64% and 72% across all groups | none significant |

\*Average marginal effect from the multivariable logistic model. "pp" means percentage points; "SD" means one standard deviation of the factor.

**How much this explains:** pseudo-R² = 0.066. Cross-validated AUC is 0.65 for logistic regression and 0.63 for gradient boosting. These factors are real but explain only a small share of who gets flagged. Most of the variation in the label isn't explained by anything in this file, which fits the label quality concerns above. A churn-risk score built on this data would not be good enough to target outreach to individual patients.

**What does not drive it:** no region, specialty or payer stands out. Churn here is not a problem of one state or one service line, so programmes aimed at a particular location would not be supported by this data.

## 4. Recommendations

**Step 1: fix the measurement (prerequisite, about 2–4 weeks)**
1. **Write down the definition of `Churned`.** It should say what event counts, over what window, and which system sets it. Then rebuild the flag directly from the visit and appointment history, for example "no completed visit in 18 months while not deceased, transferred or aged out". Check the rebuilt flag against the current one. Patients who were seen recently but are flagged churned are the obvious place to start.
2. **Reconcile the visit fields.** Visits_Last_Year, Days_Since_Last_Visit and Tenure contradict each other in a large share of rows. Find out which source system each one comes from.
3. **Start keeping history.** Store a monthly snapshot, or simply use the dated visit records, so churn can be reported by month and by cohort, such as 12-month retention for patients who joined in 2024 vs 2025. That is the only way to answer "is it getting worse?".

**Step 2: low-regret actions on the visible drivers (can start now)**
These are worth doing even if the label turns out to be wrong, because each one is good patient experience in its own right.
- **Billing:** resolve billing issues quickly and follow up with each affected patient. The group is small (8% of patients) but has the largest per-patient effect.
- **Portal adoption:** only 21% of patients use the portal. Push sign-up at check-in. *Caveat:* portal users may simply be more engaged patients to begin with, so pilot this with a control group rather than assuming the 8 pp gap will close.
- **Satisfaction follow-up:** contact patients whose overall or wait-time satisfaction score is 2.5 or below, and look at what drives wait times.
- **Access and cost:** for patients more than 30 miles away or with high out-of-pocket costs, test telehealth options and cost-estimate or payment-plan offers.

**Step 3: evaluate properly.** Run the portal and satisfaction-outreach changes as randomised or staggered pilots, and measure them against the rebuilt churn metric. The figures in Section 3 are rough upper estimates of the possible effect, not forecasts.

## Assumptions and limitations
- `Churned` is taken as given. Its definition is unknown and, based on the checks above, questionable.
- The snapshot date (2026-01-20) is worked out from the data. Join dates are approximate (tenure × 30.44 days).
- All findings are associations from data at a single point in time. None of them is a causal estimate.
- Effects in percentage points are averages across the population. Confidence intervals are 95% normal approximations.
