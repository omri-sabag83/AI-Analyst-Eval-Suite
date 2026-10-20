# Age-group classifier v1: evaluation and deployment recommendation

## Bottom line

**Do not deploy this model to production yet.**

- On the 1,000-profile sample it labels **62%** of profiles correctly. Most of that comes from profiles where the bio simply states the person's age.
- On the 84% of profiles without a stated age, accuracy is **55%**.
- It mislabels users as *older* than they are far more often than younger. That inflates the Gen X and Baby Boomer segments: fewer than 3 in 10 users labelled Gen X really are Gen X, and fewer than 4 in 10 labelled Baby Boomer are.
- A one-line rule that only looks at the user's hashtags is as good as the model, and on raw accuracy it is better.
- A simple model fitted on the same inputs reaches roughly 73–79%. So there is clear room to improve, and this should be treated as a v1 to iterate on, not a dead end.

Evidence tags used below: [OBS] = computed directly from the data; [CON] = the conclusion the evidence best supports; [HYP] = plausible explanation, not proven.

## Data and method

- **What the data is:** `model_evaluation_sample.xlsx`, a single sheet with 1,000 rows, one per profile and a unique `User_ID`. There are no missing values and no duplicate rows. Labels are clean: four classes, no spelling variants.
- **Class mix in the sample:** Gen Z 458, Millennials 401, Gen X 103, Baby Boomers 38.
  - The sample is heavily skewed to younger users.
  - Results that depend on class mix (overall accuracy, precision) are **only valid for this sample**. They will change if the production population has a different age mix.
  - For that reason I also report per-class recall and balanced accuracy, which don't depend on the mix.
- **Assumptions:**
  - `Actual Class` is correct ground truth. Where checkable it looks consistent: the 157 bios that state an age ("Age: 34") all fall in the right generation band. Age 28 appears under both Gen Z and Millennials, which fits a birth-year cut-off.
  - How the sample was drawn, and how labels were obtained for profiles without a stated age, is **not documented**. This should be confirmed.
- **Data features that matter for the evaluation:**
  - Hashtags take only **4 distinct sets** (e.g. `#trending #viral #yolo`, `#career #familylife #retirement`), each shown in different orders.
  - 157 bios (16%) state the user's age outright.
  - 380 bios start with a role word: "Student", "Parent" or "Retired".
- **Methods:** confusion matrix, per-class metrics, bootstrap 95% confidence intervals, a comparison with simple baselines, and a confidence calibration check.

## Findings

### 1. Overall performance is modest [OBS]

| Metric | Value |
|---|---|
| Accuracy | **62.0%** (95% CI 59–65%) |
| Always predicting "Gen_z" (majority class) | 45.8% |
| Balanced accuracy (mean per-class recall) | 64.9% |
| Macro F1 | 0.55 |
| Cohen's kappa | 0.43 (moderate agreement) |

Confusion matrix (rows = actual, columns = predicted):

| Actual \ Predicted | Gen_z | Millennials | Gen_x | Baby Boomers | Recall |
|---|---|---|---|---|---|
| Gen_z (458) | **276** | 131 | 34 | 17 | 60% |
| Millennials (401) | 38 | **265** | 85 | 13 | 66% |
| Gen_x (103) | 4 | 25 | **45** | 29 | 44% |
| Baby Boomers (38) | 0 | 2 | 2 | **34** | 89% |
| **Precision** | 87% | 63% | **27%** | **37%** | |

### 2. The headline accuracy is propped up by bios that state the age [OBS]

- **Bios with "Age: N" (157):** 100% correct. That is a trivial case, close to reading the answer.
- **The other 843 profiles:** **54.9% correct**, with balanced accuracy of 58%. This is the case that matters, because most real profiles won't state an age.

### 3. Errors are biased toward older age groups, which distorts segment sizes [OBS]

- Of 380 errors, **309 (81%) predict an older group** than the true one and only 71 predict a younger one.
- The two biggest errors:
  - Gen Z labelled as Millennials: 131 profiles.
  - Millennials labelled as Gen X: 85 profiles.
- The client-facing deliverable is segment shares, and the model gets them materially wrong (within this sample):

| Segment | Actual share | Model's share |
|---|---|---|
| Gen Z | 45.8% | 31.8% |
| Millennials | 40.1% | 42.3% |
| Gen X | 10.3% | 16.6% |
| Baby Boomers | 3.8% | 9.3% |

- So a client would be told Gen X and Boomers are 1.6× and 2.4× bigger than they are, and Gen Z is about a third smaller.
- Any insight attributed to "Gen X" would be **73% driven by other generations**, mostly Millennials.

### 4. The model behaves almost like a hashtag lookup, and the lookup's mapping is wrong for older groups [OBS / HYP]

- The model's prediction matches a simple hashtag rule on 80% of profiles. The rule:
  - `#trending/#viral/#yolo` → Gen Z
  - `#foodie/#travel/#workhard` → Millennials
  - `#career/#familylife/#retirement` → Gen X
  - `#classics/#history/#grandparents` → Boomers
- That rule on its own scores **68.5%**, against 62.0% for the model.
  - On raw accuracy the gap is +6.5 points (95% CI +3.7 to +9.3; McNemar p < 0.001).
  - On balanced accuracy the two are statistically level: 66.4% vs 64.9%, CI −1.4 to +4.2.
  - The rule wins on Gen Z. The model is slightly better on the other three groups. Either way, **the model adds little beyond the hashtags** [CON].
- The data doesn't support the stereotyped mapping for older groups:
  - Only 23% of `#career/#familylife/#retirement` users are Gen X; **62% are Millennials**.
  - Only 33% of `#classics/#history/#grandparents` users are Boomers.
- [HYP] This looks like a model trained on class-balanced data or hand-picked "typical" examples, then applied to a population dominated by younger users. That would explain both the over-prediction of older classes and the high Boomer recall paired with low Boomer precision. Confirming it needs the training set's class mix and the feature importances.
- The model also under-uses strong signals that are already available:
  - **"Student"** bios: 211 are Gen Z and 79 Millennial, never older. Yet the model labels 40 of them Gen X or Boomer.
  - **Posting style** differs clearly by age. Median avg. word count is 8 for Gen Z vs 14 for Boomers. Median post/likes rate is 0.95 for Gen Z vs 1.85 for Boomers.

### 5. Confidence scores rank errors only weakly and overstate accuracy [OBS]

| Confidence band | Profiles | Actual accuracy |
|---|---|---|
| 0.50–0.60 | 212 | 40% |
| 0.60–0.70 | 206 | 58% |
| 0.70–0.80 | 189 | 65% |
| 0.80–0.90 | 224 | 71% |
| 0.90–1.00 | 169 | 80% |

- Higher confidence does mean more likely correct, but only weakly: AUC 0.66 for separating right from wrong predictions.
- Confidence also runs about 10–15 points above actual accuracy in every band.
- So confidence can't yet be used as a reliable filter. Keeping only predictions above 0.9 would keep 17% of profiles and still be wrong 1 time in 5.

### 6. There is clear room to improve with the same inputs [OBS, estimate]

I fitted a plain logistic regression on the same inputs: hashtag set, bio role word, word count and post/likes rate. With **no use of the stated age**, 5-fold cross-validation gives:

- **78.6% accuracy** (balanced 64%), or
- **73.4% accuracy / 70% balanced accuracy** with class weighting.

These are both well above the model's 62% / 65%.

Caveat: this baseline was trained and tested on the same 1,000-profile evaluation sample, which is small and may not represent production. Treat it as evidence of headroom, not as a benchmark to promise.

### 7. Gender: watch item, not a finding [OBS]

- Accuracy is 60% for profiles labelled female vs 65% for male.
- Within classes the gap is mostly inside Gen Z (58% vs 66%); the other classes are within 3 points.
- The sample is small, so this should be monitored in the next evaluation rather than acted on.

## Recommendation

**Not ready for production** [CON]. Accuracy on realistic profiles (no stated age) is 55%, the model makes systematic "too old" errors, and segment shares are distorted. Client deliverables built on it would overstate Gen X and Boomer audiences and misattribute Millennial behaviour to them. This conclusion was checked independently (all figures reproduced). The one nuance: the "hashtag rule beats the model" result holds on raw accuracy, but on balanced accuracy they are only level.

### Next steps

1. **Fix the class-prior / calibration problem first.** Retrain, or at minimum re-weight the output probabilities, on data whose age mix matches the production population, and recalibrate confidence (e.g. temperature or isotonic scaling). This targets the "too old" bias directly.
2. **Use the signals the model under-uses:** an age stated in the bio (as a rule-based override), role words (Student / Parent / Retired), word count and post/likes rate. The simple baseline suggests this alone could lift accuracy into the 70s.
3. **Set acceptance criteria before the next review**, measured on a held-out sample of profiles *without* stated ages:
   - per-class recall and precision (especially Gen X and Boomers);
   - segment-share error (e.g. each segment within ±3 points);
   - calibration error;
   - beating the hashtag-only rule on both raw and balanced accuracy.
4. **Get a larger, documented evaluation set.** 38 Boomers and 103 Gen X are too few for tight per-class estimates. Document how profiles were sampled and how ground-truth ages were obtained.
5. **Interim option if a client needs something now:**
   - Report only Gen Z vs "Millennial+" (Gen Z precision is already 87%).
   - Or correct the aggregate segment shares with the confusion matrix (inverting the misclassification rates).
   - Don't label individual profiles as Gen X or Boomer.
