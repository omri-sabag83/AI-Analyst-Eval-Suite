# Customer churn drivers: findings and recommendations

## Summary

1. **Retention has not been getting steadily worse for two years.** The jump in churn *counts* (from 6 recorded churn events in Q1 2023 to 251 in Q4 2024) mostly reflects growth: there were about 30 open subscriptions in mid-2023 and about 2,800 by Q4 2024. Measured as a **rate**, subscription churn held at roughly **0.8–1.0% per month** from 2023 through mid-2024.
2. **Something did change in the second half of 2024, and it affects new subscriptions only.** Among subscriptions started in Jul–Nov 2024, **4.1% ended within 30 days**. The figure was **0.5–0.75%** for subscriptions started in 2023 or H1 2024, so the rate is about 6–8× higher. Subscriptions older than 6 months churn at the same rate as before (about 0.7–0.9% per month). The overall rate went to about 1.6% per month in Jul–Nov 2024 and **4.5% in December 2024**.
3. **No customer segment explains it.** The early-churn jump is about the same size in every plan tier, billing frequency, auto-renew setting, trial status, industry, country and acquisition channel (joint test p = 0.84). Across the whole history, none of these attributes, nor the support-ticket metrics, is a meaningful churn driver either. The timing points to a cause that hit every new subscription at once, such as onboarding, provisioning or billing, a pricing or packaging change, a product release, or a change in how subscriptions are recorded. The data cannot tell these apart.
4. **The usual "why" data cannot be trusted as it stands.** Churn reason codes are spread almost evenly across six categories and are statistically unrelated to the customer's own feedback text (p = 0.99). The three churn flags in the data disagree with each other. 78% of feature-usage records fall outside the window of the subscription they belong to.
5. **This is subscription churn, not lost customers.** All 500 accounts still have at least one open subscription at the end of 2024, including every account with a recorded churn event. So customers are cutting back (contraction), not leaving. It still costs money: about **$0.87M of MRR ended in Q4 2024**, against about $6.0M open at the start of the quarter.

**Recommendation:** Don't fund a broad retention programme aimed at a particular segment, pricing or support. The evidence does not support one. Instead, (a) quickly diagnose what changed for new subscriptions around July 2024, starting with the first 30 days, (b) fix the churn data so that future "why" questions can be answered, and (c) re-measure before committing larger funding.

---

## Data and definitions

The data covers 2023-01-01 to 2024-12-31: 500 accounts, 5,000 subscriptions, 600 churn events, 2,000 support tickets and 25,000 feature-usage rows. I found no duplicate keys, except for 21 duplicate `usage_id`s, which I dropped.

**Which "churn"?** The extracts contain three churn signals, and they disagree:

| Signal | Count | Consistency |
|---|---|---|
| `accounts.churn_flag` | 110 accounts (22%) | Independent of the other two. 35 flagged accounts have no churn event, and 277 accounts with churn events are *not* flagged. All 110 flagged accounts still have open subscriptions. |
| `churn_events` | 600 events on 352 accounts | All 352 accounts still have open subscriptions. 10% of events are marked as reactivations. |
| `subscriptions.end_date` / `churn_flag` | 486 subscriptions ended (on 312 accounts) | Internally consistent: `churn_flag` is True exactly when `end_date` is filled. |

**Assumption:** I used **subscription ends** as the primary churn measure. It is the only one that is internally consistent and has an exposure base to divide by. All rates are per subscription-month at risk, so a fast-growing base does not inflate them. I use the account flag and the churn events only as secondary checks.

## 1. Has retention deteriorated?

**Counts vs rates**

| Quarter | Open subs at quarter start | Subs ended in quarter | Quarterly churn rate | Churn events (count) |
|---|---|---|---|---|
| 2023 Q3 | 135 | 1 | 0.7% | 19 |
| 2023 Q4 | 336 | 12 | 3.6% | 37 |
| 2024 Q1 | 648 | 19 | 2.9% | 54 |
| 2024 Q2 | 1,093 | 31 | 2.8% | 92 |
| 2024 Q3 | 1,742 | 51 | 2.9% | 130 |
| 2024 Q4 | 2,769 | 116 | 4.2% | 251 |

Measured on subscriptions open at the start of each quarter, the quarterly rate was flat at about 3% until Q4 2024. Counts rose about 10× because the base did too.

**An exposure-based monthly rate, split by subscription age, shows where the change is.** These are subscription ends per 100 subscription-months.

| Tenure | 2023 | 2024 H1 | 2024 Jul–Nov | 2024 Dec |
|---|---|---|---|---|
| First month | 0.45 | 0.87 | **2.97** | **13.9** |
| 1–3 months | 0.92 | 1.14 | 1.77 | 2.82 |
| 3–6 months | 0.82 | 0.87 | 1.15 | 1.16 |
| 6–12 months | 0.96 | 0.84 | 0.90 | 0.80 |
| 12+ months | – | 1.07 | 0.72 | 1.21 |

I also fitted a Poisson model of churn with an exposure offset, controlling for tenure. Relative to H1 2024, churn was 1.8× higher in Jul–Nov 2024 (95% CI 1.35–2.36) and 4.9× higher in December 2024 (95% CI 3.7–6.5). 2023 was not significantly different from H1 2024 (RR 0.63, p = 0.09).

Early-life cohort check, using the share of new subscriptions that ended within 30 days. Every cohort has a full 30 days of follow-up.
- Started in 2023: 0.75% (666 subs)
- Started Jan–May 2024: 0.55% (910 subs)
- Started Jul–Nov 2024: **4.1%** (2,223 subs)

**Conclusion:** Leadership's belief is only partly right. There was no gradual two-year decline. Instead, a new problem appeared in H2 2024, concentrated in the first weeks of new subscriptions, and it got sharply worse in December.

**Caveats on December:** 61 of December's 193 ends fall on 29–31 December, the last three days of the extract. That could be real year-end cancellations or a period-end or extract-cutoff artefact. Even without those three days, December would still be about 3% per month. The H2 rise is also visible in Aug–Nov (1.2–2.1% per month), so it does not depend on December.

## 2. What is driving churn?

**I found no segment or account attribute that drives churn.** I fitted a Poisson model of subscription ends with an exposure offset on all 5,000 subscriptions. It included plan tier, billing frequency, auto-renew, trial, upgrade and downgrade flags, seats, industry, country, referral source, ticket volume, resolution time and first-response time. Every rate ratio for plan, billing, auto-renew, trial and seats lies between 0.92 and 1.12, and none is significant. Raw rates per 100 subscription-months are similar across groups:
- Basic 1.71, Pro 1.80, Enterprise 1.90
- Monthly 1.74, annual 1.87
- Auto-renew on 1.81, off 1.79
- Trial 1.82, non-trial 1.80

A few coefficients reached p < 0.05: India churns less (RR 0.53), and first-response time has a tiny effect. With about 25 coefficients tested, a few chance hits are expected, so I don't treat these as findings.

- **Account-level check:** a logistic model of `accounts.churn_flag` on the same attributes plus tenure is not significant overall (likelihood-ratio p = 0.18). Churn rates are 22% on every plan tier.
- **The H2 2024 early-churn jump is uniform.** Within the Jul–Nov 2024 cohort, 30-day churn is 3.5–4.6% across plan tiers, 3.9–4.4% across billing types, 3.6% for trials vs 4.2% for paid, and 2.9–5.3% across channels. Joint test p = 0.84. Whatever changed hit every new subscription at once.
- **Support experience** (ticket count, resolution time, first-response time, CSAT, escalations) shows no consistent relationship with churn. Rates are flat across quartiles.
- **Upgrades and downgrades:** subscriptions with a downgrade flag churn somewhat more (2.13 vs 1.79) and upgraded ones somewhat less (1.48 vs 1.84). Neither difference is significant (p = 0.34 and p = 0.10). The direction is plausible but the signal is weak.

**Stated reasons can't be used.** In the churn events, the reason codes are features 19%, support 17%, budget 17%, unknown 16%, competitor 15% and pricing 15%. That is close to an even split. They are also independent of the customer's own feedback text: a chi-square test of reason code against feedback gives p = 0.99. For example, "too expensive" appears just as often under "features" as under "pricing". The reason mix has not changed over time either (p = 0.66). So these fields say nothing reliable about why customers leave, and **pricing, support or competition should not be named as the driver on this basis.**

**Product usage could not be assessed.** 78% of feature-usage rows are dated outside the start/end window of the subscription they are linked to. The link between usage and subscriptions looks broken, so I did not use usage as a driver. Measured naively, "usage per day" correlates strongly with churn, but that is an artefact: short-lived subscriptions have a small denominator.

## 3. Recommendations

1. **Investigate the new-subscription experience from July 2024 onward (highest priority, low cost).** Build a list of everything that changed around June–August 2024: onboarding flow, provisioning, billing or invoicing system, pricing or packaging, sales incentives, product releases, and subscription-recording logic. Then pull a sample of the 280 subscriptions that ended within 90 days of starting in H2 2024 and check what actually happened to each one.
   - Was it cancelled?
   - Was it replaced by another subscription on the same account?
   - Was it a billing failure?

   About 57% of Q4 ends have another subscription starting on the same account within ±7 days. However, new subscriptions start so often that this is roughly what chance would produce, so the data cannot confirm whether these are re-plans. Because no account has fully churned, *some* of this may be re-plans being recorded as churn.
2. **Check the December spike before reacting to it.** Confirm with the billing or data owner whether the ends on 29–31 December are real cancellations or a year-end or extract artefact.
3. **Fix churn instrumentation before funding a large retention programme.**
   - Agree on one churn definition: logo churn vs contraction, and how reactivations and re-plans are handled.
   - Reconcile `accounts.churn_flag`, `churn_events` and subscription ends.
   - Make reason codes mandatory and validated against the customer's feedback text.
   - Repair the link between feature usage and subscriptions so that usage can be tested as a leading indicator.
4. **Don't fund targeted fixes for a specific segment, a pricing cut, or a support overhaul on this evidence.** None of them is associated with churn in this data.
5. **Track the right KPI going forward:** monthly churn per 100 subscription-months (or MRR-weighted), split by tenure band, with first-30-day churn of new subscriptions as an early-warning metric. Raw churn-event counts will keep rising with growth even when retention is healthy.

## Limitations

- 2023 has few churn observations (18 subscription ends), so early rates are imprecise.
- The extract ends on 31 Dec 2024, so recent cohorts have short follow-up. I handled this by using exposure-based rates and complete 30-day windows.
- The patterns described are associations, not proven causes. The H2 2024 shift is clear in the data, but what caused it is a hypothesis to test with the operational checks in recommendation 1.
- Some features of the data (uniform reason codes, usage dated outside its subscription) suggest data-generation or extraction problems. All findings should be re-validated on a corrected extract.
