# NYC Short-Term Rental Market Entry: What the Airbnb Listing Data Shows

## Summary

1. **Regulation is the biggest risk, and the data shows it clearly.** 88% of entire-home listings (22,254) accept stays under 30 nights. Under New York State and City rules (outside context, not in the file), renting a whole apartment for under 30 days is generally illegal in most multi-unit buildings unless the host is present. The largest professional operators in the file (Sonder, Blueground, "Corporate Housing") have already moved to **30-night minimums**: the median minimum stay for hosts with 21+ listings is 30 nights. A plan built on nightly entire-home rentals carries serious legal risk. The realistic options are a 30+-night furnished-rental model, or host-present private rooms.
2. **Much of the supply is dormant.** Only 49% of listings were reviewed in the 6 months before the snapshot. 21% have never been reviewed and another 20% were last reviewed more than 12 months earlier. The headline count of 48,895 listings overstates the real competition, and averages across all listings understate what active listings achieve.
3. **The strongest driver of booking frequency is a short minimum stay, not location or price.** Among active listings, median reviews per month fall from 2.41 (1-night minimum) to 0.40 (30-night minimum). This holds after controlling for room type, borough, price, host size, availability and listing age.
4. **Manhattan earns the most per listing. The outer boroughs get booked more often.** Manhattan has the highest prices (median entire home $195 vs $145 in Brooklyn and $120 in Queens) and the highest estimated revenue, but its active entire homes are booked *less* often (1.2 reviews/month vs 2.1 to 2.4 in Queens and the Bronx). Queens and the Bronx also have the largest active share (59% and 62%, vs 46% for Manhattan).
5. **Well-performing listings stand out mainly by being available.** Listings that are open 31 to 300 days a year are reviewed about twice as often as those with 0 open days. Among active entire homes, the top revenue quartile has a median of 194 available days vs 32 for the bottom quartile, a higher price ($245 vs $130), and is more often in Manhattan (64% vs 38%). In other words, top performers are priced up *and* sell their calendar. Moderate pricing helps a little (see §4), but availability and minimum stay matter far more.

## 1. Data and how "performance" is measured

- `listings.csv`: 48,895 listings with 16 fields. No duplicate IDs. The latest review is dated 2019-07-08, so **this is a mid-2019 snapshot**. It is about 7 years old today. Absolute levels (prices, supply, how many listings are legal) will have changed a lot, especially after NYC's 2023 short-term rental registration law (Local Law 18; outside knowledge). Treat the findings as structural patterns, not current market sizing. **The data should be refreshed before any capital decision.**
- The file contains **no bookings, occupancy or revenue data.** I used these proxies:
  - **Active** = last review within 180 days of 2019-07-08.
  - **Demand** = `reviews_per_month` (rpm), assessed only for active listings.
  - **Estimated revenue (rough)** = rpm ÷ 0.5 review rate × max(min nights, 3) nights per stay × 12 × price, capped at 70% occupancy. This is the common "InsideAirbnb-style" method, and all its parameters are assumptions. It is **highly sensitive** for long-minimum-stay listings: if every stay is assumed to last 3 nights, the median estimate for active 30-night listings falls from $22.2k to $3.1k. 24% of active listings (56% of 30-night listings) hit the occupancy cap. Revenue figures here are for **ranking only, not forecasting**.
- `availability_365` = 0 for 36% of listings. 80% of those that are stale (>12 months since a review) have 0 availability, which suggests "0" mostly means a blocked or inactive calendar, not "fully booked".
- Data quality: 11 listings have a price of $0 and 298 have a price of $1,000 or more. Some of these are event spaces, film locations or a yacht, and many have no reviews. Medians are used throughout, so these outliers have little effect. `reviews_per_month` is inflated for very new listings (4,194 reviewed listings are less than 3 months old). It also falls steadily with age: median 1.9 for listings 1 to 3 months old vs 0.37 for listings over 2 years old. The regression controls for listing age.

## 2. Supply and pricing

| Borough | Listings | Active share | Median price, entire home | Median price, private room |
|---|---|---|---|---|
| Manhattan | 21,661 | 46% | $191 | $90 |
| Brooklyn | 20,104 | 50% | $145 | $65 |
| Queens | 5,666 | 59% | $120 | $60 |
| Bronx | 1,091 | 62% | $100 | $54 |
| Staten Island | 373 | 70% | $100 | $50 |

Room types are 52% entire home, 46% private room and 2% shared. 34% of listings belong to hosts with more than one listing. The ten largest hosts control about 1,270 listings.

## 3. Active listings: demand and estimated revenue by segment

| Segment | Active listings | Median rpm | Median est. revenue/yr |
|---|---|---|---|
| Entire home | 12,652 | 1.48 | $22.0k |
| Private room | 10,901 | 1.63 | $9.5k |
| Shared room | 578 | 1.53 | $5.2k |
| Manhattan, entire home | 5,886 | 1.2 | $26.6k |
| Brooklyn, entire home | 5,105 | 1.6 | $20.0k |
| Queens, entire home | 1,276 | 2.1 | $19.2k |
| Bronx, entire home | 255 | 2.4 | $17.6k |

**Minimum nights (active listings):**

| Min nights | 1 | 2 | 3 | 4–6 | 7–29 | 30 | 31+ |
|---|---|---|---|---|---|---|---|
| Active share (all listings) | 52% | 60% | 55% | 46% | 31% | 33% | 24% |
| Median rpm | 2.41 | 1.94 | 1.46 | 1.06 | 0.62 | 0.40 | 0.54 |

**Availability (active listings):** median rpm is 0.82 at 0 open days, 1.33 at 1 to 30 days, about 2.0 at 31 to 300 days, and 1.28 at 301 to 365 days. A calendar open almost all year usually means unsold nights, not strong demand.

**Host size:** hosts with 2 to 5 listings have the highest active share (62 to 71%) and rpm (1.7 to 1.8). Hosts with 21+ listings have low rpm (0.58) because they mostly run 30-night stays, but they have the highest estimated revenue per active listing ($23.3k; this figure depends on the assumptions above).

**Neighbourhoods with the highest estimated revenue** (active entire homes, minimum stay of 5 nights or less, at least 40 listings): Financial District ($37.6k, rpm 2.1), Hell's Kitchen ($37.4k, rpm 2.3), Murray Hill, Midtown, SoHo, Chelsea. Outer-borough neighbourhoods with unusually high demand: **East Elmhurst** (rpm 4.15) and **Woodside** (rpm 2.87). Both are close to the LaGuardia and JFK airports, and the busiest listings in the whole file are airport-adjacent private rooms. **East Harlem** has high demand (rpm 2.06) at a moderate price of $160.

## 4. What separates strong from weak performers (controlled view)

I ran an OLS regression of log(rpm) on active listings at least 3 months old (n = 19,930, R² = 0.28, robust standard errors). Approximate effects, all p < 0.001 unless stated:

- **Minimum nights:** compared with a 1-night minimum, 3 nights means about 36% fewer reviews, 4 to 6 nights about 51% fewer, 7 to 29 about 71% fewer, and 30 nights about 78% fewer. This is the largest effect in the model. Part of it is mechanical, because longer stays produce fewer reviews per night booked.
- **Availability:** 31 to 300 open days means roughly 2.0 to 2.3 times the rpm of a listing with 0 open days.
- **Price:** elasticity of about −0.17 (a 10% higher price goes with about 1.6% fewer reviews). Demand is fairly insensitive to price, which is why higher-priced listings earn more revenue.
- **Room type:** private rooms are about 16% lower and shared rooms about 33% lower than entire homes once price is held constant.
- **Borough:** small effects once the factors above are controlled (Manhattan +9%, p = 0.015). The raw outer-borough demand advantage comes mostly from lower prices and shorter minimum stays.
- **Large hosts (21+ listings):** about 41% lower, after controlling for minimum stay. This may reflect a different guest type (corporate or long-stay) rather than worse operations.

These are associations from a single snapshot. They are not causal effects. The data contains no ratings, amenities, photos, size or cancellation information, so a listing-quality effect cannot be ruled out.

## 5. Risks

1. **Regulatory risk (highest).** Most entire-home inventory in the data appears to be offered on terms that conflict with NYC's 30-day rule for whole-unit rentals. Enforcement has tightened since 2019 (outside knowledge). Revenue from nightly entire-home rentals should be treated as at risk.
2. **Old data.** The snapshot is from 2019, before COVID and before Local Law 18. Market size and prices need to be checked against current data.
3. **Proxy risk.** Revenue estimates depend on assumed review rates and stay lengths. They could be wrong by a factor of 5 or more for long-stay listings.
4. **Concentration and competition.** Professional operators are concentrated in Manhattan (81% of 21+-host listings) and already run the 30-night model there at scale.

## 6. Recommendations

1. **Build the entry plan around a compliant model.** The options are 30+-night furnished rentals (the model incumbents already use) and/or host-present private rooms. Do not size the opportunity using nightly entire-home listings. Get legal review before committing.
2. **For 30+-night units, target Manhattan business districts** (Financial District, Midtown, Murray Hill, Chelsea, Hell's Kitchen). These have the highest prices and proven demand. Expect fewer, longer bookings.
3. **For short stays (private rooms or registered units), look at high-demand, lower-cost outer-borough areas:** Queens near the airports (East Elmhurst, Woodside, Jackson Heights) and East Harlem. These have the highest booking frequency and the most active supply.
4. **Operating levers:** keep calendars genuinely open (the best results come at roughly 90 to 300 open days), set the shortest minimum stay the law allows, and price at the market median or slightly above. Demand drops only modestly with price.
5. **Next steps on data:** get a current (2025/26) listings and calendar file with occupancy and real revenue (e.g. calendar or booking data), plus the list of registered listings. Use these to re-estimate the market and to check how many competitors remain legally operating.
