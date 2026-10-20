# Appointment No-Shows: Drivers and SMS Reminder Recommendation

## Bottom line

1. **Keep the SMS reminder programme and expand it. Do not cut it.** In the raw numbers, patients who got an SMS missed *more* appointments (27.6% vs 16.7%). That comparison is misleading. SMS is only ever sent for appointments booked **3 or more days ahead**, and those appointments have far higher no-show rates whatever happens. When we compare like with like (same booking lead time), patients who got an SMS no-show **about 3–5.5 percentage points less** (roughly a 10–17% relative reduction).
2. **The biggest driver of no-shows is how far ahead the appointment was booked.** Same-day appointments: 4.6% no-show. Appointments booked 2+ weeks out: about 33%. The next strongest predictor is **a patient's own history of missing appointments**. After that come age (teens and young adults miss most, over-60s least) and being on the welfare programme (`Scholarship`).
3. **What to do:** shorten booking lead times where possible. Send reminders for every appointment booked in advance, not just the ~59% of eligible ones that get one today. Add extra contact (a second reminder or a confirmation call) for patients who have missed before and for long-lead bookings.

## Data and assumptions

- 110,527 appointments for 62,299 patients. Appointment dates run 29 Apr – 8 Jun 2016, about six weeks. The overall no-show rate is **20.2%** (22,314 no-shows).
- Lead time = appointment date minus booking date, in calendar days. `AppointmentDay` has no time of day, so same-day bookings count as 0.
- I excluded 5 rows where the appointment comes before the booking (all recorded as no-shows, so probably data errors) and 1 row with age −1. That leaves 110,521 rows.
- There are no missing values and no duplicate appointment IDs. `Handcap` runs 0–4, so I treated it as a level rather than a yes/no flag.
- **Limitations:** the data covers only about six weeks. It has no cost data, no reason codes and no clinic or specialty field. SMS was **not randomly assigned**, so every SMS effect below is an observational estimate, not a measured causal effect.

## Finding 1: SMS looks harmful in the raw data only because of who gets it

| Booking lead time | Appointments | No-show rate | Share sent an SMS |
|---|---|---|---|
| Same day (0) | 38,562 | 4.6% | 0% |
| 1–2 days | 11,938 | 22.7% | 0% |
| 3–7 days | 20,247 | 25.0% | 57% |
| 8–14 days | 12,025 | 30.5% | 58% |
| 15–30 days | 17,371 | 32.6% | 61% |
| 31+ days | 10,378 | 33.0% | 61–64% |

No appointment booked less than 3 days ahead ever received an SMS. The "no SMS" group is therefore dominated by low-risk same-day visits, and that is the whole reason SMS looks bad in the raw comparison.

**Like-for-like comparison.** This uses only the 60,021 appointments booked 3+ days ahead, where SMS was actually in use:

| Lead time | No-show, no SMS | No-show, SMS | Difference |
|---|---|---|---|
| 3–7 days | 26.6% | 23.8% | −2.8 pp |
| 8–14 days | 33.8% | 28.1% | −5.6 pp |
| 15–30 days | 36.9% | 29.8% | −7.1 pp |
| 31–60 days | 38.4% | 31.5% | −6.9 pp |
| 61+ days | 33.9% | 25.5% | −8.4 pp |
| **All eligible** | **32.7%** | **27.6%** | **−5.1 pp** |

I checked how robust this is. All estimates are reductions in no-show probability from receiving an SMS:

| Method | Estimated effect |
|---|---|
| Matched on exact lead day (105 lead-day groups) | −5.5 pp |
| Logistic regression controlling for lead time, age, sex, welfare, conditions, weekday | −5.5 pp (95% CI −4.7 to −6.2) |
| Linear model adding neighbourhood; errors clustered by patient | −5.2 pp (±0.8) |
| Adding booking month | −5.4 pp |
| **Same patient compared with themselves** (6,219 patients who had appointments both with and without an SMS) | **−2.7 pp (±1.2)** |

- The two groups look alike on what we can measure: similar age (37.5 vs 37.7), similar welfare, hypertension and diabetes rates, and similar lead time.
- The same-patient comparison removes stable differences between patients that we can't observe, so it is the most conservative figure. I treat **−2.7 to −5.5 pp as the plausible range**.
- The benefit appears in every age group and in both welfare groups.
- **Caveat:** for bookings made in June 2016 (2,675 appointments, mostly short-lead), SMS and non-SMS no-show rates were the same (22.3% vs 21.9%). The overall pattern is consistent, but this is worth watching.

**What it is worth (estimate, not measured).** SMS reached 35,482 appointments in the six-week window.
- At 2.7–5.5 pp, that suggests roughly **1,000–1,950 no-shows avoided** in six weeks.
- Cutting the programme would be expected to *add* about that many.
- Sending reminders to the 24,539 eligible appointments that currently get none could avoid roughly **650–1,350** more.
- We have no cost data. Even so, SMS usually costs very little per message, so the case for keeping it is strong unless costs are unusually high.

## Finding 2: What drives no-shows

Effects below come from a model that includes all factors at once (average marginal effect on no-show probability). The model has AUC 0.73, which is moderate: useful for prioritising patients, not for predicting individual no-shows reliably.

| Factor | Raw no-show rates | Adjusted effect |
|---|---|---|
| **Lead time** | 4.6% same day → 25% (3–7 d) → ~33% (15+ d) | Same-day bookings −25 pp; risk keeps rising with longer lead |
| **Previous no-show** (earlier in this window) | 29.1% vs 17.0% for those who always attended | +8.2 pp (vs first visit); −2.0 pp if always attended |
| **Age** | Teens 13–18: 26.1%; 19–30: 24.7%; 61–75: 14.9% | Teens +5.5 pp, over-60s −6 to −8 pp (vs under-5s) |
| **Welfare (`Scholarship`)** | 23.7% vs 19.8% | +3.1 pp |
| Alcoholism | 20.1% vs 20.2% raw | +4.5 pp adjusted (members are older, which hides the effect in the raw rate) |
| Diabetes, hypertension | lower raw rates (older patients) | small or none once age is controlled |
| Gender, weekday | 20.3% F vs 20.0% M; 19–21% across weekdays | negligible |
| Neighbourhood | 15.7%–28.9% across the 54 neighbourhoods with 500+ appointments | partly reflects age, welfare and lead-time mix |

The risks compound. Patients with a previous no-show whose appointment was booked 31+ days ahead missed **54%** of appointments. First-time or reliable patients booked the same day missed about **3–4%**.

"Previous no-show" only counts misses earlier in the same six-week window, so it understates how much each patient's history matters.

## Recommendations

1. **SMS programme: keep it and expand it.**
   - Send reminders for **all** appointments booked 3+ days ahead. Today about 41% of them get none, and the data doesn't show why.
   - Consider extending reminders to appointments booked 1–2 days ahead. These have a 22.7% no-show rate and currently receive no SMS. We have no data on how SMS performs at this lead time, so test it rather than assume.
2. **Run a proper test.** Randomly hold back SMS (or a second reminder) for a small share of eligible appointments for 4–8 weeks. That would replace the observational 2.7–5.5 pp estimate with a measured effect, and would show whether 1–2-day and two-reminder versions are worth it. This is the only way to settle the cost-effectiveness question with confidence.
3. **Reduce lead times.** No-show risk rises sharply with days between booking and visit. Where capacity allows, offer more same-day and next-few-days slots. For long-lead bookings, send a reminder close to the date and ask patients to confirm or cancel, so freed slots can be rebooked.
4. **Target the high-risk patients.** Use a simple risk flag (prior no-show, long lead, age 13–30, welfare recipient) to trigger extra contact: a second SMS, a phone call, or controlled overbooking in high-risk slots.
5. **Fix data collection.** Record why SMS was or wasn't sent, when it was sent, delivery status, cancellations, and clinic or specialty. These gaps currently limit how precisely the programme can be judged.
