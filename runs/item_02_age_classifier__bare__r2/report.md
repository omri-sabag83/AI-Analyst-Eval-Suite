# Age-group classifier v1: evaluation and deployment recommendation

## Recommendation: do not deploy to production yet

The model gets about **62% of profiles right**. The main problem is in the older groups. When it says "Gen X" it is right **27%** of the time, and when it says "Baby Boomers" it is right **37%** of the time. It also leans older across the board: it moves Gen Z users into Millennials and Millennials into Gen X. The age mix it would report to clients is therefore noticeably wrong: Gen Z is undercounted by about 14 points, and Gen X and Boomers together are overcounted by about 12 points. Clients buy exactly these segment views, so these errors would reach them directly.

The model can be fixed. A simple lookup on one of its inputs (the hashtags) already beats it, and a basic model built on its own five inputs does much better (details below). The next step is a short retraining cycle, not a launch.

---

## 1. Headline performance (n = 1,000 labelled profiles)

| Metric | Value |
|---|---|
| Accuracy | **62.0%** (95% CI ≈ 59–65%) |
| Balanced accuracy (average recall over the 4 classes) | 64.9% |
| Macro F1 | 0.55 |
| Cohen's kappa | 0.43 (moderate agreement) |
| Always predict the largest group ("Gen Z") | 45.8% |
| Simple rule: predict from the hashtag set alone | **68.5%** |

The model beats always guessing the largest group, but it **loses to a one-line rule that uses only the hashtags**.

## 2. Where it goes wrong

Confusion matrix (rows = actual age group, columns = predicted):

| Actual \ Predicted | Gen Z | Millennials | Gen X | Boomers | Total |
|---|---|---|---|---|---|
| **Gen Z** | **276** | 131 | 34 | 17 | 458 |
| **Millennials** | 38 | **265** | 85 | 13 | 401 |
| **Gen X** | 4 | 25 | **45** | 29 | 103 |
| **Boomers** | 0 | 2 | 2 | **34** | 38 |
| Total predicted | 318 | 423 | 166 | 93 | 1,000 |

| Class | Precision (when it says X, how often is it X?) | Recall (of real X, how many does it find?) | F1 |
|---|---|---|---|
| Gen Z | 0.87 | 0.60 | 0.71 |
| Millennials | 0.63 | 0.66 | 0.64 |
| Gen X | **0.27** | 0.44 | 0.34 |
| Baby Boomers | **0.37** | 0.90 | 0.52 |

Key patterns:

- **It skews older.** Of the 380 errors, 309 (81%) put the user in an older group than their real one, and only 71 put them in a younger one. Most errors are one generation off (310). Another 70 are two or three generations off, for example 17 Gen Z users labelled Baby Boomers.
- **It misses 40% of Gen Z**, the largest group. 131 Gen Z users are labelled Millennials. Most of these (100) have the typical Gen Z hashtags (#yolo/#viral/#trending), so the evidence was there and the model did not use it.
- **Gen X and Boomer predictions are mostly wrong.** Of 166 "Gen X" predictions, 85 are actually Millennials and 34 are Gen Z. Of 93 "Boomer" predictions, 59 are younger users. These are small groups, and a client looking at them would be looking mostly at the wrong people.

### Impact on what clients would see (segment sizes)

| Age group | True share | Share the model reports | Error |
|---|---|---|---|
| Gen Z | 45.8% | 31.8% | **−14.0 pts** |
| Millennials | 40.1% | 42.3% | +2.2 pts |
| Gen X | 10.3% | 16.6% | **+6.3 pts (≈ 1.6×)** |
| Baby Boomers | 3.8% | 9.3% | **+5.5 pts (≈ 2.4×)** |

In a client report, the "Boomer" segment would be about 2.4 times its real size and roughly 63% made up of younger users. Any insight about "what Boomers share" would mostly describe Gen Z and Millennials.

## 3. Why it underperforms: it relies almost entirely on hashtags and ignores stronger signals

- **It is mostly a hashtag lookup.** Each profile has one of four hashtag sets, and each set fits one generation (#yolo/#viral/#trending → Gen Z, #foodie/#travel/#workhard → Millennials, #career/#familylife/#retirement → Gen X, #classics/#grandparents/#history → Boomers). In 79.6% of cases the model's prediction is exactly the class its hashtag set suggests. Even so, it makes that lookup *less* accurately than the plain rule (62% vs 68.5%).
- **It ignores clear bio signals.** The 243 profiles whose bio starts with "Student." are all Gen Z (178) or Millennials (65); none are Gen X or Boomers. The model still labels 40 of them Gen X or Boomers. Likewise, "Parent." and "Senior Director." bios are never Gen Z in this sample, but the model calls 18 of them Gen Z. Accuracy on these profiles is only 41–44%.
- **The "#career #familylife #retirement" hashtag set is the biggest single error.** The model treats it as Gen X (140 of 180), but 62% of those users are actually Millennials.
- **The two numeric inputs carry signal the model doesn't seem to use.** Posts/likes ratio and average word count rise steadily with age (average word count: Gen Z 8.3, Millennials 9.9, Gen X 12.1, Boomers 14.0).

**Evidence that there is room to improve:** I fitted a plain logistic regression on the same five inputs (hashtag set, bio prefix, gender, posts/likes ratio, word count), using 5-fold cross-validation on this sample. It reached **79% accuracy** with default settings. With class balancing it reached **73% accuracy and 70% balanced accuracy**, and Gen X recall rose from 44% to 46% while Gen X precision went from 27% to about 30%. It also no longer called students Boomers. This is only a rough benchmark (see caveats), but it shows the inputs support a clearly better model.

## 4. Confidence scores are meaningful but overstated

The model's confidence does rank predictions sensibly: higher confidence means higher accuracy. But the stated confidence is consistently too high:

| Confidence band | n | Stated confidence (avg) | Actual accuracy |
|---|---|---|---|
| 0.50–0.60 | 212 | ~0.55 | 40% |
| 0.60–0.70 | 206 | 0.66 | 58% |
| 0.70–0.80 | 189 | 0.76 | 65% |
| 0.80–0.90 | 224 | 0.86 | 71% |
| 0.90–1.00 | 169 | 0.95 | 80% |

Filtering on confidence does not rescue the model. Keeping only predictions at ≥0.8 confidence raises accuracy to only 75%, and 59% of profiles are dropped. Keeping ≥0.9 gives 78% accuracy on 20% of profiles. This also leaves an unrepresentative sample for segmentation.

## 5. Fairness check: gender

Accuracy is 60.4% for women (n = 659) and 65.1% for men (n = 341). This gap is modest and within what sampling noise could produce at these sizes. The pattern of errors is the same for both. It is worth monitoring but is not the main issue.

## 6. Recommended next steps

1. **Do not ship v1 to clients.** If a segmentation is urgently needed, a transparent hashtag-plus-bio rule would be more accurate (≥68.5%) than v1. Even then, Gen X and Boomer segments should be labelled low-reliability.
2. **Retrain using all available inputs:** bio keywords such as Student/Parent/Senior Director/Retired, hashtags, posts/likes ratio and word count. Handle class imbalance with class weights or resampling, because Gen X and Boomers are only 14% of the data.
3. **Recalibrate the confidence scores** (e.g. Platt/isotonic scaling) so that "0.9" really means about 90%. Clients can then filter on confidence, or the company can apply a "can't tell" threshold.
4. **If clients use segment sizes, report bias-corrected shares.** The confusion matrix above can be used to adjust the predicted segment shares toward the true mix.
5. **Agree acceptance criteria before the next review.** For example: overall accuracy ≥ 75%, precision ≥ 0.6 for every class, each segment's share within ±3 pts of truth, and a calibration error below 0.05. Measure these on a fresh holdout set that was not used for training.
6. **Collect more labelled Gen X and Boomer profiles.** With only 103 and 38 examples, metrics for these groups are imprecise. Boomer recall of 0.90 has a 95% CI of roughly 0.76–0.97.
7. **Check that the sample matches production.** The bios and hashtags here are highly templated (5 bio texts, 4 hashtag sets). Real Instagram profiles will be messier, so the next evaluation should use real data.

## Assumptions and caveats

- `Actual Class` is treated as ground truth. Because label quality cannot be checked here, all errors are attributed to the model.
- The 1,000 profiles are assumed to be representative of the production population and not to have been used to train v1.
- The 79%/73% logistic-regression figures are cross-validated on this same 1,000-row sample. They are a rough benchmark, not a production estimate.
- Bio "prefixes" (Student/Parent/Senior Director/Retired) were extracted from the bio text. Hashtag order was ignored, since each profile has one of four sets of three tags in varying order.
- User name was not used as an evaluation feature (all names are unique and carry no obvious age signal in this sample).
