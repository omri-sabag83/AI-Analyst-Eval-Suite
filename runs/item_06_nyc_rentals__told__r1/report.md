# NYC short-term rental market entry: what the Airbnb listings data says

## Bottom line

1. **Half of NYC listings are not really operating.** Only 49% had a guest review in the six months before the snapshot. Supply is much thinner than the 48,895 headline count suggests: about 24,000 listings are active.
2. **What most separates listings that perform well from those that don't is how they are operated. Location and price matter much less.** Listings from hosts who run 2–20 listings are active 61–71% of the time, against 43% for single-listing hosts. The gap holds within every borough and room type, and after controlling for price, minimum stay and listing age (an independent re-check confirmed this, with one caveat below). Within a segment, price matters little except at the top: the most expensive fifth of each borough × room-type segment is less likely to be active.
3. **Manhattan entire homes have the highest revenue potential but the weakest activity.** Outer-borough listings are more often active and get more reviews per month, but they earn less per listing.
4. **The biggest risk is regulatory, not commercial.** 46% of all listings, and 88% of entire-home listings, are entire homes offered for stays under 30 nights. Under New York law this is generally not allowed. The data is also from mid-2019, and enforcement has tightened a lot since then (see Risks). **Any entry plan has to be built on what is legal: 30+ night rentals, or hosted private rooms.** It should not copy the configuration that dominates this 2019 file.

## Data and method (read first)

- **Grain and coverage:** one row per listing; 48,895 listings, 37,457 hosts, 5 boroughs, 221 neighbourhoods. It is a **single snapshot**. The latest review date is 2019-07-08, so I treat that as the snapshot date. The data is therefore about 7 years old, and nothing here measures trends.
- **There is no booking, occupancy or revenue field.** "Performance" has to be inferred from reviews. I use three proxies:
  - **Active:** last review within 180 days of the snapshot. This is my own definition; I tested 90 and 365 days and the conclusions don't change.
  - **Reviews per month among active listings:** a demand-intensity measure.
  - **Revenue estimate (an estimate, not measured):** price × estimated nights. Estimated nights = reviews per month ÷ 0.5 (assuming half of stays leave a review) × the larger of minimum nights and 3, capped at 21 nights a month. Dormant listings are counted as zero.
- **Data quality:**
  - 11 listings are priced at $0 and 239 above $1,000 (up to $10,000). I excluded these 250, leaving 48,645.
  - 10,052 listings (21%) have never been reviewed, so reviews per month is blank for them. They may be new rather than failing, so I used `id` (assigned roughly in creation order) as an age proxy. The newest 10% of listings are 52% never-reviewed.
  - `availability_365 = 0` (36% of listings) is ambiguous: it could mean fully booked or blocked/inactive. 69% of dormant listings show 0, so I read it mostly as "switched off" and did not use it as a performance measure.
  - Reviews understate activity for long stays: a 30-night guest leaves at most one review a month. This biases review-based measures against long-stay listings (see Finding 3).

## Findings

### 1. Half the market is inactive [OBS]
| Status | Share of listings |
|---|---|
| Active (reviewed in last 6 months) | 49% |
| Dormant (last review more than 6 months ago) | 30% |
| Never reviewed | 21% |

This is a within-sample figure based on my activity definition. Delisted listings are not in the file at all, so the true inactive share in the market may be higher. Implication [CON]: competition for bookings comes from roughly 24k active listings, not 49k. But a large dormant pool could come back into supply.

### 2. Host operating scale is the strongest differentiator [CON, independently verified with caveat]
| Host's listing count | Listings | Active rate | Median price |
|---|---|---|---|
| 1 | 32,135 | 43% | $117 |
| 2 | 6,634 | 62% | $90 |
| 3–5 | 5,121 | 71% | $79 |
| 6–20 | 2,552 | 64% | $81 |
| 21+ (e.g., Sonder, Blueground) | 2,203 | 35% | $189 |

- **Adjusted effect:** in a logistic regression controlling for borough, room type, minimum-stay band and within-segment price quintile, the odds of being active are 2.2× higher for 2-listing hosts and 3.5–3.8× higher for 3–20-listing hosts than for single-listing hosts.
- **Independent re-check:** a separate check that never saw my reasoning reproduced the gap (43.4% vs 65.3%). It held in every room type and borough, under 90- and 365-day windows, among reviewed-only listings, and with an id-decile age control (odds ratios 2.2–3.6). It is not driven by a few big hosts: the top 10 hosts in the 2–20 group hold only 1.3% of that group's listings.
- **Caveat:** the advantage disappears among the newest ~10% of listings, where single-listing hosts are level or slightly ahead.
- **The 21+ group:** its low raw rate mostly reflects corporate operators with 30+ night minimums (68% of their listings) and a pipeline of new, not-yet-reviewed units (45% never reviewed). After controlling for age it is not significantly different from single hosts. There are only 38 hosts in this group, so treat it with care.
- **Why this might be [HYP]:** a large share of single-listing hosts are hobbyists who list a home once and let it lapse, while small professional operators keep calendars, pricing and responses up to date. The causation could also run the other way: hosts who do well go on to add listings. Settling this needs data the file lacks, such as host tenure, response rates and repeated snapshots.
- **What this means for the company [CON]:** a professionally managed portfolio competes mainly against a large, weakly operated amateur base. Execution quality is a real, exploitable edge.

### 3. Minimum stay: short stays get more reviews, but this is partly a measurement artefact [OBS + caution]
| Minimum nights | Listings | Active rate | Median reviews/month (active) | Median implied nights/month (reviewed listings)* |
|---|---|---|---|---|
| 1 | 12,617 | 52% | 2.41 | 3.7 |
| 2 | 11,667 | 60% | 1.94 | 3.3 |
| 3 | 7,977 | 55% | 1.46 | 2.3 |
| 4–6 | 7,067 | 45% | 1.06 | 2.1 |
| 7–29 | 4,866 | 31% | 0.62 | 2.9 |
| 30 | 3,730 | 33% | 0.40 | 7.5 |

*Reviews/month × the larger of minimum nights and 3; it does not depend on any review-rate assumption.

- **Activity:** listings with 1–3 night minimums are far more often active (adjusted odds ratio for 30 nights vs 2 nights: 0.22).
- **Nights sold:** among listings that do get reviewed, 30-night listings imply *more* nights sold per month, because each stay is long. So "long minimums perform badly" holds for *whether a listing is in use*. It does not hold for *nights sold once it is in use*. Two- to three-night minimums are the sweet spot among short-stay listings.

### 4. Location: Manhattan earns more per listing; outer boroughs are more often active [OBS]
| Borough | Listings | Active rate | Median price | Reviews/month (active) | Mean est. revenue/month |
|---|---|---|---|---|---|
| Manhattan | 21,488 | 46% | $149 | 1.43 | ~$1,000 (~$830 under the alternative assumption) |
| Brooklyn | 20,041 | 50% | $90 | 1.50 | ~$690 |
| Queens | 5,656 | 59% | $75 | 1.99 | ~$690 |
| Staten Island | 371 | 70% | $75 | 1.79 | ~$720 |
| Bronx | 1,089 | 62% | $65 | 1.94 | ~$610 |

- **Top neighbourhoods for entire homes** (at least 100 listings, estimated mean revenue per month): Financial District (~$1,800), Hell's Kitchen (~$1,730) and SoHo (~$1,630). Flushing in Queens (~$1,530) and East Harlem (~$1,390) combine high activity with lower prices.
- **Weakest neighbourhoods:** Kensington, Midwood, Morningside Heights and Inwood (~$330–$400 per month).
- **Sensitivity:** the ranking (Manhattan first, entire homes about 2.4× private rooms) holds when I drop the minimum-night multiplier from the revenue estimate. Revenue figures are estimates and are useful for *ranking*, not budgeting.
- **Supply:** Manhattan and Brooklyn hold 85% of supply, so they are the most competitive markets.

### 5. Price positioning: avoid the top of the segment [OBS]
Within each borough × room-type segment:
- **Top price quintile:** less likely to be active (adjusted odds ratio 0.74 vs the middle quintile) and about 16% fewer reviews per month when active.
- **Bottom quintile:** also slightly less active (odds ratio 0.87).
- **Middle quintiles:** perform best. Underpricing does not buy much extra demand.

The models explain only part of the variation (pseudo-R² 0.07 for activity; R² 0.21 for reviews per month). Most of the performance difference between listings comes from things this file doesn't record: photos, reviews, amenities, host responsiveness.

## Risks
- **Regulatory (highest).** Most of this market's activity in 2019 came from entire homes rented for under 30 nights (46% of all listings). New York State's Multiple Dwelling Law generally prohibits this in most buildings. I also understand from general knowledge (not from this data, and to be checked with counsel) that NYC's Local Law 18 has required host registration since 2023 and has sharply reduced short-stay listings. **This file therefore probably overstates today's legal short-stay supply and demand.**
- **Stale data.** The snapshot is from 2019, before COVID-19 and the regulatory changes, so all levels should be re-measured on a current extract.
- **Concentration and competition.** 34% of listings belong to multi-listing hosts. Well-funded operators (Sonder 327 listings, Blueground 232) already focus on 30+ night stays, which is the legal segment.
- **Measurement.** Every performance metric here is a review-based proxy. There is no observed occupancy or revenue.

## Recommendations
1. **Get current, richer data before committing capital.** That means a recent listings extract, calendar/occupancy data and actual revenue (for example, from a data vendor or the company's own existing NYC units). Get a legal review of the current registration and 30-day rules.
2. **Design the offer around what is legal:**
   - **Furnished 30+ night stays:** where long-stay listings are in use they sell more nights per month, and corporate operators already validate the model.
   - **Hosted private rooms**, where permitted.
   - **Do not build a portfolio of short-stay entire homes.**
3. **Compete on operations.** The clearest performance gap in the data is between actively managed and neglected listings. Professional calendar management, pricing in the middle of the segment, and fast onboarding to first reviews are the levers.
4. **Location:**
   - **For yield:** target central Manhattan (Financial District, Hell's Kitchen, SoHo/Lower East Side).
   - **For activity at lower cost:** test high-activity, lower-cost areas such as Flushing, East Harlem and western Queens/Bronx.
   - **Validate first:** confirm these on current data before scaling.
5. **Use the dormant pool as an opportunity.** About 15,000 dormant listings suggest owners with under-used units. These are potential management or master-lease partners, subject to the same legal constraints.

## Notes on process
- **Rigor check:** a rigor checklist was run on the draft. It led to the age control, the review-rate-neutral nights measure, the alternative activity windows and the revenue sensitivity check.
- **Independent verification:** the host-scale finding was checked by a separate process that saw only the data. Verdict: holds, with the caveat that the gap disappears among the newest ~10% of listings.
- **No root-cause investigation:** the brief asks about market structure, not a change or incident, so a root-cause investigation was not needed.
