# Customer churn drivers: assessment for leadership

## Bottom line

1. **The data does not show that retention has deteriorated.** Raw churn counts rise steeply through 2024, but the customer base and the number of subscriptions grew just as fast. The way dates are recorded in these extracts also makes almost every event cluster near the end of 2024, whatever the true trend. Once growth is accounted for, the subscription churn rate was flat at about 1% per month from January to September 2024. The rise in Q4 2024 matches the same recording artifact and should not be read as real deterioration yet.
2. **None of the recorded attributes explains churn.** I tested about 25 account, subscription, support and usage variables against two churn definitions. No variable separates churned from retained customers beyond what chance would produce, and a multivariate model predicts churn no better than a coin flip (cross-validated AUC 0.50). The reason codes customers give for leaving don't match their own free-text feedback, so they can't be used to rank causes either.
3. **The main finding is data quality.** The three churn records (the account flag, subscription end dates and churn events) contradict each other, and usage timestamps don't line up with subscription dates. Until this is fixed, any churn programme would be funded without evidence.

**Recommendation:** don't fund a large churn-response programme based on this data. Spend a small amount (weeks, not quarters) on fixing the churn definition and the data pipeline, then repeat this analysis. Details are at the end.

---

## 1. Has retention deteriorated?

### What the raw numbers show (and why they mislead)

| Quarter | Churn events recorded | Subscriptions ended | Accounts signed up (cumulative) | New subscriptions started |
|---|---|---|---|---|
| 2023 Q1 | 6 | 0 | 55 | 31 |
| 2023 Q3 | 19 | 2 | 162 | 203 |
| 2024 Q1 | 54 | 27 | 283 | 472 |
| 2024 Q3 | 130 | 80 | 420 | 1,107 |
| 2024 Q4 | 251 | 324 | 500 | 2,069 |

Churn events grew roughly 40× from 2023 Q1 to 2024 Q4. That growth is what would make retention look like it is collapsing. Over the same period, though, the number of accounts grew about 9× and the number of subscriptions started each quarter grew about 65×.

### Rates once growth is accounted for

Churn rate here means subscriptions ended ÷ subscription-months at risk in the period:

| Period | Monthly subscription churn rate |
|---|---|
| 2023 Q4 | 0.97% |
| 2024 Q1 | 1.06% |
| 2024 Q2 | 0.88% |
| 2024 Q3 | 1.19% |
| Oct / Nov / Dec 2024 | 1.9% / 2.1% / 4.6% |

Revenue-weighted (MRR) churn follows the same pattern. The rate was flat for nine months and then rose in the last quarter of the extract.

### Why I don't treat the Q4 2024 rise as real

The way dates are spread in these extracts shows that they don't behave like a real time series:

- **Dates are spread evenly between signup and the extract date.** For every account, subscription start dates and churn-event dates fall evenly across the window from signup to 31 Dec 2024. The 10th, 25th, 50th, 75th and 90th percentiles of each date's position in that window are 0.10, 0.24, 0.50, 0.75 and 0.90. Subscription end dates behave the same way within the window from start to extract date.
- **The number of events doesn't depend on how long an account has been a customer.** Accounts that signed up in 2023 Q1 (about 22 months of history) have 1.16 churn events each. Accounts that signed up in 2024 Q4 (under 2 months) have 1.11. The number of subscriptions per account is also unrelated to tenure (correlation 0.06).
- When each customer's events are squeezed into the time between their signup and the extract date, the apparent churn rate rises toward that date automatically. Per account-month, churn events rise from 0.05 for the oldest signup cohort to 0.66 for the newest. That is the artifact, not a change in customer behaviour.
- **Subscription length doesn't behave like billing.** 97% of churned *annual* subscriptions ended less than 12 months after they started, and 10.8% of subscriptions under 30 days old are already marked ended. Real annual contracts don't end like that.

**Conclusion:** the claim that retention has deteriorated isn't supported. The visible increase is explained by growth plus how dates are recorded. The data can't rule out a real Q4 2024 rise either. That question should be answered again once the date issues below are fixed.

### What the level of churn looks like

- 22% of accounts (110 of 500) carry `churn_flag = True`.
- About 9.7% of subscriptions have ended.
- 70% of accounts (352) have at least one churn event, and there are 600 events in total, 61 of which are reactivations.

These three numbers can't all be true at once; see section 3.

---

## 2. What is driving churn?

### Method

- I built one row per account (500 accounts), covering firmographics, plan, seats, trial status, subscriptions, support tickets and feature usage.
- I compared churned and retained accounts under two definitions: the official `churn_flag`, and "has any churn event". I used chi-square tests for categories and Mann-Whitney tests for numbers.
- I repeated the test at subscription level (5,000 subscriptions) with a Poisson rate model, so that subscriptions observed for longer don't get unfair weight.
- I fitted multivariate models (regularised logistic regression and a random forest) and scored them with 5-fold cross-validation, repeated 5 times.

### Results

**No meaningful driver was found.**

| Candidate driver | Churned vs retained (account `churn_flag`) | p-value |
|---|---|---|
| Plan tier (Basic / Pro / Enterprise) | 22.0% / 21.9% / 22.1% churn | 1.00 |
| Trial vs paid | 25.8% vs 21.1% | 0.39 |
| Seats (mean) | 19.2 vs 20.9 | 0.69 |
| Support tickets per account | 3.9 vs 4.0 | 0.34 |
| Mean resolution time (h) | 35.5 vs 36.5 | 0.72 |
| CSAT (mean) | 4.00 vs 3.95 | 0.54 |
| Escalations per account | 0.22 vs 0.18 | 0.40 |
| Share of subscriptions upgraded / downgraded | 10.3% vs 10.6% / 4.1% vs 4.4% | 0.89 / 0.73 |
| Auto-renew share, annual billing share | 80% vs 80%, 49% vs 49% | 0.86 / 0.88 |
| Feature usage, error rate, beta-feature share | no material difference | 0.12 to 0.87 |
| Country | — | 0.66 |

At subscription level, the plan, billing frequency, auto-renew, trial, upgrade, downgrade and seats effects are all non-significant (all p > 0.15).

**Multivariate models can't predict churn.** Cross-validated AUC is 0.51 for logistic regression and 0.50 for the random forest on `churn_flag`, and 0.45 to 0.48 for "any churn event". An AUC of 0.50 is coin-flip performance.

**Weak signals I would not act on yet:**

- **Industry:** DevTools accounts churn at 31%, against 16 to 22% in the other industries (p = 0.066).
- **Referral source:** event-sourced accounts churn at 30%, against 15% for partner-sourced (p = 0.079).

Neither is significant even before allowing for the roughly 50 comparisons I ran, and a few results this strong are expected by chance. The one nominally significant result (tickets per month, p = 0.046) points the "wrong" way: churned accounts file *fewer* tickets per month. It is what you'd expect from chance alone.

**A trap to avoid:** churned subscriptions appear to have more than twice the daily usage of retained ones (4.3 vs 1.8 uses per day, p < 0.001). This is purely an artifact: churned subscriptions are observed for fewer days, and 77% of usage records are dated *before* the subscription they belong to started. It should not be read as "heavy users churn".

### Stated churn reasons are unreliable

- Reason codes are spread almost evenly: features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%. The mix didn't change between 2023 and 2024 (p = 0.48).
- More importantly, the reason code is unrelated to the customer's own feedback text. For example, events coded "budget" are as likely to say "switched to competitor" (24) as "too expensive" (28) or "missing features" (24). Events coded "competitor" say "too expensive" more often than "switched to competitor".
- So these fields can't be used to choose between a pricing, product or support response.

---

## 3. Data-quality problems that block a real answer

| Issue | Evidence |
|---|---|
| Three churn definitions disagree | 35 of the 110 accounts with `churn_flag` have no churn event. 277 accounts with churn events are flagged *not* churned. **All 110 flagged accounts still have active subscriptions.** No account has all of its subscriptions ended. |
| Event dates look generated or backfilled rather than recorded when they happened | Start, end and churn dates are spread evenly between signup (or start) and the extract date. Event counts don't depend on tenure. |
| Subscription terms don't match billing | 97% of churned annual subscriptions ended within 12 months. Many subscriptions end within days of starting. |
| Usage isn't linked to the subscription timeline | 77% of usage rows are dated before their subscription's start date. |
| Reason codes contradict feedback text | The coded reason and the free-text feedback are independent of each other. |
| Smaller issues | 21 duplicate `usage_id`s. 41% of tickets have no CSAT score. 4 subscription rows are exact duplicates apart from their ID. |

### Assumptions I made

- 2024-12-31 is the extract or observation date.
- A subscription with no `end_date` is still active.
- `churn_flag` in `accounts.csv` is the "official" account churn label.
- Because none of these sources is clearly authoritative, I tested drivers against both the account flag and churn events, and against subscription end dates. The conclusions are the same under all three.

---

## 4. Recommendations

1. **Hold off on a large retention investment justified by "churn is getting worse" or by any single driver.** This data supports neither claim. If money goes into pricing changes, support staffing or product features now, it can't be shown to work, because the baseline itself is unreliable.
2. **Agree one churn definition and enforce it in the data (top priority, low cost).** For example: an account has churned when its last paid subscription ends and doesn't renew within 30 days. Then make `churn_flag`, subscription `end_date` and `churn_events` consistent with that definition, and store reactivations as separate events.
3. **Fix how dates are recorded.**
   - Find out why subscription start and end dates and churn dates appear spread evenly up to the extract date. This could be a backfill, or an extract that rewrites history.
   - Make annual subscriptions carry real term-end dates.
   - Make usage records join to the subscription that was active on the usage date.
4. **Make churn reasons trustworthy.** Use a single required reason field, captured at cancellation, with the free text kept alongside it. Audit a sample of recent cancellations against CRM notes.
5. **Then re-run this analysis.** Use monthly logo and MRR churn rates by signup cohort with a proper at-risk denominator, plus a survival model for drivers. With clean data, 500 accounts is enough to detect large effects. It is not enough for small ones, so also widen the extract to include all accounts, not a sample.
6. **Low-cost monitoring meanwhile.**
   - Track monthly subscription churn rate, not churn counts. The baseline is about 1% per month.
   - Watch whether the Q4 2024 rise persists in Q1 2025 once those months have fully closed.
   - Keep an eye on DevTools and event-sourced accounts, which are the weak signals above. Treat them as hypotheses to confirm, not as places to spend money.
