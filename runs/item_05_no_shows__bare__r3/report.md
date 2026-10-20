# Appointment No-Shows: Drivers, SMS Reminders, and Recommendations

## Summary

- **Overall no-show rate: 20.2%** (22,319 of 110,527 appointments, Apr 29 – Jun 8 2016, 62k patients, 81 neighbourhoods).
- **SMS reminders work. Keep the programme and expand it.** At first glance the data say the opposite: patients who got an SMS missed 27.6% of appointments, against 16.7% for those who didn't. That gap is misleading. SMS is only sent when an appointment is booked **3 or more days ahead**, and those appointments have far more no-shows to begin with. Compared like for like, an SMS **reduces no-shows by about 4–5 percentage points**, from about 30% to about 25%, a relative drop of roughly 15–17%. Three separate methods give the same answer, including a natural experiment described below.
- **The biggest driver is lead time**, meaning the days between booking and the appointment. Same-day appointments: 4.6% no-show. Booked 1–2 days ahead: about 22%. Booked more than 2 weeks ahead: about 33%.
- **Other drivers:** having missed an appointment before (29% vs 17% for patients who always attended); age (teens and young adults 25–27%, over-55s about 15–16%); being on the welfare programme ("Scholarship", 24% vs 20%); alcoholism. Sex, hypertension, disability and day of the week make little or no difference.

## 1. Data and assumptions

- One row per appointment. Lead time = appointment date minus booking date, in calendar days. Booking timestamps include a time of day, but appointment dates don't, so I compared dates only.
- I removed 6 invalid rows: 5 with the appointment dated before the booking, and 1 with age −1. That leaves 110,521 rows. The 7 patients aged over 100 were kept.
- "Prior history" means a patient's earlier appointments **within this 6-week window** (anything before Apr 29 is not in the data). Patients with several appointments on the same day are counted in the order they appear.
- `Scholarship` is assumed to mean enrolment in a welfare programme, a marker of low income.
- Everything here is observational. For the SMS question I lean on a natural experiment (Section 3) rather than on simple comparisons.

## 2. What drives no-shows

| Factor | Group | No-show rate | Appointments |
|---|---|---|---|
| **Lead time** | Same day (0 days) | **4.6%** | 38,562 |
| | 1–2 days | 22.7% | 11,938 |
| | 3–6 days | 24.4% | 15,341 |
| | 7–14 days | 29.4% | 16,931 |
| | 15–30 days | 32.6% | 17,371 |
| | 31–60 days | 34.2% | 8,283 |
| **Patient history** | Missed at least one earlier appointment | **29.1%** | 15,965 |
| | Attended all earlier appointments | 17.0% | 32,258 |
| | First appointment seen in the data | 19.5% | 62,298 |
| **Age** | 13–17 | 26.6% | 6,343 |
| | 18–25 | 25.1% | 11,220 |
| | 56–65 / 66–75 / 76+ | 15.8% / 15.1% / 16.1% | 27,504 |
| **Welfare (Scholarship)** | Yes vs No | 23.7% vs 19.8% | 10,861 / 99,666 |
| **Neighbourhood** (≥500 appts) | Worst: Santos Dumont, Santa Clara, Itararé | 26–29% | |
| | Best: Do Cabral, Santa Martha, Jardim da Penha | 16% | |
| **Not important** | Sex (F 20.3%, M 20.0%), disability, weekday (19–21%) | | |

The direction of each effect holds in a multivariable logistic regression. It includes lead-time band, age band, sex, welfare, chronic conditions, alcoholism, disability, prior history and SMS, with standard errors clustered by patient. Adjusted odds ratios:
- Lead time, relative to same-day: 1–2 days **6.8×**, 3–6 days 8.4×, 7–14 days 10.0×, 15–30 days 12.3×, 31–60 days 13.4×.
- Prior no-show **1.77×**; prior full attendance 0.87× (both relative to a first appointment).
- Age 13–17: 1.49×; age over 65: 0.62× (both relative to under-5s).
- Welfare 1.23×, alcoholism 1.36×, diabetes 1.16×.
- **SMS received: 0.77×.**

Lead time is by far the strongest factor. Same-day appointments make up 35% of all bookings but very few of the no-shows.

## 3. SMS reminder programme: does it work?

### Why the simple comparison is wrong
| | No-show rate |
|---|---|
| SMS received | 27.6% |
| No SMS | 16.7% |

The SMS share by lead time is 0% for lead times of 0–2 days, 33% at 3 days, and about 60% beyond that. So the "no SMS" group is mostly same-day and next-day bookings, which hardly ever no-show. This comparison measures lead time, not reminders.

### Like-for-like comparisons (appointments with lead time of 3+ days only)
| Lead time | No SMS | SMS | Difference |
|---|---|---|---|
| 3–6 days | 26.2% | 23.1% | −3.1 pp |
| 7–14 days | 32.0% | 27.5% | −4.6 pp |
| 15–30 days | 36.9% | 29.8% | −7.1 pp |
| 31–60 days | 38.4% | 31.5% | −6.9 pp |
| 61+ days | 33.9% | 25.5% | −8.4 pp |

- Standardised to the same mix of lead times (exact day): **−5.5 pp**.
- Logistic regression (controls: lead time, age, sex, welfare, conditions, prior history, weekday): average effect **−5.3 pp**.

### Natural experiment: days when no reminders were sent
On 7 appointment dates (May 9, 13, 16–20), **not one** eligible appointment received an SMS. On every other weekday about 80% did. This looks like an operational gap, not a decision about which patients to remind, so it gives a fair comparison:

| | Normal days | No-SMS days |
|---|---|---|
| Lead time 3+ days (eligible): SMS coverage | 81.7% | 0% |
| Lead time 3+ days (eligible): no-show rate | 28.6% | **32.5%** |
| Lead time 0–2 days (never sent SMS): no-show rate | 8.9% | 8.9% |

- After adjusting for lead time, age, history, welfare and weekday (errors clustered by date), eligible appointments on no-SMS days had **+3.9 pp more no-shows (95% CI +2.5 to +5.3)**.
- The comparison group, appointments that never get an SMS, showed **no change (+0.1 pp, CI −0.9 to +1.1)**. So the rise was not a general bad patch for attendance. It was specific to the appointments that lost their reminders.
- The rise appears in every lead-time band (e.g. 15–30 days: 31.2% → 36.7%).
- Scaling up for 82% coverage gives about **−4.8 pp per SMS actually sent**. That matches the regression estimate.

**Conclusion:** each SMS prevents roughly 1 no-show for every 20 reminders sent. Cutting the programme would raise no-shows on reminded appointments by about 4–5 pp. With about 35k reminded appointments in 6 weeks, that is **about 1,700 extra missed appointments per 6 weeks**.

Caveats:
- The no-SMS days fall in one stretch of mid-May, so some timing effect can't be ruled out completely. The flat rate in the comparison group argues against it.
- The data contain no costs, so the cost-effectiveness case rests on SMS costing far less than a wasted clinic slot. That is almost always true.

## 4. Recommendations

1. **Keep the SMS programme and expand it.** Cutting it is not supported by the evidence. The negative raw comparison is an artefact of who gets sent a reminder.
2. **Close the coverage gaps.**
   - About 18% of eligible appointments get no SMS even on normal days. That share is higher among patients with a prior no-show (76% covered vs 84% for first-timers) and among over-65s (75%). Collect and verify mobile numbers at booking.
   - Monitor delivery daily. A 7-day lapse like the one in May should trigger an alert.
3. **Extend reminders to appointments booked 1–2 days ahead.** These 11,900 appointments get no SMS today, yet they no-show at 21–24%, almost as high as 3–6-day bookings. Roll this out as a **randomised pilot** (e.g. alternate days or patient IDs), so the effect is measured directly.
4. **Shorten lead times where possible.**
   - Same-day and near-term booking is the strongest lever: 4.6% no-show same-day vs over 30% beyond two weeks.
   - Add same-day/next-day capacity, use waitlists to fill earlier slots, and avoid booking more than 2 weeks out where clinically appropriate.
   - For long-lead bookings, add a second reminder close to the date, with an easy way to confirm or cancel.
5. **Target extra contact at high-risk patients.** Prior no-show, age 13–25, welfare recipients, alcoholism, and long lead time. Use a phone call, a confirmation request or extra reminders. For example, a prior no-shower booked 15+ days out is likely above 40% risk. Free cancelled slots for the waitlist, and consider **targeted overbooking** of slots held by high-risk patients.
6. **Look into the high-rate neighbourhoods** (Santos Dumont, Santa Clara, Itararé, Jesus de Nazareth, Ilha do Príncipe; 23–29%). Barriers such as transport or opening hours may be fixable locally.
7. **Measure going forward.**
   - Record why each SMS was or wasn't sent, and the outcome after any rescheduling.
   - Run any change to the programme (timing, content, number of reminders) as a randomised test, so future decisions don't rely on confounded comparisons like the raw SMS figures.
