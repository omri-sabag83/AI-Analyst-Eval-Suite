# Appointment No-Shows: Drivers and SMS Reminder Programme

## Bottom line

1. **Keep the SMS reminder programme and expand it.** At first glance SMS looks harmful: 27.6% of patients who got a text missed their appointment, against 16.7% of those who didn't. That comparison is misleading. Texts only go to appointments booked **3 or more days ahead**, and those appointments have far higher no-show rates whether or not a text is sent. When we compare like with like, **SMS lowers the no-show rate by about 4–5 percentage points**, from roughly 33% to roughly 28%, which is about a 15% relative reduction. An unplanned outage on 7 days in May, when no texts were sent, gives the cleanest test, and it confirms the effect.
2. **The biggest driver of no-shows is how far ahead the appointment was booked.** Same-day appointments are missed 4.6% of the time. Appointments booked 1–2 days ahead are missed 21–24% of the time, and those booked 2–8 weeks ahead 30–34% of the time. Other independent drivers are a previous no-show, being aged 12–35, being on the welfare programme (`Scholarship`), alcoholism, and neighbourhood.
3. **What to do:** make sure SMS goes out reliably to every eligible appointment, extend reminders to appointments booked 1–2 days ahead (as a test), shorten booking lead times where capacity allows, and add extra contact for the small group of repeat no-show patients.

---

## Data and assumptions

- 110,527 appointments for 62,299 patients. Appointment dates run from 29 Apr to 8 Jun 2016, a 6-week window. Overall no-show rate: **20.2%** (22,314 no-shows).
- I removed 6 rows: 5 where the appointment date was before the booking date, and 1 with age −1. That leaves 110,521 rows.
- Lead time = appointment date minus booking date, counted in calendar days.
- "Prior no-show" only counts the patient's **earlier appointment days within this 6-week window**. Same-day sibling appointments are excluded so the outcome can't leak into the predictor. History from before the window is not available, so this signal is understated.
- The data has no costs, no reason for each missed appointment, no record of whether a patient has a phone number, and no clinic or specialty field. All effects are estimated from observational data. They are not from a randomised trial.

## 1. What drives no-shows

No-show rate by factor (raw rates; all 110.5k appointments):

| Factor | Group | No-show rate | Appointments |
|---|---|---|---|
| **Lead time** | same day | **4.6%** | 38,562 |
| | 1–2 days | 21–24% | 11,938 |
| | 3–7 days | 25% | 20,247 |
| | 8–14 days | 31% | 12,025 |
| | 15–60 days | 33–34% | 25,654 |
| **Patient history** | missed an earlier appointment in window | **26.9%** | 14,114 |
| | attended all earlier ones | 18.8% | 30,119 |
| | first appointment in window | 19.4% | 66,288 |
| **Age** | 13–17 / 18–25 | 26.6% / 25.1% | 17,561 |
| | 56–75 | 15–16% | 22,112 |
| **Welfare (Scholarship)** | yes / no | 23.7% / 19.8% | 10,861 / 99,660 |
| **Neighbourhood** (>500 appts) | range | 15.7% (Do Cabral) – 28.9% (Santos Dumont) | |
| Gender, weekday, hypertension, disability | | essentially flat (19–21%) | |

**Adjusted model.** I fitted a logistic regression on all appointments, with standard errors clustered by patient. It includes lead time, age, sex, welfare, the chronic conditions, weekday, prior no-show and SMS. Results as odds ratios:
- Lead time dominates. Compared with same-day appointments, the odds are about 6× higher at 1 day ahead and 11–13× higher at 2+ weeks ahead.
- Prior no-show in the window: OR 1.51. Alcoholism: 1.37. Welfare: 1.23. Diabetes: 1.16 (all p<0.001).
- Age 13–17: OR 1.51 vs under-5s. Age 56–75: OR about 0.6.
- Gender, weekday and hypertension have little or no practical effect.

**Concentration.** 3,223 patients (5% of patients) missed 2 or more appointments in the 6 weeks. Together they account for **35% of all no-shows**.

Lead time is partly a proxy: same-day bookings are probably walk-ins or urgent visits, so the 4.6% partly reflects what kind of visit it is. Even among advance bookings, though, no-shows climb steadily with lead time (25% at 3–7 days, 33% beyond 2 weeks).

## 2. SMS reminders: do they work?

### Why the raw comparison is misleading
| | No SMS | SMS |
|---|---|---|
| No-show rate | 16.7% | 27.6% |
| Median lead time | 0 days | 14 days |

**No appointment booked fewer than 3 days ahead received an SMS.** That group includes all same-day bookings (4.6% no-show). The "no SMS" group is therefore mostly low-risk short-notice visits. This is Simpson's paradox: within every lead-time band, SMS recipients miss **fewer** appointments.

| Lead time | No SMS | SMS | Difference |
|---|---|---|---|
| 3–7 days | 26.6% | 23.8% | −2.8 pts |
| 8–14 days | 33.8% | 28.1% | −5.6 pts |
| 15–30 days | 36.9% | 29.8% | −7.1 pts |
| 31–60 days | 38.4% | 31.5% | −6.9 pts |
| 61+ days | 33.9% | 25.5% | −8.4 pts |

### Four independent estimates of the SMS effect (eligible appointments, lead ≥ 3 days)

| Method | Effect on no-show rate | 95% CI |
|---|---|---|
| Lead-time-standardised difference | −5.4 pts | — |
| Regression (lead days, age, sex, welfare, conditions, prior no-show, neighbourhood, appointment date) | −5.5 pts | −6.7 to −4.4 |
| **Natural experiment: SMS outage days** (difference-in-differences) | **−4.0 pts at day level ≈ −4.9 pts per SMS sent** | −2.2 to −5.7 (day level) |
| Same patient, with vs without SMS (patient fixed effects, 6,219 patients) | −2.6 pts | −3.8 to −1.4 |

**The outage natural experiment.** On 9, 13 and 16–20 May, **no SMS was sent at all** (0% coverage, 16,584 eligible appointments). On every other weekday, about 80–84% of eligible appointments got one. This looks like an operational failure, not a choice about which patients to text, so it works close to a randomised switch-off. I compared eligible appointments (≥3 days) with short-lead appointments (never texted, so a control group) on the same days. On outage days, no-shows among eligible appointments rose by **4.0 points** relative to the control (p<0.001). Short-lead appointments on outage days showed **no change** (8.9% vs 8.9%), which is a placebo check that the outage days were not simply "bad days."

**Caveats.**
- The within-patient estimate (−2.6 pts) is smaller. A simple comparison restricted to 2–25 May is also smaller: −1.0 pt, with a CI that includes zero.
- On normal days, the ~18% of eligible appointments that did not get an SMS may be patients without a usable phone number. That could inflate the cross-sectional estimates.
- A fair summary is **a true effect of roughly 3–5 points (about 10–17% relative)**, with the outage difference-in-differences as the most credible single estimate (about 4–5 points).

### What the programme is worth (estimates, 6-week window)
- The outage days alone (16.6k eligible appointments with no SMS) probably cost about **650 extra no-shows** (0.04 × 16.6k).
- Texting the ~7,900 eligible appointments that went unreached on normal days would prevent about **250–400 more no-shows** (3–5 points × 7.9k).
- SMS is cheap per message. With a ~4-point effect, one no-show is avoided per ~25 messages. Unless a text costs more than about 1/25 of the cost of an empty slot, the programme pays for itself. No cost data was provided, so leadership should plug in its own figures.

## 3. Recommendations

1. **Keep and expand SMS. Do not cut it.** The headline "SMS patients no-show more" is caused by who gets texted, not by the text itself.
2. **Fix delivery reliability.** Seven weekdays with zero sends cost an estimated ~650 attendances. Add monitoring with a daily alert if sends drop to 0. Also find out why about 18% of eligible appointments go unsent on normal days; if it is missing phone numbers, capture numbers at booking.
3. **Extend reminders to appointments booked 1–2 days ahead.** These 11.9k appointments get no reminder today and have a 21–24% no-show rate. Run this as an A/B test (randomise by patient or by day) to measure the effect directly. A randomised design would also settle the 3-vs-5-point uncertainty above.
4. **Reduce lead times.** No-shows rise from 25% to 33%+ as lead time grows from under a week to over two weeks. Where capacity allows, offer more short-notice or open-access slots. For long-lead bookings, send a second reminder and/or ask patients to confirm or cancel so slots can be released.
5. **Target high-risk patients with extra contact,** such as a phone call or confirmation request. Priority groups are patients with a previous no-show (5% of patients cause 35% of no-shows), teenagers and young adults, welfare recipients, and the highest-rate neighbourhoods. A simple risk score built from lead time, prior no-show, age and welfare status could also guide targeted overbooking.
6. **Collect better data:** SMS delivery and phone-on-file status, cancellation vs no-show, clinic or specialty, and longer patient history. This would sharpen both the targeting and the evaluation.
