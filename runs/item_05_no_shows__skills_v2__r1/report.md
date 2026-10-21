# Appointment no-shows: what drives them, and what to do about SMS reminders

## Summary

1. **Keep the SMS reminder programme and expand it. Do not cut it.** In the raw data, patients who got an SMS look *worse*: 27.6% of them missed their appointment, against 16.7% of those who didn't get one. That gap is misleading. SMS is only sent for appointments booked 3 or more days ahead, and those appointments have far more no-shows to begin with. Once you compare like with like, SMS **lowers** no-shows by about **3–5 percentage points**. That is roughly 10–15% of the no-shows it targets.
2. **The strongest evidence comes from a natural experiment.** On 7 appointment days in May 2016, no SMS was sent at all. On those days, no-shows among appointments that would normally get an SMS rose by about 4 points. No-shows among appointments that never get an SMS did not move.
3. **How far ahead the appointment was booked (lead time) matters most.** Same-day appointments have a 4.6% no-show rate. Appointments booked 1 day or more ahead run at 21–34%. Appointments booked 3+ days ahead produce **80% of all no-shows**.
4. **Other drivers, in order of size:** having missed an appointment before (odds about 1.8× those of a first-time patient), being a teenager or young adult, receiving welfare support (`Scholarship`), alcoholism, and neighbourhood. Gender, weekday and most health conditions matter little.

## Data and assumptions

- The file has 110,527 appointments for 62,299 patients. Appointment dates run from 29 Apr to 8 Jun 2016 (27 days, about 6 weeks). Overall no-show rate: **20.2%**.
- **Lead time** is the appointment date minus the booking date, counted in days. I excluded 5 rows where the appointment comes before the booking (all recorded as no-shows, so probably data errors) and 1 row with age −1. Nothing else needed cleaning, and there are no duplicate appointment IDs.
- **"Prior no-show"** only counts appointments inside this 6-week file. Patients' earlier history isn't available, so this factor is understated.
- I had no cost data for SMS or for a missed slot, so I can't give a return-on-investment figure. Impact is given as the number of avoided no-shows.

## 1. The SMS programme

### Why the raw comparison misleads

SMS is never sent for appointments booked fewer than 3 days ahead. Those are mostly same-day bookings, which have very few no-shows. So the "no SMS" group is full of low-risk appointments. Once you compare within the same lead time, SMS is linked to fewer no-shows in every band:

| Lead time | No-show, no SMS | No-show, SMS | Appointments (no SMS / SMS) |
|---|---|---|---|
| 0 days (same day) | 4.6% | – (never sent) | 38,563 / 0 |
| 1 day | 21.4% | – (never sent) | 5,213 / 0 |
| 2–3 days | 24.0% | 21.3% | 8,556 / 906 |
| 4–7 days | 27.1% | 24.0% | 6,868 / 10,642 |
| 8–14 days | 33.8% | 28.1% | 5,021 / 7,004 |
| 15–30 days | 36.9% | 29.8% | 6,851 / 10,520 |
| 31–60 days | 38.4% | 31.5% | 3,224 / 5,059 |
| 61+ days | 33.9% | 25.5% | 744 / 1,351 |

I then ran regressions on appointments booked 3+ days ahead. They controlled for lead time, age, gender, welfare status, health conditions, prior attendance, weekday and neighbourhood. Both versions estimate that SMS lowers the no-show rate by **5.0 points** (95% CI 4.3–5.8; odds ratio 0.78). I also compared the same patient with and without an SMS, which removes stable differences between patients. That gives a smaller but still clear **2.7-point** reduction (±1.2).

### The natural experiment: days with no SMS

Normally about 82% of appointments booked 3+ days ahead get an SMS. On 9, 13 and 16–20 May 2016 the rate was **0%**, apparently a system outage or a pause in the programme. On every other weekday it was 76–84%. Being due on an outage day says nothing about the patient, so this works like a test with a control group:

| | Normal days | Outage days | Change |
|---|---|---|---|
| Booked 3+ days ahead (normally get SMS) | 28.6% | 32.5% | **+3.9 pts** |
| Booked 0–2 days ahead (never get SMS), the check group | 8.9% | 8.9% | 0.0 pts |

- The check group did not change. So the rise is not explained by something else that happened on those days.
- The estimate holds when I adjust for each date and for lead time (+4.1 points, CI 3.0–5.1). It also holds when the check group is limited to the most similar appointments, those booked 1–2 days ahead (+4.3, CI 2.2–6.4).
- If I only use 2–25 May, closest to the outages, the estimate is smaller: +2.8 points (CI 1.6–3.9). No-shows were falling in early June, which inflates the comparison over the full period a little. **A cautious estimate is about 3–5 fewer no-shows per 100 SMS sent**, against a baseline of about 32%.

**What this is worth:** across the roughly 35,500 SMS sent in this period, about **1,000–1,700 no-shows were avoided** in 6 weeks.

**What we don't know:** whether SMS works for appointments booked 1–2 days ahead (it was never sent for them), and how much each SMS costs. The outages also show the programme has no monitoring: it was down for 7 of 27 days, apparently without anyone noticing.

## 2. What drives no-shows

These results come from a multivariable logistic regression on all appointments (AUC 0.74). Figures are odds ratios after adjusting for every other factor.

| Factor | Effect | Notes |
|---|---|---|
| **Lead time** | Same day 4.6% no-show; 1–2 days 21–24%; 3–7 days 25%; 8–30 days 29–33%; 31–60 days 33–34% | By far the largest driver. Odds are 6–14× higher than for same-day appointments. Same-day bookings are probably partly walk-ins, so read this as an association, not proof that shorter waits would cut no-shows this much. |
| **Prior no-show (within the window)** | OR 1.76 against first visit. A patient who attended before: OR 0.88 | 29% no-show if they had missed before, 17% if they had attended. 5% of patients account for 35% of all no-shows. |
| **Age** | Ages 12–18: OR 1.58; 18–25: 1.42; 50–80: 0.68–0.76 (all against ages 35–50) | Rates: 26% for teens, 15–17% for over-50s. |
| **Welfare (`Scholarship`)** | OR 1.20 | 23.7% against 19.8%. |
| **Alcoholism** | OR 1.35 | Small group (3% of appointments). |
| **Neighbourhood** | Rates range from 16% to 29% (areas with 500+ appointments) | Examples: Santos Dumont 29%, Itararé 26%. |
| Gender, weekday, hypertension, disability | Effects of 5% or less, or not significant | Not worth targeting. |
| SMS received | OR 0.78 | Protective once lead time is controlled for (see Section 1). |

These are associations, except for the SMS result, which is backed by the natural experiment. They tell us **whom to target**. They don't tell us that changing a factor such as age group would change behaviour.

## 3. Recommendations

1. **Keep and expand SMS reminders.** This is the one intervention with near-causal evidence that it works.
   - **Fix reliability first.** Add a daily check that sends an alert if the SMS rate for eligible appointments falls far below about 80%. The May outage alone cost an estimated 500–700 extra no-shows (16,600 appointments × 3–4 points).
   - **Cover the eligible appointments that are missed.** On normal days, about 18% of appointments booked 3+ days ahead (about 8,000) still got no SMS. Find out why, for example missing phone numbers, and close the gap.
   - **Pilot SMS for appointments booked 1–2 days ahead** (about 12,000 appointments, 22–24% no-show rate). Run it as a randomised test, because there's no data on this group yet.
2. **Shorten the gap between booking and appointment where possible.** Lead time is the strongest predictor. Offer earlier or same-day slots, and send long-lead bookings (15+ days, about 33% no-show) a second reminder or ask them to confirm, so unconfirmed slots can be given to someone else.
3. **Target high-risk patients with extra contact, such as a phone call.** Focus on patients who have missed before (the 5% of patients behind 35% of no-shows), teens and young adults, welfare recipients and the highest-risk neighbourhoods. The risk model (AUC 0.74) can rank upcoming appointments by risk, so calls go where they're most likely to help.
4. **Use the risk scores to overbook carefully** in sessions with many high-risk, long-lead appointments, to recover lost clinic capacity.
5. **Measure as you go.** Roll out changes in a randomised way, for example by day or by clinic, so their effect can be measured, just as the accidental outage made it possible to measure SMS. Also collect SMS costs, so the next review can compare cost per avoided no-show.

**Limitations:** the data covers only 6 weeks, so seasonal effects and long-term patient history are missing. There is no cost data. The outage days were not chosen at random, although the unchanged check group makes it unlikely that something else on those days explains the result. Neighbourhood is the only location information, and there is no field for clinic or specialty.
