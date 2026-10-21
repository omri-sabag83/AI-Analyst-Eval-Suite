# Checkout page A/B test (Aug 3–16, 2026): findings and recommendation

## Bottom line

**Don't ship the new checkout page on this evidence.**

- On the raw numbers, the new page appears to lift conversion by 8.5% (p = 0.0007). That headline is not valid. The test has a data-collection defect: from Aug 5 onward, about 5,000 treatment users on the Android app version 5.1.4 are missing from the data. That segment converts at less than half the average rate, so losing it from treatment makes treatment look better than it is.
- If we compare like with like (only the users who were randomised properly), the new page's lift is **+0.17 percentage points (6.50% vs 6.33%, +2.7% relative)**. The 95% CI runs from −0.14 to +0.48pp and p = 0.28, so it is **not statistically significant**. Revenue per user does not move either (p = 0.64).
- Next steps: find and fix the 5.1.4 problem, then re-run the test, ideally with more traffic or for longer.

Tags used below: **[OBS]** means seen directly in the data. **[CON]** means a conclusion the evidence supports. **[HYP]** means a plausible explanation that has not been verified.

## Data and method

- **What the data covers:** one row per user, 104,978 users, assigned Aug 3–16, 2026. Every one of the 14 days is complete.
- **Data quality:** there are no duplicate users and no missing values. Revenue is above 0 exactly when `converted = 1`.
- **Definitions:**
  - Conversion = share of users with `converted = 1`.
  - Revenue = mean revenue per assigned user.
- **Tests used:**
  - two-proportion z-test for conversion, and Welch's t-test for revenue;
  - a binomial test of the group split against 50/50, to check for sample-ratio mismatch (SRM);
  - stratified (CMH) tests and a regression with segment controls, as robustness checks.
- **Assumption:** each user's `converted` flag reflects their outcome within the test, and a user's app version is fixed at assignment.

## Finding 1: the groups are not 50/50, and the imbalance is in one segment

**[OBS]** The test was designed 50/50, but it has 54,898 control users and 50,080 treatment users. The chance of a gap this large under a true 50/50 split is about 5 × 10⁻⁵⁰. The randomisation or the logging is broken somewhere.

**[OBS]** Breaking it down by segment shows exactly where:

| Segment | Control n | Treatment n | Treatment share | SRM p |
|---|---|---|---|---|
| Android app 5.1.4 | 6,569 | 1,517 | 18.8% | ≈0 |
| Android app 5.3.2 | 7,185 | 7,219 | 50.1% | 0.78 |
| iOS app 6.2.1 | 19,205 | 19,357 | 50.2% | 0.44 |
| Web | 21,939 | 21,987 | 50.1% | 0.82 |

**[OBS]** The problem starts on a specific date. On Aug 3 and 4, Android 5.1.4 was balanced (control/treatment 507/486 and 485/464). From Aug 5 onward, treatment gets only about 40–55 users a day, against about 470 a day in control. Over Aug 5–16 that is 567 vs 5,577 users, so about **5,000 treatment users are missing**. With 5.1.4 excluded, no single day shows an imbalance.

**[HYP]** Something changed on Aug 5 that affects only the new page on app 5.1.4. Possible causes:
- (a) the new page crashes or fails to load on that old app version, so users never reach the point where they are logged;
- (b) an exposure or logging event that 5.1.4 doesn't fire for the new page;
- (c) a targeting or config change that stopped serving treatment to 5.1.4.

The data can't tell these apart. They can be settled with:
- client crash and error logs for 5.1.4;
- the raw assignment log, compared with the exposure log;
- the release and feature-flag history for Aug 4–5.

This matters for the shipping decision. If (a) is true, the new page is actively broken for these customers.

## Finding 2: the headline lift is mostly caused by the missing users

**[OBS]** Headline (all users): treatment 6.38% vs control 5.88%, +0.50pp (+8.5%), p = 0.0007. Revenue per user is $4.31 vs $4.02 (p = 0.01).

**[OBS]** Android 5.1.4 users convert at about 2.6%, against about 6.4% for everyone else. They make up 12.0% of control but only 3.0% of treatment. Splitting the +0.50pp gap into its parts:
- **mix effect, +0.34pp:** the groups contain different shares of each segment, mostly because 5.1.4 users are missing from treatment;
- **within-segment effect, +0.15pp:** genuine differences in conversion inside each segment;
- **interaction, +0.01pp.**

**[CON]** About two-thirds of the headline lift comes from the different mix of users, not from the page changing behaviour. The p-value of 0.0007 is not valid evidence that the new page works.

## Finding 3: comparing like with like, there is no demonstrated lift

**[OBS]** Results on the properly randomised users, with Android 5.1.4 excluded from both groups:

| Metric | Control | Treatment | Difference | 95% CI | p |
|---|---|---|---|---|---|
| Users | 48,329 | 48,563 | | | SRM p = 0.45 |
| Conversion | 6.33% | 6.50% | +0.17pp (+2.7%) | −0.14 to +0.48pp | 0.28 |
| Revenue per user | $4.34 | $4.39 | +$0.06 | | 0.64 |

**[OBS]** By segment (the 5.1.4 row covers all its users, including the unbalanced days):

| Segment | n (C / T) | Control CR | Treatment CR | Difference | p |
|---|---|---|---|---|---|
| iOS 6.2.1 | 19,205 / 19,357 | 6.88% | 7.32% | +0.44pp | 0.09 |
| Android 5.3.2 | 7,185 / 7,219 | 5.47% | 5.78% | +0.31pp | 0.42 |
| Web | 21,939 / 21,987 | 6.14% | 6.02% | −0.12pp | 0.60 |
| Android 5.1.4 (unbalanced) | 6,569 / 1,517 | 2.56% | 2.57% | +0.01pp | 0.98 |

None of these is significant. iOS is the closest, but with four segments tested, p = 0.09 is a weak signal.

**[OBS] Robustness:** every alternative way of making the comparison fair gives the same answer, about +0.16 to +0.17pp with p ≈ 0.27–0.30:
- excluding only the unbalanced 5.1.4 days (Aug 5–16) and keeping Aug 3–4;
- a CMH test stratified by app version (odds ratio 1.028, p = 0.29);
- a CMH test stratified by app version × date;
- logistic regression with segment controls.

The result is also stable over time: week 1 shows +0.16pp and week 2 shows +0.18pp. An independent re-analysis by a separate agent, which saw only the claim and the raw data, reproduced all of these figures. Its verdict was **HOLDS**.

**[OBS] Power:** at a baseline of about 6.3% and about 48k users per group, this test could reliably detect (80% power) a lift of about **0.44pp, or about +7% relative**. The true effect could still be a small positive one that the test was too small to detect. The data are also consistent with zero, and with a small negative effect.

**[CON]** The new page has **not been shown to increase conversion**. Its effect is small: plausibly between −2% and +7.5% relative.

## What the missing users could mean (estimates)

We can't observe what happened to the roughly 5,050 missing treatment users. These two scenarios bound the full-population result. Both are estimates under the stated assumptions, not measurements:
- **If the missing users converted at the 5.1.4 control rate (2.56%)**, that is, the problem was only logging: treatment would be about 6.03% vs control 5.88%, a +0.15pp gap. That is about the same as the clean result.
- **If none of them converted**, for example because the page broke for them: treatment would be about 5.80% vs control 5.88%. **The new page would be net negative.**

## Recommendations

1. **Don't ship yet.** The test shows no reliable conversion or revenue gain, and the new page may be broken on Android 5.1.4.
2. **Investigate the 5.1.4 problem first** (engineering and the experimentation-platform owner). Check the crash and error logs, compare the assignment log with the exposure log, and review changes released on Aug 4–5. If the new page fails on 5.1.4, fix it, or exclude that version from the rollout, before any launch.
3. **Re-run the test once the fix is in.** At the current traffic of about 7,500 users a day, two weeks can only detect a lift of about +7%. To detect a +3% relative lift (about 0.19pp) with 80% power you need about 260k users per group, which means a longer test or more traffic. Agree the minimum lift worth shipping before the test starts.
4. **Add a guardrail:** run an automatic sample-ratio check, overall and per platform/app version, every day. Alert when p < 0.001. In this test it would have flagged the problem on Aug 5 or 6, with nine days still left to fix it.
5. **Optional:** if the team wants to act before a re-test, the most promising signal is on iOS (+0.44pp, p = 0.09). That is a hypothesis to test, not a basis for shipping.
