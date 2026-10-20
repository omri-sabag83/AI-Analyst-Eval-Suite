# Customer churn drivers: assessment for leadership

## Bottom line

1. **Retention did not decline steadily over two years.** Once the rate is adjusted for the size of the customer base, churn was flat from 2023 through about July 2024. **A real deterioration started in late Q3 2024 and accelerated in Q4 2024.** The rise in raw churn counts before that point came almost entirely from the fact that the business grew about 15-fold.
2. **The Q4 2024 deterioration is concentrated in brand-new subscriptions.** Established subscriptions (3+ months old) churn at about 1% per month, and that rate has not changed. The share of new subscriptions cancelled within 30 days rose from about 0.5% (Feb–Jul 2024) to 3.4% (Sep–Oct) and 7.7% (Nov).
3. **No customer attribute explains the churn.** Plan tier, billing frequency, auto-renew, trial status, seats, industry, country, acquisition channel, support experience and product usage/errors all have no meaningful link to churn. The early-life spike hits every segment about equally. That pattern points to something **systemic and recent**, such as a change in onboarding, provisioning, billing or pricing, or in how churn is recorded. It does not point to a particular customer type.
4. **The company's own churn records can't be used to answer "why".** The account churn flag, the churn-event log and the subscription data contradict each other. The recorded reason codes look like random labels. Funding a response aimed at a "top reason" from these records would not be justified by the evidence.

**Recommendation:** Don't fund a broad retention programme yet. Spend 2–4 weeks finding out what changed around Aug–Sep 2024 in the first 30 days of a subscription, and fix the churn data, before committing larger budgets. Details are in the recommendations section below.

---

## Data and assumptions

- 500 accounts, 5,000 subscriptions (about 10 per account), 600 churn events, 2,000 support tickets and 25,000 feature-usage rows, covering Jan 2023 – Dec 2024.
- **Assumptions:**
  - A subscription with an `end_date` (equivalently `churn_flag = True` in subscriptions; the two match exactly, 486 rows) has churned.
  - A missing `end_date` means the subscription was still active on 31 Dec 2024.
  - Rates are expressed **per subscription-month of exposure**, which avoids penalising periods with more customers.
- Basic integrity checks passed: no duplicate IDs (apart from 21 repeated usage IDs, which don't matter here), no subscriptions starting before account signup, and no end dates before start dates.

## 1. Has retention deteriorated?

**Raw counts are misleading.** Churn events rose from 6 in Q1 2023 to 251 in Q4 2024. Over the same period, the active subscription base grew from 31 to about 4,800 and active accounts from 21 to 500. Churn per active base is the right measure.

| Quarter | Subs active in quarter | Subs ended | Churn rate (subs) | MRR lost from opening base |
|---|---|---|---|---|
| 2023 Q4 | 662 | 14 | 2.1% | 7.3%* |
| 2024 Q1 | 1,120 | 27 | 2.4% | 2.0% |
| 2024 Q2 | 1,779 | 37 | 2.1% | 2.3% |
| 2024 Q3 | 2,849 | 80 | 2.8% | 2.2% |
| 2024 Q4 | 4,838 | 324 | **6.7%** | **5.1%** |

\*Small base; it is volatile.

Monthly subscription churn was 0.7–0.9% from Feb to Jul 2024. It then rose to 1.2% (Aug–Sep), 1.8–1.9% (Oct–Nov) and 4.1% (Dec).

A Poisson rate model controls for subscription age, plan, billing, auto-renew, trial, upgrade/downgrade, industry, channel and seats. Relative to H1 2024, the churn rate was:
- **2023:** 0.6× (not significantly different)
- **2024 Q3:** 1.3× (borderline, p≈0.10)
- **Oct–Nov 2024:** **2.2×** (95% CI 1.7–3.0)
- **Dec 2024:** **4.9×** (95% CI 3.7–6.5)

**So the deterioration is real but recent (roughly the last 4–5 months). It is not a two-year trend.**

## 2. Where the deterioration is happening

Churn rate per 100 subscription-months, by subscription age:

| Subscription age | 2023 | 2024 H1 | 2024 Q3 | Oct–Nov 2024 | Dec 2024 |
|---|---|---|---|---|---|
| < 1 month | 0.5 | 0.9 | 1.7 | **4.1** | **14.1** |
| 1–2 months | 0.9 | 1.1 | 1.4 | 2.3 | 2.7 |
| 3–5 months | 0.8 | 0.8 | 1.2 | 1.1 | 1.3 |
| 6–11 months | 0.9 | 0.9 | 0.5 | 1.3 | 0.8 |
| 12+ months | – | 0.9 | 0.8 | 0.6 | 1.2 |

The age mix of the base barely changed (about 22–25% of exposure is in the first month in every 2024 period), so this is not a mix effect. **Mature subscriptions are as sticky as ever. The problem is the first 30–60 days.**

Share of new subscriptions cancelled within 30 days, by start month:

| Started | Jan–Jul 2024 | Aug | Sep | Oct | Nov |
|---|---|---|---|---|---|
| Cancelled ≤30 days | 0–2% | 2.4% | 3.4% | 3.4% | **7.7%** |

**The December figure should be read with caution.**
- 61 of the 193 December cancellations are dated 29–31 Dec, the last three days of the extract.
- 103 churned subscriptions both started and ended in December.

This clustering at the data cut-off may be partly a year-end process or extraction artifact, such as bulk closures or contract clean-up. Even without December, Oct–Nov churn is more than double the H1 2024 rate.

**Customers are not leaving the company outright.** Every one of the 500 accounts still had at least one active subscription on 31 Dec 2024. 94% of subscription cancellations happened while the same account had another active subscription. The loss is mostly **contraction** (dropped subscriptions or products within retained accounts), not logo loss. This matters for the response: it is about protecting revenue within accounts, not winning back lost logos.

## 3. What is driving churn? Candidate drivers tested

I tested every available attribute at two levels:
- **Subscription level:** the Poisson model above.
- **Account level:** the `churn_flag` field, using logistic regression and a random-forest model.

| Candidate driver | Finding |
|---|---|
| Plan tier (Basic/Pro/Enterprise) | No effect (churn 9.5% / 10.0% / 9.7%; IRR ≈1.0, p>0.6) |
| Billing frequency, auto-renew | No effect (p>0.3) |
| Trial vs paid | No effect (10.0% vs 9.7%) |
| Upgrades / downgrades | No significant effect (downgrade IRR 1.2, p=0.35) |
| Seats / company size | No effect |
| Industry | Not significant once other factors are controlled for (subscription level). DevTools accounts are flagged churned more often (31% vs 16–22%), but overall p=0.07 across 5 industries. Treat this as a weak lead, not a finding. |
| Acquisition channel | Not significant (p=0.08 overall; p>0.3 in the controlled model) |
| Country | Not significant (p=0.66) |
| Support: ticket volume, CSAT, escalations, resolution and response times | No meaningful difference between churned and retained accounts (CSAT 4.00 vs 3.95; resolution 35 h vs 36 h) |
| Product usage, error rate, beta-feature use | No meaningful difference. Usage volume per subscription is nearly identical in every period (about 5 records per subscription), so this data carries little signal. |

Overall, the account-level model has no predictive power. Its cross-validated AUC is 0.49, which is no better than a coin flip. Taken together, the logistic model is not significant (p=0.10). **None of the attributes in these extracts distinguish churners from non-churners.** The early-life spike in Sep–Nov 2024 is spread evenly across all tiers, industries, channels, countries and billing types (every test p>0.17).

## 4. Why the churn records can't be used to find the cause

- **The three churn sources disagree.**
  - 110 accounts are flagged `churn_flag = True`, yet all 110 still have active subscriptions.
  - 277 accounts that are *not* flagged have churn events, and 35 flagged accounts have none.
  - Only 8% of the 600 churn events fall within 7 days of a subscription end date, and 36% belong to accounts with no ended subscription at all.
- **Reason codes look random.**
  - The six reason codes (features, support, budget, pricing, competitor, unknown) each account for 15–19% of events, and the mix doesn't shift over time.
  - The free-text feedback ("too expensive", "missing features", "switched to competitor") is spread evenly across every reason code. For example, events coded "support" are as likely to say "too expensive" as anything else.
  - In practice, these fields are not being captured in a meaningful way.
- **Cohorts aren't getting worse.** By the account churn flag, newer signup cohorts show *lower* flagged churn (15–23% for 2024 cohorts vs 21–29% for 2023), as expected from shorter exposure. There is no sign that recently acquired customers are worse quality.

## Recommendations

1. **Investigate the first-30-day problem now. This is where the money is leaking.**
   - Find out what changed operationally from about Aug 2024: onboarding flow, provisioning, a pricing or packaging change, billing or invoicing processes, a sales compensation change that encourages short-lived add-on subscriptions, or CRM/subscription-system changes.
   - Interview account owners for a sample of the roughly 200 subscriptions started Sep–Nov 2024 and cancelled within 30 days.
   - Because no customer segment is driving the rise, look for an internal process cause first.
2. **Check whether the December spike is real** before reporting it upward. Confirm with billing/RevOps why 61 cancellations are dated 29–31 Dec and 103 subscriptions opened and closed within December, which could reflect year-end clean-up or contract consolidation.
3. **Reframe the metric.** Churn here is mainly subscription contraction inside retained accounts, not lost customers. Report **gross and net revenue retention** and **logo churn** separately, both per active base. Stop reporting raw churn counts, which rise automatically with growth.
4. **Fix churn data capture before funding reason-specific programmes.**
   - Reconcile `accounts.churn_flag`, `churn_events` and subscription end dates into one definition.
   - Make reason codes mandatory and validated, with a single primary reason consistent with the free-text feedback.
   - Without this, no pricing, support or feature investment can be justified from the data.
5. **Hold off on broad, expensive responses for now.** The data does not support a large pricing, support or product programme aimed at a specific segment. Pricing changes, support headcount and Enterprise-focused retention teams all lack supporting evidence here. Mature-customer retention is stable. A targeted onboarding and early-life health check (an outreach at days 7 and 21 for every new subscription) is a low-cost hedge while the root cause is found.
6. **Re-run this analysis after Q1 2025** with clean churn definitions. That will show whether the Q4 2024 rise persists beyond the year-end period.

## Limitations

- The extract ends on 31 Dec 2024. Recent subscriptions have short observation windows, and the year-end clustering may distort Q4.
- Usage, support and account attributes show almost no variation linked to churn. Real drivers may sit in data not provided, such as contract terms, sales-rep changes, pricing history or NPS.
- The account churn flag and the churn events have unclear definitions. My conclusions about trend and timing rest on subscription start and end dates, which are internally consistent.
