# NYC 311 — August 2026 Monthly Briefing

*Data: NYC Open Data "311 Service Requests from 2020 to Present", pulled 2026-09-15. Comparisons are against the May–Jul 2026 monthly average ("recent baseline") and August 2025 ("YoY").*

## Bottom line

1. **Overall volume was normal.** There were 328,701 requests in August, 10,603 a day. That is 3.4% below the May–Jul daily rate and 8.1% above August 2025, and it sits right on the 12-month average (328,557). Nothing in the total needs action.
2. **Housing (HPD) is the real story.** HPD requests were **+40% YoY** (40,078 → 56,003) and +9% against the recent baseline, even though summer is normally HPD's quiet season. HPD alone accounts for about two-thirds of the city's YoY growth (+15.9k of +24.7k).
3. **Two possible intake failures need checking now:** (a) DHS homeless-assistance requests almost stopped on **Aug 7–10**; (b) **helicopter noise (EDC) fell 88% YoY**, and every August ticket is still "In Progress".
4. **A DEP category rename breaks trend lines.** "Water System" and "Sewer" disappeared, replaced by "Water Maintenance" and "Sewer Maintenance". Any complaint-type dashboard will show false ±100% swings unless the old and new names are mapped together.
5. **Several of the biggest "movers" are artefacts, not real change:** the rename above, normal seasonality (fireworks, heat), a one-off spike in August 2025 (Drug Activity), and open/closed status that is incomplete because the data was pulled only 15 days after month end.

---

## 1. What happened in August

| | Aug 2026 | May–Jul 2026 avg/month | Aug 2025 |
|---|---|---|---|
| Requests | 328,701 | 336,632 | 304,039 |
| Per day | 10,603 | 10,977 (−3.4%) | 9,808 (+8.1%) |

- Daily volume was steady: 9,249–11,667 a day, with the usual weekday highs and weekend lows. No day of data is missing at the citywide level.
- Top complaint types: Illegal Parking (51.2k), Residential Noise (30.6k), Street/Sidewalk Noise (23.6k), HPD Unsanitary Condition (14.7k), Blocked Driveway (14.6k), Street Condition (9.6k), Water Maintenance (8.9k).
- NYPD handles 46% of requests (149.9k), almost all of them parking and noise.

## 2. What changed: agencies

| Agency | Aug 2026 | vs May–Jul avg | vs Aug 2025 | Read |
|---|---|---|---|---|
| **HPD** | 56,003 | +4,692 (+9%) | **+15,925 (+40%)** | Real; biggest mover (Section 3) |
| NYPD | 149,901 | −9,853 (−6%) | −4,336 (−3%) | Mostly seasonal: fireworks −2.5k, residential noise −3.1k after July |
| DOT | 23,395 | −3% | +6,074 (+35%) | Street Condition +71% YoY (potholes, cave-ins) |
| DOB | 12,239 | +13% | +3,231 (+36%) | Building/Use +63% YoY |
| DEP | 22,233 | −6% | +2,966 (+15%) | Storm-driven sewer/water; taxonomy change (Section 5) |
| DPR | 15,705 | −18.5% | +2,797 (+22%) | Damaged Tree +46% YoY; storm days |
| DHS | 4,188 | −12% | −1,895 (−31%) | Partly an intake gap (Section 4a) |
| EDC | 229 | −67% | −1,613 (−88%) | Suspicious (Section 4b) |
| OOS (Sheriff) | 390 | flat | new since Aug 2025 | Cannabis Retailer complaints; a new line of work, not a spike |

**Boroughs:** Brooklyn drove the YoY rise (+15.6k, +18%). Queens was flat (+0.6%). Against the recent baseline every borough was 1–4% lower, which is consistent with the seasonal dip.

**Channels:** Online kept gaining share, +22% YoY (now 51% of requests), while phone (−11%) and mobile (−6.5%) fell. Part of the volume growth may come from easier online reporting rather than more underlying problems.

## 3. Priority finding: housing complaints are well above last year

HPD complaint types, August 2026:

| Type | Aug 2026 | vs May–Jul avg | vs Aug 2025 |
|---|---|---|---|
| Unsanitary Condition (pests 7.9k, mold 4.1k) | 14,650 | +22% | +35% |
| Plumbing | 6,666 | −3% | +40% |
| Paint/Plaster | 6,604 | +22% | +39% |
| Water Leak | 5,481 | **+52%** | **+75%** |
| General | 4,479 | +16% | +67% |
| Door/Window | 4,417 | +6% | +34% |
| Elevator | 2,646 | +8% | +47% |

- The rise is broad: it covers every major HPD type, not just one. The largest volumes are in Brooklyn (17.5k) and the Bronx (17.3k).
- Some of it is weather. Water Leak requests jumped on the same days as sewer backups and fallen trees (Aug 3, 20, 21 and 23), which looks like rain events. *Hypothesis: I had no weather data to confirm this.* But pests, paint and plaster, and door/window complaints are also up, and those do not follow storms.
- HPD is also the slowest agency to close requests: median 219 hours (about 9 days) for closed tickets, and 21% of August HPD tickets were still "Open" on Sep 15.
- **What I can't tell from this data:** whether this is a lasting rise or whether August 2025 was unusually low. I only have HPD at the three snapshot periods, not monthly, and no breakdown by channel within HPD. The +9% against May–Jul, during a season when housing complaints usually fall, suggests the rise is real.

## 4. Unusual and needs attention

**(a) DHS intake gap, Aug 7–10.** Homeless Person Assistance requests fell from about 125 a day to **2, 2, 2 and 15** on Aug 7–10, then recovered on Aug 11. The drop hit every channel (online, phone and mobile), which points to an intake or routing failure inside DHS rather than a real fall in need. Estimated shortfall: **~480 requests**, about 12% of the month. That gap fully explains DHS's −12% against the baseline. *Action: confirm with DHS/311 whether requests were lost, rerouted or entered late, and whether people needing help were reached.*

**(b) Helicopter noise collapse (EDC).** There were 229 requests, against 1,842 in Aug 2025 and a recent average of 684 a month. Volume ran at about 4 a day in Aug 1–9, then about 10 a day. **All 229 are still "In Progress"** and none are closed. Either reporting really fell or there is an intake/routing change. *Action: check with EDC whether the complaint form or routing changed.*

**(c) Storm-like days.** Aug 3, 20, 21 and 23 show joint spikes in Sewer Maintenance (e.g. 486 and 521 a day against about 100), Damaged Tree, Water Leak and Street Condition. Hydrant complaints peaked on Aug 6–11 (up to 626 a day), which looks like a heat-related pattern. These are one-off events, not standing trends, but they explain much of the DEP, DPR and HPD-leak volume.

## 5. Movers that are artefacts — do not act on these as real trends

- **DEP taxonomy change.** "Water System" (10.5k/month in May–Jul) and "Sewer" (3.4k/month) are at **zero** in August. They were replaced by "Water Maintenance" (8,925) and "Sewer Maintenance" (5,060). The new names already appeared in small numbers in May–Jul, so the switch probably happened during July. Combined like-for-like: water is 8.9k against an 11.2k baseline (−21%), and sewer is 5.1k against 3.9k (+28%, storm-driven).
- **Seasonality.** Illegal Fireworks (−83% against May–Jul) and HEAT/HOT WATER (−40%) are normal post-July patterns. Against August 2025 both are flat or slightly up.
- **Drug Activity "−83% YoY"** reflects a spike in **August 2025** (5,447 against a normal ~850). August 2026 (947) is in line with the recent baseline. The 2025 spike is a historical question, not a current one.
- **Status/backlog.** August shows 16,884 "Open" and 21,899 "In Progress" tickets, far above earlier periods. That is expected, because August tickets were at most 45 days old when the data was pulled, while baseline tickets had months to close. The open share rises steadily by week of creation (6% for week 1 up to 20% for the last days). **Backlog cannot be compared across periods from this extract.**

## 6. What to investigate next (priority order)

1. **HPD surge:** get HPD monthly volume for the past 24 months, broken down by borough and channel. That will show whether +40% YoY is a step change, a trend, or an unusually low August 2025, and whether the move to online reporting is inflating it. Check the 9-day median close time and open backlog against equal-age cohorts.
2. **DHS Aug 7–10 outage:** confirm the cause and whether requests were lost. Add a daily volume alert per agency (e.g. flag any agency below 50% of its trailing 7-day average).
3. **EDC helicopter complaints:** confirm intake and routing, and why nothing has closed.
4. **Standardise the DEP mapping** (Water System ↔ Water Maintenance, Sewer ↔ Sewer Maintenance) in all reporting before the next briefing.
5. **Backlog reporting:** compare closure rates at a fixed age (e.g. % closed within 14 days) rather than status on the pull date.
6. *Lower priority:* zip 11366 (Queens CB 8) appears unusually often in low-volume categories (Drug Activity, Traffic, House of Worship noise, Vehicle noise 311). This may be one or a few frequent reporters. Worth a look before treating those category trends as citywide.

## Assumptions and limitations

- May–Jul 2026 is used as a monthly average (total ÷ 3). The totals comparison is also shown per day to adjust for month length.
- Baseline breakdowns are one-dimensional (no agency × borough or agency × channel), so the reasons for mix changes inside an agency are inferred from the August row-level data only.
- No weather data was available; the storm and heat explanations are hypotheses based on the timing of the complaints.
- Status fields reflect the 2026-09-15 pull and are not comparable across periods.
- 334 closed tickets have a close time earlier than their creation time. This is a minor data-quality issue and has no effect on volume findings.
