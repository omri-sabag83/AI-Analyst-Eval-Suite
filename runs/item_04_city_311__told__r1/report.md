# NYC 311 — August 2026 Monthly Briefing

*Prepared 2026-10-19 from an NYC Open Data extract pulled 2026-09-15.*

## Bottom line

1. **August was a normal month for volume.** There were **328,701 requests (10,603 per day)**. That is 3.4% below the May–July daily rate and 8.1% above August 2025 (304,039). It sits inside the 12-month range of 302k–349k.
2. **The two biggest "movers" are a renaming, not a real change.** "Water System" and "Sewer" fell to **zero**, and "Water Maintenance" (+8,925) and "Sewer Maintenance" (+5,060) appeared in their place. Both are the same DEP request stream under new complaint-type names. Taken together, water and sewer were **451 per day in August vs 495 per day in May–July (−9%)**, which is in line with normal weather-driven variation. This was independently re-checked (see Evidence). **Any dashboard, alert or KPI that filters on the old names is now silently showing zero.**
3. **The real year-on-year growth is in housing and buildings.** HPD (housing) is **+15,925 requests (+40%) vs August 2025** and is now 17.0% of all 311 volume, up from 13.2%. DOB (buildings) is +36%, and DOT (streets) is +35%, led by Street Condition (+71%). These rises are much faster than total volume (+8%).
4. **Several categories collapsed year on year and need an explanation:** Noise – Helicopter −88%, Drug Activity −83% and Traffic −71%. The data can't tell us whether this is a real drop or a change in how these requests are taken in or routed.
5. **Do not read August's open-case figures as a backlog.** 12.3% of August requests were not closed at extract time, against 1.9% for August 2025. That gap is mostly because August 2026 cases had only 15–45 days to close, while August 2025 cases had more than a year.

---

## Data, scope and caveats (read first)

- **What the data covers:**
  - The request file has one row per 311 request created 1–31 August 2026 (328,701 rows, no duplicate keys).
  - The comparison tables give counts by complaint type, borough, agency, channel and status for May–July 2026 combined, August 2025 and August 2026.
  - The monthly totals cover September 2025 to August 2026.
- **The totals tie out.** The August file's row count matches both the monthly total and the August 2026 breakdown total. May + June + July monthly totals (1,009,896) match the baseline total exactly.
- **How comparisons are made:**
  - **Against May–July:** I compare per-day rates (92 days vs 31) so that the three-month period can be compared with one month.
  - **Against August 2025:** I compare raw counts (both months have 31 days).
  - **Seasonality:** May–July is a recent comparison but includes seasonal items. For example, Illegal Fireworks peak around July 4, and tree damage peaks in storm season. August 2025 controls for season but is a year old.
- **Status is right-censored.** Status reflects the 2026-09-15 extract. The share of August requests still open rises steadily with creation date: 9.5% for the 1st–7th, 15.4% for the 22nd–28th. Status comparisons across periods are therefore not like-for-like.
- **Other complaint-type renames:**
  - Hazardous Materials → Hazardous Material
  - Bike/Roller/Skate Chronic → Bike/Roller/Skate
  - A new "Cannabis Retailer" type (OOS agency, 390 requests)
  - The "OTHER" channel has disappeared (1,855 requests in May–July, 0 in August).
- **Record quality issues in the August file:**
  - 342 requests have a closed date earlier than their created date.
  - 5,267 requests are not "Closed" but do have a closed date.
  - 367 requests have borough "Unspecified".
  - None of these is large enough to change the findings, but anyone building time-to-close metrics should handle them.
- **What the data cannot tell us:** I had no weather data, no descriptor-level history before August, and no per-month breakdown inside May–July. Statements about causes below are labelled as hypotheses **[HYP]**. Things computed directly from the data are labelled **[OBS]**.

## 1. Overall volume — normal **[OBS]**

| Period | Requests | Per day |
|---|---|---|
| Aug 2025 | 304,039 | 9,808 |
| May–Jul 2026 (avg month) | 336,632 | 10,977 |
| **Aug 2026** | **328,701** | **10,603** |

- No single day stood out: daily volume ranged from 9,249 to 11,667.
- By borough, every borough was 2–5% below its May–July daily rate.
- Year on year, Brooklyn is the outlier at +18% (+15,601). Other boroughs are +1% to +8%. Brooklyn's rise is consistent with the HPD growth below [HYP: not cross-tabbed against 2025, because 2025 data is only available as one-way totals].

## 2. The water/sewer renaming — the biggest apparent change, and not a real one **[OBS → CON]**

| Complaint type | May–Jul 2026 | Aug 2025 | Aug 2026 |
|---|---|---|---|
| Water System | 31,420 | 7,129 | **0** |
| Sewer | 10,308 | 2,477 | **0** |
| Water Maintenance | 2,306 | 0 | **8,925** |
| Sewer Maintenance | 1,507 | 2 | **5,060** |
| **Combined, per day** | **495** | **310** | **451** |

**Evidence that this is a renaming:**
- 100% of the new types are handled by DEP.
- Their descriptors are the old categories' content. For Water Maintenance: Fire Hydrant Emergency, Leak, Water Main Break, No Water. For Sewer Maintenance: Catch Basin Clogged, Backup, Flooding on Street.
- Old and new names already co-existed in May–July, which points to a switch-over during that window.
- No other complaint type gains enough volume to have absorbed the drop instead.
- DEP's total per-day volume moved only −6.6%.

**Verification.** A separate check by an agent that saw only the claim and the raw files reached **"holds, with caveats"**. It reproduced every count and the 495 → 451 per day comparison. It noted three caveats:
- Old vs new descriptors can't be compared directly before August.
- The −9% might be weather.
- Combined water/sewer is about +46% vs August 2025, which is either real growth or a sign that the old names covered fewer descriptors. This is unresolved.

**Why it matters:** this is the finding with the most operational consequence. Ranked naively, Water System and Sewer are August's largest decliners and Water/Sewer Maintenance its largest risers. Any monitoring keyed on the old names now reports zero.

## 3. What moved most — complaint types and agencies (renaming excluded)

**Agencies vs August 2025 [OBS]**

| Agency | Aug 2025 | Aug 2026 | Change |
|---|---|---|---|
| HPD (housing) | 40,078 | 56,003 | **+15,925 (+40%)** |
| DOT (streets) | 17,321 | 23,395 | +6,074 (+35%) |
| DOB (buildings) | 9,008 | 12,239 | +3,231 (+36%) |
| DEP (environment) | 19,267 | 22,233 | +2,966 (+15%) |
| DPR (parks) | 12,908 | 15,705 | +2,797 (+22%) |
| NYPD | 154,237 | 149,901 | −4,336 (−3%) |
| DHS (homeless services) | 6,083 | 4,188 | −1,895 (−31%) |
| EDC | 1,842 | 229 | −1,613 (−88%) |

- **HPD's growth is broad, not one category:**
  - Unsanitary Condition +3,808
  - Water Leak +2,356 (+75%)
  - Plumbing +1,919
  - Paint/Plaster +1,839
  - General +1,795
  - Door/Window +1,120
  - Elevator +849

  HPD is also +8% per day vs May–July, so the rise continues into the most recent months. A broad rise across housing-condition types looks more like a sustained change in demand or intake [HYP] than a single incident.
- **DOT:** Street Condition is +3,962 (+71%) and Traffic Signal Condition is +1,040.
- **DOB:** Building/Use is +1,287 (+63%).
- **NYPD:** volume is slightly down overall (Noise – Residential −2,134, Street/Sidewalk noise −1,561), while Illegal Parking is +3,973 (+8%).

**Against May–July (per day)**, the declines are mostly seasonal [HYP]:
- Illegal Fireworks −83% (July 4 falls in the baseline)
- HEAT/HOT WATER −41%
- Damaged Tree −29%
- DPR as a whole −19%
- NYPD −7%

## 4. Unusual items that need attention

**a) Unexplained year-on-year collapses [OBS; cause HYP]**

| Complaint type | Aug 2025 | Aug 2026 | Change | Notes |
|---|---|---|---|---|
| Noise – Helicopter (EDC) | 1,842 | 229 | −88% | Also −67% per day vs May–July |
| Drug Activity (NYPD) | 5,447 | 947 | −83% | Already at the August level in May–July, so the drop happened before May |
| Traffic (NYPD) | 1,619 | 474 | −71% | |
| Homeless Person Assistance | 4,646 | 3,396 | −27% | |
| Lead | 2,780 | 1,505 | −46% | |

- Drops this sharp in one category are more often caused by routing, form or category changes than by real changes in conditions [HYP].
- All 229 helicopter requests are still "In Progress", so EDC appears not to close these in 311 at all.

**b) Weather-type event spikes [OBS; cause HYP]**
- **Sewer Maintenance** spiked on **3, 20, 21, 23 and 27 August**, up to 521 per day against a typical ~100. The spikes were Backups, Clogged Catch Basins and Flooding on Street. This pattern is typical of heavy-rain days.
- **Fire-hydrant complaints** roughly tripled on **6–11 August** (340–552 per day vs ~175). This is typical of hydrant opening in a heat wave.
- Both should be confirmed against NWS daily precipitation and temperature.

**c) Channel shift [OBS]**
- Phone is −11% YoY (−8,577) and the mobile app is −7%. Online is +22% (+30,498).
- "UNKNOWN" channel is +32%, but this is not a channel finding. In August, UNKNOWN is essentially all DOB requests (100% of DOB) plus 56% of DOT. It rises because DOB and DOT volume rose.

**d) Open cases (censoring-limited) [OBS]**
- These agencies had the largest shares of August requests still open on 15 September:
  - TLC 82%
  - DPR 57%
  - DOHMH 45%
  - DCWP 43%
  - DOB 36%
  - HPD 21% (11,673 cases, the largest open count)
- HPD's open share climbs from 15% for 1st–7th August to 32% for the last days of the month.
- HPD has the slowest median time-to-close among closed cases (about 9 days). NYPD's is about 1 hour.
- This is a standing pattern, not something new in August. A backlog judgment needs an age-matched comparison.

## Recommendations — what to investigate next

1. **Fix monitoring for the renaming (immediate).** Map Water System → Water Maintenance and Sewer → Sewer Maintenance, plus the minor renames, in all dashboards and alerts. Ask DEP / 311 for the change date and the descriptor mapping. Then confirm whether combined water/sewer really is up about 46% vs August 2025.
2. **Investigate HPD's +40% year on year.** Pull monthly HPD volume by complaint type and borough for the past 24 months. Determine whether the growth comes from more housing problems, more online reporting (HPD is 58% online), or policy/outreach changes. Check whether HPD's close times are keeping up.
3. **Ask EDC, NYPD and DHS to explain the collapses** in Helicopter noise, Drug Activity, Traffic and Homeless Person Assistance. Specifically, check for routing to other systems or category retirements.
4. **Replace the open-status comparison with a like-for-like one.** Compare each month's share closed within 14 and 30 days of creation, measured at the same age. Pull August 2025 statuses as of mid-September 2025 if archived snapshots exist.
5. **Confirm the weather hypotheses** by matching NWS rain and heat data to the 3/20/21/23/27 August sewer spikes and the 6–11 August hydrant spike.
6. **Data hygiene:** ask the data owner about the 342 cases closed before they were created and the 5,267 non-closed cases that have a closed date.
