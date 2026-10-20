# Customer churn: has retention deteriorated, and what is driving it?

## Bottom line

1. **Over most of the two years, retention has not got worse. Churn counts went up because the customer base grew.** Recorded churn events rose about 7× (73 in 2023, 527 in 2024). Over the same period the number of active subscriptions rose about 6×. Measured as a *rate*, churn among established subscriptions held steady at about 1% per month from 2023 through December 2024.
2. **There is one real-looking deterioration, and it is narrow.** Since about August 2024, and sharply in Nov–Dec 2024, *newly started* subscriptions have been cancelled within their first weeks. This one pattern accounts for nearly all of the rise in the 2024 churn rate. Some of its features (below) suggest it may be partly a data-recording artifact. It needs to be confirmed before money is spent on it.
3. **The data does not identify any driver of churn.** I compared churned and retained customers on product usage, error rates, support experience, plan, seats, price, industry, country and acquisition channel. None of these clearly separates the two groups. The recorded churn reasons are spread almost evenly across six categories, and they don't match the customers' own feedback text.
4. **The data itself is the biggest problem.** The five systems disagree with each other on basic facts, including which customers have churned. Any churn programme funded now would be built on numbers that don't reconcile.

**Recommendation:** don't fund a broad retention programme based on this data. Fund two smaller things first: (a) a short investigation of the Q4‑2024 early-cancellation spike, and (b) a fix to churn definitions and data linkage. Details are at the end.

---

## 1. Has retention deteriorated?

### Raw counts are misleading because the base grew
| | 2023 | 2024 |
|---|---|---|
| Churn events recorded (`churn_events.csv`) | 73 | 527 |
| Subscriptions started | 666 | 4,334 |
| Active subscriptions at start of Jan / Dec of the year | 0 → 530 | 648 → 3,754 |
| New accounts signed up | 227 | 273 |

Churn events per 100 active subscriptions per month were 2–3 in late 2023 and 2–3 across 2024 (Dec 2024: 3.1). On that measure the rate is flat.

### Rate by subscription age (monthly churn = subscriptions ending as churned in the month ÷ subscriptions active in the month)
| Month | Started this month | Age < 90 days | Age 90+ days |
|---|---|---|---|
| Jan–Jun 2024 (range) | 0–1.5% | 0.2–1.8% | 0.4–1.5% |
| Jul 2024 | 0.0% | 1.2% | 0.8% |
| Aug 2024 | 1.5% | 1.5% | 0.9% |
| Sep 2024 | 1.8% | 1.5% | 0.9% |
| Oct 2024 | 1.4% | 2.6% | 1.4% |
| Nov 2024 | 3.6% | 2.9% | 0.8% |
| **Dec 2024** | **10.8%** (103 of 953) | **4.5%** | **1.0%** |

- **Established subscriptions (90+ days) show no deterioration.** Their churn stays around 1% per month for the whole period.
- **Early-life churn has risen.** Share of subscriptions churned within 30 days of starting, by start quarter: 2023Q2–2024Q2 between 0.6% and 1.0%; **2024Q3 2.4%; 2024Q4 6.0%**. Within 90 days: about 3% for 2023Q3–2024Q2 starts, then **6.5%** for 2024Q3 starts.
- Pooled subscription churn was 0.77% per month in 2023 and 1.44% in 2024. Almost all of that gap comes from Q4 2024 (1.97% per month, against about 1% in Q1–Q3 2024).
- **In revenue terms:** MRR on subscriptions that churned was $147k in 2024Q3 and **$872k in 2024Q4**. About $294k of that Q4 figure comes from subscriptions that started *and* ended within December.

### Why the Q4 spike needs checking before acting on it
The December cases don't look like normal customer behaviour:
- 103 subscriptions started in December 2024 and churned in December. Their median life was **7 days**, and **60 of them were annual-billed** contracts.
- Half of them (51) carry end dates of **28–31 December**, right at the edge of the extract. Churned-subscription end dates bunch the same way (Dec 31: 24, Dec 29: 19, Dec 30: 18, against a typical 3–8 per day).
- The increase is the same in **every segment**. For H2‑2024 starts, 30-day churn is 3–6.5% in every plan tier, industry, country, billing frequency, auto-renew setting and acquisition channel, against under 1.5% before. The mix of new subscriptions (plan, trial, billing, auto-renew) did not change.

A spike that is identical in every segment, bunched at year-end and full of week-old annual contracts fits either of two causes: something company-wide that started around Q3 2024 (onboarding, provisioning, billing or a policy change), or a year-end process that closed records out (cleanup, migration, or the way the extract stamps end dates). **I can't tell these apart with this data.** Treat the deterioration as *probable but unconfirmed*.

Account-level churn rates by signup cohort fall over time (2023H1 26.6%, 2023H2 24.6%, 2024H1 21.5%, 2024H2 17.1%). That isn't evidence either way: older accounts have simply had longer to churn, and the account churn flag has no date.

## 2. What is driving churn?

### No product, support or commercial factor separates churners from retained customers
| Factor | Retained | Churned | Test p-value |
|---|---|---|---|
| Usage records per subscription | 5.0 | 4.9 | 0.37 |
| Errors per use | 0.059 | 0.056 | 0.67 |
| Share of usage on beta features | 10.2% | 10.7% | 0.74 |
| Distinct features used | 4.7 | 4.6 | 0.41 |
| Seats (subscription) | 29.9 | 29.8 | 0.56 |
| MRR (subscription) | $2,251 | $2,426 | 0.90 |
| Support tickets per account | 4.0 | 3.9 | 0.34 |
| Avg resolution time (h) | 36.5 | 35.5 | 0.72 |
| First response (min) | 89.6 | 84.9 | 0.10 |
| Satisfaction score (1–5) | 3.95 | 4.00 | 0.54 |
| Escalation rate | 4.4% | 6.2% | 0.39 |

The first six rows compare at subscription level (subscription churn flag). The support rows compare at account level (account churn flag). Tests are Mann-Whitney.

- **Plan tier:** account churn is 22.0% for Basic, 22.1% for Enterprise and 21.9% for Pro.
- **Trial vs paid, country, seats:** no significant difference.
- **Multivariate model** (logistic regression of account churn on industry, channel, plan, trial and seats): it does not beat a model with no predictors (p = 0.13). The one notable coefficient is **DevTools**: 31% churn against 16–22% for the other industries (p = 0.01 on its own). That is one of 13 coefficients in a model that isn't significant overall, so treat it as a lead to check, not a finding. Accounts referred by events (30%) and partners (15%) are similarly only suggestive.

### Stated churn reasons don't point anywhere
- The reason codes are spread almost evenly: features 19%, support 17%, budget 17%, unknown 16%, pricing 15%, competitor 15%. The mix did not change between 2023 and 2024 (χ² p = 0.48).
- The reason codes have **no relationship** to the customers' own feedback text (χ² p = 0.95). For example, "switched to competitor" feedback is filed under budget, pricing, support and features about as often as under competitor. Across the free text, "too expensive" (161), "missing features" (155) and "switched to competitor" (136) are about equally common; 148 events have no text.

**Conclusion:** the available fields don't explain who churns. Either churn is driven by something not captured here (contract events, champion turnover, budget cycles, the onboarding experience), or the linkage problems below are hiding the signal.

## 3. Data quality: read before relying on any churn number

| Issue | Evidence |
|---|---|
| The account churn flag and the churn-events table disagree | 277 of 390 "not churned" accounts have at least one churn event; 35 of 110 "churned" accounts have none |
| "Churned" accounts are still active | All 500 accounts still have open subscriptions; flagged-churned accounts average 9.2 open subscriptions each |
| Plan tier doesn't match across tables | A subscription's plan tier matches its account's plan tier only 33% of the time; trial status matches 71% |
| Usage isn't tied to subscription dates | 77% of usage records are dated *before* the subscription they belong to started; usage volume is flat at about 3,100 rows per quarter while subscriptions grew 6× |
| Support tickets come before signup | 54% of tickets are dated before the account's signup date |
| Reason codes don't match feedback text | They are statistically independent (p = 0.95) |
| Duplicate IDs | 21 usage IDs are reused across different subscriptions |
| Year-end bunching | Churned subscriptions' end dates bunch on 28–31 Dec 2024 |

Because of these problems, the usage and support comparisons above rely on links that may be broken. "No driver found" is therefore partly "no driver *can* be found in this data".

## 4. Recommendations

1. **Don't fund a broad retention programme yet.** Established customers aren't churning more. A programme aimed at "deteriorating retention" in general would target a problem the data doesn't show.
2. **Investigate the Q4‑2024 early-cancellation spike first (about 2 weeks).** Pull the 103 December start-and-cancel subscriptions and the roughly 50 from Oct–Nov, and check them against billing and CRM records:
   - Were they genuine customer cancellations, or system closures (migration, duplicate cleanup, failed provisioning, year-end process)?
   - Did anything change around Aug–Sep 2024 in onboarding, provisioning, pricing or contract terms?
   - If the spike is real, the response is **onboarding and early-life activation for new subscriptions**. That cohort is the only one that got worse, and it was about $290k MRR in December alone.
3. **Fix the measurement before measuring the drivers.** Agree one definition of churn (account vs subscription, with a churn date). Reconcile the account churn flag with the churn-events table. Repair the subscription ↔ usage and account ↔ ticket date links. Make the churn reason a required, validated field consistent with the feedback.
4. **Follow up cheap leads once the data is clean:** higher churn in DevTools (31%) and among event-sourced accounts (30%). These are only hypotheses at present.
5. **Track retention as rates, not counts.** Report monthly churn rate and MRR churn rate split by subscription age (new / under 90 days / 90+ days). Raw churn counts will keep rising as the company grows, even if retention holds.

## Method and assumptions
- **Period:** January 2023 – 31 December 2024 (extract end). Subscriptions with no end date are treated as active at extract end.
- **Subscription churn** means `churn_flag = True` in `subscriptions.csv`; the churn date is `end_date`. These two always coincide in the data.
- **Account churn** uses `accounts.churn_flag`; churn events use `churn_events.csv`. They can't be reconciled (section 3), so I report each separately and don't merge them.
- **Monthly rate** = subscriptions ending as churned in the month ÷ subscriptions active at any point in the month. Fixed-horizon cohort rates only include cohorts with the full horizon observed.
- Usage per subscription is not adjusted for exposure time, because usage dates don't line up with subscription dates. Comparisons use non-parametric tests, and p-values are not corrected for multiple comparisons; marginal results are labelled as hypotheses.
