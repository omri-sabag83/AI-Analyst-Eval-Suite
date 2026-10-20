# Age-group classifier (v1): evaluation and deployment recommendation

## Bottom line

**Do not deploy v1 to production.** The model's labels are correct for **62%** of the 1,000 sample profiles. That figure is inflated: 157 of the profiles state the user's age in the bio, and the model gets every one of those right. On the other 843 profiles, which are the cases a model is actually needed for, accuracy is **55%**.

Three further problems:

- A simple rule based only on the hashtags beats the model (**75%**).
- The model is worst on exactly the segments clients are likely to buy as niche audiences. Profiles labelled Gen X are 73% wrong, and profiles labelled Baby Boomers are 63% wrong.
- The confidence score cannot be used to filter out bad predictions for those segments.

A quick benchmark model built on the same inputs reached about **81%** in cross-validation. That suggests the inputs carry enough signal and the problem lies in v1 itself, so the next version can probably be fixed rather than redesigned.

## Data and assumptions

- `model_evaluation_sample.xlsx` has 1,000 profiles and no missing values. The true class mix is Gen Z 458, Millennials 401, Gen X 103 and Baby Boomers 38.
- I assume `Actual Class` is reliable ground truth, and that the sample was not used to train v1.
- I assume the sample's class mix resembles production traffic. If it doesn't, accuracy in production will differ. In particular, it will be worse if older users make up a bigger share.
- `Gender` is in the file but is not one of the model's stated inputs. I used it only to check whether the model works equally well for women and men.

## Findings

### 1. Overall performance is weak

| Metric | Value |
|---|---|
| Accuracy | 62.0% |
| Balanced accuracy (average recall across the four classes) | 64.9% |
| Macro-F1 | 0.55 |
| Cohen's kappa | 0.43 (moderate agreement) |
| Baseline: always predict "Gen Z" | 45.8% |

Confusion matrix (rows = actual, columns = predicted):

| Actual \ Predicted | Gen Z | Millennials | Gen X | Baby Boomers | Recall |
|---|---|---|---|---|---|
| Gen Z (458) | **276** | 131 | 34 | 17 | 60% |
| Millennials (401) | 38 | **265** | 85 | 13 | 66% |
| Gen X (103) | 4 | 25 | **45** | 29 | 44% |
| Baby Boomers (38) | 0 | 2 | 2 | **34** | 89% |
| **Precision** | 87% | 63% | 27% | 37% | |

The model systematically predicts users to be older than they are. 309 profiles are placed in an older group than their true one, compared with 71 placed in a younger group. As a result the sizes of the client segments come out wrong:

| Segment | True share | Predicted share | Share of the predicted segment that is correct |
|---|---|---|---|
| Gen Z | 45.8% | 31.8% | 87% |
| Millennials | 40.1% | 42.3% | 63% |
| Gen X | 10.3% | 16.6% | **27%** |
| Baby Boomers | 3.8% | 9.3% | **37%** |

A client who buys "Gen X insights" would get a segment in which roughly three-quarters of the profiles are not Gen X. Most of them are Millennials (85) and Gen Z (34). The segment is also 60% larger than it should be. The Baby Boomer segment has the same problem and is about 2.5 times its true size.

### 2. The headline accuracy is flattered by easy cases

157 profiles (16%) state an age in the bio, for example "Age: 34. Student. …". The model gets **all 157** right. On the 843 profiles without a stated age:

- accuracy is **54.9%**
- macro-F1 is **0.48**

These 843 are the cases the model exists for. In production, the 55% figure is the better guide to how it will perform on them.

### 3. The model misreads its strongest signal: hashtags

Every profile uses one of four hashtag sets. Each set lines up with one age group:

| Hashtag set | Most common true class | Model's most common prediction |
|---|---|---|
| #trending #viral #yolo (423) | Gen Z (377, 89%) | Gen Z (296); 110 sent to Millennials |
| #foodie #travel #workhard (299) | Millennials (234, 78%) | Millennials (275) |
| #career #familylife #retirement (180) | **Millennials (111, 62%)** | **Gen X (140)** |
| #classics #grandparents #history (98) | **Gen X / Gen Z / Millennials (66, 67%)**; Baby Boomers only 32 | **Baby Boomers (85)** |

Two of the four mappings are wrong:

- v1 treats #career/#familylife as Gen X, but most of these users are Millennials.
- v1 treats #classics/#grandparents as Baby Boomers, but two-thirds of these users are not.

These two errors largely explain the low precision on the Gen X and Baby Boomer segments.

A rule that predicts the most common true class for each hashtag set scores **75.4%** (75.1% on profiles without a stated age), well above v1's 62%. The rule does have a weakness: it never predicts Gen X, so it is not a production candidate either. What it shows is that v1 is not making good use of its inputs.

Bio keywords are also informative, and v1 underuses them:

- "Grandparent": always Baby Boomers.
- "Professor" and "Retired": always Gen X or Baby Boomers.
- "Senior Director" and "Parent": Millennials or Gen X.
- "Student": Gen Z or Millennials.

Older users also post longer texts (median 14 words for Baby Boomers vs 8 for Gen Z) and have a higher posts-to-likes ratio (median 1.85 vs 0.95).

### 4. A better model looks achievable with the same inputs

As a quick benchmark, I fitted simple models using only the stated inputs: hashtag set, bio keywords, stated age when present, word count and posts-to-likes ratio. I evaluated them with 5-fold cross-validation on this sample.

| Model | Accuracy | Accuracy, no stated age | Macro-F1 |
|---|---|---|---|
| v1 (production candidate) | 62.0% | 54.9% | 0.55 |
| Hashtag rule | 75.4% | 75.1% | 0.53 |
| Logistic regression (benchmark) | 80.9% | 80.2% | 0.67 |
| Random forest (benchmark) | 80.6% | 79.1% | 0.66 |

Caveats:

- These benchmarks were trained and tested on the same 1,000 rows, using cross-validation. Treat them as a sign of how much improvement is available, not as a validated replacement.
- Even the benchmarks find Gen X hard: the random forest catches only 26% of true Gen X users. With 103 Gen X and 38 Baby Boomer examples, the older classes need more labelled data whichever model is used.

### 5. The confidence scores are only partly useful

Overall, higher confidence does go with higher accuracy:

| Confidence | n | Mean confidence | Accuracy |
|---|---|---|---|
| 0.50–0.60 | 212 | 0.55 | 40% |
| 0.60–0.70 | 206 | 0.66 | 58% |
| 0.70–0.80 | 189 | 0.76 | 65% |
| 0.80–0.90 | 224 | 0.86 | 71% |
| 0.90–1.00 | 169 | 0.95 | 80% |

However, the scores are consistently too high, by 10–15 points in the upper bands. For the older segments they are misleading. Predictions with confidence above 0.85 are right only **48%** of the time for Gen X and **45%** for Baby Boomers. Filtering on confidence therefore does not rescue v1:

- Keeping only predictions with confidence of at least 0.8 raises accuracy to 75%, but discards 59% of profiles.
- Even at that threshold, the older segments remain unreliable.

### 6. Fairness check by gender

Accuracy is 60.4% for women and 65.1% for men (p = 0.17). Within Gen Z the gap is 57.6% vs 66.0% (p = 0.11). Neither difference is statistically significant in this sample, but both are worth tracking in the next evaluation.

## Recommendation and next steps

1. **Do not ship v1.** Segments built from it would be materially wrong in size and makeup, especially the Gen X and Baby Boomer segments. That is a direct quality risk for clients.
2. **Fix how hashtags and bio keywords are used.** Retrain with:
   - hashtag-set and bio-keyword features ("Student", "Parent", "Senior Director", "Retired", "Professor", "Grandparent", and a stated "Age: N")
   - word count and posts-to-likes ratio.
   
   A simple model of this kind already reaches about 80% on this sample.
3. **Collect more labelled older users.** Gen X and Baby Boomers make up only 14% of the sample. Oversample them, or weight them more heavily in training, and judge the model on per-class recall and precision, not just overall accuracy.
4. **Recalibrate confidence** (for example with temperature or isotonic scaling), and check calibration separately for each class. Then use a confidence threshold with an "unknown" option, so that low-confidence profiles are excluded from client segments instead of being forced into one.
5. **Set acceptance criteria before the next evaluation**, and test against a fresh hold-out sample that reflects production traffic. Suggested criteria:
   - at least 80% accuracy on profiles **without** a stated age
   - at least 70% precision for every segment sold to clients
   - segment-size error of 2 percentage points or less
   - no significant gap between genders
6. **Report segment sizes with corrections.** If an interim product is unavoidable, use only high-confidence Gen Z and Millennial predictions. Adjust segment sizes using the error rates from the confusion matrix, and do not sell Gen X or Baby Boomer segments yet.
