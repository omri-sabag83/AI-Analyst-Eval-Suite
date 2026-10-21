# Checkout page A/B test (2026-08-03 to 2026-08-16): readout

## Bottom line
- **The headline result doesn't hold up.** Comparing all users, treatment looks like a win: conversion of 6.38% vs 5.88% (+0.50 pp, +8.5%, p = 0.0007) and revenue per user of $4.31 vs $4.02 (p = 0.01). That gap is an artifact of broken data, not a real effect of the new page.
- **Treatment is missing about 5,000 users, all from one place.** These are Android users on app version **5.1.4**, and they stop appearing in treatment from **2026-08-05** onward. Those users convert far less than anyone else (about 2.6%). Losing them from treatment only, and not from control, pushes treatment's average up.
- **The fair comparison shows no significant lift.** Restricted to the groups where assignment worked, conversion is **6.50% vs 6.33%: +0.17 pp (+2.7%), 95% CI −0.14 to +0.48 pp, p = 0.28**. Revenue per user is $4.39 vs $4.34 (p = 0.64).
- **Recommendation: don't ship on this evidence.** First find out what the new page does on Android 5.1.4. The most likely explanation is that the new page fails on that app version. If so, shipping it would hurt those users. Then fix the bug and rerun the test (details below).

## 1. The randomisation broke (sample-ratio mismatch)
Users were meant to be split 50/50, but the data has 54,898 in control and 50,080 in treatment. A gap that large has essentially no chance of happening by luck (chi-square p ≈ 5×10⁻⁵⁰).

| Segment (platform / version) | Control | Treatment | Balanced? |
|---|---|---|---|
| Android 5.1.4 | 6,569 | **1,517** | **No** (p ≈ 0) |
| Android 5.3.2 | 7,185 | 7,219 | Yes (p = 0.78) |
| iOS 6.2.1 | 19,205 | 19,357 | Yes (p = 0.44) |
| Web (browser) | 21,939 | 21,987 | Yes (p = 0.82) |

The timing narrows it down further. On Aug 3–4, Android 5.1.4 was balanced (992 control vs 950 treatment). From **Aug 5 to Aug 16**, treatment recorded only about 40–55 users from that version per day, compared with about 450–500 in control. In total, **about 5,010 treatment users are missing**. Every other segment is balanced on every day.

What this most likely means (a hypothesis; the data can't confirm it): something changed on about Aug 5, such as a release, a config change or a feature flag. After that, the new checkout page appears to fail on app 5.1.4: it crashes, doesn't load, or doesn't fire the event that logs a user into the experiment. As a result, most 5.1.4 users assigned to treatment never enter the dataset. The engineering and instrumentation logs need to confirm this.

## 2. Why the headline lift is misleading
Users on Android 5.1.4 convert at only about 2.6%, compared with 5.5–7.3% everywhere else. Removing most of them from treatment, but not from control, raises treatment's overall conversion rate even though the page itself hasn't changed anything. The lifts within each segment are all small and none is statistically significant. Pooled together, the imbalance turns them into an apparent +8.5%.

Conversion by segment, in full:

| Segment | Control CR | Treatment CR | Difference | p |
|---|---|---|---|---|
| Android 5.1.4 (broken) | 2.56% | 2.57% | +0.01 pp | 0.98 |
| Android 5.3.2 | 5.47% | 5.78% | +0.31 pp | 0.42 |
| iOS 6.2.1 | 6.88% | 7.32% | +0.44 pp | 0.09 |
| Web | 6.14% | 6.02% | −0.12 pp | 0.60 |
| **All, excluding 5.1.4 (valid comparison)** | **6.33%** | **6.50%** | **+0.17 pp [−0.14, +0.48]** | **0.28** |
| All except 5.1.4 from Aug 5 on (keeps the balanced Aug 3–4 users) | 6.25% | 6.42% | +0.17 pp [−0.13, +0.47] | 0.27 |

- **Do the segments respond differently?** iOS looks a little positive and web a little negative. A formal test (logistic regression with a treatment × platform interaction, excluding 5.1.4) finds no significant difference between platforms (p = 0.27). Treat the per-segment numbers as noise.
- **Revenue gives the same answer.** In the valid comparison, revenue per user is $4.34 (control) vs $4.39 (treatment), p = 0.64. Average order value is roughly the same in both arms ($66–70).

## 3. What the clean result does and doesn't tell us
- Excluding 5.1.4 leaves about 48,000 users per arm. With that sample, the test could reliably detect (80% power, 5% significance) a lift of about **0.44 pp, or roughly +7% relative**. Any lift larger than about +0.48 pp is unlikely. A small real lift of about 2–3% is possible but unproven, and so is a small loss.
- **For Android 5.1.4 users, the new page could be very harmful.** Measured conversion in that segment (2.57%) only covers the treatment users who made it into the data. Suppose the roughly 5,000 missing users couldn't check out at all. Then only 17 conversions came from about 5,577 assigned users, which is around 0.3% against 2.6% in control. That is a worst-case bound, not an estimate. It shows the 5.1.4 problem has to be fixed before launch rather than ignored.
- Data quality was otherwise clean: no missing values, no duplicate users, and revenue is greater than zero exactly when `converted = 1`.

## 4. Recommendations
1. **Don't ship based on this test.** The +8.5% headline comes from the data problem. The valid comparison shows +2.7%, which is not statistically significant, and the true effect could be zero or slightly negative.
2. **Investigate Android 5.1.4 now.** Check what changed on about Aug 5, crash logs for the new checkout page on 5.1.4, and whether its exposure/assignment event fires. If the page fails on that version, it would hurt those users after launch. About 8% of test traffic was on that version.
3. **Fix the bug and rerun the test** with an automatic sample-ratio check on every platform and version, run daily. To detect a lift of about 2–3% (about 0.15–0.2 pp at a 6.3% baseline), you need roughly **250k–450k users per arm**, about 5–9 times this test. Alternatively, agree in advance on the smallest lift worth shipping and size the test for that.
4. **If the business would ship with no measurable lift** (for example, for maintenance or design reasons), the clean data supports that only if the 5.1.4 problem is fixed first. Even then, it rules out a large gain, not a small loss (lower bound −0.14 pp).

## Assumptions and method
- Each row is one user; "conversion" means `converted = 1`. Users are analysed in the group they were assigned to.
- **Excluding Android 5.1.4 is the main analysis.** Assignment is balanced in the other three segments on every day, so the comparison there is still randomised. That makes it a valid estimate of the effect for users on those versions, but not for 5.1.4 users.
- Conversion was tested with two-proportion z-tests and revenue with Welch t-tests, both two-sided at α = 0.05. Imbalance was tested with chi-square goodness-of-fit against 50/50.
