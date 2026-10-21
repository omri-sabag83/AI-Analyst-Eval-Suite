# Appointment No-Shows: Drivers and the SMS Reminder Programme

## Bottom line

1. **Keep the SMS programme and expand it.** SMS reminders work. They cut the no-show rate by about **5 percentage points** for the appointments that get them: roughly 33% → 28%, a relative drop of about 15%. The raw data seems to show the reverse (SMS recipients miss 27.6% of appointments, non-recipients 16.7%). That gap is an artefact of *which* appointments get an SMS, not an effect of the SMS.
2. **The biggest driver of no-shows is lead time,** meaning the gap between booking and the appointment. Same-day appointments are missed 4.6% of the time. Appointments booked a week or more ahead are missed 30–34% of the time.
3. **The second driver is the patient's own record of missed appointments,** followed by age (teenagers and young adults miss most). Other patient attributes have only small effects.
4. **Recommendations:** send an SMS for every eligible appointment (about 18% currently get none), keep the system from failing (a week-long gap in May cost around 650 extra no-shows), test reminders for appointments booked 1–2 days ahead, shorten lead times where possible, and give high-risk bookings extra follow-up (a phone call or overbooking).

## Data and assumptions

- `appointments.csv`: 110,527 appointments for about 62,000 patients. Appointment dates run from 29 Apr to 8 Jun 2016; bookings go back to Nov 2015. The overall no-show rate is **20.2%**.
- I dropped 5 rows whose appointment date is before the booking date (data errors) and 1 row with age −1. The single Saturday (14 May, 39 appointments) is excluded from the outage analysis.
- Lead time = appointment date minus booking date, in calendar days.
- "Prior history" counts the patient's earlier appointments *within this dataset only*. The data covers only about 6 weeks of appointments, so history is truncated and many patients look like first-timers.
- I assume `SMS_received` records whether a reminder was actually sent and received for that appointment.

## 1. Why the raw SMS comparison is misleading

SMS is **only ever sent for appointments booked 3 or more days ahead**. Not one appointment booked 0–2 days ahead received an SMS. Short-notice appointments have very low no-show rates, so the no-SMS group is full of low-risk appointments. Compare like with like, within each lead-time band, and SMS recipients miss *fewer* appointments in every band:

| Lead time (days) | No-show, no SMS | No-show, SMS | Appointments (no SMS / SMS) |
|---|---|---|---|
| 0 (same day) | 4.6% | – | 38,563 / 0 |
| 1–2 | 21–24% | – | 11,938 / 0 |
| 3 | 24.6% | 21.3% | 1,831 / 906 |
| 4–7 | 27.1% | 24.0% | 6,868 / 10,642 |
| 8–14 | 33.8% | 28.1% | 5,021 / 7,004 |
| 15–30 | 36.9% | 29.8% | 6,851 / 10,520 |
| 31–60 | 38.4% | 31.5% | 3,224 / 5,059 |
| 60+ | 33.9% | 25.5% | 744 / 1,351 |

This is a classic Simpson's paradox. Anyone judging the programme on the raw 27.6% vs 16.7% gap would wrongly conclude that SMS increases no-shows.

## 2. Evidence that SMS causes the reduction: a natural experiment

Within lead-time bands, the SMS and no-SMS groups could still differ in other ways. The data contains a much cleaner test. On **seven appointment days (9 May, 13 May, and 16–20 May)**, *no* eligible appointment received an SMS. On every other weekday, 76–84% of eligible appointments did. This looks like a programme outage or pause that had nothing to do with the patients themselves.

| | Normal days | Outage days | Change |
|---|---|---|---|
| Eligible appointments (lead time ≥ 3 days), SMS coverage | 82% | 0% | |
| Eligible appointments, no-show rate | 28.6% | **32.5%** | **+3.9 pts** |
| Short-notice appointments (never get SMS), no-show rate | 8.92% | 8.92% | **0.0 pts** |

Short-notice appointments act as a control group. Their no-show rate did not move at all during the outage week, so the rise among eligible appointments is not a bad-week effect. A difference-in-differences regression gives **+3.9 points (95% CI 2.2–5.7)**. It controls for appointment day, lead-time band, age, prior attendance, gender, welfare enrolment (the dataset's `Scholarship` flag) and conditions, with standard errors clustered by day. Coverage normally reaches only 82% of eligible appointments, so **the effect per SMS sent is about 4.8 points.**

Three independent approaches give the same answer:

| Method | Effect of SMS on no-show probability |
|---|---|
| Outage difference-in-differences, scaled per SMS | −4.8 pts |
| Instrumental variable (day-level SMS coverage as instrument) | −5.1 pts (SE 0.5) |
| Regression with controls on eligible appointments (lead time, age, history, conditions, weekday, neighbourhood) | −4.9 pts (CI −5.6 to −4.1) |

SMS and non-SMS recipients are also similar on age, welfare enrolment, chronic conditions and prior history, which supports these estimates.

**What this means in practice:** about **1 no-show is avoided for every 20 SMS sent.** The outage week alone is estimated to have caused about **650 extra missed appointments** (16,600 eligible appointments × 82% normal coverage × 4.8 pts).

## 3. What drives no-shows

The table below shows effects from a linear probability model on all appointments, with all factors entered together. Each figure is the change in no-show probability in percentage points.

| Driver | Effect | Comment |
|---|---|---|
| **Lead time**, vs same day | +20 (1–2 days), +24 (3–7), +29 (8–14), +31 (15–30), +33 (31–60) | By far the largest driver. 35% of appointments are same-day, with a 4.6% no-show rate. Appointments booked 3+ days ahead make up about 80% of all no-shows. |
| **Prior missed appointment** | +11 vs patients who attended all prior visits | The raw rate climbs with the number of earlier misses: 18.7% (0), 27.1% (1), 30.7% (2), 43.2% (3+). |
| **Age** | Teens (13–18) +5, ages 19–30 +3; ages 46–60 −5, 61–75 −8, 76+ −6 (vs ages 0–12) | Teens and young adults miss most; older adults least. |
| **SMS reminder** | −5 | See above. |
| **Alcoholism** | +4 | |
| **Welfare enrolment (`Scholarship`)** | +3 | |
| Diabetes | +2 | Small. |
| Gender, hypertension, disability, weekday | 0 to ±1 | Not meaningful. Hypertension looks protective in the raw data only because it tracks with older age. |
| Neighbourhood | Raw rates range from about 16% to 29% (among areas with 500+ appointments) | Highest: Santos Dumont, Santa Clara, Itararé, Jesus de Nazareth. Worth a local look, but partly overlaps with the factors above. |

**The model can target outreach usefully.** A simple risk model trained on earlier dates scores an AUC of 0.74 on later dates (1.0 is perfect, 0.5 is chance). The 20% of appointments it ranks riskiest have a 36% no-show rate and account for **39% of all no-shows**. The bottom 30% have a no-show rate of about 3%.

## 4. Recommendations

**On the SMS programme: keep it and expand it. Do not cut it.**

1. **Close the coverage gap.** On normal days, about 18% of eligible appointments still get no SMS. Coverage is weakest for appointments booked exactly 3 days ahead (33% get one). Full coverage would avoid an estimated **~380 no-shows** over a period like this one (≈7,900 uncovered eligible appointments × 4.8 pts).
2. **Make the system reliable.** The week-long gap in May cost about 650 missed appointments. Monitor daily send volumes and set an alert if they drop to zero.
3. **Pilot SMS for appointments booked 1–2 days ahead.** These are not covered today, and their no-show rate is high (21–24%; about 12,000 appointments, or 12% of all no-shows). The effect has not been measured for this group. Run a randomised pilot (for example, alternate days or patients) rather than assuming the 5-point effect carries over.
4. **Shorten lead times where clinically possible.** Lead time is the strongest driver. Options include more same-day or short-notice slots, and asking patients booked far ahead to re-confirm.
5. **Target extra effort at high-risk bookings.** Use the risk factors above (long lead time, earlier misses, age 13–30, welfare enrolment) to flag about the top 20% of appointments. Give them a phone call or a second reminder, or overbook those slots. Patients with 3 or more earlier misses (43% no-show rate) are the clearest group to start with.
6. **Measure future changes properly.** Do not judge the programme by comparing recipients with non-recipients. That raw comparison points the wrong way. Use randomised rollout or holdout days.

## Limitations

- The outage was not a planned experiment. Its cause is unknown, and its timing (mid-May) could coincide with other events. However, the unchanged rate among short-notice appointments that same week argues against any general shock.
- The data covers only about 6 weeks of appointments, so prior-attendance history is incomplete and seasonal patterns cannot be assessed.
- The data has no cost information (for SMS or for a missed slot), so I cannot compute return on investment. At 1 avoided no-show per ~20 messages, the programme is very likely cost-effective, since SMS is cheap compared with a wasted clinic slot.
- The SMS effect is estimated only for appointments booked 3 or more days ahead. Whether it applies to shorter lead times is unknown, which is why recommendation 3 is a pilot.
