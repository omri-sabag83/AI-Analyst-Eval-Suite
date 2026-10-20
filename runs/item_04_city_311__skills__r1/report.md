# NYC 311: August 2026 Monthly Briefing

*Data: NYC Open Data, "311 Service Requests from 2020 to Present", extracted 2026-09-15. August 2026 = 328,701 requests created 1–31 Aug. Comparisons: **"vs. baseline"** = August against the May–July 2026 monthly average; **"YoY"** = August 2026 against August 2025.*

## Summary

1. **Total volume was normal.** August had 328,701 requests. That is 4.2% below July (343,085) and 2.4% below the May–July average (336,632). It is 8.1% above August 2025 (304,039) and in the middle of the 12-month range (302k–349k). No single day stood out: daily counts ran from 9.2k to 11.7k, with the usual weekend dips.
2. **Housing complaints (HPD) are the biggest real increase and need attention.** HPD received 56,003 requests, **+9% vs. baseline and +40% YoY (+15.9k)**. Excluding seasonal heat/hot-water complaints, HPD was **+16% vs. baseline and +41% YoY**. The rise covers almost every HPD category: Unsanitary Condition +22% (+2.7k), Water Leak +52% (+1.9k), Paint/Plaster +22% (+1.2k), General +16%, Appliance +16%.
3. **Two of the biggest "movers" are a relabelling, not real change.** "Water System" and "Sewer" (about 13.9k a month in May–July) fell to **zero**. At the same time "Water Maintenance" and "Sewer Maintenance" rose from about 1.3k to 14.0k. Combined, water and sewer requests were **−8% vs. baseline** (15,180 → 13,985). Any dashboard or trend line keyed on the old names will break.
4. **The jump in open requests is mostly an artefact of timing.** 12.3% of August requests are not closed, against about 6% for May–July: "Open" is up 260% and "In Progress" up 68%. August requests had at most 6 weeks to close before the extract, while baseline requests had 1.5–3.5 months. The open share also rises steadily with creation week (9.5% in week 1 → 15% in week 4), which is what you'd expect when recent requests haven't had time to close. **Do not report this as a backlog yet** (see "Investigate next").
5. **The NYPD decline is mostly seasonal.** NYPD fell 6% vs. baseline (−9.8k). The main contributors were Illegal Fireworks (−2.5k, after the July 4th peak), Noise – Residential (−3.1k) and Illegal Parking (−2.8k). NYPD is −3% YoY.

## What changed: agencies

| Agency | Aug 2026 | vs. May–Jul avg | YoY | Note |
|---|---:|---:|---:|---|
| NYPD | 149,901 | −6% | −3% | Seasonal: fireworks and noise down |
| **HPD** | 56,003 | **+9%** | **+40%** | Broad increase in housing-condition complaints |
| DSNY | 30,220 | +7% | 0% | Dirty Condition +12%, Illegal Dumping +11%, Missed Collection +9% |
| DOT | 23,395 | −3% | +35% | Street Condition +71% YoY; Street Light Condition +22% vs. baseline |
| DEP | 22,233 | −6% | +15% | Water/sewer relabel (see above) |
| DPR | 15,705 | **−18%** | +22% | Fewer storm-related tree complaints than in early summer |
| **DOB** | 12,239 | **+13%** | **+36%** | Building/Use +39% vs. baseline, Elevator +8% |
| DHS | 4,188 | −12% | −31% | Homeless Person Assistance −27% YoY |
| EDC | 229 | **−67%** | −88% | Helicopter noise; all 229 still open |

## What changed: complaint types (largest real moves vs. May–July)

- **Up:** Unsanitary Condition +2,672 (+22%); Water Leak +1,863 (+52%); Paint/Plaster +1,195 (+22%); Building/Use +928 (+39%); Dirty Condition +759 (+12%); Street Light Condition +677 (+22%); Obstruction +627 (+30%); Rodent +513 (+19%).
- **Down:** Noise – Residential −3,137 (−9%); Illegal Parking −2,832 (−5%); Illegal Fireworks −2,537 (−83%, seasonal); Heat/Hot Water −2,499 (−40%, seasonal); Damaged Tree −1,857 (−28%); Street Condition −1,373 (−13%).
- **Large YoY gaps that were already there before August** (the May–July level matches August): Drug Activity −83% YoY (5,447 → 947) but +11% vs. baseline; Street Condition +71% YoY; Noise – Helicopter −88% YoY. These step changes happened between Aug 2025 and May 2026. They are not August events, but they are large enough that someone should confirm whether they are real or caused by reporting or classification changes.

## Channel and geography

- **Channel:** Online requests were +5% vs. baseline and +22% YoY. Phone was −9% and −11%, mobile −11% and −7%. Part of the mobile drop comes from the mix: NYPD is 82% of mobile traffic, and NYPD volume fell. HPD intake is 58% online and 41% phone.
- **Borough:** Every borough was flat or slightly down vs. baseline (−1% to −4%). YoY, **Brooklyn is +18% (+15.6k)**, while Queens is +1% and the other boroughs +4% to +8%. Brooklyn's YoY gain is about the same size as HPD's YoY gain (+15.9k), and Brooklyn is HPD's largest borough (17.5k in August). That is a coincidence of totals, not a proven link, because the baseline file has no borough × agency breakdown.

## Data-quality notes and assumptions

- Requests are counted by creation date. Counts for August should be close to complete by 15 Sep, but status and closure fields are **not** comparable with older periods because of the different time each had to close.
- Taxonomy changes found: Water System → Water Maintenance, Sewer → Sewer Maintenance, and probably Hazardous Materials → Hazardous Material (203/mo → 0 and 0 → 229). OOS is a new agency code (390 requests; none in Aug 2025).
- The baseline is the May–July average, so it carries early-summer seasonality (fireworks, storms). YoY is the better seasonal comparison but mixes in a year of structural change. I report both.
- I attributed complaint types to agencies using the agency that handles each type in August.

## Recommendations / investigate next

1. **HPD increase (highest priority).** Complaints were +40% YoY across nearly all categories. Check whether this is real (housing conditions, summer leaks or pests) or comes from how complaints are taken in (for example a new online form, a campaign, or a change in duplicate handling). Pull HPD by borough, channel and month for the last 13 months, plus the duplicate/unique-building rate. Also check HPD closure capacity: 32% of last-week HPD requests are still open.
2. **Backlog check done properly.** Compare open shares at the same age, e.g. the share still open 14 and 30 days after creation for August vs. May–July. This needs a request-level extract for earlier months. Flag agencies with high open rates for August requests as a whole: TLC 82%, DPR 57%, DOHMH 45%, DCWP 43%, DOB 36%. EDC helicopter complaints are 100% open, which suggests they may not be being worked through 311 at all.
3. **Update reporting for the DEP relabel.** Map the old and new water/sewer names together in every dashboard and in KPI definitions. Confirm the exact cut-over date (it appears to be during July 2026).
4. **Explain the YoY step changes.** Find out why Drug Activity (−83%), Helicopter noise (−88%), DHS Homeless Assistance (−27%) and DOT Street Condition (+71%) shifted between Aug 2025 and May 2026.
5. **DOB Building/Use (+39% vs. baseline).** Check whether this is concentrated in particular community boards (possible illegal-conversion or occupancy issues).
