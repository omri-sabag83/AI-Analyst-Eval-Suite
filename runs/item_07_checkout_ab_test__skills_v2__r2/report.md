# Checkout page A/B test (2026-08-03 to 2026-08-16): findings and recommendation

## Bottom line
- **The headline result is not valid.** On the raw numbers treatment converts at 6.38% and control at 5.88%, which is +0.50 pp (+8.5% relative, p < 0.001). That lift comes from a data or delivery fault, not from the new page.
- **About 5,000 treatment users on Android app version 5.1.4 are missing from the data from 5 August onward.** Users on that version convert far less than everyone else (about 2.6%). With them gone, the treatment group is left with a mix of higher-converting users, and its average goes up.
- **With the broken segment removed, there is no significant lift.** Treatment is at 6.50% and control at 6.33%: +0.17 pp (+2.7% relative), 95% CI −0.14 to +0.48 pp, p = 0.28. Revenue per user does not move either: $4.39 vs $4.34, p = 0.64.
- **Recommendation: do not ship based on this test.** First find out why treatment users on Android 5.1.4 disappeared, because the new page may be broken on that version. Then re-run the test, ideally sized to detect a smaller lift (details below).

## Data
The file has 104,978 users, one row each, with no duplicate IDs and no missing values. The test was meant to split 50/50, but it has 54,898 control users and 50,080 treatment users. A chi-square test of that split gives p ≈ 5e-50: a severe **sample ratio mismatch (SRM)**, meaning the groups are not the sizes random assignment should produce.

### Where the missing users are
| Segment | Control n | Treatment n | SRM p |
|---|---|---|---|
| Android 5.1.4 | 6,569 | **1,517** | ≈ 0 |
| Android 5.3.2 | 7,185 | 7,219 | 0.78 |
| iOS 6.2.1 | 19,205 | 19,357 | 0.44 |
| Web (browser) | 21,939 | 21,987 | 0.82 |
| All except 5.1.4 | 48,329 | 48,563 | 0.45 |

Looking at Android 5.1.4 day by day:
- **3–4 August:** the split is balanced, about 490 users per group per day.
- **From 5 August:** treatment drops to about 40–55 users a day, while control stays at about 470. That is roughly 5,010 treatment users missing.

This looks like an event on 5 August, for example a crash, a page that fails to load, or a logging or assignment bug that affected only the new page on the old Android version. The data can't tell these apart. The ~10% of affected users who still appear are probably not a random subset of the group.

### Why this inflates the headline
Android 5.1.4 users convert at about 2.6%, against 5.5–7.3% for the other segments. Control keeps all its low converters; treatment loses most of them. Treatment's average therefore rises even if the page has no effect. This is a group-mix effect, not a change in behaviour.

In the two clean days (3–4 August), Android 5.1.4 shows no effect: control 2.32% (n = 992), treatment 2.32% (n = 950).

## Effect of the new page on the valid groups
These figures exclude Android 5.1.4; all remaining segments are balanced.

| Segment | Control CR | Treatment CR | Diff (pp) | 95% CI (pp) | p |
|---|---|---|---|---|---|
| **All valid users** | 6.33% | 6.50% | **+0.17** | −0.14 to +0.48 | 0.28 |
| iOS 6.2.1 | 6.88% | 7.32% | +0.44 | −0.07 to +0.95 | 0.09 |
| Android 5.3.2 | 5.47% | 5.78% | +0.31 | −0.45 to +1.06 | 0.42 |
| Web | 6.14% | 6.02% | −0.12 | −0.57 to +0.33 | 0.60 |

- **Adjusting for segment changes nothing.** A regression controlling for app version gives +0.17 pp (CI −0.14 to +0.48, p = 0.29).
- **Revenue:** revenue per user is $4.39 vs $4.34 (p = 0.64). Average order value among buyers is $67.6 vs $68.5 (p = 0.33), so there is no sign the page changes basket size.
- **Apps vs web:** in the apps, the point estimate is +0.41 pp (p = 0.06). On web it is flat to slightly negative. The difference between the two is not significant (interaction p = 0.10). Treat it as something to test again, not as a finding; it would also be one of several subgroup cuts, which raises the chance of a false positive.
- **Over time:** the daily differences go both ways around zero, with no clear trend over the two weeks.

### What the test could detect
With about 48k users per group and a ~6.3% baseline, the test had 80% power only for lifts of about **0.44 pp (about 7% relative)** or more. The data rule out a large lift. They do not rule out a real lift of about 2–5%, which could still be worth having commercially.

## Recommendations
1. **Do not ship on this evidence.** The +8.5% headline comes from the missing users. On valid data the lift is small and not significant.
2. **Treat the Android 5.1.4 drop-off as a possible production bug.** Check crash logs, page-load errors and assignment or exposure logging for the new page on 5.1.4 from 5 August. If the new page fails on that version, shipping it would hurt about 8% of users, who may be unable to check out at all.
3. **Fix the problem and re-run.** Add an automatic SRM check, overall and per platform and app version, with alerts in the first days of any test. At 80% power and α = 0.05, current traffic is about 48k valid users a week across both groups. To detect a 5% relative lift (+0.32 pp), the next test needs about 95k users per group, roughly 4 weeks. A 3% lift needs about 260k per group, roughly 11 weeks. That may be too long, so agree up front on the smallest lift worth detecting. Before starting, decide whether apps (iOS and Android) will be the primary analysis, since that is where any effect seems to be.
4. **Optional:** if the bug is fixed and the business is comfortable with a small, unproven upside, an app-only rollout as a holdout test would be reasonable. Pre-commit to the conversion metric and to revenue per user as a guardrail.

## Assumptions and limitations
- Each row is a user counted when they were assigned to the test. I assume the missing 5.1.4 treatment users were really assigned but never recorded or never reached the page; the data can't confirm this.
- I excluded Android 5.1.4 entirely rather than only from 5 August. The few treatment users who still appear after that date are probably a biased subset. Keeping all 5.1.4 users in a regression adjusted for app version (which removes most of the group-mix bias) does not change the conclusion: +0.16 pp, p = 0.29.
- Conversion is binary per user, and revenue includes zeros for non-buyers. Tests used are: two-proportion z-tests, Welch t-tests for revenue, and regression with robust standard errors for the adjusted estimates.
