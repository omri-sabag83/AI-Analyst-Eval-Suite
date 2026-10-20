# Appointment no-shows: what drives them, and what to do about SMS reminders

## Summary

- **Recommendation on SMS: keep the programme and expand it. Do not cut it.** Taken at face value the data says the opposite: patients who got an SMS missed their appointment **more** often (27.6% vs 16.7%). That gap is not caused by the SMS. SMS reminders only go to appointments booked **3 or more days ahead**, and those appointments have a much higher no-show rate whatever happens. When SMS and non-SMS appointments with the same lead time are compared, **SMS is linked to fewer no-shows in every lead-time band**: about **5 percentage points** lower after adjustment (from roughly 32% to 27%). A stricter comparison of the same patient with and without an SMS gives about **2.5 points** lower.
- **The biggest driver of no-shows is lead time**, meaning the days between booking and the appointment. Same-day appointments have a 4.6% no-show rate. Appointments booked 1–2 days ahead reach about 23%, and those booked 15 or more days ahead reach about 33%. Bookings made 3+ days ahead account for **80% of all no-shows**.
- **Other drivers:** having missed an earlier appointment (29% no-show vs 17% for patients who attended their earlier ones), age (teenagers and young adults about 25–27%, over-55s about 15–16%), receiving the Bolsa Família welfare benefit (the `Scholarship` field), alcoholism, and neighbourhood (16% to 29%). Gender, weekday, hypertension and disability make little or no difference.
- **What to do:** (1) send SMS to every appointment booked 3+ days ahead; today about 41% of them (24,500 in this sample) get none. (2) Keep booking lead times short, and add a second contact for long-lead bookings. (3) Focus extra outreach on patients who have missed before and on high-risk groups. (4) Run the SMS expansion as a randomised rollout so the effect is measured properly.

## Data and assumptions

- 110,527 appointments for 62,299 patients. Appointment dates run from 29 Apr to 8 Jun 2016, and booking dates go back to Nov 2015. There are no missing values. The overall no-show rate is **20.2%**.
- I removed 5 rows where the appointment came *before* the booking date (all were recorded as no-shows, so they are probably data errors) and 1 row with age −1. That leaves 110,521 rows.
- Lead time = appointment date − booking date, in calendar days. `AppointmentDay` has no time of day.
- "Prior no-show" uses only the patient's *earlier* appointments within this six-week window. It is a partial history: 56% of appointments are the patient's first one in the data.
- I assume `Scholarship` refers to enrolment in the Bolsa Família welfare programme, and that `Handcap` (0–4) counts disabilities.
- The data has no cost information and no reason why an eligible appointment did or did not get an SMS (for example, no phone number on file). This limits how far the SMS estimate can be read as causal; see Caveats.

## Finding 1: The raw SMS comparison is misleading because of who gets an SMS

| Lead time (days) | Appointments | No-show rate | Share with SMS |
|---|---|---|---|
| 0 (same day) | 38,563 | 4.6% | **0%** |
| 1 | 5,213 | 21.4% | **0%** |
| 2 | 6,725 | 23.8% | **0%** |
| 3 | 2,737 | 23.5% | 33% |
| 4–7 | 17,510 | 25.2% | 61% |
| 8–14 | 12,025 | 30.5% | 58% |
| 15–30 | 17,371 | 32.6% | 61% |
| 31–60 | 8,283 | 34.2% | 61% |
| 61+ | 2,095 | 28.4% | 64% |

No appointment booked fewer than 3 days ahead ever got an SMS. That group includes the 38,563 same-day appointments, which almost always go ahead. So the "no SMS" group is full of low-risk same-day visits, and the "SMS" group is made up entirely of higher-risk long-lead bookings. Comparing the two groups directly mostly measures lead time, not the SMS.

## Finding 2: Among comparable appointments, SMS is linked to fewer no-shows

Comparison restricted to the 60,021 appointments that *could* get an SMS (lead time 3+ days):

| Lead time (days) | No-show, no SMS | No-show, with SMS | Difference |
|---|---|---|---|
| 3 | 24.6% | 21.3% | −3.3 pts |
| 4–7 | 27.1% | 24.0% | −3.1 pts |
| 8–14 | 33.8% | 28.1% | −5.6 pts |
| 15–30 | 36.9% | 29.8% | −7.1 pts |
| 31–60 | 38.4% | 31.5% | −6.9 pts |
| 61+ | 33.9% | 25.5% | −8.4 pts |

The SMS group does better in every band, and the difference grows with lead time. That makes sense, since a reminder is more useful when the booking was made long ago. I checked this three ways:

| Method (eligible appointments) | Estimated effect of SMS on no-show rate |
|---|---|
| Raw difference | −5.1 pts |
| Logistic regression adjusting for lead-time band, age, sex, welfare benefit, health conditions, disability, prior no-show history, appointment date and neighbourhood | odds ratio 0.78 (95% CI 0.74–0.83); about **−4.9 pts** |
| Linear model with the same controls plus booking week | −5.0 pts (95% CI −6.1 to −3.8) |
| Within-patient comparison (6,219 patients who had eligible appointments both with and without SMS; adjusted for lead time) | **−2.5 pts** (95% CI −3.7 to −1.3) |

Standard errors are clustered by patient. All four estimates point the same way and none of the confidence intervals include zero. I treat **about 2.5–5 points** as the plausible range. The within-patient figure is the most conservative because it removes fixed differences between patients. The effect looks largest for patients who have missed before (−12 pts raw, 47% → 35%) and smallest for patients who have always attended (−0.7 pts).

**What this means in practice:** about 20–40 SMS messages prevent one no-show. In this six-week sample, 24,539 eligible appointments got no SMS, and their no-show rate was 32.7%. Reaching them could prevent roughly **600–1,200 no-shows** over a comparable period. This is an estimate, not a measured result.

## Finding 3: What drives no-shows

These results come from a logistic regression on all appointments (AUC 0.73). Each odds ratio is adjusted for all the other factors.

| Factor | Raw no-show rate | Adjusted odds ratio |
|---|---|---|
| **Lead time**: same day | 4.6% | reference |
| 1–2 days | 23% | about 6–7.6× |
| 8–14 days | 30% | 10.7× |
| 15–60 days | 33–34% | 12–13× |
| **Prior no-show in window** (vs first appointment in data) | 29.1% vs 19.5% | 1.78× |
| Earlier appointments all attended | 17.0% | 0.87× |
| **Age** 12–17 / 18–25 (vs 0–5) | 26.6% / 25.1% vs 18.6% | 1.49× / 1.31× |
| Age 55–65 / 65–75 | 15.8% / 15.1% | 0.64× / 0.58× |
| **Welfare benefit (Scholarship)** | 23.7% vs 19.8% | 1.23× |
| **Alcoholism** | 20.1% vs 20.2% | 1.37× (the raw rate is flat because alcoholism is mostly found among older patients) |
| Diabetes | 18.0% vs 20.4% | 1.16× |
| Male | 20.0% vs 20.3% | 1.06× (negligible) |
| Hypertension, disability, weekday | — | no meaningful effect |
| **Neighbourhood** (areas with more than 500 appointments) | 16% (e.g. Santa Martha, Jardim da Penha) to 29% (Santos Dumont, Itararé, Jesus de Nazareth) | not modelled individually |

The two levers the network can actually change are **lead time** and **reminders**. Patient characteristics are useful for targeting outreach, not as things to change.

## Recommendations

1. **Keep the SMS programme and expand it to every appointment booked 3+ days ahead.** About 41% of eligible appointments currently get no SMS. Find out why (missing or invalid phone numbers, how sending is set up). Sending patterns vary a lot from week to week: 30% to 87% of eligible appointments got an SMS depending on booking week. That suggests the gaps come from how the programme is run rather than from a deliberate choice. SMS is cheap compared with a wasted clinical slot.
2. **Run the expansion as a randomised rollout**, for example by randomising by clinic or by week, so the network gets a clean causal estimate. The current estimate is observational.
3. **Try SMS for 1–2 day bookings as well**, and send a **second reminder** for bookings made 15+ days ahead. These groups have 23–34% no-show rates and no reminders today. That benefit is reasonable to expect but has not been tested.
4. **Cut lead time where possible.** Use more same-day or short-notice slots and waiting-list backfill. No-show rates rise steeply with booking lead time.
5. **Target outreach**, such as phone calls or rebooking prompts, at patients with an earlier no-show. They have the highest risk and also the largest apparent SMS benefit. Add teenagers and young adults, welfare-benefit recipients and the highest-rate neighbourhoods. Overbooking long-lead slots slightly, guided by predicted risk, is another option.

## Caveats

- **The SMS effect is observational.** I adjusted for everything recorded in the data, but whatever decides who gets an SMS among eligible appointments is unknown. For example, patients with a working phone number may be more engaged anyway. That would make the effect look bigger than it is. The within-patient estimate (−2.5 pts) is less exposed to this problem. In the other direction, the effect for patients who are currently missed (for example, those with no phone number) could be smaller.
- The data covers six weeks of appointments in 2016, and prior-attendance history is truncated to that window.
- Same-day appointments may be walk-ins, which explains their very low no-show rate. "Moving everyone to same day" is not literally possible.
- There is no cost data, so the cost-effectiveness argument is qualitative: about 20–40 SMS per prevented no-show.
