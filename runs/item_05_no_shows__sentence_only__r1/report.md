# Appointment No-Shows: Drivers, the SMS Reminder Programme, and What to Do

**Data:** `appointments.csv`, 110,527 appointments for 62,298 patients. Appointments fall between 29 Apr and 8 Jun 2016, with bookings going back to Nov 2015. The overall no-show rate is **20.2%**, or 22,314 missed appointments.

## Bottom line

1. **Keep the SMS programme and expand it. Do not cut it.** The raw numbers make SMS look harmful: people who got a text missed **27.6%** of appointments, against **16.7%** for people who didn't. That comparison is misleading. Texts only go out for appointments booked 3 or more days ahead, and those appointments are missed far more often whether or not a text is sent. Once that is accounted for, SMS **reduces** no-shows. The best evidence is a natural experiment: on 7 appointment days no texts were sent at all. On those days, no-shows among text-eligible appointments rose by about **4 percentage points** (from 28.6% to 32.5%). Over the same days, no-shows among appointments that never get texts did not change at all.
2. **The main driver of no-shows is how far ahead the appointment was booked.** Same-day appointments: 4.6% no-shows. Next 1–2 days: 23%. 2–4 weeks ahead: 33%. A patient's past attendance, age, and welfare (Scholarship) status are the next most important factors.
3. **Recommendations:** fix gaps in SMS delivery and extend texts to more appointments. Shorten booking lead times where possible. Give the patients most likely to miss (who can be identified ahead of time) more intensive reminders and overbooking.

---

## 1. What drives no-shows

### Lead time (days from booking to appointment): by far the strongest factor

| Lead time | Appointments | No-show rate | % who got an SMS |
|---|---|---|---|
| Same day | 38,562 | **4.6%** | 0% |
| 1–2 days | 11,938 | 22.7% | 0% |
| 3–7 days | 20,247 | 25.0% | ~55% |
| 8–14 days | 12,025 | 30.5% | 58% |
| 15–30 days | 17,371 | 32.6% | 61% |
| 31–60 days | 8,283 | **34.2%** | 61% |
| 61+ days | 2,095 | 28.4% | 64% |

Appointments booked 3 or more days ahead are 54% of all appointments but **80% of all missed appointments**. Part of the same-day figure is built in: someone booking on the day is often already at the clinic. Even so, the rise from 1 day out to 30+ days out (23% to 34%) is a real and steady gradient.

### Other factors

I fitted a logistic regression that includes all factors together. Odds ratios are shown with 95% confidence intervals. The model's AUC is 0.73.

| Factor | Effect |
|---|---|
| **Has missed an earlier appointment in this data** | no-show rate 29.1% vs 17.0% for patients who attended every earlier appointment; OR 1.78 (1.71–1.86) vs first-time patients |
| **Age 12–25** | highest-risk ages, 25–26% raw; OR 1.35–1.52 vs age 35–45 |
| **Age 55+** | lowest-risk ages, 15–16% raw; OR 0.61–0.69 |
| **Scholarship** (welfare programme) | 23.7% vs 19.8%; OR 1.23 (1.17–1.30) |
| **Alcoholism** | OR 1.37 (1.24–1.50) after adjustment |
| **Diabetes** | OR 1.16 (1.08–1.24) after adjustment (lower raw rate, because diabetic patients tend to be older) |
| Gender, hypertension, disability, weekday | small or no effect (all ORs between 0.9 and 1.1) |
| Neighbourhood | ranges from about 15% to 29% among the 81 neighbourhoods (those with ≥200 appointments); highest are Santos Dumont, Santa Cecília, Santa Clara, Itararé |

**Risk is concentrated and predictable.** If appointments are split into ten equal groups by predicted risk, the riskiest group has a 43% no-show rate and accounts for 21% of all misses. The top three groups account for **53% of all misses**. The bottom three groups miss fewer than 4% of appointments.

## 2. The SMS reminder programme

### Why the raw comparison is wrong
In this data, SMS is **never** sent for appointments booked 0–2 days ahead. Those are the lowest-risk appointments. So the "no SMS" group is mostly same-day bookings, and of course it looks better. If you compare like with like, within each lead-time band from the table above, patients who got a text missed **3–8 points less often** than those who didn't (for example, 15–30 days: 29.8% with SMS vs 36.9% without). That within-band comparison could still be biased, for instance if patients without a phone number differ in other ways. So I relied on a cleaner test.

### Natural experiment: the days with no texts
On most appointment days, about 82% of eligible appointments got a text. On **9, 13 and 16–20 May**, the share was **0%**. This looks like a programme pause or outage; the reason isn't recorded. These 7 days cover 16,584 eligible appointments. Patients on those days look the same as on other days: average age 37.2 vs 37.7, Scholarship share 9.5% vs 9.6%, average lead time 17.6 vs 18.8 days, and the same mix of past-attendance histories.

| | Normal SMS days | No-SMS days | Difference |
|---|---|---|---|
| Eligible appointments (booked ≥3 days ahead) | 28.6% | 32.5% | **+4.0 pts** |
| Never-texted appointments (booked 0–2 days ahead; comparison group) | 8.93% | 8.92% | 0.0 pts |

The comparison group shows nothing else different about those days, such as weather or staffing, that would raise no-shows on its own. A regression that also adjusts for lead time, age, conditions, gender and weekday, with standard errors clustered by appointment day, gives:

- **Effect of the programme running vs not running: −4.0 points** (95% CI −2.3 to −5.8). That is about a 12% relative reduction among eligible appointments.
- A stricter version uses only appointment days from 2–25 May, to rule out any trend over time. It gives −2.7 points (95% CI −0.7 to −4.7).
- Only about 82% of eligible patients actually get a text. Adjusting for that, **each text delivered prevents about 3–5 missed appointments per 100 texts.**

The effect looks somewhat larger for higher-risk groups: patients with an earlier no-show (+6.0 points when texts stopped), Scholarship patients (+5.4) and under-18s (+5.1). It was smaller for appointments booked 3–7 days ahead (+1.9) than for 8+ days ahead (+5 to +6). These subgroup figures are indicative only; I did not test them formally.

### What this means in numbers
- The 7 no-SMS days had roughly **650 extra missed appointments** (16,584 × ~4 points).
- On normal days, **7,955 eligible appointments still got no text.** At 3–5 points, that's another ~250–400 missed appointments per six weeks that could be avoided.
- Appointments booked 1–2 days ahead (11,938 appointments, 22.7% no-shows) never get a text. Their no-show rate is close to the eligible group's, so they are an obvious group to extend texts to. The effect there hasn't been measured yet.

**Recommendation: keep and expand.** An SMS costs very little compared with a wasted clinic slot. The data doesn't include costs, but even at 3 avoided no-shows per 100 texts, the programme almost certainly pays for itself.

## 3. Recommendations

1. **Make SMS delivery reliable.** Find out what happened on 9, 13 and 16–20 May and stop it happening again. Raise coverage among eligible appointments from 82% toward 100%, starting with collecting and checking mobile numbers.
2. **Extend SMS to appointments booked 1–2 days ahead,** and consider a second reminder for appointments booked weeks ahead. Run these changes as a randomised trial (for example, alternate days or a random half of patients) so the benefit is measured directly, not inferred.
3. **Shorten lead times.** Lead time is the strongest driver. Use more same-day or short-notice slots, and for appointments booked weeks out, ask the patient to confirm a few days beforehand and release the slot if they don't.
4. **Target high-risk appointments.** Flag appointments booked ≥8 days ahead for patients aged 12–35, on Scholarship, or with a previous no-show. Give them a phone call or a reminder they must reply to, and overbook those slots carefully. The riskiest 30% of appointments account for over half of all misses.
5. **Look at the highest-no-show neighbourhoods** (Santos Dumont, Santa Cecília, Santa Clara, Itararé, Jesus de Nazareth) for access problems such as transport or opening hours.

## Assumptions and limitations
- **Lead time** = appointment date minus booking date, in calendar days. Appointment times are recorded only as dates. I dropped 5 records where the appointment came before the booking and 1 with a negative age (6 rows, 110,521 used).
- **SMS eligibility (lead time ≥3 days) and the outage days** are worked out from the data. They are not documented rules. The outage analysis covers only 7 days in one six-week window and isn't a randomised trial. The strict version gives a smaller effect (2.7 points) than the full version (4.0 points), so the size of the effect is uncertain, but both show a reduction.
- **"Previous no-show"** only counts appointments inside this six-week window, so a patient's real history isn't captured. With more history, this factor would probably predict even better.
- The **same-day low rate** partly reflects patients booking while already at the clinic. It doesn't mean every appointment could be same-day with a 5% no-show rate.
- There is no cost data, no information on whether a text was actually read, and no reason recorded for missed appointments. 618 rows match another row on everything except appointment ID. I treated these as genuine separate bookings.
