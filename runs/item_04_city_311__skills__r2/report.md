# NYC 311 — August 2026 Monthly Briefing

*Data: NYC Open Data "311 Service Requests from 2020 to Present", pulled 2026-09-15. Comparisons: July 2026, the May–July 2026 monthly average ("recent baseline", 336,632/month), and August 2025 ("YoY").*

## Headline

**August 2026 was an ordinary month overall. 311 received 328,701 requests**, which is down 4.2% on July, down 2.4% on the May–July average and up 8.1% on August 2025 (304,039). That total sits inside the past 12 months' range of 302k–349k. Daily volume was steady at 9.2k–11.7k, with the normal weekday/weekend pattern and no outage-like gaps.

The headline figure hides three things that need attention:

1. **Two of the biggest "movers" are not real changes.** DEP's *Water System* and *Sewer* complaint types were renamed *Water Maintenance* and *Sewer Maintenance*. Anyone who reads the type-level tables at face value will see −100% and +1,000% swings.
2. **Housing (HPD) demand is clearly up: +40% YoY and +9% on the recent baseline.** It is the largest real increase this month.
3. **Open/backlog figures for August cannot be compared with earlier periods.** The data was pulled only 2–6 weeks after these requests were created. Do not report them as a performance decline.

---

## 1. Data caveats (read before the numbers)

| Issue | Evidence | How I handled it |
|---|---|---|
| **Complaint-type rename at DEP** | *Water System* fell from 7,129 (Aug-25) to 0, and *Sewer* from 2,477 to 0. *Water Maintenance* rose to 8,925 and *Sewer Maintenance* to 5,060, all of it DEP. Their descriptors (hydrants, water main breaks, catch basins, backups) match the old types. The new names already appear in May–July (3,813 combined), so the switch came partway through the baseline period. | Treated old and new names as one category (see §3). |
| **Status is a snapshot, not an outcome** | 11.8% of August requests are Open/In Progress (38,783), against 1.6% for August 2025 (4,979). The open count climbs steadily toward the end of the month: 548 open on Aug 1 versus 2,245 on Aug 31. That is what a young cohort looks like, not a collapse in closures. HPD (median close time about 9 days), DPR, DOHMH and TLC hold most of the open items. | Excluded status from the "what changed" findings. |
| **Minor data-quality issues** | 342 requests have a closed date before their created date. 3,425 rows are identical except for `unique_key`, which suggests duplicate submissions. Both are about 1% or less of volume. | Noted. They do not change any finding. |
| **Baseline has no monthly detail** | The type, agency and borough breakdowns cover May–July only as a combined total. | Divided by 3 to get a monthly average. This hides any trend *within* May–July. |

## 2. What changed: agencies

| Agency | Aug-26 | vs May–Jul avg | vs Aug-25 | Read |
|---|---:|---:|---:|---|
| NYPD | 149,901 | −6.2% | −2.8% | Seasonal: post-July-4 drops in fireworks (−83% vs baseline) and residential noise (−9%) |
| **HPD** | 56,003 | **+9.1%** | **+39.7% (+15,925)** | **Real increase. Largest absolute YoY mover** |
| DSNY | 30,220 | +6.7% | −0.4% | Normal |
| **DOT** | 23,395 | −3.1% | **+35.1% (+6,074)** | Street Condition +71% YoY (potholes, cave-ins) |
| DEP | 22,233 | −5.6% | +15.4% | Water/sewer volume is weather-driven (see §4) |
| DPR | 15,705 | −18.5% | +21.7% | Tree complaints below a stormy early summer but above last August |
| **DOB** | 12,239 | **+13.1%** | **+35.9%** | Building/Use +63% YoY, +38% vs baseline |
| DHS | 4,188 | −12.2% | **−31.2%** | Homeless Person Assistance −27% YoY |
| **EDC** | 229 | **−66.5%** | **−87.6%** | Helicopter-noise reports have nearly vanished |

## 3. What changed: complaint types (with the rename fixed)

**Biggest real increases vs August 2025**

- **HPD housing-condition types:** Unsanitary Condition +3,808 (+35%; mostly pests and mold), Water Leak +2,356 (+75%), Plumbing +1,919 (+40%), Paint/Plaster +1,839 (+39%) and General +1,795 (+67%). These are also up 16–52% on the recent baseline, so the rise is not just year-ago seasonality. It is the clearest sustained signal in the month.
- **DEP water and sewer, combined:** 13,985 versus 9,606 in Aug-25 (+46%), but 8% *below* the May–July average (15,180/month). That fits a wet, hot summer: see the event days in §4.
- **Street Condition (DOT):** +3,962 (+71% YoY), led by Pothole (4,292) and Cave-in (2,776). It is 13% below the baseline, so the step-up began before August.
- **Damaged Tree:** +46% YoY. Storm-driven: spikes on Aug 3, 7, 20 and 21.
- **Illegal Parking:** +3,973 (+8%). This is the largest type by volume (51,216) and is growing roughly in line with the total.

**Biggest real decreases**

- **Drug Activity:** 947 versus 5,447 in Aug-25 (−83%), but flat against May–July (852/month). This was a step change some time between September 2025 and May 2026, not an August event.
- **Noise – Helicopter (EDC):** 229 versus 1,842 YoY and 684/month in the baseline. The fall is continuing.
- **Lead (DEP lead-kit requests):** −46% YoY, though +27% vs baseline.
- **Homeless Person Assistance:** −27% YoY.
- **Fireworks and residential/street noise:** normal post-July seasonal decline.

**New since last year (not an August event):** *Cannabis Retailer* complaints under a new "OOS" agency code (390 in August, about 409/month in the baseline).

## 4. Unusual within August

- **Weather events show up clearly in the daily data.** On Aug 3, 20, 21 and 23, Sewer Maintenance spiked 3–5× its typical day (486, 521, 411 and 448 against about 110). Water Leak, Damaged Tree and Street Condition jumped on the same days, consistent with heavy-rain or storm days. Separately, Aug 6–11 had a run of fire-hydrant complaints (Water Maintenance at 430–630/day against about 220), which looks like a heat wave. I did not have weather data, so this attribution is an inference from timing and descriptors.
- **Channel mix continues to shift to online.** ONLINE is 51% of requests (+22% YoY), while PHONE is down 11% and MOBILE down 7% YoY. Daily channel counts are smooth, so no app or phone outage is visible. *Unknown* channel (+32% YoY) is almost entirely DOB and DOT records. That is a data-capture gap at those agencies, not citizen behaviour.

## 5. Recommendations: what to investigate next

1. **HPD housing conditions (highest priority).** Volume is up about 40% YoY and still rising against the summer baseline: pests, mold, leaks and plumbing. Check whether this is concentrated in particular buildings, landlords or community boards, which would point to enforcement targets. Also check HPD's real closure times once the August cohort has matured; HPD already has the slowest median close time (about 9 days).
2. **Fix reporting for the DEP rename.** Map *Water System → Water Maintenance* and *Sewer → Sewer Maintenance* in all dashboards and trend reports. Check other agencies for similar silent renames.
3. **Helicopter noise (EDC) and Drug Activity (NYPD).** Both have fallen 80–90% YoY. Confirm whether these complaints are now routed elsewhere (another agency, form or channel) or whether demand really dropped. If they are being re-routed, the YoY "decline" is an artefact and residents' complaints may be going untracked.
4. **DOT street condition and DOB Building/Use.** Both are up 35–70% YoY. Separate one-off causes (storm damage, cave-ins, a construction surge) from a sustained rise, and check whether DOT's high cave-in volume (2,776) is concentrated in particular locations.
5. **DHS −31% YoY.** Check whether demand is lower or whether requests are moving to other channels or programmes before treating it as an improvement.
6. **Backlog reporting.** Re-pull August status around mid-October and compare closure rates with August 2025 at the same age (e.g., the share closed within 30 days). Until then, do not publish August "open request" counts.
7. **Data hygiene.** Ask DOB and DOT to populate the intake channel. Review the about 3.4k near-duplicate rows and the 342 negative-duration records.

---
*Assumptions: May–July baseline taken as a monthly average (combined ÷ 3). Weather explanations are inferred from timing and descriptors, not confirmed with weather data. Percentages are of raw request counts; I did not adjust for population or for the number of weekdays in each month (August 2026 has 21 weekdays).*
