# Age-group classifier (v1): evaluation and deployment recommendation

## Recommendation: do not deploy v1 to production

The model gets **62% of profiles right**. That figure is inflated by easy cases. On profiles that don't state their age in the bio, which is most real users, accuracy falls to **55%**. The model does worst on the two smallest groups, and these are the segments clients are most likely to pay for:

- Of the profiles it labels **Baby Boomers**, only 37% really are.
- Of the profiles it labels **Gen X**, only 27% really are.

As a result, client segment counts would be badly distorted. Two simple baselines built from the same inputs do better than the model. Its problem is how it uses the inputs, not a lack of signal in the data, so a better v2 looks achievable with modest effort.

---

## 1. Headline performance (1,000 profiles)

| Metric | Value | 95% bootstrap CI |
|---|---|---|
| Accuracy | **62.0%** | 59–65% |
| Balanced accuracy (mean recall per class) | 64.9% | – |
| Macro F1 | 0.55 | 0.51–0.59 |
| Cohen's kappa | 0.43 (moderate agreement) | – |
| Always predict "Gen_z" (majority class) | 45.8% | – |

### Confusion matrix (rows = actual, columns = predicted)

| Actual \ Predicted | Baby Boomers | Gen_x | Gen_z | Millennials | Total |
|---|---|---|---|---|---|
| **Baby Boomers** | **34** | 2 | 0 | 2 | 38 |
| **Gen_x** | 29 | **45** | 4 | 25 | 103 |
| **Gen_z** | 17 | 34 | **276** | 131 | 458 |
| **Millennials** | 13 | 85 | 38 | **265** | 401 |
| **Total predicted** | 93 | 166 | 318 | 423 | 1,000 |

### Per-class results

| Class | Precision (share of predictions that are correct) | Recall (share of the true group found) | F1 |
|---|---|---|---|
| Baby Boomers | **0.37** | 0.89 | 0.52 |
| Gen_x | **0.27** | 0.44 | 0.34 |
| Gen_z | 0.87 | **0.60** | 0.71 |
| Millennials | 0.63 | 0.66 | 0.64 |

Precision CIs (bootstrap): Baby Boomers 27–46%, Gen X 20–34%. Even at the top of their ranges, these segments are mostly wrong.

## 2. What this means for clients

Clients receive segment-level data, so what matters is how pure each segment is and how large it appears.

- **Older segments are over-predicted and polluted.** The model labels 93 profiles as Baby Boomers, but only 38 exist, so the segment looks 2.4× its real size, and 63% of it is younger users. Gen X looks 1.6× too big (166 vs 103), and 73% of it is mainly Millennials (85) and Gen Z (34).
- **Gen Z is under-counted.** Only 318 profiles are predicted Gen Z out of 458 real ones. 40% of Gen Z users are missed, mostly moved into Millennials (131 profiles).
- Any insight a client draws about what Boomers or Gen X share would be driven mostly by younger users. That is the most damaging failure for a product sold on age segmentation.

## 3. Why the model performs this way

**a) The 62% is flattered by trivially easy profiles.** 157 of the 1,000 bios state an age explicitly (e.g. "Age: 34. …"). The model gets **all 157 right** (100%). On the other 843 profiles, accuracy is **54.9%**, macro F1 is 0.48, Gen X precision is 18%, and Baby Boomer precision is 31%. Most production users won't state an age, so **~55% is the realistic expectation**, not 62%.

**b) The model is mostly a hashtag lookup, and a worse one than the plain rule.** Every profile carries one of four hashtag sets. The model's prediction matches the "obvious" generation for its hashtag set in 80% of cases. The mapping is:

| Hashtag set | Obvious class |
|---|---|
| #yolo #viral #trending | Gen Z |
| #foodie #travel #workhard | Millennials |
| #career #familylife #retirement | Gen X |
| #classics #grandparents #history | Baby Boomers |

But the true labels follow that mapping less closely than the model does. For example, 111 of the 180 "#career/#familylife/#retirement" profiles are actually Millennials, yet the model calls 140 of them Gen X. Using the hashtag rule alone would score **68.5% accuracy (68% on profiles with no stated age)**, beating the model. In the 204 cases where the model departs from the hashtag rule, it is right only **32%** of the time.

**c) Useful signals are being underused.** Activity metrics differ clearly by generation:

| Actual group | Median posts/likes rate | Median avg. word count |
|---|---|---|
| Gen Z | 0.95 | 8 |
| Millennials | 1.14 | 9 |
| Gen X | 1.53 | 12 |
| Baby Boomers | 1.85 | 14 |

Bio keywords also help, for example "Student", "Grandparent", "Retired" and "Professor". I built a quick check on this same sample: a simple model using only hashtag set, bio keyword, stated age, posts/likes rate and word count. Under 5-fold cross-validation it reached **~81% accuracy (macro F1 0.67–0.70)**, against 62% / 0.55 for v1. This is an indicative ceiling, not a production model. It is trained on only 1,000 rows from the same sample, so expect it to be optimistic. Still, it shows there is a lot of headroom.

**d) Confidence scores carry information but overstate certainty.**

| Confidence band | Actual accuracy (all) | Actual accuracy (no stated age) |
|---|---|---|
| 0.50–0.60 | 40% | 32% |
| 0.60–0.70 | 58% | 48% |
| 0.70–0.80 | 65% | 59% |
| 0.80–0.90 | 71% | 64% |
| 0.90–1.00 | 80% | 76% |

Higher confidence does mean more likely correct (mean confidence is 0.78 when correct vs 0.70 when wrong). But scores are 10–20 points above the real hit rate in most bands. A "90% confident" prediction is right about 3–4 times in 4. A confidence cutoff alone does not rescue v1: even at ≥0.90, a quarter of non-trivial predictions are wrong.

## 4. What should happen next

1. **Hold v1 back from client-facing deployment.** If something must ship, limit it to a Gen Z vs. not-Gen Z flag (87% precision) and clearly mark it as experimental.
2. **Retrain with the existing inputs used properly.** Combine the hashtags with bio keywords, explicit stated ages, posts/likes rate and word count, rather than leaning almost entirely on hashtags. Deal with class imbalance: Baby Boomers are 3.8% and Gen X 10.3% of the sample. Use class weights or threshold tuning per class, and optimise for **per-class precision**, not raw accuracy.
3. **Use a hybrid rule for stated ages.** Where the bio gives an age, map it straight to the generation. The model already does this perfectly; make it an explicit rule so it can't regress.
4. **Calibrate confidence**, e.g. with isotonic or Platt scaling on a held-out set. Then use it to abstain on low-confidence profiles ("age unknown") instead of forcing a label. Reporting a smaller but cleaner segment is better for clients than a large, polluted one.
5. **Set acceptance criteria before v2 is evaluated.** As a suggestion: ≥75% precision in every class on profiles **without** a stated age, plus segment sizes within ±15% of the truth. Evaluate on a fresh, held-out, representative sample. Report results separately for profiles with and without a stated age, and include the hashtag-only baseline as a floor the model must beat.
6. **Check label and data quality.** The class cut-offs implied by stated ages overlap: age 28 appears as both Gen Z and Millennial. Confirm how "Actual Class" was determined and whether the generation boundaries are consistent. Also confirm the sample is representative. There are only four hashtag sets and a few dozen template bios, which suggests synthetic or heavily templated data, so real-world performance may differ.

## Assumptions and limitations

- I took `Actual Class` as ground truth and assumed the 1,000 profiles are representative of production traffic and were not used to train v1.
- The "~81% achievable" figure comes from cross-validation on this same small sample, using the same features available to v1. It shows headroom, not a guaranteed v2 result.
- The `Gender` field was not part of the stated model inputs, so I did not use it. Accuracy is similar by gender (60% female, 65% male), and gender often looks inconsistent with first names, which is another sign the data may be synthetic.
