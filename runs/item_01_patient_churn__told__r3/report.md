# Patient churn: is it getting worse, what drives it, what to do next

## Bottom line

1. **This export cannot show that churn is getting worse, and the time views it does allow do not point that way.** The file is a single snapshot taken on 20 Jan 2026, with one row per patient. There is no history to compute a churn rate per period from. Patients last seen in 2025 are flagged churned *less* often than those last seen in 2024 (65% vs 72%). The number of churned patients per quarter is flat. One cut does rise: newer joiners churn more than long-tenured patients. That reflects tenure, not a change over time (see §2).
2. **The churn flag itself needs explaining before anyone acts on it.** 68% of patients are flagged as churned. That is implausibly high for an outpatient provider. Two-thirds of patients seen in the last 90 days are also flagged as churned. The label has no written definition, and the file has internal inconsistencies (see §1). Every figure below describes this file only. None should be quoted as the organisation's churn rate.
3. **Within this file, the most consistent driver is patient experience, especially overall satisfaction.** Billing problems, portal use, out-of-pocket cost, distance and missed appointments also matter. Even so, the signal is weak: all the data together predicts churn only modestly (a score of AUC ≈ 0.65, where 0.5 is a coin flip). State, specialty, insurance type and gender make no detectable difference.
4. **Recommendation:** first fix how churn is measured: a written definition and monthly snapshots. Then test, on a small scale, actions on the strongest levers: service recovery for dissatisfied patients, resolving billing issues, and portal enrollment. A large retention programme is not justified on this evidence.

Tags: **[OBS]** = computed from the data; **[HYP]** = consistent with the data but not shown; **[CON]** = the best-supported reading.

---

## 1. Data and its limits (read first)

- **Grain and coverage [OBS].** `patients.csv` has 2,000 rows, one per patient, with no duplicate IDs and no missing values. Patients come from 10 states, 7 specialties and 4 insurance types.
- **It is one snapshot [OBS].** Last_Interaction_Date + Days_Since_Last_Visit equals **2026-01-20 for every row**. So the file is a single as-of extract, and those two columns carry the same information. Last interactions run from Jan 2024 to 19 Jan 2026. 2026Q1 is partial: 19 days, 52 patients.
- **The churn label is undefined and the base rate is implausible [OBS].**
  - 68.4% of patients are flagged as churned (1,367 of 2,000).
  - Among patients seen in the last 90 days, 66% are flagged churned. For the last 365 days it is 64%.
  - So the label is clearly not "stopped visiting". It may mean something else, such as a transfer, a survey-based intent flag, or a model score. It is also possible the export over-samples churned patients rather than covering everyone.
- **Fields contradict each other [OBS].**
  - 940 patients (47%) have Visits_Last_Year > 0 but a last visit more than 365 days ago.
  - 191 patients have a last visit earlier than the date their tenure started.
  - Either the fields use different reference dates, or the extract is unreliable. This should be resolved with the data owner.
- **Assumptions I made:**
  - "Churned = 1" is taken as given.
  - Tenure is assumed to be counted back from the snapshot date.
  - Effects are reported as within-sample associations, not causes.

## 2. Is churn getting worse?

**[CON] This data cannot establish a trend, and nothing in it shows churn rising.** A churn *rate* over time needs, for each period, how many patients were active at the start and how many churned during it. A single snapshot has neither.

The views that can be built [OBS]:

| Last interaction | Churned (count) | Patients | Share flagged churned |
|---|---|---|---|
| 2024 Q1 | 166 | 218 | 76% |
| 2024 Q2 | 154 | 231 | 67% |
| 2024 Q3 | 193 | 256 | 75% |
| 2024 Q4 | 168 | 241 | 70% |
| 2025 Q1 | 155 | 220 | 70% |
| 2025 Q2 | 185 | 276 | 67% |
| 2025 Q3 | 147 | 254 | 58% |
| 2025 Q4 | 165 | 252 | 65% |
| 2026 Q1 (partial, 19 days) | 34 | 52 | 65% |

- **By year:** 72% for 2024 (n = 946) vs 65% for 2025 (n = 1,002). The difference is statistically significant (χ² p = 0.001). It persists after adjusting for patient attributes (−6.6 pp, p = 0.001), so it is not explained by a different patient mix.
- **This is not a trend.** It groups patients by *when they were last seen*, which is a recency measure. Patients seen longer ago are naturally more likely to be counted as lost.
- **Churned counts per quarter are flat**, at roughly 150–190, with no upward drift.
- **Why newer joiners churn more.** Grouping by join year (snapshot date minus tenure):
  - 2016–2018 joiners: 58–68% churned.
  - 2022–2025 joiners: 68–77% churned (72.6% vs 65.5% for earlier joiners, p = 0.001).
  - This should not be read as "churn getting worse". Join year is just tenure in reverse, and newer patients always have the least loyalty built up.
  - [HYP] It could also mean recent patients are less well matched or onboarded. Only cohort retention curves, tracked over time, can tell these two apart.

An independent check by a separate analyst agent, which saw only the claim and the raw file, confirmed these numbers. Its verdict was "holds with caveat"; the caveat is the newer-joiner cut above.

## 3. What is associated with churn (within this file)

Method: a logistic regression of the churn flag on all patient attributes. Effects are shown as the average change in the probability of being flagged churned. Days_Since_Last_Visit and Last_Interaction_Date are **excluded** because they are tied to the snapshot date. Including them changes nothing below.

| Factor [OBS] | Effect on churn probability | 95% CI |
|---|---|---|
| Billing issue recorded (7.9% of patients) | +10 pp | +2 to +18 |
| Portal user (21% of patients) | −8 pp | −13 to −4 |
| Overall satisfaction, per 1 point (1–5 scale) | −7 pp | −9 to −5 |
| Wait-time satisfaction, per 1 point | −3.5 pp | −5.5 to −1.5 |
| Provider rating, per 1 point | −3 pp | −6 to −0.2 |
| Out-of-pocket cost, per $1,000 | +~6 pp | — |
| Distance to facility, per 10 miles | +2.6 pp | +1.2 to +4.0 |
| Missed appointments, each | +1.6 pp | +0.3 to +2.8 |
| Tenure, per year | −1.2 pp | −1.8 to −0.5 |
| Age, per 10 years | −1.5 pp | −2.8 to −0.2 |
| Referrals made, each | −1.9 pp | −3.6 to −0.1 |
| State, specialty, insurance, gender, staff satisfaction | no significant effect | — |

What the raw splits show [OBS]:
- **Satisfaction:** patients scoring ≤2 churn at 78%, vs 52% for those scoring 4.5–5.
- **Satisfaction and portal together:** among highly satisfied patients (>4), portal users churn at 44% (n = 116) vs 63% for non-users (n = 437). Among dissatisfied patients, portal use helps much less (70% vs 78%).
- **Distance:** patients more than 30 miles away churn at about 72%, vs about 65% for those under 20 miles.

Robustness [OBS]: a gradient-boosting model also ranks overall satisfaction clearly first, followed by tenure, age, provider rating, distance and portal use. Wait-time satisfaction and billing issues rank lower there, so treat those two as less certain.

**How much to trust these effects [CON].** These are associations on top of a 68% base rate, with weak overall predictive power. Some may be reverse causation [HYP]: patients who are already leaving may rate lower and stop using the portal. None should be read as a guaranteed retention gain if the factor changes.

## 4. Recommendations

**Do first: fix the measurement.**
1. **Write down what "Churned" means.** Spell out the rule, who sets the flag, and whether the export is the full patient base or a sample. Until then, do not report 68% as a churn rate.
2. **Resolve the field conflicts** with the data owner: Visits_Last_Year vs Days_Since_Last_Visit, and last visit dated before tenure start.
3. **Start monthly as-of snapshots**, or record a churn date for each patient. Then report churn per month as patients lost during the month ÷ patients active at its start, along with retention curves by join cohort. This is the only way to answer "is it getting worse".

**Do next: small, measurable tests on the strongest levers.** Run each with a control group so the effect can be measured.
4. **Service recovery for dissatisfied patients:** follow up when someone gives a low satisfaction score, especially on wait times. This is the most consistent signal.
5. **Resolve billing issues quickly**, and give estimates up front for patients with high out-of-pocket costs.
6. **Portal enrollment for new patients.** Patients in their first year churn the most (76%, vs 62% for those with more than 7 years), and portal users churn less.
7. **Consider telehealth or reminders for distant patients**, and outreach after missed appointments. These are lower priority because the effects are smaller.

**Don't do yet:** target specific states, specialties or payers (no difference was found), or fund a large retention programme before items 1–3 are done.
