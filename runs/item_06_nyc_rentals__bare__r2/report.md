# NYC Short-Term Rental Market: What Separates Strong from Weak Listings

**Data:** `listings.csv` has 48,895 Airbnb listings in New York City, held by 37,457 hosts. The latest review date is 8 July 2019, so this is a **mid-2019 snapshot**. Treat it as historical. The regulatory situation in NYC has changed a lot since 2019 (see Risk 1).

## Summary

1. **Many listings are inactive.** 40% of listings have either never been reviewed (21%) or have had no review in the last 12 months (20%). Only 49% had a review in the last 6 months. Headline listing counts overstate real competing supply by roughly 2x.
2. **Minimum-stay length is the strongest measurable driver of booking frequency.** After controlling for room type, borough, price, host size and availability, a listing with a 1-night minimum gets about **4x the reviews per month** of one with a 30+ night minimum, and about 1.6x one with a 3-night minimum. Whether this means more *revenue* depends on stay length, which the data does not contain.
3. **Location matters more for price than for demand.** Once other factors are controlled, borough has no significant effect on booking frequency. Manhattan wins on price: median entire-home price is $190 there versus $145 in Brooklyn and $100–120 in the outer boroughs. The highest estimated revenue for entire homes is in Financial District, Hell's Kitchen, Chelsea, SoHo, Midtown and Murray Hill. Long Island City and East Harlem perform well for their lower cost.
4. **Higher prices lose little demand.** Within entire homes, price and booking frequency are almost uncorrelated (Spearman ρ = –0.08). Listings priced 5–25% above their neighbourhood median get slightly *more* reviews per month than those priced at the median, and listings priced below 75% of the median get the fewest.
5. **Large operators underperform on booking frequency.** Hosts with 21+ listings get about 45% fewer reviews per month than single-listing hosts, after controls. 46% of their listings have never been reviewed. Small multi-listing hosts (2–5 listings) do best. This is the most relevant finding for a company that would itself be a large operator.
6. **Regulation is the main risk.** 88% of entire-home listings allow stays under 30 nights. NYC law generally prohibits renting a whole apartment for under 30 days unless the host is present. Since 2019 the city has tightened enforcement a lot (Local Law 18, effective 2023). A business plan built on short whole-unit stays may not be legal.

## How "performance" was measured (assumptions)

The file contains no bookings, occupancy or revenue figures, so I used proxies:

- **Booking frequency:** `reviews_per_month`. This assumes a roughly constant share of stays leave a review.
- **Activity status:** days from `last_review` to the snapshot date. "Active" means a review in the last 180 days.
- **Estimated revenue (indicative only):** nights per month ≈ reviews per month ÷ 0.5 (assumed review rate) × max(minimum nights, 3), capped at 27 nights. Monthly revenue ≈ nights × listed price. This follows the common Inside Airbnb-style occupancy model. The figures are useful for *ranking* listings, not as forecasts.
- **Main analysis set:** listings that were active, priced $1–$1,000, and had at least about 6 months of review history (`number_of_reviews / reviews_per_month`). This gives n = 17,681. The tenure filter removes new listings, whose per-month rate is inflated by a short history.
- **Exclusions:** 11 listings priced at $0 and 239 priced above $1,000 were treated as data errors or outliers and dropped from price analyses.
- **Ambiguous field:** `availability_365 = 0` can mean fully booked or blocked by the host, so it is not used as a performance measure.

## Evidence

### 1. Supply is overstated by dormant listings

| Status | Share of all listings |
|---|---|
| Reviewed in last 6 months | 49.4% |
| Last review 6–12 months ago | 10.3% |
| Last review >12 months ago | 19.8% |
| Never reviewed | 20.6% |

Never-reviewed listings tend to have high prices (4.2% are above $500, versus 1.6% of active listings), longer minimum stays (median 3 vs 2 nights) and near-zero calendar availability (median 6 vs 123 days). Many are abandoned or not really bookable. Manhattan has the most dormant supply (21.5% stale and 23.2% never reviewed). Staten Island, Bronx and Queens have the most active supply, but these are small markets: they account for 0.8%, 2.2% and 11.6% of listings.

### 2. What separates high and low performers

Model: OLS regression of log(reviews per month) on the factors below, using the active analysis set, with robust standard errors. R² = 0.25. Effects are multiplicative relative to the reference group.

| Factor | Effect on reviews/month | Reference |
|---|---|---|
| Min. nights 2 / 3 / 4–6 / 7–29 / 30+ | ×0.78 / ×0.62 / ×0.47 / ×0.28 / ×0.23 | 1 night |
| Calendar open 1–60 / 61–180 / 181–300 / 301–365 days | ×1.65 / ×1.88 / ×2.05 / ×1.43 | 0 days open |
| Host with 2 / 3–5 / 6–20 / 21+ listings | ×1.08 / ×1.06 / n.s. / ×0.56 | single-listing host |
| Private room / shared room | ×0.88 / ×0.73 | entire home |
| Price (+10%) | about –1.4% | — |
| Borough | not significant (all p > 0.27) | Bronx |

(n.s. = not statistically significant.)

How to read this:

- **Minimum stay.** Part of this effect is mechanical: longer stays mean fewer separate guests and therefore fewer reviews. Applying the revenue proxy to entire homes gives estimated revenue that is U-shaped in minimum nights: 1 night ≈ $2,080/month, 3 nights ≈ $1,400, 30+ nights ≈ $2,520. The 30+ figure depends heavily on the assumption that every stay lasts the full 30 nights, so treat it as an upper bound. Still, it shows that legal 30-day-plus rentals can earn comparable revenue on far fewer bookings.
- **Availability.** Listings that are open most of the year perform best, with a peak at 181–300 open days. Listings with 0 open days are mostly dormant.
- **Large hosts.** Corporate operators (e.g. Sonder with 327+96 listings, Blueground 232, "Corporate Housing" 91) mostly offer 30+ night stays. Their per-listing booking frequency is low even after controlling for minimum stay.

Entire homes, comparing the top and bottom revenue-proxy quartiles:

| | Bottom 25% | Top 25% |
|---|---|---|
| Median price | $131 | $200 |
| Median reviews/month | 0.47 | 2.99 |
| Median days open in calendar | 27 | 187 |
| Share in Manhattan | 38% | 55% |

Top performers combine a higher price, a calendar that stays open, and a central location. Low performers are mostly part-time listings with closed calendars, not listings that are priced too high.

### 3. Pricing headroom

Entire homes, by price relative to their neighbourhood median:

| Price vs. neighbourhood median | Reviews/month | Est. revenue/month |
|---|---|---|
| < 75% | 1.10 | $1,136 |
| 75–95% | 1.33 | $1,501 |
| 95–105% | 1.53 | $1,716 |
| 105–125% | 1.58 | $1,968 |
| > 125% | 1.38 | $2,592 |

Cheap listings do not get more bookings. They are probably lower-quality units. This is correlation, not a measured price elasticity, but it suggests well-presented units can price above the local median without losing demand.

### 4. Where to locate

Median estimated monthly revenue for active entire homes. Only neighbourhoods with at least 40 listings are included.

| Neighbourhood | n | Median price | Est. nights/mo | Est. revenue/mo |
|---|---|---|---|---|
| Financial District | 68 | $200 | 15.1 | $2,909 |
| Hell's Kitchen | 374 | $198 | 13.1 | $2,467 |
| Chelsea | 232 | $200 | 11.9 | $2,377 |
| SoHo | 83 | $235 | 9.0 | $2,343 |
| Midtown | 271 | $199 | 11.5 | $2,276 |
| East Harlem | 205 | $150 | 12.7 | $2,124 |
| Long Island City | 72 | $150 | 15.1 | $2,105 |
| *Weakest: Greenpoint, Prospect Heights, Windsor Terrace, Flatbush* | | $110–158 | 6–10 | $1,050–1,190 |

By borough, Manhattan entire homes lead the revenue proxy at $1,938/month, against about $1,450–1,610 elsewhere. That lead comes from price, not occupancy. Under the alternative assumption of a fixed 3-night stay, the borough differences almost disappear ($1,290–1,465 everywhere). This finding is therefore sensitive to the assumption. For **private rooms**, Hell's Kitchen ($1,860), Chelsea ($1,536) and Midtown ($1,453) lead.

Simple wording in listing names (e.g. "renovated" and "subway" are associated with more reviews per month, "luxury" and "loft" with fewer) is correlated with performance but confounded with price and room type. It is a hint for listing copy, not a firm finding.

## Risks

1. **Regulation, the biggest risk.** NYC's Multiple Dwelling Law bars whole-unit rentals under 30 days in most buildings unless the permanent resident is present. 88% of entire-home listings here offer shorter minimum stays. Local Law 18 (2023) added host registration and platform enforcement, which removed most such listings after this snapshot was taken. Any model that relies on short whole-unit stays is high risk.
2. **Stale data.** The 2019 snapshot predates COVID and the 2023 enforcement. Prices, supply and demand will have shifted.
3. **Proxy uncertainty.** Revenue and occupancy are inferred from reviews. Review rates vary by guest type, stay length and operator, and corporate operators may get fewer reviews per stay. Validate against real booking data (e.g. a current Inside Airbnb or AirDNA pull) before committing capital.
4. **Scale penalty.** Large hosts in this data show weaker per-listing engagement. Scale alone does not guarantee better performance.

## Opportunities and recommendations

1. **Lead with a compliant model.** Focus on (a) furnished stays of 30+ nights for business travellers, relocations and medical stays, which the revenue proxy suggests can match short-stay revenue, and/or (b) host-present private-room products, which perform well in Hell's Kitchen, Chelsea and Midtown. Get legal review before entering.
2. **Target central Manhattan and well-connected, lower-cost areas.** Prioritise Financial District, Hell's Kitchen, Chelsea and Midtown for premium pricing. Long Island City and East Harlem offer strong occupancy at lower acquisition cost. Avoid neighbourhoods with thin demand, such as Greenpoint and Prospect Heights.
3. **Run units as full-time inventory.** Keep calendars open most of the year, use the shortest legally allowed minimum stay, and price at or slightly above the neighbourhood median rather than discounting.
4. **Plan for weaker engagement at scale.** Large operators' low review and booking rates suggest a need for investment in guest experience and listing quality. Set KPIs per unit, not just on unit count.
5. **Size the market on active listings only.** Use roughly 24,000 recently active listings rather than the headline 49,000 when estimating competing supply.
6. **Next step:** get current data with actual occupancy and revenue, and confirm the legal status of the target product, before making the final decision.
