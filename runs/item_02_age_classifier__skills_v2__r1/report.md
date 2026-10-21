# Age-group classifier: evaluation and deployment recommendation

## Recommendation: do not deploy this version

The model gets **62% of profiles right** (95% CI 59–65%). A simple rule that just looks at a profile's hashtags gets **68.5%**. The model also distorts the thing clients are paying for, the age-group mix: it **overstates Baby Boomers by about 2.5× and Gen X by about 1.6×, and understates Gen Z by 14 points.** Clients would get wrong segment sizes, and the smallest segments (Gen X, Boomers) would be made up mostly of people who don't belong in them.

## What I evaluated
- `model_evaluation_sample.xlsx`: 1,000 profiles, each with a true class, a predicted class and a confidence score. No values were missing.
- True mix: Gen Z 45.8%, Millennials 40.1%, Gen X 10.3%, Baby Boomers 3.8%.
- **Assumptions:** (1) This sample is representative of production traffic and was not used to train the model. I can't check either. (2) "Ready for production" means usable for client-facing segment reporting, with sensible accuracy on every segment and segment sizes that are roughly right.

## Findings

### 1. Overall accuracy is low and below a trivial baseline
| | Accuracy | Macro-F1 |
|---|---|---|
| Model | **62.0%** (CI 59–65%) | 0.55 (CI 0.51–0.59) |
| Always predict "Gen Z" | 45.8% | — |
| Hashtag rule (map each hashtag set to its obvious generation) | **68.5%** | 0.57 |
| Hashtag rule + age stated in bio, where present | 72.8% | 0.62 |

The hashtag rule beats the model by 6.5 points (bootstrap CI +3.8 to +9.3), so the gap is not noise. The model agrees with the hashtag rule 80% of the time. Where it overrides the rule (204 profiles), it is usually wrong: 139 of those 204 predictions are errors.

### 2. Per-segment performance: Gen X and Boomer predictions are mostly wrong
Confusion matrix (rows = actual, columns = predicted):

| Actual \ Pred | Gen Z | Millennials | Gen X | Boomers | Total |
|---|---|---|---|---|---|
| Gen Z | **276** | 131 | 34 | 17 | 458 |
| Millennials | 38 | **265** | 85 | 13 | 401 |
| Gen X | 4 | 25 | **45** | 29 | 103 |
| Boomers | 0 | 2 | 2 | **34** | 38 |

| Segment | Precision (CI) | Recall | F1 |
|---|---|---|---|
| Gen Z | 0.87 (0.83–0.90) | 0.60 | 0.71 |
| Millennials | 0.63 (0.58–0.67) | 0.66 | 0.64 |
| Gen X | **0.27** (0.21–0.34) | 0.44 | 0.34 |
| Baby Boomers | **0.37** (0.27–0.46) | 0.89 | 0.52 |

- The model systematically pushes people **older**. 40% of Gen Z are misclassified, mostly as Millennials (131). Millennials get pushed into Gen X (85).
- Of the 166 profiles labelled Gen X, only 45 actually are Gen X. Of the 93 labelled Boomers, only 34 are Boomers.

### 3. Segment sizes come out wrong
| Segment | True share | Model's share |
|---|---|---|
| Gen Z | 45.8% | 31.8% |
| Millennials | 40.1% | 42.3% |
| Gen X | 10.3% | 16.6% |
| Baby Boomers | 3.8% | 9.3% |

Any client report built on these labels would misstate audience composition. The small, older segments would be mostly misclassified younger users.

### 4. The model's success comes from "easy" profiles
- 157 profiles state their age in the bio ("Age: 24."). The model gets **all 157 right**. On the other **843 profiles, accuracy falls to 54.9%** (macro-F1 0.48), against 68.0% for the hashtag rule on those same profiles. Most real profiles won't state an age, so the headline 62% probably *overstates* production performance.
- Bio role cues carry age information: "Student" means Gen Z or Millennial, "Retired" or "Grandparent" means Gen X or Boomer, and "Parent" or "Senior Director" means Millennial or Gen X. The model doesn't use them well. Accuracy is only 52–53% on profiles with "Parent" or "Senior Director".
- Engagement features differ clearly by generation. Average word count rises from 8.3 (Gen Z) to 14.0 (Boomers), and the posts/likes rate rises from 1.00 to 1.89. So there is real signal the model is not using.

### 5. Confidence is informative but overconfident
| Confidence | n | Mean confidence | Actual accuracy |
|---|---|---|---|
| 0.50–0.60 | 212 | 0.55 | 40% |
| 0.60–0.70 | 206 | 0.66 | 58% |
| 0.70–0.80 | 189 | 0.76 | 65% |
| 0.80–0.90 | 224 | 0.86 | 71% |
| 0.90–1.00 | 169 | 0.95 | 80% |

Accuracy rises with confidence, so the score ranks predictions usefully. But the model is 8–15 points overconfident in every band, and there are 43 errors at confidence ≥0.90. Keeping only predictions with confidence ≥0.8 raises accuracy to 75%, but that covers just 41% of profiles, and the kept set is still below what the simple rules achieve on *all* profiles. Filtering by confidence doesn't rescue the model.

### 6. Better performance looks achievable
As a rough check on headroom, I fitted a plain logistic regression on the same inputs: hashtag set, bio role cue, stated age, word count and posts/likes rate. With 5-fold cross-validation it reached **82% accuracy (macro-F1 0.71)**. **Treat this as an estimate, not a benchmark.** I engineered those features after looking at this same sample, and 1,000 rows is small. Gen X is still the weakest class (38% recall). The point is only that the inputs carry far more signal than the current model extracts.

## Caveats
- The data looks templated: 24 hashtag sets drawn from 4 generation-themed groups, and a small set of bio phrases. Real profiles will be noisier, so all of these numbers, including the baselines, may be optimistic.
- The `Gender` field often doesn't match the first name (e.g., "Rita Clark – Male"). That suggests label-quality issues in the profile metadata. It isn't used by the model, but it's worth checking.
- I couldn't check whether this sample overlaps the model's training data. If it does, true performance is worse.
- Gen X (103) and Boomer (38) counts are small, so their metrics have wide intervals (see the CIs above). The conclusions hold even at the favourable end of those intervals.

## What should happen next
1. **Hold the release.** At minimum, the model must beat the hashtag + stated-age rule (≈73% accuracy, macro-F1 0.62) on a held-out set before it is reconsidered.
2. **Agree acceptance criteria with the business first.** For example: macro-F1 above a set bar, a minimum precision for each segment (Gen X and Boomers are the weak spots), and predicted segment shares within ±2–3 points of the true shares.
3. **Retrain using the signal that's already there.** Use bio role cues and stated age explicitly, along with word count and posts/likes rate. Use class weighting or threshold tuning so the model stops over-predicting the older classes. Then recalibrate confidence, e.g. with temperature or isotonic scaling.
4. **Evaluate properly.** Use a fresh, representative, held-out sample with enough Gen X and Boomer profiles (several hundred each). Report results separately for profiles with and without a stated age, since most production profiles won't have one.
5. **If clients need segment sizes before a better model exists,** report them using a prevalence correction based on the confusion matrix, not raw predicted counts, and flag Gen X and Boomer figures as low-confidence.
