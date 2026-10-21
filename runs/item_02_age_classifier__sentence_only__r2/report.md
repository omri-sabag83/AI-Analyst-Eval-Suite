# Age-group classifier v1: evaluation and deployment recommendation

## Bottom line

**Do not deploy this model to production.** On the 1,000-profile sample it gets **62% of profiles right** (95% CI 59–65%). A one-line rule that only looks at a profile's hashtag set gets **68.5%**. The model is weakest exactly where clients need it to be reliable:

- **Most profiles it labels Gen X are not Gen X.** Only 27% of its "Gen X" predictions are correct.
- **Most profiles it labels Baby Boomers are not Baby Boomers.** Only 37% are correct.
- **It undercounts Gen Z.** Gen Z is 46% of the sample but 32% of the predictions.
- **The older segments come out inflated.** Gen X shows as 17% (true share 10%) and Baby Boomers as 9% (true share 4%).

A segmentation product built on these labels would give clients the wrong age mix and contaminated older-age segments. The data also shows that a clearly better model is within reach (see "What should happen next").

## What I evaluated

- **Data:** `model_evaluation_sample.xlsx`, 1,000 profiles, each with true class, predicted class, confidence and the input fields. There are no missing values and no duplicate users.
- **True class mix:** Gen Z 458, Millennials 401, Gen X 103, Baby Boomers 38.
- **Metrics:**
  - overall accuracy, balanced accuracy and per-class precision/recall, with bootstrap 95% CIs;
  - the confusion matrix;
  - calibration of the confidence score;
  - comparison against simple baselines;
  - an error breakdown by input.

## Findings

### 1. Overall performance is modest and below a trivial baseline

| Approach | Accuracy | Balanced accuracy | Macro F1 |
|---|---|---|---|
| Always predict "Gen Z" | 45.8% | 25.0% | 0.16 |
| **Model v1** | **62.0%** | **64.9%** | **0.55** |
| Rule: map hashtag set → age group | 68.5% | 66.4% | 0.57 |
| Rule: age stated in bio if present, else hashtag rule | 72.8% | 71.7% | 0.62 |

Cohen's kappa is 0.43, which is only moderate agreement beyond chance.

### 2. Confusion matrix (rows = actual, columns = predicted)

| Actual \ Predicted | Gen Z | Millennials | Gen X | Baby Boomers | Recall |
|---|---|---|---|---|---|
| Gen Z (458) | **276** | 131 | 34 | 17 | 60% |
| Millennials (401) | 38 | **265** | 85 | 13 | 66% |
| Gen X (103) | 4 | 25 | **45** | 29 | 44% |
| Baby Boomers (38) | 0 | 2 | 2 | **34** | 89% |
| **Precision** | 87% | 63% | 27% | 37% | |

Per-class 95% CIs:

| Class | Recall | Precision |
|---|---|---|
| Gen Z | 55–65% | 83–91% |
| Millennials | 62–71% | 58–67% |
| Gen X | 35–54% | 21–34% |
| Baby Boomers | 79–98% | 27–46% |

**The model systematically shifts people into older groups.**
- 40% of Gen Z users are labelled Millennials or older.
- 24% of Millennials are labelled Gen X or Baby Boomers.

**The minority classes are flooded with false positives.**
- In the "Gen X" segment, 121 of 166 profiles are someone else, mostly Millennials (85).
- In the "Baby Boomer" segment, 59 of 93 profiles are someone else.

The high Baby Boomer recall is a side effect of over-predicting that class, not evidence of skill.

### 3. Impact on client-facing segment sizes

| Group | True share | Model's share |
|---|---|---|
| Gen Z | 45.8% | 31.8% |
| Millennials | 40.1% | 42.3% |
| Gen X | 10.3% | 16.6% |
| Baby Boomers | 3.8% | 9.3% |

Any client report built on these labels would understate the youngest audience by about a third. It would also overstate the two oldest groups by roughly 1.6× (Gen X) and 2.4× (Baby Boomers).

### 4. The model under-uses the information it is given

- **Bios that state an age.** 157 bios contain an explicit age ("Age: 24."). That age falls in the correct generation 98.7% of the time. The model gets all 157 right. On the other **843 profiles it is only 54.9% accurate** (balanced accuracy 57.9%). That subset is the realistic case, and there Gen X precision drops to 18%.
- **Hashtags.** Each profile has one of only four hashtag sets, and each set lines up strongly with one generation. For example, 377 of the 423 users with `#trending #viral #yolo` are Gen Z. The model agrees with the hashtag rule on 80% of profiles. Where it overrides the rule (204 cases), it is right only 32% of the time (65 of 204).
- **Overrides look like noise, not signal.** Take the 377 Gen Z users with Gen Z hashtags. The model sends 100 of them to Millennials. Those 100 have essentially the same post/likes rate (0.92 vs 0.87) and word count (7.5 vs 7.6) as the ones it gets right.
- **Bio keywords are ignored.** Keywords such as "Grandparent", "Professor", "Retired", "Student" and "Parent" carry age signal. On the 12 "Professor" profiles, all actually Gen X, the model is right only 42% of the time.

### 5. The confidence score is not trustworthy as-is

- **It does go up with accuracy:**

  | Confidence band | Accuracy |
  |---|---|
  | 0.5–0.6 | 40% |
  | 0.6–0.7 | 58% |
  | 0.7–0.8 | 65% |
  | 0.8–0.9 | 71% |
  | 0.9–1.0 | 80% |

- **But it is overconfident by about 13 points on average** (expected calibration error 0.13).
- **It separates right from wrong answers only weakly** (AUC 0.66).
- **Wrong Gen X and Baby Boomer predictions carry the same confidence as right ones** (about 0.77 vs 0.76).
- **Thresholding cannot rescue the model.** Keeping only predictions with confidence ≥ 0.8 keeps 41% of profiles at 75% accuracy, which is still worse than the age+hashtag rule applied to every profile.

### 6. Fairness check (gender)

There is a `Gender` column, although it is not listed as a model input. Accuracy is 60% for women and 65% for men. The difference is not statistically significant (χ² p = 0.17; within Gen Z p = 0.11). Gender values often do not match the first names (for example "Rita Clark" is listed as Male), so the field's quality is doubtful.

## What should happen next

1. **Keep v1 out of production.** It loses to a hashtag lookup, and its older-group segments are mostly wrong.
2. **Rebuild the model around the signals that actually carry information:**
   - an explicit age in the bio, which settles the label almost deterministically;
   - the hashtag set;
   - bio role keywords (Student, Parent, Professor, Retired, Grandparent);
   - posting behaviour (older groups have a higher post/likes rate and use more words).

   As a feasibility check only, I ran a quick gradient-boosted model with 5-fold cross-validation on this same sample:
   - accuracy was about 76–79%, with Gen Z and Millennial F1 of about 0.75–0.89;
   - Gen X and Baby Boomers stayed hard (F1 about 0.35–0.47) because there are only 103 and 38 examples.

   So substantial gains are realistic. Gen X and Baby Boomers will need more labelled data, or class weighting or resampling.
3. **Fix the bias toward older classes.** Check the class priors and weights used in training against the real Instagram age mix, and tune decision thresholds for each class.
4. **Calibrate the confidence score** (for example with temperature or isotonic scaling). Then use it to abstain or route to an "unknown" bucket rather than force a label.
5. **Report segment sizes with correction.** For client aggregates, adjust predicted shares using the confusion matrix, or report them with error bars, instead of raw counts of predicted labels.
6. **Set acceptance criteria before the next evaluation.** For example:
   - beat the age+hashtag rule (about 73% accuracy, about 72% balanced accuracy);
   - at least 60% precision in every class;
   - predicted class shares within ±3 points of the true shares.

   Evaluate on a fresh hold-out set that is large enough to have at least 100 Baby Boomers.

## Assumptions and caveats

- **Hold-out data.** I assumed `Actual Class` is correct and that this sample was not used to train the model. If it was training data, real-world performance is likely worse.
- **Representativeness.** I assumed the sample's class mix resembles production traffic. If older users are more common in production, the overall accuracy figure would change, but the per-class precision problems would remain.
- **Generation boundaries.** For the "age in bio" baseline I used ≤28 Gen Z, 29–43 Millennials, 44–59 Gen X, 60+ Baby Boomers, as inferred from the data. Stated ages fall in the labelled generation 98.7% of the time.
- **Optimistic benchmark.** The baselines and the cross-validated model were built and scored on this same sample. They show what is achievable, but they are not production estimates and could be slightly optimistic.
- **Data looks synthetic.** The data has signs of being synthetic or templated: four hashtag sets, templated bios, and names that don't match the gender field. Real Instagram data will be messier, which makes it even more important to validate on real profiles before any launch.
