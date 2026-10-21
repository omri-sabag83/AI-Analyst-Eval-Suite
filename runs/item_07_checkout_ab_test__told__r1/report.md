# Checkout page A/B test (3–16 Aug 2026): readout

## Bottom line

**Don't ship the new checkout page yet on the claim that it increases conversion.**

- **Why the topline looks good:** it shows +0.50 percentage points (pp), or +8.5%, with p < 0.001. That result is an artefact of a data problem. About 5,000 treatment users on one old Android app version (5.1.4) are missing from the data from 5 August on. Those users convert at a low rate, so dropping them makes treatment look better than it is.
- **The real comparison:** in the part of the test where the random split is intact, the new page shows **+0.17pp (+2.7%), 95% CI −0.14 to +0.48pp, p = 0.28**. The revenue-per-user difference is +$0.06 (p = 0.64). That is not a demonstrated improvement.
- **It is not proof the page is worse either.** The page is roughly neutral, and the test cannot rule out a small gain. It also cannot rule out a small loss.
- **Before any decision:** find out why the Android 5.1.4 treatment users disappeared. If the new page fails on that app version, that alone blocks shipping.

## Data and method

- **Grain and coverage:** `experiment_users.csv` has one row per user, 104,978 users in total. Users were assigned over 14 complete days (3–16 Aug 2026), about 7,300–8,000 per day. There are no nulls and no duplicate user IDs.
- **Conversion and revenue agree:** every converter has revenue above zero (mean $67.93) and every non-converter has $0.
- **Segments:** web (browser) has 43,926 users, iOS app 6.2.1 has 38,562, Android 5.3.2 has 14,404 and Android 5.1.4 has 8,086. Each platform has one app version, except Android, which has two.
- **Tests used:** two-proportion z-tests for conversion and Welch-type tests for revenue per user. I checked robustness with logistic regression (adjusting for app version and assignment date) and with estimates stratified by app version.
- **Assumption:** "conversion" means `converted = 1` at the user level, and the test is meant to be read on all users.

## Finding 1: the randomisation is broken, and only in one segment

The design is a 50/50 split, but the data has **54,898 control vs 50,080 treatment users**. The chance of a gap this large under a true 50/50 split is about 5×10⁻⁵⁰ (a sample ratio mismatch, or SRM).

The gap sits entirely in one segment on one set of days:

| Segment | Control n | Treatment n | Treatment share | SRM p-value |
|---|---|---|---|---|
| Web (browser) | 21,939 | 21,987 | 50.1% | 0.82 |
| iOS 6.2.1 | 19,205 | 19,357 | 50.2% | 0.44 |
| Android 5.3.2 | 7,185 | 7,219 | 50.1% | 0.78 |
| **Android 5.1.4** | **6,569** | **1,517** | **18.8%** | ≈0 |
| – 5.1.4, 3–4 Aug | 992 | 950 | 48.9% | 0.34 |
| – 5.1.4, 5–16 Aug | 5,577 | **567** | 9.2% | ≈0 |

- **[OBS]** From 5 August, Android 5.1.4 treatment users fall from about 475 a day to 40–56 a day. Control on 5.1.4 stays at about 470 a day. About 5,000 expected treatment users (roughly 90%) are missing.
- **[OBS]** Every other segment is balanced on every day.
- **[HYP]** The data can't say why. Two likely explanations:
  - A tracking or assignment bug for the new page on 5.1.4 that started on 5 August, for example a release or config change.
  - The new page fails to load or crashes on 5.1.4, so those users never record an exposure.

  To settle it, pull 5.1.4 assignment-service logs, client error and crash logs, and the deploy/config history for 4–5 August.

## Finding 2: the headline lift is mostly a mix effect from the missing users

Android 5.1.4 users convert at **2.6%**, against 5.5–6.9% in the other segments. With most of them gone from treatment only, treatment's user mix tilts toward higher-converting segments.

| Analysis | Control CR | Treatment CR | Lift (pp) | 95% CI | p |
|---|---|---|---|---|---|
| Naive, all users (invalid) | 5.88% | 6.38% | +0.50 (+8.5%) | +0.21 to +0.79 | 0.0007 |
| Excluding Android 5.1.4, both arms (SRM p = 0.45) | 6.33% | 6.50% | **+0.17 (+2.7%)** | −0.14 to +0.48 | 0.28 |
| Stratified by app version (5.1.4 from 3–4 Aug only) | – | – | +0.15 | ±0.30 | ~0.32 |
| Logistic regression, adjusted for version and date (excl. 5.1.4) | – | – | odds ratio 1.03 | 0.98–1.08 | 0.28 |

- **[OBS] Split of the naive +0.50pp:** about **+0.35pp comes from the shift in user mix** and about **+0.15pp from actual differences in conversion within segments**.
- **[OBS] Revenue per user, clean population:** +$0.06 (CI −$0.18 to +$0.30, p = 0.64). The naive figure was +$0.29 (p = 0.01).
- **[OBS] Average order value among converters (excl. 5.1.4):** $67.58 for treatment vs $68.47 for control (p = 0.33). There is no difference.
- **[OBS] Stable over time:** the clean-population lift is +0.18pp in week 1 and +0.16pp in week 2. The small positive estimate is not a novelty spike, and it does not change over the test.

## Finding 3: by segment, nothing is conclusive

| Segment (clean) | Control n / CR | Treatment n / CR | Lift | p |
|---|---|---|---|---|
| iOS 6.2.1 | 19,205 / 6.88% | 19,357 / 7.32% | +0.44pp (+6.4%) | 0.09 |
| Android 5.3.2 | 7,185 / 5.47% | 7,219 / 5.78% | +0.31pp | 0.42 |
| Web | 21,939 / 6.14% | 21,987 / 6.02% | −0.12pp | 0.61 |
| Android 5.1.4, 3–4 Aug only | 992 / 2.32% | 950 / 2.32% | 0.00pp | 1.00 |

- **[OBS]** The app segments lean positive and web leans slightly negative. However, the treatment × platform interaction terms are not significant (p = 0.34 and 0.91).
- **[HYP]** "It works in the app but not on web" is a lead worth testing, not a finding. iOS alone at p = 0.09 would not survive the fact that several segments were examined.

## How much the test can tell us

- **What it could detect:** with about 48,000 users per arm in the clean population and a 6.3% baseline, the test had 80% power to detect about **+0.44pp (≈ +7% relative)**.
- **What it rules out:** the new page very likely does **not** lift conversion by more than about 0.5pp.
- **What it cannot settle:** whether the effect is a small gain (up to about +0.48pp), zero, or a small loss (down to about −0.14pp).
- **Value of the point estimate [estimate, not a measured gain]:** +0.17pp would be about 2.7% more orders, on the assumption that it holds after launch. The test cannot tell that apart from zero.

## Recommendations

1. **Don't ship on the basis of this test's headline.** The significant +8.5% lift comes from the data defect. With the defect removed, conversion and revenue per user show no significant change.
2. **Investigate Android 5.1.4 first.** Determine whether the missing treatment users are a logging/assignment bug or real failures of the new page on that app version.
   - **If the page breaks on 5.1.4:** fix it, or exclude 5.1.4 from any rollout. Those users may have been unable to check out at all, so the true effect for them could be negative.
   - **If it's a tracking bug:** fix it and add an automated sample-ratio check to the experiment pipeline, so a test is flagged on day one rather than after it ends.
3. **If the team still believes in the page, run it again once the fix is in.**
   - Pre-register conversion as the primary metric.
   - Run SRM checks daily.
   - Size the test for the effect worth shipping. Detecting about +0.2pp (≈ 3% relative) at 80% power needs roughly 230,000 users per arm, about 4–5× this test.
   - Optionally pre-register an app-vs-web comparison to test the iOS/Android lean.
4. **If the page has other benefits** (maintainability, accessibility, brand), shipping it as a neutral change is defensible, but only after the 5.1.4 issue is resolved. Don't present it as a conversion win.

## Checks performed

- **Rigor checklist:** I ran an analytical-rigor checklist on the draft. It led me to add the mix-vs-rate split of the lift, the power and smallest-detectable-effect statement, and the revenue/conversion consistency check. It also led me to use only 3–4 Aug for the 5.1.4 stratum, because the few 5.1.4 treatment users recorded after 5 Aug are probably not a random subset.
- **Independent check:** a separate agent saw only the raw CSV and the central claim, not my reasoning. Its verdict was **HOLDS**:
  - It reproduced the naive +0.50pp (p = 0.0007).
  - It confirmed the imbalance is confined to Android 5.1.4 treatment from 5 August (5,577 control vs 567 treatment).
  - It found every other segment and day balanced.
  - It estimated the lift on the intact population at +0.16 to +0.17pp, not significant (p ≈ 0.27–0.28).
