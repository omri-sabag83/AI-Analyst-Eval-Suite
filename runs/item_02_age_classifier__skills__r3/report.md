# Age-Group Classifier v1: Evaluation and Deployment Recommendation

## Bottom line

**Don't deploy this model to production yet.** On the 1,000-profile sample it gets **62% of profiles right** (95% CI roughly 59–65%). That is only 16 points better than labelling everyone "Gen_z" (45.8%). Clients would also get the wrong segment sizes. The model's age-group mix differs from the true mix by up to 14 percentage points: it understates Gen Z by 14 pp and more than doubles the size of Baby Boomers. The confidence score overstates how reliable the predictions are, so it can't safely be used to filter out bad predictions. A simple model trained on the same inputs gets about 72–77% right (estimated with 5-fold cross-validation). So the gap looks like a problem with the model, not a limit of the data, and it should be fixable.

## What was evaluated

- `model_evaluation_sample.xlsx`: 1,000 profiles, one row each, with the true class, the predicted class, the model's confidence, and the input fields. No missing values and no duplicates.
- True class mix: Gen_z 458, Millennials 401, Gen_x 103, Baby Boomers 38. The classes are heavily imbalanced, so I report per-class metrics and balanced metrics as well as overall accuracy.
- **Assumptions:** (1) `Actual Class` is correct ground truth. (2) The sample is representative of the profiles the model will see in production and was not used to train the model. (3) The client use case is **segmenting audiences**, so getting the age-group *mix* right matters as much as getting each profile right.

## Findings

### 1. Overall performance is weak

| Metric | Value |
|---|---|
| Accuracy | 62.0% (95% bootstrap CI 59–65%) |
| Majority-class baseline ("everyone is Gen_z") | 45.8% |
| Balanced accuracy (average recall across classes) | 64.9% |
| Macro F1 | 0.55 |
| Cohen's kappa | 0.43 (moderate agreement) |

Confusion matrix (rows are the true class, columns are the predicted class):

| Actual \ Predicted | Baby Boomers | Gen_x | Gen_z | Millennials | Total |
|---|---|---|---|---|---|
| Baby Boomers | **34** | 2 | 0 | 2 | 38 |
| Gen_x | 29 | **45** | 4 | 25 | 103 |
| Gen_z | 17 | 34 | **276** | 131 | 458 |
| Millennials | 13 | 85 | 38 | **265** | 401 |
| Total predicted | 93 | 166 | 318 | 423 | 1000 |

Per class:

| Class | Precision | Recall | F1 | n |
|---|---|---|---|---|
| Gen_z | 0.87 | 0.60 | 0.71 | 458 |
| Millennials | 0.63 | 0.66 | 0.64 | 401 |
| Gen_x | **0.27** | 0.44 | 0.34 | 103 |
| Baby Boomers | **0.37** | 0.90 | 0.52 | 38 |

- **Gen_x and Baby Boomer predictions are mostly wrong.** Only 27% of profiles labelled Gen_x and 37% of those labelled Baby Boomers actually belong to that group. The model over-predicts both older groups and misses 40% of Gen Z users. Of the 458 Gen Z users, 131 are labelled Millennials.
- Most errors are between neighbouring generations: 310 of the 380 errors are one generation off. But 70 are two or three generations off, including 17 Gen Z users labelled Baby Boomers.

### 2. Segment sizes delivered to clients would be distorted

| Group | True share | Predicted share | Error |
|---|---|---|---|
| Gen_z | 45.8% | 31.8% | **−14.0 pp** |
| Millennials | 40.1% | 42.3% | +2.2 pp |
| Gen_x | 10.3% | 16.6% | +6.3 pp (×1.6) |
| Baby Boomers | 3.8% | 9.3% | +5.5 pp (×2.4) |

For a product that sells segmented insights, this is the most important problem. A client asking "what do Baby Boomers share?" would get a segment that is **63% non-Boomers**. Because these errors are systematic, collecting more data would not average them out.

### 3. The model works only when the bio states an age

- 157 profiles (16%) have an explicit "Age: NN" in the bio. The model gets **all 157 right (100%)**.
- On the other 843 profiles, which have no stated age and are the cases where a model is actually needed, accuracy falls to **54.9%**. Macro F1 is 0.48, Gen_x precision is 0.18, and Baby Boomer precision is 0.31.
- So the overall 62% flatters the model. Most of the useful work is reading a number out of the bio, which a regular expression could do. The 54.9% is the more honest figure for the cases that need inference.

### 4. The model misreads the strongest signal it has

The sample has four hashtag bundles, and each bundle strongly indicates an age group. The model's mapping is wrong for two of them:

| Hashtag bundle | Most common true class | Model mostly predicts | Model accuracy in this bundle |
|---|---|---|---|
| #trending #viral #yolo (423) | Gen_z (377 = 89%) | Gen_z (296), but Millennials 110 times | 65% |
| #foodie #travel #workhard (299) | Millennials (234 = 78%) | Millennials (275) | 79% |
| #career #familylife #retirement (180) | **Millennials (111 = 62%)** | **Gen_x (140)** | **38%** |
| #classics #grandparents #history (98) | Baby Boomers (32 = 33%), spread evenly | Baby Boomers (85) | 41% |

Predicting the most common true class for each bundle would score **75.4%** on this sample. That is an in-sample figure, so it is optimistic. Even so, it shows the model is using its main feature badly, probably because of a training-data skew or label mapping that overweights the older classes.

The other inputs also carry signal the model may not be using well. Average word count and the posts-to-likes ratio both rise with age: the median ratio is 0.95 for Gen Z and 1.85 for Boomers, and median word count is 8 vs 14. Bio roles are also informative. "Student" is 73% Gen Z, "Grandparent" is 100% Boomer, "Professor" is 100% Gen_x, and "Senior Director" and "Parent" are mostly Millennial.

### 5. The confidence score overstates reliability

| Confidence band | n | Mean confidence | Actual accuracy |
|---|---|---|---|
| 0.50–0.60 | 212 | 0.55 | 40% |
| 0.60–0.70 | 206 | 0.66 | 58% |
| 0.70–0.80 | 189 | 0.76 | 65% |
| 0.80–0.90 | 224 | 0.86 | 71% |
| 0.90–1.00 | 169 | 0.95 | 80% |

- Confidence is higher than actual accuracy in every band. Average confidence is 0.75 while accuracy is 0.62, and the expected calibration error is 0.13. Confidence does rank predictions in a useful order (AUC 0.66 for telling right from wrong predictions).
- Filtering on confidence doesn't solve the problem. Keeping only predictions with confidence of at least 0.8 still gives just 75% accuracy, and 59% of profiles are dropped. A threshold of 0.9 gives 78% accuracy and keeps only 20% of profiles.
- Confidence is about the same across true classes (0.74–0.76), even for Gen_x, where only 44% of true members are found and only 27% of Gen_x predictions are right. The score gives no warning for the weakest classes.

### 6. Better performance is achievable with the same inputs

As a headroom check, I fitted a plain logistic regression on the provided inputs: the hashtag bundle, posts-to-likes ratio, word count, and the "Student" and "Grandparent" bio flags. It deliberately does not use the stated age. I measured it with 5-fold stratified cross-validation on this sample:

| Model | Accuracy | Balanced accuracy | Macro F1 |
|---|---|---|---|
| Current model v1 | 62.0% | 64.9% | 0.55 |
| Logistic regression, hashtags only | 75.4% | 63.1% | 0.53 |
| Logistic regression, all inputs | 76.8% | 58.1% | 0.58 |
| Logistic regression, all inputs, class-balanced | 72.4% | 69.9% | 0.62 |

**Caveat:** this check uses a small sample that was meant for evaluation, not training. It is not a model to deploy. It shows that the current model is about 10–15 points below what simple methods get from the same features. On the minority classes even the simple models are only moderate, which reflects how few Gen_x and Boomer examples there are and how much their hashtags overlap with other groups.

### Data-quality notes

- `Gender` looks unreliable. For example, "Rita Clark" is labelled Male and "Liam Thomas" Female. It isn't a model input, so I didn't use it for any conclusion. The accuracy gap by gender (Female 60%, Male 65%) is small and within the noise.
- The sample looks synthetic or templated: four hashtag bundles and about 69 distinct bios. Real Instagram data will be much messier, so production performance is likely to be *lower* than these numbers, not higher.
- Gen_x (103) and especially Baby Boomers (38) have few examples, so their per-class metrics carry wide uncertainty. Even allowing for that, Boomer precision of 37% (34 of 93) is clearly poor.

## Recommendation

**Don't deploy v1.** Its accuracy is only modestly better than a trivial baseline, it gets only 55% right on profiles without a stated age, which are the ones that actually need a model, it would materially distort the segment sizes clients pay for, and its confidence score can't be relied on to catch errors.

### Suggested next steps

1. **Fix the obvious errors first.**
   - Take the stated age from the bio using a rule. That covers about 16% of profiles at near-100% accuracy.
   - Investigate why the model maps #career/#familylife/#retirement to Gen_x and over-predicts Baby Boomers. Check training-set class balance, the label mapping, and any class weights or oversampling that might be too aggressive.
2. **Retrain and set targets before re-evaluating.** For example:
   - Accuracy on profiles **without** a stated age of at least 75%.
   - Precision of at least 0.6 for every class.
   - Predicted segment shares within ±3 pp of the true shares.
   - Make use of word count, the posts-to-likes ratio, and bio role keywords.
3. **Calibrate the confidence score** using temperature or isotonic scaling on held-out data, then report accuracy at each confidence threshold. Consider returning "unknown" for low-confidence profiles instead of forcing a label.
4. **Correct the aggregate segment shares.** Even after retraining, adjust the shares delivered to clients for known misclassification rates, for example by using the confusion matrix to invert predicted shares. Show clients uncertainty ranges for small segments such as Boomers.
5. **Evaluate on a larger, real, held-out sample.** Include enough Gen_x and Boomer profiles (a few hundred each) and messier real-world bios and hashtags, and confirm that none of it was used in training.
6. **Re-evaluate against the targets above** before any production release. A limited pilot is reasonable only for the Gen Z vs. Millennial split, and only after calibration.

---
*Method notes: all metrics are computed directly from `Actual Class` vs `Predicted Class` over the 1,000 rows. The confidence interval comes from 5,000 bootstrap resamples. Expected calibration error uses 10 equal-width confidence bins. Baseline models were scikit-learn logistic regression with 5-fold stratified cross-validation (random_state=0).*
