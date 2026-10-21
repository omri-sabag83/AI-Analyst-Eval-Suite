# Customer churn: has retention deteriorated, and what is driving it?

## Bottom line

1. **The data does not show that retention has got worse.** Churn *counts* rose steeply through 2024 (churn events went from 6 in Q1 2023 to 251 in Q4 2024). But the customer base grew just as fast: open subscriptions went from 31 to about 2,800. Measured per subscription, the chance that a subscription churns is flat at about 10% for every start cohort.
2. **The apparent late-2024 "spike" is almost certainly a recording artifact, not a change in customer behaviour.** In these extracts, how likely a subscription or account is to churn does not depend on how long it has been a customer. Churn dates are spread evenly between the start date and the extract date (31 Dec 2024). Real churn does not behave this way. One result of the pattern is that new subscriptions look like they churn fast, and that pushes up recent churn rates.
3. **No variable in the data meaningfully predicts churn.** Plan tier, billing frequency, auto-renew, trial status, seats, MRR, industry, country, referral source, upgrades/downgrades, product usage and support experience all show churn rates within noise of each other. The recorded churn reason codes do not agree with the customers' own feedback text.
4. **Recommendation: do not fund a broad churn programme based on this data yet.** First fix how churn is recorded (a 4–6 week data effort). Then rebuild a cohort retention metric and repeat the driver analysis. Details are below.

## Data and assumptions

- Five extracts, all dated 2023-01-01 to 2024-12-31: 500 accounts, 5,000 subscriptions, 25,000 usage rows, 2,000 tickets and 600 churn events. There are no orphan keys and no duplicate IDs, apart from 21 repeated `usage_id`s.
- **Assumption:** the extract date is 31 Dec 2024. Subscriptions with no `end_date` are treated as active on that date. Subscription-level churn (`churn_flag` plus `end_date`, which agree exactly: 486 churned subscriptions, all with an end date) is used as the main measure. It is the only churn record that is internally consistent (see the data-quality section).
- The company's base grew fast. Accounts signing up per quarter rose from 55 to 80. Subscriptions starting per quarter rose from 31 to 2,069. Any count-based churn metric will rise by construction.

## Finding 1: retention has not measurably deteriorated

**Share of each subscription start cohort that has churned by the extract date:**

| Start quarter | Subscriptions | % churned to date |
|---|---|---|
| 2023 Q1 | 31 | 19.4% (small n) |
| 2023 Q2 | 106 | 10.4% |
| 2023 Q3 | 203 | 15.8% |
| 2023 Q4 | 326 | 11.0% |
| 2024 Q1 | 472 | 9.3% |
| 2024 Q2 | 686 | 8.6% |
| 2024 Q3 | 1,107 | 8.1% |
| 2024 Q4 | 2,069 | 10.1% |

The rate is flat at about 10%, with no upward trend in recent cohorts.

**The "it's getting worse" view comes from two metrics that do rise:**

| Quarter | Open subs at start | Subs churned in quarter | Quarterly sub churn rate | Churn events (all accounts) |
|---|---|---|---|---|
| 2023 Q4 | 336 | 12 | 3.6% | 37 |
| 2024 Q1 | 648 | 19 | 2.9% | 54 |
| 2024 Q2 | 1,093 | 31 | 2.8% | 92 |
| 2024 Q3 | 1,742 | 51 | 2.9% | 130 |
| 2024 Q4 | 2,769 | 116 | 4.2% | 251 |

- Churn counts rose about 7× in a year because the base rose about 8×. The quarterly churn *rate* was flat at roughly 3% for all of 2024 until Q4.
- The Q4 2024 rise to 4.2%, and the high 30-day churn of recent cohorts (about 0.6–1% for cohorts up to mid-2024, then 3.6% for Sep–Oct starts and 7.7% for Nov starts), come from the artifact described next. I would not read them as real deterioration.

## Finding 2: the churn timing in these extracts is mechanical, not behavioural

Three tests point to the same conclusion:

- **Churn does not depend on exposure.** A subscription that started two weeks before the extract has the same chance of being flagged as churned as one that started two years earlier:

  | Days from start to extract | % churned |
  |---|---|
  | ≤30 | 10.8% |
  | 31–90 | 9.4% |
  | 91–180 | 8.1% |
  | 181–365 | 8.9% |
  | 366–730 | 12.8% |

  In a logistic regression of churn on log exposure, the coefficient is −0.005 (p = 0.89). With real churn, cumulative churn rises with time as a customer.
- **Churn dates are spread evenly across each subscription's window.** For churned subscriptions, I measured where the end date falls between the start date and 31 Dec 2024 (0 = at start, 1 = at the extract date). The value is uniform: mean 0.50, and about 37–61 subscriptions fall in each tenth of the window. Account churn events show the same pattern (51–67 per tenth). Accounts average about 1.2 churn events whether they joined 1 month or 2 years before the extract.
- **What follows from this:** recently started subscriptions must have their churn dates squeezed into a short window. That makes new customers *look* like they churn fast, and it inflates the most recent quarter's rate. The same mechanism produces the rising count of churn events.

This is consistent with end dates and churn events being backfilled or assigned when the extract was built, rather than recorded when the churn happened. **I'm treating this as a hypothesis to confirm with the data owners.** If it is wrong, and these dates are real, then the alternative reading is that recent customers churn much faster. That would be a real and serious finding. The way to settle it is to check the billing system's actual cancellation timestamps for a sample of Q4 2024 churned subscriptions.

## Finding 3: no meaningful churn driver can be identified

Subscription-level churn rate by attribute (n = 5,000; overall rate 9.7%):

| Attribute | Range of churn rate across groups | p-value |
|---|---|---|
| Plan tier (Basic / Pro / Enterprise) | 9.5% – 10.0% | 0.89 |
| Billing (monthly / annual) | 9.4% – 10.0% | 0.49 |
| Auto-renew on / off | 9.6% – 9.7% | 0.98 |
| Trial vs paid | 9.7% – 10.0% | 0.81 |
| Upgrade flag / downgrade flag | 8.7% – 9.8% / 9.6% – 11.5% | 0.45 / 0.44 |
| Industry | 8.4% – 10.8% | 0.31 |
| Country | 6.6% – 11.8% | 0.23 |
| Referral source | 8.7% – 10.9% | 0.44 |
| Seats, MRR (median churned vs retained) | 23.5 vs 24 seats; $882 vs $931 | 0.56, 0.90 |

- **Product usage:** churned and retained subscriptions are the same on usage events (4.9 vs 5.0), usage count, duration, distinct features used, errors and error rate (all p > 0.2). Churned subscriptions do show higher usage *per day* (p < 0.001), but only because their observed lifetime is shorter while their usage totals are the same. That is an artifact, not a driver.
- **Support:** at account level, ticket volume, resolution time, first-response time, satisfaction score, escalation rate and urgent share do not differ between churned and retained accounts (all p > 0.1).
- **Multivariable model:** a logistic model with all the subscription attributes reaches an AUC of 0.61. That lift comes entirely from the usage-per-day artifact above. Every real attribute is non-significant.
- **Account-level flag:** accounts in DevTools (31% churned) and those referred from events (30%) look high. However, the tests are only borderline (industry p = 0.07, referral p = 0.08), and I ran many tests. Treat these as weak leads, not findings. The account flag does rise with tenure (15% for accounts younger than 90 days, 27% for those older than 18 months), which is the expected pattern. But the flag has no churn date, so it cannot be used for a trend.
- **Stated reasons are not usable.** Reason codes are spread almost evenly (features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%). They are statistically independent of the customer's own feedback text: for example, a "pricing" code is no more likely than any other code to come with "too expensive". The mix did not change between 2023 and 2024 in any way that matters. Read literally, the text says roughly one third "too expensive", one third "missing features" and one third "switched to competitor", with no trend.

## Data-quality issues (these block a reliable driver analysis)

1. **Three churn definitions that disagree.** `accounts.churn_flag` marks 110 accounts. `churn_events` covers 352 accounts, and 277 of them are flagged *not* churned. 35 flagged accounts have no churn event. 38 flagged accounts have no ended subscription at all, and flagged accounts still hold about 9 open subscriptions on average. Only 8% of churn events fall within 7 days of a subscription end.
2. **Churn timing looks synthetic or backfilled** (Finding 2).
3. **Usage is mislinked.** 77% of usage records are dated *before* the subscription they belong to started, and 290 are dated after it ended.
4. **Reason codes don't match feedback text.** 25% of events have no feedback, and 16% are coded "unknown".
5. About 10 subscriptions per account, including accounts that signed up in the last weeks of 2024. This suggests `subscriptions` holds line items or renewals, not contracts. I couldn't confirm which.

## Recommendations

1. **Hold off on a large, untargeted retention investment.** The data supports neither the claim that retention is getting worse nor any specific cause. Money spent now would be aimed at a lever that the data does not show exists.
2. **Fix churn measurement first (owner: RevOps / data engineering, about 4–6 weeks):**
   - Agree a single definition of churn, for example "an account with no active paid subscription for 30 or more days". Derive it from billing records with real cancellation timestamps.
   - Confirm how `end_date` and `churn_date` are filled in. Spot-check about 50 Q4 2024 churned subscriptions against the billing system. This one check tells us whether Finding 2 is an artifact (most likely) or a real early-churn problem (urgent).
   - Repair the link between usage and subscriptions. Make the churn reason a required field, matched to the customer's stated feedback.
3. **Report retention as cohort curves, not counts:** logo and net revenue retention at 3, 6 and 12 months by signup cohort. In a growing base, churn counts will always rise.
4. **Then repeat the driver analysis.** Use survival models on the cleaned data and test the weak leads from this round: DevTools accounts, event-sourced accounts, downgrades, and the "too expensive" / "missing features" feedback themes.
5. **If leadership wants to act now,** run a small, measurable pilot instead of a broad programme. For example, a customer-success outreach to a random half of new accounts in their first 90 days, compared against the other half. That produces clean causal evidence, whatever the data issues turn out to be.

*Method notes:* subscription churn rates use open subscriptions at the start of each quarter as the denominator. Fixed-window (30/60/90-day) churn includes only subscriptions with full follow-up. Group differences were tested with chi-square (categorical) and Mann–Whitney (continuous) tests. With about 20 tests run, a p-value of around 0.05 to 0.1 should be expected by chance.
