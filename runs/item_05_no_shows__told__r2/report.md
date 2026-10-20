# Appointment no-shows: what drives them, and what to do about SMS reminders

## Bottom line

1. **Keep the SMS reminder programme and fix its gaps. Do not cut it.** At first glance SMS looks harmful: patients who got an SMS no-showed *more* (27.6% vs 16.7%). That comparison is misleading. SMS is only sent for appointments booked **3 or more days ahead**, and those appointments carry most of the no-show risk. Comparing like with like, an SMS lowers the chance of a no-show by about **2–6 percentage points**, with a best estimate of **≈4 points** (roughly a 15% relative reduction). A natural experiment backs this up: on 7 days in May no SMS went out at all, and no-shows among eligible appointments rose on exactly those days.
2. **The biggest driver of no-shows is how far ahead the appointment was booked.** Same-day bookings no-show 4.6% of the time. Bookings made 1–2 days ahead no-show 23% of the time, and bookings made 2+ weeks ahead about 33%. Appointments booked 3+ days ahead are 54% of all appointments but **80% of all no-shows**.
3. **Other drivers are secondary.** These are teenagers and young adults (13–30), patients on the *Scholarship* welfare programme, patients who already missed an appointment in this window, and a handful of neighbourhoods. Gender, weekday, hypertension and diabetes make little or no difference.

---

## Data and method (read first)

- **Grain and coverage:** one row per scheduled appointment. There are 110,527 appointments for 62,299 patients across 81 neighbourhoods. Appointment dates run from **29 Apr to 8 Jun 2016**, 27 days in total (about 6 weeks). Some bookings were made as early as Nov 2015.
- **Overall no-show rate:** 20.2% (22,319 no-shows).
- **Data quality:**
  - I excluded 5 rows where the appointment date is before the booking date (all were no-shows) and 1 row with age −1. That leaves 110,521 rows.
  - 7 ages above 100 look implausible but were kept.
  - `Handcap` is coded 0–4, not yes/no.
  - Only 39 appointments fall on a Saturday.
  - There are no missing values and no duplicate appointment IDs.
- **Definitions I had to assume:**
  - *Lead time* is the appointment date minus the booking date, in calendar days.
  - `SMS_received` is taken to mean an SMS was delivered. The data has no record of SMS sent but not delivered, and no send dates.
  - The data shows a clear SMS rule: **no appointment with a lead time of 0–2 days ever got an SMS**. From 3 days onward, about 82% did on normal days. I inferred the "3+ days" eligibility rule from this pattern. Nobody confirmed it.
- **Window limits:**
  - "Previous no-show" only counts appointments on earlier days *inside this 6-week window*. A patient labelled "first in window" may still have a longer history.
  - Six weeks of data cannot show a trend or any seasonal pattern.
- **Methods:**
  - Cross-tabulations, with rates always shown next to counts.
  - Comparisons standardised for lead time.
  - Logistic and linear regressions with controls.
  - A natural experiment using the SMS outage days.
- **Checks:**
  - I put the findings through a rigor checklist.
  - A separate analyst re-checked the SMS conclusion from the raw data without seeing my reasoning. Their verdict was "holds, with a caveat on the size of the effect", which is reflected below.
- **Tags:** OBS = computed directly from the data; CON = the best-supported conclusion; HYP = plausible but not shown by this data.

---

## Finding 1: SMS reminders reduce no-shows. The raw comparison points the wrong way.

**[OBS] The raw comparison is confounded by lead time.**

| Lead time | Appointments | No-show rate | Share with SMS |
|---|---|---|---|
| Same day (0) | 38,562 | 4.6% | 0% |
| 1–2 days | 11,938 | 22.7% | 0% |
| 3–7 days | 20,247 | 25.0% | 57% |
| 8–14 days | 12,025 | 30.5% | 58% |
| 15–30 days | 17,371 | 32.6% | 61% |
| 31+ days | 10,378 | 33.0% | 62% |

Appointments without an SMS are mostly same-day bookings, which almost always attend. That is why "no SMS" looks better in the raw totals.

**[OBS] Within each lead-time band, SMS recipients no-show less.**

| Lead time | No SMS: rate (n) | SMS: rate (n) | Difference |
|---|---|---|---|
| 3–7 days | 26.6% (8,699) | 23.8% (11,548) | −2.8 pp |
| 8–14 days | 33.8% (5,021) | 28.1% (7,004) | −5.6 pp |
| 15–30 days | 36.9% (6,851) | 29.8% (10,520) | −7.1 pp |
| 31–60 days | 38.4% (3,224) | 31.5% (5,059) | −6.9 pp |
| 61+ days | 33.9% (744) | 25.5% (1,351) | −8.4 pp |

**[OBS] Several adjusted estimates point the same way, among appointments booked 3+ days ahead:**

| Method | Effect of SMS on no-show rate |
|---|---|
| Standardised to each exact lead-time day (105 groups) | −5.5 pp |
| Linear regression: lead time, age, sex, Scholarship, health conditions, weekday, neighbourhood (clustered by patient) | −5.2 pp (95% CI −6.0 to −4.5) |
| Logistic regression with the same controls | odds ratio 0.76–0.78 |
| Same patient, SMS vs no-SMS appointments (independent check) | −2.8 pp |
| **SMS outage natural experiment** (below) | **−1.7 to −5.0 pp**, depending on which days it is compared with |

**[OBS] The SMS outage natural experiment.**
- On 9 May, 13 May and 16–20 May, **no appointment received an SMS**. On every other weekday, about 80% of eligible appointments did.
- On those days, no-shows among eligible (3+ days) appointments were **32.5%** (16,584 appointments). On all other days they were **28.6%** (43,437 appointments). Adjusted for lead time, age and other factors, the jump is **+3.9 pp (95% CI 2.7–5.2)**.
- **A control group that never gets an SMS did not change.** Appointments booked 0–2 days ahead no-showed **8.9% on outage days and 8.9% on other days**. So the outage days were not generally bad days for attendance.
- Every outage day shows the effect. Dropping any single outage day leaves the jump between +3.5 and +4.2 pp.
- **Caveat:** eligible no-shows were drifting down over the period, from about 30% in early May to about 27% in June. Comparing only with nearby days shrinks the estimate:
  - against early May only: +2.4 pp;
  - in the tightest window tested (4–25 May): about +1.3 pp, which is not statistically significant.
  - Seven outage days is a small natural experiment.

**[CON] SMS reminders cause a real reduction in no-shows of roughly 2–6 percentage points per eligible appointment, with a best estimate of about 4 pp.** Every method agrees on the direction. The size is uncertain: the cleaner designs give the lower end of the range.

**[HYP] Why some eligible appointments got no SMS on normal days is unknown.** About 18% of eligible appointments on normal days missed out. Possible reasons include missing phone numbers, opt-outs or failed sends. This group no-showed 33% of the time, against 27.6% for those reached. Part of that gap may come from who these patients are, not from the missing SMS. *To confirm:* get the SMS provider's send and delivery logs and the rule that decides who gets an SMS.

**[OBS / estimate] Value of the programme over the 6-week window.**
- Counterfactual: 35,482 SMS-reached appointments × 2–5 pp effect ≈ **700–1,800 no-shows avoided**, central estimate ≈1,400. That is about 6% of all no-shows.
- This is an **estimate**. It assumes the effect is the same across the people who were reached.

**Two kinds of coverage gap:**
- **One-off incident:** the 7-day outage left 16,584 eligible appointments without a reminder. At the estimated effect, that is roughly **300–800 avoidable no-shows** (estimate).
- **Ongoing gap:** about 8,000 eligible appointments every 6 weeks get no SMS even on normal days. That is roughly **150–400 avoidable no-shows** per 6 weeks (estimate).

## Finding 2: Lead time is the dominant driver of no-shows

- **[OBS]** The no-show rate rises steeply with lead time (table above). In a logistic model with all other factors held constant, the odds of a no-show are **7–13× higher** for appointments booked ahead than for same-day ones.
- **[OBS]** Lead time alone separates no-shows from attenders about as well as the full model:
  - lead time only: AUC 0.70;
  - full model: AUC 0.73.
- **[OBS]** The pattern holds in every age group.
- **[HYP]** Many same-day bookings may be walk-ins registered when the patient arrives. That would make their 4.6% rate partly an artefact of how bookings are recorded, not something to copy. *To confirm:* a booking-channel field (walk-in vs phone vs online).
- **[HYP]** Long waits mean patients forget, recover, or get care elsewhere. The data cannot tell which.

## Finding 3: Secondary patient-level drivers

These figures come from a logistic model that holds lead time, SMS and the other factors constant. **[OBS]**

| Factor | Raw no-show rate (n) | Adjusted odds ratio |
|---|---|---|
| Age 13–18 | 26.1% (7,830) | 1.48 vs age 31–45 |
| Age 19–30 | 24.7% (16,763) | 1.26 |
| Age 61–75 | 14.9% (14,370) | 0.59 |
| Scholarship (welfare) recipient | 23.7% (10,861) vs 19.8% | 1.24 |
| Previous no-show earlier in window | 26.9% (14,114) vs 18.8% if previously attended | 1.51 |
| Alcoholism | 20.1% (3,360) | 1.37 (adjusted) |
| Neighbourhoods (≥500 appts) | range 15.7% (Do Cabral) to 28.9% (Santos Dumont) | — |
| Gender, weekday, hypertension | differences ≤1 pp | ≈1.0 |

**[OBS]** No-shows are spread across many patients rather than concentrated in a few:
- 28% of patients missed at least one appointment;
- the 5% of patients with 2 or more no-shows account for 35% of all no-shows.

**[CON]** These are risk markers, useful for targeting. They do not show *why* patients miss appointments.

---

## Recommendations

1. **SMS programme: keep it and expand its reach. Do not cut it.** The apparent harm comes entirely from who gets an SMS. The programme avoids an estimated 700–1,800 no-shows every 6 weeks.
   - **Prevent another outage.** Set up monitoring and alerts when daily SMS volume drops to zero. The 9–20 May outage cost an estimated 300–800 attendances.
   - **Close the ongoing gap.** Find out why about 18% of eligible appointments get no SMS on normal days (missing or invalid phone numbers? opt-outs?) and fix it.
   - **Test before extending.** Run a randomised trial of reminders for 1–2-day bookings (22.7% no-show, currently no SMS), and of a second reminder for long-lead bookings. Randomise by appointment to measure the effect cleanly; this would also settle the 2-vs-6-point uncertainty.
2. **Shorten lead times where possible.** Lead time is the strongest lever. Options:
   - more same-day or next-few-days slots, via open-access scheduling;
   - waitlist and cancellation backfill;
   - asking patients with long-lead appointments to confirm or cancel, so their slots can be re-offered.
3. **Target extra contact at high-risk appointments.** Score each booking on lead time, age 13–30, Scholarship status, previous no-shows and neighbourhood. Then:
   - phone the highest-risk bookings;
   - consider measured overbooking for those slots.
4. **Fix the data so the programme can be managed.** Record:
   - SMS send and delivery logs with timestamps;
   - booking channel (walk-in or scheduled);
   - appointment type and specialty;
   - patient phone availability;
   - a longer history (more than 6 weeks).
   Without these, the size of the SMS effect and the reasons behind it stay partly unresolved.

## Limits

- This is observational data from 6 weeks in one network.
- The SMS effect rests on adjustment plus a 7-day natural experiment, not a randomised trial. Its size is uncertain (2–6 pp), but its direction is consistent across every method.
- Impact figures are counterfactual estimates, not measured losses.
- (The `investigator` root-cause skill was not used. The question is about standing drivers of no-shows, not the cause of a specific change. The SMS outage was handled as a natural experiment within Finding 1.)
