# Appointment no-shows: what drives them, and what to do about SMS reminders

## Bottom line

1. **Keep the SMS reminder programme and expand it.** The raw numbers make SMS look harmful: patients who got an SMS missed 27.6% of appointments, against 16.7% for those who didn't. That comparison is misleading. SMS was only ever sent for appointments booked **3 or more days ahead**, and those appointments have a much higher no-show rate whatever happens. When we compare like with like, SMS **lowers** no-shows by about **4–5 percentage points**, from roughly 33% to 28% among eligible appointments. That is about a 15% relative reduction. Over the ~6 weeks of data it works out to about **1,700–1,900 fewer missed appointments** (≈300 per week).
2. **The main driver of no-shows is how far ahead the appointment was booked.** Same-day appointments: 4.6% no-show. 1–2 days ahead: ~23%. More than a week ahead: 30–34%. Appointments booked 3+ days ahead make up 54% of appointments but **80% of all no-shows**.
3. **The other strong drivers are:** a previous no-show by the patient (29% vs 17%), age (teenagers and young adults are highest at ~25%; people 55+ are lowest at ~15–16%), and welfare enrolment (`Scholarship`, 23.7% vs 19.8%). Neighbourhood also varies, from 15% to 29%. Gender, hypertension and disability make little or no difference once other factors are accounted for.

## Data and assumptions

- 110,527 appointments for 62,299 patients. Appointment dates run 29 Apr – 8 Jun 2016 (about 6 weeks); booking dates go back to Nov 2015. Overall no-show rate: **20.2%**.
- Lead time = appointment date minus booking date, in calendar days. I dropped 5 rows with negative lead time because they are impossible. A handful of odd ages (−1, >100) were kept; they don't affect the results.
- "Previous no-show" only counts appointments inside this 6-week window. Patients' earlier history isn't in the data, so this measure understates how much history matters.
- Nothing about why an SMS was or wasn't sent is in the data. I worked out the sending rule from the pattern in the data (below).

## Finding 1: The raw SMS comparison is confounded by lead time

| Days between booking and appointment | Appointments | No-show rate | Share with SMS | No-show, no SMS | No-show, SMS |
|---|---|---|---|---|---|
| 0 (same day) | 38,563 | 4.6% | 0% | 4.6% | — |
| 1 | 5,213 | 21.4% | 0% | 21.4% | — |
| 2 | 6,725 | 23.8% | 0% | 23.8% | — |
| 3 | 2,737 | 23.5% | 33% | 24.6% | 21.3% |
| 4–7 | 17,510 | 25.2% | 61% | 27.1% | 24.0% |
| 8–14 | 12,025 | 30.5% | 58% | 33.8% | 28.1% |
| 15–30 | 17,371 | 32.6% | 61% | 36.9% | 29.8% |
| 31–60 | 8,283 | 34.2% | 61% | 38.4% | 31.5% |
| 61+ | 2,095 | 28.4% | 64% | 33.9% | 25.5% |

No appointment booked fewer than 3 days ahead ever got an SMS. Those appointments include the very reliable same-day bookings, and they make up the entire "no SMS" baseline that the raw comparison uses. **Within every lead-time band, SMS recipients miss fewer appointments.**

## Finding 2: An SMS outage gives a clean test that SMS works

On seven appointment days (9, 13, 16, 17, 18, 19 and 20 May 2016), **nobody received an SMS**, even though appointments on those days had the usual mix of lead times. On every other day, about 82% of eligible (3+ day) appointments got one. This works like a natural experiment, because whether a patient was reminded depended on the date of the appointment, not on anything about the patient.

| Eligible appointments (booked 3+ days ahead) | Appointments | SMS coverage | No-show rate |
|---|---|---|---|
| Normal SMS days | 43,437 | 82% | **28.6%** |
| Outage days | 16,584 | 0% | **32.5%** |

- Difference: **+3.9 points** on outage days (+4.4 after adjusting for lead time). A 95% confidence interval from resampling appointment days is +2.4 to +5.5 points.
- **Placebo check:** appointments booked 0–2 days ahead never get SMS. On outage days and normal days they had the *same* no-show rate (8.9% vs 8.9%). So the outage days were not simply "bad days" for some other reason.
- The rise appears in every lead-time band, every patient-history group and almost every age group. It is largest among patients with a previous no-show (+6.0 points) and young children (+6.1 points).
- Only 82% of patients on normal days got an SMS. Scaling the gap up to a per-message effect gives **≈5 points per SMS sent**.
- A separate regression check agrees. It is a logistic/linear model of eligible appointments controlling for lead time, age, gender, welfare, chronic conditions, previous no-show and weekday, with errors clustered by patient. It gives SMS an odds ratio of **0.77 (95% CI 0.74–0.80)**, or **−5.2 points (−6.0 to −4.5)**.

**The cost of the outage:** about 16,600 eligible appointments went without reminders, which likely led to **~650–700 extra no-shows** in that week and a half.

## Finding 3: Who misses appointments

Results from the adjusted model (eligible appointments, all factors considered together):

| Factor | Raw no-show rate | Effect after adjustment |
|---|---|---|
| Booked 15–60 days ahead vs 3 days | 33–34% vs 23.5% | strongest effect |
| Previous no-show in window | 29.1% (vs 17.0% if attended before) | OR 1.69 vs first-timers |
| Age 13–25 | ~25–26% | highest-risk ages |
| Age 55+ | ~15–16% | lowest-risk ages (OR ≈0.55–0.6 vs ages 0–5) |
| Welfare (`Scholarship`) | 23.7% vs 19.8% | OR 1.25 |
| Alcoholism flag | 20.1% (raw, no difference) | OR 1.5 once age is accounted for |
| Neighbourhood (≥200 appts) | from 14.6% to 28.9% | wide spread, e.g. Santos Dumont, Santa Cecília, Itararé |
| Gender, hypertension, disability, weekday | within ~1–2 points | negligible |

Same-day appointments are probably a different kind of visit (walk-ins or urgent care). So the 4.6% rate does **not** mean that switching to same-day booking would cut no-shows by that much. What it does show is that **the long wait between booking and visit is where the problem lies**.

## Recommendations

1. **Keep SMS. Don't cut it.** It is the one intervention in the data with clear evidence that it works: about 1 no-show avoided for every ~20 messages, at a cost of a text message each.
2. **Make sure every eligible appointment gets an SMS.** About 18% of eligible appointments on normal days (~8,000 in 6 weeks) still got none. Whole days went unreminded in mid-May. Set up monitoring so that a day with zero SMS sent triggers an alert straight away.
3. **Expand to appointments booked 1–2 days ahead.** These are ~12,000 appointments with a 23% no-show rate and no reminders at all today. This is untested, so roll it out as a **randomised pilot** (for example, alternating days or patient-ID parity) and measure the effect.
4. **Target extra effort at high-risk appointments.** These are long-lead bookings, patients with a previous no-show, ages 13–25, welfare recipients, and the high-rate neighbourhoods. Options to test: a second reminder close to the visit, a confirm/cancel reply that frees the slot, or a phone call.
5. **Shorten the gap between booking and visit where possible.** No-show risk rises steadily as lead time grows. Ways to do this include releasing slots closer to the date, keeping more same-day or short-notice capacity, and running waitlists that backfill cancelled slots. For long-lead slots that stay unavoidable, consider careful overbooking based on predicted no-show risk.
6. **Measure properly from now on.** Record why each SMS was or wasn't sent, and what time it went out. Run future changes as controlled tests so the programme's value can be shown directly rather than worked out after the fact.

## Limitations

- The data covers about 6 weeks for one network, from 2016. Effects may differ today.
- The SMS effect comes from an observational natural experiment, not a randomised trial. The placebo check and the agreement between the two methods make it credible, but a deliberate test would be stronger.
- Patient history is limited to the window, and there is no data on appointment type, clinic or specialty, travel distance, or reminder timing. Any of these may explain part of the lead-time and neighbourhood effects.
