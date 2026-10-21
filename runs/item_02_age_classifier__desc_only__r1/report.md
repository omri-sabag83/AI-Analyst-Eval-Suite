# Age-group classifier v1: evaluation and deployment recommendation

## Bottom line

**Don't deploy v1 to production yet.** It gets 62% of profiles right, against 46% for a rule that always guesses "Gen_z". That gain is too small for client-facing segmentation, and the errors are not random. Three problems stand out:

1. **The segment sizes it would give clients are wrong.** It reports 9.3% Baby Boomers when the true figure is 3.8% (2.4×), and 16.6% Gen_x when the true figure is 10.3% (1.6×). It reports 31.8% Gen_z when the true figure is 45.8%, so Gen_z is undercounted by about 30%.
2. **Two of the four segments would be mostly the wrong people.** 73% of profiles labelled "Gen_x" are not Gen_x. 63% of profiles labelled "Baby Boomers" are not Baby Boomers.
3. **It throws away information it already has.** The model leans mostly on hashtags and misreads clear cues in the bio. A simple model I trained on the same inputs, as a test, reached about 81% accuracy. So this is fixable. The next step is a v2 rebuild, not abandoning the project.

## Data and assumptions

- 1,000 profiles in one sheet. No missing values and no duplicates. True class mix: Gen_z 458, Millennials 401, Gen_x 103, Baby Boomers 38.
- **Assumption:** `Actual Class` is reliable ground truth, and the sample is representative of production traffic and was not used to train the model. If either is false, these results are optimistic.
- **Data-quality flag:** the `Gender` field looks unrelated to the user's name. For example, "Olivia" is tagged Male 18 times and Female 12 times, and "Frank" is tagged Female 24 times. Every first name appears with both genders. Gender isn't one of the model's stated inputs, but this suggests the sample may be partly synthetic or badly joined. That should be checked before trusting any evaluation on this data, including this one.

## Performance

| Metric | Value |
|---|---|
| Accuracy | **62.0%** (95% bootstrap CI 59–65%) |
| Baseline: always predict "Gen_z" | 45.8% |
| Balanced accuracy (average recall over classes) | 64.9% |
| Macro F1 | 0.55 (CI 0.51–0.59) |
| Cohen's kappa | 0.43 (moderate agreement) |

Confusion matrix (rows = actual, columns = predicted):

| Actual \ Predicted | Baby Boomers | Gen_x | Gen_z | Millennials | Recall |
|---|---|---|---|---|---|
| Baby Boomers (38) | **34** | 2 | 0 | 2 | 89% |
| Gen_x (103) | 29 | **45** | 4 | 25 | 44% |
| Gen_z (458) | 17 | 34 | **276** | 131 | 60% |
| Millennials (401) | 13 | 85 | 38 | **265** | 66% |
| **Precision** | **37%** | **27%** | 87% | 63% | |

What this means for each segment:
- **Gen_z** (the largest group): when the model says Gen_z it is usually right (87% precision). But it misses 40% of real Gen_z users, mostly labelling them Millennials (131 of them). So Gen_z audiences come out too small.
- **Gen_x and Baby Boomers:** the model sends too many people into these groups. 85 Millennials and 34 Gen_z users end up in "Gen_x". 30 of the 93 profiles labelled "Baby Boomers" are actually Gen_z or Millennials. Any client insight about older audiences would be driven mainly by younger users.
- Errors are not limited to neighbouring generations. 17 Gen_z users were labelled Baby Boomers and 34 were labelled Gen_x.

## Confidence scores: useful for ranking, not as probabilities

| Confidence | Profiles | Actual accuracy | Mean stated confidence |
|---|---|---|---|
| 0.50–0.60 | 212 | 40% | 0.55 |
| 0.60–0.70 | 206 | 58% | 0.66 |
| 0.70–0.80 | 189 | 65% | 0.76 |
| 0.80–0.90 | 224 | 71% | 0.86 |
| 0.90–1.00 | 169 | 80% | 0.95 |

Higher confidence does mean higher accuracy. But the model is overconfident everywhere, by about 10–15 points. Filtering on confidence doesn't fix it either. Keeping only predictions at 0.8 or above keeps 41% of profiles and lifts accuracy only to 75%. Keeping 0.9 or above keeps 20% of profiles at 78% accuracy. Neither cut is good enough to make the model shippable, and dropping most profiles would also skew the segments.

## Why it fails (diagnostics)

The inputs are highly templated. There are only four hashtag sets, and bios combine a role (Student, Parent, Retired, Senior Director, or none) with a hobby phrase, sometimes with "Age: NN." added.

- **It mostly follows the hashtags.** Map each hashtag set to its obvious generation (#yolo/#viral → Gen_z, #foodie/#travel → Millennials, #career/#retirement → Gen_x, #classics/#grandparents → Baby Boomers). The model's prediction matches that mapping for 79.6% of profiles. Hashtags are a noisy signal, though: for example, 111 of the 180 #career/#familylife/#retirement users are actually Millennials. The model inherits that noise. On its own, the hashtag mapping is right 68.5% of the time, which is better than the model.
- **It ignores bio cues that rule out a generation.** In this sample, no "Student" is Gen_x or Baby Boomer, and no "Retired" user is Gen_z or Millennial. Even so, the model made 43 predictions that contradict these cues (for example, Student → Baby Boomers), and all 43 were wrong.
- **It is perfect only when the bio states the age.** The 157 profiles with "Age: NN" in the bio were 100% correct. On the other 843 profiles, accuracy is **55%**, only about 9 points better than the "always Gen_z" baseline. Gen_x accuracy on those profiles is 32%. Most production profiles probably won't state an age, so 55% is the more realistic expectation.

**Headroom check.** I trained a simple gradient-boosting model as a test, on the same inputs: hashtag set, bio role, stated age if present, posts-to-likes ratio and word count. Under 5-fold cross-validation it reached **80.8% accuracy and macro F1 of 0.67**, against 62% and 0.55 for v1. This is a rough benchmark on a small sample, not a replacement model. Rare classes remain hard (Gen_x F1 is about 0.48). But it shows the gap is mostly in the model, not a lack of signal in the inputs.

## Recommendations

1. **Hold the production release.** If a client urgently needs something, offer at most Gen_z vs. "everyone else", where precision is 87%. Even then, adjust audience sizes for the known undercount. Don't publish Gen_x or Baby Boomer segments from v1.
2. **Build v2 that uses the features properly:** parse bio roles and stated ages as structured features, treat hashtags as one noisy signal among several, and use the engagement and word-count features. Handle the class imbalance (only 3.8% Baby Boomers and 10.3% Gen_x) with class weights or resampling.
3. **Calibrate the confidence scores** (for example with isotonic or temperature scaling) so that a confidence of 0.8 actually means about 80% correct. Then route low-confidence profiles to "unknown" instead of forcing a label.
4. **Fix the evaluation set first.** Confirm how `Actual Class` was obtained, explain the gender–name mismatch, and evaluate on a larger, held-out sample of real profiles that matches production. Include enough Gen_x and Baby Boomer users that their metrics are stable (at least 200 per class is a reasonable target).
5. **Agree acceptance criteria before v2 is reviewed.** Two suggestions:
   - Precision and recall of at least 0.75 for every class, plus correct segment shares.
   - Every segment's predicted share within ±2 percentage points of the true share, since that is what clients actually consume.

   If individual-level accuracy stays limited, also consider correcting aggregate segment shares using the confusion matrix, rather than counting raw predictions.
