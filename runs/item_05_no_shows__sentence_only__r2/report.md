# Appointment no-shows: what drives them, and what to do about SMS reminders

**Data:** 110,527 appointments (62,298 patients) due between 29 Apr and 8 Jun 2016, across 81 neighbourhoods. The overall no-show rate is **20.2%**.

## Bottom line

1. **Keep the SMS programme and expand it.** In the raw numbers, patients who got an SMS look *worse*: 27.6% no-show with SMS against 16.7% without. That gap is misleading. SMS is only ever sent for appointments booked 3 or more days ahead, and those appointments miss far more often whatever happens. Three separate comparisons all find the opposite: **an SMS cuts the chance of a no-show by about 3–5 percentage points**, roughly a 12–15% relative reduction. The strongest of these comes from a week when SMS sending stopped completely.
2. **The biggest driver of no-shows is how far ahead the appointment is booked.** Same-day appointments: 4.6% no-show. Appointments booked 3+ days ahead: 28.6%. Booked 1–2 days ahead: 22.7%.
3. **The next biggest driver is the patient's own record.** Patients who missed most of their earlier appointments in this window miss 47% of their advance-booked appointments. Patients with a clean record miss 26%.
4. Younger patients (teenagers and those in their 20s), patients on the welfare scholarship and some neighbourhoods also run higher. These effects are smaller.

## 1. The SMS programme

### Why the simple comparison is wrong
- **No appointment booked less than 3 days ahead ever got an SMS.** That covers 38,562 same-day bookings and 11,928 bookings made 1–2 days ahead. Same-day bookings almost always attend.
- So the "no SMS" group is mostly short-notice bookings that rarely miss, while the "SMS" group is all long-notice bookings that often miss. Comparing them measures booking lead time, not the effect of the SMS.

### Evidence that SMS works (appointments booked 3+ days ahead only)

| Method | Effect of SMS on no-show rate |
|---|---|
| Matching by lead time (5 lead-time bands) | Lower with SMS in every band: by 2.8 to 8.4 points |
| Regression adjusting for lead time, age, sex, welfare, health conditions, weekday, neighbourhood and the patient's past no-shows | **−4.8 points** (95% CI −5.6 to −4.0) |
| Same patient, comparing their appointments with and without an SMS (6,219 patients) | −2.7 points (−3.9 to −1.5) |
| **Natural experiment: SMS outage** (below) | **−4.0 points** across everyone eligible; about **−4.7 points per SMS actually sent** |

**The outage.** On 7 appointment days (9 May, 13 May and 16–20 May), *none* of the 16,584 eligible appointments got an SMS. On the other 19 days, 82% did. The outage days don't look different in other respects: similar lead times, ages, welfare share and share of first-time patients.
- On outage days, eligible appointments had a 32.5% no-show rate, against 28.6% on normal days.
- That rise could just be a bad stretch of days. To check, I used appointments booked less than 3 days ahead as a control group, because they never get an SMS anyway. Their no-show rate was **exactly the same on outage and normal days (8.9% on both)**.
- Comparing the change in the two groups gives an effect of **+3.8 points** in no-shows when SMS stops (95% CI +2.1 to +5.5).
- I also re-ran the comparison with the 7 "outage" days assigned at random among the 26 days, many times over. A gap this large came up only about 2% of the time (p ≈ 0.02).

**Scale.** Across the 35,482 SMS sent in this window, an effect of about 4.7 points means roughly **1,600–1,700 visits that would otherwise have been missed**. Cutting the programme would bring those no-shows back.

### SMS recommendations
- **Keep the programme.** The evidence that it works is consistent across methods, and texts cost little.
- **Close the coverage gap.** On normal days, 7,947 eligible appointments (18%) still got no SMS. If these patients react like the rest, about **370 more visits** would be kept in this window.
- **Set up monitoring and alerts for SMS sending.** The 7-day outage most likely cost about **630 extra no-shows** (3.8 points × 16,584 appointments).
- **Run a trial of SMS for appointments booked 1–2 days ahead.** These miss 22.7% of the time and get no SMS today. This data can't show whether a text would help this group, so test it, for example by randomising by day or by clinic.

## 2. What drives no-shows

These are odds ratios from a single model fitted to all appointments, with each factor adjusted for the others.

| Factor | Raw no-show rate | Adjusted effect |
|---|---|---|
| **Booking lead time** | same day 4.6%; 1–2 days 22.7%; 3–7 days 25.0%; 8–14 days 30.5%; 15–60 days 33–34% | Odds 7–13× higher than same-day. This is by far the largest effect. |
| **Patient's own past no-shows** | none 17%; missed under half 24%; missed half or more 35% | Odds 1.6× and 2.6× higher than a clean record |
| **Age** | 13–30: 25–26%; 61+: 15–16% | Odds 1.25–1.47× higher at ages 13–30; 0.6–0.7× at 61+ |
| Welfare scholarship | 23.7% vs 19.8% | Odds 1.23× higher |
| Alcoholism | 20.1% (similar to others in raw terms) | Odds 1.37× higher once other factors are adjusted |
| Neighbourhood | 16% to 29% (areas with 500+ appointments) | Large differences between areas |
| Sex, hypertension, diabetes, disability, weekday | Within about 1–3 points | Small or no effect |

Lead time is the main lever. 54% of appointments are booked 3+ days ahead, and they account for **80% of all no-shows**.

## 3. Recommendations to reduce no-shows

1. **Keep SMS, fix the gaps and monitor it** (Section 1). This is the most clearly proven action.
2. **Cut booking lead times where clinically possible.** Options include same-day or next-few-days slots ("open access"), shorter waiting lists, and a re-confirmation contact for appointments booked more than 2 weeks ahead. *Caveat:* same-day patients are partly a different group (for example, people who came in with an acute need). Shortening lead times probably won't bring every booking down to the same-day rate of 4.6%. Pilot it and measure the result.
3. **Focus on high-risk appointments.** Flag bookings with a long lead time, a patient with past no-shows, a patient aged 13–30 or on welfare, or a high no-show neighbourhood. Give them extra contact, such as a phone call or a second SMS, and offer easy rescheduling. For example, patients with a poor record booked 3+ days ahead miss **47%** of appointments.
4. **Use targeted overbooking** in clinics and time slots with long lead times and high predicted risk, so that capacity lost to no-shows can be refilled.
5. **Look at the worst neighbourhoods** (e.g. Santos Dumont 29%, Santa Clara 26%, Itararé 26%) for barriers such as transport, opening hours or contact details that are out of date.
6. **Test new measures properly.** Roll them out by randomised day or clinic, as the accidental outage showed is possible, so the effect can be measured.

## Assumptions and limitations
- **Lead time** is calendar days from booking date to appointment date. 5 appointments with a negative lead time and 1 with age −1 were dropped from the models.
- **"Past no-shows"** only counts appointments within this 6-week window, put in order by appointment date. Appointments on the same day may be ordered imperfectly.
- **SMS is not randomly assigned.** The outage comparison is the strongest evidence, but it rests on the assumption that nothing else happened on those 7 days that affected advance bookings differently from short-notice bookings. I could not observe the cause of the outage.
- **The data cover only ~6 weeks in 2016** and only one SMS design. The effect of different timing, wording or more than one text is unknown.
- **No cost data was provided.** The SMS recommendation rests on the effect size together with the usual very low cost per text. Leadership should check that against the actual programme cost.
- **The drivers in Section 2 are associations, not proven causes.** The model is for targeting high-risk appointments, not for proving that changing a factor will change behaviour.
