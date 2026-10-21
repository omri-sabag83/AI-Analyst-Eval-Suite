# Age-group classifier v1: evaluation and deployment recommendation

## Bottom line

**Do not deploy v1 to production.** It gets **62% of profiles right** (95% CI 59–65%) on the 1,000-profile sample. That is better than always guessing the largest group (Gen Z, 46%), but not good enough to segment client data:

- **It distorts the segment sizes clients would see.** It reports Gen Z as 32% of users when the real figure is 46%. It more than doubles Baby Boomers (9% vs 4%) and inflates Gen X (17% vs 10%).
- **Its Gen X and Baby Boomer segments are mostly the wrong people.** Only 27% of profiles labelled "Gen X" really are Gen X, and only 37% of those labelled "Baby Boomers" really are Boomers.
- **Its confidence score overstates how often it is right.** Average confidence is 75%, but it is correct only 62% of the time. Even predictions with confidence of 0.9 or higher are right only 80% of the time.
- **It ignores clear signals that are already in its inputs.** A simple model I fitted on the same inputs reached **about 83% accuracy** under cross-validation. The current model has a lot of room to improve, and fixing it looks easier than starting over.

## Data and assumptions

- One sheet, 1,000 profiles, one row each. There are no missing values and no duplicate IDs. Columns: actual class, predicted class, confidence, user name, bio, gender, hashtags, posts/likes rate, and average word count.
- Actual class mix: Gen Z 458, Millennials 401, Gen X 103, Baby Boomers 38.
- Assumptions:
  1. `Actual Class` is correct ground truth.
  2. The sample is representative of production traffic. If it is not, the segment-size bias described below will be different in production.
  3. The data looks templated: there are only 4 hashtag sets and a few bio phrases. Absolute numbers may not carry over exactly to real Instagram data, but the comparisons between models and between segments should still hold.
- The 83% benchmark comes from 5-fold cross-validation on this same sample. It is a rough estimate of what is achievable, not a production-ready model.

## Findings

### 1. Overall and per-class performance

| Actual \ Predicted | Baby Boomers | Gen X | Gen Z | Millennials | Total |
|---|---|---|---|---|---|
| Baby Boomers | **34** | 2 | 0 | 2 | 38 |
| Gen X | 29 | **45** | 4 | 25 | 103 |
| Gen Z | 17 | 34 | **276** | 131 | 458 |
| Millennials | 13 | 85 | 38 | **265** | 401 |
| Total predicted | 93 | 166 | 318 | 423 | 1,000 |

| Class | Precision | Recall | F1 | Actual n |
|---|---|---|---|---|
| Baby Boomers | 0.37 | 0.89 | 0.52 | 38 |
| Gen X | 0.27 | 0.44 | 0.34 | 103 |
| Gen Z | 0.87 | 0.60 | 0.71 | 458 |
| Millennials | 0.63 | 0.66 | 0.64 | 401 |

Overall: accuracy 0.62, balanced accuracy 0.65, macro-F1 0.55, Cohen's kappa 0.43 (only moderate agreement).

- **Gen Z** has the largest segment and the largest volume of errors. When the model says Gen Z it is usually right (87%), but it misses 40% of real Gen Z users. 131 of them are labelled Millennials, 34 Gen X and 17 Baby Boomers.
- **Millennials → Gen X** is the second-largest error (85 profiles). Real Millennials make up half of everything the model calls "Gen X".
- **Gen X** is the weakest class on both measures: it finds only 44% of real Gen X users, and only 27% of its Gen X labels are correct.
- **Baby Boomers** are rarely missed (89% found), because the model assigns the label very freely. 59 of its 93 Boomer labels go to younger people, including 17 Gen Z users.
- Some errors are implausible. Of the 290 profiles whose bio says "Student" (all really Gen Z or Millennials), 40 were labelled Baby Boomers or Gen X.

### 2. Client-facing impact: segment sizes are biased

| Segment | True share | Share reported by model | Error |
|---|---|---|---|
| Gen Z | 45.8% | 31.8% | −14.0 pp |
| Millennials | 40.1% | 42.3% | +2.2 pp |
| Gen X | 10.3% | 16.6% | +6.3 pp (×1.6) |
| Baby Boomers | 3.8% | 9.3% | +5.5 pp (×2.4) |

A client asking "what do Boomers share?" would get an answer that comes mostly (63%) from younger users. The older segments are the smallest and probably the most valuable to clients, and they are also the most contaminated.

### 3. The confidence score is overconfident

| Confidence band | Profiles | Avg confidence | Actual accuracy |
|---|---|---|---|
| 0.50–0.60 | 212 | 0.55 | 0.40 |
| 0.60–0.70 | 206 | 0.66 | 0.58 |
| 0.70–0.80 | 189 | 0.76 | 0.65 |
| 0.80–0.90 | 224 | 0.86 | 0.71 |
| 0.90–1.00 | 169 | 0.95 | 0.80 |

Confidence does rank predictions in a useful order: higher confidence means higher accuracy (AUC 0.66 for separating right from wrong predictions). But in every band it overstates accuracy by 10–15 points. Filtering on confidence does not rescue the model either. Keeping only predictions at 0.8 or above leaves 41% of profiles at 75% accuracy, and keeping 0.9 or above leaves 20% at 78%. Throwing away most of the data would also bias coverage in its own way.

### 4. Why it fails: it under-uses signals that are already in its inputs

- **It handles stated ages well.** 157 bios state an age ("Age: 24"), and the model gets all 157 right. On the other 843 profiles, accuracy falls to **55%**.
- **It leans heavily on hashtags.** Its prediction matches the age group most typical of the hashtag set in 80% of cases. Hashtags are only a moderate signal, though. For example, 111 of the 180 users posting #career/#familylife/#retirement are Millennials, yet the model labels 140 of those 180 as Gen X. That pattern drives most of the Millennial → Gen X errors.
- **It ignores strong bio keywords.** In this sample, "Professor" is always Gen X (12/12) but the model gets only 42% of them right. "Grandparent" is always a Boomer. "Senior Director" and "Parent" are 80% Millennials, yet the model is right only 53% and 52% of the time on those groups.
- **Engagement features carry signal.** Older groups have higher posts/likes rates (median 1.85 for Boomers vs 0.95 for Gen Z) and longer posts (median 14 words vs 8).
- **Benchmark.** A plain logistic regression using only these inputs reached **83% accuracy and 0.72 macro-F1** in 5-fold cross-validation, against 62% and 0.55 for v1. Its main remaining weakness is still Gen X, which it mostly confuses with Millennials.
- The model's accuracy is about the same for men and women (no large gap). Gender is not one of the model's listed inputs.

## Recommendations

1. **Do not ship v1 for client segmentation.** The biased segment sizes and the low precision for Gen X and Boomers would mislead clients directly.
2. **Retrain v2 before reconsidering deployment**, with these changes:
   - Make better use of the bio text: stated ages and occupation or life-stage keywords such as Student, Parent, Grandparent, Retired, Professor and Senior Director.
   - Reduce the reliance on hashtags.
   - Weight or rebalance the classes so the small Gen X and Boomer segments are learned properly without being over-predicted.
3. **Calibrate the confidence scores** (for example with Platt or isotonic scaling) so that 0.8 means roughly 80% correct.
4. **Correct segment sizes when reporting to clients.** Whatever model ships, adjust reported group shares using the confusion matrix rather than raw prediction counts, and report uncertainty for the small segments.
5. **Agree on acceptance criteria with the business before re-evaluating.** As a suggestion:
   - overall accuracy of at least 80%;
   - precision of at least 70% for every segment that will be sold to clients;
   - predicted segment shares within ±3 pp of the true shares;
   - calibration error of no more than 5 pp.

   The evaluation should use a fresh, held-out and representative sample, with enough Gen X and Boomer profiles to measure them reliably. This sample has only 38 Boomers, so the Boomer precision estimate is wide (95% CI 27–47%).
6. **Check whether the data reflects real Instagram profiles.** This sample looks templated, so v2 should also be tested on real, messy profiles before go-live.
