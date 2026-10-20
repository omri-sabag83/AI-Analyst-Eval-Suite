# Age-group classifier v1: evaluation and deployment recommendation

## Recommendation: not ready for production

On the 1,000-profile sample the model gets **62% of profiles right** (95% bootstrap CI 59–65%). For 4 classes that is not good enough. The bigger problem is *where* it goes wrong. The two older segments are mostly wrong: **63% of profiles labelled "Baby Boomers" and 73% labelled "Gen X" belong to other generations.** The model also undercounts Gen Z by about 30%. Clients buy data split by age group, so they would get segments that are mostly mislabelled and segment sizes that are badly off. The model's confidence score cannot be used to filter out the bad predictions either. The model needs another iteration, and some of the fixes are clear (see "What should happen next").

## Data and assumptions
- One sheet, 1,000 rows, one row per user, no missing values or duplicate users. `Actual Class` is treated as ground truth.
- The true class mix is unbalanced: Gen Z 458, Millennials 401, Gen X 103, Baby Boomers 38. Because of this I report per-class and macro-averaged results, not just overall accuracy.
- I assume the sample represents the profiles the model will see in production. The share of profiles that state their age in the bio matters a lot here (see Finding 4).
- The `Gender` column often contradicts the first name (e.g. "Nina Adams – Male"). The model doesn't use this field, but it suggests the data is synthetic or loosely curated. Treat the numbers as indicative.

## Findings

### 1. Overall performance is modest
| Metric | Value |
|---|---|
| Accuracy | 62.0% (CI 59–65%) |
| Macro F1 | 0.55 (CI 0.51–0.59) |
| Cohen's kappa | 0.43 (moderate agreement) |
| Baseline: "always predict Gen Z" | 45.8% |

### 2. The older segments are unreliable, and segment sizes are distorted
| Class | True n | Predicted n | Precision | Recall | F1 |
|---|---|---|---|---|---|
| Gen Z | 458 | 318 | 0.87 | 0.60 | 0.71 |
| Millennials | 401 | 423 | 0.63 | 0.66 | 0.64 |
| Gen X | 103 | 166 | **0.27** | 0.44 | 0.34 |
| Baby Boomers | 38 | 93 | **0.37** | 0.90 | 0.52 |

Confusion matrix (rows = actual, columns = predicted):

| | BB | Gen X | Gen Z | Mill. |
|---|---|---|---|---|
| **Baby Boomers** | 34 | 2 | 0 | 2 |
| **Gen X** | 29 | 45 | 4 | 25 |
| **Gen Z** | 17 | 34 | 276 | 131 |
| **Millennials** | 13 | 85 | 38 | 265 |

- The model pushes people into older classes than they are. It predicts 2.4× as many Boomers as exist and 1.6× as many Gen X. The two largest error cells are Gen Z → Millennials (131) and Millennials → Gen X (85).
- What this means for clients: a "Gen X" report would be about 51% Millennials and 20% Gen Z. A "Boomer" report would be 63% other generations. Only the Gen Z segment is reasonably pure (87%), and it misses 40% of real Gen Z users.

### 3. Confidence scores don't help
| Confidence | n | Actual accuracy |
|---|---|---|
| 0.50–0.60 | 212 | 40% |
| 0.60–0.70 | 206 | 58% |
| 0.70–0.80 | 189 | 65% |
| 0.80–0.90 | 224 | 71% |
| 0.90–1.00 | 169 | 80% |

- The scores do rank predictions in the right order, but they are overconfident by 8–15 points in every band. Their ability to separate right from wrong predictions is weak (AUC 0.66).
- Only keeping predictions with confidence ≥ 0.9 keeps 20% of profiles and still gets only 78% of them right. A threshold can't rescue the model.

### 4. The headline accuracy is flattered by profiles that state their age
- 157 profiles (16%) have "Age: NN" in their bio. The model is **100% correct on these** and **55% correct on the other 843** (Gen X precision 0.18, Boomer precision 0.31, macro F1 0.48).
- Most real Instagram users don't write their age in their bio. If production has fewer of these profiles than the sample does, real accuracy will be closer to **55% than 62%**. This is the most important caveat for the deployment decision.
- (The stated ages agree with the labels in 155 of 157 cases. The two exceptions are age 28, right on the Gen Z / Millennial boundary, so the labels look sound.)

### 5. Why it fails: hashtags are over-trusted and mapped to the wrong group
Each profile has one of four fixed hashtag sets. The model mostly follows them. Its prediction matches the "intended" age group of the hashtag set 80% of the time. But that mapping is wrong for one set and too strong for another:

| Hashtag set | Profiles | Actual majority | Model mostly predicts | Model accuracy |
|---|---|---|---|---|
| #career #familylife #retirement | 180 | **Millennials (62%)**; Gen X only 23% | Gen X (140) | 38% |
| #classics #grandparents #history | 98 | Boomers only 33% | Boomers (85) | 41% |
| #foodie #travel #workhard | 299 | Millennials (78%) | Millennials | 79% |
| #trending #viral #yolo | 423 | Gen Z (89%) | Gen Z, but 110 sent to Millennials | 65% |

The model also ignores clear signals in the bio. "Student" profiles are 73% Gen Z and 27% Millennial, yet the model labels 40 of them Gen X/Boomer. "Grandparent" profiles are 100% Boomer, "Professor" 100% Gen X, and "Senior Director" 80% Millennial, and the model handles these inconsistently.

### 6. There is clear room to improve (indicative)
- A one-line rule, "predict the most common true age group for each hashtag set", gets **75.4%** on this sample, compared with the model's 62%.
- A simple logistic regression on hashtag set, bio keywords, post/likes rate and word count, with 5-fold cross-validation on this sample, reaches **~80% accuracy / 0.66 macro F1**.
- Caveat: these baselines are fitted and scored on the same 1,000 profiles, so they are optimistic. They show headroom, not a production estimate. Still, the gap is large enough to say v1 is under-using the inputs it already has.

## What should happen next
1. **Don't deploy v1 for age-segmented client deliverables.** If something has to ship, only Gen Z is usable, as a high-precision but incomplete segment (87% precision, 60% recall), and it should be clearly marked as such.
2. **Fix the obvious modelling problems:** re-learn how hashtags map to age from data instead of from assumed meanings (#retirement/#career/#familylife is mainly Millennial). Add bio keywords (Student, Grandparent, Professor, Senior Director, Parent, Retired) and stated age as features. Handle class imbalance with class weights or resampling so Gen X and Boomers aren't over-predicted.
3. **Calibrate the confidence scores** (e.g. Platt or isotonic scaling on a held-out set) so a stated 0.9 really means about 90%.
4. **Re-evaluate on a proper held-out set** that reflects production: realistic share of stated-age bios, realistic generation mix, and more Gen X/Boomer examples (only 38 Boomers here, so their metrics are noisy). Report results with and without stated-age profiles.
5. **Agree acceptance criteria with the business before the next round.** For example: per-segment precision ≥ 0.75 for every age group a client can buy, error in predicted segment size within ±10%, and a calibrated confidence score. If a segment can't meet the bar, it shouldn't be sold.
6. Since segment *sizes* are a product in their own right, consider correcting predicted counts with the confusion matrix when reporting aggregate shares.
