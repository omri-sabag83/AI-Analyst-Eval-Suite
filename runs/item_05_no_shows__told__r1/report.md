# Appointment no-shows: drivers, the SMS reminder programme, and what to do

## Bottom line

1. **Keep the SMS reminder programme and expand it. Do not cut it.** On the raw numbers, patients who received an SMS miss *more* appointments (27.6% vs 16.7%). That comparison is misleading. SMS is sent only to appointments booked 3 or more days ahead, and those are the appointments that are missed most often. On a fair comparison, an SMS **lowers** the chance of a no-show by about **3–5 percentage points**, from about 33% to about 28%. That is roughly a 15% relative reduction.
2. **How far ahead an appointment is booked (lead time) is by far the strongest predictor of a no-show.** Same-day appointments are missed 4.6% of the time. Appointments booked 3+ days ahead are missed 29.7% of the time. Those 3+-day bookings are 54% of appointments but **80% of all no-shows**.
3. **Other risk factors are smaller but useful for targeting:** age 13–30, a previous no-show, the Scholarship (welfare) flag, alcoholism, and certain neighbourhoods.
4. **One-off incident:** on 7 appointment days in May 2016, no SMS was sent at all. I estimate this caused roughly **650–700 additional no-shows**. Whatever caused the gap should be found and stopped from recurring.

Tags used below: **[OBS]** means computed directly from the data. **[CON]** means the conclusion the evidence best supports, with the remaining uncertainty stated. **[HYP]** means plausible but not proven, with the data that would settle it.

---

## Data and method

- **Grain and coverage:** one row per scheduled appointment. There are 110,527 appointments for 62,299 patients across 81 neighbourhoods. Appointment dates run from 29 Apr to 8 Jun 2016, covering 27 distinct days. Booking dates go back to Nov 2015.
- **Outcome:** `No-show = Yes`. The overall rate is 20.2% (22,319 no-shows).
- **Data-quality issues**, listed before the findings:
  - 5 rows have the appointment date *before* the booking date. All 5 are recorded as no-shows, so they look like data errors. One row has Age = −1. These 6 rows were dropped, leaving 110,521 for analysis.
  - Some weekdays are missing from the calendar (21–23 and 26–27 May). There are only 39 Saturday appointments.
  - 8,718 appointments are a second or later appointment for the same patient on the same day. They are kept as separate appointments.
  - The appointment window is short, about 6 weeks. "Previous no-show history" therefore covers only earlier appointments *inside this extract*, and most appointments (72%) have no prior history at all. To avoid using information from the future, history counts only appointments that took place before the current one was booked.
  - The data has no field for visit type, specialty, clinic, phone-number availability or SMS delivery status. This limits how far causes can be explained.
- **Methods:**
  - Cross-tabulations, always reported with counts.
  - Logistic regression for drivers.
  - For the SMS effect, a *natural experiment*: a difference-in-differences comparison using days when no SMS was sent. It is checked against placebo groups, a permutation test, within-patient comparisons and covariate-adjusted models.

---

## Finding 1: lead time dominates [OBS]

| Lead time (booking → appointment) | Appointments | Share of appts | No-show rate | Share of all no-shows |
|---|---|---|---|---|
| Same day | 38,562 | 35% | 4.6% | 8% |
| 1–2 days | 11,938 | 11% | 22.7% | 12% |
| 3+ days | 60,021 | 54% | 29.7% | 80% |

More detail by lead-time band:

| Lead time | 3–7 d | 8–14 d | 15–30 d | 31–60 d | 61+ d |
|---|---|---|---|---|---|
| No-show rate | 25.2% | 30.5% | 32.6% | 34.2% | 28.4% |
| Appointments | 17,510 | 12,025 | 17,371 | 8,283 | 2,095 |

- The pattern holds after adjusting for age, sex, health conditions, Scholarship, day of week, SMS and history. Compared with same-day appointments, the odds of a no-show are about 6–8× higher for 1–3-day lead times and 11–13× higher for 8+ days.
- It also holds within every age group. For example, among 18–30-year-olds the no-show rate is 5.1% same-day vs 36.5% for 3+ days.

**[HYP] Is lead time itself the cause?** Not established. Same-day appointments may be largely walk-ins or urgent visits, where the patient is already motivated or even present. Long-lead appointments may be routine follow-ups. Two things would show whether shortening lead times prevents no-shows rather than just moving them around:
- visit type and specialty data;
- a pilot that offers shorter-notice slots for the same visit types.

## Finding 2: the SMS programme works; the raw comparison is confounded [CON]

**Why the raw numbers mislead [OBS].**
- SMS is never sent to appointments booked fewer than 3 days ahead (0 of about 50,500).
- About 82% of 3+-day appointments receive one on normal days.
- So the SMS group is made up almost entirely of high-risk, long-lead appointments.

Within every lead-time band on normal days, SMS recipients miss **fewer** appointments:

| Lead time | No-show, no SMS | No-show, SMS | Appointments (no SMS / SMS) |
|---|---|---|---|
| 3–7 d | 27.1% | 24.0% | 6,868 / 10,642 |
| 8–14 d | 33.8% | 28.1% | 5,021 / 7,004 |
| 15–30 d | 36.9% | 29.8% | 6,851 / 10,520 |
| 31–60 d | 38.4% | 31.5% | 3,224 / 5,059 |
| 61+ d | 33.9% | 25.5% | 744 / 1,351 |

(This table includes the no-SMS days, so the "no SMS" column mixes eligible non-recipients with outage-day appointments.)

**Natural experiment: the stronger evidence [OBS].** On 9, 13 and 16–20 May (7 appointment days), *no* appointment received an SMS. On every other day, 76–84% of eligible appointments did. That lets me compare the same kinds of appointment with and without the programme running:

| No-show rate | Normal days | No-SMS days | Change |
|---|---|---|---|
| Eligible (lead ≥3 d) | 28.6% (n=43,437) | 32.5% (n=16,584) | **+3.9 pp** |
| Not eligible (lead 0–2 d) – control | 8.93% (n=37,127) | 8.93% (n=13,379) | 0.0 pp |
| Lead 1–2 d only – placebo | 22.7% | 22.7% | 0.0 pp |

- **Difference-in-differences with date and lead-time controls:** +4.1 pp (SE 0.9, clustered by date). This is the effect of the programme as it actually runs, where 82% of eligible appointments get an SMS.
- **Per SMS actually received:** about **−5 pp**.
- Checks that agree:
  - an adjusted regression within normal days: −5.7 pp;
  - a date-level permutation test: p ≈ 0.04 in my run, p < 0.01 in the independent check;
  - a within-patient comparison (the same patient's appointments with vs without SMS): **−2.5 pp** (SE 0.6), the most conservative estimate.
- Patient mix (age, Scholarship, conditions) on no-SMS days matched normal days.

**Remaining uncertainty.**
- The no-SMS days fall in one block in mid-May. A narrower window (2–25 May only) gives a smaller effect of +2.8 to +3.2 pp, which is borderline significant.
- I do not know *why* SMS stopped on those days, or whether anything else changed at the same time.
- An independent re-analysis that did not see my reasoning reached the same verdict: the claim holds, with this caveat.

**Conclusion:** the effect is most likely **2.5–5 pp per SMS**, and it is clearly not harmful.

## Finding 3: other drivers, for targeting [OBS]

The rates below are raw. The odds ratios (OR) are adjusted for lead time and the other factors.

- **Age:**

  | Age | 0–12 | 13–18 | 19–30 | 31–45 | 46–60 | 61–75 | 76+ |
  |---|---|---|---|---|---|---|---|
  | No-show rate | 20.5% | 26.1% | 24.7% | 21.4% | 17.8% | 14.9% | 16.1% |
  | Appointments | 21,035 | 7,830 | 16,763 | 21,953 | 23,179 | 14,370 | 5,391 |

  Adjusted ORs: 1.41 for ages 13–18 and 0.56 for ages 61–75, both compared with children aged 0–12.
- **Previous no-show in this window:** 21.5% (n=9,913) vs 13.5% for patients who attended all earlier appointments (n=20,966). Adjusted ORs are 1.42 and 0.83 compared with no history.
- **Scholarship (welfare):** 23.7% (n=10,861) vs 19.8%. Adjusted OR 1.25.
- **Alcoholism:** adjusted OR 1.38, n=3,360. The raw rate shows no gap only because these patients tend to be older.
- **Diabetes:** adjusted OR 1.16.
- **Neighbourhood:** among neighbourhoods with more than 500 appointments, rates range from 15.7% (Do Cabral) to 28.9% (Santos Dumont). Itararé has 26.3% on 3,514 appointments.
- **Negligible:** sex (OR 1.06), hypertension, disability, day of week (19–21%).

These are associations for identifying who to target, not proven causes **[HYP]**. Scholarship and neighbourhood probably stand in for barriers such as transport, work and cost.

## Incident vs standing issues

- **Incident:** the 7-day SMS gap in May.
  - Rough counterfactual **estimate**: 16,584 eligible appointments × 4.1 pp ≈ **680 additional no-shows**.
  - This assumes normal-day SMS coverage and the effect estimated above.
  - The cause of the gap needs to be found, whether a system outage, a contract lapse or a policy change.
- **Standing issues:**
  - The long-lead booking pattern.
  - About 18% of eligible appointments get no SMS even on normal days (7,955 appointments in this window). These non-recipients have a 33.1% no-show rate.
  - For about 10% of repeat patients, every eligible appointment went without an SMS. That suggests missing or invalid phone numbers **[HYP]**. Phone-number data would confirm it.

---

## Recommendations

**SMS programme: keep it and expand it.**

1. **Make delivery reliable.**
   - Monitor daily send volumes and alert when they fall to zero.
   - The May gap alone is estimated to have cost about 680 attended visits.
2. **Close the 18% coverage gap among eligible appointments.**
   - Collect and validate mobile numbers at booking.
   - At 2.5–5 pp, reaching these 7,955 appointments would avoid an **estimated 200–400 no-shows per 6 weeks**. This assumes the patients are reachable by SMS.
   - Use a phone call for patients without a mobile.
3. **Test SMS for 1–2-day lead times**, currently excluded. These appointments have a 22.7% no-show rate on about 12,000 appointments. The effect here is not measured, so run a **randomised** pilot rather than rolling it out network-wide.
4. **Test timing and content** in randomised trials, so future decisions do not rely on accidental outages:
   - a second reminder for long-lead appointments;
   - an easy way to confirm or cancel by replying to the SMS.

**Wider no-show reduction.**

5. **Reduce long lead times where clinically possible.** Options include more same-day or short-notice capacity and reminder-and-confirm workflows for bookings made 2+ weeks out. Pilot this first, because the lead-time effect may partly reflect visit type (see [HYP] in Finding 1).
6. **Target high-risk appointments with extra contact**, such as a call or a confirmation request. High risk means:
   - lead time of 2+ weeks;
   - patient aged 13–30;
   - a previous no-show;
   - the Scholarship flag;
   - the highest-rate neighbourhoods.

   A simple risk score built from these fields could rank daily appointment lists.
7. **Re-use freed slots.** Make it easy to cancel by SMS reply, and consider careful overbooking only for the highest-risk long-lead slots.
8. **Collect the missing data:** visit type and specialty, SMS delivery status, phone-number availability, and a longer appointment history. Without these, causes can't be confirmed and the risk targeting can't be sharpened.
