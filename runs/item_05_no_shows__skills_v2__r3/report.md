# Appointment no-shows: drivers and the SMS reminder decision

## Bottom line
1. **Keep the SMS programme and expand it. Do not cut it.** If you just compare SMS against no SMS, it looks like SMS *raises* no-shows (27.6% vs 16.7%). That comparison is misleading. SMS is only ever sent for appointments booked 3 or more days ahead, and those appointments have far higher no-show rates whatever happens. If we compare like with like (same lead time, similar patient), appointments with an SMS have **about 2.5 to 5 percentage points fewer no-shows**. That is roughly 8–16% fewer in relative terms.
2. **How far ahead the appointment was booked (lead time) is by far the biggest driver.** Same-day appointments: 4.6% no-show. Booked 1–7 days ahead: about 24%. Booked 15–60 days ahead: about 33%. Appointments booked 3+ days ahead are 54% of bookings but **80% of all no-shows**.
3. **Other drivers, in order of strength:** a previous no-show by the same patient (26.9% vs 18.8% for patients who attended before), age (teens and young adults about 25%, people over 60 about 15%), being on the welfare programme (`Scholarship`, 23.7% vs 19.8%), and neighbourhood (from 15% to 29% among neighbourhoods with 200+ appointments). Gender, weekday and disability make little or no difference.

## Data and assumptions
- `appointments.csv`: 110,527 appointments for 62,298 patients. No missing values and no duplicate IDs. Appointment dates run from 29 Apr to 8 Jun 2016 (about 6 weeks); bookings go back to Nov 2015. Overall no-show rate: **20.2%**.
- **Excluded 6 rows:** 5 where the appointment date is before the booking date, and 1 with age −1. Analysis covers 110,521 rows.
- Lead time = appointment date minus booking date, in calendar days. `AppointmentDay` has no time of day, so this cannot be more precise than whole days.
- "Prior no-show" only counts the patient's appointments on **earlier** dates inside this 6-week window. That avoids leaking information from the same day, but it undercounts real history.
- **Assumption:** the data doesn't say how patients were picked for SMS. It shows that **no appointment booked less than 3 days ahead received one**, and that 59% of those booked 3+ days ahead did. I treat 3+ days as the programme's eligibility rule. Within that group, I don't know why 41% got no SMS.

## Finding 1: The raw SMS comparison is biased by lead time

| Lead time (days) | No-show, no SMS | No-show, SMS | Appointments (no SMS / SMS) |
|---|---|---|---|
| 0 (same day) | 4.6% | — never sent | 38,562 / 0 |
| 1–2 | 22.7% | — never sent | 11,938 / 0 |
| 3 | 24.6% | 21.3% | 1,831 / 906 |
| 4–7 | 27.1% | 24.0% | 6,868 / 10,642 |
| 8–14 | 33.8% | 28.1% | 5,021 / 7,004 |
| 15–30 | 36.9% | 29.8% | 6,851 / 10,520 |
| 31–60 | 38.4% | 31.5% | 3,224 / 5,059 |
| 61+ | 33.9% | 25.5% | 744 / 1,351 |

The "no SMS" group is mostly same-day bookings, which are almost always attended. That is why SMS looks bad overall. **In every lead-time band where SMS is actually used, SMS appointments have fewer no-shows**, by 3 to 8 points. The gap gets bigger as lead time grows.

Checks on this, all restricted to appointments booked 3+ days ahead:
- **Patient mix is the same.** SMS and non-SMS appointments have nearly identical average age (37.5 vs 37.7), welfare share (9.9% vs 9.2%), hypertension and diabetes rates, and lead time (19.0 vs 17.6 days).
- **Regression adjustment.** I controlled for lead-time band, lead time, age group, sex, welfare status, health conditions, disability, weekday, prior no-show and neighbourhood, with standard errors clustered by patient. SMS goes with **−5.1 points** (95% CI −5.9 to −4.3). In the logistic version the odds ratio is 0.77 (CI 0.74–0.80).
- **Same patient compared with themselves.** 6,219 patients had some eligible appointments with an SMS and some without (18,791 appointments). Comparing each patient only with themselves, SMS goes with **−2.5 points** (95% CI −3.7 to −1.3). This removes any fixed patient differences, so I treat it as the cautious lower end.
- **Same direction in every patient-history group.** First visit: 32.2% → 27.0%. Attended before: 30.8% → 25.8%. Missed before: 38.9% → 33.8%.

**Caveat (association, not proven cause):** the data is observational. If the 41% of eligible appointments without an SMS differ in ways the data doesn't record (for example, no valid mobile number), part of the gap could come from that. The within-patient estimate reduces this concern but doesn't remove it. That's why I give a range (2.5–5 points) rather than one number.

## Finding 2: What drives no-shows

| Factor | Pattern | Strength |
|---|---|---|
| Lead time | 4.6% same day → ~23% at 1–3 days → ~33–34% at 15–60 days | **Very strong**, the dominant factor |
| Prior no-show (within window) | 26.9% vs 18.8% (attended before) / 19.4% (first seen) | Strong; logistic coefficient +0.33, p<0.001 |
| Age | 0–5: 18.6%, 13–18: 26.1%, 19–30: 24.7%, 46–60: 17.8%, 61–75: 14.9% | Strong; holds after adjustment |
| Welfare enrolment (`Scholarship`) | 23.7% vs 19.8% | Moderate; holds after adjustment |
| Neighbourhood | 14.6% (Mário Cypreste) to 28.9% (Santos Dumont), counting only neighbourhoods with 200+ appointments | Moderate; points to local access barriers |
| Booking time of day | Booked before 9am: 17.4%; after 3pm: 23.8% | Modest; likely tied to same-day walk-in bookings |
| Alcoholism, diabetes | Lower rates in raw numbers, but **higher** risk after adjusting for age | Small; confounded by age |
| Sex, weekday, disability, hypertension | Within about 1–2 points, or not significant after adjustment | Weak or none |

The lower raw no-show rate for chronic conditions like hypertension is mostly an age effect. These patients are older, and older patients attend more.

## Recommendations
1. **SMS: keep it and expand it.** Of the appointments booked 3+ days ahead, 24,539 (41%) got no SMS, and their no-show rate was 32.7%. Reaching them is estimated to avoid **about 600–1,250 no-shows per 6-week period** (2.5–5 points × 24,539). That is 3–6% of all no-shows. This is a rough estimate, not a measurement. First find out why these appointments were missed (no phone number on file? an opt-out? which clinic?). Then fix the contact data.
2. **Test SMS for bookings made 1–2 days ahead.** They have never received one, yet their no-show rate is 22.7% across 11,938 appointments. Run this as a **randomised pilot**, e.g. randomly holding back SMS for 10% of appointments. That would measure the real effect of SMS, which this data can't fully do, and settle the cause-versus-association question.
3. **Shorten lead times wherever you can.** Same-day and next-few-day slots almost always get used. Options: hold back capacity for short-notice booking, avoid booking routine visits weeks ahead, and use a "book closer to the date" or recall-list approach for long-range follow-ups.
4. **Extra contact for high-risk patients.** Flag appointments with long lead time plus any of: a previous no-show, age 13–30, welfare enrolment, or a high no-show neighbourhood. Give these a second reminder, a phone call, or an easy confirm/reschedule reply option. Overbook carefully in clinics where these patients are concentrated.
5. **Investigate the high no-show neighbourhoods** (Santos Dumont, Santa Cecília, Santa Clara, Itararé, Jesus de Nazareth). Look for transport and access problems; these need local fixes rather than more messages.
6. **Improve the data:** record when each SMS was sent, its delivery status, and why it wasn't sent. Keep a longer attendance history. Without these, the true value of SMS can only be estimated, not measured.

## Limitations
- The data covers only about 6 weeks of appointments from a single network, so it can't show seasonality or long-term trends.
- The SMS effect is estimated from observational data; how patients were chosen to get an SMS is unknown.
- Lead time is only accurate to the day, and patient history is cut off at the start of the window.
- There is no data on cost per SMS or cost per no-show, so the return on investment is not computed. At 600–1,250 avoided no-shows per 24,500 extra messages, the programme pays off if one no-show costs more than about 20–40 SMS messages.
