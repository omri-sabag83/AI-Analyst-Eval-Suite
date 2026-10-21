# Appointment no-shows: what drives them, and what to do about SMS reminders

**Data:** `appointments.csv`, 110,527 appointments for 62,299 patients. Appointments fall between 29 Apr and 8 Jun 2016 (27 clinic days). 22,319 of them (20.2%) were no-shows.

## Bottom line

1. **Keep the SMS reminder programme, and expand it.** In the raw data, patients who got an SMS look *worse* (27.6% no-show against 16.7% for those who didn't). That comparison is misleading, because SMS is only sent for appointments booked 3 or more days ahead, and those carry the highest risk. A cleaner test comes from a 7-day period when no reminders went out at all. During that period, no-shows rose by **about 4 percentage points** among appointments that would normally have got an SMS. Among appointments that never get an SMS, the no-show rate did not move. My estimate is that each reminder actually delivered prevents roughly **5 no-shows per 100 messages**. Across the network that is about 85–90 fewer missed appointments per clinic day.
2. **The biggest driver of no-shows is how far ahead the appointment was booked.** Same-day appointments are 35% of the volume but have only a 4.6% no-show rate. Appointments booked a month or more ahead have a rate of about 33–34%. Appointments booked 3 or more days ahead account for 80% of all no-shows.
3. **Secondary drivers:** age (teenagers and young adults are worst, over-55s best), having missed an earlier appointment, being on the Scholarship (welfare) programme, and neighbourhood.

## 1. The SMS programme

### Why the simple comparison is wrong
| Booking lead time | Share sent an SMS | No-show rate |
|---|---|---|
| Same day | 0% | 4.6% |
| 1 day | 0% | 21.4% |
| 2–3 days | 10% | 23.7% |
| 4–7 days | 61% | 25.2% |
| 8–14 days | 58% | 30.5% |
| 15–30 days | 61% | 32.6% |
| 31–60 days | 61% | 34.2% |

The rule for who gets an SMS is visible in the data: nobody booked 0–2 days ahead receives one. The no-SMS group is therefore made up largely of same-day and next-day bookings, which are low risk. That is the only reason SMS looks harmful in the raw totals. **Within every lead-time band, patients who received an SMS missed fewer appointments**, by 3 to 12 points. Even so, comparisons within a band could still be biased, because something decided which eligible patients got a message. So I relied on the test below.

### The natural experiment: a 7-day reminder outage
On 9 May and 13–20 May, **not a single SMS was sent**. On normal days, 82% of appointments booked 3 or more days ahead got one. I'm assuming this was a system outage or a pause in the programme; the data does not record the reason. During those days, patient mix was unchanged: mean age was 37.2 vs 37.7, Scholarship 9.5% vs 9.6%, hypertension 19.4% vs 19.8%, and median lead time 13 days vs 14.

| Group | Normal days | Outage days | Change |
|---|---|---|---|
| Appointments booked ≥3 days ahead (normally get an SMS) | 28.6% (n=43,437) | 32.5% (n=16,584) | **+4.0 pts** |
| Appointments booked 0–2 days ahead (never get an SMS) | 8.93% (n=37,127) | 8.93% (n=13,379) | 0.0 pts |

- The control group stayed flat. That rules out the outage days simply being "bad days" for attendance.
- In a difference-in-differences regression, controlling for lead-time band and weekday with standard errors clustered by day, the effect is **+4.1 pts (95% CI about 2.4–5.8)**. Restricting to eligible appointments and also controlling for age and Scholarship gives **+4.0 pts (CI about 2.8–5.2)**.
- The increase showed up in every lead-time band: +1.9 pts for 3–7 days, and +5 to +6 pts for 8 days or more.
- **Per message:** losing reminders for the 82% who normally get one raised no-shows by 4.0 pts. That implies roughly **4.9 pts per delivered SMS** (about 3.4–6.4), a ~15% relative reduction. At normal volumes (~2,170 eligible appointments per clinic day), the programme prevents about **87 no-shows per clinic day** across the network.

**Recommendation on SMS: keep it, and expand it.** The case for expanding is an estimate, not something tested directly:
- **Close the coverage gap.** About 18% of eligible appointments still get no SMS on normal days, and coverage is lowest for patients aged 65+ (75%) and children (79%). Check why: missing or invalid phone numbers, or opt-outs.
- **Extend to bookings made 1–2 days ahead.** These 11,938 appointments currently get no SMS and have a 22.7% no-show rate, close to the eligible group's. Whether reminders work at short lead times is **untested**; the outage effect was smallest in the 3–7-day band. Roll this out as a randomised pilot (for example, by alternating days or clinics) rather than network-wide.
- **Make sure outages can't happen silently.** A 7-day gap went unnoticed in the data, and it cost an estimated ~600 extra no-shows. Set up an alert for any day with zero reminders sent.

## 2. What drives no-shows

These are odds ratios from a logistic regression with all factors fitted together. The model ranks risk moderately well (AUC 0.73).

| Factor | Raw no-show rate | Adjusted odds ratio |
|---|---|---|
| **Lead time** (vs same day) | 4.6% → 21–34% | 6.7× (1–2 days) up to 12–13× (15+ days) |
| **Age** (vs 0–5) | 13–18: 26.1%, 19–25: 25.4%; 65+: 15.5% | 13–18: 1.48; 65+: 0.62 |
| **Missed an earlier appointment in this window** | 26.9% vs 18.8–19.4% | 1.51 |
| **Scholarship (welfare) enrolment** | 23.7% vs 19.8% | 1.24 |
| Alcoholism | 20.1% vs 20.2% | 1.37 (only once age and lead time are accounted for) |
| Neighbourhood (≥500 appointments) | 15.7% to 28.9% | not modelled; e.g. Santos Dumont 28.9%, Itararé 26.3% |
| Gender, hypertension, disability | small differences | ~1.0–1.06, not material |

Risk is concentrated. The riskiest 10% of appointments by model score have a 41% no-show rate. The safest 30% have 3–5%.

## 3. Recommendations to reduce no-shows

1. **Shorten booking lead times where possible.** Lead time is the strongest driver. Options include open or same-week scheduling, and releasing slots closer to the date instead of booking weeks ahead. *Caveat:* part of the lead-time effect may reflect the type of visit (urgent walk-in vs routine follow-up), which the data doesn't record. The effect of shortening lead times should be tested, not assumed.
2. **Keep and expand SMS** as described above. It is the one lever with near-causal evidence behind it.
3. **Target extra contact at high-risk appointments.** These are long lead times, ages 12–35, patients who have missed before, Scholarship patients, and the worst neighbourhoods. Options are a second reminder or a phone call 1–2 days before the appointment, and a simple way to confirm or cancel so the slot can be offered to someone else.
4. **Use the risk score for slot management.** The model separates 3% from 41% risk groups, so it can support targeted overbooking or waitlist backfill for high-risk slots.
5. **Measure as you go.** Run the reminder expansions and outreach as randomised pilots so their effect can be measured directly.

## Assumptions and data notes
- I measured lead time in calendar days, from the booking date to the appointment date. `AppointmentDay` has no time-of-day.
- I excluded 5 appointments with appointment dates before the booking date, and 1 with age −1. Ages above 100 (7 rows) were kept.
- "Missed an earlier appointment" uses only appointments within this 6-week window. True history is longer, so the effect is probably understated.
- I am treating the zero-SMS days as an operational outage that had nothing to do with patient behaviour. Balanced patient mix and a flat control group support this, but I cannot confirm the reason. The per-message estimate (~5 pts) assumes the outage affected only people who would otherwise have received an SMS.
- Data covers one city network over about 6 weeks in 2016. There is no information on visit type, specialty or cost, so I could not calculate the programme's return on investment. To do that, compare the cost per SMS against the value of ~0.05 avoided no-shows per message.
- Associations other than SMS (age, Scholarship, neighbourhood) are correlations, not proven causes.
