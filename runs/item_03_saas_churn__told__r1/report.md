# Customer churn drivers: findings and recommendations

## Bottom line

1. **Retention did not decline steadily over two years.** Raw churn counts rose sharply, but only because the customer base grew so fast: active subscriptions went from 31 to 4,838. Measured against the base, subscription churn stayed flat at about **0.8–1.2% per subscription-month** from late 2023 through mid-2024.
2. **There is one recent, sharp problem.** From **Aug–Sep 2024**, and much more in **Q4 2024**, churn rose to **3.0% per month**: 1.9% in Oct, 2.1% in Nov and 4.5% in Dec. Almost all of the rise is in **subscriptions in their first ~90 days**. Subscriptions older than three months stayed at about 0.9–1.1% per month.
3. **The data does not identify a driver.** The early churn is spread evenly across plan, billing, trial, auto-renew, industry, referral source, country and seat count. The churn reason codes are spread evenly too and don't match the customers' own feedback text. The usage and support data don't line up with the subscriptions, so they can't be used to explain anything.
4. **The data itself is the first thing to fix.** The three "churn" records contradict each other. Every account in the extract, including the 110 flagged as churned, still has active subscriptions. And part of the December spike may be an artefact of where the extract was cut off.

**Recommendation:** don't fund a broad retention programme on this evidence. Fund a short, focused piece of work: (a) confirm the Q4 new-subscription churn is real, (b) if it is, find out what changed in onboarding, billing or checkout around Aug–Sep 2024, and (c) fix the churn definitions and data plumbing so the question can be answered properly.

Tags used below: **[OBS]** is computed from the data; **[HYP]** is a plausible explanation that hasn't been shown; **[CON]** is the reading best supported by the evidence.

---

## 1. Data, scope and quality issues (read first)

| File | Grain | Rows | Window |
|---|---|---|---|
| accounts.csv | 1 row per account | 500 | signups 2023-01-02 to 2024-12-31 |
| subscriptions.csv | 1 row per subscription | 5,000 (2–19 per account) | starts 2023-01-09 to 2024-12-31 |
| churn_events.csv | 1 row per churn event | 600 (352 accounts) | 2023-01-25 to 2024-12-31 |
| support_tickets.csv | 1 row per ticket | 2,000 | 2023-01-02 to 2024-12-31 |
| feature_usage.csv | 1 row per usage record | 25,000 (21 duplicate IDs) | 2023-01-01 to 2024-12-31 |

The extract runs to 2024-12-31. A subscription with no end date is treated as active on that date. 2023 is thin: before 2023Q4 there were fewer than 3 subscription churns per quarter, so rates for that period can't be interpreted.

**Problems that limit what can be concluded [OBS]:**

- **Three churn definitions that disagree.**
  - `accounts.churn_flag` marks 110 of 500 accounts (22%) as churned and has no date.
  - Yet 277 of the 390 "retained" accounts have at least one churn event, and 35 of the 110 "churned" accounts have none.
  - In `subscriptions`, all 500 accounts, including the 110 flagged ones, still hold active subscriptions (about 9 each on average) at 2024-12-31.
  - Only 47 of the 600 churn events fall within 7 days of a churned subscription's end date.
  - Nobody has written down what "churn" means at either the account or the subscription level.
- **No account has fully left.** That is implausible for a real B2B customer base. The most likely explanation is that the extract contains only current customers, which would leave out lost logos. **True customer-level (logo) churn therefore cannot be measured from this data.** All figures here describe this sample only.
- **Usage data doesn't fit the subscriptions.** 77% of usage records are dated *before* the subscription they belong to started. Usage volume is flat at about 3,100 records per quarter while the subscription base grew roughly 150-fold.
- **Support data doesn't scale with the base either.** Tickets stay at about 250 per quarter throughout, and 41% have no satisfaction score.
- **Reason codes look unreliable.** The six codes each account for 15–19% of churn events. Feedback text is independent of the code: "budget" churns are as likely to say "switched to competitor" as "too expensive".
- **The extract edge looks suspicious.** 61 of December's 193 subscription churns fall on Dec 29–31, 24 of them on Dec 31 alone. December also had 953 new subscriptions, almost double November's 612.

Because of these problems, I base the trend on **subscription records**: they are the only dated table where churn and exposure are consistent (churn_flag and end_date agree on all 5,000 rows). I use account and event data only as supporting evidence.

## 2. Has retention deteriorated?

### The raw counts are misleading [OBS]
Churn events went from 6 (2023Q1) to 251 (2024Q4), and churned subscriptions from 0 to 324. Over the same period active subscriptions grew from 31 to 4,838, so the counts mostly reflect growth.

### Churn measured against the base [OBS]
Rate = churns ÷ subscription-days active in the quarter × 30.

| Quarter | Active subs | Sub churns | Churn %/sub-month | Churned MRR | MRR churn %/month |
|---|---|---|---|---|---|
| 2023Q4 | 662 | 14 | 0.95 | $49k | 1.73 |
| 2024Q1 | 1,120 | 27 | 1.04 | $50k | 0.96 |
| 2024Q2 | 1,779 | 37 | 0.87 | $59k | 0.64 |
| 2024Q3 | 2,849 | 80 | 1.17 | $147k | 0.98 |
| 2024Q4 | 4,838 | 324 | **2.99** | **$872k** | **3.61** |

Monthly in 2024: Jan–Jul 0.8–1.5%, Aug 1.22%, Sep 1.36%, Oct 1.88%, Nov 2.10%, Dec 4.50%.

**[CON]** There was no steady two-year decline. Retention was stable until about Aug 2024 and then got clearly worse in Q4 2024. Even without the suspicious Dec 29–31 cluster, Q4 is about 2.5% per month, so the rise doesn't depend on those days.

**Why leadership may see a steady decline:** if you count churn events per *account*, the rate climbs from about 5% to 17% per month over 2023–24. But each account keeps adding subscriptions, so per active *subscription* the event rate is flat at about 2.1–2.5 per 100 subscription-months from 2023Q4 to 2024Q4. The "deterioration" on that measure is a denominator effect, and the event table's link to real departures is doubtful anyway (see §1).

### Where the Q4 rise sits: rate vs mix [OBS]
Exposure and churn split by subscription age at the start of each month:

| Quarter | New this month: churns / %/mo | 1–3 months old: churns / %/mo | 3+ months old: churns / %/mo |
|---|---|---|---|
| 2024Q1 | 2 / 0.9 | 14 / 1.3 | 11 / 0.9 |
| 2024Q2 | 2 / 0.6 | 15 / 0.9 | 20 / 0.9 |
| 2024Q3 | 11 / 2.1 | 35 / 1.5 | 34 / 0.9 |
| 2024Q4 | **128 / 13.6** | **130 / 3.5** | 66 / 1.1 |

- **Mix-only:** applying the Q1–Q3 2024 rate for each age band to Q4's age mix gives 1.05% per month, the same as the baseline. A younger book of business explains none of the rise.
- **Rate-only:** applying Q4's rates to the baseline mix gives 2.96%. **The rise is entirely a change in rates.**
- **Counterfactual (estimate):** at Q1–Q3 rates, Q4 would have had about **113** subscription churns instead of 324, so about **210 were excess**. Of those, about 115 were in the first month, about 83 at 1–3 months and about 13 at 3+ months. This assumes Q1–Q3 2024 is the right baseline. On MRR, the same logic puts roughly **$650k of Q4's $872k churned MRR** above the baseline. That is an estimate, not a measured loss.
- **Cohort view:** the share of new subscriptions that churn within 30 days was 0–1% for most start months in H1 2024. It rose to 2.7% in Aug, 3.6% in Sep and Oct, and 7.7% in Nov. Within 90 days, it ran 1.6–4.8% from Jul-2023 to Jul-2024 cohorts, then rose to 6.8–10.3% for Aug–Nov 2024 cohorts.
- **December:** 100 of December's 193 churns were subscriptions that started *and* ended in December, with a median life of 7 days.

**[CON]** The problem is new subscriptions failing early, starting around Aug–Sep 2024 and sharpening in Nov–Dec. The established base did not deteriorate meaningfully: 0.87% → 1.07% per month for subscriptions 3+ months old, about 66 churns against about 53 expected.

## 3. What is driving churn?

To pin down the problem, I compared where it appears with where it doesn't, across every dimension in the data.

**Subscription level [OBS].** Among Q4-2024 starts, the rate of churning within 30 days was:

| Dimension | Range |
|---|---|
| Plan | Basic 7.5%, Pro 8.9%, Enterprise 8.0% |
| Billing | monthly 7.1%, annual 9.1% |
| Trial | yes 7.4%, no 8.2% |
| Auto-renew | off 9.4%, on 7.8% |
| Industry | 6.4–10.1% |
| Referral source | 6.1–10.1% |
| Country | 5.8–10.1% |

Seat count and MRR medians are the same for early churners and everyone else. The early churns are spread across many accounts: 176 churns in 140 accounts, with the top 10 accounts holding only 14%. A multivariable Poisson model of subscription churn (plan, billing, trial, auto-renew, upgrade/downgrade, seats, industry, referral, start quarter) finds **no significant factor except start quarter**. Q4-2024 starts churn about 9× faster per day than 2023Q1 starts (p<0.001). Every other factor has p>0.17.

**Account level [OBS].** With `churn_flag` as the outcome, nothing is significant:

- plan: 22.0% / 22.1% / 21.9%
- trial vs non-trial: 25.8% vs 21.1% (p=0.39)
- seats: p=0.69
- support ticket count, resolution time, first-response time, satisfaction, escalation rate: all p≥0.10
- usage volume and error rate: p≥0.12

Industry (DevTools 31% vs 16–22%, p=0.07) and referral source (event 30%, partner 15%, p=0.08) are borderline. After testing about 15 factors, those p-values are what chance alone would produce, so I treat them as noise. Churned accounts also have *longer* tenure (median 380 vs 301 days), which is consistent with simply having had more time to be flagged.

**Stated reasons [OBS].** Over all 600 events: features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%. The mix is stable quarter to quarter, including Q4 2024, and the feedback text doesn't match the codes. There's no evidence of a dominant reason such as pricing or competitors.

**Support and product quality over time [OBS].** Per-ticket resolution time (about 35–37 h), first response (about 86–91 min), satisfaction (3.9–4.1) and the usage error rate (0.53–0.60 per record) are flat across all eight quarters. Nothing in the data suggests service or product quality got worse.

**[CON]** None of the measured customer, product or service attributes drives churn in this data. The Q4-2024 rise hits all segments equally. That pattern points to a change that affected *every new subscription at once* rather than any particular kind of customer.

**[HYP] Candidate causes, and what would settle each:**

| Hypothesis | Evidence that would settle it |
|---|---|
| H1: **Data/extract artefact.** Cancellations, abandoned checkouts or test records were stamped at the extract date, or the Q4 surge in subscription creation (2,069 starts, 953 in Dec) includes non-genuine records. | An extract running past 2024-12-31; the source of `end_date` for the Dec 29–31 cluster; whether Dec same-month start/end subscriptions were ever billed. |
| H2: **A change to sign-up, onboarding, pricing or billing around Aug–Sep 2024** made new subscriptions cancel quickly, e.g. a new self-serve checkout, a promotion, or a provisioning or invoicing problem. | Release and pricing-change log for Jul–Oct 2024; payment-failure and refund logs; onboarding-step completion for Q4 subscriptions. |
| H3: **Lower-quality acquisition in a volume push.** New subscriptions per month doubled from Sep (440) to Dec (953). | Campaign/source per *subscription* (only account-level referral exists, and it shows no effect); sales-led vs self-serve flag. |
| H4: **Plan changes recorded as churn.** A subscription closed and replaced within the same account would look like churn, which would explain why no account ever fully leaves. | Whether each churned subscription has a replacement starting within a few days in the same account; the system's definition of `churn_flag`. |

## 4. Recommendations

1. **Before funding a response, check that the Q4 spike is real (1–2 weeks, data and billing owners).** Pull January–February 2025 data and trace the Dec 29–31 churns and the December same-month subscriptions back to billing. If they turn out to be artefacts or plan changes (H1/H4), the underlying churn rate is about 1% per month and stable, and no retention programme is warranted on this evidence.
2. **If the spike is real, focus on the first 90 days, not the whole base.** Review what changed in sign-up, provisioning, pricing and billing around Aug–Sep 2024 (H2/H3). Put an early-life check in place, such as a health check before day 30 for every new subscription. Broad discounts, support overhauls or feature bets aren't supported by the data: the established base isn't deteriorating, and no segment, price or support signal stands out.
3. **Fix the measurement so the question can be answered.**
   - Write one definition of churn: logo churn (account has no active paid subscription) and gross/net MRR churn.
   - Make `accounts.churn_flag`, `churn_events` and subscription end dates agree with that definition.
   - Include lost customers in future extracts.
   - Repair the link between usage and subscriptions; 77% of usage records currently predate their subscription.
   - Replace the free-form reason codes with a required, validated exit reason.
4. **Monitor it.** Track monthly subscription churn per subscription-month, split by age band (new / 1–3 months / 3+ months), with volumes alongside. Based on 2024 H1, a reasonable alert is: 3+ month churn above about 1.5% per month, or 30-day churn for a start-month cohort above about 3%.

## 5. Checks performed

- **Rigor checklist.** I ran the analysis through a rigor checklist before writing. Results:
  - Rate vs mix: decomposed above.
  - Volumes: shown next to every rate.
  - Recent window: the right-censored, suspicious-looking period is flagged.
  - Undefined churn label: flagged, and all figures kept within-sample.
  - Usage per day: excluded from the driver analysis, because it is mechanically tied to how long a subscription lasted.
- **Method sensitivity.** Assigning subscription age by exact daily age instead of age at the start of the month gives the same picture (3+ month band 0.84–1.10% per month across all quarters). The cohort view (churn within 30 or 90 days by start month) agrees as well.
- **Independent check.** A separate reviewer, working only from the raw subscriptions file, verified the main conclusion and returned **"holds with caveat"**. It reproduced the quarterly rates (0.95 / 1.04 / 0.87 / 1.17 / 2.99%), the under-90-day vs 90+ split (Q4: 5.5% vs 1.07% per month) and the stable 90+ rate. Its caveats are now in the text: the rise begins in Aug–Sep 2024 rather than suddenly in Q4, Q4 is dominated by December and the Dec 29–31 cluster, and the 2023 rates rest on very small counts.
