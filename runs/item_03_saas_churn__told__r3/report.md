# Customer churn drivers: 2023–2024 assessment

## Bottom line

1. **The data doesn't support "retention has deteriorated over two years."** Raw churn went up about 7× (73 churn events in 2023, 527 in 2024). Over the same period the customer base grew even faster: active subscriptions rose from 648 at end‑2023 to 4,514 at end‑2024. Measured per active subscription, churn events have stayed flat at about **5 per 100 active subscriptions per quarter** since mid‑2023.
2. **There is one unresolved warning sign: subscriptions that started in H2 2024 are ending much sooner after they start.**
   - 30‑day churn was 0.6–1.0% for 2023–24Q2 starts.
   - It was 2.4% for 24Q3 starts and 6.0% for 24Q4 starts.
   - Subscription terminations reached 6.7 per 100 active subscriptions in 24Q4, against 2–3 earlier.

   This pattern is exactly what you would see if every subscription has a fixed ~10% chance of being flagged churned, however long it has existed. That points either to a real speed‑up in early churn or to the way churn dates are recorded. **The data can't tell these apart.** Settling it is the first priority (see Recommendations).
3. **No driver of churn can be identified from this data.** Plan, price, seats, billing terms, trial status, auto‑renew, industry, country, acquisition channel, product usage, error rates, support volume, resolution time, CSAT and escalations all show no meaningful relationship with churn. The recorded churn reasons are effectively random.
4. **The data has serious integrity problems,** and they limit any driver analysis (details below). Before funding a retention programme, fix the churn definition and its data. Otherwise the money will go to a cause nobody can name.

## Data and method (read first)

- **Coverage:**
  - 500 accounts (signups Jan 2023–Dec 2024).
  - 5,000 subscriptions (starts Jan 2023–Dec 2024).
  - 600 churn events.
  - 2,000 support tickets.
  - 25,000 feature‑usage rows.
  - The extract ends 2024‑12‑31, so everything recent is **right‑censored**: recent subscriptions have had little time to churn.
- **Growth is extreme:**
  - Subscription starts went from 31 in 23Q1 to 2,069 in 24Q4.
  - The average subscriptions per account went from about 1.3 to 9.7.
  - Raw counts are therefore meaningless as a trend. Every rate below sits beside its volume.
- **There are three different "churn" definitions, and they disagree:**

  | Source | What it says |
  |---|---|
  | `accounts.churn_flag` | 110 of 500 accounts (22%) flagged churned, yet **every** account still has at least one open subscription. 277 accounts flagged *not* churned have churn events. |
  | `churn_events` | 600 events on 352 accounts; 10% are reactivations. Only ~1% match a subscription end on the same date, and ~8% within 7 days. No `subscription_id` to link them. |
  | `subscriptions.churn_flag` / `end_date` | 486 ended subscriptions (9.7%). Flag and end date agree exactly. |

  I use subscription end dates and churn events as the main measures. I treat the account flag as undefined and don't rely on it.
- **Timestamps aren't coherent across tables:**
  - 77% of feature‑usage rows are dated *before* their subscription started, and 290 are dated after it ended.
  - 54% of support tickets predate the account's signup.
  - So usage and support data can't be lined up in time with churn ("usage fell, then they churned" can't be tested). I used them only as lifetime totals.
- **Other quality notes:**
  - 21 duplicate `usage_id`s.
  - 41% of tickets have no CSAT score.
  - 25% of churn events have no feedback text.
  - The churn `reason_code` is statistically independent of the free‑text feedback (e.g., "pricing" churners are as likely to say "missing features" as "too expensive").
- **Method:** descriptive rates by quarter and by start cohort, follow‑up‑matched early‑churn rates, and logistic regressions of churn on all candidate drivers. Claims are tagged **[OBS]** (computed from the data), **[CON]** (the best reading of the evidence) or **[HYP]** (plausible but not shown).

## Finding 1: no sustained deterioration per unit of business

| Quarter | Active subs | Churn events | Events per 100 active subs | Subscription ends | Ends per 100 active subs |
|---|---|---|---|---|---|
| 2023Q3 | 338 | 19 | 5.6 | 2 | 0.6 |
| 2023Q4 | 662 | 37 | 5.6 | 14 | 2.1 |
| 2024Q1 | 1,120 | 54 | 4.8 | 27 | 2.4 |
| 2024Q2 | 1,779 | 92 | 5.2 | 37 | 2.1 |
| 2024Q3 | 2,849 | 130 | 4.6 | 80 | 2.8 |
| 2024Q4 | 4,838 | 251 | 5.2 | 324 | 6.7 |

- [OBS] Churn events per active subscription are flat from 2023Q3 to 2024Q4.
- [OBS] Subscription terminations ran at about 2–3 per 100 per quarter until a spike in 2024Q4. December alone had 193 ends, versus 58–73 in October–November.
- [OBS] The share of subscriptions that ever churn, by start quarter, was 9.3%, 8.6%, 8.1% and 10.1% across 2024. The small 2023 cohorts ran 10–19%.
- [OBS] Measured **per account**, churn events did rise: from 0.16 per account per quarter in 23Q4 to 0.50 in 24Q4. That rise matches the growth in subscriptions per account (2.9 to 9.7). Churn events scale with how many subscriptions a customer holds, not with how many customers there are.
- [OBS] Revenue view: churned MRR was about 2% of the opening MRR per quarter through 24Q3, and 5.1% in 24Q4.
- [CON] Through 2024Q3, the evidence shows no deterioration per subscription. Everything that looks like deterioration is concentrated in 2024Q4 (Finding 2).

## Finding 2: an early‑churn spike in late 2024 that the data can't resolve

| Start quarter | Subs (≥30 days follow‑up) | Churned within 30 days | Expected if every sub has a flat 9.7% churn chance, dated at random over its observed life |
|---|---|---|---|
| 2023Q2–2024Q2 | 1,793 | 0.6–1.0% | 0.5–1.3% |
| 2024Q3 | 1,107 | 2.4% | 2.3% |
| 2024Q4 | 1,135 | 6.0% | 5.7% |

- [OBS] Early churn among H2‑2024 starts is 3–6× the earlier rate. The rise appears equally in every plan, billing term, industry, country and channel; no segment concentrates it.
- [OBS] The structural pattern:
  - The chance that a subscription is flagged churned doesn't depend on how long it has been observed (logit p = 0.11).
  - A subscription started last month is as likely to be flagged as one started two years ago.
  - Churned subscriptions' end dates are spread uniformly across their observed lifetime (KS test vs uniform, p = 0.25).
  - The "flat probability" column in the table above reproduces the observed rise almost exactly.
- **Two readings fit equally well:**
  - [HYP‑A, real] Recently acquired subscriptions churn much faster than earlier ones. That would be a genuine and urgent onboarding/fit problem, possibly linked to the very rapid H2‑2024 acquisition push.
  - [HYP‑B, recording artefact] Churn is being flagged at a steady rate and stamped with a date somewhere inside the subscription's observed window, possibly at extract time. December end dates also bunch in the final days (24 on 12‑31, 18 on 12‑30, 19 on 12‑29), which fits this reading.
- **What would settle it:**
  - Confirm with the billing/source system how `end_date` is set and whether the December 2024 terminations are real cancellations.
  - Re‑pull the extract through mid‑2025 and compare 90‑day survival curves for H1‑ vs H2‑2024 cohorts at equal tenure.
  - Check a sample of December‑2024 terminations against invoices and cancellation records.

## Finding 3: no identifiable churn driver

- [OBS] **Subscription level** (n = 5,000, base churn 9.7%). In a multivariable logit, no candidate driver is significant (all p > 0.2). Ranges by group:
  - plan tier: 9.5–10.0%
  - billing: 9.4% monthly vs 10.0% annual
  - trial vs paid: 10.0% vs 9.7%
  - auto‑renew: 9.6% vs 9.7%
  - seats and MRR quartiles: 9.0–10.6%
  - usage volume, error rate, beta‑feature share and feature breadth quartiles: 8.7–11.1%
  - support tickets, resolution time, first‑response time, CSAT and escalation: 8.7–11.2%
  - downgraded subscriptions: 11.5% vs 9.6% (n = 218, not significant)
- [OBS] **Account level** (n = 500):
  - DevTools accounts show a higher flagged churn rate (31% vs 16–22% for other industries).
  - The test across all industries is not significant (p = 0.07), and the gap doesn't appear in subscription churn (p = 0.31) or in churn events per account (p = 0.88).
  - Given ~20 dimensions tested, I treat it as noise. [CON]
- [OBS] **Stated reasons** are spread evenly: features 19%, support 17%, budget 17%, unknown 16%, competitor 15%, pricing 15%. `reason_code` is independent of the customer's own feedback text. [CON] They can't be used to choose where to invest.
- [CON] This data doesn't show that churn is driven by price, product usage, support quality, plan or customer segment. That is not proof those factors don't matter. The integrity problems above (misdated usage and tickets, unlinkable churn events, an undefined account flag) could hide a real signal.

## Recommendations

1. **Don't fund a broad churn‑reduction programme yet.** The premise of a two‑year deterioration isn't supported, and no driver has been found to target. Money spent now on pricing, support or product would rest on guesswork.
2. **Resolve the Q4‑2024 signal within weeks, not quarters.** It is the one thing that could be a real, recent problem.
   - Audit how `end_date` and churn flags are written.
   - Verify a sample of December cancellations against billing.
   - Re‑pull data into 2025 for tenure‑matched cohort survival.
   - If HYP‑A is confirmed, the response is an **onboarding and early‑life programme for new subscriptions** (first‑30/90‑day health checks), not a programme aimed at the installed base.
3. **Fix the churn data before the next analysis:**
   - Write down one definition of churn (customer vs subscription vs revenue).
   - Add `subscription_id` to churn events.
   - Reconcile the account‑level flag with it.
   - Fix timestamp lineage for usage and support data so they fall inside the subscription's lifetime.
   - Make the churn reason a required, validated field captured at cancellation (e.g., by the CSM or in an exit survey). The current codes carry no information.
4. **Track churn as rates on the right base.** Use churn per active subscription (or net revenue retention) by start‑cohort and tenure, never raw counts, which will keep rising as long as the business grows.

## Verification

- An analytical‑rigor checklist was run on the draft. It caught a misquoted count, corrected here: ended subscriptions were 18 in 2023 and 468 in 2024. It also prompted the per‑account vs per‑subscription check in Finding 1.
- A fresh, independent agent re‑tested the headline claim from raw data.
  - It reproduced the per‑subscription figures: 73 → 527 events, 4.6–5.6 events per 100 active subs, 2024 cohort churn shares of 8–10%.
  - It returned **CONTRADICTED** on "no deterioration": tenure‑matched early churn and Q4‑2024 terminations rise, and per‑account events rise.
- I accepted that challenge. The report no longer claims "no deterioration" without qualification. It separates the stable 2023–24Q3 picture from the unresolved H2‑2024 early‑churn rise and shows why that rise can't yet be told apart from a recording artefact.
