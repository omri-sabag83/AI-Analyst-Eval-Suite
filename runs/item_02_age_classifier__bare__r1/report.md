# Age-Group Classifier v1: Evaluation and Deployment Recommendation

## Recommendation: do not deploy this version

The model is better than guessing, but it is not good enough to segment client data by age group. It gets **62% of profiles right** overall (95% bootstrap CI 59–65%). Among profiles that don't state their age in the bio, it gets only **55% right**. The bigger problem is that its errors all lean the same way: **it makes people look older than they are**. Any client report built on it would show too few Gen Z users and two to two-and-a-half times too many Gen X and Baby Boomer users. The confidence scores are also too high, so they can't be relied on to filter out bad predictions.

The model can probably be fixed. A simple model I built from the same profile fields, as a sanity check, did much better (see §5). The next step is to retrain, not to deploy.

---

## 1. Headline metrics (n = 1,000)

| Metric | Value |
|---|---|
| Accuracy | **62.0%** (CI 59–65%) |
| Baseline: always predict "Gen_z" | 45.8% |
| Balanced accuracy (average recall across classes) | 64.9% |
| Macro F1 | 0.55 |
| Cohen's kappa | 0.43 (moderate agreement) |

Confusion matrix (rows = actual, columns = predicted):

| Actual \ Predicted | Gen_z | Millennials | Gen_x | Baby Boomers | Total |
|---|---|---|---|---|---|
| **Gen_z** | **276** | 131 | 34 | 17 | 458 |
| **Millennials** | 38 | **265** | 85 | 13 | 401 |
| **Gen_x** | 4 | 25 | **45** | 29 | 103 |
| **Baby Boomers** | 0 | 2 | 2 | **34** | 38 |
| Total predicted | 318 | 423 | 166 | 93 | 1,000 |

Per class:

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Gen_z | 0.87 | 0.60 | 0.71 | 458 |
| Millennials | 0.63 | 0.66 | 0.64 | 401 |
| Gen_x | **0.27** | 0.44 | **0.34** | 103 |
| Baby Boomers | **0.37** | 0.90 | 0.52 | 38 |

When the model says a profile is Gen X, it is right only 27% of the time. For Baby Boomers it is right 37% of the time. These are exactly the small segments where clients most need reliable numbers.

## 2. The errors lean one way: the model makes people older

I treated the classes as an ordered scale (Gen Z < Millennials < Gen X < Boomers):

- **309 of the 380 errors (81%) predict an older group** than the truth. Only 71 predict a younger one.
- 40% of Gen Z users are put in an older group, including 17 labelled Baby Boomers.

This changes the segment sizes clients would see:

| Segment | True share | Share the model would report |
|---|---|---|
| Gen_z | 45.8% | **31.8%** (−14 pts) |
| Millennials | 40.1% | 42.3% |
| Gen_x | 10.3% | **16.6%** (×1.6) |
| Baby Boomers | 3.8% | **9.3%** (×2.4) |

In this sample, about 63% of users the model labels "Baby Boomer" are not Boomers. For the Gen X label it's about 73%. Insights attributed to older audiences would mostly reflect younger users' content.

## 3. Why: the model relies too much on hashtag stereotypes

Hashtags come in four fixed sets, and each set reads like a generational stereotype. The model's prediction matches the stereotype for **80%** of profiles. The true age group matches it for only **69%**:

| Hashtag set | What the model predicts | What users actually are |
|---|---|---|
| #career #familylife #retirement | Gen_x 140 / 180 | **Millennials 111**, Gen_x 42 |
| #classics #grandparents #history | Baby Boomers 85 / 98 | Boomers only 32. The rest are spread across Gen X 25, Gen Z 24, Millennials 17 |
| #trending #viral #yolo | Gen_z 296 / 423 | Gen_z 377 |
| #foodie #travel #workhard | Millennials 275 / 301 | Millennials 234 |

When the model goes against the stereotype, it is right only 32% of the time. It also ignores clear clues in the bio. Of the users whose bio starts with "Student.", it labelled 9 as Baby Boomers and 28 as Gen X, even though every Student is actually Gen Z or a Millennial.

## 4. The headline accuracy is flattered by easy cases

157 profiles (16%) state their age in the bio (e.g. "Age: 36."). The model gets **all 157 right**. On the other **843 profiles, accuracy is 54.9%**, against a 47% "always Gen Z" baseline. Balanced accuracy there is 58%, Gen X F1 is 0.23 and Boomer precision is 0.31. In production, most profiles will not state an age, so **55% is the more realistic figure**. (It's also worth asking how the "Actual Class" labels were created. If some of them came from stated ages, the evaluation would lean even further toward these easy cases.)

## 5. The confidence scores are too high

Confidence does go up with accuracy, but it consistently overstates it:

| Confidence band | n | Average confidence | Actual accuracy |
|---|---|---|---|
| 0.50–0.60 | 212 | 0.55 | 40% |
| 0.60–0.70 | 206 | 0.66 | 58% |
| 0.70–0.80 | 189 | 0.76 | 65% |
| 0.80–0.90 | 224 | 0.86 | 71% |
| 0.90–1.00 | 169 | 0.95 | 80% |

Expected calibration error is about 0.13, meaning confidence overstates accuracy by about 13 points on average. Keeping only predictions with confidence ≥ 0.8 drops 59% of profiles and still gives only 75% accuracy, so a confidence cutoff doesn't rescue the model.

**The signal is there; this version isn't using it well.** As a quick check, I fit a plain logistic regression on the same fields (hashtag set, bio prefix, gender, posts/likes rate, word count) and scored it with 5-fold cross-validation on this sample. It reached about **81% accuracy**, or 75% accuracy with 72% balanced accuracy when the classes are weighted equally, against the model's 62% / 65%. This is an in-sample, small-data check, not a replacement model. It does suggest a large improvement is realistic.

Other checks: accuracy is similar for women (60%) and men (65%). The gap mostly comes from female Gen Z users being pushed into older groups more often. This is worth watching, but it isn't the main problem.

## 6. What should happen next

1. **Retrain to correct the lean toward older groups.** Weight or resample the classes, and tune decision thresholds against a target such as macro F1 or per-segment precision, not raw accuracy.
2. **Use the bio properly.** Extract stated age and role keywords (Student, Retired, Grandparent, Parent, Senior Director) as features, and override the prediction when an age is stated. Rely less on hashtags: their stereotyped labels (e.g. #retirement) are misleading here.
3. **Recalibrate confidence** (e.g. temperature or isotonic scaling) so scores can drive an "unknown / low confidence" bucket, not forced labels.
4. **Correct segment sizes, not just individual labels.** For client reporting, adjust aggregate segment shares using the confusion matrix, so the totals aren't distorted even when individual predictions are noisy.
5. **Set acceptance criteria before the next review**, for example: accuracy ≥ 80% on profiles *without* a stated age, precision ≥ 0.6 for every segment, each segment's predicted share within ±3 points of the true share, and calibration error < 0.05. Evaluate on a larger held-out sample with more Gen X and Boomer users (only 103 and 38 here, so their metrics are uncertain).
6. **Document where the labels come from** and check for leakage between the label source and the bio's stated age.

## Assumptions and limitations
- I assumed `Actual Class` is correct ground truth and that this sample is representative of production traffic. Either could be wrong, especially the class mix, which was not specified.
- `Gender` is in the file but isn't one of the listed model inputs. I used it only for the fairness check and the baseline.
- The comparison logistic regression was fit and scored on this same 1,000-row sample (with cross-validation). It shows achievable headroom, not a production estimate.
- Small classes (Boomers n = 38) have wide uncertainty on their per-class metrics.
