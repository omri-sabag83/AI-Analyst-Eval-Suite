# Age-group classifier v1: evaluation and deployment recommendation

## Bottom line

**The model should not go to production as it is.**

- **Overall:** it gets the age group right for 62% of the 1,000 sample profiles.
- **Profiles that state their age:** about 16% of profiles write "Age: NN" in their bio. On those the model is 100% correct, because the answer is written in the bio.
- **Everyone else:** on the other 84% of profiles it is right only **55%** of the time.
- **Against a one-line rule:** a rule that only looks at which hashtag set a profile uses gets 68% of those profiles right, so it beats the model.
- **Segment sizes for clients:** the model would make Gen_z look much smaller than it is (32% of predictions vs 46% actual). It would make Gen_x and Baby Boomers look much bigger (17% vs 10%, and 9% vs 4%).
- **Confidence score:** it can't yet be trusted to filter predictions. Even predictions with confidence of 0.9 or more are wrong 1 time in 5.

Simple models built on the same public inputs reach about 80% accuracy in cross-validation. A better model is clearly possible, and the next step is to fix this one rather than give up on the idea.

Labels used below: **[OBS]** is computed directly from the data. **[CON]** is the conclusion the evidence best supports. **[HYP]** fits the data but isn't proven.

---

## 1. Data and method

- **What's in the sample:** `model_evaluation_sample.xlsx` has one row per Instagram profile, 1,000 rows in total. There is no time dimension. Columns are the true class, the predicted class, the model's confidence, and the inputs (user name, bio, hashtags, average word count, posts-to-likes rate), plus `Gender`.
- **Data quality [OBS]:**
  - No missing values and no duplicate users.
  - The data looks heavily templated, possibly synthetic. There are only 4 hashtag sets (the same 3 tags in different orders), around 56 distinct bio templates, and user names built from a small pool of first and last names.
  - The four hashtag sets are #yolo/#viral/#trending, #workhard/#travel/#foodie, #career/#familylife/#retirement and #history/#classics/#grandparents.
  - `Gender` is in the file but isn't one of the model's stated inputs.
- **Label quality [OBS]:**
  - We don't know how the true labels were obtained.
  - Where a bio states an age (157 profiles), the label always matches the generation that age implies. Gen_z covers ages 15–28, Millennials 28–43, Gen_x 44–59 and Baby Boomers 63–72. The only overlap is at age 28, which is the expected cohort boundary.
  - So the labels look internally consistent.
- **Class mix (in this sample):** Gen_z 458 (45.8%), Millennials 401 (40.1%), Gen_x 103 (10.3%), Baby Boomers 38 (3.8%).
  - We don't know whether this matches the Instagram population the clients care about.
  - All figures here describe this sample only. Overall accuracy will change if the production class mix is different.
- **Assumptions:**
  - I assume this sample is held out, i.e. not used to train the model. If it was used in training, real performance will be worse than reported here.
  - "Stated age" means the bio matches `Age: <number>`.
  - Confidence intervals are 95% bootstrap intervals.

## 2. Findings

### 2.1 Headline accuracy is modest, and most of it comes from a giveaway

| Group of profiles | n | Accuracy (95% CI) | Macro-F1 |
|---|---|---|---|
| All profiles | 1,000 | **62.0%** (59–65%) | 0.55 |
| Bio states "Age: NN" | 157 | **100%** | 1.00 |
| No stated age | 843 | **54.9%** (52–58%) | 0.48 |
| *Baseline: always predict "Gen_z"* | 1,000 | 45.8% | 0.16 |

- **[OBS]** 0.157 × 100% + 0.843 × 54.9% = 62.0%.
- **[CON]** The stated-age profiles lift the headline number. They need no model at all, since a simple text lookup would do. The 55% on the other profiles is the honest measure of what the model adds.
- **[OBS]** Confidence is almost the same on stated-age profiles (average 0.75) and on the rest (0.76). The confidence score therefore doesn't recognise when the answer is certain.

### 2.2 A one-line hashtag rule beats the model

Each profile uses exactly one of the four hashtag sets. The rule maps each set to the generation it obviously suggests, e.g. #yolo/#viral/#trending → Gen_z and #history/#classics/#grandparents → Baby Boomers.

| Method | Accuracy, all | Accuracy, no stated age | Macro-F1, no stated age |
|---|---|---|---|
| Model v1 | 62.0% | 54.9% | 0.48 |
| Hashtag rule | 68.5% | 68.0% | 0.56 |
| Stated age if present, otherwise hashtag rule | 72.8% | 68.0% | 0.56 |
| Simple logistic regression / small decision tree (5-fold cross-validation) | ~80% | ~80% | — |

The simple models use hashtag set, word count, posts-to-likes rate and bio keywords (Student, Retired, Parent, Senior Director and so on).

- **[OBS]** On profiles without a stated age, the rule beats the model by 13 points (95% CI +10 to +16). Where the two disagree, the rule is right 130 times and the model 20 times.
- **[OBS]** An independent check found the gap is concentrated in **Gen_z**:
  - The model labels 131 of the 458 real Gen_z profiles as Millennials. Its Gen_z recall is 54% on no-age profiles, against 81% for the rule.
  - Within the other three hashtag groups, the model is about as good as the rule or slightly better.
- **[HYP]** The model mostly follows the hashtags but overrides them in the wrong direction too often. It agrees with the hashtag rule on 81% of no-age profiles. We can't see inside the model, so this is an inference.
- **[OBS]** The ~80% from simple models held across 3 random splits and 2 model types (79–81%).
  - Caveat: these models were fitted and tested on this same 1,000-row sample using cross-validation. Treat 80% as a sign of what's achievable, not a validated benchmark.
  - Gen_x and Baby Boomers stay hard for them too.

### 2.3 Performance by age group: the older groups are unreliable

| True class | n | Recall (95% CI) | Precision | F1 |
|---|---|---|---|---|
| Gen_z | 458 | 60% (56–65%) | 87% | 0.71 |
| Millennials | 401 | 66% (61–71%) | 63% | 0.64 |
| Gen_x | 103 | 44% (35–53%) | **27%** | 0.34 |
| Baby Boomers | 38 | 89% (79–97%) | **37%** | 0.52 |

Confusion matrix (rows are the true class, columns the predicted class):

| | Gen_z | Millennials | Gen_x | Boomers |
|---|---|---|---|---|
| **Gen_z** (458) | 276 | 131 | 34 | 17 |
| **Millennials** (401) | 38 | 265 | 85 | 13 |
| **Gen_x** (103) | 4 | 25 | 45 | 29 |
| **Boomers** (38) | 0 | 2 | 2 | 34 |

- **[OBS]** Almost all errors push people into an *older* group. Of the 380 errors, 309 predict an older generation than the true one.
- **[OBS]** Of the profiles the model calls Gen_x, 73% are not Gen_x. Of those it calls Baby Boomers, 63% are not Boomers.
- **[OBS]** Gen_x and Boomers are small groups (103 and 38 profiles), so their confidence intervals are wide. The precision problem is still large enough to be clear.

### 2.4 What clients would see: segment sizes would be wrong

| Segment | Actual share | Model's share | Distortion |
|---|---|---|---|
| Gen_z | 45.8% | 31.8% | −14.0 pts |
| Millennials | 40.1% | 42.3% | +2.2 pts |
| Gen_x | 10.3% | 16.6% | +6.3 pts (×1.6) |
| Baby Boomers | 3.8% | 9.3% | +5.5 pts (×2.4) |

- **[OBS]** These figures are within this sample.
- **[CON]** Any client insight like "what Baby Boomers share" would be mostly built from younger users' posts, since fewer than 4 in 10 predicted Boomers are actually Boomers.
- **Estimate:** the size of the distortion in production depends on the real class mix. This is a projection, not a measured outcome.
- The hashtag rule over-predicts the same two groups (Gen_x 180, Boomers 98). Older-group signals are weak in these inputs generally, not only in this model. It still makes the model's output unfit for segment reporting.

### 2.5 The confidence score helps a little but overstates certainty

| Confidence | n | Actual accuracy | Average confidence |
|---|---|---|---|
| ≤ 0.60 | 212 | 40% | 0.55 |
| 0.60–0.70 | 206 | 58% | 0.66 |
| 0.70–0.80 | 189 | 65% | 0.76 |
| 0.80–0.90 | 224 | 71% | 0.86 |
| > 0.90 | 169 | 80% | 0.95 |

- **[OBS]** Higher confidence does mean more likely correct, but only weakly. The AUC for telling right from wrong predictions is 0.66.
- **[OBS]** The score is consistently 10–15 points over-confident. On profiles without a stated age, the top band (average confidence 0.95) is right 76% of the time.
- **[CON]** Filtering to "high-confidence only" would not make the output reliable, and it would throw away most of the data.

## 3. Recommendation

**[CON] Do not deploy v1.** Its usable accuracy (55% on profiles without a stated age) is below a trivial hashtag rule. It systematically inflates the older segments clients would pay for. Its confidence score overstates reliability.

This conclusion was checked by an independent re-computation from the raw file. The verdict was "holds, with caveats", and those caveats are reflected above.

Suggested next steps for the data science team:

1. **Fix the Gen_z → Millennials confusion first.** It accounts for most of the gap to the hashtag rule.
2. **Handle stated ages with a rule.** Pull them out of the bio and map them deterministically. Report model accuracy only on profiles without a stated age.
3. **Set an explicit bar before the next review.** For example: on a held-out set without stated ages, beat the hashtag-rule baseline on both accuracy and macro-F1, reach at least ~0.5 precision for Gen_x and Boomers, and keep each segment's predicted share within a few points of its true share. Simple models reached ~80% here, so the bar is realistic.
4. **Fix the class imbalance.** Gen_x and Boomers are 14% of the sample. Collect more labelled older users, or use class weighting.
5. **Calibrate the confidence score** (e.g. temperature or isotonic scaling) so that "0.9" really means 90%.
6. **Adjust aggregate shares.** If clients mainly need segment *sizes*, correct the predicted shares using the confusion matrix rather than counting raw predictions.
7. **Answer the open data questions:**
   - Was this sample held out from training?
   - How were the true labels obtained?
   - How does the sample's age mix compare with the real client population?
   - Is the templated look of the data representative of real profiles? Real bios and hashtags will be much messier, and performance on real data needs its own test.
   - Confirm `Gender` is not a model input. If it is to be used, check for fairness. Accuracy is similar across genders here: 60% for female, 65% for male.
