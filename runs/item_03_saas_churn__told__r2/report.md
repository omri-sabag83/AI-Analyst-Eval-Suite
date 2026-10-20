# Customer churn drivers: assessment of the 2023–2024 data

## Bottom line

1. **This data does not show that retention got worse.** Churn events rose from 6 a quarter to 251 a quarter. Over the same period, the number of subscriptions grew about 30-fold. Adjusted for the size of the base, churn among established subscriptions was flat at about 1% a month. Every other upward trend in the data can be fully explained by how the dates are recorded, without any change in customer behaviour.
2. **No churn driver can be identified.** None of the following separates customers who churn from those who stay: plan tier, billing frequency, auto-renew, trial status, seat count, upgrades or downgrades, product errors, support experience, or the recorded churn reasons. Each churn reason accounts for 15–19% of events, and the reason codes don't agree with customers' own written feedback.
3. **The data is not fit to support a funding decision.** There are three conflicting definitions of churn. Most "churned" accounts are still paying. More than half of the usage and support records are dated before the customer existed.

**Recommendation:** don't fund a broad churn programme on the basis of this data. Spend first on a small, quick fix to churn measurement (Section 4). Then re-run this analysis on clean data, ideally covering at least one more quarter.

Each claim below is tagged: **[OBS]** = seen directly in the data; **[CON]** = the conclusion the evidence best supports; **[HYP]** = a possible explanation not yet proven.

---

## 1. Data, scope and quality problems (read before the findings)

**Scope.** The analysis covers five extracts dated 2023-01-01 to 2024-12-31, with 2024-12-31 taken as the snapshot date:
- 500 accounts
- 5,000 subscriptions, of which 486 have ended
- 600 churn events across 352 accounts
- 2,000 support tickets
- 25,000 feature-usage rows

All 2024-Q4 figures sit at the edge of the extract.

**Quality problems that limit what can be concluded:**

| # | Issue | Evidence | Consequence |
|---|---|---|---|
| Q1 | **Three definitions of "churn" that disagree** [OBS] | 110 accounts have `churn_flag`=True. 352 accounts have a churn event. 312 accounts have an ended subscription. Of the 110 flagged accounts, 35 have no churn event. Of the 390 unflagged accounts, 277 have one. | There is no single, defensible churn number. Every figure depends on which definition is used. |
| Q2 | **"Churned" accounts are still customers** [OBS] | Not one of the 500 accounts has all its subscriptions ended. Of the 75 flagged accounts that have events, 61 started a new subscription after their last churn event. | The data records subscription-level ends, not customer (logo) loss. A real lost-customer rate can't be measured. |
| Q3 | **Usage and ticket records are dated before the customer existed** [OBS] | 77% of usage rows are dated before their subscription started. 53% of usage rows and 54% of tickets are dated before the account signed up. | Any link between product usage or support and churn rests on records that can't be correct. These sources were analysed but carry little weight. |
| Q4 | **Churn reason codes contradict the free-text feedback** [OBS] | Reason code and feedback text are statistically independent (chi-square p = 0.95). For example, events coded "support" carry "too expensive" feedback as often as any other code. 16% of events are coded "unknown" and 25% have no feedback. | Reason codes can't be trusted to point at a cause. |
| Q5 | **Event dates follow the extract window, not the customer lifecycle** [OBS] | See Section 2. | Trend lines built from these dates are mostly artefacts. |
| Q6 | Minor issues [OBS] | 21 duplicate `usage_id` values; 825 tickets (41%) have no satisfaction score. | Not material. |

---

## 2. Has retention deteriorated?

**[OBS] Raw counts rose steeply, but so did the base.**

| Quarter | Churn events | Subscriptions started | Subscription-months at risk | Subscriptions ended | Monthly subscription churn rate |
|---|---|---|---|---|---|
| 2023 H2 | 56 | 529 | 1,885 | 15 | 0.80% |
| 2024 Q1 | 54 | 472 | 2,335 | 25 | 1.07% |
| 2024 Q2 | 92 | 686 | 3,874 | 34 | 0.88% |
| 2024 Q3 | 130 | 1,107 | 6,161 | 67 | 1.09% |
| 2024 Q4 | 251 | 2,069 | 9,738 | 192 | 1.97% |

(Rate = subscriptions ended in the month ÷ subscriptions active at the start of the month, pooled over the period.)

**[OBS] Established subscriptions (90 days or older) churned at a flat rate throughout.** By period, the rate was:
- 2023 H2: 0.76% (95% CI 0.28–1.64%)
- 2024 Q1: 0.87%
- 2024 Q2: 0.87%
- 2024 Q3: 0.88%
- 2024 Q4: 1.09% (95% CI 0.84–1.39%)

All the confidence intervals overlap. The 2024-Q4 jump in the table above comes from subscriptions under 90 days old, whose rate went from 0.8–1.4% in earlier periods to 3.4%.

**[OBS] The dates are distributed in a way real customer behaviour wouldn't produce.**
- **Lifetime churn doesn't grow with time observed.** Subscriptions started in 2024 Q4, observed for at most 3 months, have already ended at 10.1%. That is the same as 2024-Q1 subscriptions observed for 12 months (9.3%). Accounts signed up in 2024 Q4 average 1.11 churn events, the same as 2023-Q1 accounts after 24 months (1.16). In real data, churn builds up the longer a cohort is observed.
- **Each event falls at a uniform point in its window.** Measured as a fraction of the time between start/signup and 2024-12-31, the position of each event is uniform (mean 0.49 for subscription ends; KS test against uniform p = 0.25). This holds in every cohort.
- **The oldest cohort shows no calendar trend.** Accounts that signed up in 2023 Q1 had 0.27, 0.38, 0.27 and 0.24 churn events per account in successive half-years.

**[OBS] Uniform dating predicts the apparent decline in cohort retention.** The share of each signup cohort with a churn event within 90 days appears to climb from 18% (2023 Q1) to 60% (2024 Q3). If each account's churn events are placed at random between signup and the snapshot date, the predicted share goes from 15% to 55%. That is the same rise, with no change in behaviour.

**[CON] The data does not show any deterioration in retention.** The upward trends come from:
- a growing base, which inflates the raw counts;
- event dates being spread over each customer's remaining window up to the extract date. This compresses the churn of recent cohorts into a short span and inflates their short-term rates, including the Q4-2024 rise among new subscriptions.

**Independent check.** A separate reviewer who did not see this reasoning tested the conclusion from the raw files. The verdict was **holds, with caveats**. The reviewer re-dated every churned subscription at random within its own window, 300 times. The observed Q4-2024 figures fell inside the simulated range:
- overall quarterly rate: 4.19% observed vs 4.31% simulated (range 3.86–4.81%);
- subscriptions in their first 90 days: 5.68% vs 6.16% (range 5.46–6.83%).

**The caveat matters: "not shown to be worse" is not the same as "shown to be fine".** If the dates carry no real timing information, this data can't show an improvement either. Leadership's concern may still be right. This data simply can't confirm it.

**[HYP] Early-life churn rose in Q4 2024.** This can't be ruled out, but the random-dating simulation reproduces it fully. To settle it, re-measure once Q1-2025 data is in, using dates that record real cancellations.

---

## 3. What is driving churn?

The methods used to look for drivers:
- **Account level:** churn-flag rates and churn events per account-year by segment, plus logistic and Poisson models that control for each account's exposure time.
- **Subscription level:** ends per 100 subscription-months, plus a Poisson model with exposure.

**[OBS] Commercial and product attributes make no difference.**

| Attribute | Subscription churn (per 100 subscription-months) |
|---|---|
| Plan tier: Basic / Pro / Enterprise | 1.73 / 1.83 / 1.92 |
| Billing: annual / monthly | 1.89 / 1.76 |
| Auto-renew: on / off | 1.83 / 1.81 |
| Trial: yes / no | 1.84 / 1.82 |
| Upgrade flag: yes / no | 1.50 / 1.87 |
| Downgrade flag: yes / no | 2.16 / 1.81 |

Taken together, these attributes plus seat count, error rate and beta-feature use don't predict churn (joint model p = 0.84). No single coefficient is significant.

**[OBS] Account segments make no difference either.** The share of accounts flagged as churned is 22% on every plan tier (p = 1.0). The differences by country (p = 0.66) and by acquisition channel (p = 0.08) aren't significant. Seats, satisfaction score, resolution time, first-response time and escalations don't differ between churned and retained accounts (all p > 0.1).

**[OBS] The one weak signal is the DevTools industry.** 31% of DevTools accounts are flagged as churned, against 19% for all others (35 of 113 vs 75 of 387; Fisher p = 0.014). Controlling for signup date doesn't remove it (p = 0.014). But it is one of five industries tested; after correcting for that (Bonferroni), p = 0.07. It also doesn't show up in churn events (DevTools 1.31 events per account-year vs 1.20–1.48 elsewhere).
- **[HYP]** DevTools customers may churn more. Treat this as a lead to check on clean data, not a finding to fund against.

**[OBS] Recorded churn reasons are evenly spread and stable.**
- Features: 114 events (19%), $1,906 refunded
- Support: 104 (17%), $1,220
- Budget: 104 (17%), $1,248
- Unknown: 95 (16%), $1,742
- Competitor: 92 (15%), $1,204
- Pricing: 91 (15%), $1,333

The reason mix didn't change between 2023 and 2024 (p = 0.48) and doesn't vary by plan (p = 0.75). Refunds total only $8,650 across all 600 events.
- **[CON]** There is no dominant reason to target, and Q4 shows the codes don't reliably reflect what customers said anyway.

**Excluded as misleading.** Support tickets per account-year look strongly linked to churn events per account-year (Poisson z = 13). That is an artefact: both are divided by the same exposure time. Raw ticket counts have no link to churn (ρ = −0.00). Usage and ticket measures are also undermined by Q3.

**[CON] No credible churn driver can be identified from this data.** That is either because none exists in these dimensions or because the data quality hides it (Q1–Q5). The data can't tell which.

---

## 4. Proposed actions

The evidence doesn't justify a large retention programme. These actions are sized to that.

1. **Fix churn measurement first** (data / RevOps owner; low cost; do now).
   - Agree one written definition of churn: logo churn means an account with no active paid subscription, plus a separate revenue (MRR) churn measure.
   - Make `accounts.churn_flag` and `churn_events` follow from it.
   - Record the real cancellation date rather than a derived one.
2. **Repair the data feeds** (engineering).
   - Usage and ticket records need valid subscription and account keys and dates (Q3).
   - Churn reasons need a single, required, controlled field reconciled with the feedback text (Q4).
3. **Re-run this analysis on the corrected data**, including Q1 2025. In particular, check:
   - (a) early-life churn of new subscriptions — the Q4-2024 [HYP];
   - (b) the DevTools segment [HYP];
   - (c) usage and support signals, once their dates are valid.
4. **Set up a standing control** (owner: whoever owns retention reporting).
   - Track monthly churn for subscriptions 90 days or older, and separately for subscriptions under 90 days.
   - Show the count of subscriptions at risk alongside each rate.
   - Investigate any month above about 1.5% for established subscriptions. That is three standard errors above the 2024 baseline of 0.9%, at about 2,000 subscriptions at risk (0.9% + 3 × 0.21 points). Recompute the limit as the base changes.
   - Investigate an early-life rate that stays above the 2024 Q1–Q3 range (0.9–1.4%) for two or more consecutive months.
5. **Hold off funding** price changes, support restructuring or feature programmes "against churn" until step 3 is done. With current data, none of these has better support than the others.

## 5. What would change these conclusions

- A source of real cancellation dates showing rising, exposure-adjusted churn among established customers would overturn finding 1.
- A trustworthy definition of churn could show segment differences that the conflicting flags currently hide.
- Usage and ticket records with valid dates could reveal engagement or support drivers that can't be tested today.

*Methods note: all rates are within this sample of 500 accounts and shouldn't be read as company-wide figures. Assumptions: 2024-12-31 is the snapshot date; a subscription with a blank `end_date` is active; "churn" in Section 2 means a subscription ending, because no account was ever fully lost (Q2).*
