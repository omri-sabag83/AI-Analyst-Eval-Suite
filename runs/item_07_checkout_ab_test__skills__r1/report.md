# Checkout page A/B test (3–16 Aug 2026): readout

## Bottom line
- **The headline lift is not real. It comes from a broken experiment.** A naive comparison shows treatment converting at 6.38% vs 5.88% for control (+0.50 pp, +8.5%, p < 0.001). That number is invalid: from 5 August, about 90% of treatment users on **Android app version 5.1.4** are missing from the data. These are the lowest-converting users (≈2.6% conversion), so losing them from treatment makes treatment look better than it is.
- **On the clean, balanced data, the new page shows no statistically significant effect on conversion:** +0.17 pp (6.50% vs 6.33%, +2.7% relative), 95% CI −0.14 to +0.48 pp, p = 0.28. Revenue per user is also flat ($4.39 vs $4.34, p = 0.64).
- **Recommendation: do not ship based on this test.** First, find out what happened to treatment users on Android 5.1.4. The new page may fail to load or crash on that version, or fail to log. Fix that, then rerun the test, or extend it, with sample-ratio monitoring turned on.

## 1. The experiment is broken: sample ratio mismatch
The design was a 50/50 split. The data has 54,898 control users and 50,080 treatment users (47.7% treatment). A chi-square test against 50/50 gives p ≈ 10⁻⁵⁰. That is far beyond what chance can explain.

The whole imbalance sits in one segment:

| Segment | Control | Treatment | Treatment share | SRM p-value |
|---|---|---|---|---|
| Android 5.1.4 | 6,569 | 1,517 | **18.8%** | ≈ 0 |
| Android 5.3.2 | 7,185 | 7,219 | 50.1% | 0.78 |
| iOS 6.2.1 | 19,205 | 19,357 | 50.2% | 0.44 |
| Web (browser) | 21,939 | 21,987 | 50.1% | 0.82 |

It also has a clear start date. For Android 5.1.4, treatment and control were balanced on 3–4 August (486 vs 507 and 464 vs 485). From 5 August on, treatment gets only about 40–55 users a day, against roughly 450–490 for control. All other segments stay at about 50% every day of the test (daily share range 49.2%–51.2%).

**Likely mechanism (hypothesis, not verified):** something changed on 5 August that stops treatment users on Android 5.1.4 from entering the dataset. Possible causes: the new page crashes or won't render on that old version, assignment or exposure logging fails for it, or a config or deploy change began filtering them out. Users who are never logged have no recorded outcome. If the new page is actually broken on 5.1.4, those users probably could not check out at all. That would be a real harm the data cannot show. **Engineering should check the client logs and crash reports for 5.1.4 around 5 August.**

## 2. Why the mismatch inflates the result
Android 5.1.4 users convert at about 2.6%, well below the roughly 6–7% of the other segments. Control kept all of them (12% of control users). Treatment kept only a few (3% of treatment users). The treatment group is therefore tilted toward higher-converting segments. That mix shift, not the page, creates most of the naive +0.50 pp.

Within every segment, the difference is small and not significant:

| Segment | Control CR | Treatment CR | Diff (pp) | 95% CI (pp) | p |
|---|---|---|---|---|---|
| Android 5.1.4 | 2.56% | 2.57% | +0.01 | −0.78 to +1.00 | 0.98 |
| Android 5.3.2 | 5.47% | 5.78% | +0.31 | −0.45 to +1.06 | 0.42 |
| iOS 6.2.1 | 6.88% | 7.32% | +0.44 | −0.07 to +0.95 | 0.09 |
| Web | 6.14% | 6.02% | −0.12 | −0.57 to +0.33 | 0.60 |

## 3. Clean estimates of the effect
I used three ways to remove the bias. They agree:

| Approach | Lift (pp) | 95% CI (pp) | p |
|---|---|---|---|
| Naive, all users (**invalid**) | +0.50 | +0.21 to +0.79 | 0.0007 |
| Exclude Android 5.1.4 (remaining groups pass SRM) | +0.17 | −0.14 to +0.48 | 0.28 |
| All users, adjusted for app version (regression) | +0.16 | −0.14 to +0.46 | 0.29 |
| 3–4 Aug only, before the breakage (all segments) | 0.00 | −0.75 to +0.75 | 0.99 |

Revenue per user (excluding 5.1.4): $4.34 control vs $4.39 treatment, p = 0.64. Average order value among converters is the same in both groups (about $68).

**What this means:** the best estimate is a small positive effect of about +0.17 pp (+2–3% relative). The data cannot rule out zero or a small negative effect. With about 48k users per arm and a 6.3% baseline, the test could reliably detect (80% power, α = 0.05) a lift of about 0.44 pp (≈7% relative). A real effect of +2–3% relative would need a test roughly 6–7× larger to detect.

**On iOS and Android apps:** excluding 5.1.4, app users show +0.41 pp (p = 0.06) and web shows −0.12 pp. These subgroup cuts were chosen after seeing the data, and the treatment × segment interaction terms are not significant (all p > 0.4). Treat this as a lead for the next test, not a finding.

## 4. Recommendations
1. **Don't ship on this evidence.** The claimed +8.5% lift comes from the data problem. The valid estimate is not significant.
2. **Diagnose Android 5.1.4 now.** If the new page breaks on that version, shipping it would hurt those roughly 8% of users. Their missing outcomes are exactly the data we can't see.
3. **Rerun after the fix**, with an automated daily SRM check per platform and version, and a sample size planned for the smallest lift that is worth having. If +2–3% matters, plan for about 300k+ users per arm or a longer test. Pre-register any web vs app split if you want to test it.
4. If the product team wants to ship anyway for non-conversion reasons (design consistency, maintenance), the data gives no sign of harm on web, iOS or Android 5.3.2. It still must not go to Android 5.1.4 until item 2 is resolved.

## Assumptions and notes
- Each row is one unique randomized user (no duplicate IDs, no missing values). `converted` and `revenue` are consistent: revenue > 0 exactly when converted = 1.
- The `app_version` value "browser" is the same as platform = web. iOS has a single version (6.2.1).
- Tests are two-sided at α = 0.05: two-proportion z-tests and Newcombe CIs for conversion, Welch t-tests for revenue, and OLS with robust standard errors for the version-adjusted estimate.
- Excluding Android 5.1.4 entirely assumes the remaining segments were not affected. Their per-day balance supports that, but it cannot be proven from this file alone.
