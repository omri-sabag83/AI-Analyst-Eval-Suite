# NYC 311 — August 2026 Monthly Briefing

*Data: NYC Open Data "311 Service Requests from 2020 to Present", pulled 2026-09-15. Comparisons are against the May–July 2026 monthly average (the "recent baseline") and against August 2025 (year over year, or YoY).*

## Bottom line

1. **Overall volume was normal.** There were **328,701 requests**. That is −4.2% vs July, −2.4% vs the May–July average (336,632) and **+8.1% YoY** (304,039). It falls in the middle of the last 12 months, which ranged from 302k to 349k.
2. **Housing (HPD) is the biggest story.** HPD received **56,003 requests**, +9% vs the recent baseline and **+40% YoY (+15,900)**. That gain is about two-thirds of the city's entire YoY increase. The rise is spread across apartment-condition complaints, not tied to the season.
3. **DEP's water and sewer numbers are not comparable month to month.** "Water System" and "Sewer" fell to zero and were replaced by "Water Maintenance" and "Sewer Maintenance". Without adjusting for this, DEP's categories show false swings of −100% and +1,000%.
4. **Two problems in how requests were captured need follow-up.** (a) *Homeless Person Assistance* requests almost stopped on **Aug 7–10**: 2, 2, 2 and 15 per day against a typical ~119. (b) On **Aug 19**, 111 *Animal-Abuse* complaints came from one Brooklyn location (ZIP 11210) in a few hours.
5. **Several storm-like surges hit drainage.** Sewer complaints ran 3–4× normal on Aug 3, 20, 21 and 23, mostly in Queens and Brooklyn.

## 1. What happened in August

| | Aug 2026 | vs May–Jul avg | vs Aug 2025 |
|---|---|---|---|
| Total requests | 328,701 | −2.4% | +8.1% |
| NYPD | 149,901 (45.6%) | −6.2% | −2.8% |
| HPD | 56,003 (17.0%) | **+9.1%** | **+39.7%** |
| DSNY | 30,220 | +6.7% | −0.4% |
| DOT | 23,395 | −3.1% | **+35.1%** |
| DEP | 22,233 | −5.6% | +15.4% |
| DPR (Parks) | 15,705 | **−18.5%** | +21.7% |
| DOB | 12,239 | **+13.1%** | **+35.9%** |
| DHS | 4,188 | −12.2% | **−31.2%** |
| EDC | 229 | −66.5% | −87.6% |

The top complaint types were Illegal Parking (51,216), Noise – Residential (30,622), Noise – Street/Sidewalk (23,644), Unsanitary Condition (14,650) and Blocked Driveway (14,636).

By borough, every borough was 1–4% below the recent baseline. Year over year, **Brooklyn was up 17.7% (+15,600)**, while Queens was flat (+0.6%). Brooklyn accounts for most of the citywide YoY increase. The baseline file has no borough × agency cross-tab, so I could not break the Brooklyn increase down by agency for 2025.

## 2. What moved the most

### Rising
- **HPD housing conditions (largest, most persistent).** These complaint types rose against both comparisons:

  | Complaint type | Aug 2026 | vs May–Jul avg | vs Aug 2025 |
  |---|---|---|---|
  | Unsanitary Condition | 14,650 | +22% | +35% |
  | Water Leak | 5,481 | +52% | +75% |
  | Paint/Plaster | 6,604 | +22% | +39% |
  | General | 4,479 | +17% | +67% |
  | Plumbing | 6,666 | −3% | +40% |

  Requests are concentrated in Brooklyn (17.5k) and the Bronx (17.3k). Housing complaints normally fall in summer, so rising volume in August points to a real increase in demand or a change in intake. Seasonality does not explain it.
- **DOB Building/Use:** 3,336 (+39% vs baseline, +63% YoY).
- **DOT Street Condition:** 9,552, +71% YoY, mostly potholes (4,292) and cave-ins (2,776). It is slightly below the early-summer baseline, so this is a year-over-year rise, not a new August surge.
- **DSNY:** up 6.7% vs baseline. Dirty Condition (+12%), Illegal Dumping (+11%) and Rodent (+19%) all rose.

### Falling
- **Seasonal declines, expected:** Illegal Fireworks (−83% vs the July-heavy baseline; flat YoY), Heat/Hot Water (−40%), Noise – Residential (−9%) and Damaged Tree (−28%). These do not need action.
- **DHS −31% YoY:** Homeless Person Assistance fell from 4,646 to 3,396. About 450 of the missing requests come from the Aug 7–10 gap in Section 3.
- **Big YoY drops that probably reflect unusual months in 2025:** Drug Activity (947 vs 5,447), Noise – Helicopter / EDC (229 vs 1,842), Traffic (474 vs 1,619) and Lead (1,505 vs 2,780). Drug Activity and Helicopter are close to their recent baseline (+11% and −67%), which suggests August 2025 was the outlier.

### Channel shift
Online made up **50.8%** of requests, up from 47.2% in the baseline and 44.9% a year ago. Phone fell 9% and the mobile app fell 11% vs the baseline. The "OTHER" channel (~618/month) dropped to zero, which is probably a recoding. HPD relies heavily on online and phone (32k and 23k), so channel mix and the HPD rise may be linked.

## 3. Unusual: needs attention

**A. Homeless Person Assistance intake gap, Aug 7–10.**

| | Aug 4 | Aug 5 | Aug 6 | **Aug 7** | **Aug 8** | **Aug 9** | **Aug 10** | Aug 11 |
|---|---|---|---|---|---|---|---|---|
| Homeless Person Assistance | 132 | 161 | 86 | **2** | **2** | **2** | **15** | 148 |
| Encampment (also DHS) | 33 | 34 | 27 | 28 | 21 | 18 | 34 | 35 |

The drop happened across all channels: phone, online and app. Encampment requests, which also go to DHS, kept flowing. A real fall in need would not look like this; a routing, form or system failure would. About **450 requests are likely missing** (4 days × ~119 median − 21 received). A homeless outreach request that was never logged may have gone unanswered.

**B. DEP category change.** Here is how the old and new categories compare:

| Category | May–Jul monthly avg | August 2026 |
|---|---|---|
| Water System + Water Maintenance | 11,242 | 8,925 (**−21%**) |
| Sewer + Sewer Maintenance | 3,938 | 5,060 (**+28%**) |

The new categories' descriptors (fire hydrant, leak, water main break; catch basin, backup, flooding) match the old ones. The baseline already contains some "Maintenance" records, so the switch probably happened partway through May–July. **Hazardous Materials** (~203/month) also dropped to zero, and I could not tell where those requests went. Any DEP trend reporting needs to map old categories to new ones first.

**C. Storm-driven drainage surges.** Sewer Maintenance requests normally run about 122 per day. On the surge days they were:

| Day | Sewer Maintenance requests |
|---|---|
| Aug 3 | 486 |
| Aug 20 | 521 |
| Aug 21 | 411 |
| Aug 23 | 448 |

These were mostly Backup, Clogged Catch Basin and Flooding on Street, concentrated in Queens and Brooklyn. Damaged Tree also spiked on Aug 3 and 21. Staten Island had its own spike on Aug 27 (106 that day vs ~10–20 normally). *Assumption:* these are rain events. There is no weather data in this folder, so that is not confirmed.

**D. Animal-Abuse cluster, Aug 19.** There were 159 requests that day against a median of 30. Of these, 111 came from ZIP 11210 (Brooklyn), about 96 from essentially the same coordinates (40.639, −73.947), mostly between 4 pm and 11 pm. This is almost certainly a single incident reported many times over, or an organised reporting campaign. It should be handled as one case, and it inflates August's Animal-Abuse count.

**E. Data quality notes.**
- **Status and closure numbers for August are not comparable to earlier periods.** The data was pulled 15 days after month-end, so 12.3% of August requests were still open, against 5.9% for the baseline and 1.9% for August 2025. That difference is mostly the shorter time to close. Still, some agencies stand out:
  - All 229 EDC requests were still open.
  - 82% of TLC requests were still open.
  - DPR (57%) and DOHMH (45%) also had high open shares.
  - HPD's median time to close was about 9 days (219 hours).
- 342 records have a closed date before their created date.
- Agency code OOS appears in 2026 with 390 requests but had none in August 2025.

## 4. Recommendations: what to investigate next

1. **HPD surge (highest priority).** Find out why housing-condition complaints are up 40% YoY and rising in summer. Steps:
   - Split by building and community board to see whether a small number of buildings or landlords are driving it.
   - Check for repeat complaints from the same units.
   - Check for HPD policy or outreach changes and any online-form changes.
   - Watch HPD time to close, since the backlog risk grows heading into heat season (October).
2. **DHS intake outage, Aug 7–10.** Confirm with DHS and the 311 technology team whether Homeless Person Assistance routing failed. Recover or re-contact any lost requests, and add a daily alert when a high-volume complaint type falls far below normal.
3. **DEP taxonomy.** Get the official mapping from old to new categories, including Hazardous Materials, and the date it took effect. Restate historical trends on the new basis. Then check whether the −21% in water complaints is real.
4. **Brooklyn +18% YoY.** Run a borough × agency comparison for August 2025 against August 2026, which the provided summaries do not allow, to confirm how much of this is HPD.
5. **Channel shift.** Check whether phone and app declines reflect call-centre capacity or wait times, or an app problem, rather than a change in what residents prefer.
6. **Storm response.** Pull weather records for Aug 3, 20, 21, 23 and 27. Check how quickly DEP closed the flooding and catch-basin requests on those days.
7. **Open-request follow-up.** Re-pull the data in about 30 days and compare closure rates fairly. In the meantime, check EDC (100% open) and TLC (82% open) now.

## Assumptions and method
- The May–July baseline is the combined three-month count divided by 3. Percentage changes for very small categories (under ~100 per month) are not discussed.
- Daily anomalies were flagged by comparing each complaint type's daily count to its own August median, using a robust z-score (median absolute deviation). Only types with more than 300 requests in the month were screened.
- I had no weather, staffing or policy data, so explanations for storms, outages and recodings are hypotheses to verify.
