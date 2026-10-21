# Appointment no-shows: drivers and the SMS reminder programme

## Bottom line

1. **Keep the SMS reminder programme and expand it.** The raw data seems to say SMS makes things worse: patients who got an SMS missed 27.6% of appointments, against 16.7% for those who didn't. That comparison is misleading. SMS is only sent for appointments booked 3 or more days ahead, and those appointments are missed far more often whatever happens. A natural experiment in the data shows that **an SMS reminder cuts the no-show rate by about 4–5 percentage points**, from roughly 32–33% to about 28%, which is a relative drop of about 15%.
2. **The main driver of no-shows is how far ahead the appointment is booked.** Same-day appointments are missed 4.6% of the time. Appointments booked a week or more ahead are missed 30–33% of the time. **The second strongest predictor is having missed an appointment before** (29% vs 17%). Age (teenagers and young adults are highest), being on the welfare programme ("Scholarship") and alcoholism add smaller effects.
3. **Recommended actions:** fix gaps in SMS delivery and coverage; trial reminders for appointments booked 1–2 days ahead; shorten booking lead times where possible; and give extra outreach to high-risk bookings (long lead time plus a previous no-show).

## Data and assumptions

- 110,527 appointments for 62,299 patients. Appointment dates run from 29 Apr to 8 Jun 2016 (27 clinic days); bookings were made from Nov 2015 onwards. Overall no-show rate: **20.2%**.
- **Lead time** = appointment date minus booking date, in calendar days. Five rows where the appointment came before the booking, and one row with age −1, were dropped as data errors.
- **Prior no-show history** only counts appointments inside this 6-week window. A patient's "first" appointment here is not necessarily their first ever.
- No cost data was provided (cost per SMS, cost of a missed slot), so impact is given in avoided no-shows, not money.
- Apart from the natural experiment described below, all results are observational associations, not proven causes.

## 1. What drives no-shows

| Factor | Group | No-show rate | Appointments | Adjusted odds ratio* |
|---|---|---|---|---|
| **Lead time** | Same day | 4.6% | 38,562 | (reference) |
| | 1–2 days | 22.7% | 11,938 | 6.8 |
| | 3–7 days | 25.0% | 20,247 | 8.2 |
| | 8–14 days | 30.5% | 12,025 | 10.6 |
| | 15–30 days | 32.6% | 17,371 | 12.4 |
| | 31+ days | 33.0% | 10,378 | 12.5–13.7 |
| **History* *** | Missed an earlier appointment in window | 29.1% | 15,976 | 1.93 |
| | Earlier appointments all attended | 17.0% | 32,250 | 0.93 |
| | First appointment in window | 19.5% | 62,295 | (reference) |
| **Age** | 13–18 / 19–25 | 26.1% / 25.4% | | 1.39 (13–18) |
| | 56–65 / 66+ | 15–16% | | 0.61 (55+) |
| Scholarship (welfare) | Yes vs No | 23.7% vs 19.8% | 10,861 | 1.24 |
| Alcoholism | Yes vs No | 20.1% vs 20.2% | 3,360 | 1.35 |
| Gender, hypertension, disability, weekday | | differences ≤ 1–2 pts | | ~1.0 (not meaningful) |

\*Logistic regression on all appointments. It adjusts for lead time, age, sex, scholarship, the health conditions, prior history, SMS and appointment date. Standard errors are clustered by patient. All odds ratios shown have p < 0.01.
\*\*The "History" row means a previous no-show within this 6-week window.

Key observations:
- **Lead time is the dominant factor.** Same-day bookings are 35% of appointments but only 8% of no-shows. Appointments booked 3 or more days ahead are 54% of appointments but 80% of no-shows.
- **No-shows cluster in certain patients.** Patients who have already missed once miss again 29% of the time.
- Neighbourhood rates range from about 16% to 29% (for areas with more than 500 appointments). Without travel or socio-economic data we can't tell why, so this is not used as a lever here.

## 2. The SMS reminder programme

### Why the raw comparison misleads
SMS was **never** sent for appointments booked fewer than 3 days ahead. That group includes all same-day appointments, which have a 4.6% no-show rate. The "no SMS" group is therefore mostly short-lead, low-risk appointments. **When you compare like with like (same lead-time band), SMS recipients always miss less:**

| Lead time | No SMS | SMS | Difference |
|---|---|---|---|
| 3 days | 24.6% | 21.3% | −3.3 pts |
| 4–7 days | 27.1% | 24.0% | −3.1 pts |
| 8–14 days | 33.8% | 28.1% | −5.6 pts |
| 15–30 days | 36.9% | 29.8% | −7.1 pts |
| 31–60 days | 38.4% | 31.5% | −6.9 pts |
| 61+ days | 33.9% | 25.5% | −8.4 pts |

### Stronger evidence: SMS stopped on 7 days
On 7 appointment days (9, 13 and 16–20 May), **no SMS was sent to anyone**. On every other day, 76–84% of eligible appointments (booked 3 or more days ahead) got one. This looks like a system outage or suspension, which gives a natural experiment:

| | Normal days | SMS-off days |
|---|---|---|
| Eligible appointments (≥3 days lead) — SMS coverage | 81.7% | 0% |
| Eligible appointments — no-show rate | **28.6%** | **32.5%** |
| Ineligible appointments (<3 days lead, never get SMS) — no-show rate | 8.9% | 8.9% |

- No-shows went up only for the appointments that would normally have received an SMS. Appointments that never get an SMS stayed at exactly 8.9%. That makes it unlikely the rise was caused by something general about those days.
- **Difference-in-differences estimate** (compares the change for eligible appointments with the change for ineligible ones, controlling for lead time): turning SMS off raised no-shows by **+4.0 pts (95% CI 3.1–5.0)**. Coverage on normal days is 82%, so the effect per SMS actually sent is about **5 pts**.
- The result holds when the 16–20 May week is excluded: using only 9 and 13 May as SMS-off days gives +3.7 pts.
- A separate check, an adjusted regression on eligible appointments, gives a similar answer: SMS is linked to **−5.2 pts (95% CI −6.3 to −4.2)**.

**Estimated impact:** about 35,500 SMS were sent in these 6 weeks. At about 5 pts each, that is roughly **1,800 missed appointments avoided**, about 1 for every 20 messages. An SMS costs very little compared with an unused clinical slot, so the programme very likely pays for itself. Confirming this needs the network's own cost figures.

### Gaps in the current programme
- **Patchy coverage.** On normal days, 7,947 eligible appointments (18%) got no SMS. Those not sent an SMS also include more patients with previous no-shows (19% vs 13%), so the programme is missing some of the highest-risk bookings.
- **Unreliable delivery.** On 7 of 26 clinic days no SMS was sent at all. By the estimate above, that cost roughly 16,600 × 4 pts ≈ **650 extra no-shows**.
- **Short lead times not covered.** Appointments booked 1–2 days ahead (11,938, with a 22.7% no-show rate) never get a reminder. We have no data on whether SMS works for them.

## 3. Recommendations

1. **SMS programme: keep it and expand it. Do not cut it.**
   - Make delivery reliable. Monitor the share of eligible appointments sent an SMS each day and alert on drops, so that SMS-off days like those in May don't happen again.
   - Close the coverage gap (aim for close to 100% of eligible bookings). Find out why 18% were missed; one likely cause is missing or invalid phone numbers, so collect and check them at booking.
   - **Pilot SMS for appointments booked 1–2 days ahead, and a second reminder for long-lead bookings, as randomised trials.** Keep a small random group without the reminder so the true effect is measured directly instead of inferred.
2. **Reduce lead times.** This is the biggest lever. Wherever clinically suitable, offer same-day or next-day slots (open-access scheduling) instead of booking weeks out. For bookings that must be far ahead, add a confirm-or-cancel step a few days before so the slot can be given to someone else.
3. **Target high-risk bookings.** Combine lead time and prior no-show history (adding age and scholarship status) into a simple risk score. Use it to choose who gets stronger outreach, such as a phone call or help with transport. Patients with a previous no-show and a booking 2 or more weeks ahead miss well over 30% of the time.
4. **Use predicted risk for slot management.** Moderate overbooking on clinic sessions with a high expected no-show rate (long-lead, high-risk bookings) can recover lost capacity. This should be monitored for crowding.

## Caveats
- The data covers only 6 weeks in 2016. Results should be re-checked on current data.
- The SMS-off days were not randomly chosen. Most fall in one week of May, so something else specific to that week could explain part of the effect. The unchanged control group and the 9/13-May-only check reduce this concern, but a randomised holdout is the right way to confirm the effect size.
- The other drivers (age, scholarship and so on) are associations. They are useful for targeting, but they are not proven causes.
