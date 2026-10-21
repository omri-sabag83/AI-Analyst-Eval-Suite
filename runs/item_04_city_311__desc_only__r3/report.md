# NYC 311 — August 2026 Monthly Briefing

*Data: NYC Open Data "311 Service Requests from 2020 to Present", pulled 2026-09-15. Comparisons: July 2026, the May–July 2026 average (converted to a 31-day month: count ÷ 92 days × 31), and August 2025 (year over year, "YoY").*

## Summary

1. **Volume was normal.** There were **328,701 requests** in August, 4.2% fewer than July (343,085) and 3.4% fewer per day than May–July. That is **+8.1% YoY** (304,039), and within the past 12 months' range of 302k–349k. Nothing city-wide looks wrong.
2. **The biggest "movers" on a raw table are a DEP relabelling, not real change.** "Water System" (10.6k/month in May–July) and "Sewer" (3.5k/month) **dropped to zero** in August. At the same time "Water Maintenance" (8,925) and "Sewer Maintenance" (5,060) appeared with the same descriptors. Once the old and new names are added together, the real picture is: **water down 21%** vs May–July (+25% YoY) and **sewer up 27%** (+104% YoY). Any dashboard or trend line keyed on complaint type will be wrong until the names are mapped.
3. **Weather-type events drove DEP volume.** Sewer/flooding complaints spiked on **Aug 3, 20, 21, 23 and 27**. Those 5 days held 43% of the month's sewer complaints, and Queens and Brooklyn accounted for 80% of them. Fire-hydrant complaints roughly tripled on **Aug 6–11** (340–552/day vs ~120–170 normally). These patterns fit rainstorms and a heat spell. I'm assuming that: there is no weather data here to confirm it.
4. **Housing (HPD) is the real growth story: 56,003 requests, +40% YoY (+15.9k) and +8% vs May–July.** It is broad-based: Unsanitary Condition +35% YoY (mostly pests 7.9k and mold 4.1k), Water Leak +75% YoY / +50% vs May–July, Paint/Plaster +39%, Plumbing +40%. Of all agencies, HPD has the largest number of requests still "Open" (11,673, 21%).
5. **Other agencies that grew YoY:** DOT +35% (Street Condition +71% YoY: 4.3k potholes, 2.8k cave-ins) and DOB +36% (Building/Use +63%, mostly illegal residential conversions).
6. **Helicopter noise (EDC) has nearly disappeared:** 229 requests vs 1,842 in Aug 2025 (−88%) and ~690/month in May–July (−67%). All 229 are still "In Progress". This looks more like an intake or routing change than residents complaining less, and it needs checking.

## What changed vs previous months

### Agencies (August 2026 count; change vs May–July monthly average; change vs Aug 2025)
| Agency | Aug 2026 | vs May–Jul | YoY | Comment |
|---|---|---|---|---|
| NYPD | 149,901 | −7% | −3% | Seasonal drop after July: Illegal Fireworks −83% (515 vs ~3.1k), Residential Noise −10%, Illegal Parking −6% (but +8% YoY) |
| HPD | 56,003 | +8% | **+40%** | Broad housing-condition growth (see above) |
| DSNY | 30,220 | +6% | 0% | Stable |
| DOT | 23,395 | −4% | **+35%** | Street Condition +71% YoY, Traffic Signal +30% YoY |
| DEP | 22,233 | −7% | +15% | Relabelled water and sewer types, plus storm/heat spikes |
| DPR | 15,705 | −19% | +22% | Damaged Tree −29% vs May–July (likely early-summer storms) but +46% YoY |
| DOB | 12,239 | +12% | **+36%** | Illegal conversions |
| DHS | 4,188 | −13% | −31% | Homeless Person Assistance −27% YoY, flat vs May–July |
| EDC | 229 | **−67%** | **−88%** | Helicopter noise only (see above) |

### Complaint types (after combining the relabelled DEP names)
- **Largest real increases vs May–July:** Unsanitary Condition +2.5k (+21%), Water Leak +1.8k (+50%), Paint/Plaster +1.1k (+21%), Sewer (combined) +1.1k (+27%), Building/Use +0.9k (+37%).
- **Largest decreases vs May–July:** Residential Noise −3.5k, Illegal Parking −3.4k, Illegal Fireworks −2.6k, HEAT/HOT WATER −2.6k (−41%), Water (combined) −2.4k, Damaged Tree −1.9k. Most of these are normal seasonal changes from early summer.
- **Large YoY drops that are flat vs May–July:** Drug Activity (−83% YoY) and Lead test kits (−46% YoY). These were step changes that happened before May 2026, not new August events.

### Boroughs
All five boroughs were 2–5% below their May–July pace. YoY, Brooklyn led (+18%, 103,859 requests) and Queens was flat (+1%). No borough stands out.

### Channels
Online intake rose to **50.8%** of requests (44.9% in Aug 2025; 47.2% in May–July). Phone fell to 21.7% (26.3% YoY) and mobile app to 18.7% (21.6% YoY). The "OTHER" channel, which had 1,855 requests in May–July, recorded **zero** in August, so its definition has probably changed.

## Things that need attention / caveats
- **Open-request counts can't be compared with earlier periods.** 12.3% of August requests (40.4k) were not "Closed" when the data was pulled, against 6% for May–July and 2% for Aug 2025. Most of that gap is because August requests have had less time to close: the open share rises from 9.5% for requests made in week 1 to 14.8% for those made in the last week. Do not read it as a backlog crisis. Within August, the agencies with the most unresolved requests are TLC (82%), DPR (57%), DOHMH (45%), DCWP (43%), DOB (36%) and HPD (21%, the largest number at 11.7k). NYPD has almost none.
- **Data quality in the August file:**
  - 342 requests have a closed date before their created date.
  - 5,550 have a closed date exactly equal to the created date (closed instantly).
  - 5,267 have a closed date but a status other than "Closed".
  - 1.9% have no coordinates.

  These problems are small, but they will distort resolution-time metrics if they aren't filtered out.
- **The baseline file has no agency × status or complaint × descriptor breakdowns.** So I can't tell whether HPD's open rate or the cave-in volume is unusual compared with earlier months.

## Recommendations / what to investigate next
1. **Fix the reporting taxonomy now.** Map Water System → Water Maintenance, Sewer → Sewer Maintenance and Hazardous Materials → Hazardous Material in every trend report. Ask DEP for the date the change took effect: some "Maintenance" records already appear in May–July. Also confirm what happened to the "OTHER" channel.
2. **HPD housing conditions (top priority).** Growth of +40% YoY across pests, mold, leaks and plumbing is the one sustained, substantive increase in this month's data. Check whether it is real demand or an intake effect (for example, HPD's online share or a new form). Then check whether HPD has enough inspection capacity, since it already has 11.7k open requests and the slowest median closure time of any agency (~9 days).
3. **Helicopter noise / EDC.** Confirm with EDC and 311 whether complaints are being routed elsewhere or intake has changed. A drop of nearly 90% in one category is unlikely to be real.
4. **Storm response by DEP and DOT.** Overlay the Aug 3/20/21/23/27 sewer spikes and the Aug 6–11 hydrant surge on weather and open-hydrant data. Review how quickly catch-basin and flooding requests in Queens and Brooklyn were resolved. Also check whether the 2.8k street cave-ins are linked to the flooding.
5. **DOB illegal conversions (+63% YoY) and DOT street condition (+71% YoY).** Find out whether these are new enforcement campaigns or proactive inspections being logged through 311, or genuinely more complaints.
6. **Re-measure the open/backlog figures at a fixed age** (for example, share still open 30 days after creation) so months can be compared fairly, and filter out the inconsistent closed dates before reporting resolution times.

*Assumptions: May–July figures are scaled to a 31-day month by day count. Links to weather are inferred from the timing and descriptors of complaints, not from weather data. I treated status as recorded on 2026-09-15.*
