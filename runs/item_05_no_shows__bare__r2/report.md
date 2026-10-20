# Appointment no-shows: drivers and the SMS reminder programme

## Bottom line
1. **Keep the SMS programme and expand it.** At first glance SMS looks harmful: 27.6% of patients who got an SMS missed their appointment, against 16.7% of those who didn't. That comparison is misleading. Reminders are only sent for appointments booked **3 or more days ahead**, and those appointments have far higher no-show rates whatever happens. When you compare like with like, an SMS **lowers** the no-show rate by about **5 percentage points**: from about 33% to about 28%, a relative cut of about 15%.
2. **The strongest evidence is an accidental test.** On 7 weekdays in May 2016 no reminders went out at all. On those days no-shows among reminder-eligible appointments **rose by 3.9 points**. No-shows among appointments that never get reminders did not change.
3. **How far ahead the appointment is booked (lead time) drives no-shows more than anything else.** Same-day appointments: 4.6% no-show. Appointments booked 1–2 days ahead: 23%. Booked 2+ weeks ahead: 33–34%. The other strong signals are a patient's own past no-shows, and age (teenagers and young adults miss most, over-55s least).
4. **Recommendations:** make sure the SMS system cannot silently stop sending. Close the coverage gaps: about 18% of eligible appointments on normal days got no SMS, and appointments booked 1–2 days ahead never get one. Shorten booking lead times where possible. Focus extra contact on high-risk patients: those with past no-shows, long lead times, and ages 12–35.

## Data and assumptions
- 110,527 appointments for 62,299 patients. Appointment dates run from 29 Apr to 8 Jun 2016 (27 clinic days). Overall no-show rate: 20.2%.
- I dropped 5 rows where the booking date was after the appointment date, and 1 row with a negative age. That leaves 110,521 rows.
- **Lead time** = appointment date minus booking date, in calendar days. The appointment time of day is not recorded.
- Whether an SMS was sent was not randomised, so every comparison below adjusts for lead time. Results are associations unless they come from the outage test.
- "Past no-shows" counts only earlier appointments for the same patient that are inside this ~6-week dataset.

## 1. What drives no-shows

| Lead time | Appointments | No-show rate | Share sent an SMS |
|---|---|---|---|
| Same day | 38,562 | 4.6% | 0% |
| 1 day | 5,213 | 21.4% | 0% |
| 2 days | 6,725 | 23.8% | 0% |
| 3 days | 2,737 | 23.5% | 33% |
| 4–7 days | 17,510 | 25.2% | 61% |
| 8–14 days | 12,025 | 30.5% | 58% |
| 15–30 days | 17,371 | 32.6% | 61% |
| 31–60 days | 8,283 | 34.2% | 61% |
| 61+ days | 2,095 | 28.4% | 64% |

- **Lead time is the main driver.** Same-day bookings almost always attend. Once an appointment is a day or more away, the risk jumps about fivefold and keeps climbing.
- **Past behaviour:** patients with no earlier no-shows miss 17% of the time. Patients who missed more than half their earlier appointments miss 35% of the time.
- **Age:** no-show rates are 25–26% for ages 13–25 and 15–16% for ages 56 and over. In a multivariable model, ages 13–18 have about 1.5 times the odds of the 0–5 group; ages 66–75 have about 0.6 times.
- **Welfare enrolment (the `Scholarship` field):** 23.7% vs 19.8% for others. Adjusted odds about 1.25 times. This probably reflects social and economic barriers.
- **Neighbourhood:** rates range from about 16% to 29% among neighbourhoods with 500+ appointments; Santos Dumont, Santa Clara and Itararé are highest.
- **Little or no effect:** gender, day of week, hypertension, diabetes and disability make little difference. The chronic-condition groups are, if anything, slightly *more* reliable before adjustment.

## 2. Does the SMS reminder work?

**Why the raw numbers mislead.** No appointment booked 0–2 days ahead ever received an SMS. Those are the appointments with the lowest no-show rates, so they pull the "no SMS" group's rate down. Once you compare within the same lead time, SMS recipients do better in every band:

| Lead time | No-show rate, no SMS | No-show rate, SMS |
|---|---|---|
| 3 days | 24.6% | 21.3% |
| 4–7 days | 27.1% | 24.0% |
| 8–14 days | 33.8% | 28.1% |
| 15–30 days | 36.9% | 29.8% |
| 31–60 days | 38.4% | 31.5% |
| 61+ days | 33.9% | 25.5% |

I estimated the effect for eligible appointments with regression models. They adjust for exact lead time, age, gender, welfare enrolment, health conditions, neighbourhood, booking date and the patient's own no-show history. Standard errors allow for the same patient appearing more than once. The estimated SMS effect is **−4.6 to −6.2 points** in every version, with 95% confidence intervals well below zero. Restricting to each patient's first appointment gives −5.5 points.

**Natural experiment: the SMS outage.** For appointments on 9, 13, 16, 17, 18, 19 and 20 May 2016, **no** SMS went out to anyone. On every other weekday, 76–84% of eligible appointments got one. This works like an unplanned test:

| | Normal days | Outage days | Difference |
|---|---|---|---|
| Eligible (booked 3+ days ahead), share sent an SMS | 82% | 0% | |
| Eligible: no-show rate | 28.6% | 32.5% | **+3.9 points** |
| Not eligible (booked 0–2 days ahead): no-show rate | 8.92% | 8.92% | 0.0 points |

The group that never gets reminders behaved exactly the same on outage days. So the rise among eligible patients is not explained by something else happening on those dates. A difference-in-differences regression (adjusting for appointment date, lead time and patient characteristics) gives **+4.0 points (95% CI 2.9 to 5.0)**. Coverage was only 82% on normal days, so one SMS is worth about **4.8 fewer no-shows per 100 reminders sent**. This matches the regression estimates.

**What the outage cost:** about 16,600 eligible appointments were affected. At about 82% normal coverage and a 4.8-point effect, that is roughly **650 extra missed appointments** in 7 clinic days.

## 3. Recommendations

1. **Keep the SMS programme. Don't cut it.** It reliably prevents about 1 no-show per 20 messages, and texts are cheap compared with a wasted clinic slot.
2. **Make sending reliable.** Set up a daily check that alerts staff if the number of messages sent falls far below normal. A single week-long failure cost about 650 attended visits.
3. **Expand coverage:**
   - On normal days about 7,900 eligible appointments (18%) still got no SMS. Find out why (e.g. missing phone numbers) and fix it. At the measured effect, that would prevent roughly 380 no-shows over a comparable 6-week period.
   - Extend reminders to appointments booked 1–2 days ahead: about 12,000 appointments with a 23% no-show rate. The benefit for these is untested. Roll it out as a randomised pilot, e.g. send to alternate days or random halves, so the effect can be measured. If the effect is similar, it would prevent about 550 no-shows per 6 weeks.
   - Test a second reminder for appointments booked 2+ weeks ahead, where no-shows stay around 30% even with an SMS.
4. **Shorten lead times.** Same-day and next-few-days scheduling (open access) works much better than booking weeks out. Where long waits can't be avoided, add a confirm-or-cancel step a few days before so freed slots can be offered to someone else.
5. **Give extra attention to high-risk appointments.** Target long lead times, patients with past no-shows, ages 12–35, welfare recipients and the highest-rate neighbourhoods. Options include a phone call, a two-way confirmation text, or careful overbooking in those slots.

## Limitations
- The data cover only about 6 weeks in 2016. Patient history is cut off at the start of the window.
- Apart from the outage, who got an SMS among eligible appointments was not random. Something unrecorded (such as having a phone number on file) may affect both SMS receipt and attendance. The outage comparison avoids this problem and gives a consistent answer.
- The data don't record reminder cost, clinic type or appointment time, so I couldn't compute a cost-benefit ratio or analyse the effect by specialty.
