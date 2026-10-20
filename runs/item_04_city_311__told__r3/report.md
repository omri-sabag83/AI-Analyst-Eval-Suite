# NYC 311 — August 2026 Monthly Briefing

**Bottom line**
- **Total volume was normal.** 328,701 requests is 4.2% below July and 2.4% below the May–July monthly average, but 8.1% above August 2025. It sits inside the last 12 months' range of 302k–349k.
- **The real story is housing.** HPD (housing) requests are up **40% year over year (+15.9k)**. That is about two-thirds of the city's net YoY growth, and the rise covers every HPD complaint category. HPD is also still rising against recent months (+8%, or +15% excluding seasonal heat complaints).
- **One operational problem needs action now.** DHS *Homeless Person Assistance* requests almost stopped for four days (Aug 7–10). That points to an intake or routing failure, not a fall in need.
- **Don't read the raw "top movers" list at face value.** The biggest complaint-type swings (*Water System*, *Sewer*, *Water Maintenance*, *Sewer Maintenance*) come from a DEP category rename. The jump in open requests reflects how recently the data was pulled, not a backlog.

Tags: **[OBS]** = computed from the data; **[HYP]** = consistent with the data but not proven; **[CON]** = the best-supported reading.

---

## 1. Data and method (read before the findings)

- **Grain and coverage:** one row per service request created 1–31 Aug 2026. That is 328,701 rows over 31 complete days, with 9,249–11,667 requests a day and no missing days. The row count matches `monthly_totals.csv` and the August period total in `baseline_breakdowns.csv`. The May–July baseline (1,009,896) equals the sum of the three monthly totals.
- **Comparisons:**
  - *Recent baseline:* May–July 2026 scaled to a 31-day month (× 31/92).
  - *Year over year (YoY):* August 2025.
  - The baselines are only available as one-way breakdowns (agency, type, borough, channel, status). Cross-dimension comparisons with earlier periods (e.g. HPD × borough) are therefore not possible.
- **Censoring (important):** the data was pulled on 2026-09-15, so August requests were only 2–6 weeks old. 12.3% of them are not "Closed", against 5.9% in the May–July baseline and 1.9% in August 2025. The share still open rises steadily from week 1 (9.5%) to week 4 (15.4%). That pattern comes from request age, not from performance. **Status is not compared across periods in this briefing.**
- **DEP category rename:** *Water System* and *Sewer* (41.7k in May–July; 9.6k in August 2025) have zero requests in August 2026. They were replaced by *Water Maintenance* (8,925) and *Sewer Maintenance* (5,060), which have the same descriptors (hydrants, leaks, catch basins, backups). The new names already appear in the May–July baseline (3.8k), so the cut-over was probably in late July. In this briefing the four types are combined.
- **Smaller taxonomy changes YoY:** *Cannabis Retailer* (new agency OOS, 390), *Hazardous Materials* → *Hazardous Material*, and *Bike/Roller/Skate Chronic* → *Bike/Roller/Skate*.
- **Data quality:**
  - 342 requests have a closed date earlier than their created date.
  - 4,820 rows (1.5%) duplicate another row's timestamp, type, descriptor, ZIP code and coordinates. These are probably repeat submissions; they were kept in the counts.
  - 1.9% of rows have no coordinates and 0.1% have borough "Unspecified".
  - None of these issues is large enough to change the findings.

---

## 2. What happened in August

| Metric | Aug 2026 | vs Jul 2026 | vs May–Jul avg | vs Aug 2025 |
|---|---|---|---|---|
| Total requests | 328,701 | −4.2% | −2.4% | **+8.1%** (+24,662) |

**[OBS]** The largest complaint types were Illegal Parking (51.2k), Noise – Residential (30.6k), Noise – Street/Sidewalk (23.6k), Unsanitary Condition (14.7k) and Blocked Driveway (14.6k). NYPD handled 46% of requests and HPD 17%.

**[CON]** The small fall against May–July is seasonal. The categories that drop in August are the ones that peak in early summer:

| Type | Aug 2026 | vs May–Jul avg |
|---|---|---|
| Illegal Fireworks (July 4) | 515 | −83% |
| HEAT/HOT WATER | 3,682 | −41% |
| Damaged Tree | 4,814 | −29% |
| Noise – Residential | 30,622 | −10% |
| Illegal Parking | 51,216 | −6% |

Each of these is flat or up compared with August 2025, so none of them is a concern.

### Agencies that moved most (YoY; together they reconcile to the +24,662 net change)

| Agency | Aug 2025 | Aug 2026 | Change | % |
|---|---|---|---|---|
| **HPD** (housing) | 40,078 | 56,003 | **+15,925** | **+40%** |
| DOT (transport) | 17,321 | 23,395 | +6,074 | +35% |
| DOB (buildings) | 9,008 | 12,239 | +3,231 | +36% |
| DEP (environment) | 19,267 | 22,233 | +2,966 | +15% |
| DPR (parks) | 12,908 | 15,705 | +2,797 | +22% |
| NYPD | 154,237 | 149,901 | −4,336 | −3% |
| DHS (homeless services) | 6,083 | 4,188 | −1,895 | −31% |
| EDC (helicopter noise) | 1,842 | 229 | −1,613 | −88% |

### Complaint types that moved most (DEP water and sewer types combined)

| Type | Aug 2025 | Aug 2026 | YoY | vs May–Jul avg |
|---|---|---|---|---|
| DEP water + sewer (renamed) | 9,608 | 13,985 | +46% | −9% |
| Street Condition (DOT) | 5,590 | 9,552 | +71% | −14% |
| Unsanitary Condition (HPD) | 10,842 | 14,650 | +35% | +21% |
| Water Leak (HPD) | 3,125 | 5,481 | +75% | +50% |
| Paint/Plaster (HPD) | 4,765 | 6,604 | +39% | +21% |
| Building/Use (DOB) | 2,049 | 3,336 | +63% | +37% |
| Drug Activity (NYPD) | 5,447 | 947 | −83% | +10% |
| Noise – Helicopter (EDC) | 1,842 | 229 | −88% | −67% |
| Homeless Person Assistance (DHS) | 4,646 | 3,396 | −27% | 0% |

---

## 3. Findings that matter

### A. Housing complaints are structurally higher and still rising (standing issue, highest priority)
- **[OBS]** HPD has the largest absolute increase of any agency: **+15,925 (+40%) YoY**. That is about 65% of the city's *net* YoY increase, or about 49% of the gross increase before subtracting the agencies that fell. An independent re-computation confirmed these figures.
- **[OBS]** All 13 HPD complaint types rose YoY. The largest single contributor, Unsanitary Condition (+3.8k), accounts for only 24% of HPD's rise. Water Leak (+75%), General (+67%), Plumbing (+40%) and Paint/Plaster (+39%) follow.
- **[OBS]** The rise is not only a year-old step change. HPD is +8% against the May–July average even though heat complaints fall off seasonally, and +15% when HEAT/HOT WATER is excluded. Weekday HPD volume held steady at about 2,000–2,300 a day throughout August.
- **[OBS]** Water Leak and Unsanitary Condition spiked on the same days as street flooding and sewer complaints (Aug 3 and Aug 20). Part of the August uplift is therefore weather-linked.
- **[HYP]** Brooklyn (+15.6k YoY) and the ONLINE channel (+30.5k YoY, against −8.6k for PHONE and −4.3k for MOBILE) rose by similar amounts. These may be the same housing increase seen from different angles: HPD's August requests are 58% online, and 31% are in Brooklyn and 31% in the Bronx. The baseline data has no cross-tabs, so this cannot be confirmed. Treat these as one possible mechanism, not three separate findings.
- **[HYP] The cause is not established.** A rise that is uniform across every category fits two explanations equally well:
  - housing conditions are getting worse, or
  - filing got easier (for example a change to the online form or portal, or outreach), which would lift all categories together.
  Separating them needs HPD × channel × month data for 2025–26 and HPD's own record of portal or process changes.

### B. DHS Homeless Person Assistance intake gap, Aug 7–10 (incident, needs action)
- **[OBS]** These requests ran at about 125–160 a day, then fell to **2 a day on Aug 7, 8 and 9, and 15 on Aug 10**. They recovered to 148 on Aug 11. All three intake channels (mobile, online, phone) fell together. DHS *Encampment* requests continued normally (18–35 a day), and no other complaint type rose to absorb the missing requests.
- **[OBS — estimate]** About **480 requests are missing**: 125 a day (the rate on the other 27 days) × 4 days, minus the 21 observed. This is a counterfactual estimate, not a measured loss.
- **[HYP]** The likely cause is an intake, routing or form failure for this one complaint type. A fall in need is unlikely. The data does not show whether residents who were turned away were helped through another route.
- This type was also −27% YoY (and flat against May–July), so its lower level predates the incident.

### C. Helicopter-noise reports have almost disappeared (standing change, verify)
- **[OBS]** EDC *Noise – Helicopter* had 229 requests in August, against about 690 a month in May–July and 1,842 in August 2025. The count was low on every day (0–21), with no single break visible within August. 96% came through the online channel.
- **[HYP]** Either the intake or routing changed (for example a form change, or reports moving to another system) or there was a real change in flight activity. EDC or OTI should confirm before this is read as an improvement.

### D. Weather-driven days (incidents, explained)
- **[OBS]** Aug 3, 7 and 20 show simultaneous spikes in Sewer Maintenance (up to 521 a day against a median of 122), Water Maintenance, Water Leak, Damaged Tree and Traffic Signal Condition.
- **[HYP]** These look like heavy-rain or storm days. Check against weather records. If confirmed, they explain day-level noise in the agency data rather than a trend.

### E. Other structural breaks to note
- **[OBS]** NYPD *Drug Activity* is −83% YoY but in line with May–July. The drop happened between August 2025 and May 2026, so it is not news this month. The cause is unknown and could be a reclassification.
- **[OBS]** DEP *Lead* is −46% YoY.
- **[OBS]** DOT *Street Condition* is +71% YoY. Separately, 56% of DOT requests have channel "UNKNOWN", which limits channel analysis.

### F. Open and in-progress requests (do not read as a backlog)
- **[OBS]** 12.3% of August requests are not yet closed. This is driven by request age (see section 1).
- Within August, some agencies keep many requests open: DPR has 57% "In Progress", TLC 82%, EDC 100%, HPD 21% "Open" and DOB 36% not closed.
- These are only meaningful against requests of the same age from earlier months, which this data cannot provide.

---

## 4. Recommendations: what to investigate next
1. **DHS intake outage (now).** Ask DHS and 311 operations what happened to *Homeless Person Assistance* on Aug 7–10. Confirm whether about 480 callers or app users were dropped or misrouted, and add a daily volume alert for low-volume, high-need complaint types.
2. **HPD growth (highest-impact standing issue).** Pull HPD requests by month × channel × borough for 2025–26 and HPD's log of portal or form changes. This will show whether the +40% reflects worse conditions or easier filing. Either way, check HPD's inspection capacity against the higher volume.
3. **Helicopter-noise collapse.** Confirm with EDC and OTI whether the reporting path changed.
4. **Fix the comparison basis.**
   - Map the DEP renames (Water System → Water Maintenance, Sewer → Sewer Maintenance) and the other renames in dashboards so they stop showing as top movers.
   - Compare closure rates at a fixed request age (e.g. closed within 14 days) rather than raw status at pull date.
5. **Data hygiene.** Ask the data owners about the 342 closed-before-created records and the roughly 1.5% likely duplicate submissions.
6. **Confirm the Aug 3, 7 and 20 weather events** so storm days can be flagged automatically in future briefings.

*Assumptions:*
- Baseline counts are taken as published, scaled by calendar days.
- The renamed DEP types are treated as like-for-like, based on identical descriptors.
- No weather, staffing or system-change data was available, so every causal statement above is a hypothesis.
