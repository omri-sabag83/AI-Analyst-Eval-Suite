# Patient churn: is it getting worse, and what drives it?

## Bottom line

1. **This export can't show that churn is getting worse, and nothing in it suggests it is.** The file is one snapshot taken on 2026-01-20 and has no churn date. Grouped by the quarter of each patient's last interaction, the number of churned patients is flat at about 150–190 a quarter. The churn rate drifts *down*, from about 72% in 2024 to about 62–65% in late 2025. That fall is most likely a recency artefact, not an improvement. To judge the trend, the organisation needs a churn date or monthly snapshots.
2. **The churn label needs checking before anyone acts on it.** 68% of patients are flagged as churned, which is implausibly high for an outpatient provider. 60% of patients seen in the last 30 days are also flagged. Until the definition is confirmed, read every figure here as describing this extract only, not the patient population.
3. **The factors linked to churn are experience and access, not segment.** Lower overall satisfaction and wait-time satisfaction, billing problems, not using the portal, longer distance, higher out-of-pocket cost, missed appointments and shorter tenure all go with more churn. State, specialty, insurance type and gender show no meaningful difference. These links are real but **weak**: a model using every field ranks churners only modestly better than chance (AUC about 0.65).
4. **Recommendation:** first fix the measurement (definition, dates, monthly tracking). Then run small, controlled pilots on the two strongest levers, patient experience (satisfaction and wait times) and the billing/portal friction points. A large retention programme isn't justified on this evidence yet.

---

## Data and method (read first)

- **Grain:** one row per patient. 2,000 patients and 21 columns, with no missing values and no duplicate IDs.
- **Time window:** every row satisfies `Last_Interaction_Date + Days_Since_Last_Visit = 2026-01-20`, so this is a single as-of snapshot. Last interactions run from 2024-01-21 to 2026-01-19. 2026Q1 has only 19 days (n=52) and is a partial period.
- **The outcome has no definition and no date.** `Churned` comes from the business without a written definition, and no column records *when* a patient churned.
- **Data-quality red flags:**
  - **Base rate:** 1,367 of 2,000 patients (68.4%) are flagged as churned.
  - **Recently seen patients flagged as churned:** 46 of the 77 patients seen in the last 30 days (60%) are flagged. So are 66% of those seen in the last 90 days (n=249). If churn meant inactivity, this shouldn't happen.
  - **Contradictory visit fields:** 940 of the 996 patients whose last visit was more than 365 days ago still show `Visits_Last_Year > 0`.
  - **Visit before joining:** 191 patients' last visit falls before their tenure start.
  - Taken together, the label and the activity fields may be unreliable or may follow rules we can't see. Possibly the extract isn't a random sample of patients either. Every figure below therefore describes this extract only.
- **Methods:** churn rates by segment (with n), and a multivariable logistic regression on all fields. I left out the recency fields (`Days_Since_Last_Visit`, `Last_Interaction_Date`) because they are tied to the snapshot date and to the outcome itself. Including them didn't change the other results. I cross-checked the regression with a random forest using permutation importance, and both agree on the top factor. Both models are weak (cross-validated AUC 0.65 for the regression, 0.64 for the forest).
- **Claim tags:** [OBS] = computed from the data. [HYP] = a plausible explanation the data doesn't prove. [CON] = the reading the evidence best supports.

---

## 1. Is churn getting worse?

[OBS] Churned patients by quarter of last interaction:

| Quarter | Churned | Patients | Churn rate |
|---|---|---|---|
| 2024Q1 | 166 | 218 | 76% |
| 2024Q2 | 154 | 231 | 67% |
| 2024Q3 | 193 | 256 | 75% |
| 2024Q4 | 168 | 241 | 70% |
| 2025Q1 | 155 | 220 | 70% |
| 2025Q2 | 185 | 276 | 67% |
| 2025Q3 | 147 | 254 | 58% |
| 2025Q4 | 165 | 252 | 65% |
| 2026Q1 (partial, 19 days) | 34 | 52 | 65% |

- [OBS] Counts are flat and show no significant trend. The rate *falls* over time: a regression of churn on date gives −0.32 log-odds per year, p≈0.0001.
- [HYP] The falling rate is probably not a real improvement. Patients whose last contact is more recent have had less time to be classed as churned (right-censoring), so recent quarters are bound to look better.
- [OBS] By tenure-start year, churn ranges from 58% (2017 starters) to 77% (2022), and the most recent joiners run higher (2025 starters: 76%; tenure ≤12 months: 76%; tenure 7–10 years: 62%). The rise across start years is statistically significant.
  - In a single snapshot, start year is just the snapshot date minus tenure, so this is the same pattern as "long-tenure patients churn less."
  - Among patients with 1–60 months of tenure, the effect disappears (p=0.83).
  - [HYP] It reflects survivorship: patients who stayed for years are the ones who didn't leave. It is not evidence that new cohorts are getting worse.
- [CON] **This data doesn't support "churn is getting worse," and doesn't disprove it either.** It simply can't measure a trend. An independent check of this conclusion, from the raw file by a separate analyst agent, reproduced every figure above. It added the tenure-cohort caveat, which is included here.

**What would settle it:** a churn or cancellation date for each patient, or monthly snapshots of active patients. Then churn rate = patients who churned in month *m* ÷ patients active at the start of *m*.

## 2. What is associated with churn

[OBS] These figures come from the multivariable model (all p<0.05, recency fields excluded). Effects are average changes in churn probability with everything else held constant. Simple rates come from the raw grouping.

| Factor | Simple churn rate (n) | Model effect |
|---|---|---|
| Overall satisfaction (1.5–5 scale) | ≤2.0: 78% (305) vs >4.0: 59% (553) | −6.9 pts per scale point. The strongest factor in both models. |
| Billing issue | yes: 77% (157) vs no: 68% (1,843) | +10 pts (wide range, about +2 to +18) |
| Portal use | users: 62% (412) vs non-users: 70% (1,588) | −8 pts |
| Wait-time satisfaction | ≤2.5: 75% (564) vs >3.5: 65% (868) | −3.5 pts per scale point |
| Distance to facility | 0–20 mi: 65% (765) vs 30–50 mi: 73% (797) | +3 pts per 10 miles |
| Out-of-pocket cost | <$500: 66% (845) vs $1,500+: 73% (377) | +4 pts per $500 (odds ×1.17) |
| Missed appointments | 0–1: 65% (908) vs 5: 74% (215) | +1.6 pts per missed appointment |
| Provider rating | — | −2.9 pts per scale point |
| Referrals made | 0: 72% (483) vs 3: 66% (477) | −1.9 pts per referral |
| Tenure, age | — | small: about −1 pt per year of tenure, −1 pt per 10 years of age |

- [OBS] **No meaningful difference** by state (64–72%), specialty (64–70%), insurance type (67–71%) or gender (68% vs 69%). None is significant in the model.
- [OBS] Satisfaction and billing problems add up rather than overlap:
  - satisfaction ≥2.5 and no billing issue: 65% churn (n=1,355);
  - low satisfaction and a billing issue: 81% (n=48).
- [OBS] The predictors are almost uncorrelated with each other (all |r| < 0.06), so these effects don't double-count.
- [CON] Patient experience is the clearest signal, followed by billing friction, digital engagement, and access (distance and cost). All the effects are a few points on a high base, and together they explain little of who churns.
- [HYP] Some of these factors may be consequences rather than causes. For example, patients who are already disengaging may skip the portal and miss appointments. Only an intervention test can separate the two.

## 3. Recommendations

**Do now (measurement):**
1. **Write down the churn definition** (e.g. no visit in 12 months, a transfer of records, or an explicit cancellation). Explain why 60% of recently seen patients are flagged, and say how this extract was sampled.
2. **Add a churn date, and fix the visit fields** (`Visits_Last_Year` vs `Days_Since_Last_Visit`; last visit vs tenure start).
3. **Build a monthly churn-rate series** (churned ÷ active at the start of the month), split by state and specialty. This is the only way to answer "is it getting worse."

**Then (small, measurable pilots, using randomised or matched control groups):**
4. **Patient experience and wait times:** follow up quickly with low-satisfaction patients, and target wait-time improvements at the sites with the lowest scores.
5. **Billing:** set up a fast-resolution route for billing disputes. Only about 8% of patients have a billing issue, but they churn about 10 points more.
6. **Portal enrolment:** push enrolment for non-users, and measure whether it changes retention rather than assuming it does.
7. **Access:** for distant and high-cost patients, test telehealth or reminder options and cost-estimate or payment-plan offers.

**Don't, yet:** fund a large retention programme or target particular states, specialties or insurance types. The data shows no segment-level problem, and the overall signal is too weak and the label too uncertain to justify one.

## Estimated impact (illustrative only)

[HYP] Suppose every patient with overall satisfaction ≤2.5 (n=586, 76% churn) churned at the rate of mid-satisfaction patients (2.5–3.5, n=597, about 69%). That would mean about 40 fewer churned patients in this extract, roughly 2 points of the overall rate. This is a counterfactual *estimate* that assumes the association is causal. It is not a measured loss.
