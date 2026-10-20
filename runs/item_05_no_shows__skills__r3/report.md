# Appointment no-shows: what drives them, and what to do about SMS reminders

**Data:** 110,527 appointments (62,299 patients, 81 neighbourhoods). Appointments ran from 29 Apr to 8 Jun 2016 and were booked between Nov 2015 and Jun 2016. The overall no-show rate is **20.2%**.

## Bottom line

1. **Keep the SMS programme and expand it.** On the raw numbers, patients who got an SMS missed *more* appointments (27.6% vs 16.7%). That comparison is misleading. SMS is only ever sent for appointments booked **3 or more days ahead**, and those appointments carry much higher risk anyway. Once you compare like with like, an SMS **reduces** no-shows by roughly **4–5 percentage points** (about 15–20% fewer no-shows) among the appointments that receive one.
2. **The biggest driver is how far ahead the appointment was booked (lead time).** Same-day appointments have a 4.6% no-show rate. For appointments booked 15 days or more ahead it is 28–34%. Patient characteristics matter much less.
3. **Recommended actions:** (a) extend reminders to the gaps they currently miss, (b) shorten lead times or add a confirm/release step for long-lead bookings, and (c) give extra contact to patients who have missed appointments before.

## 1. What drives no-shows

### Lead time (by far the strongest factor)
| Days between booking and appointment | Appointments | No-show rate | Share of all no-shows |
|---|---|---|---|
| 0 (same day) | 38,562 | 4.6% | 8% |
| 1 | 5,213 | 21.4% | 5% |
| 2 | 6,725 | 23.8% | 7% |
| 3–4 | 8,027 | 23.4% | 8% |
| 5–7 | 12,220 | 26.0% | 14% |
| 8–14 | 12,025 | 30.5% | 16% |
| 15–30 | 17,371 | 32.6% | 25% |
| 31+ | 10,378 | 33.0% | 15% |

Same-day bookings make up 35% of appointments but only 8% of no-shows. Appointments booked 8 or more days ahead make up 36% of appointments and **57% of no-shows**. In a multivariable logistic model, booking 15–30 days ahead has an odds ratio of about 12 compared with same-day, after adjusting for every other factor below.

### Other factors (multivariable logistic model; odds ratios, all adjusted for lead time, SMS, weekday and each other)
- **Prior no-show history:** a patient who has already missed an earlier appointment in this data has OR **1.78** (29.1% raw no-show rate, against 17.1% for patients who attended all earlier appointments). This is the most useful patient-level flag.
- **Age:** patients aged 12–25 are the highest-risk group (OR 1.36–1.52 vs age 35–45; raw rates 25–26%). Patients over 55 are the lowest (OR 0.61–0.69; raw rate ~15–16%).
- **Welfare enrolment ("Scholarship"):** OR 1.22. **Alcoholism:** OR 1.37. **Diabetes:** OR 1.16.
- **Small or no effect:** gender (OR 1.06), hypertension (none after adjustment), disability (n.s.), weekday (Wed/Thu are slightly lower).
- **Neighbourhood:** among neighbourhoods with 200+ appointments, rates range from about 15% to 29% (e.g. Santos Dumont 29%, Santa Cecília 27%, Itararé 26%). I did not model this beyond the description, and some of the spread probably reflects differences in mix (lead time, age).

## 2. SMS reminders: do they work?

### Why the raw comparison is wrong
- **No appointment with a lead time under 3 days ever received an SMS** (0 of 50,506), and those are the lowest-risk appointments. The "no SMS" group is therefore dominated by low-risk same-day visits.
- **Within every lead-time band from 3 days up, SMS recipients have *lower* no-show rates**, for example:

| Lead time | No SMS | SMS |
|---|---|---|
| 3 days | 24.6% | 21.3% |
| 5–7 days | 28.4% | 24.6% |
| 8–14 days | 33.8% | 28.1% |
| 15–30 days | 36.9% | 29.8% |
| 31–60 days | 38.4% | 31.5% |

- **Adjusted estimate:** this uses only eligible appointments (lead time ≥3 days) on normal days, controlling for lead time, age, conditions, gender, prior history and appointment date. An SMS is associated with a **5.4-percentage-point** lower no-show probability (95% CI 4.4–6.5; OR 0.76).

### Stronger evidence: the outage period
On **7 appointment days (9 May, 13 May, 16–20 May)** not a single SMS was sent. On every other weekday, about 82% of eligible appointments received one. I assume this was a system outage or pause rather than a choice tied to those particular patients. The outage gives a comparison that does not depend on who was chosen to get an SMS:

| | Normal days | Outage days |
|---|---|---|
| Eligible appointments (lead ≥3 days, which would normally get an SMS) | 28.6% | **32.5%** |
| Ineligible appointments (lead <3 days, never get an SMS) | 8.9% | **8.9%** |

No-shows rose only in the group that lost its reminders. The group that never gets reminders did not change, so the rise was not a general bad patch for attendance. The difference-in-differences is **+3.9 points** (95% CI 0.8–7.0, with standard errors clustered by day). Since only 82% of eligible appointments normally get an SMS, that works out to roughly **4–5 points per SMS**, which matches the adjusted regression.

**Caveat:** no-show rates in the eligible group fell somewhat in late May and June. If I compare only against nearby weeks (2–25 May), the outage effect shrinks to +2.9 points (CI −0.5 to +6.3). The effect is clearly in the "SMS helps" direction across every analysis I ran, but its exact size is uncertain: somewhere around 3–5 points.

### What that means in volume
Normal-day coverage is about 35,500 SMS over 6 weeks. At ~4–5 avoided no-shows per 100 SMS, that is roughly **1,400–1,900 attended appointments over the period** that would otherwise have been missed. I don't have the SMS cost or the cost of a missed slot, but an SMS typically costs a few cents while a wasted clinical slot costs far more, so the programme is very likely cost-effective.

### Recommendation on SMS: **keep and expand**
- **Close the coverage gap:** on normal days, 7,955 eligible appointments (18%) still got no SMS. Coverage is weakest at exactly 3 days' lead (53%) and among patients with a prior no-show (76%), who are the people who most need a reminder.
- **Extend to 1–2-day lead appointments:** 11,900 appointments with 21–24% no-show rates currently get no reminder. *This is an untested extension.* Roll it out as a randomised pilot (for example, alternate days or a random half of patients) so the effect can be measured directly.
- **Build in resilience and monitoring:** the outage went undetected long enough to cover 7 appointment days. Add an alert for when daily SMS volume drops to zero.

## 3. Other actions to reduce no-shows
1. **Shorten lead times where possible.** No-show risk rises steeply with lead time. Options include more same-day/open-access slots, and not booking routine follow-ups weeks out unless clinically needed.
2. **For long-lead bookings (≥8 days, 57% of no-shows): add a second reminder or a confirm/cancel step** a day or two before the appointment, and release slots that are not confirmed to a waitlist. (This needs piloting; it is not tested in this data.)
3. **Target extra outreach**, such as a phone call or a second SMS, at high-risk patients: those with a prior no-show, those aged 12–25, and welfare-enrolled patients, especially on long-lead bookings.
4. **Overbook selectively** using predicted risk (lead time plus history) rather than overbooking across the board.
5. **Measure:** run future changes as randomised pilots. The outage was a lucky natural experiment, but a deliberate test would settle how large the effect really is.

## Assumptions and data notes
- Lead time = appointment date minus booking date, in calendar days. Five rows had negative lead times (appointment before booking; all recorded as no-shows), and one row had age −1. I excluded these from the models. Seven patients are aged over 100; I kept them.
- "Prior no-show" uses only earlier appointments that fall inside this ~6-week window, so it understates true history. 62% of patients appear only once.
- The outage interpretation assumes those 7 days differed from the others only in SMS delivery. Eligible appointments on outage days were similar in lead time (median 13 vs 14 days) and age (37.2 vs 37.7).
- 8,718 rows are a second appointment for the same patient on the same day. I kept them as separate appointments.
- These are observational data from one network over 6 weeks in 2016. The effect sizes are estimates, not guarantees.
