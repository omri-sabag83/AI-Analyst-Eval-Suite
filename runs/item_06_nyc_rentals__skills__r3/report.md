# NYC Short-Term Rental Market Entry: What the Airbnb Listing Data Shows

**Data:** `listings.csv`, 48,895 NYC Airbnb listings. The latest review date is 8 Jul 2019, so I treat the file as a mid-2019 snapshot. It has no duplicate IDs. 11 listings have price $0 and 26 have price ≥ $5,000. I excluded both groups from the price analysis.

## Bottom line

1. **The file contains no bookings, occupancy or revenue, so "performance" can only be estimated.** I use **reviews per month** as a demand proxy. For revenue I use a rough estimate: reviews/month ÷ 0.5 review rate × assumed stay length (the greater of the minimum nights or 3), capped at 70% occupancy, × price. All revenue figures below come from this model. They are estimates, not observed results.
2. **Much of the listed supply is not really operating.** Only **60%** of listings had a review in the last 12 months. **21%** have never been reviewed and **20%** have gone quiet for more than 12 months. Raw listing counts therefore overstate competition by about 40%.
3. **What separates strong listings from weak ones is mostly how they are run, not where they are.** Once room type is held fixed, the borough adds almost nothing. The factors that matter are short minimum stays, a calendar that is actually open, and a price close to the local median.
4. **Regulation is the biggest risk.** 46% of all listings are entire homes offered for stays under 30 nights. That is the segment New York State and City law restricts (see Risks). The large professional operators in the data have mostly moved to stays of 30 nights or more.

## 1. The market

| Borough | Listings | Share active (review ≤12m) | Median price (all listings) |
|---|---|---|---|
| Manhattan | 21,661 | 55% | $150 |
| Brooklyn | 20,104 | 61% | $90 |
| Queens | 5,666 | 68% | $75 |
| Bronx | 1,091 | 72% | $65 |
| Staten Island | 373 | 80% | $75 |

- Manhattan and Brooklyn hold **85%** of supply. Five neighbourhoods account for 30% of all listings: Williamsburg, Bedford-Stuyvesant, Harlem, Bushwick and the Upper West Side.
- By room type, 52% are entire homes (median $160), 46% are private rooms ($70) and 2% are shared rooms ($45).
- **Hosts:** 66% of listings come from single-listing hosts. A small professional tier of hosts with 21 or more listings controls 4.5% of supply; examples are Sonder (327 + 96 listings), Blueground (232) and Corporate Housing (91). In that tier, **78% are entire homes, the median minimum stay is 30 nights, and 45% of listings have never been reviewed.** These are effectively monthly furnished rentals.

## 2. What differentiates strong and weak performers

**Method.** I used only the 29,152 active listings. Within each borough × room-type group I ranked listings by reviews/month, then compared the top quartile with the bottom quartile. Ranking inside each group keeps the comparison from simply reflecting the mix of locations and room types. I also fit a regression of log(reviews/month) on borough, room type, price relative to the neighbourhood median, minimum-nights band, availability band and host size (R² = 0.28, robust standard errors).

| Characteristic (median or share) | Bottom quartile | Top quartile |
|---|---|---|
| Minimum nights (median) | 4 | 2 |
| Share with 1-night minimum | 14% | 42% |
| Share with 30+ night minimum | 17% | 1% |
| Days available in next year (median) | 63 | 133 |
| Price ÷ neighbourhood median for same room type | 0.97 | 1.00 |
| Listing from a host with 21+ listings | 7.2% | 1.2% |

**Findings, roughly in order of strength:**

- **Minimum stay is the strongest differentiator.** Holding everything else in the regression constant, reviews/month fall steadily as the minimum stay rises: about −19% at 2 nights, −38% at 3 nights, −55% at 4–6 nights and −79% at 30+ nights, all compared with a 1-night minimum. *Caveat:* guests leave roughly one review per stay, not per night. Longer stays therefore mechanically produce fewer reviews, and part of this gap is an artefact of the measure. In fact my revenue estimate puts 30+ night listings highest (median about $1,710/month), but that figure depends almost entirely on the assumption that every stay lasts the full minimum. Treat it as unproven.
- **The calendar has to be open.** Listings with 0 days of availability get 50% fewer reviews per month than those with 1–30 days open, and those with 91–270 days open do best. Zero availability usually means the host has blocked the calendar or paused the listing; it does not mean the listing is fully booked. Listings open almost all year (271–365 days) perform worse than those open 91–270 days. This suggests unsold inventory rather than a sign of success.
- **Pricing near the local median maximises demand, and a premium costs little.** Reviews/month peak at 0.9–1.3× the neighbourhood median for the same room type. Listings priced well below the median (<0.7×) actually do *worse*, which probably reflects lower quality. The regression gives a demand elasticity of only about −0.2 with respect to relative price, and within-group correlations between price and reviews are close to zero (|ρ| ≤ 0.2 for entire homes and private rooms). The revenue estimate therefore rises with price: about $1,010/month at the median price versus about $1,430 at 1.3–2× the median. This points to room to price above the median for well-presented units.
- **Host scale:** listings from hosts with 2–5 listings beat single-listing hosts by about 9–11%, which is consistent with more professional operation. Hosts with 21 or more listings do 33% *worse* on reviews, but this is largely because of their 30-night business model.
- **Location matters more for price than for demand.** Once room type is held fixed, borough effects on reviews/month are small and not significant (|coef| < 0.07, p > 0.08). Manhattan's advantage is price: the estimated median revenue for an entire home is about $1,850/month there versus about $1,370 in Brooklyn. Among entire-home neighbourhoods with at least 40 active listings, the highest estimated revenue is in Theater District, Tribeca, Financial District and Hell's Kitchen (about $2,500–3,200/month). The highest *demand* is in outer-borough neighbourhoods near the airports and at moderate prices: East Elmhurst at 4.0 reviews/month (next to LGA), Jamaica (JFK) and Woodside. The Financial District combines both, with 1.7 reviews/month at a $229 median price.
- **Listing titles barely matter.** Titles mentioning "private" or "subway" have somewhat higher median reviews (1.55–1.76 vs about 1.15). "Luxury", "loft", "view" and "sunny" do slightly worse. These differences are small and confounded with room type and price, so they are not a lever to rely on.

**Robustness.** Repeating the comparison on listings with at least 10 reviews (n = 17,480) gives the same picture: the same falling trend with minimum nights (2.9 → 0.65 reviews/month), the same peak in the middle of the availability range, and the same flat-then-falling price curve. This lowers the risk that new listings with inflated reviews/month are driving the results. I deliberately did **not** use "days since last review" as a driver. It is very strongly linked to reviews/month (92% of the top quartile were reviewed in the last 30 days), but it measures the same activity, not a cause of it.

## 3. Risks

1. **Regulation (outside knowledge; check with counsel).** Under New York's Multiple Dwelling Law, renting a whole apartment in most multi-unit buildings for fewer than 30 days while the permanent resident is away is generally illegal, and advertising such rentals is fined. **87% of entire-home listings in the data (22,250 listings, 46% of the market) have minimum stays under 30 nights.** 4,330 of them belong to multi-listing hosts. A business model built on short entire-home stays is exposed to enforcement and platform delisting. The shift of the largest operators to 30+ night minimums is consistent with this.
2. **Competitive supply is overstated and fragmented.** 40% of listings show no recent activity. Concentration in Williamsburg, Bed-Stuy and Harlem means those markets are crowded.
3. **Data limits.** The file is a single snapshot, so it shows no trend or seasonality. It has no occupancy, cost or rating data. Reviews/month cannot tell high demand apart from guests who are simply more willing to review. The revenue figures are modelled, not observed.

## 4. Recommendations

1. **Lead with legally robust formats:** 30+ night furnished rentals (the model Sonder and Blueground use) and private rooms in host-occupied homes. Model short-stay entire-home revenue only as upside, after legal review.
2. **If the company runs shorter stays where they are legal, set minimums of 1–2 nights, keep 90–270 days of the calendar open, and price at or slightly above the neighbourhood median for the room type.** These are the habits that separate top-quartile listings.
3. **Pick locations by revenue opportunity, not listing counts.** Use the Financial District and Midtown West/Hell's Kitchen for higher rates with solid demand. Consider outer-borough areas near the airports (East Elmhurst, Jamaica, Woodside) for high demand with less competition. Size competition using the active-listing count only.
4. **Validate before committing capital.** Get actual occupancy and ADR data, from a data vendor or from pilot units, to replace the review-based proxy. In particular, test whether 30+ night listings really earn what the model implies.
