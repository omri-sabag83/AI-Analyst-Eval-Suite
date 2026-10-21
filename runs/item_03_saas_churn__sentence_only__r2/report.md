# Customer churn drivers: assessment for leadership

## Bottom line

1. **The data does not show that retention has deteriorated.** Raw churn counts rose sharply in 2024 (churn events went from 6 in Q1 2023 to 251 in Q4 2024). That rise comes from a growing customer base and from how the extract is built. Once churn is measured per account, cohort by cohort, it is flat or slightly better in 2024.
2. **No variable in these extracts reliably explains churn.** Plan tier, seats, billing terms, trial status, support experience, product usage and errors all look the same for churned and retained customers. Models built on every available variable predict churn no better than a coin flip (cross-validated AUC 0.47–0.54).
3. **The churn data is inconsistent enough that it cannot be used to make funding decisions as it stands.** The three systems disagree about who has churned. The recorded churn reasons don't match the customers' own feedback.

**Recommendation:** don't fund a large churn-reduction programme based on "retention has deteriorated". The evidence doesn't support that claim, and we can't yet tell what such a programme should target. Spend first, and modestly, on fixing churn measurement. Then run small, targeted tests (details below).

---

## 1. Has retention deteriorated?

### What the headline numbers show (and why they mislead)

| Quarter | New accounts | New subscriptions | Subscriptions ended | Churn events |
|---|---|---|---|---|
| 2023 Q1 | 55 | 31 | 0 | 6 |
| 2023 Q3 | 53 | 203 | 2 | 19 |
| 2024 Q1 | 56 | 472 | 27 | 54 |
| 2024 Q3 | 72 | 1,107 | 80 | 130 |
| 2024 Q4 | 80 | 2,069 | 324 | 251 |

Churn counts grew about 40-fold, but the base at risk grew just as fast. New subscriptions grew about 65-fold, and the account base grew from 55 to 500. A rising count of churn events is what a growing business looks like, not proof of worse retention.

### Measured per account, by signup cohort

| Signup cohort | Accounts | `churn_flag` rate | Share with any churn event | Churn events per account |
|---|---|---|---|---|
| 2023 Q1 | 55 | 29% | 73% | 1.16 |
| 2023 Q2 | 54 | 24% | 57% | 1.06 |
| 2023 Q3 | 53 | 21% | 75% | 1.38 |
| 2023 Q4 | 65 | 28% | 80% | 1.28 |
| 2024 Q1 | 56 | 20% | 70% | 1.25 |
| 2024 Q2 | 65 | 23% | 72% | 1.22 |
| 2024 Q3 | 72 | 19% | 68% | 1.18 |
| 2024 Q4 | 80 | 15% | 68% | 1.11 |

- Account-level churn (`churn_flag`): **25.6% for 2023 signups vs 19.0% for 2024 signups.** Newer cohorts have had less time to churn, so this comparison favours 2024 somewhat, but it shows no worsening.
- About 70% of accounts in every cohort have at least one churn event, with roughly 1.1–1.4 events per account. Cohort makes no difference.

### Why a naive tenure analysis would wrongly show deterioration

Each churn event happens at some point between the account's signup and the end of the extract (31 Dec 2024). Where in that window it falls looks statistically random: the timing is uniform, with KS test p = 0.92. Accounts that signed up in 2024 have a short window, so all of their churn events are squeezed into a few months.

That makes a metric like "churned within 180 days of signup" look much worse for 2024 (57–68% vs 17–45% for 2023). This is an artefact of the shorter window, not a change in customer behaviour. Subscription start dates follow the same pattern.

### Subscription-level churn rate

Of the subscriptions active at the start of each quarter, the share that ended during that quarter was steady at about 2.8–3.6% from Q4 2023 to Q3 2024. It then rose to 4.2% in Q4 2024.

Part of the Q4 2024 jump looks like an artefact of the extract boundary:
- The subscriptions that started in Q4 2024 and have already ended have a median life of 11 days.
- 24 subscriptions end on exactly 31 Dec 2024.

**Treat Q4 2024 as something to watch, not as evidence of a trend.** Re-check it once Q1 2025 data exists.

---

## 2. What is driving churn?

I tested each available attribute against two outcomes: account `churn_flag`, and "has any churn event". I also used subscription-level churn per subscription-year of exposure.

| Factor | Finding |
|---|---|
| Plan tier | 22.0% / 22.1% / 21.9% (Basic / Enterprise / Pro). No difference. |
| Trial vs paid, billing frequency, auto-renew | No difference (subscription-level rates 0.21–0.23 per year for all of them). |
| Upgrades / downgrades | Small differences in the expected direction (0.18 vs 0.26 per subscription-year), not significant (p = 0.15 and 0.36). |
| Seats, MRR | No difference. |
| Support tickets (volume, resolution time, first response, CSAT, escalations) | No difference. In the 90 days before a churn event, accounts filed 0.52 tickets, against a baseline of 0.49. Pre-churn CSAT was 4.08 vs 3.98 overall. |
| Product usage (volume, duration, features used, error rate, beta usage) | Identical for churned and retained subscriptions (e.g. 10.03 vs 10.02 uses per record, 0.57 vs 0.56 errors). |
| Country, referral source | Not significant (p = 0.66 and 0.08). |
| **Industry** | DevTools has a 31% `churn_flag` rate vs 16–22% for other industries (Fisher p = 0.014; still significant after adjusting for tenure, plan and usage). **However, this is weak evidence:** see below. |

Why I don't treat DevTools as a confirmed driver:
- Roughly 30 comparisons were run, so one p ≈ 0.01 result is about what chance alone would produce. It does not pass a multiple-testing correction.
- It doesn't hold on the other churn measures. 73.5% of DevTools accounts have a churn event, against about 69% for the rest. At subscription level, DevTools churns at 0.23 per subscription-year, which is within the range of the other industries (Cybersecurity is highest at 0.25).

Multivariate check: random-forest and logistic models using every attribute above reach a cross-validated AUC of 0.47–0.54. In other words, **the available data has essentially no power to predict who churns.**

### Recorded churn reasons

- The reason codes are spread almost evenly: features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%.
- The mix did not change between 2023 and 2024 (χ² p = 0.48).
- **The reason codes don't match the customers' feedback text.** For example, churns coded "pricing" are just as likely to say "missing features" or "switched to competitor" as "too expensive", and the same holds for every code.

So the reason field cannot currently be used to decide where to invest (pricing vs product vs support).

---

## 3. Data quality problems that block a reliable answer

1. **The three churn definitions disagree.**
   - 110 accounts have `churn_flag = True`, but only 75 of them have a churn event.
   - 277 of the 390 "non-churned" accounts do have churn events.
   - Every account, including all 110 flagged as churned, still has at least one open subscription.
2. **The reason codes and the feedback text are unrelated** (see above).
3. **Usage records are mostly not tied to live subscriptions.** 78% of usage records fall outside the start and end dates of the subscription they belong to.
4. **The extract ends at 31 Dec 2024**, so the most recent cohorts and quarters are incomplete.

These problems likely explain why no driver stands out. If churn labels are partly noise, real drivers get washed out.

---

## 4. Recommendations

1. **Don't fund a broad retention programme on the premise that retention has deteriorated.** The per-account, cohort-adjusted measures don't show it. The counts behind the concern are inflated by growth.
2. **First, fund a small fix to churn measurement (weeks, not quarters):**
   - Agree one definition of churn, for example "account has no active paid subscription for 30+ days", and make the CRM flag, billing and the churn-event log all follow it.
   - Make the churn reason a required, validated field at cancellation, and audit it against the feedback text.
   - Fix the link between usage records and subscriptions.
3. **Report retention as rates by cohort, not counts:**
   - logo churn per account-month, broken out by signup cohort;
   - net and gross revenue retention.
   Re-check Q4 2024 when Q1 2025 data arrives.
4. **Run small, targeted tests instead of a broad programme:**
   - Interview churned DevTools customers to confirm or rule out the industry signal.
   - Gather structured exit feedback from a sample of churned accounts. At present we cannot tell whether pricing, features or competitors matter most.
5. **Revisit funding in about 1–2 quarters**, once churn is measured cleanly. If a real driver shows up then, it can be funded with confidence.

## Assumptions and limitations

- The analysis covers only the five extracts (500 accounts, 2023–2024). There is no data after 31 Dec 2024.
- Main account-level churn outcome: `churn_flag`. Cross-checks: having any churn event, and subscription `churn_flag` / `end_date` (which agree perfectly with each other). Conclusions held on all three.
- I treated subscriptions with no `end_date` as active through 31 Dec 2024.
- With 110 churned accounts, the analysis could reliably detect only moderate or large effects. Small effects can't be ruled out.
