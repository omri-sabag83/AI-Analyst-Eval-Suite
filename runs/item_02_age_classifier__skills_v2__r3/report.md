# Age-group classifier v1: evaluation and deployment recommendation

## Bottom line

**Do not deploy this model to production as it is.** It gets 62% of profiles right, against 46% for a trivial "always guess Gen Z" rule. But the errors fall where they do the most damage for a segmentation product:

- **Older segments would be mostly wrong.** 73% of profiles labelled Gen X and 63% of profiles labelled Baby Boomers belong to a different age group.
- **Segment sizes would be distorted.** Gen Z would be under-counted by about a third, Baby Boomers over-counted about 2.4×, and Gen X over-counted about 1.6×.
- **The headline accuracy is flattered.** It includes the 16% of profiles whose bio states an age outright. On every other profile, accuracy falls to 55%.
- **The confidence score overstates reliability.** It cannot yet be used to filter out bad predictions safely.

The model is a reasonable first version. The way forward is targeted retraining plus a few product guardrails, not abandoning the approach (see "What should happen next").

## Data and assumptions

- 1,000 profiles, one row each, with no missing values and no duplicate IDs. Each row has the true class, the predicted class, the model's confidence (0.50–0.99) and the model inputs (name, bio, gender, hashtags, posts-to-likes rate, average word count).
- True class mix: Gen Z 458, Millennials 401, Gen X 103, Baby Boomers 38.
- **Assumptions:**
  - The sample is representative of the profiles the model will see in production.
  - The sample was *not* used to train the model. If it was, real performance is worse than shown here.
  - `Actual Class` is reliable ground truth.
  - None of these can be checked from the file.
- Only 38 Baby Boomers and 103 Gen X profiles are in the sample, so the per-class figures for these groups are imprecise (roughly ±8–15 percentage points). They still point clearly in one direction.

## Findings

### 1. Overall performance is moderate

| Metric | Value |
|---|---|
| Accuracy | **62.0%** (95% bootstrap CI 59–65%) |
| Baseline: always predict Gen Z | 45.8% |
| Balanced accuracy (mean recall across classes) | 64.9% |
| Macro F1 | 0.55 |
| Cohen's kappa | 0.43 (moderate agreement) |

Confusion matrix (rows = actual, columns = predicted):

| Actual \ Predicted | Gen Z | Millennials | Gen X | Baby Boomers | Total |
|---|---|---|---|---|---|
| Gen Z | **276** | 131 | 34 | 17 | 458 |
| Millennials | 38 | **265** | 85 | 13 | 401 |
| Gen X | 4 | 25 | **45** | 29 | 103 |
| Baby Boomers | 0 | 2 | 2 | **34** | 38 |
| Total predicted | 318 | 423 | 166 | 93 | 1,000 |

### 2. Labels on the older segments are mostly wrong

| Class | Precision (labels that are correct) | Recall (true members found) | F1 |
|---|---|---|---|
| Gen Z | 0.87 | 0.60 | 0.71 |
| Millennials | 0.63 | 0.66 | 0.64 |
| Gen X | **0.27** | 0.44 | 0.34 |
| Baby Boomers | **0.37** | 0.89 | 0.52 |

- The model pushes predictions toward older groups. It labels 166 profiles Gen X, but only 45 of them are Gen X; 85 are actually Millennials. It labels 93 profiles Baby Boomers, but only 34 are; 29 are Gen X and 17 are Gen Z.
- Gen Z labels are trustworthy (87% precision), but 40% of real Gen Z users are missed, mostly labelled Millennials (131 profiles).

### 3. Segment sizes delivered to clients would be distorted

| Segment | True share | Predicted share | Distortion |
|---|---|---|---|
| Gen Z | 45.8% | 31.8% | −14 pts (under-counted by about a third) |
| Millennials | 40.1% | 42.3% | +2 pts |
| Gen X | 10.3% | 16.6% | about 1.6× |
| Baby Boomers | 3.8% | 9.3% | about 2.4× |

Clients buy segment-level insight. A client studying "what Baby Boomers share" would get a segment where nearly two-thirds of the content comes from younger users. That is the main business risk, and accuracy alone hides it.

### 4. Headline accuracy is inflated by bios that state an age

157 profiles (15.7%) have a bio such as "Age: 24. Student. …". The model gets **all 157 right (100%)**, and the stated age always matches the true class. On the other 843 profiles:

- Accuracy is **54.9%**. A majority-class guess on the same profiles scores 47.3%.
- Precision is 0.18 for Gen X and 0.31 for Baby Boomers. Macro F1 is 0.48.

Reading an age from the bio is fine as a rule, but it is not "prediction". Expect about 55% accuracy on the large majority of profiles that don't state an age. If production has fewer self-declared ages than this sample, overall accuracy will be lower than 62%.

### 5. The model leans mostly on hashtag stereotypes

Each profile carries one of four fixed hashtag sets, and the model's prediction follows the set almost one-for-one. The real age mix inside each set is much broader:

| Hashtag set | Model mostly predicts | Actual mix | Accuracy |
|---|---|---|---|
| #trending #viral #yolo | Gen Z (296/423) | 89% Gen Z | 65% |
| #foodie #travel #workhard | Millennials (275/299) | 78% Millennials | 79% |
| #career #familylife #retirement | Gen X (140/180) | **62% Millennials**, 23% Gen X | **38%** |
| #classics #grandparents #history | Baby Boomers (85/98) | 33% BB, 26% Gen X, 24% Gen Z | **41%** |

- The two "older-sounding" hashtag sets are where most of the over-prediction of Gen X and Baby Boomers comes from (finding 2).
- Average word count and posts-to-likes rate also differ by age (Baby Boomers 14.0 words and 1.89 vs Gen Z 8.3 words and 1.00). The model seems to exaggerate these differences too: profiles it predicts as Gen X average 13.9 words, against 12.1 for actual Gen X.
- Bio role words carry real signal that the model under-uses. "Professor" profiles are all Gen X, yet only 42% are predicted correctly. "Parent" profiles are 80% Millennials, yet only 52% are predicted correctly.

This is inferred from how predictions line up with inputs; I don't have access to the model's internals.

### 6. Confidence is informative but overconfident

| Confidence band | n | Mean confidence | Actual accuracy |
|---|---|---|---|
| 0.50–0.60 | 212 | 0.55 | 40% |
| 0.60–0.70 | 206 | 0.66 | 58% |
| 0.70–0.80 | 189 | 0.76 | 65% |
| 0.80–0.90 | 224 | 0.86 | 71% |
| 0.90–1.00 | 169 | 0.95 | 80% |

- Higher confidence does mean higher accuracy (point-biserial r = 0.27). But the score overstates accuracy by about 10–15 points in every band (expected calibration error 0.13).
- Average confidence is 0.76 even on the 157 age-stated profiles that are always correct. So the score doesn't fully reflect what the model actually knows.
- Keeping only predictions with confidence ≥ 0.8 gives 75% accuracy, but on only 41% of profiles. Keeping ≥ 0.9 gives 78% accuracy on 20% of profiles. Thresholding helps, but it does not reach production quality on its own.
- Gender: accuracy is 60% for profiles marked female and 65% for male. The gap is small and within noise for this sample size, but it should be monitored.

## Recommendation

**Not ready for production.** Specifically:

1. Do not use it to produce Gen X or Baby Boomers segments: most members of those segments would be mislabelled.
2. Do not report segment sizes from raw predictions, because the older groups would be inflated 1.6–2.4×.

At most, a limited internal pilot could be justified. It would use Gen Z labels (87% precision) and age-stated profiles (100%), with a confidence cut-off and the stated error rates shown to users.

## What should happen next

1. **Fix the over-prediction of older groups.**
   - Retrain with class weights or a resampled training set.
   - Tune decision thresholds per class to maximise precision on Gen X and Baby Boomers, not raw accuracy.
   - Reduce reliance on hashtag stereotypes: use richer hashtag and post text than four coarse sets, and make better use of bio role words (Parent, Professor, Retired, Grandparent).
2. **Treat a stated age as a deterministic rule outside the model.** Then evaluate and report the model only on profiles without one; that is its real job.
3. **Calibrate the confidence score** (e.g. temperature or isotonic scaling on a hold-out set) so that 0.9 means about 90%. Then use it to abstain on low-confidence profiles rather than force a label.
4. **Correct segment sizes when reporting.** If segment shares are a deliverable, adjust them using the confusion matrix (prior-shift correction) instead of counting raw predictions.
5. **Evaluate on a larger, properly held-out sample.** Include at least about 200 Gen X and 200 Baby Boomers so their precision can be measured to within about ±5 points. Confirm the sample was not used in training.
6. **Set acceptance criteria before the next round.** As a suggestion: precision ≥ 0.70 for every class on profiles without a stated age; predicted segment shares within ±3 points of the true shares; calibration error ≤ 0.05. Re-run this evaluation against them.
