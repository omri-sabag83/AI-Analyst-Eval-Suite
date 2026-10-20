# NYC 311 — August 2026 Monthly Briefing

*Data: NYC Open Data "311 Service Requests from 2020 to Present", extracted 2026-09-15. Grain: one row per service request, created 1–31 Aug 2026 (328,701 rows, all 31 days present). Comparisons: May–Jul 2026 combined (92 days, scaled to a 31-day month, "baseline") and August 2025 ("YoY"). Tags: **[OBS]** computed from the data; **[HYP]** plausible but not shown by this data; **[CON]** the best-supported reading.*

## Bottom line

1. **Volume was normal for summer.** There were 328,701 requests (10,603/day). That is 3.4% below the May–Jul daily rate, 4.2% below July, and **8.1% above August 2025**. [OBS]
2. **The two biggest complaint-type "moves" are a relabel, not a change in demand.** At DEP, "Water System" and "Sewer" fell to zero and "Water Maintenance" and "Sewer Maintenance" rose by the same amount. Any dashboard tracking these types by name will show false alarms. [CON, independently verified]
3. **Housing (HPD) is the real growth story.** HPD is up 40% YoY (+15.9k) and 8% vs baseline, led by unsanitary conditions, water leaks and paint/plaster. About a fifth of the YoY increase is exact-duplicate rows that need checking. [OBS / CON]
4. **Two short incidents:** a fire-hydrant surge on 6–11 Aug, and sewer backup/flooding spikes on 3, 20–21, 23 and 27 Aug. [OBS; causes are HYP]
5. **Needs attention:** EDC helicopter-noise complaints are down 67% vs baseline, and none of August's 229 has been closed. This looks like a broken or changed intake/handling path. [OBS / HYP]

## Data notes (read before the numbers)

- **Totals reconcile.** The row-level file (328,701) matches `monthly_totals.csv` and the August breakdown total. May+Jun+Jul monthly totals (1,009,896) match the baseline total. The August 2025 total (304,039) comes only from the breakdown file, because `monthly_totals` starts in Sep 2025.
- **Status is right-censored, so open counts are not a backlog trend.** August requests were only 15–45 days old when the data was pulled, while baseline requests were 45–137 days old. "Open" is 16,884 in August vs about 4,750/month in the baseline, and "In Progress" is 21,899 vs about 13,200. Not-closed share rises with recency (week 1: 9.5%, whole month: 12.3%). Most open items sit with slow-closing agencies: HPD (11.7k not closed), DPR (8.9k), DOB (4.4k), DOHMH (4.0k), DOT (3.8k) and TLC (2.6k, 82% not closed). A fair backlog comparison needs status measured at equal age.
- **Duplicates.** 3,425 rows are exact copies of another row on every field except `unique_key` (same timestamp to the second, same location, same descriptor). 98.6% of them are HPD, mostly UNSANITARY CONDITION and PAINT/PLASTER. They may be legitimate (HPD logs one record per problem or apartment, and the apartment field is not in this extract) or they may be double ingestion. I have **not** removed them. I also can't tell whether earlier periods contain the same pattern.
- **Minor issues.** 342 records (334 of them DEP) have a close time a few seconds *before* the create time. The "OTHER" intake channel (about 625/month in the baseline) recorded zero requests in August.
- **Assumption:** baseline monthly-equivalents are the May–Jul total × 31/92. The effects of summer seasonality on that comparison are discussed where relevant.

## What changed: complaint types

| Complaint type | Aug 2026 | Baseline (31-day equiv.) | Δ vs baseline | Aug 2025 | Δ YoY | Reading |
|---|---|---|---|---|---|---|
| Water System | 0 | 10,587 | −10,587 | 7,129 | −7,129 | Relabelled |
| Water Maintenance | 8,925 | 777 | +8,148 | 0 | +8,925 | Relabelled |
| Sewer | 0 | 3,473 | −3,473 | 2,477 | −2,477 | Relabelled |
| Sewer Maintenance | 5,060 | 508 | +4,552 | 2 | +5,058 | Relabelled |
| Noise – Residential | 30,622 | 34,126 | −3,504 (−10%) | 32,756 | −6.5% | Seasonal / soft |
| Illegal Parking | 51,216 | 54,635 | −3,419 (−6%) | 47,243 | +8.4% | Normal |
| Illegal Fireworks | 515 | 3,085 | −2,570 (−83%) | 499 | flat | July 4th seasonality |
| HEAT/HOT WATER | 3,682 | 6,248 | −2,566 | 2,929 | +26% | Seasonal (May off-season tail) |
| UNSANITARY CONDITION (HPD) | 14,650 | 12,108 | **+2,542 (+21%)** | 10,842 | **+35%** | Real rise |
| WATER LEAK (HPD) | 5,481 | 3,657 | **+1,824 (+50%)** | 3,125 | **+75%** | Real rise |
| PAINT/PLASTER (HPD) | 6,604 | 5,468 | +1,136 (+21%) | 4,765 | +39% | Real rise |
| Street Condition (DOT) | 9,552 | 11,043 | −1,491 | 5,590 | **+71%** | YoY step-up |
| Drug Activity (NYPD) | 947 | 861 | flat | 5,447 | **−83%** | Standing change, pre-dates the baseline |

**The relabel, verified.** [CON] Water+sewer combined is 13,985 in August vs 15,345 baseline-equivalent (−8.9%) and 9,608 in Aug 2025 (+46%). DEP's agency total moves the same way (−6.6% vs baseline). The new types are 100% DEP, and their descriptors cover the old scope: hydrants, leaks, main breaks and no-water under Water Maintenance; catch basins, backups, street flooding and manholes under Sewer Maintenance. The new names already appear in May–Jul (3.8k rows), so the cutover was **phased** and finished by August, not a single switch on 1 Aug. A smaller pair, "Hazardous Materials" → "Hazardous Material", follows the same pattern. An independent verifier agent recomputed this from the raw files and returned *holds with caveat*. The caveat: the −9% is close enough to the margin that a modest real decline, masked by the weather spikes below, can't be ruled out.

## What changed: agencies

| Agency | Aug 2026 | Δ vs baseline | Δ YoY | Driver |
|---|---|---|---|---|
| NYPD | 149,901 | −7% | −3% | Seasonal noise and fireworks decline; Drug Activity down YoY |
| **HPD** | 56,003 | **+8%** | **+40% (+15.9k)** | Unsanitary, water leak, paint/plaster, plumbing, general |
| DSNY | 30,220 | +6% | 0% | Stable |
| DOT | 23,395 | −4% | +35% | Street Condition |
| DEP | 22,233 | −7% | +15% | Water/sewer (relabelled; see above) |
| DPR | 15,705 | −19% | +22% | Damaged/overgrown trees down from the early-summer peak |
| DOB | 12,239 | +12% | +36% | Building/Use (+37% vs baseline) |
| DHS | 4,188 | −13% | −31% | Homeless Person Assistance down YoY |
| **EDC** | 229 | **−67%** | **−88%** | Helicopter noise only; all 229 still open |

**HPD sensitivity:** [OBS] removing the 3,378 extra HPD duplicate rows leaves about 52.6k, which is still **+31% YoY**. So the housing-conditions rise is real and does not come from duplicates. It is not explained by heat complaints, which are a small seasonal share.

**Channels:** [OBS] Online made up 51% of requests (+4% vs baseline, +22% YoY). Phone (−10%) and Mobile (−12%) fell vs baseline, Unknown was +32% YoY, and Other went to zero. [HYP] The growth in online and the drop in "Other" may be tied to HPD and EDC intake changes, but the baseline file has no agency × channel cross-tab to test that.

## Incidents in August

- **Fire-hydrant surge, 6–11 Aug.** [OBS] For these six days the usual hydrant descriptors (Running / Running Full / Leaking, about 150–200/day combined) drop to zero. A descriptor not seen on any other day, "Fire Hydrant Emergency", takes their place at 300–520/day (2,190 in total, all now closed). The rest of the month is normal. Net excess is roughly +1,200 requests above normal hydrant volume. [HYP] This could be a heatwave (hydrants opened illegally) combined with a temporary emergency intake code. To confirm, check NWS temperatures and DEP's ops log for an emergency declaration.
- **Sewer backup/flooding spikes on 3, 20, 21, 23 and 27 Aug.** [OBS] Sewer Maintenance hit 320–520/day vs a typical 50–150. The spikes were dominated by Backup, Catch Basin Clogged and Flooding on Street, and HPD WATER LEAK spiked on the same days (e.g. 462 on 20 Aug vs about 150–200 normally). [HYP] These look like heavy-rain events. To confirm, check NWS rainfall by day and borough.

## Standing issues (not August-specific)

- **HPD housing-condition complaints are structurally higher than last year** (+31–40% YoY). [CON]
- **Drug Activity is 83% below last year but flat vs May–Jul,** so this is a step change from earlier in the year. Its cause (reclassification, routing to another channel, or a real decline) is unknown. [OBS / HYP]
- **EDC helicopter noise.** Volume has fallen steeply: 1,842 (Aug 2025) → about 690/month (May–Jul) → 229. Every August record is still open, 96% arrived online and 97% have descriptor "Other". [HYP] The intake form or channel may have changed (consistent with the "Other" channel disappearing), and/or no one is closing these records.

## Recommendations / what to investigate next

1. **Fix reporting for the DEP taxonomy change.** Map Water System→Water Maintenance, Sewer→Sewer Maintenance and Hazardous Materials→Hazardous Material in all trend dashboards, and get the official cutover date from DEP/OTI. Without this, DEP's two biggest series look like a collapse plus a 10× surge.
2. **Brief HPD on the +31–40% YoY rise** in unsanitary, leak and paint/plaster complaints. Get a borough/community-board split and repeat-building analysis to tell whether this is broad deterioration or concentrated in particular buildings.
3. **Resolve the HPD duplicate rows** with OTI/HPD: are they legitimate multi-problem records or double ingestion? Apply the same check to prior months before trusting HPD trend counts.
4. **Escalate the EDC helicopter path.** Confirm whether the intake changed and why no August case has been closed.
5. **Confirm the two incident causes** with weather data and DEP ops logs. If the hydrant code is a temporary emergency protocol, document it so future heatwaves are recognised.
6. **Measure backlog properly.** Build a status-at-fixed-age metric (e.g. % closed within 14 and 30 days of creation) so open counts can be compared across months. Today's open-count gap reflects snapshot timing.
7. **Lower priority:** confirm the Drug Activity step-change with NYPD, and fix the DEP close-before-create timestamps.
