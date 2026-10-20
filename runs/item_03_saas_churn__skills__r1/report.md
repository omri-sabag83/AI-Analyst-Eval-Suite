# Customer churn drivers: findings and recommendation

## Bottom line

1. **The data does not show that retention has deteriorated.** Recorded churn events went from 6 in Q1 2023 to 251 in Q4 2024, but most of that is because the customer base grew from 55 to 500 accounts. What's left after allowing for growth comes from the way churn events are dated in the extract. It doesn't reflect how customers behave (details below). The one churn measure that doesn't have this problem, the account-level `churn_flag`, is *lower* for newer customers than for older ones. That is the pattern you'd expect if retention is stable.
2. **No reliable churn driver shows up.** Churned and retained accounts look almost identical on plan, seats, trial status, acquisition channel, country, support experience, product usage, errors, billing terms and auto-renew. Recorded churn reasons are spread almost evenly across six categories, and the free-text feedback doesn't match the reason codes.
3. **The real problem is measurement.** The five systems disagree on who has churned and when. Usage and support records are dated outside the subscriptions and accounts they belong to. Until this is fixed, no analysis can say reliably what drives churn.

**Recommendation:** don't fund a large churn programme on this evidence yet. Fund a short (roughly 4–6 week) effort to fix churn instrumentation and agree on one churn definition, and then repeat this analysis. Details are at the end.

---

## 1. Has retention deteriorated?

### What the headline numbers say

| Quarter | Accounts signed up to date | Churn events | Events per account | Accounts with ≥1 event / accounts |
|---|---|---|---|---|
| 2023 Q1 | 55 | 6 | 0.11 | 11% |
| 2023 Q2 | 109 | 11 | 0.10 | 10% |
| 2023 Q3 | 162 | 19 | 0.12 | 10% |
| 2023 Q4 | 227 | 37 | 0.16 | 16% |
| 2024 Q1 | 283 | 54 | 0.19 | 18% |
| 2024 Q2 | 348 | 92 | 0.26 | 22% |
| 2024 Q3 | 420 | 130 | 0.31 | 25% |
| 2024 Q4 | 500 | 251 | 0.50 | 36% |

Looked at alone, this table seems to confirm leadership's concern. Even after dividing by the customer base, the churn-event rate rises about fourfold. Comparing signup cohorts over the same tenure gives the same picture: the share of accounts with a churn event within 90 days of signing up rises from 13–18% for 2023 H1 signups to 46–60% for 2024 Q2–Q3 signups. Subscriptions ending within 60 days of starting also rise in late 2024.

### Why I don't believe it

The rise is explained by how the records are dated, not by how customers behave:

- **Every account has about the same number of churn events and subscriptions, however long it has been a customer.** Accounts that signed up in Q1 2023 average 1.16 churn events and 9.5 subscriptions. Accounts that signed up in Q4 2024, which are at most a few weeks old, average 1.11 churn events and 9.2 subscriptions. In a real churn process, older accounts would build up more events because they've been exposed for longer.
- **Within each account, churn events are spread evenly between signup and the end of the extract.** I placed each event on a scale from 0 (signup date) to 1 (31 Dec 2024). The five equal bands hold 120 / 119 / 123 / 111 / 127 events. Subscription start dates follow the same even pattern.
- Taken together, these produce the trend mechanically. Every account gets about one event whatever its age. A new account's event therefore falls into a short window, and new accounts are concentrated in late 2024. So the event rate *per account per period* has to climb over time, even though no customer is any more likely to leave.
- **Churn events don't remove anyone.** Of the 352 accounts with a churn event, 277 (79%) are still marked active in `accounts.csv`, and only 61 events are marked as reactivations. Accounts with `churn_flag = True` still hold about 9 open subscriptions on average, the same as active accounts. Only 47 of the 600 churn events fall within 7 days of a subscription ending on the same account.

### The measure that does not have this problem

`accounts.csv` has a single churn flag per account. Here is the share flagged as churned, by signup quarter:

| Signup quarter | 23Q1 | 23Q2 | 23Q3 | 23Q4 | 24Q1 | 24Q2 | 24Q3 | 24Q4 |
|---|---|---|---|---|---|---|---|---|
| Churned (`churn_flag`) | 29% | 24% | 21% | 28% | 20% | 23% | 19% | 15% |

Older cohorts have had more time to churn, so slightly higher rates for them are expected. Nothing here suggests that newer customers churn faster. Overall, 110 of 500 accounts (22%) are flagged as churned.

**Conclusion (moderate confidence):** the claim of deteriorating retention isn't supported. The rising counts come from customer growth plus an artifact of how events are dated. I can't prove the opposite, that retention is stable, because the flag has no churn date, so a monthly churn rate can't be built from it.

## 2. What is driving churn?

I tested each candidate driver against two outcomes: (a) `churn_flag`, and (b) having a churn event within 90 days of signup, compared across cohorts with equal tenure. I also tested subscription-level early termination. For each, I compared raw rates and fitted a logistic regression that controls for signup date and the other attributes.

### Account attributes: no meaningful differences

| Attribute | Range of churn-flag rate across groups | Test |
|---|---|---|
| Plan tier (Basic / Pro / Enterprise) | 22% / 22% / 22% | p = 1.00 |
| Trial vs paid | 26% vs 21% | p = 0.39 |
| Country (7) | 13%–32% (small groups) | p = 0.66 |
| Referral source (5) | 15% (partner) – 30% (event) | p = 0.08, not significant in regression |
| Seats (quartiles) | 19%–25% | n.s. |
| Industry | DevTools 31% vs 16–22% for others | overall p = 0.07; DevTools vs Cybersecurity p = 0.02 in regression |

DevTools is the only lead. But it is one of more than 30 comparisons I ran, it isn't significant overall, and it doesn't hold up on the churn-event measure, where DevTools is no worse than average (35% vs 22–40%). I treat it as a hypothesis to watch, not a finding.

### Behavioural signals: churned and retained accounts look the same

| Average per account | Churned | Retained |
|---|---|---|
| Support tickets | 3.9 | 4.0 |
| Escalations | 0.22 | 0.18 |
| Satisfaction score (1–5) | 4.00 | 3.95 |
| Resolution time (hours) | 35.5 | 36.5 |
| First response (minutes) | 85 | 90 |
| Feature usage count | 522 | 495 |
| Errors per use | 5.4% | 5.7% |
| Share of beta-feature usage | 10.2% | 10.2% |
| Share of annual billing | 49% | 49% |
| Share auto-renew | 80% | 80% |

None of these differences is statistically significant in the regression. Escalations come closest (p = 0.08). At the subscription level, plan tier, billing frequency, auto-renew, trial status, upgrades, downgrades and seat count don't predict early termination either (all p > 0.2).

### Stated churn reasons: no dominant reason

Across 600 churn events: features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%. The mix barely changes between 2023 and 2024. The free-text feedback is unrelated to the reason code: "too expensive" appears just as often under `features` or `support` as under `pricing`. So the reason codes can't be used to target a response either.

## 3. Data quality problems (these limit everything above)

| Issue | Evidence |
|---|---|
| Three churn definitions that disagree | `accounts.churn_flag` (110 accounts), `churn_events` (352 accounts, 600 events), `subscriptions.churn_flag` (486 subscriptions). 277 accounts with churn events are flagged active; 35 flagged-churned accounts have no churn event. Flagged-churned accounts still have about 9 open subscriptions. |
| Churn events not linked to subscriptions | Only 47 of 600 events fall within 7 days of a subscription ending on that account. |
| Event dates look synthetic or backfilled | Events per account don't depend on tenure; dates are spread evenly across each account's lifetime. |
| Usage outside the subscription it belongs to | 19,142 of 25,000 usage records (77%) are dated before their subscription started; 290 are dated after it ended. 21 usage IDs are duplicated. |
| Support tickets before the customer existed | 1,077 of 2,000 tickets (54%) are dated before the account's signup date. |
| Missing satisfaction scores | 41% of tickets have no satisfaction score. |

Because usage and support records don't line up in time with the accounts and subscriptions they belong to, I couldn't run "what happened in the 90 days before churn" analyses. Those are the analyses most likely to find real leading indicators.

## 4. Recommendations

1. **Don't fund a broad retention programme (pricing changes, support overhaul, feature push) on this data.** None of these levers shows any link to churn, and the deterioration it would respond to hasn't been shown.
2. **Fix churn measurement first (small, quick investment):**
   - Agree on one churn definition. I suggest: an account churns when its last paid subscription ends without renewal within N days. Also track revenue churn (lost MRR) separately from logo churn.
   - Link each churn event to the subscription(s) that ended, and record the real cancellation date.
   - Audit the date fields in the usage and support pipelines: why does usage predate subscriptions, and why do tickets predate signup? Remove duplicate usage IDs.
   - Make the cancellation reason a required single choice at cancellation, captured together with the free text, so the two can't contradict each other.
3. **Then re-run the analysis** on a monthly churn rate (churned ÷ active at start of month) and do a "90 days before churn" comparison of usage, errors and support. That will show whether retention is changing and what precedes churn.
4. **Low-cost hypotheses to track meanwhile:** the higher churn flag in DevTools (31% vs 22% overall) and escalated support tickets (weak signal). Check both in the corrected data before acting on them.

## Assumptions and method notes

- The extract is assumed to end on 31 Dec 2024, the latest date in every file. Cohort comparisons only include accounts or subscriptions with a full observation window (for example, 90 days after signup).
- "Active base" for a quarter means accounts that had signed up by the end of that quarter. Churn events don't remove accounts in this data, so I couldn't build a cleaner base.
- Behavioural aggregates (tickets, usage) are lifetime totals per account. Because of the date problems above, they can't be restricted to the period before churn.
- Tests are chi-square tests for group rates and logistic regressions with signup-date controls. With 500 accounts and more than 30 comparisons, some p-values below 0.05 are expected by chance, and I've interpreted them that way.
