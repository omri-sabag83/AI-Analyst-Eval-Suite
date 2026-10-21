# Customer churn: has retention deteriorated, and what drives it?

## Bottom line

1. **The data does not show that retention has deteriorated.** Raw churn counts rose sharply: recorded churn events went from 6 in Q1 2023 to 251 in Q4 2024. Over the same period the customer base grew from 55 to 500 accounts, and active subscriptions grew from 31 to about 4,800. Measured as a share of the base, churn was roughly flat at about 2–3% of subscriptions per quarter from Q4 2023 to Q3 2024. Only Q4 2024 jumps (to 6.7%), and that jump has the marks of a data-extract artifact rather than a change in customer behaviour (see §2).
2. **No customer attribute, usage pattern or support pattern in this data reliably predicts churn.** Plan tier, seats, MRR, billing frequency, auto-renew, trial status, product usage, error rates, ticket volume, resolution time, first-response time and CSAT all show churn rates within a point or two of each other. A model using all of them explains less than 5% of the variation (pseudo-R² 0.048), and the model as a whole is not significant (p = 0.07).
3. **The three "churn" records in the company's systems contradict each other**, and the churn-reason data is internally inconsistent. Until these are reconciled, nobody can reliably say what is driving churn from this data, including this analysis.

**Recommendation:** Do not fund a large churn response aimed at a specific driver yet. The evidence cannot tell you which driver to target. Spend a small amount first on fixing churn measurement (§5). That work takes weeks, not quarters, and it decides whether a larger investment is warranted.

---

## 1. What I did and what I assumed

- Data: 500 accounts, 5,000 subscriptions, 25,000 feature-usage rows, 2,000 support tickets and 600 churn events, covering January 2023 to December 2024.
- **Assumption:** a subscription with an `end_date` has churned. This is exact in the data: `churn_flag = True` if and only if `end_date` is filled.
- **Assumption:** the extract ends on 2024-12-31. Subscriptions still open on that date are treated as "still active" (right-censored). Rates are calculated against the base that was actually at risk, because comparing raw counts across a period of 9× growth would mislead.
- Three churn measures exist: the account-level `churn_flag`, subscription end dates, and `churn_events`. I analysed all three and report where they disagree.

## 2. Has retention deteriorated?

### Raw counts rise steeply, but they are driven by growth

| Quarter | Accounts signed up to date | Subscriptions exposed in quarter | Subscriptions ended | **Ended / exposed** | Churn events |
|---|---|---|---|---|---|
| 2023 Q2 | 109 | 137 | 2 | 1.5% | 11 |
| 2023 Q3 | 162 | 338 | 2 | 0.6% | 19 |
| 2023 Q4 | 227 | 662 | 14 | 2.1% | 37 |
| 2024 Q1 | 283 | 1,120 | 27 | 2.4% | 54 |
| 2024 Q2 | 348 | 1,779 | 37 | 2.1% | 92 |
| 2024 Q3 | 420 | 2,849 | 80 | 2.8% | 130 |
| 2024 Q4 | 500 | 4,838 | 324 | **6.7%** | 251 |

Churn events grew about 40× while the subscription base grew about 150×. From Q4 2023 to Q3 2024 the subscription churn rate stayed in a narrow 2.1–2.8% band.

### The Q4 2024 jump is probably not real

- 193 of the 324 Q4 end dates fall in December, and 79 fall in the last six days of the year (24 on 31 December alone). That kind of pile-up at the edge of an extract usually comes from how the data was cut, not from customers.
- **The data behaves as if every customer churns about the same amount regardless of how long they have been a customer.** On average:

  | Signup year | Subscriptions / account | Churned subscriptions / account | Churn events / account | Account `churn_flag` rate |
  |---|---|---|---|---|
  | 2023 (12–24 months observed) | 10.1 | 0.97 | 1.22 | 26% |
  | 2024 (0–12 months observed) | 9.9 | 0.97 | 1.18 | 19% |

  An account that signed up in Q4 2024 has, within a few weeks, already accumulated as many subscriptions, churned subscriptions and churn events as an account with two years of history. When churn happens, its timing is spread evenly between start date and extract end. For churned subscriptions, the fraction of the observable window that had passed at churn is statistically indistinguishable from uniform (KS test p = 0.25). Churn events are spread the same way across each account's time since signup.
- This pattern means that any rate measured per calendar period mechanically rises as the base gets younger, which is exactly what happened in 2024. There are only two readings, and the data cannot separate them:
  - (a) **Real effect:** newer customers churn many times faster than older ones did, compressed into their first weeks.
  - (b) **Data artifact:** churn dates in this extract do not reflect real timing. Examples would be backfilled or synthetic dates, or an extract that assigns end dates within the window.

  Reading (b) fits better, given the data-quality problems in §4. Before anyone acts on a "deterioration" story, the data owners need to confirm which reading is correct.
- On the one measure that is not tied to calendar timing, the account `churn_flag`, newer cohorts look *better*: 29% for Q1 2023 signups versus 15% for Q4 2024 signups. That is what you would expect simply because older accounts have had more time to churn. It is not evidence of deterioration.

**Conclusion:** I cannot confirm that retention deteriorated. Excluding the questionable Q4 2024 quarter, the base-adjusted rate was stable. The headline rise in churn counts is mostly explained by a 9× larger customer base.

## 3. What drives churn?

I tested every available attribute against both the account-level `churn_flag` and subscription churn, with subscription churn adjusted for time at risk.

**Subscription level (5,000 subscriptions, 486 churned; churn per 1,000 subscription-days, ~0.60 overall):**

- Plan tier: Basic 0.57, Pro 0.60, Enterprise 0.63
- Trial vs paid: 0.61 vs 0.60
- Monthly vs annual billing: 0.58 vs 0.62
- Auto-renew on vs off: 0.60 vs 0.60
- Seat or MRR quartile: 0.54–0.66, with no trend
- Error rate in product usage: 0.54–0.64, with no trend
- Prior downgrade: 0.71 vs 0.60, on only 218 subscriptions. This was a small, non-significant difference and is directionally plausible.

**Account level (110 of 500 churned, 22%):**

- Plan tier: 22.0% / 22.1% / 21.9% (p = 1.0)
- Support: churned and retained accounts look alike on ticket count (3.9 vs 4.0), resolution time (35 vs 36 h), first-response time (85 vs 90 min), CSAT (4.0 vs 4.0) and escalation share (6% vs 4%). None of these differences is significant.
- Usage: churned accounts used the product slightly *more* than retained ones (522 vs 495 feature uses), with similar error rates.
- Industry: DevTools stands out (31% vs 16–22% elsewhere; p = 0.015 in a multivariable model). However, I ran about 20 tests, so one result like this is expected by chance. It also does not hold up at the subscription level (DevTools 0.64 vs 0.60 overall). **Treat it as a lead to watch, not a driver.**
- Referral source (partner 15%, event 30%) and country (DE 32%, AU 13%) show differences of a similar kind. None is significant, and the groups are small.

**Stated churn reasons** are spread almost evenly: features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%. The mix barely moves between 2023 and 2024. As §4 shows, these codes are not reliable.

**Conclusion:** nothing in this data is a demonstrated churn driver. Funding a response aimed at pricing, support speed, onboarding or a specific plan tier would currently rest on assumption, not on evidence from this data.

## 4. Data-quality problems that block a reliable answer

1. **The account churn flag does not match subscriptions.** All 110 accounts flagged as churned still have active (open) subscriptions, averaging 9.2 each.
2. **Churn events do not match the churn flag.** 71% of *non-churned* accounts have at least one churn event, compared with 68% of churned accounts. Events per account are 1.19 for retained and 1.23 for churned accounts.
3. **Churn events do not match subscription end dates.** Only 1% of churn events fall on the same day as one of that account's subscription end dates, and only 8% within 7 days.
4. **Reason codes contradict the customer's own feedback.** For example, events coded `features` carry "too expensive" as often as "missing features", and `pricing`-coded events say "switched to competitor" as often as "too expensive". The reason code and the feedback text are statistically independent.
5. **Subscription volume is implausible.** The average account has about 10 subscriptions, and 2,069 subscriptions started in Q4 2024 alone, against 80 new accounts. This suggests "subscription" may record plan or seat changes rather than contracts, which would make subscription-level churn overstate customer loss.
6. Minor issues: 41% of tickets have no CSAT score, and there are 21 duplicate `usage_id`s, which do not affect any conclusion.

## 5. Recommendations

1. **Before funding anything, fix how churn is measured. This is the priority.**
   - Agree on one definition of churn: an account with no active paid subscription, with a churn date.
   - Reconcile `accounts.churn_flag`, subscription end dates and `churn_events` against billing or revenue records.
   - Confirm with the data owners whether the late-December 2024 end dates and the flat per-account churn counts reflect real behaviour or the extract process.
2. **Then re-measure the trend properly.** Track monthly logo churn and net/gross MRR churn against the active base at the start of each month, plus cohort retention curves (share of each signup cohort still active at 3, 6 and 12 months). If those show deterioration, the case for funding becomes sound.
3. **Fix how churn reasons are captured.** Use one mandatory reason at cancellation that is validated against the free-text feedback, so the next driver analysis has usable labels.
4. **Low-cost, reversible step in the meantime:** watch the two weak leads, DevTools accounts and accounts that downgrade. A downgrade could reasonably trigger a customer-success check-in. Do not commit significant spend to them until clean data confirms them.
5. **What would change this conclusion:** clean data showing that cohort 6- or 12-month retention fell for 2024 signups compared with 2023 signups would confirm deterioration. A segment that keeps its churn gap after controlling for tenure and plan would be a fundable target.

## Confidence

- **High:** raw churn growth is largely explained by growth in the base, and the three churn records are mutually inconsistent.
- **Medium:** the Q4 2024 spike is an artifact. The pattern strongly suggests it, but only the data owners can confirm it.
- **High:** none of the measured attributes is a strong churn driver *in this data*. That does not prove that none exists in reality, given the labelling problems above.
