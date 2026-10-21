# Checkout page A/B test (3–16 Aug 2026): readout

## Bottom line

- **The test doesn't show that the new checkout page increases conversion. Don't ship it on this evidence.**
- The headline numbers look like a clear win: conversion is 6.38% vs 5.88% (+8.5%, p = 0.0007). That win is not real. It comes from a broken split. About 5,000 treatment users on the old Android app (version 5.1.4) are missing from the data from 5 Aug onward.
- Those missing users are the lowest-converting group in the test. Losing them from treatment pushes the treatment average up, whatever the page itself does.
- Comparing like with like, the new page's effect is **+0.17 percentage points (6.33% → 6.50%, +2.7%), 95% CI −0.14 to +0.48pp, p = 0.28**. That is not statistically significant. Revenue per user doesn't differ either.
- **Recommendation:**
  1. Find and fix why treatment users on Android 5.1.4 drop out of the test.
  2. Re-run with daily checks on the 50/50 split.
  3. Decide on the re-run.

  The missing users could also be a warning sign: the new page may be broken for them, which would be real harm that this data cannot show.

## Data and method

- **Data:** `experiment_users.csv`, one row per assigned user, 104,978 users, assignment dates 3–16 Aug 2026 (14 days, all complete).
- **Quality:** no missing values and no duplicate user IDs. Revenue is above 0 exactly when `converted = 1`.
- **Platforms and versions:** each app version belongs to one platform. Android has 5.1.4 and 5.3.2, iOS has 6.2.1, and web has "browser".
- **Assumption on conversion:** I take `converted` to mean the user converted within the test, with the same measurement for both groups. The data doesn't define a conversion window. Conversion doesn't fall for users assigned later in the test, so there's no sign that late assignees had too little time to convert.
- **Tests:** conversion was compared with two-proportion z-tests, revenue with Welch t-tests. Robustness checks used a regression adjusted for app version and post-stratification by version.

## Finding 1: the 50/50 split is broken

The brief says users were split 50/50. The data has **54,898 control vs 50,080 treatment**; under a true 50/50 split a gap that large is essentially impossible (p ≈ 5×10⁻⁵⁰).

All of the imbalance comes from one segment:

| Segment | Control | Treatment | Treatment share | p (vs 50/50) |
|---|---|---|---|---|
| Android 5.1.4 | 6,569 | 1,517 | **18.8%** | ≈0 |
| Android 5.3.2 | 7,185 | 7,219 | 50.1% | 0.78 |
| iOS 6.2.1 | 19,205 | 19,357 | 50.2% | 0.44 |
| Web | 21,939 | 21,987 | 50.1% | 0.82 |

Within Android 5.1.4, the split is normal on 3 Aug (507 control / 486 treatment) and 4 Aug (485 / 464). **From 5 Aug onward, treatment gets only 39–56 users a day, against 423–491 in control**, every day to the end of the test. That puts about 5,000 treatment users missing.

**Likely cause (not confirmed):** something that changed around 5 Aug stops treatment users on the old Android 5.1.4 app from loading the new page or being logged. Examples are a deployment, a crash, or a tracking event the old app doesn't send. This data can't tell us which. To confirm it, we need:
- the assignment-service logs (were these users assigned and then lost?);
- client crash and error logs for Android 5.1.4 from 5 Aug;
- release notes for any change made on 4–5 Aug.

## Finding 2: the headline lift comes from the missing users, not the page

Android 5.1.4 users convert at about 2.6%, against 5.5–7.3% for everyone else. Treatment lost most of them and control kept them, so the treatment average goes up even if the page changes nothing.

| Comparison | Control CR | Treatment CR | Difference | 95% CI | p |
|---|---|---|---|---|---|
| Naive, all users (biased) | 5.88% | 6.38% | +0.50pp | +0.21 to +0.79 | 0.0007 |
| Excluding Android 5.1.4 (balanced) | 6.33% | 6.50% | **+0.17pp** | −0.14 to +0.48 | 0.28 |
| All users, adjusted for app version | | | +0.16pp | −0.14 to +0.46 | 0.29 |
| Treatment re-weighted to control's version mix | 5.88% | 6.03% | +0.15pp | | |
| All users, 3–4 Aug only (before the problem started) | 6.16% | 6.15% | −0.00pp | −0.75 to +0.74 | 0.99 |

- About **0.35pp of the 0.50pp headline lift is a mix effect**: the change in which users are in each group. Only about 0.15pp is a difference in conversion within comparable users.
- Three different ways of correcting for the imbalance give the same answer.
- An independent re-analysis, done from scratch without seeing my reasoning, reproduced these figures and confirmed the conclusion.

## Finding 3: no clear effect in any segment, and none on revenue

Results for balanced users, i.e. excluding Android 5.1.4:

| Segment | n (C / T) | Control CR | Treatment CR | Difference | p |
|---|---|---|---|---|---|
| Android 5.3.2 | 7,185 / 7,219 | 5.47% | 5.78% | +0.31pp | 0.42 |
| iOS 6.2.1 | 19,205 / 19,357 | 6.88% | 7.32% | +0.44pp | 0.09 |
| Web | 21,939 / 21,987 | 6.14% | 6.02% | −0.12pp | 0.60 |

- **Segments:** the test for whether the effect differs by platform isn't significant (p = 0.24). iOS is the strongest hint, but it isn't significant even before correcting for testing several segments.
- **Over time:** the effect is stable, +0.18pp in week 1 and +0.16pp in week 2.
- **Revenue per user:** $4.34 control vs $4.39 treatment (p = 0.64).
- **Average order value among converters:** $68.47 vs $67.58 (p = 0.33).
- **The Android 5.1.4 treatment users who do appear after 5 Aug** (567 of them) convert at 3.0% vs 2.6% in control. They are a self-selected remainder and too few to read anything into.

## What this test can and can't rule out

- With about 48,000 users per group and a 6.3% baseline, the test could reliably detect a lift of about **0.44pp (about 7% relative)**, at 80% power and 5% significance.
- **Ruled out:** a large effect like the +8.5% the headline suggests.
- **Not ruled out:** a small real lift. The upper end of the CI is +0.48pp, and iOS leans positive.
- So the conclusion is "no demonstrated improvement", not "proven to have no effect".

## Recommendations

1. **Don't ship based on this test.** The only significant result comes from the broken split.
2. **Investigate Android 5.1.4 first.** If the new page fails or crashes on that version, shipping it would hurt about 8% of users, and this data can't measure that harm, because those users never appear in it.
3. **Fix the problem and re-run the test.**
   - Track the treatment share daily, by platform and app version, and stop or alert when it drifts from 50/50.
   - To detect a lift of about +3% relative (about 0.2pp), plan for roughly 230,000+ users per group, about 4–5× this test. The alternative is to accept that only lifts of 7% or more will be detectable.
4. **If the business still wants to act now**, the most it could defend is a limited rollout to iOS and web, with monitoring. Even then the evidence is weak (iOS p = 0.09, web flat), so I don't recommend it over a clean re-run.
