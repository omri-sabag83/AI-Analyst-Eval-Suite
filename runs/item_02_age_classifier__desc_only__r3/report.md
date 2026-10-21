# Age-group classifier v1: evaluation and deployment recommendation

## Recommendation: do not deploy v1 yet

The model gets **62% of profiles right** (95% CI 59–65%). It is badly wrong on the two older groups and makes the age mix it reports look older than it is. Clients buy age *segments*, so the most important problem is this: if the model were used on this sample as it stands, it would report:

| Segment | True share | Share the model reports | Distortion |
|---|---|---|---|
| Gen_z | 45.8% | 31.8% | under-counted by 14 pts |
| Millennials | 40.1% | 42.3% | about right (but see errors below) |
| Gen_x | 10.3% | 16.6% | over-counted 1.6× |
| Baby Boomers | 3.8% | 9.3% | over-counted 2.4× |

Of the profiles the model labels Gen_x, 73% are not Gen_x. Of those it labels Baby Boomers, 63% are not Baby Boomers. Any insight a client draws about "what Gen X / Boomers share on Instagram" would mostly reflect what younger users share.

The fixes look achievable. A simple model I built on the same inputs reaches about 75–80% accuracy (details below). So the next step is a targeted v2, not dropping the approach.

---

## 1. Overall performance (1,000 labelled profiles)

| Metric | Value |
|---|---|
| Accuracy | **62.0%** (bootstrap 95% CI 59–65%) |
| Balanced accuracy (average recall over the four groups) | 64.9% |
| Macro F1 | 0.55 (CI 0.51–0.59) |
| Cohen's kappa (agreement beyond chance) | 0.43 (moderate) |
| Baseline: always predict "Gen_z" | 45.8% |

**Confusion matrix** (rows = actual, columns = predicted)

| Actual \ Predicted | Gen_z | Millennials | Gen_x | Baby Boomers | Total |
|---|---|---|---|---|---|
| Gen_z | **276** | 131 | 34 | 17 | 458 |
| Millennials | 38 | **265** | 85 | 13 | 401 |
| Gen_x | 4 | 25 | **45** | 29 | 103 |
| Baby Boomers | 0 | 2 | 2 | **34** | 38 |

**Per-class results**

| Class | Precision | Recall | F1 | n |
|---|---|---|---|---|
| Gen_z | 0.87 (CI 0.83–0.90) | 0.60 (0.56–0.65) | 0.71 | 458 |
| Millennials | 0.63 (0.58–0.68) | 0.66 (0.62–0.71) | 0.64 | 401 |
| Gen_x | **0.27** (0.20–0.34) | 0.44 (0.34–0.53) | 0.34 | 103 |
| Baby Boomers | **0.37** (0.28–0.46) | 0.89 (0.79–0.98) | 0.52 | 38 |

How the errors run: the model consistently pushes people into **older** groups. 40% of Gen Z users are labelled older, mostly as Millennials (131). 24% of Millennials are labelled older, mostly as Gen X (85). Gen X users are often labelled Boomers (29). Almost no one is labelled younger than they are. That pattern is what produces the skewed segment shares above.

## 2. Why it fails: what drives the errors

**a) The model mostly copies the hashtags.** Each profile has one of four hashtag sets. Each set lines up with a generation: #yolo/#viral/#trending → Gen Z; #travel/#workhard/#foodie → Millennials; #career/#familylife/#retirement → Gen X; #history/#classics/#grandparents → Boomers. The model's prediction equals the "hashtag generation" for **79.6%** of profiles. But hashtags match the true generation for only 68.5% of users:

| Profiles where hashtags… | n | Model accuracy | Mean confidence |
|---|---|---|---|
| match the true generation | 685 | 81% | 0.74 |
| do **not** match | 315 | **21%** | 0.76 |

When the hashtags are misleading, the model still follows them 77% of the time, and it is just as confident as when it is right. Example: 111 true Millennials use the career/family/retirement tags, and the model mostly calls them Gen X. Most of the over-ageing comes from this.

**b) The model under-uses the other signals it has.**
- *Bio:* "Student" appears only on Gen Z and Millennials, never on older users. "Grandparent" appears only on Boomers. "Retired" appears only on Gen X and Boomers.
- *Writing style:* average word count rises with age (median 8 for Gen Z → 14 for Boomers). So does the posts-to-likes ratio (median 0.95 → 1.85).

A model that weighed these properly would catch many of the hashtag-misleading cases.

**c) The headline accuracy is flattered by easy cases.** 157 profiles (16%) state their age in the bio ("Age: 24."). The model gets all of them right. On the other 843 profiles, which is the real test, accuracy is **54.9%** and macro F1 is **0.48**. In production, how often bios state an age will set the accuracy you actually see. If real users state their age less often than this sample does, accuracy will be lower.

## 3. Confidence scores can't be used as-is to filter out bad predictions

Higher confidence does go with higher accuracy, but the scores are overconfident at every level:

| Confidence band | n | Mean confidence | Actual accuracy |
|---|---|---|---|
| 0.50–0.60 | 212 | 0.55 | 40% |
| 0.60–0.70 | 206 | 0.66 | 58% |
| 0.70–0.80 | 189 | 0.76 | 65% |
| 0.80–0.90 | 224 | 0.86 | 71% |
| 0.90–1.00 | 169 | 0.95 | 80% |

Keeping only predictions with confidence ≥ 0.8 raises accuracy to 75%, but throws away 59% of profiles. Even at ≥ 0.9, one prediction in five is wrong. A cut-off won't make v1 fit for purpose, though recalibrating the scores (e.g. temperature or isotonic scaling) would be worthwhile in v2.

## 4. Other checks

- **Gender:** Gender is not listed as a model input. Accuracy is 60% for profiles marked female and 65% for male. The error pattern is the same for both, and the gap is within sampling noise for groups this size. No clear bias found, but keep monitoring it.
- **Small classes:** with only 103 Gen X and 38 Boomer profiles, the figures for those groups are uncertain (wide CIs above). Even so, the best case for Gen X precision (34%) is still unacceptable.

## 5. Evidence that a better model is within reach

As a quick benchmark, I fitted simple models on the **same public inputs**: hashtag set, word count, posts/likes ratio, bio keywords, and stated age where present. I used 5-fold cross-validation on this sample:

| Model | Accuracy | Macro F1 | Balanced accuracy |
|---|---|---|---|
| Current v1 | 62.0% | 0.55 | 64.9% |
| Logistic regression (class-weighted) | 75.4% | 0.66 | 73.5% |
| Gradient boosting | 80.6% | 0.68 | 66.3% |

Treat these as rough indications, not production estimates. The sample is small and is the same one used to diagnose the problems, and I engineered the features after looking at the data. Still, they show that a large share of v1's errors can be fixed with the information it already has.

## 6. What should happen next

1. **Hold the release.** Agree acceptance criteria with the client-facing team before v2. For example: per-class precision ≥ 0.70 for every segment, and each segment's reported share within ±2 points of its true share, both measured on profiles **without** a stated age.
2. **Retrain to rely less on hashtags.** Give proper weight to bio keywords (Student, Retired, Grandparent, Parent, Senior Director), word count and posts/likes ratio. Use class weighting or resampling so Gen X and Boomers aren't swamped by the two big groups. Then recalibrate the confidence scores.
3. **Report segment shares corrected for known errors.** If anything ships before v2, don't publish raw predicted shares. Correct them using the error rates in the confusion matrix, or report only aggregate patterns with clear uncertainty.
4. **Build a better evaluation set.** Use more labelled Gen X and Boomer profiles (aim for several hundred each), drawn to match the real production population. Keep it separate from training data, and report results with and without stated-age profiles.
5. **Monitor after launch.** Track the predicted class mix, the share of bios that state an age, and accuracy on a regularly relabelled audit sample.

## Assumptions and limitations

- I assumed `Actual Class` is reliable ground truth. Where an age is stated in the bio, it is always consistent with the label (Gen Z 15–28, Millennials 28–43, Gen X 44–59, Boomers 63–72).
- I assumed the 1,000 profiles are a fair sample of what the model will see in production. Its class mix (46% Gen Z, 4% Boomers) and its share of stated ages may not be. Both affect the accuracy you would actually get.
- I don't know whether the sample overlaps the model's training data. If it does, true performance is likely *worse* than reported here.
- No business accuracy target was provided. The recommendation rests on the size of the segment-share distortion and the low Gen X / Boomer precision, not on a single threshold.
