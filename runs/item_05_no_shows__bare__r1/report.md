# Appointment No-Shows: Drivers and the SMS Reminder Programme

## Summary

- **One in five appointments is missed.** 22,319 of 110,527 appointments were no-shows (20.2%). The data covers appointment dates from 29 Apr to 8 Jun 2016.
- **Keep the SMS programme and expand it.** On a raw comparison, SMS looks harmful: 27.6% of patients who got an SMS missed their appointment, against 16.7% of those who didn't. That comparison is misleading. SMS is only sent for appointments booked 3 or more days ahead, and those appointments are much more likely to be missed anyway. A clean natural experiment gives the real picture. On 7 appointment days no reminders were sent at all, and on those days no-shows among patients who would normally get an SMS rose by about **4 percentage points**. That works out to roughly **5 points (about 15%) fewer no-shows per reminder sent**, or about **one missed appointment avoided for every 20 SMS**.
- **The biggest driver is booking lead time.** Same-day bookings are missed 4.6% of the time. Bookings made 1–2 days ahead are missed about 23% of the time, and bookings made more than 2 weeks ahead 33–38% of the time. The other strong drivers are a **past no-show** (29% vs 17% for patients who attended their previous visits), **age 12–35** (23–26%), and being on the **Bolsa Família welfare programme** (`Scholarship`: 23.7% vs 19.8%).
- **Recommendations:**
  1. Keep SMS and extend it to appointments booked 1–2 days ahead, which currently get no reminder.
  2. Close the coverage gap: about 18% of appointments that qualify for a reminder never receive one.
  3. Add a second contact (a call or a second SMS) for high-risk appointments, using a simple risk score.
  4. Shorten booking lead times where possible.
  5. Put monitoring in place so that reminder outages are noticed.

## Data and assumptions

- There is one row per appointment: 110,527 appointments for 62,298 patients across 81 neighbourhoods.
- **Lead time** = appointment date minus booking date, in days. `AppointmentDay` has no time of day, so I worked in calendar days.
- I removed 5 appointments with a negative lead time (booked after the appointment date) and 1 with a negative age. That leaves 110,521 rows.
- I read `Scholarship` as enrolment in the Bolsa Família welfare programme. The dataset doesn't say this; it's an assumption.
- **"Past no-show" only looks back within the data window, which is about 6 weeks.** A patient's earlier appointments are counted only if they fall inside that window.
- There's no cost data, so I describe the SMS return in terms of messages per no-show avoided.

## 1. What drives no-shows

**No-show rate by group**

| Factor | Group | No-show rate | Appointments |
|---|---|---|---|
| **Lead time** | Same day | 4.6% | 38,563 |
| | 1–2 days | 22.7% | 11,938 |
| | 3–7 days | 25.2% | 20,247 |
| | 8–14 days | 30.6% | 12,025 |
| | 15–30 days | 32.6% | 17,371 |
| | 31–60 days | 34.2% | 8,283 |
| **Patient history** (within the window) | Previous appointments all attended | 17.0% | 32,258 |
| | First appointment seen | 19.5% | 62,298 |
| | At least one previous no-show | 29.1% | 15,965 |
| **Age** | 0–5 | 18–19% | 11,732 |
| | 13–25 | 25–26% | 17,563 |
| | 51–65 | 16.5% | 22,122 |
| | 66 and over | 15–16% | 13,301 |
| **Welfare (`Scholarship`)** | Yes | 23.7% | 10,861 |
| | No | 19.8% | 99,666 |
| **Neighbourhood** (those with ≥500 appointments) | Lowest | ~16% | |
| | Highest (e.g. Santos Dumont 28.9%, Itararé 26.3%) | up to 29% | |

I also fitted a multivariable logistic regression, so each factor is measured with the others held constant. Results are odds ratios, all p<0.001 unless stated:

- **Lead time:** OR 7–13 for any lead time versus same-day booking. This is by far the strongest effect.
- **Past no-show:** OR 1.78.
- **Age 13–18:** OR 1.46. Age 66 and over: OR 0.62 (both compared with age 0–5).
- **Alcoholism:** OR 1.36.
- **Welfare:** OR 1.24.
- **Diabetes:** OR 1.15.
- **Male:** OR 1.06.

Some factors matter little:

- Day of the week varies by only about 2 points (Thursday 19.4%, Friday 21.2%).
- Gender changes the rate by less than 1 point on its own.
- Hypertension and disability add nothing once age is taken into account.

**These are associations, not proven causes,** except for the SMS result below. For example, long lead times may partly reflect the type of appointment (such as routine follow-ups) rather than the wait itself.

**How well can no-shows be predicted?** I trained a simple model on appointments before 25 May and tested it on appointments after that date. It reached an AUC of 0.73.

- The 20% of appointments it rated riskiest had a 35% no-show rate and contained 38% of all no-shows.
- The bottom 30% had a no-show rate of about 3%. These are almost all same-day bookings.

That is good enough to decide where to spend extra outreach effort.

## 2. The SMS reminder programme

### The raw comparison is misleading

| | No-show rate |
|---|---|
| SMS received | 27.6% |
| No SMS | 16.7% |

This gap comes from who gets an SMS, not from the SMS itself:

- **No appointment booked 0–2 days ahead ever gets an SMS.** These include the same-day bookings, which have a 4.6% no-show rate.
- Coverage starts at 3 days of lead time. About 82% of appointments booked further ahead get a reminder.

So "no SMS" is mostly short-notice, low-risk appointments. **Within each lead-time band, patients who received an SMS miss fewer appointments**, for example 28.1% vs 33.8% at 8–14 days and 29.8% vs 36.9% at 15–30 days.

### A natural experiment: the reminder outage

On 7 appointment days (9 May, 13 May and 16–20 May 2016), **no SMS was sent to anyone**, including appointments that would normally get one. On every other weekday, 76–84% of qualifying appointments got a reminder. The outage depended only on the date. It had nothing to do with the patient, so it works like a randomised test.

| Qualifying appointments (booked 3+ days ahead) | SMS coverage | No-show rate |
|---|---|---|
| Normal days | 82% | 28.6% (n=43,437) |
| Outage days | 0% | **32.5%** (n=16,584) |

**Checks:**

- **Placebo test.** Appointments booked 0–2 days ahead never get an SMS, so the outage shouldn't affect them. Their no-show rate was identical on outage and normal days: 8.92% vs 8.93% (1–2 days ahead alone: 22.7% vs 22.8%). This rules out the outage days simply being bad days for attendance.
- **Comparison against the same calendar days.** I compared qualifying appointments with short-notice ones on the same dates, controlling for lead time, age and health conditions. The outage still added **+3.9 points** to no-shows among qualifying appointments.
- **Consistency across lead-time bands.** The rise was +5 to +6 points at every lead time from 8 days up, and +1.9 points at 3–7 days. It appeared in every age group, and was larger for welfare recipients (+5.4 points vs +3.8).

**Estimated effect of one reminder:**

- Losing the SMS raised no-shows by 4.1 points, while coverage dropped by 82 points.
- So one SMS cuts the chance of a no-show by about **5.1 points** (95% CI roughly 4.0–6.1), from about 33% to about 28%. That is roughly a 15% relative reduction.
- That is about **20 SMS per missed appointment avoided**. Over the 6-week window, the 35,482 SMS sent prevented roughly 1,800 no-shows.

### Recommendation on SMS: keep it and expand it

1. **Keep it.** The effect is real, sizeable and cheap. One SMS costs far less than an empty clinic slot.
2. **Extend it to appointments booked 1–2 days ahead.** These currently get no reminder and are missed about 23% of the time (11,938 appointments, or about 2,700 no-shows in the window). If the effect seen at 3–7 days holds (about +2 points), this would prevent roughly 250–300 no-shows over 6 weeks. That is an estimate and should be tested. Same-day bookings (4.6%) don't need a reminder.
3. **Close the coverage gap.** About 18% of qualifying appointments get no SMS, probably because of a missing or invalid phone number; the data doesn't say why. Collecting mobile numbers at booking would extend the benefit to them.
4. **Monitor sending.** The 7-day outage appears to have cost about 650 extra no-shows (16,584 × ~4 points). A daily check that compares SMS sent against SMS expected would catch this kind of failure.

## 3. What the network should do to reduce no-shows

1. **Expand SMS** as described above. This is the only intervention here with causal evidence behind it.
2. **Focus extra outreach on high-risk appointments.** Score each appointment by lead time, past no-shows, age, welfare status and neighbourhood. For the riskiest ~20%, which hold about 38% of no-shows, add a phone call or a second reminder a day before, with an easy way to cancel or rebook. This effect hasn't been measured yet; pilot it as an A/B test.
3. **Shorten lead times.** No-shows climb steeply from 5% for same-day bookings to over 30% beyond 2 weeks. Options include more same-day or short-notice slots, releasing slots closer to the date, and a confirm-or-release step for appointments booked more than 2 weeks ahead.
4. **Overbook carefully where risk is predictable.** Clinic sessions dominated by long-lead or high-risk appointments could take a modest number of extra bookings, sized from predicted no-shows, to keep capacity used.
5. **Support specific groups.** Teens and young adults have the highest no-show rates (25–26%), as do welfare recipients and a handful of neighbourhoods (Santos Dumont, Itararé, Santa Clara, Jesus de Nazareth). Reminders worked particularly well for welfare recipients. Ask patients in these groups about barriers such as transport and work hours.
6. **Test changes properly.** The outage showed how clear a comparison becomes when there's a proper control group. Roll out the changes above with randomised or staggered starts so that each one can be measured.

## Limitations

- Only about 6 weeks of data are available, so "past no-show" history is short, and there are no seasonal effects.
- There's no information on appointment type, clinic, specialty or contact details, which may explain some of the lead-time and coverage differences.
- The SMS result covers a single reminder for appointments booked 3+ days ahead. The benefit for 1–2-day bookings is an extrapolation and should be tested.
- Apart from SMS, all drivers are associations, not proven causes.
