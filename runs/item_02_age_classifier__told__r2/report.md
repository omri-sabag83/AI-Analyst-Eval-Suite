# Age-group classifier (v1): evaluation and deployment recommendation

## Bottom line

**The model is not ready for production.**

- **Overall accuracy is 62%.** That figure is inflated: 16% of profiles state their age in the bio ("Age: 24"), and the model gets every one of those right.
- **On the other 84%, accuracy is 55%.** That is barely above the 47% you would get by always guessing "Gen_z".
- **The two older classes are mostly wrong when predicted.**
  - When the model says **Gen_x**, it is right only **27%** of the time.
  - When it says **Baby Boomers**, it is right only **37%** of the time.
- **Segment shares delivered to clients would be distorted.**
  - Gen Z would be reported as 32% of profiles instead of 46%.
  - Baby Boomers would be reported as 9% instead of 4%.
- **The confidence score overstates reliability.**
- **The model leaves a lot of accuracy unused.** A plain logistic regression on the same inputs reaches about 80% accuracy in cross-validation on this sample.

**Next step:** retrain and re-evaluate against agreed acceptance criteria (below) before any client use.

## Data and method (read first)

- **What the data is:** `model_evaluation_sample.xlsx` has 1,000 profiles, one row per profile, with no dates. Columns are the true class, the predicted class, the model's confidence, and the inputs: name, bio, gender, hashtags, posts-to-likes rate and average word count. There are no missing values and no duplicate users.
- **Unknowns.** I don't know how the sample was drawn, how the true labels were obtained, or what data the model was trained on. So **all figures are within-sample**. They describe production only to the extent this sample is representative.
- **Class imbalance.** The sample is 458 Gen_z, 401 Millennials, 103 Gen_x and 38 Baby Boomers. Baby Boomer figures in particular rest on few rows and are imprecise.
- **Inconsistent label boundary.** Among profiles that state an age, age 28 is labelled Gen_z three times and Millennials twice. The generation age bands need a written definition.
- **The inputs follow fixed templates.** There are only 4 distinct hashtag sets, and bios combine a few role words (Student, Parent, Senior Director, Retired, Professor, Grandparent) with one of five interest phrases. Real profiles will be messier, so all results, including my benchmark, are likely optimistic.
- **Assumption:** `Actual Class` is correct ground truth.

## Findings

Tags: **[OBS]** means computed directly from the data, **[CON]** is my conclusion, **[HYP]** is a hypothesis not proven by this data.

### 1. Headline performance is weak [OBS]

| Metric | Value (95% bootstrap CI) |
|---|---|
| Accuracy | **62.0%** (59–65%) |
| Macro-F1 (each class weighted equally) | **0.55** (0.51–0.59) |
| Baseline: always predict Gen_z | 45.8% |

**Results by true class (rows) vs predicted class (columns):**

| Actual \ Predicted | Gen_z | Millennials | Gen_x | Boomers | n | Recall |
|---|---|---|---|---|---|---|
| Gen_z | **276** | 131 | 34 | 17 | 458 | 60% |
| Millennials | 38 | **265** | 85 | 13 | 401 | 66% |
| Gen_x | 4 | 25 | **45** | 29 | 103 | 44% |
| Baby Boomers | 0 | 2 | 2 | **34** | 38 | 89% |
| **Precision** | 87% | 63% | **27%** | **37%** | | |

**How to read precision:** of the 166 profiles the model labels Gen_x, only 45 are actually Gen_x. Of the 93 it labels Baby Boomers, only 34 are. For a client buying an "older audience" segment, most of what they receive would be younger users.

### 2. The headline is inflated by profiles that state their age [OBS]

- **157 profiles** (15.7%) have "Age: NN" in the bio. The model is right on **157/157**.
- These profiles have roughly the same class mix as the rest, so the mix doesn't explain the perfect score. The model is effectively reading the number.
- **On the 843 profiles without a stated age, accuracy is 54.9%** and macro-F1 is 0.48. Only 8 points beat the 47% "always Gen_z" baseline on this subset.

**Precision on the 843 profiles without a stated age:**

| Class | Precision | Correct / predicted |
|---|---|---|
| Gen_z | 84% | |
| Millennials | 55% | |
| Gen_x | **18%** | 27/148 |
| Baby Boomers | **31%** | 26/85 (rough 95% range 22–41%) |

**[CON]** The 55% figure is the better measure of the model's ability to *infer* age, which is the point of the product. Reading a stated age doesn't need a model.

### 3. How the model goes wrong: it maps hashtags to stereotypes [OBS mechanism; HYP cause]

Each profile carries one of four hashtag sets. The model treats each set as a near-direct label, but those labels don't match reality:

| Hashtag set | n | Model mostly predicts | Actual mix |
|---|---|---|---|
| #career #familylife #retirement | 180 | Gen_x (140) | **Millennials 111**, Gen_x 42, Gen_z 24, Boomers 3 |
| #history #classics #grandparents | 98 | Baby Boomers (85) | Boomers 32, Gen_x 25, Gen_z 24, Millennials 17 |
| #foodie #travel #workhard | 299 | Millennials (275) | Millennials 234, Gen_z 33, Gen_x 29 |
| #trending #viral #yolo | 423 | Gen_z (296) | Gen_z 377, Millennials 39 |

- Most Gen_x and Baby Boomer false positives come from the first two sets.
- Most Gen_z misses are profiles labelled Millennials despite carrying Gen_z-typical signals.
- **[HYP]** Possible causes:
  - The model was trained on data with a different class mix, or on stereotyped rules.
  - It under-weights the posting-behaviour features, which do separate the groups. Average word count is 8.3 for Gen_z, 9.9 for Millennials, 12.1 for Gen_x and 14.0 for Boomers. Posts-to-likes rate rises from 1.00 to 1.89 in the same order.
  - Confirming this needs the training data and the model's feature weights.

### 4. Segment shares would be distorted [OBS within-sample; real impact is an estimate]

| Segment | Actual share | Share the model reports |
|---|---|---|
| Gen_z | 45.8% | **31.8%** |
| Millennials | 40.1% | 42.3% |
| Gen_x | 10.3% | **16.6%** |
| Baby Boomers | 3.8% | **9.3%** |

- If production has a similar mix, clients would see Gen Z under-counted by about a third.
- They would also see older groups inflated by 1.6–2.4×.
- The size of the error in production depends on the real population mix. Treat these figures as an estimate.

### 5. Confidence is useful for ranking, but overstated [OBS]

| Confidence band | n | Accuracy |
|---|---|---|
| 0.50–0.60 | 212 | 40% |
| 0.60–0.70 | 206 | 58% |
| 0.70–0.80 | 189 | 65% |
| 0.80–0.90 | 224 | 71% |
| 0.90–1.00 | 169 | 80% |

- Higher confidence does mean higher accuracy, so the score can be used to filter.
- But it is consistently too high: average confidence is 0.75 against 62% accuracy.
- **43 predictions** were wrong despite confidence of 0.9 or more.
- A raw confidence number can't be shown to clients as a probability.

### 6. Accuracy by gender: no significant gap, but worth watching [OBS]

- Accuracy is 60.4% for female profiles (n=659) and 65.1% for male profiles (n=341). The difference is not statistically significant (chi-square p=0.17).
- Within Gen_z the gap is 57.6% vs 66.0% (p=0.11).
- Not proven, but this should be tracked in the next evaluation.

### 7. The inputs can support a much better model [OBS on this sample; CON with caveat]

I built benchmarks with 5-fold cross-validation on this same sample. Inputs were hashtag set, bio role keyword, posts-to-likes rate and word count.

| Model | Accuracy | Macro-F1 |
|---|---|---|
| Logistic regression | **0.80** | 0.67 |
| Logistic regression + "use the stated age when present" rule | **0.83** | 0.72 |
| Gradient boosting / shallow tree / k-NN | 0.79–0.80 | 0.63–0.68 |
| Class-balanced logistic regression | 0.76 | 0.67 (Gen_x recall 61%, Boomer recall 92%) |
| **Current model** | 0.62 | 0.55 |

**Caveats:**
- The benchmark is cross-validated on the same 1,000 profiles, not on a separate held-out set. Some model types do worse: an unpruned decision tree reaches about 0.71, Naive Bayes about 0.61.
- The inputs are templated, so expect lower numbers on real data.
- **[CON]** Even so, the gap of roughly 18 points means the current model is under-using signal that is already in its inputs.
- Gen_x remains the hardest class for every model, with recall of 40–60%.

## Verification performed

- **Rigor checklist.** I checked the findings against an analysis-rigor checklist. Fixes applied: tagging observations vs hypotheses, stating data limits up front, the within-sample framing, and testing the gender gap for significance.
- **Strongest counter-argument.** Clients want *aggregate* shares, and a known error matrix can be used to correct aggregate counts. That partly holds. But the correction only works if production error rates match this sample's, and it doesn't fix per-profile segments (27% Gen_x precision) or the overconfident scores. The recommendation stands.
- **Independent re-check.** A separate analysis that saw only the claim and the raw file re-checked the key claim (62% inflated by stated-age profiles, 55% on the rest, low Gen_x/Boomer precision, simple models do much better). Verdict: **holds with caveat**. All figures reproduced and other ways of writing an age found no additional profiles. The caveat is that the benchmark result depends on model choice (0.71–0.81 for reasonable models), and Baby Boomer precision is imprecise because there are only 38 true Baby Boomers.

## Recommendations

1. **Do not deploy v1** for client segmentation.
2. **Retrain**, giving more weight to posting-behaviour features and less to the hashtag-set stereotypes.
   - Use class weighting or resampling for Gen_x and Baby Boomers.
   - When an age is stated, use it directly as a rule rather than relying on the model.
3. **Calibrate the confidence score** (e.g. isotonic or temperature scaling).
   - Set per-class thresholds.
   - Below the threshold, return "unknown" rather than a guess.
4. **Fix the labels.** Write down the generation age or birth-year bands, resolve the age-28 overlap, and document how ground truth is obtained.
5. **Re-evaluate on a fresh held-out sample** drawn from the production population.
   - Include enough Gen_x and Baby Boomers, at least ~200 each.
   - Report results separately for stated-age and non-stated-age profiles.
6. **Agree acceptance criteria before the re-test.** Suggested starting point:
   - Accuracy of at least 80% on profiles without a stated age.
   - At least 60% precision for every class.
   - Every class's predicted share within 3 points of its actual share.
   - Calibration error at most 0.05.
   - No significant accuracy gap by gender.
7. **If clients need numbers sooner:** deliver only aggregate segment shares, corrected using the error matrix measured on the new evaluation set, with error bars. Do not deliver per-profile labels for Gen_x or Baby Boomers.
