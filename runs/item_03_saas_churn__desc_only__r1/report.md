# Customer churn: has retention deteriorated, and what is driving it?

## Bottom line

1. **Retention did not decline steadily over the two years.** Raw churn counts went up about 40-fold between 2023 and late 2024. Over the same period the number of active subscriptions went up about 150-fold. Measured as a rate (churn per unit of exposure), subscription churn held steady at about **0.3 churns per 1,000 subscription-days (about 0.9% a month)** from 2023 through mid-2024. Any chart showing churn counts rising over 2023–2024 is mostly showing that the business grew.
2. **There is one recent change: brand-new subscriptions started churning in their first weeks, from about August 2024.** It peaked in November and December 2024. Among subscriptions in their first 30 days, the churn hazard rose from about 0.2–0.6 to **3.3 per 1,000 days in Q4 2024**, roughly 5–10 times higher. Subscriptions older than 90 days showed **no change**. Because Q4 sign-ups were also unusually large, this one effect produced most of the year's lost MRR: **about $872k of churned MRR in Q4 2024, against $147k in Q3**.
3. **The data does not show *why* customers churn.** Plan, billing terms, trial status, seats, MRR, support experience, product usage and errors do not separate churners from retained customers, either at the account level or the subscription level. The recorded churn reasons cannot be trusted (details below). The only weak lead is that DevTools accounts churn more often (31% against 16–22% for other industries). That result is marginal and needs confirming before anyone acts on it.
4. **The Q4 2024 spike has to be confirmed before money is spent on it.** It sits right at the end of the data extract (churn end dates bunch up on 28–31 December). The separate churn-events table shows no spike at all. It may be real, or it may come from year-end processing or how the data was extracted.

**Recommendation:** Do not fund a broad retention programme aimed at the whole customer base. The long-standing churn rate has not moved. First, spend 1–2 weeks of a data owner's time confirming the Q4 2024 early-churn spike. If it holds, fund a targeted **onboarding / first-30-days** response for new subscriptions started since August 2024. Fix the churn-reason data collection at the same time, so that drivers can actually be identified.

---

## 1. Has retention deteriorated?

### Counts vs. rates

| Quarter | Active subscriptions | Subscriptions churned | Churn rate (churned ÷ active) | Churned MRR as % of active MRR |
|---|---|---|---|---|
| 2023 Q2 | 137 | 2 | 1.5% | 0.6% |
| 2023 Q3 | 338 | 2 | 0.6% | 0.1% |
| 2023 Q4 | 662 | 14 | 2.1% | 3.7% |
| 2024 Q1 | 1,120 | 27 | 2.4% | 2.2% |
| 2024 Q2 | 1,779 | 37 | 2.1% | 1.5% |
| 2024 Q3 | 2,849 | 80 | 2.8% | 2.4% |
| **2024 Q4** | **4,838** | **324** | **6.7%** | **7.9%** |

"Active" means any subscription active at some point in the quarter. "Churned" means a subscription with `churn_flag = True` whose `end_date` falls in the quarter.

Churn counts rise every quarter, but the rate stays flat at about 2–3% a quarter until Q4 2024. The monthly rate tells the same story: 0.7–0.9% a month from February to July 2024, 1.2% in August–September, 1.8–1.9% in October–November, and **4.1% in December 2024**.

### Where the Q4 increase sits: new subscriptions only

The table shows churn hazard per 1,000 subscription-days, by calendar quarter and by how old the subscription was:

| Quarter | 0–30 days | 31–90 days | 91–180 days | 181–365 days | >365 days |
|---|---|---|---|---|---|
| 2024 Q1 | 0.38 | 0.36 | 0.46 | 0.20 | – |
| 2024 Q2 | 0.15 | 0.31 | 0.32 | 0.31 | 0.29 |
| 2024 Q3 | 0.63 | 0.50 | 0.43 | 0.16 | 0.30 |
| **2024 Q4** | **3.31** | **1.06** | 0.38 | 0.37 | 0.33 |

- Subscriptions older than 90 days churn at the same rate as before (about 0.3–0.4). Established customers are not leaving faster.
- The increase is entirely among subscriptions in their first 90 days, and mostly in their first 30 days.
- **This is a real rise in rates, not a change in the customer mix.** The share of exposure that comes from young subscriptions was about the same in Q3 and Q4 (15–16% at 0–30 days). Weighting every quarter to Q4's tenure mix gives a flat 0.27–0.30 per 1,000 days from 2023 Q2 to 2024 Q2, then 0.39 in Q3 and 1.00 in Q4.
- By start month, the share of new subscriptions cancelled within 30 days was 0–2% in every month through July 2024. It was then 2.4% (August), 3.4% (September), 3.4% (October), 7.7% (November) and 10.5% (December, but only 19 subscriptions have a full 30 days of data). The 14-day view uses more December data: 1.2% (October), 4.7% (November) and 7.1% (December).
- The new subscriptions look the same as earlier ones: trial share 15% vs 16%, Enterprise share 35% vs 34%, annual billing 49% vs 49%, auto-renew 80% vs 80%, median MRR $931 vs $882. Early churn in Q4 is spread evenly across plan tiers (7–9%), industries (6–10%), referral sources (6–10%) and trial vs paid. It also covers many customers, not a handful: 173 early churns across 138 accounts.

### Account-level view

22% of accounts (110 of 500) have `churn_flag = True`. Accounts that signed up in 2023 show 25.5%, and 2024 sign-ups show 19.0%. Older accounts have simply been exposed for longer, so this does **not** suggest that newer customers are worse. By signup quarter the rate falls fairly steadily, from 29% (2023 Q1) to 15% (2024 Q4).

### Why the Q4 spike needs checking before acting on it

- **The end dates bunch up at the edge of the data.** December 2024 accounts for 193 churned subscriptions, and 71 of those end on 28–31 December (24 on 31 December itself). 103 of the December churners also *started* in December, with a median life of 14 days. This pattern is what you would expect from year-end cancellation processing, from a batch close, or from subscriptions being end-dated at the time of extraction.
- **The churn-events system does not show it.** Measured per active subscription, recorded churn events are about 5% a quarter in every quarter from 2023 Q3 to 2024 Q4, including Q4 (251 events against 4,838 active subscriptions = 5.2%).
- The rise begins in August, well before year-end, and the November cohort (fully observed for 14 days) is already high. So the effect is probably not *entirely* an artifact. Its size is uncertain.

---

## 2. What is driving churn?

### Tested, no meaningful relationship found

- **Account-level**: churned vs. retained accounts compared on plan tier, seats, country, referral source, trial status, tenure, support tickets, support experience and product use. The support measures were ticket count, resolution time, first-response time, CSAT, escalations and urgent tickets. The product measures were usage volume, duration, error rate, breadth of features used and beta-feature use. The comparisons used Mann-Whitney / chi-square tests, plus a multivariable logistic regression. No factor reached conventional significance apart from the industry result below. Plan tier gives almost identical churn rates (Basic 22.0%, Pro 21.9%, Enterprise 22.1%). The full model explains very little (pseudo-R² = 0.056).
- **Subscription-level** (a Cox survival model, which accounts for tenure): plan tier, billing frequency, trial, upgrade/downgrade, auto-renew, MRR, seats, error rate and beta usage all have hazard ratios close to 1 with p > 0.29. The only strong term is *started in H2 2024* (hazard ratio 3.1, p < 0.001). That is the timing effect from Section 1 again, not an explanation of it.
- **Support and product trends over time are flat.** Ticket volume, resolution time (35–37 hours), first-response time (86–91 minutes), CSAT (3.9–4.1), escalation rate, urgent share, usage per record and errors per record barely change across all eight quarters. Nothing in these extracts lines up with the Q4 2024 change.

### Weak lead

- **DevTools industry**: 31% of DevTools accounts churned, against 16–22% elsewhere (chi-square across industries p = 0.07). In the multivariable model DevTools vs. Cybersecurity gives p = 0.01. However, this is one of many comparisons, and DevTools is *not* over-represented in the Q4 early-churn spike (6.4% early churn, the lowest of the industries). Treat it as a hypothesis to test, not a finding.

### Churn reasons cannot be used as they stand

- `reason_code` is split almost evenly across six categories, including "unknown" (features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%), and the shares do not change in any consistent way over time.
- `feedback_text` does not agree with `reason_code`. For example, events coded "pricing" are as likely to say "missing features" or "switched to competitor" as "too expensive". The two fields are essentially independent, so neither can be relied on.

---

## 3. Data quality problems (these limit what the data can show)

| Issue | Evidence | Impact |
|---|---|---|
| The three churn definitions disagree | 110 accounts are flagged churned. 352 accounts have churn events (600 events). Only 75 accounts appear in both, and 35 flagged accounts have no event at all. No account has all of its subscriptions ended. | There is no single trustworthy definition of "churned customer". I used subscription end dates for the trend and stated which source each number comes from. |
| Feature usage is not tied to subscription periods | 77% of usage records are dated *before* their subscription started. Usage volume is flat (about 3,100 records a quarter) while active subscriptions grew 150-fold. | Usage cannot be used as a churn driver or an early-warning signal from this extract. |
| Support tickets are flat while the customer base grew | About 250 tickets a quarter across every period. | Tickets are probably sampled or limited to one channel. Support findings are weak. |
| End-of-extract bunching | 71 churn end dates on 28–31 December 2024. | The size of the Q4 spike is uncertain (see Section 1). |
| Minor issues | 21 duplicate `usage_id`s and 1 duplicate churn event. | Negligible. |

**Assumptions:** the data runs to 31 December 2024. A subscription with no `end_date` is active. A subscription "churns" when `churn_flag = True`, and its `end_date` is the churn date. Rates are calculated against the subscriptions active at the time, not against sign-ups.

---

## 4. Recommendations

1. **Change the retention story leadership is working from.** The view that churn has been worsening for two years comes from counts that grow with the customer base. The underlying churn rate was stable for about 18 months. Report churn as a rate (by subscription and by MRR, split by tenure) from now on, not as a count.
2. **Check the Q4 2024 spike first (about 1–2 weeks, low cost).** Billing and finance should confirm whether the subscriptions end-dated in December 2024 were real customer cancellations. They could instead be year-end clean-up, migrations, failed payments or duplicate subscriptions that were closed. Then re-run the 30-day churn view on January–February 2025 data. This decides whether a significant budget is needed at all.
3. **If the spike is confirmed, fund a targeted early-life programme, not a broad one.** The excess churn is in the first 30–90 days of new subscriptions, across every segment. That points to something that changed for all new customers from about August 2024, such as the onboarding flow, provisioning, a pricing or packaging change at checkout, a sales-qualification change, or a product release. Product, sales and billing should list what changed in July–September 2024. Spending should go to onboarding and activation for new subscriptions, with a target of bringing 30-day churn back to its earlier 0–2% level. On Q4 figures, the opportunity is several hundred thousand dollars of MRR a quarter. That is an upper bound until step 2 is done.
4. **Do not spend on support, pricing tiers or product-usage interventions on the strength of this data.** None of them shows any link to churn here, and established customers' churn has not changed.
5. **Fix the data so drivers can be measured:** use one churn definition across systems, require a single validated cancellation reason, tie usage events to subscription periods, and make sure ticket data is complete. Without this, the "why" question cannot be answered.
6. **Optional follow-up:** run a small retention review of DevTools accounts to test the weak industry signal.
