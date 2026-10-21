# NYC 311 — August 2026 Monthly Briefing

*Source: NYC Open Data "311 Service Requests from 2020 to Present", pulled 2026-09-15. Comparisons: May–Jul 2026 ("recent baseline"; scaled to a 31-day month by dividing by 92 days and multiplying by 31) and August 2025 ("year-over-year", YoY).*

## Bottom line

1. **August was a normal-volume month.** There were **328,701 requests**, about 10,600 a day. That is 3.4% below the May–Jul daily rate, 4.2% below July, and level with the 12-month average (328,600). Daily volume stayed between 9,250 and 11,670 with no spike or outage.
2. **The real story is year-over-year growth driven by housing complaints.** Volume was **8.1% higher than August 2025 (+24,700)**. HPD (housing) accounts for **+15,900 of that, about 64%**. HPD requests rose 40% YoY and 8% above the summer baseline, even though heat complaints are seasonally low. Mold, pests, leaks, paint and plumbing are all up 35–75% YoY.
3. **Three things in the data could mislead a reader, and should be read correctly:**
   - **DEP renamed its main complaint codes.** "Water System" and "Sewer" have been replaced by "Water Maintenance" and "Sewer Maintenance". On a naive complaint-type ranking these show up as the biggest risers (+8,900 and +5,100) and fallers (−10,600 and −3,500). They are a relabel, not a real change.
   - **The "open" backlog looks like it exploded, but this is mostly an artefact of when the data was pulled.** August requests had only 15–45 days to close before the pull, whereas August 2025 had a full year.
   - **Helicopter-noise complaints (EDC) collapsed, and none of the August ones have been closed.** This looks like a routing or intake problem rather than a real fall in noise.

## 1. What happened in August

| Measure | Aug 2026 | vs May–Jul (per 31 days) | vs Aug 2025 |
|---|---|---|---|
| Total requests | 328,701 | −3.4% | **+8.1%** (+24,662) |
| NYPD | 149,901 (46%) | −7.2% | −2.8% |
| HPD | 56,003 (17%) | +8.0% | **+39.7%** (+15,925) |
| DSNY | 30,220 | +5.5% | −0.4% |
| DOT | 23,395 | −4.2% | **+35.1%** (+6,074) |
| DEP | 22,233 | −6.6% | +15.4% |
| DPR | 15,705 | −19.4% | +21.7% |
| DOB | 12,239 | +11.9% | **+35.9%** |
| DHS | 4,188 | −13.2% | **−31.2%** |
| EDC | 229 | **−66.9%** | **−87.6%** |

Top complaint types: Illegal Parking (51,216), Noise – Residential (30,622), Noise – Street/Sidewalk (23,644), Unsanitary Condition (14,650), Blocked Driveway (14,636).

By borough, Brooklyn grew most YoY (+17.7%, +15,600) and Queens was flat (+0.6%). Compared with the summer baseline, every borough was 2–5% lower. About 62% of HPD's housing-condition complaints come from Brooklyn and the Bronx, which fits Brooklyn's YoY growth. However, the baseline files only have one-way breakdowns, so I cannot break borough growth down by agency.

## 2. What changed, and why it matters

### A. Housing-condition complaints are rising sharply (the main finding)
- HPD excluding HEAT/HOT WATER: **52,321 in August**, up **+14.7% on the summer rate** and **+40.8% YoY**.
- Complaint types driving it (Aug 2026 vs Aug 2025): Unsanitary Condition 14,650 vs 10,842 (+35%; mostly pests 7,901 and mold 4,107), Water Leak 5,481 vs 3,125 (+75%; +50% vs summer), Plumbing +40%, Paint/Plaster +39%, General +67%, Door/Window +34%.
- DOB (buildings) is also up 36% YoY, and Building/Use complaints are up 63%.
- *Interpretation (hypothesis, not proven):* the rise is broad across many housing-condition codes rather than one code. That makes a pure recoding artefact unlikely. Possible causes are worsening conditions, an outreach or awareness campaign, or easier online filing: HPD gets 58% of its requests online, and online filing citywide rose 22% YoY. The data here cannot tell these apart.

### B. Street and infrastructure complaints are up YoY
- DOT Street Condition: 9,552 vs 5,590 (+71% YoY), though 13.5% below the summer rate. Street Light Condition and Traffic Signal Condition are both up 20–30% YoY.
- DEP water and sewer, with old and new codes combined: **13,985 in August vs 9,608 in Aug 2025 (+46%)**, and 9% below the summer rate. The largest items are fire-hydrant complaints (about 5,900, a typical summer pattern), clogged catch basins and sewer backups.

### C. Declines worth noting
- **DHS −31% YoY.** Homeless Person Assistance fell from 4,646 to 3,396 but is flat against the summer baseline, so the drop happened before May. Encampment is flat at about 4,990.
- **NYPD Drug Activity −83% YoY** (5,447 → 947) and **Traffic −71% YoY** (1,619 → 474). Drug Activity is flat against the summer baseline, so the step change came before May. Traffic is still falling (−33% vs summer). Sudden drops of this size usually mean a routing or category change, not a real change in behaviour.
- **Lead (DEP) −46% YoY**, but +26% vs summer.
- Seasonal effects that are expected and need no action: Illegal Fireworks −83% vs the July-heavy baseline, HEAT/HOT WATER −41%, residential and commercial noise −10 to −14%, tree damage (DPR) −29% vs summer.

### D. Channel mix is moving online
Online filing was **+22% YoY** (now 51% of all requests). Phone was −11% and the mobile app −6.5%. Against the summer baseline, phone (−10%) and mobile (−12%) fell faster than total volume. The small "OTHER" channel (about 600 a month in the baseline) recorded zero in August, which suggests a channel-coding change.

## 3. Unusual items needing attention

1. **Complaint-code changes are distorting comparisons.** DEP retired "Water System" and "Sewer" and introduced "Water Maintenance" and "Sewer Maintenance". The new codes already appear in a small way in the May–Jul baseline (777 and 508 per month), so the switch happened partway through that period. "Hazardous Materials" also became "Hazardous Material". **Any dashboard ranking movers by complaint type will currently show false top movers.** A mapping between old and new codes is needed.
2. **Helicopter noise (EDC): volume fell, and nothing is being closed.** There were 229 requests, against about 690 a month in the summer baseline and 1,842 in Aug 2025. **None of the 229 has a close date.** At the pull date the oldest had been open for 45 days. Every other agency has closed at least some of its August requests. Either intake or routing changed (for example, complaints going to the FAA or another portal), or the cases are not being worked.
3. **Apparent backlog is mainly censoring.** In August, 12.3% of requests were not yet closed, against 1.9% in the Aug 2025 snapshot and 5.9% in May–Jul. "Open" status is 16,884 against 245 a year ago. However, the not-closed share rises steadily with creation date: 9.5% for requests created 1–7 Aug, 15.4% for 22–28 Aug. That is the signature of requests that simply haven't had time to close yet, not of a backlog. **Do not report these status shifts as a deterioration until like-for-like ages are compared.** Agencies with high unclosed shares worth watching: TLC 82%, DPR 57%, DOHMH 45%, DCWP 43%, DOB 36%, HPD 21% (11,673 HPD requests in "Open").
4. **Minor data-quality items:** 342 records (0.1%) have a close date earlier than their create date. 1.9% lack coordinates and 2.4% lack a council district. 367 have borough "Unspecified" (+83% YoY, but still tiny). None of these affect the conclusions.

## 4. Recommended next steps

1. **HPD surge (highest priority).** Pull monthly HPD counts by complaint type and borough for Sep 2025–Aug 2026 to see when the rise began. Check it against any HPD outreach campaign, online-form changes, or 311 routing changes. If the rise is real, check whether HPD inspection capacity is keeping pace: HPD's median time to close is already about 9 days.
2. **EDC helicopter complaints.** Ask EDC and the 311 operations team whether intake or routing changed, and why no August case has been closed.
3. **Code crosswalk.** Get the effective dates for the DEP code changes (and any NYPD category changes behind the Drug Activity and Traffic drops) and apply a mapping in monthly reporting.
4. **Fair backlog metric.** Report "share closed within N days of creation" (for example 7 or 14 days) rather than status at the pull date, so that months can be compared fairly.
5. **DHS homelessness requests.** Confirm whether the YoY decline reflects a routing change (for example to 911 or outreach teams) or real demand.

## Assumptions and limitations
- The May–Jul baseline is pooled. I put it on the same footing as August by daily rate (92 days → 31). Aug 2025 has the same number of days as Aug 2026.
- I assume the Aug 2025 and May–Jul figures come from the same 2026-09-15 pull, which makes them much more mature than August 2026. That is why status comparisons are not like-for-like.
- The baselines are one-way breakdowns only (by type, borough, agency, channel or status), so I cannot measure cross-effects, such as HPD growth by borough, against the past. Findings about causes above are hypotheses to test.
- Only 12 monthly totals are available, so YoY seasonality is judged from a single prior August.
