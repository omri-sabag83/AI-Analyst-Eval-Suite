# Age-Group Classifier v1: Evaluation and Deployment Recommendation

## Recommendation: do not deploy v1 to production

The model gets **62% of profiles right** (95% CI 59–65%). Its predictions for the two smaller age groups are mostly wrong. Its confidence score is not reliable enough to filter on. Most importantly, **simple rules built from the same inputs do much better** (75–83% accuracy). The model is not using the signal that is already in its inputs. The age-group splits it would give clients would be noticeably distorted.

## What I evaluated
- `model_evaluation_sample.xlsx`: 1,000 profiles, each with the true class, the predicted class, the model's confidence and the input fields. The file has no missing values and no duplicate IDs.
- Class mix (true): Gen Z 458, Millennials 401, Gen X 103, Baby Boomers 38. The classes are imbalanced, so I report results per class and as macro-averages, not only overall accuracy.
- Assumptions: `Actual Class` is correct ground truth, and this sample looks like the profiles the model will see in production. I don't know how the sample was drawn or whether these profiles were used to train the model. If they were, the real-world numbers would be *worse* than those below.

## Findings

### 1. Overall performance is modest
| Metric | Value |
|---|---|
| Accuracy | 0.620 (95% bootstrap CI 0.591–0.651) |
| Macro F1 | 0.552 |
| Cohen's kappa | 0.43 (moderate agreement) |
| Baseline: predict "Gen Z" for everyone | 0.458 accuracy |

### 2. Results are poor for the smaller age groups
| Class | Support | Precision | Recall | F1 |
|---|---|---|---|---|
| Gen Z | 458 | 0.87 | 0.60 | 0.71 |
| Millennials | 401 | 0.63 | 0.66 | 0.64 |
| Gen X | 103 | **0.27** | 0.44 | 0.34 |
| Baby Boomers | 38 | **0.37** | 0.89 | 0.52 |

Confusion matrix (rows = actual, columns = predicted):

| | Boomers | Gen X | Gen Z | Millennials |
|---|---|---|---|---|
| **Boomers** | 34 | 2 | 0 | 2 |
| **Gen X** | 29 | 45 | 4 | 25 |
| **Gen Z** | 17 | 34 | 276 | 131 |
| **Millennials** | 13 | 85 | 38 | 265 |

- The model predicts too many people as older. It predicts 166 Gen X (true count: 103) and 93 Boomers (true count: 38). Of profiles labelled Gen X, only 27% are actually Gen X. Of those labelled Boomers, only 37% are.
- 40% of Gen Z are missed, mostly labelled as Millennials (131).
- For clients, this means a "Gen X" or "Boomer" segment would be mostly younger users. The overall mix would also be skewed: Gen Z would show as 32% instead of 46%, and Boomers as 9% instead of 4%.

### 3. Most of the correct answers come from age stated in the bio
- 157 bios (16%) state an age outright ("Age: 34. …"). The model gets **all 157 right**. A plain age-to-generation rule would also get 98.7% of them right.
- On the other **843 profiles, accuracy is only 55%** (macro F1 0.48), and Gen X precision falls to 18%. That is the model's real performance whenever the bio doesn't give the answer away. Most profiles will look like this.

### 4. The model is worse than a hashtag lookup using its own inputs
Each profile carries one of four hashtag sets (youth/viral, travel/work, career/family, history/grandparents). The model's prediction matches a fixed one-to-one "hashtag set → class" mapping 80% of the time. The difference is that it maps the career/family set to Gen X, while the true majority for that set is Millennials (111 of 180). When the model departs from the hashtag signal on a profile with no stated age, it is right only 13% of the time (20 of 159).

Simple benchmarks, all scored on the same 1,000 profiles. The fitted ones use 5-fold cross-validation, so they never score a profile they were trained on:

| Approach | Accuracy (95% CI) | Macro F1 |
|---|---|---|
| **Current model** | **0.620 (0.59–0.65)** | **0.552** |
| Majority class per hashtag set | 0.754 (0.73–0.78) | 0.528 |
| Stated age if present, else hashtag lookup | 0.788 (0.76–0.81) | 0.623 |
| Logistic regression (hashtag set, bio role words, likes ratio, word count) | 0.798 (0.77–0.82) | 0.650 |
| Stated age if present, else that logistic regression | 0.828 (0.81–0.85) | 0.721 |

The "stated age else hashtag" rule beats the model by **+16.8 accuracy points** (paired bootstrap 95% CI +14 to +20). These benchmarks were fitted on a small sample, so treat them as rough estimates. But the gap is far too large to be noise.

### 5. The confidence score cannot be used to filter predictions
| Confidence | n | Actual accuracy |
|---|---|---|
| 0.50–0.60 | 212 | 0.40 |
| 0.60–0.70 | 206 | 0.58 |
| 0.70–0.80 | 189 | 0.65 |
| 0.80–0.90 | 224 | 0.71 |
| 0.90–1.00 | 169 | 0.80 |

Confidence goes up with accuracy, but it overstates it by about 10–15 points in every band. It only weakly separates right from wrong answers (AUC 0.66). Keeping only predictions with confidence ≥ 0.9 still gives just 78% accuracy, and it discards 80% of profiles.

### 6. Other observations
- The file contains a `Gender` column (66% Female), but gender is not listed as a model input. Accuracy is similar for both (Female 60%, Male 65%).
- Inputs vary very little: 4 hashtag sets and about 180 distinct bios. Real Instagram data is far more varied. Results on this sample may not carry over, and they are more likely to be optimistic than pessimistic.

## What should happen next
1. **Fix the model before deploying.** At a minimum, the model should beat the simple benchmarks above: use a stated age directly when the bio contains one, and learn the true hashtag-to-class pattern (career/family hashtags point mostly to Millennials, not Gen X). Weight or rebalance the classes so precision for Gen X and Boomers improves instead of the model over-predicting them.
2. **Agree on acceptance criteria with clients up front.** For example: accuracy and macro F1 above the best simple benchmark, at least ~60% precision for each class, and an error in the predicted age mix of no more than a few points per group. Measure these on held-out data **with stated-age profiles reported separately**.
3. **Recalibrate confidence** (e.g. temperature or isotonic scaling) so a 0.9 score really means about 90% accuracy. Then confidence can be used to abstain or to flag uncertain profiles.
4. **Evaluate on a larger, more realistic sample** that was not used in training, with clear documentation of how it was drawn and how ground-truth ages were obtained. Make sure it includes enough Gen X and Boomer profiles: 38 Boomers is too few for stable estimates.
5. If clients mainly need **age mix at the aggregate level** rather than per-user labels, consider correcting the predicted mix using the confusion matrix, and report uncertainty ranges with it.
