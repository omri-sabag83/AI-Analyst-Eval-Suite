# NYC 311 — August 2026 Monthly Briefing

*Data: NYC Open Data "311 Service Requests from 2020 to Present", pulled 2026-09-15. Comparisons use the May–July 2026 average ("recent baseline") and August 2025 ("last year"). All baseline comparisons are scaled to a 31-day month, because May–July has 92 days.*

## Headline

- **Overall volume was normal.** There were **328,701 requests** in August, or 10,603 a day. That is **3% below the May–July daily rate** and **8% above August 2025** (304,039). It sits in the middle of the last 12 months, where the range was 10,073–11,953 a day. Daily counts stayed between 9,249 and 11,667, with no gaps or outage days.
- **The biggest real change is housing (HPD).** HPD requests rose **8% on the recent baseline and 40% on last year** (56,003 vs 40,078; +15.9k). This happened even though heating complaints fell seasonally. It is the largest increase of any agency, and it is broad-based.
- **The biggest *apparent* changes are not real.** DEP renamed its complaint types: "Water System" and "Sewer" became "Water Maintenance" and "Sewer Maintenance". As a result, the old types show −100% and the new ones +900–1,000%. **Any dashboard tracking these types by name is now broken.**
- **One Astoria building produced 929 HPD requests,** 722 of them about *cooking gas*. Every one of them was filed online. This needs a look today: either tenants lack gas, or the online channel is being used to flood the system.
- **Do not read the "open" counts as a backlog yet.** 12% of August requests were still not closed when the data was pulled. That share rises steadily with how recent the request is, so it is mostly a timing effect.

## 1. What changed, and which changes are real

### Agencies (requests per 31-day month)

| Agency | Aug 2026 | vs May–Jul | vs Aug 2025 | Read |
|---|---:|---:|---:|---|
| NYPD | 149,901 | −11.6k (−7%) | −4.3k (−3%) | Mostly seasonal: the July fireworks peak passed, and summer noise and parking eased |
| **HPD** | **56,003** | **+4.1k (+8%)** | **+15.9k (+40%)** | **Real increase. See §2** |
| DSNY | 30,220 | +1.6k (+6%) | flat | Normal |
| DOT | 23,395 | −1.0k (−4%) | +6.1k (+35%) | Street Condition is up 71% YoY (+4.0k) but down 14% on the summer level |
| DEP | 22,233 | −1.6k (−7%) | +3.0k (+15%) | Taxonomy change. See §3 |
| DPR | 15,705 | −3.8k (−19%) | +2.8k (+22%) | Tree complaints falling from an early-summer peak (Damaged Tree −1.9k) |
| DOB | 12,239 | +1.3k (+12%) | +3.2k (+36%) | Building/Use is +37% on the baseline and +63% YoY |
| DHS | 4,188 | flat | −1.9k (−31%) | The fall happened before this summer, not in August |
| EDC | 229 | −0.5k (−67%) | −1.6k (−88%) | Helicopter noise. All 229 requests are still open |

### Complaint types: the largest real movers
- **Up on both comparisons (worth watching):** HPD *Unsanitary Condition* (+21% on baseline / +35% YoY), *Water Leak* (+50% / +75%), *Paint/Plaster* (+21% / +39%), DOB *Building/Use* (+37% / +63%), DOT *Street Light Condition* (+21% / +22%), *Obstruction* (+28% / +30%), *Rodent* (+17% / −4%).
- **Down from the summer, but seasonal:** *Illegal Fireworks* (3,085 → 515), *Noise – Residential* (−10%), *Illegal Parking* (−6%), HPD *Heat/Hot Water* (−41%; still +26% YoY).
- **Down YoY, but the fall happened before August:** *Drug Activity* (5,447 → 947, −83% YoY), but August is level with the May–July rate (861). *Homeless Person Assistance* and *Traffic* follow the same pattern. These look like intake or routing changes made earlier in the year. They are not August events.

## 2. Housing complaints are rising (HPD)

- HPD rose +8% on the summer baseline even though *Heat/Hot Water* fell by 2.6k. **Without heat complaints, HPD is up about 15%.** The increase comes from habitability complaints: unsanitary conditions (+2.5k), water leaks (+1.8k) and paint/plaster (+1.1k).
- The increase is broad, not driven by one place. The top 100 locations account for only about 10% of HPD volume, spread over 12.6k distinct locations. HPD requests are concentrated in the Bronx (31% of HPD vs 20% of all 311) and Northern Manhattan (CB 10 and CB 12).
- HPD has the slowest closure of any agency: the median closed request took **9.1 days**, against 0.1 days for NYPD and 0.7 days for DEP. 11,673 HPD requests (21%) were still open at the pull date. Higher volume plus slow closure is where a real backlog would form first.

## 3. Data and definition changes that will distort the numbers

1. **DEP complaint types were renamed.** *Water System* (31,420 in May–Jul) and *Sewer* (10,308) dropped to zero in August. *Water Maintenance* (8,925) and *Sewer Maintenance* (5,060) replaced them, keeping the same descriptors (hydrants, catch basins, sewer backups, water main breaks). Small volumes under the new names already appeared in May–July (2,306 and 1,507), so the switch was probably phased in. *Hazardous Materials* was likewise renamed *Hazardous Material*.
   - On a like-for-like basis (old and new names combined), DEP water and sewer requests were **13,985 in August: −9% on the summer level and +46% on August 2025** (9,608). The YoY rise is real and deserves its own look. It may reflect a stormy summer, but that cannot be verified from this data.
2. **The "OTHER" intake channel disappeared.** It carried about 625 requests a month in May–July, none in August, and about 1 in August 2025. It was a short-lived label and is not material.
3. **Online keeps gaining share.** Online requests were 51% of the total in August (+22% YoY), while phone fell 11% YoY and mobile fell 7%. DOT records 56% of its requests with an "UNKNOWN" channel, so channel analysis for DOT is unreliable.
4. **Timestamps:** 342 requests, almost all DEP, have a closed date *before* the created date. Most are seconds apart (median 15 s), so this is a minor system artifact.
5. **Open/In-Progress counts are biased by timing.** The share not yet closed rises steadily with creation date, from 6% for Aug 1–2 to 15% for the last full week. The baseline months had longer to close before the pull. So the jump in "Open" (16.9k vs about 4.7k a month in the baseline) is mostly a timing effect, **not evidence of a backlog**. Re-check after a longer settling period.

## 4. Anomalies that need attention

| Location | What | Why it matters |
|---|---|---|
| **Single building, Astoria, Queens (ZIP 11103, CB 1)** | 929 HPD requests (722 *Cooking Gas*, plus Water Supply and Garbage), plus 174 DOHMH rodent complaints at the same point. **All online.** Filed every day of the month, with a peak of 108 on Aug 18, often at 4–6 am. | Either a large complex has been without cooking gas for a month (a tenant-safety issue), or this is automated or bulk submission. Either way, 1,123 requests from one point inflate HPD and DOHMH figures by about 2%. |
| Jamaica, Queens (ZIP 11432) | 210 HPD requests from one building, in bursts (74 on Aug 16). Mixed issues: power outage, gas range, mold. | Possible building-wide failure. |
| Gravesend/Bensonhurst, Brooklyn (one point) | 1,119 *Noise – Residential* requests | Likely a single repeat caller. This inflates the noise statistics. |
| EDC helicopter noise | All 229 requests still open; volume is −88% YoY | Possibly a change in intake or routing. Confirm the requests are actually being worked. |

## 5. Recommendations and what to investigate next

1. **Today:** have HPD confirm the status of the Astoria building (11103) and the Jamaica building (11432). If there is a gas outage, escalate it. If the submissions are automated, ask DoITT/OTI to review rate limits on the online channel.
2. **Fix reporting** for the DEP rename. Map *Water System → Water Maintenance*, *Sewer → Sewer Maintenance* and *Hazardous Materials → Hazardous Material* in every trend dashboard before the September briefing. Then explain the +46% YoY rise in water and sewer requests.
3. **HPD capacity:** habitability complaints are up 35–75% YoY, and requests take 9 days to close. Review HPD inspection staffing ahead of heating season, which starts on Oct 1 and historically adds the largest HPD load.
4. **Explain the earlier step-changes** in *Drug Activity* (−83%), *Homeless Person Assistance* (−27%) and *Traffic* (−71%) YoY. Determine whether these were policy or routing changes or a real drop in need.
5. **Re-measure the open backlog** with a fixed age cut-off, for example the share still open 30 days after creation, compared across months. This avoids the timing bias described in §3.5.
6. **Add repeat-location flags** (for example, more than 100 requests per location per month) to the monthly pipeline so that clusters like these are separated from genuine citywide trends.

## Assumptions and limitations
- Baseline and YoY figures come from the pre-aggregated file. I cross-checked the request-level file against it: August totals and May–July totals reconcile exactly with `monthly_totals.csv`.
- The baselines are not broken down by agency and complaint type together, or by location. So complaint types are attributed to the agency that handles most of them in August, and I cannot test whether the Astoria cluster existed before August.
- "Seasonal" judgements rest on comparing with both the summer baseline and August 2025. Only one prior August is available, so this is indicative only.
- Requests are counted by creation date. Location is the reported latitude/longitude, which for HPD normally means one building address.
