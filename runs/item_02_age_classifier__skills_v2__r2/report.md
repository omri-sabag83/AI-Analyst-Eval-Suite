# Age-group classifier v1: evaluation and deployment recommendation

## Bottom line
**Do not deploy this model to production yet.** It gets 62% of profiles right. That beats always guessing the largest group (46%), but it falls short of what is needed to segment client data reliably:

1. **It gets the group sizes wrong in a systematic way.** Clients would see Baby Boomers at 2.4× their real share and Gen X at 1.6×, while Gen Z is undercounted by about a third. For a product that sells age-segmented insights, this is the most damaging failure.
2. **Its predictions for the two older groups are mostly wrong.** Only 37% of "Baby Boomer" labels and 27% of "Gen X" labels are correct. Any insight a client draws about those segments would come mostly from younger users.
3. **Much simpler approaches do better on the same inputs.** A rule that looks only at the hashtag set gets about 75% right. A plain logistic regression on the listed inputs gets about 83% (both cross-validated on this sample). So the gap comes from the model, not from weak data, and it can be fixed.
4. **Its confidence scores are overstated.** Predictions made with ≥90% confidence are right only 78% of the time, and confidence is a weak guide to which predictions are correct (AUC 0.66).

## What was evaluated
- `model_evaluation_sample.xlsx`: 1,000 profiles, each with the true class, predicted class, confidence and the input features. There are no missing values and no duplicate IDs.
- True class mix: Gen Z 458, Millennials 401, Gen X 103, Baby Boomers 38. The two older groups are small (141 profiles together), so their metrics carry wide uncertainty.

**Assumptions**
- `Actual Class` is correct ground truth.
- The sample is representative of production traffic. If production contains more older users, the precision problems below would shrink, but the share distortion would not go away.

## Evidence

### Overall performance
| Metric | Value |
|---|---|
| Accuracy | **62.0%** (95% bootstrap CI 59–65%) |
| Majority-class baseline (always "Gen Z") | 45.8% |
| Balanced accuracy (average of per-class recall) | 64.9% |
| Macro F1 | 0.55 |
| Cohen's kappa (agreement beyond chance) | 0.43 (moderate) |

### Confusion matrix (rows = actual, columns = predicted)
| Actual \ Predicted | Boomers | Gen X | Gen Z | Millennials | Total |
|---|---|---|---|---|---|
| Baby Boomers | **34** | 2 | 0 | 2 | 38 |
| Gen X | 29 | **45** | 4 | 25 | 103 |
| Gen Z | 17 | 34 | **276** | 131 | 458 |
| Millennials | 13 | 85 | 38 | **265** | 401 |
| Total predicted | 93 | 166 | 318 | 423 | 1,000 |

### Per-class results
| Class | Precision (share of predictions that are right) | Recall (share of the class found) | F1 |
|---|---|---|---|
| Baby Boomers | 0.37 | 0.89 | 0.52 |
| Gen X | 0.27 | 0.44 | 0.34 |
| Gen Z | 0.87 | 0.60 | 0.71 |
| Millennials | 0.63 | 0.66 | 0.64 |

The model leans toward older groups: it predicts "older than actual" far more often than "younger". The largest single error is Gen Z predicted as Millennials (131 profiles, 29% of all Gen Z). Next are Millennials predicted as Gen X (85) and Gen X predicted as Baby Boomers (29 of 103).

### Impact on the segment sizes clients would see
| Segment | True share | Predicted share | Distortion |
|---|---|---|---|
| Gen Z | 45.8% | 31.8% | −14.0 pts (−31%) |
| Millennials | 40.1% | 42.3% | +2.2 pts |
| Gen X | 10.3% | 16.6% | +6.3 pts (×1.6) |
| Baby Boomers | 3.8% | 9.3% | +5.5 pts (×2.4) |

In this sample, 63% of the profiles the model labels "Baby Boomer" (59 of 93) are actually younger. Of those it labels "Gen X", 73% are wrong (121 of 166), and 119 of those 121 are younger. Reports such as "what Boomers share" would mostly describe Millennials and Gen Z.

### Confidence is overstated and only weakly informative
| Confidence band | n | Actual accuracy | Mean stated confidence |
|---|---|---|---|
| 0.50–0.60 | 212 | 40% | 0.55 |
| 0.60–0.70 | 206 | 58% | 0.66 |
| 0.70–0.80 | 189 | 65% | 0.76 |
| 0.80–0.90 | 224 | 71% | 0.86 |
| 0.90–1.00 | 169 | 80% | 0.95 |

Accuracy does rise with confidence, but every band from 0.6 upward is overconfident, by 8–15 points. There are 43 wrong predictions with confidence ≥0.9. Keeping only predictions with confidence ≥0.8 raises accuracy to just 75%, and discards 59% of profiles. A confidence threshold is therefore not a viable workaround.

### The headline 62% flatters the model
- 157 bios state the age outright (e.g. "Age: 24."). The model gets **all 157** right, which is expected. On the other 843 profiles, where the model actually has to infer age, accuracy is **54.9%** (95% CI 52–58%).
- The model mostly follows the hashtag set. The sample contains only four hashtag sets, and the model maps each to roughly one class. One mapping is wrong: the `#career #familylife #retirement` set goes to Gen X 140 of 180 times, yet 62% of those users are Millennials. The model also labels every user with `#trending #viral #yolo` as Gen Z or Millennial, even though role words in the bio (e.g. "Senior Director", "Parent") and higher word counts and post/likes ratios point to older users. Older groups do post longer captions (median 12–14 words vs 8–9) and have higher post/likes ratios (median 1.5–1.85 vs 0.95–1.14).

### Simple benchmarks beat the model on the same inputs
Both benchmarks were scored with 5-fold cross-validation on this sample.
| Approach | Accuracy | Macro F1 |
|---|---|---|
| Current model | 62.0% | 0.55 |
| Hashtag set → most common class (4-row lookup) | 75.4% | 0.53 |
| Logistic regression: hashtag set, bio role keyword, stated age (if any), word count, post/likes ratio | **82.7%** | **0.71** |

This is a quick sanity check, not a replacement model. It was fitted on only 1,000 rows, and the data looks templated (few distinct bios and hashtag sets), so real-world performance will likely be lower. Still, it shows the inputs contain far more signal than v1 uses. Even this benchmark has weak Gen X recall (40%), so separating Gen X from Millennials remains the hardest part of the problem.

### Gender
`Gender` is in the file but not listed as a model input. Accuracy is 60.4% for female and 65.1% for male profiles. That gap is not statistically significant at this sample size, but it should be tracked.

## Recommendations
1. **Do not release v1 to clients.** The size distortion and low precision for older segments would produce misleading insights, especially for Gen X and Baby Boomers.
2. **Retrain with the features v1 under-uses.** Use bio role keywords (Student, Parent, Senior Director, Retired, Grandparent, Professor), stated age when present (map it by rule), word count and post/likes ratio together with hashtags. Handle class imbalance with class weights or resampling so the model does not over-predict the older groups. The logistic-regression benchmark (~83%) is the bar the next version should clearly beat.
3. **Calibrate confidence** (e.g. temperature or isotonic scaling on a held-out set), so a low-confidence result can be routed to "unknown age" instead of a wrong segment.
4. **Set acceptance criteria before the next evaluation.** Suggested:
   - overall accuracy ≥ 80% on profiles without a stated age;
   - precision ≥ 70% for every class;
   - each segment's predicted share within ±2 points of its true share;
   - calibration error ≤ 5 points.
5. **Evaluate on a bigger, independent, production-like holdout.** It should include at least ~200 Gen X and ~200 Baby Boomer profiles so metrics for the small classes are reliable. It should also check that ground-truth labels are reliable, and that the test data does not share the templated structure of the training data.
6. **If clients need something in the meantime**, report segment sizes corrected using the confusion matrix (adjusting the model's counts by its known error rates), and label Gen X and Baby Boomer insights as low-reliability.
