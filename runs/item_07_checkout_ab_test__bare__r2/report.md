# Checkout page A/B test (3–16 Aug 2026): readout

## Bottom line
- **The headline result is not valid.** The raw numbers show treatment converting at 6.38% against 5.88% for control (+8.5% relative, p < 0.001). That lift comes from a data and tracking defect, not from the new page.
- **On the valid part of the data, we can't detect a lift.** Treatment converted at 6.50% and control at 6.33%: +0.17 percentage points (pp), or +2.7% relative. The 95% confidence interval is −0.14 pp to +0.48 pp and p = 0.28. Revenue per user is also flat: $4.39 vs $4.34, p = 0.64.
- **Recommendation: don't ship on the strength of this test.** First fix the Android app 5.1.4 problem described below. Then either re-run the test with enough users to detect the lift you care about, or ship only if the new page is wanted for other reasons and "no evidence of harm" is good enough.

## 1. The randomisation is broken (sample ratio mismatch)
Users were meant to be split 50/50. The data has 54,898 control users and 50,080 treatment users. A chi-square test against a 50/50 split gives p ≈ 10⁻⁵⁰, so chance can't explain the gap. The whole shortfall is in one segment:

| Segment | Control | Treatment | Balanced? |
|---|---|---|---|
| Android app 5.1.4 | 6,569 | 1,517 | **No** |
| Android app 5.3.2 | 7,185 | 7,219 | Yes (p = 0.78) |
| iOS app 6.2.1 | 19,205 | 19,357 | Yes (p = 0.44) |
| Web | 21,939 | 21,987 | Yes (p = 0.82) |

Android 5.1.4 was balanced on 3–4 Aug (about 490 users per arm per day). **From 5 Aug onward, treatment collected only about 40–55 users per day against about 470 in control.** About 90% of the 5.1.4 treatment users from that point are missing. The likely cause is that the new checkout page breaks, or fails to log, on that old app version. This needs engineering investigation, because it could mean real 5.1.4 users can't reach checkout.

**Why this inflates the result:** Android 5.1.4 users convert at only about 2.6%, the lowest of any segment. Removing most of them from treatment alone makes treatment's user mix more favourable, so its overall conversion rate rises even if the page itself does nothing. The same effect explains the implausible "+28% lift on Android" that appears if all Android users are pooled.

## 2. Valid comparison: excluding Android 5.1.4
I removed Android 5.1.4 from both arms. The remaining 96,892 users are balanced (48,563 treatment vs 48,329 control, SRM p = 0.45).

| Metric | Control | Treatment | Difference (95% CI) | p |
|---|---|---|---|---|
| Conversion | 6.33% | 6.50% | +0.17 pp (−0.14 to +0.48), +2.7% relative | 0.28 |
| Revenue per user | $4.34 | $4.39 | +$0.06 | 0.64 |

Checks on this result:
- **By segment:** iOS shows +0.44 pp (p = 0.09), Android 5.3.2 shows +0.31 pp (p = 0.42) and web shows −0.12 pp (p = 0.61). None is significant. Without a pre-registered hypothesis, the iOS result should be treated as a lead to follow up, not a finding.
- **Adjusted for the platform mix:** the lift is +0.17 pp, the same as the unadjusted figure.
- **Over time:** week 1 shows +0.18 pp and week 2 shows +0.16 pp. The effect is steady, with no novelty spike and no decay.
- **Clean days only (3–4 Aug, all users, before the defect started):** the lift is −0.0 pp, with a wide confidence interval.
- **Android 5.1.4 itself:** among the treatment users who were recorded, conversion matches control (2.57% vs 2.56%). However, those users are a self-selected group (the ones who got through), so this comparison can't be trusted.
- **Average order value** is essentially unchanged (about $68 in both arms).

## 3. What the data can and can't rule out
- The confidence interval on the relative lift runs from about −2% to +8%. A meaningful negative effect is unlikely. A small positive effect is possible.
- With about 48k users per arm and a baseline of 6.3%, the test could reliably detect (80% power, α = 0.05) only a lift of about 0.44 pp, roughly +7% relative. Smaller lifts would go undetected. If the team cares about a 2–3% lift, this test was too small to find it.

## Recommendations
1. **Don't claim the +8.5% result.** It is an artefact of the Android 5.1.4 defect.
2. **Fix the Android 5.1.4 issue before any rollout.** Find out whether the new page crashes, fails to load or fails to log on that version. If 5.1.4 users really can't reach the new checkout, shipping would lose sales from that segment. Alternatively, keep 5.1.4 on the old page or require users to upgrade.
3. **Decide the minimum lift worth shipping for, and re-test.** If that minimum is about 2–3%, a re-run needs roughly 4–8 times this sample, or a variance-reduction method such as CUPED that adjusts for each user's pre-test behaviour. Add an automatic sample-ratio check and per-segment alerting so a defect like this is caught within a day.
4. **If the team wants to ship anyway** (for design or maintenance reasons), the evidence supports "no detectable harm" on web, iOS and Android 5.3.2. It doesn't support "increases conversion". Exclude Android 5.1.4 until it is fixed.

## Assumptions and notes
- I assumed one row equals one randomised user and that `converted` and `revenue` measure outcomes over the test window. Revenue is greater than 0 exactly when `converted` = 1, which is consistent with this.
- I assumed the users missing from Android 5.1.4 treatment were lost because of the treatment and not randomly. The day-by-day pattern supports this: balanced on the first two days, then about a 90% shortfall in treatment only.
- Tests used are a two-proportion z-test for conversion, Welch's t-test for revenue per user, and a chi-square test for the sample ratio.
