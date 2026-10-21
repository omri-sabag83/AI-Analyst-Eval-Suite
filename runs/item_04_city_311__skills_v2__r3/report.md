# NYC 311 — August 2026 Monthly Briefing

*Source: NYC Open Data "311 Service Requests from 2020 to Present", extracted 2026-09-15. Comparisons: the May–Jul 2026 average month ("recent baseline") and August 2025 ("YoY").*

## Bottom line

1. **Volume was normal.** There were **328,701 requests** in August, about 10,600 a day. That is 4.2% below July (343,085) and 2.4% below the May–Jul monthly average (336,632). Per day it is 3.4% lower. It is **8.1% above August 2025** (304,039). August sits inside the past year's range (302k–349k a month), so no citywide alarm.
2. **The year-over-year growth comes from housing and infrastructure, not policing.** HPD (housing) is up **+15,900 (+40%) YoY** and +9% against the recent baseline. DOT (+35%), DOB (+36%), DEP (+15%) and DPR (+22%) are also up YoY. NYPD, the largest agency, is down 2.8% YoY and 6.2% against the baseline. HPD's growth is broad across housing-condition categories: Unsanitary Condition +35%, Water Leak +75%, Paint/Plaster +39%, Plumbing +40%. **This is the main item that needs attention.**
3. **Three data issues will mislead anyone reading the raw numbers.** A DEP complaint-type rename, an apparent 4-day gap in DHS homeless-assistance intake, and a jump in "Open" status caused by the extract date (details below). Without corrections, they produce false "top movers."

## 1. Data issues to correct before reading any trend

| Issue | What the data shows | Effect if ignored |
|---|---|---|
| **DEP complaint-type rename** | "Water System" (≈10,500/mo in May–Jul) and "Sewer" (≈3,400/mo) drop to **zero** in August. "Water Maintenance" (8,925) and "Sewer Maintenance" (5,060) replace them, with the same descriptors (hydrants, catch basins, backups). The new names already appear in the May–Jul data, so the switch probably started in late July. The same thing happened with "Hazardous Materials"→"Hazardous Material" and "Bike/Roller/Skate Chronic"→"Bike/Roller/Skate". | Water System/Sewer show up as the biggest fallers (−100%) and Water/Sewer Maintenance as the biggest risers (+1,000%). **Both are artefacts.** After mapping old names to new, Water Maintenance is −21% vs baseline / +25% YoY and Sewer Maintenance is +29% / +104%. |
| **Status depends on the extract date** | Non-closed requests make up 12.3% of August (Open 16,884, In Progress 21,899), against 5.9% in May–Jul and 1.9% in Aug 2025. The non-closed share rises steadily through the month: 9.5% for week 1, 15.4% for week 4. | August requests were only 2–6 weeks old when the data was pulled. The comparison periods had months or a year to close. **This is not evidence of a backlog.** Status and closure rates can only be compared at equal age. |
| **DHS "Homeless Person Assistance" intake gap, Aug 7–10** | Normally 100–170 a day. On Aug 7, 8, 9 and 10 it was 2, 2, 2 and 15, across every channel (phone, online, mobile). Encampment requests (also DHS) were unaffected. | About 450–500 requests are probably missing. DHS shows as −12% vs baseline; most of that is this gap, not lower need. |
| Minor | 342 requests (334 of them DEP) have a closed date earlier than the created date. 5,267 non-closed requests carry a closed date. Channel "OTHER" (≈600/mo in May–Jul) disappears. | Small. Exclude these rows from any resolution-time metric. |

## 2. What moved the most (after fixing the renames)

**By agency** (August vs May–Jul monthly average; YoY in brackets)

| Agency | Aug 2026 | vs baseline | vs Aug 2025 |
|---|---:|---:|---:|
| NYPD | 149,901 | −9,850 (−6.2%) | −4,340 (−2.8%) |
| HPD | 56,003 | **+4,690 (+9.1%)** | **+15,930 (+39.7%)** |
| DSNY | 30,220 | +1,900 (+6.7%) | −110 (−0.4%) |
| DOT | 23,395 | −760 (−3.1%) | +6,070 (+35.1%) |
| DEP | 22,233 | −1,320 (−5.6%) | +2,970 (+15.4%) |
| DPR | 15,705 | −3,560 (−18.5%) | +2,800 (+21.7%) |
| DOB | 12,239 | +1,420 (+13.1%) | +3,230 (+35.9%) |
| DHS | 4,188 | −580 (−12.2%)* | −1,900 (−31.2%) |
| EDC | 229 | −450 (−66.5%) | −1,610 (−87.6%) |

*mostly the Aug 7–10 intake gap.

**Complaint types: biggest risers vs the recent baseline.** Unsanitary Condition +2,670 (+22%), Water Leak +1,860 (+52%), Paint/Plaster +1,200 (+22%), Sewer Maintenance +1,120 (+29%), Building/Use +930 (+39%), Dirty Condition +760, Street Light Condition +680 (+22%), Obstruction +630 (+30%), Rodent +510 (+19%).

**Biggest fallers vs the recent baseline.** Most are seasonal or event-driven, not a signal: Noise – Residential −3,140 (−9%), Illegal Parking −2,830 (−5%), Illegal Fireworks −2,540 (−83%, the July 4 peak), HEAT/HOT WATER −2,500 (−40%, early-May heating carry-over), Water Maintenance −2,320, Damaged Tree −1,860 (−28%, likely storm damage in the baseline months), Street Condition −1,370.

**Biggest YoY movers.** Risers: Street Condition +3,960 (+71%), Illegal Parking +3,970 (+8%), Unsanitary Condition +3,810, Sewer Maintenance +2,580, Water Leak +2,360, Plumbing +1,920, Paint/Plaster +1,840. Fallers: **Drug Activity −4,500 (−83%)**, Noise – Helicopter −1,610 (−88%), Lead −1,280 (−46%), Homeless Person Assistance −1,250 (−27%), Traffic −1,150 (−71%).

By borough, Brooklyn has most of the YoY growth: +15,600 (+17.7%), against +0.6% for Queens and +4–8% elsewhere. All boroughs are 1–4% below the recent baseline, in line with the citywide dip.

## 3. What is unusual and needs attention

1. **Housing-condition complaints are growing fast, and the growth persists.** HPD is up 40% YoY and still rising against an already-high summer baseline (+9%). Water Leak (+52% vs baseline) and Unsanitary Condition (+22%) lead. HPD complaints come mostly from Brooklyn (31%) and the Bronx (31%). HPD also has the longest median time-to-close of any agency, about 219 hours (≈9 days) for August requests already closed, so more volume puts pressure on responsiveness.
2. **Hydrant surge, Aug 6–14.** Fire-hydrant requests ran at 300–550 a day on Aug 6–10, against about 130–180 normally, roughly 1,700 extra. In the same window every hydrant request was coded "Fire Hydrant Emergency"; the usual descriptors (Running, Running Full, Leaking) went to zero. Two things are happening at once: a real volume surge (probably a heat event with open hydrants; not confirmed here) and a temporary change in how descriptors were coded.
3. **Storm-type spikes.** Sewer Maintenance (Backup / Catch Basin / Street Flooding) and HPD Water Leak spiked together on **Aug 3, 20, 21, 23 and 27**, at 2–4× normal daily levels. This looks like rainfall events (hypothesis; not tested against weather data). It explains part of the Sewer and Water Leak rise.
4. **Possible reporting breaks rather than real declines.** Drug Activity was already about 850/mo in May–Jul, against 5,447 in Aug 2025, so this is a standing change from before this summer, not an August event. It is most likely a routing or category change. Noise – Helicopter (EDC) is down 88% YoY, and all 229 August requests are still "In Progress". Traffic is down 71% YoY. Before anyone reports these as improvements, they need confirmation that they are not intake or category changes.

## 4. Recommendations: what to investigate next

1. **HPD growth (highest priority).** Break HPD requests down by building, community board and complaint type for the last 12 months. Is this a broad rise or a concentration in particular buildings and landlords (possibly repeat filers or a few large portfolios)? Also check whether HPD added an intake channel or changed its process; 58% of HPD requests come in online. Track HPD time-to-close at equal request age.
2. **Ask DHS / 311 operations about Aug 7–10.** Confirm whether Homeless Person Assistance intake was down or routed elsewhere, and whether those requests can be recovered.
3. **Ask DEP about the taxonomy change and the hydrant coding.** Confirm the exact cut-over date for Water System→Water Maintenance and Sewer→Sewer Maintenance, and publish a crosswalk. Confirm whether the Aug 6–11 "Fire Hydrant Emergency" coding was a deliberate emergency protocol.
4. **Confirm the Drug Activity, Noise – Helicopter and Traffic drops** with NYPD and EDC (routing or category changes, or real declines?).
5. **Fix the reporting method.** (a) Keep a complaint-type crosswalk in the monthly pipeline so renames don't show up as movers. (b) Measure closure and backlog at a fixed request age (e.g., share closed within 14 days) instead of current status. (c) Re-pull August after 60+ days for a fair closure comparison. (d) Add a per-category daily-volume monitor to catch intake gaps like DHS's within a day or two.

## Assumptions and limitations
- The recent baseline is May–Jul 2026 divided by 3 (92 days). Per-day it is 10,977 requests a day, against 10,603 in August. Some of the baseline mix is seasonal (fireworks, early-May heat).
- Only one August-2025 snapshot is available, and baseline data is aggregated, so changes in earlier months cannot be traced day by day. Cross-dimension breakdowns (e.g., HPD by borough) can only be computed for August 2026.
- Causes such as weather, heat events or process changes are hypotheses consistent with the data. The data used here does not verify them.
- Time-to-close figures cover only requests closed by 2026-09-15, so they understate true resolution times for slow agencies.
