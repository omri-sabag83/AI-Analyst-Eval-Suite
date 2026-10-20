# Customer Churn: Has Retention Deteriorated, and What Is Driving It?

*Data: accounts (500), subscriptions (5,000), feature usage (25,000 rows), support tickets (2,000), churn events (600), covering Jan 2023 – Dec 2024.*

## Bottom line

1. **Yes, retention appears to have deteriorated, sharply in H2 2024.** This holds after adjusting for the growing customer base. Both the churn-event log and the subscription end dates show it. However, the account-level `churn_flag` does not show it, and the three churn sources contradict each other, so **the size of the deterioration is uncertain**.
2. **The data does not identify a driver.** No customer attribute, plan, billing setting, usage measure or support measure separates churners from retained customers. Predictive models do no better than a coin flip. The rise in churn is **uniform across every segment**. That points to a company-wide cause that these extracts don't capture, or to a change in how churn is recorded.
3. **Recorded churn reasons are not usable for targeting.** They are spread almost evenly across six codes, and the mix did not change between 2023 and 2024. The free-text feedback is statistically independent of the reason code it sits next to.
4. **There are serious data-integrity problems**, for example usage dated before its subscription existed. These must be fixed before any driver analysis can be trusted.

**Recommendation:** do not fund a segment- or feature-targeted retention program on the basis of this data. Fund a short, cheap diagnostic phase: fix the churn data, find out what changed in 2024, and capture reliable churn reasons. Alongside it, run a controlled early-life (first-90-day) retention pilot, because that is where the deterioration is most visible. Details below.

---

## 1. Has retention deteriorated?

Raw churn-event counts rose from 73 in 2023 to 527 in 2024. Much of that is simply a bigger customer base (accounts grew from 55 to 500), so I normalised by exposure and also looked at signup cohorts.

**Exposure-adjusted churn events, per 100 accounts per month**

| Quarter | Accounts | Churn events | Events /100 acct-months | Subscription ends /100 sub-months |
|---|---|---|---|---|
| 2023 Q1 | 55 | 6 | 7.9 | 0.0 |
| 2023 Q2 | 109 | 11 | 4.3 | 0.8 |
| 2023 Q3 | 162 | 19 | 4.7 | 0.3 |
| 2023 Q4 | 227 | 37 | 6.3 | 1.0 |
| 2024 Q1 | 283 | 54 | 7.2 | 1.1 |
| 2024 Q2 | 348 | 92 | 9.7 | 0.9 |
| 2024 Q3 | 420 | 130 | 11.2 | 1.2 |
| 2024 Q4 | 500 | 251 | **17.9** | **3.0** |

(2023 Q1 is based on only 6 events.)

**Cohort view: share of new accounts with a churn event within 90 days of signup**

| Signup cohort | Accounts | Churned within 90 days |
|---|---|---|
| 2023 H1 | 109 | 16% |
| 2023 H2 | 118 | 23% |
| 2024 H1 | 121 | 39% |
| 2024 H2 (signed up by Oct 2) | 74 | 61% |

(Chi-square p < 0.001. The 180-day view shows the same pattern: 27% → 40% → 62%.) The subscription data agrees more mildly: the share of subscriptions ending within 90 days rose from about 2–3% for 2023–H1 2024 starts to 6.5% for Q3 2024 starts.

**Caveats on the size of the decline:**
- The account-level `churn_flag` shows *no* deterioration: 25.5% of 2023 signups are flagged, versus 19.0% of 2024 signups, which is what you would expect from shorter exposure alone.
- The three churn definitions disagree heavily. 277 of the 390 accounts flagged "not churned" have at least one churn event. 35 of the 110 flagged "churned" have none. Of the 600 events, 61 are marked as reactivations, and 175 accounts have several events.
- Events pile up at the end of the extract: December 2024 alone has 117 churn events and 193 subscription ends. Subscription *starts* per account also climb steeply (0.6 per account in Q1 2023 to 4.1 in Q4 2024). This looks like a change in how subscriptions and events are generated or recorded, not purely customer behaviour.
- At 17.9 events per 100 accounts per month, the event log implies very high churn for a base that is still growing and adding subscriptions. "Churn event" probably includes partial or subscription-level cancellations, not only lost customers.

**Conclusion:** the direction is consistent: churn activity rose in 2024, especially among new customers and in Q4. But the data does not support a reliable estimate of how much revenue or how many logos were actually lost.

## 2. What is driving churn?

I tested every available attribute against three outcomes: account `churn_flag`, "account has any churn event", and subscription-level churn (exposure-adjusted, Poisson model with an offset for days active).

**No meaningful driver was found.**

| Factor tested | Result |
|---|---|
| Plan tier | Basic 22.0%, Pro 21.9%, Enterprise 22.1% flagged (p = 0.999). Same at subscription level. |
| Industry | Range 16–31% flagged (DevTools highest), p = 0.07. Not significant, not replicated on churn events (p = 0.79) or subscriptions (p = 0.31). |
| Country, referral source, trial status, seats | All p > 0.07, with no consistent pattern across the three outcomes. |
| Billing frequency, auto-renew, upgrade/downgrade flags | Subscription churn rate ratios 0.88–1.12, all p > 0.4. |
| Product usage (volume, duration, features used, errors, beta share) | Churners and retained customers are indistinguishable (e.g. 49 vs 50 usage events per subscription, p = 0.53). |
| Support (ticket volume, resolution time, first response, CSAT, escalations, urgent share) | No differences (all p > 0.04 before any multiple-testing correction; CSAT 4.00 vs 3.95). Tickets in the 90 days before a churn event: 0.52, versus 0.51 for random comparison dates. |
| Multivariate models (random forest, 5-fold CV) | AUC 0.47 (churn_flag) and 0.52 (churn event), i.e. chance level. |

One apparent signal, high usage per month among churned subscriptions (rate ratio 3.7), is an **artefact**. Short-lived subscriptions have a tiny denominator, and most usage records are dated outside the subscription's active window (see section 4). I discarded it.

**The 2024 deterioration is uniform.** 90-day churn roughly doubled or tripled in *every* plan tier (Basic 13%→49%, Pro 23%→48%, Enterprise 21%→45%), every industry, every acquisition channel, and for trial and non-trial accounts alike. A problem caused by a specific product area, segment or support failure would show up unevenly. A uniform rise points to something company-wide: a pricing or packaging change, a competitive shift, a change in onboarding or sales qualification, or a change in how churn is logged.

## 3. What do customers say?

- Reason codes are almost evenly split: features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%.
- The mix did not change from 2023 to 2024 (p = 0.48), so reasons don't explain the increase.
- The feedback text ("too expensive", "missing features", "switched to competitor", blank) is **unrelated to the reason code**. For example, "too expensive" appears about equally often under *features*, *support* and *competitor* codes. At least one of these fields is not being captured meaningfully.
- Refunds are small (median $0, mean $14), so they are not a material cost driver.

Taken together, price/budget (32%), product gaps (19%) and competition (15%) are commonly cited. But the data quality means none of these can be ranked with confidence.

## 4. Data-integrity issues (must be fixed first)

| Issue | Scale |
|---|---|
| Usage records dated before the subscription started | 77% of usage rows (only 22% fall inside the subscription's active window) |
| Support tickets dated before the account signed up | 54% of tickets |
| Account `churn_flag` contradicts churn-event log | 312 of 500 accounts |
| Account `churn_flag` contradicts subscription churn | 278 of 500 accounts |
| Churn-event reason code unrelated to feedback text | All 452 events that have text |
| Duplicate records | 21 duplicate usage IDs; 1 duplicate churn event (same account and date) |
| End-of-period clustering | December 2024 holds 20% of all churn events and 40% of subscription ends |

Because the timestamps don't line up across tables, any "leading indicator" analysis (e.g. "usage drops before churn") cannot be done reliably today.

## 5. Recommendations

1. **Do not fund a targeted program yet.** Nothing in this data justifies prioritising a tier, industry, feature or support initiative. Spending on any of them now would be a guess.
2. **Fix the churn data (2–4 weeks, low cost).** Agree one definition of churn (logo vs. subscription vs. revenue), reconcile the three churn sources, and repair the date joins for usage and tickets. Re-run this analysis on the cleaned data. It is the cheapest way to find out whether a real driver is hidden in noise.
3. **Find out what changed company-wide in 2024, especially in H2.** The deterioration is uniform, so look at pricing or packaging changes, release history, sales targets and lead qualification, onboarding process changes, and any CRM or billing-system migrations. A system change could by itself create the Q4 spike.
4. **Fix how churn reasons are captured.** Use a mandatory, structured exit reason that is consistent with the free text, plus a sample of exit interviews. Right now leadership has no trustworthy "why".
5. **Pilot an early-life retention program, with a control group.** First-90-day churn is where the rise is clearest (16% → 39%+). An onboarding/customer-success touch for new accounts, randomised against a holdout, would produce causal evidence within one or two quarters. It would also limit spend until the cause is known.

## Assumptions and methods

- 2024-12-31 is treated as the end of the observation window. Open subscriptions and recent cohorts are right-censored, and cohort metrics only include accounts with the full follow-up period.
- "Retention deteriorated" was judged on exposure-adjusted rates and signup cohorts, not raw counts.
- Statistical tests: chi-square for categorical variables, Mann-Whitney for numeric ones, a Poisson GLM with log-exposure offset for subscriptions, and a random forest with 5-fold cross-validation for overall predictability. With roughly 25 factors tested, an isolated p ≈ 0.05 is expected by chance and was not treated as a finding.
