# Patient Churn: Is It Getting Worse, What Drives It, and What to Do Next

**Data:** `patients.csv`, 2,000 patients, 21 fields, with no missing values. Every record is a single snapshot taken on **2026‑01‑20**. I derived this date because `Last_Interaction_Date + Days_Since_Last_Visit` gives 2026‑01‑20 for all 2,000 rows.

## Bottom line

1. **This export cannot show whether churn is getting worse.** It is one snapshot. It has no churn date and no earlier snapshot, so there is no churn rate over time to compare. Both trend measures I could build from it are distorted by how they are constructed, and they point in opposite directions (details below). The belief that churn is rising is **neither confirmed nor ruled out**.
2. **The `Churned` label needs checking before anyone acts on it.** It marks **68% of patients** as churned. That is very high for an outpatient provider. It also barely tracks how recently patients were seen: **60% of patients seen in the last 30 days are flagged as churned**, against 72% of those not seen for more than a year. Whatever the label measures, it is not "stopped coming".
3. **Taking the label as given, the factors linked to it are about patient experience and access, not who the patient is.** Lower overall satisfaction, lower wait-time satisfaction, billing problems, not using the portal, living farther away, higher out-of-pocket cost, more missed appointments and shorter tenure all go with higher churn. State, specialty, insurance type and gender show no meaningful difference. All of these links are **weak**: the best model separates churners from non-churners only modestly (cross-validated AUC ≈ 0.65).
4. **Recommendation:** first fix the churn definition and start recording churn over time (this is cheap and fast). Then run small, measured pilots on the levers that can be acted on: resolving billing issues, reducing wait times, and getting patients onto the portal.

---

## 1. Is churn getting worse?

The data has no churn date, so I tried the only two proxies available:

| Proxy | What it shows | Why it isn't a trend |
|---|---|---|
| Churn rate by quarter of **last interaction** | Falls from 76% (2024 Q1) to about 65% (2025 Q4) (logit slope p < 0.001) | This is built in. Patients whose last contact was long ago are more likely to have left. It says nothing about whether the churn rate is changing. |
| Churn rate by **join year** (snapshot date minus tenure) | Rises slightly: about 58–68% for 2016–2018 joiners vs 68–77% for 2022–2025 joiners | This mixes the join year with tenure. Newer patients churn more almost everywhere. Also, if churned patients' tenure stopped when they left, older groups appear better than they really were. |

**Conclusion:** the two proxies point in opposite directions and both are artefacts of how they are built. Answering "is it getting worse" needs repeated snapshots (for example monthly) or a churn date for each patient.

## 2. Data-quality issues to resolve first

- **Implausible base rate:** 1,367 of 2,000 patients (68.4%) are flagged as churned. If that were real, the organisation would be losing most of its patients.
- **The label is unrelated to recency:**

  | Days since last visit | 0–90 | 91–180 | 181–270 | 271–365 | 366–450 | 451–540 | 541–630 | 631–730 |
  |---|---|---|---|---|---|---|---|---|
  | Churn rate | 66% | 60% | 65% | 67% | 72% | 73% | 73% | 71% |

  Of the 77 patients seen in the last 30 days, 60% are marked as churned. The label may mean something else (a stated intent to leave, a transfer request, a risk score, or a mix of definitions across sites). **I have taken the label as given in the analysis below**, but this question needs an answer from whoever owns the field.
- **Fields that contradict each other:** 940 patients (47%) were last seen more than 365 days ago yet show `Visits_Last_Year > 0`. Either `Visits_Last_Year` covers a different window or one of the fields is wrong. This also weakens any finding that relies on visit counts.

## 3. What is associated with churn (taking the label as given)

**Method:** I fitted a logistic regression on all 18 patient fields (state, specialty and insurance treated as categories). The table shows average marginal effects: how much the churn rate changes, in percentage points, for a typical shift in each factor. The four satisfaction measures are almost uncorrelated with each other (|r| < 0.05), so their separate effects can be told apart. To check, I fitted a gradient-boosting model on the same fields. It did not do better than the regression (AUC 0.63 vs 0.65), so the simple model captures most of the signal.

| Factor (holding the others fixed) | Change in churn probability | p-value | Simple comparison |
|---|---|---|---|
| Billing issue (yes vs no) | **+9.7 pp** | 0.017 | 77% vs 68% (only 157 patients have a billing issue) |
| Portal user (yes vs no) | **−8.2 pp** | <0.001 | 62% vs 70% |
| Overall satisfaction (+1 SD ≈ 1 point) | **−6.9 pp** | <0.001 | bottom quarter 76% → top quarter 58% |
| Days since last visit (+1 SD ≈ 213 days) | +3.8 pp | <0.001 | see table above |
| Wait-time satisfaction (+1 SD) | −3.8 pp | <0.001 | 74% → 64% |
| Out-of-pocket cost (+1 SD ≈ $590) | +3.7 pp | 0.002 | 67% → 72% (top quarter) |
| Distance to facility (+1 SD ≈ 14 mi) | +3.6 pp | <0.001 | 63% (<13 mi) → 73% (>37 mi) |
| Tenure (+1 SD ≈ 35 months) | −3.4 pp | <0.001 | 76% (≤12 mo) → 63% (>90 mo) |
| Missed appointments (+1 SD ≈ 1.7) | +3.2 pp | 0.002 | 66% (0 missed) → 74% (5 missed) |
| Age, provider rating, referrals made | about −2 pp each | 0.02–0.04 | weak |
| State, specialty, insurance type, gender, staff satisfaction | no significant effect | — | range about 64–72% |

**How to read this:**
- These are **associations, not proven causes**. Portal use, for example, may mark patients who are already engaged rather than cause them to stay.
- The **effects are modest** and the model explains little (pseudo‑R² = 0.07). No single factor accounts for churn, and none would make a good tool for flagging individual patients.
- Several factors are **outcomes as much as causes**. Days since last visit and missed appointments probably reflect patients who are already drifting away, not the reason they leave.
- The factors the organisation can act on are **satisfaction (overall and wait time), billing problems, portal adoption and cost**. Distance and tenure are better used to decide who to target than as things to change.

## 4. Recommendations

1. **Define churn and audit the label (next 2–4 weeks).** Agree on one written definition with leadership, for example "no completed visit in 18 months and no future appointment booked". Recompute the flag from appointment records and reconcile it with the current field. Fix the conflict between `Visits_Last_Year` and `Days_Since_Last_Visit`.
2. **Start measuring churn over time.** Store a monthly snapshot, or record a churn date for each patient. Then report churn monthly or quarterly by group of patients, so that "getting worse" can actually be tested. Until then, nobody should claim churn is rising or falling.
3. **Run targeted pilots with control groups, not organisation-wide programmes.** Re-check the factors first using the corrected label.
   - **Billing issues:** proactively resolve open billing issues (a small group with the largest gap, +10 pp).
   - **Portal enrollment:** run a randomised outreach campaign. This tests whether the portal *causes* retention or only reflects engagement.
   - **Wait times and overall experience:** focus on sites or clinics with the lowest scores, and follow up with patients who give low scores.
   - **Cost and distance:** for high out-of-pocket or distant patients, test payment plans or financial counselling, and telehealth options.
4. **Don't spread resources by state, specialty or insurance type.** None of them show a meaningful difference in churn.

## Assumptions and limitations
- The snapshot date is 2026‑01‑20, derived from the data.
- Join date is approximated as the snapshot date minus `Tenure_Months` (30.44 days per month).
- `Churned` is used as provided, even though the evidence above suggests it does not measure lapsed attendance.
- All findings come from one cross-section. They show associations, not causes.
