# NYC 311 — August 2026 Monthly Briefing

*Data: NYC Open Data "311 Service Requests from 2020 to Present", extracted 2026-09-15. August 2026 = 328,701 requests (row-level file). Comparisons: August 2025 (year-over-year) and May–July 2026 (recent baseline, scaled to a 31-day month: baseline × 31/92).*

## Bottom line

1. **Volume was normal.** 328,701 requests (~10,600/day): 4.2% below July and 3.4% below the May–July daily rate, which fits the usual late-summer dip. It is **8.1% above August 2025** (+24,700).
2. **Most of the year-over-year growth is housing (HPD).** HPD requests rose **+40% YoY** (40,078 → 56,003, +15,900), about two-thirds of the city's net growth. They are also up 8% on the recent baseline, so the growth is still going on. Unsanitary-condition and leak complaints lead it: Unsanitary Condition +3,808, Water Leak +2,356, Plumbing +1,919, Paint/Plaster +1,839, General +1,795. HPD is also the slowest agency to close requests (median 9 days) and has 21% of August requests still open. **This is the item that most needs management attention.**
3. **The largest month-on-month "movers" are mostly artefacts, not real change.** DEP renamed categories (Sewer → Sewer Maintenance, Water System → Water Maintenance). The data were pulled only 2–6 weeks after the requests were created, which inflates the open/in-progress counts. Weather and holidays explain most of the other swings. Do not read these as service problems (details below).
4. **Two short-lived events should be checked:** a heat-related surge in fire-hydrant complaints on Aug 6–11, and storm-related sewer/flooding spikes (Aug 3, 20–21, 23, 27). There is also one cluster that looks like a campaign or duplicates: 136 Animal-Abuse reports from ZIP 11210 on Aug 19–20.

## 1. What happened in August

| Metric | Aug 2026 | vs May–Jul avg month | vs Aug 2025 |
|---|---|---|---|
| Total requests | 328,701 | −3.4% (per day) | +8.1% |
| NYPD | 149,901 (46%) | −7.2% | −2.8% |
| HPD | 56,003 (17%) | +8.0% | **+39.7%** |
| DSNY | 30,220 | +5.5% | −0.4% |
| DOT | 23,395 | −4.2% | **+35.1%** |
| DEP | 22,233 | −6.6% | +15.4% |
| DPR | 15,705 | −19.4% | +21.7% |
| DOB | 12,239 | +11.9% | **+35.9%** |
| DHS | 4,188 | −13.2% | **−31.2%** |
| EDC | 229 | −66.9% | **−87.6%** |

Top complaints: Illegal Parking (51,216), Noise – Residential (30,622), Noise – Street/Sidewalk (23,644), Blocked Driveway (14,636), Unsanitary Condition (14,650).

The daily volume was steady, between 9,250 and 11,670 a day, with the usual weekday highs and weekend lows. There were no outage-like gaps and no duplicate request IDs.

## 2. What changed, and why

### Real changes
- **HPD housing conditions (YoY +40%, vs baseline +8%).** Growth is spread across the main housing-maintenance categories: Water Leak +75% YoY and +50% vs baseline; Unsanitary Condition +35% / +21%; Paint/Plaster +39% / +21%; Plumbing +40% YoY. Bronx and Brooklyn account for 62% of August HPD volume. The data cannot tell us whether this reflects worse conditions, more reporting (for example online outreach), or a change in how HPD intake works. Any of these has resourcing consequences.
- **DOT Street Condition (+71% YoY, 9,552)** and **DOB Building/Use (+63% YoY, +37% vs baseline)** are real increases worth tracking. Street Light Condition (+21%) and Obstruction (+28%) are also up against the baseline.
- **Online is replacing phone and app.** ONLINE +22% YoY and +4% vs baseline. PHONE −11% and MOBILE −12% vs baseline. Online is now 51% of intake.
- **Brooklyn is +17.7% YoY** while Queens is flat (+0.6%). Brooklyn's share was 29.0% in Aug 2025 and 31.6% now, but it was already 31.3% in May–July. This is a shift that happened earlier, not something new in August.

### Seasonal or event-driven (expected)
- Illegal Fireworks −83% and Noise – Residential −10% vs baseline (post-July 4 and early-summer peaks fading). Both are about flat YoY.
- HEAT/HOT WATER −41% vs baseline (the May baseline includes the end of heating season). It is up 26% YoY, consistent with HPD's general growth.
- Damaged Tree −29% vs baseline (storm-driven in early summer), but still +46% YoY.
- **Hydrant surge Aug 6–11:** fire-hydrant descriptors averaged ~430/day, against ~155/day for the rest of the month. That pattern fits a heat wave with hydrants opened illegally.
- **Sewer spikes:** Sewer Maintenance jumped from ~100/day to 411–521/day on Aug 3, 20, 21, 23 and 27, mainly Backups, Clogged Catch Basins and Street Flooding. That pattern fits rain events.

### Artefacts (do not interpret as performance)
- **DEP category rename.** "Sewer" and "Water System" do not appear in August. "Sewer Maintenance" and "Water Maintenance" replace them (they show only a small presence in the baseline, so the switch happened around late July). Taken at face value they look like +896% and +1,049% movers. Combined like-for-like: sewer is +27% vs baseline and +104% YoY (storms); water is −21% vs baseline and +25% YoY. Any trend reporting on these categories needs a crosswalk.
- **Open/In-Progress status counts are not a backlog signal yet.** Open went from 245 (Aug 2025) to 16,884, and In Progress from 4,734 to 21,899. However, the August requests were only 2–6 weeks old when extracted, while Aug 2025 requests had a year to close. The open share rises with recency: 9.5% of week-1 requests are still open versus 15% of week-4 requests. HPD (21% open), DOB (36%), DPR (57% in progress) and TLC (82% in progress) hold most of it. A real backlog comparison needs snapshots taken at the same age.
- **EDC / Noise – Helicopter (−88% YoY, −67% vs baseline)** and **Drug Activity (−83% YoY but flat vs baseline)**. Changes this sharp usually come from routing or category changes, not from public behaviour. The Drug Activity drop happened before May 2026. **DHS Homeless Person Assistance** is −27% YoY and flat vs baseline. Lead (DEP) is −46% YoY. DOE requests are absent this year, and an "OOS" agency appears (390).
- **Data quality:** 342 records (334 DEP) have a closed time a few seconds *before* the created time. This is a timestamp artefact and immaterial to volumes. 10.7% of records have no closed date (open items).

## 3. What needs attention

1. **HPD demand and capacity.** Volume is +40% YoY, the median time to close is about 9 days (219 h), and 11,700 August requests were still open in mid-September. This is the most consequential trend for residents.
2. **Animal-Abuse cluster, ZIP 11210 (Brooklyn):** 111 reports on Aug 19 and 25 on Aug 20, against a background of about 1 a day. They were almost all filed online in the late afternoon, and most have the descriptor "Other". It could be a real incident or a coordinated or duplicate submission. Check before it distorts the DOHMH/NYPD figures.
3. **Graffiti on Aug 10 and 12** (184 and 181, against ~40/day) came almost entirely through the "UNKNOWN" channel and were concentrated in 11216, 10009 and 10002. This looks like a bulk entry or proactive sweep, not resident demand.

## 4. Recommended next steps

1. **Break down HPD growth:** by building and complainant (repeat callers or buildings), by channel, and by community district. Compare the open share against Aug 2025 *at the same age* to see whether resolution is falling behind.
2. **Set up a category crosswalk** for the DEP rename (and confirm the go-live date with DEP). Apply it to all trend dashboards.
3. **Produce status/backlog metrics at a fixed age** (e.g., % closed within 14 or 30 days) instead of raw status counts from a snapshot.
4. **Confirm the routing changes** behind EDC/Helicopter, Drug Activity, DHS and Lead with the agencies, so real declines can be separated from administrative ones.
5. **Validate the 11210 Animal-Abuse and the Aug 10/12 graffiti clusters** for duplicates or bulk entries.
6. **Watch DOT Street Condition and DOB Building/Use**, which are growing year over year.

## Assumptions and limitations
- Baseline monthly figures = May–July total × 31/92. The breakdown file has no cross-tabulations for prior periods, so borough × agency or complaint drill-downs exist only for August 2026.
- Explanations involving heat and rain are inferred from the complaint patterns. No weather data was available.
- Resolution-time figures cover only August requests closed by 2026-09-15, so they understate the true times for slow agencies.
