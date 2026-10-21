# Customer churn: has retention deteriorated, and what is driving it?

## Bottom line

1. **For most of the period, retention has not deteriorated. Churn *volume* went up because the customer base grew.** Recorded churn events rose from 73 in 2023 to 527 in 2024. Over the same period, the number of active subscriptions grew about 7x. Measured as a *rate* (churn per active subscription), churn was flat from Q4 2023 through Q3 2024. Subscriptions older than three months churned at about 1% per month the whole time.
2. **The one real deterioration is recent and narrow. In Q4 2024, and mostly in December, brand-new subscriptions churned at a much higher rate.** Subscriptions less than a month old churned at 5.7% per month in Q4 2024, compared with 0.5–1.4% in earlier quarters. About 15% of all subscription endings in the two years fall on 28–31 December 2024, so part of this spike may be a year-end or data-extract artifact. It needs to be checked before anyone acts on it.
3. **The data does not identify a churn driver.** Plan tier, billing terms, trial status, industry, acquisition channel, seat count, product usage, errors and support experience all fail to separate churners from non-churners. Predictive models score at chance level (AUC ≈ 0.50). The recorded churn reasons are spread almost evenly across categories, and they don't agree with the customers' own free-text feedback.
4. **Recommendation: don't fund a broad churn-reduction programme on this evidence.** Spend first on (a) checking whether the Q4/December spike in early churn is real and (b) fixing how churn is defined and recorded. If the spike is real, run a small, measured onboarding intervention aimed at the first 30 days of a subscription.

---

## 1. Has retention deteriorated?

### Counts mislead because the base grew
| Quarter | Subscriptions active in quarter | Subscriptions ended | Ended / active | Churned MRR as % of active MRR (paid) | Churn events | Churn events / active subscriptions |
|---|---|---|---|---|---|---|
| 2023 Q1 | 31 | 0 | 0.0% | 0.0% | 6 | (tiny base) |
| 2023 Q2 | 137 | 2 | 1.5% | 0.6% | 11 | 8.0% |
| 2023 Q3 | 338 | 2 | 0.6% | 0.1% | 19 | 5.6% |
| 2023 Q4 | 662 | 14 | 2.1% | 3.7% | 37 | 5.6% |
| 2024 Q1 | 1,120 | 27 | 2.4% | 2.2% | 54 | 4.8% |
| 2024 Q2 | 1,779 | 37 | 2.1% | 1.5% | 92 | 5.2% |
| 2024 Q3 | 2,849 | 80 | 2.8% | 2.4% | 130 | 4.6% |
| 2024 Q4 | 4,838 | 324 | **6.7%** | **7.9%** | 251 | 5.2% |

- The number of churn events rose about 40x between Q1 2023 and Q4 2024, but the number of active subscriptions rose about 150x. Churn events per active subscription have been **flat at about 5% per quarter** since mid-2023. The rising count that leadership sees comes from growth.
- If you divide churn events by *accounts* instead, the rate does climb, from 0.11 to 0.50 events per account per quarter. That happens because each account holds more subscriptions over time (10 on average by the end), and churn events track subscriptions. This is an artifact of the denominator, not a sign that customers are less healthy.
- Subscription-ending churn stayed at 2–3% per quarter until Q3 2024 and then jumped to 6.7% in Q4. By month, it ran at 0.7–1.4% from January to September 2024, then 1.8% in October, 1.9% in November and **4.1% in December**.

### The Q4 increase is confined to new subscriptions
Monthly churn rate by subscription age (share of active subscriptions that ended in the month):

| Quarter | < 1 month old | 1–3 months | 3–6 months | 6+ months |
|---|---|---|---|---|
| 2024 Q1 | 0.8% | 1.3% | 1.2% | 0.5% |
| 2024 Q2 | 0.5% | 1.0% | 0.7% | 1.1% |
| 2024 Q3 | 1.4% | 1.3% | 1.3% | 0.6% |
| 2024 Q4 | **5.7%** | **2.5%** | 1.1% | 1.0% |

- Established subscriptions (3+ months old) churned at a steady rate of about 1% per month. **Retention of the existing book has not deteriorated.**
- The increase sits entirely in subscriptions that started recently. New subscriptions are also the fastest-growing part of the base: 2,069 of the 5,000 subscriptions started in Q4 2024. Over the whole period, churn risk is highest in the first 30 days (4.6% per month, against about 1% after six months).
- **Data caveat on the spike.** 71 of the 486 subscription endings in two years (15%) fall on 28–31 December 2024, and those subscriptions lasted a median of about 11 days. The Q4 early-churn rate is similar across plan tiers, industries, channels, trial vs paid and billing frequency (6–10% ended within 30 days). An effect that spreads evenly across every segment fits a process or recording cause (year-end billing cleanup, contract-end defaults, an extract cut-off) better than a customer-behaviour cause. Before acting, check whether these endings are genuine cancellations.

## 2. What is driving churn?

I tested each candidate driver in three ways, because the data contains three churn definitions that disagree (see section 3):
- **Account `churn_flag`** (110 of 500 accounts)
- **Account has any churn event** (352 of 500 accounts)
- **Subscription ended**, adjusted for how long each subscription was observed (Poisson rate model)

| Candidate driver | Result |
|---|---|
| Plan tier (Basic / Pro / Enterprise) | No difference: 22.0% / 22.1% / 21.9% flagged; 1.7–1.9 endings per 100 subscription-months |
| Billing frequency, auto-renew, trial | No difference (rate ratios 0.96–1.08, p > 0.5) |
| Upgrades / downgrades | Directionally as expected (downgrade 2.2, upgrade 1.5, no change 1.8 per 100 subscription-months) but not significant (p = 0.43–0.56) |
| Seats, MRR | No relationship |
| Product usage, features used, error rate, beta usage | No relationship. (A naive "usage per month" metric looks strongly predictive, but it is an artifact: every subscription has about 5 usage records regardless of how long it lasted, so short-lived subscriptions mechanically show high usage per month.) |
| Support tickets, resolution time, first response, CSAT, escalations | No relationship (all p > 0.08) |
| Country, acquisition channel | No significant difference |
| Industry | DevTools has a higher account `churn_flag` rate (31% vs 19%, p = 0.013 before adjustment). This does **not** survive the roughly 40 comparisons I ran, and it doesn't replicate on the other two churn definitions (73.5% vs ~70% with a churn event; subscription rate ratio 1.07, p = 0.63). I treat it as noise. |
| All factors combined | Gradient-boosted model, cross-validated AUC = 0.50 (flag) and 0.49 (events). That is no better than a coin flip. The logistic regression is not jointly significant (p = 0.06, pseudo-R² = 0.05). |

**Recorded churn reasons don't help.** The reason codes are spread almost evenly: features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%. They also don't match the customers' own feedback. For example, churns coded "pricing" are as likely to carry "missing features" or "switched to competitor" text as "too expensive". As currently captured, the reason codes can't tell you where to spend money.

**Conclusion:** none of the tracked attributes of an account, its subscriptions, its product usage or its support experience explains who churns. Churn looks broadly spread across the customer base. The one structural pattern is that new subscriptions are the most fragile.

## 3. Data quality issues that limit any conclusion

- **The churn definitions contradict each other.** 277 accounts with `churn_flag = False` have recorded churn events, and 35 accounts with `churn_flag = True` have none. Accounts flagged as churned still hold about 9 open subscriptions on average, the same as non-churned accounts. As defined today, "churn" is not one thing.
- Churn events: 600 events across 352 accounts, including 61 reactivations and up to 5 events per account. Events seem to record subscription-level or partial churn, not the loss of the customer.
- Reason codes don't agree with the free-text feedback (above). 25% of events have no feedback, and 41% of tickets have no CSAT score.
- 21 duplicate usage IDs (immaterial). The data ends on 31 December 2024, so subscriptions that started recently have very little observation time.

**Assumptions:** an open `end_date` means the subscription was active on 31 December 2024. A subscription counts as churned when it has an `end_date`, which matches its `churn_flag` exactly. Trial subscriptions are included in subscription counts and excluded from MRR figures.

## 4. Recommendations

1. **Don't fund a broad churn-reduction programme on the "retention is deteriorating" premise.** For the established customer base it isn't true. The rising churn counts come from growth.
2. **Investigate the Q4 2024 spike in early churn first. This is a low-cost check of a few days' work.** Pull the 193 December subscription endings, especially the 71 on 28–31 December, and confirm whether they are real customer cancellations or the result of billing, contract-end, trial-expiry or extract processes. The spike is spread evenly across every segment, which points to a process cause.
3. **If the spike is real, target the first 30 days of a subscription.** Run a controlled onboarding or activation intervention (with a holdout group) on new subscriptions. Measure 30- and 90-day survival rather than the overall churn count.
4. **Fix churn measurement before the next decision.**
   - Adopt one definition of churn, and report it as a rate against active customers, broken out by cohort and tenure.
   - Report net and gross revenue retention alongside logo churn.
   - Make the churn reason a required field with a validated taxonomy that is consistent with the free-text feedback.
   - Keep `accounts.churn_flag` in sync with subscription status.
5. **Add the signals the current data lacks.** Usage logs are a fixed sample of about 5 records per subscription, so they can't measure engagement over time. Time-series product usage, health scores and contract/renewal dates would be needed to find actual drivers.
