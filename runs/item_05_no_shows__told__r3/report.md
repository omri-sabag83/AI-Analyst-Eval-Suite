# Appointment no-shows: what drives them, and what to do about SMS reminders

## Bottom line

1. **Keep the SMS reminder programme and expand it. Do not cut it.** At first glance SMS looks harmful: patients who got an SMS missed **27.6%** of appointments, against **16.7%** for those who did not. That comparison is misleading. SMS is only ever sent for appointments booked **3 or more days ahead**, and those appointments carry far more risk than the same-day and next-day bookings that make up the "no SMS" group. When like is compared with like, SMS **lowers** no-shows by roughly **3–5 percentage points** (pp) per reminder sent. That is about a 10–15% relative cut on a base of about 30%. The best evidence is a natural experiment: on 7 appointment days no SMS went out at all.
2. **The biggest driver of no-shows is how far ahead the appointment was booked.** The no-show rate is **4.6%** for same-day bookings, **21–24%** at 1–2 days, **25%** at 3–7 days and **33–34%** at 2–8 weeks. About 80% of all no-shows come from bookings made 3 or more days ahead.
3. **Other drivers are smaller.** Age matters: teenagers and young adults miss most, over-60s least. So does a past no-show (+6 pp), being on the welfare programme ("Scholarship", +3 pp) and alcoholism (+4.5 pp). Gender, weekday, neighbourhood, hypertension and disability make little or no difference.

## Data and method

- **Grain and coverage.** One row per scheduled appointment. There are 110,527 appointments for 62,299 patients, on 27 appointment days from **29 Apr to 8 Jun 2016** (about 6 weeks). Bookings were made between Nov 2015 and Jun 2016. The overall no-show rate is 20.2% (22,319 no-shows).
- **Data quality.**
  - No missing values or duplicate appointment IDs.
  - I dropped 5 rows whose appointment date is *before* the booking date (all recorded as no-shows) and 1 row with age −1. That leaves 110,521 rows.
  - Saturday 14 May has only 39 appointments; it is kept in the data but ignored where rates are compared.
  - The data has no times for appointments, only dates, so lead time is measured in calendar days.
  - About 15% of rows are a patient with more than one appointment on the same day.
- **Same-day bookings (35% of appointments) may be partly walk-ins** registered when the patient arrives. That would make their low no-show rate partly built into how they are recorded. For that reason I also quote the lead-time pattern for bookings made 1 or more days ahead.
- **"Prior no-show" history** only covers the 6-week window, so it understates each patient's real history.
- **Methods.** Comparisons within lead-time bands; logistic regression with average marginal effects; a natural experiment using the no-SMS days, checked against a placebo group and with a day-level bootstrap. A separate analyst re-checked the SMS conclusion from the raw data without seeing my reasoning (see Verification).

## Finding 1: The raw SMS comparison is confounded by booking lead time

| Days between booking and appointment | Appointments | No-show rate | Share sent an SMS |
|---|---|---|---|
| 0 (same day) | 38,562 | 4.6% | 0% |
| 1 | 5,213 | 21.4% | 0% |
| 2 | 6,725 | 23.8% | 0% |
| 3 | 2,737 | 23.5% | 33% |
| 4–7 | 17,510 | 25.2% | 61% |
| 8–14 | 12,025 | 30.5% | 58% |
| 15–30 | 17,371 | 32.6% | 61% |
| 31–60 | 8,283 | 34.2% | 61% |
| 61+ | 2,095 | 28.4% | 64% |

*Observed:* no appointment booked less than 3 days ahead ever got an SMS. So the "no SMS" group is dominated by low-risk same-day bookings. Once the comparison is limited to appointments booked 3 or more days ahead, the direction reverses:

| | Appointments | No-show rate |
|---|---|---|
| Booked 3+ days ahead, got SMS | 35,482 | 27.6% |
| Booked 3+ days ahead, no SMS | 24,539 | 32.7% |

Within every lead-time band, SMS recipients missed fewer appointments, by 3–8 pp. The drop stays at 5.4 pp after a regression adjusts for lead time, age, gender, welfare status, health conditions and weekday (95% CI 4.6–6.1). That figure is still observational: we don't know why some eligible patients got no SMS.

## Finding 2: Natural experiment shows SMS causes fewer no-shows (the key evidence)

*Observed:* on 7 appointment days (**9, 13 and 16–20 May**) **no SMS was sent to anyone**. On every other day about 82% of eligible appointments (booked 3+ days ahead) got one. Patients on the no-SMS days look like everyone else: same average age, welfare share and hypertension rate.

| Booked 3+ days ahead? | Normal SMS days | No-SMS days |
|---|---|---|
| Yes (would normally get SMS) | 28.6% (n=43,437) | **32.5%** (n=16,584) |
| No (never get SMS: placebo group) | 8.9% (n=37,123) | 8.9% (n=13,377) |

- The **placebo group shows no change**, so the no-SMS days were not unusual days in general. Only the patients who would normally have been texted missed more.
- **Size of the effect:**
  - Over the full period, the no-SMS days had 3.9 pp more no-shows (day-level bootstrap 95% CI 2.4–5.6). Controlling for patient characteristics gives the same figure.
  - Rates were drifting down into June, which inflates the full-period figure. Using only nearby days (2–25 May), the increase is 2.5 pp, or 2.9 pp after subtracting the placebo group's change.
  - Normal days reach only 82% of eligible patients, so the effect per SMS actually sent is somewhat larger: **about 3 pp (narrow window) to 5 pp (full period)**.
- **Conclusion:** SMS reminders reduce no-shows by roughly 3–5 pp per reminder sent. *Caveats:* all 7 no-SMS days fall in one 2-week block, so a shock specific to those dates cannot be fully ruled out. The reason for the outage is unknown.

**Estimated impact (counterfactual, not measured):**
- The 35,482 reminders sent averted roughly **1,000–1,800 no-shows** over the 6 weeks (35,482 × 3–5 pp). For comparison, there were 22,319 actual no-shows.
- Put another way, about 20–35 SMS are needed to prevent one no-show.
- A failed SMS system costs about 400–700 extra no-shows per week-and-a-half outage like the one in May. That is 13,500 eligible appointments that would normally have been texted × 3–5 pp.

## Finding 3: Other drivers of no-shows

These are average marginal effects from a logistic regression that adjusts for all factors together. The regression fits only moderately well (AUC 0.73, against 0.70 for lead time alone).

| Factor | No-show rate (n) | Adjusted effect |
|---|---|---|
| **Lead time** | 4.6% same day → 21–24% at 1–2 days → 33–34% at 15–60 days | +27 to +37 pp vs same day; still +13 pp from 1–2 days to 31+ days |
| Age 13–18 / 19–30 | 26.1% / 24.7% | +5.7 / +3.3 pp vs age 31–45 |
| Age 61–75 / 76+ | 14.9% / 16.1% | −7.6 / −5.7 pp |
| Missed a previous appointment (in window) | 26.9% (14,114) vs 18.8% if always attended | +6.0 pp |
| Scholarship (welfare programme) | 23.7% (10,861) vs 19.8% | +3.1 pp |
| Alcoholism | 20.1% (3,360) | +4.5 pp (raw rate is unremarkable; patients with alcoholism are older) |
| Diabetes | 18.0% | +2.1 pp after adjustment |
| Gender, weekday, hypertension, disability | ±1 pp | negligible |
| Neighbourhood (54 areas with ≥500 appts) | 15.7%–28.9%; middle half 18–22% | modest; a few hotspots (e.g. Santos Dumont 28.9%, Santa Clara, Itararé about 26%) |

The lead-time effect is a strong observed association. That **long waits themselves cause no-shows** is a hypothesis: forgetting, the problem resolving on its own, or plans changing. It is plausible but not proven. Part of the gap between same-day and other bookings may be walk-in recording (see Data and method). The rise from 21% at 1–2 days to 34% at 31–60 days is not affected by that issue.

## Recommendations

1. **Keep the SMS programme and expand it.** The evidence supports it, and texts are cheap compared with a wasted clinic slot.
   - **Find out why about 18% of eligible appointments get no SMS** on normal days (7,955 in the period). Missing or invalid phone numbers are one possibility. Closing that gap would avert an estimated 250–400 more no-shows per 6 weeks.
   - **Monitor delivery and alert on failures.** The 7-day outage in May probably cost about 400–700 extra no-shows (estimate). Find out what happened.
   - **Pilot SMS for bookings made 1–2 days ahead**, which currently get none (11,938 appointments, about 23% no-show). Whether the same effect applies there is a hypothesis, so run it as a **randomised pilot**. Trial a second reminder for bookings 2+ weeks ahead the same way.
2. **Shorten booking lead times.** This is the largest lever. Offer more same-day and short-notice slots (open access). For bookings far ahead, send a confirm-or-cancel message so freed slots can be reused or waitlisted.
3. **Target extra contact at high-risk appointments:** long lead time combined with teen or young-adult patients, a past no-show, or welfare-programme patients. Use a phone call or a second SMS. Given the model's moderate accuracy, also consider modest **overbooking** for long-lead slots, sized to the 30%+ expected no-show rate.
4. **Measure properly from now on.** Record the reasons SMS was not sent and SMS delivery status, and randomise any programme changes. With only 6 weeks of data, impact figures here are estimates. A longer data pull would also strengthen the past-no-show signal.

## Verification

- **Rigor checklist.** I ran an analytical rigor checklist on the draft. Changes it led to:
  - The SMS effect is quoted as a range, because the June downward trend inflates the full-period estimate.
  - The same-day walk-in caveat was added.
  - The causal and extrapolated claims above are marked as hypotheses.
- **Independent check.** A separate analyst re-checked the SMS conclusion from the raw data without seeing my reasoning. Verdict: **holds, with a caveat.** They found the same reversal (27.6% vs 32.7%) and the same identical placebo rates (8.92% vs 8.92%). Their implied effect per SMS sent was about 5 pp over the full period and about 3 pp in the narrow window.
  - The caveat: the size of the effect depends on the time window, and all seven no-SMS days fall in one block. One cut that limited the comparison group to bookings 1–7 days ahead gave a smaller effect that was not statistically significant.
  - The direction (SMS reduces no-shows) held in every main test.

## Assumptions

- Lead time is measured in calendar days, because appointment times are missing.
- `SMS_received` is taken to mean an SMS was sent, not necessarily read.
- "Scholarship" is taken to mean enrolment in a welfare programme.
- All figures apply only to this 6-week sample.
