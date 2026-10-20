# NYC 311 — August 2026 Monthly Briefing

*Source: NYC Open Data "311 Service Requests from 2020 to Present", extract pulled 2026-09-15. The comparisons are against the May–Jul 2026 monthly average ("recent baseline") and against August 2025 ("YoY").*

## Headlines

1. **Volume was normal.** There were **328,701 requests**: 4.2% fewer than July (343,085), 2.4% below the May–Jul average (336,632), and **8.1% more than August 2025** (304,039). That sits in the middle of the last 12 months (302k–349k). Daily volume held steady between 9.2k and 11.7k, with no outage days or gaps.
2. **Housing (HPD) is the main story.** HPD received 56,003 requests. That is **+40% YoY (+15.9k)** and +9% against the recent baseline (+4.7k). It accounts for about two-thirds of the city's whole YoY increase, and every major housing-condition category rose. HPD also holds the largest open backlog (11,673 requests, 21% of its August intake).
3. **The two biggest "movers" in the raw counts are mostly a relabelling, not real change.** DEP's "Water System" and "Sewer" categories (41.7k combined in May–Jul) have zero rows in August. "Water Maintenance" and "Sewer Maintenance" took their place. After mapping the old names to the new ones, the real movement is smaller and was driven by events (see below).
4. **Several large signals come from single addresses or single days.** One address generated 1,119 noise complaints and one building generated 722 cooking-gas complaints. These inflate category trends and need case-level follow-up.
5. **The backlog of unclosed requests is concentrated in a few agencies** (HPD, DPR, DOB, DOHMH, TLC). EDC closed none of its August requests.

## 1. What changed: agencies

| Agency | Aug 2026 | vs May–Jul avg | vs Aug 2025 |
|---|---:|---:|---:|
| NYPD | 149,901 | −9.9k (−6%) | −4.3k (−3%) |
| HPD (housing) | 56,003 | **+4.7k (+9%)** | **+15.9k (+40%)** |
| DSNY (sanitation) | 30,220 | +1.9k (+7%) | flat |
| DOT (transportation) | 23,395 | −0.8k (−3%) | **+6.1k (+35%)** |
| DEP (environment) | 22,233 | −1.3k (−6%) | +3.0k (+15%) |
| DPR (parks) | 15,705 | −3.6k (−18%) | +2.8k (+22%) |
| DOB (buildings) | 12,239 | +1.4k (+13%) | +3.2k (+36%) |
| DHS (homeless services) | 4,188 | −0.6k (−12%) | −1.9k (−31%) |
| EDC (helicopter noise) | 229 | −0.5k (−67%) | −1.6k (−88%) |

- **The NYPD decline against the recent months is seasonal.** It comes from noise and fireworks complaints, which peak earlier in summer: Illegal Fireworks fell from 3.1k/month to 515, Residential Noise fell 9%, and Commercial Noise fell 13%.
- **The DPR decline against the recent months is seasonal tree-storm work.** Damaged Tree fell 28% from the recent average, although it is still +46% YoY.
- **The YoY increase is broad across infrastructure and buildings.** By request count, DOT is +35% (Street Condition +71%, Traffic Signal +30%, Street Light +22%) and DOB is +36% (Building/Use +63%).

## 2. What changed: complaint types

**Biggest increases YoY:** Illegal Parking +4.0k (+8%), Street Condition +4.0k (+71%), Unsanitary Condition +3.8k (+35%), Water Leak +2.4k (+75%), Plumbing +1.9k (+40%), Paint/Plaster +1.8k (+39%), HPD General +1.8k (+67%), Damaged Tree +1.5k (+46%), Blocked Driveway +1.4k, Building/Use +1.3k.

**Biggest increases against the recent months:** Water Leak (+52%), Building/Use (+39%), Obstruction (+30%), Lead (+27%), Street Light (+23%), Unsanitary Condition (+22%), Paint/Plaster (+22%), Rodent (+19%).

**Biggest decreases YoY:** Drug Activity −4.5k (−83%), Residential Noise −2.1k, Helicopter Noise −1.6k (−88%), Street/Sidewalk Noise −1.6k, Lead −1.3k (−46%), Homeless Person Assistance −1.3k (−27%), Traffic −1.1k (−71%), Missed Collection −0.7k (−16%), Derelict Vehicles −0.7k (−19%).
- The Drug Activity and Traffic drops were already present in May–Jul, so they are not new in August. They look like intake or category changes (assumption: probably routing or taxonomy changes, not real declines). They should be confirmed before anyone reports them as trends.

**DEP after mapping the renamed categories (old name + new name combined):**

| | May–Jul avg | Aug 2025 | Aug 2026 |
|---|---:|---:|---:|
| Water (System + Maintenance) | 11,242 | 7,129 | 8,925 (−21% vs recent, +25% YoY) |
| Sewer (Sewer + Maintenance) | 3,938 | 2,479 | 5,060 (+28% vs recent, **+104% YoY**) |

- **The sewer surge happened on specific days.** Requests spiked on Aug 3, 20, 21, 23 and 27, with about 400–520 per day against about 100 normally. Most were Backup, Catch Basin Clogged and Flooding on Street, mainly in **Queens and Brooklyn** (Staten Island on Aug 27). HPD Water Leak spiked on the same days (379 and 462 per day against about 150). I assume these were heavy-rain events; this file has no weather data to confirm it.
- **The water spike was a hydrant cluster.** It ran from Aug 6 to Aug 11, at up to 626 per day. All 2,190 "Fire Hydrant Emergency" requests fall in those six days, spread across the Bronx, Brooklyn and Manhattan. That is consistent with hydrants being opened during a heat wave (assumption).

## 3. Unusual items needing attention

1. **Repeat callers and single buildings** distort the category numbers:
   - **One address in Bensonhurst, Brooklyn (11214): 1,119 "Banging/Pounding" residential-noise complaints**, every day of the month. All were closed by NYPD. This equals about 4% of all citywide residential-noise complaints.
   - **One building in Astoria, Queens (11103): 722 HPD "Cooking Gas" complaints** on all 31 days. This looks like a building that has gone a long time without cooking gas. It alone accounts for about 40% of the YoY increase in HPD "General".
   - **Two Blocked Sidewalk hot-spots (11222 Greenpoint, 970 complaints; 11103 Astoria, 800 complaints)**, plus several others of 300–400. Together they explain a large share of Illegal Parking's +8% YoY.
   - **One address near Times Square/Port Authority (10036): 360 Vehicle Idling Odor complaints.** 258 of them are still "In Progress".
   - **Animal Abuse spiked on Aug 19** (159 against about 30/day), with 111 complaints from four locations in 11210.
2. **HPD's increase is concentrated in the Bronx and central Brooklyn.** HPD's intake is 31% Bronx, against 20% of all 311 requests. The top ZIP codes are 11226 (Flatbush, 2,158 HPD requests), 10458, 10452, 10457 and 10467. Heat/Hot Water complaints in August are also +26% YoY, which is unusual for summer.
3. **Some agencies' requests are not getting closed.** These are the shares of August requests still not closed by Sep 15:
   - EDC: 100% (helicopter noise; none closed)
   - TLC: 82% (For-Hire Vehicle complaints: 1,648 of 1,649 open)
   - DPR: 57% (Overgrown Tree 86% open; Root/Sewer/Sidewalk 99% open)
   - DOHMH: 45% (Food Establishment 93% open)
   - DCWP: 43%
   - DOB: 36%
   - HPD: 21% (11.7k requests)

   NYPD and DSNY are close to 0% and 4%. Citywide, about 10% of requests created in the **first** week of August were still open after about 6 weeks. May–Jul requests were 5.9% unclosed when this extract was pulled. That points to a growing backlog, but newer requests have simply had less time to close, so it is only an indication (see caveats).
4. **Channel mix.** Online grew to 51% of requests (+22% YoY), while phone fell (−11% YoY) and mobile fell (−7% YoY). The "OTHER" channel went from about 600/month to zero, which is probably a recoding. There were no daily breaks, so this is not an outage.
5. **Data quality.** 342 records have a closed date earlier than their created date (334 of them DEP). 1.9% of records lack coordinates and 367 have an "Unspecified" borough (+83% YoY).

## 4. Recommendations / next investigations

1. **HPD surge (highest priority).** Find out whether the +40% YoY rise is real deterioration in housing conditions, a change in how complaints come in (for example, more online filing), or duplicate filings. Check repeat-building counts in 11226 and the West/Central Bronx, and HPD's staffing against its 21% open rate.
2. **Escalate the Astoria cooking-gas building and the Bensonhurst noise address** for case-level resolution. Report these two separately so they do not distort category trends (for example, add a "top repeat locations" line to future briefings).
3. **Confirm the DEP rename with DEP and OTI.** Publish a mapping from old to new categories so trend reports and dashboards don't show false −100% / +1000% moves. Do the same check for Drug Activity, Traffic, Lead and the "OTHER" channel.
4. **Storm response.** Overlay the sewer-backup and water-leak spike days on rainfall data. Target catch-basin cleaning in the Queens and Brooklyn ZIP codes that were hit hardest.
5. **Agencies with zero or near-zero closures.** EDC (helicopter) and TLC (for-hire vehicles) close almost nothing within 6 weeks. Confirm whether those requests are being worked at all, or only not being closed in 311.
6. **Fix the 342 records closed before they were created** (mostly DEP), and the rising number with an unspecified borough.

## Assumptions and caveats

- "Recent baseline" means the May–Jul 2026 total divided by 3.
- **The status comparisons depend on when each request was created.** The August 2025 statuses reflect a full year in which requests could be closed, so YoY status comparisons (for example, "Open" +6,800%) are meaningless. Comparisons with May–Jul are also biased against August, because August requests are newer. A proper backlog trend needs past snapshots or closure-time distributions, which were not provided.
- I did not have weather or event data. The explanations of storm and heat-wave effects are inferences from the timing and descriptors of the requests.
- "Address" means identical latitude/longitude coordinates. I did not identify individual callers.
