# NYC Short-Term Rental Market Entry: What the Airbnb Listing Data Shows

## Bottom line

1. **The data is old, and the regulatory risk is the most important thing to settle.** The file is a snapshot taken around **8 July 2019**, which is the latest review date in it. That is more than seven years ago. The most profitable-looking segment in the data is whole apartments rented for stays under 30 nights. Under NYC law that segment is largely illegal unless the host lives there (see the risks section). **Get a legal and regulatory review before any investment decision.** The numbers below describe the 2019 market, not today's.
2. **The headline supply figure is inflated.** Of 48,895 listings, only **45% had a review in the last 90 days**. 21% have never been reviewed, and 20% have had no review in more than a year. Roughly 40% of the "market" is dormant.
3. **Good and poor performers differ mainly in minimum stay and in how professionally the listing is run.** Location and price matter less. Listings with a 1–2 night minimum get 2–4 times more reviews per month than listings with a 7+ night minimum, holding other things equal. Hosts with 2–20 listings beat single-listing hosts by about 1.8–2.4 times. Large corporate operators (21+ listings) do worst on bookings, because most of their units are 30-night corporate rentals.
4. **Opportunity:** among active listings, outer-borough entire homes near transit or airports have the highest demand per listing. Examples are Bed-Stuy, Bushwick, East Flatbush, Long Island City, Astoria/Ditmars and Jamaica. Their nightly rates are 30–45% below Manhattan's, so estimated revenue per unit is similar. Manhattan core areas (Hell's Kitchen, Midtown, FiDi, Chelsea) have the highest estimated revenue per unit but softer demand per listing.

## Data and how I measured performance

- `listings.csv` has 48,895 listings from 37,457 hosts, with no duplicate rows. It does **not** contain revenue, occupancy, ratings or listing size. "Performance" therefore has to be inferred from proxies.
- **Main proxy: reviews per month (RPM).** This is a standard stand-in for bookings. It has known biases, and I corrected for them as follows:
  - Very new listings show inflated RPM; the top value, 58.5, comes from a listing that is about 2.7 months old. I therefore limited the performance comparisons to listings at least 6 months old (age estimated as total reviews ÷ RPM), and I controlled for age in the regression.
  - Long stays produce fewer reviews per night booked.
- **Secondary, assumption-heavy proxy: estimated occupancy and revenue.** I used the common "San Francisco model":
  - nights booked = (RPM ÷ 0.5 review rate) × max(minimum nights, 3);
  - capped at 70% occupancy;
  - multiplied by the listed price.
  
  Treat these figures as relative indicators only, not forecasts.
- **Cleaning:** I excluded 11 listings priced at $0 and 239 priced above $1,000 per night (the maximum is $10,000) from the price and revenue analysis.
- **Caution about `availability_365`:** a value of 0 does not mean "fully booked". 80% of listings with no review in over a year show 0 availability, compared with 9% of active ones. A zero mostly means the calendar is blocked or the listing is inactive, so I did not use it as a success measure.

## Finding 1: Much of the listed supply is not really operating

| Status (last review before the snapshot) | Share of listings |
|---|---|
| Active (≤ 90 days) | 45.5% |
| Last review 3–12 months ago | 14.2% |
| Last review over 12 months ago | 19.8% |
| Never reviewed | 20.6% |

Manhattan and Brooklyn have the most dormant listings (only 42% and 46% active). The outer boroughs are much more active (Queens 55%, Bronx 58%, Staten Island 67%). Real competition is therefore roughly half of what the raw count suggests. On the other hand, many people tried hosting in Manhattan and Brooklyn and stopped.

## Finding 2: What separates strong from weak performers

**Regression.** I ran a regression on 32,333 listings that are at least 6 months old, priced $1–1,000, and have at least one review. The outcome is log RPM, with controls for borough, room type, relative price, minimum stay, host size and listing age. All effects below are statistically significant at p < 0.01. R² is 0.17, so much of the variation (photos, ratings, amenities) is not in this data.

| Driver | Effect on reviews/month vs. baseline |
|---|---|
| Minimum stay 2 nights (vs 1) | +14% |
| Minimum stay 4–6 nights | −36% |
| Minimum stay 7–29 nights | −60% |
| Minimum stay 30+ nights | −61% |
| Host has 2 listings (vs 1) | +84% |
| Host has 3–5 listings | +136% |
| Host has 6–20 listings | +102% |
| Host has 21+ listings | −27% |
| Private room (vs entire home) | −22% |
| Brooklyn / Manhattan (vs Bronx) | −32% each |
| Price relative to the neighbourhood median for that room type | Small positive effect; there is no sign that underpricing buys more bookings |

**Active, established listings by RPM quartile** (16,239 listings reviewed in the last 90 days, at least 6 months old):

| | Bottom 25% | Top 25% |
|---|---|---|
| Median reviews per month | 0.41 | 3.94 |
| Median minimum nights | 3 | 2 |
| Median price | $120 | $99 |
| Share in Manhattan | 43% | 38% |
| Estimated occupancy | 12% | 70% (cap) |
| Estimated revenue per month | ~$420 | ~$2,090 |

**What this means.**
- Top performers accept short stays and are priced at market rate or slightly below the premium end. Their hosts usually run a small, professional portfolio of 2–20 units, which points to responsiveness, consistent quality and calendar management. Being in Manhattan is not what drives success.
- Single-listing hosts, mostly people renting out their own homes occasionally, are the weakest group outside the corporate operators. 25% of single-host listings have had no review in over a year.
- **About the 30+ night segment:** this segment gets few reviews, but its *estimated* occupancy and revenue (~$2,000 per month median) look high. That estimate depends heavily on the assumed review rate and the 70% cap, so it is very uncertain. Corporate operators such as Blueground, "Corporate Housing" and several hosts with 50–120 listings use this model almost exclusively.

## Finding 3: Where the demand is (active, established listings)

| Borough, entire home | Median price | Estimated occupancy | Estimated revenue/month |
|---|---|---|---|
| Manhattan | $185 | 36% | ~$2,010 |
| Brooklyn | $145 | 40% | ~$1,670 |
| Queens | $119 | 48% | ~$1,590 |
| Bronx | $102 | 53% | ~$1,470 |

- **Highest demand per listing** (entire homes, at least 40 active listings): Jamaica, Ditmars-Steinway, East New York, Long Island City, Canarsie, East Flatbush, Flushing, Bushwick and Bed-Stuy. Their median RPM is 2.2–2.7, against 1.5 citywide.
- **Highest estimated revenue per unit:** Financial District, Hell's Kitchen, SoHo, Midtown, Murray Hill and Chelsea (about $2,250–2,850 per month). Long Island City (~$2,125) is the only outer-borough area in the top tier, combining high demand with a near-Manhattan price.
- Private rooms earn roughly half as much per listing as entire homes in every borough. Shared rooms are a small niche (2% of listings) with low revenue.

## Risks

1. **Regulation.** This comes from my general knowledge, not from the data, and needs to be checked by counsel.
   - NYC's Multiple Dwelling Law has long banned renting whole apartments in most buildings with 3+ units for under 30 days unless the permanent resident is present.
   - Local Law 18, enforced since September 2023, requires hosts to register. It in effect limits short stays to hosts who are present, with at most two guests, and platforms must block unregistered listings.
   - The "entire home, 1–3 night minimum, multi-listing operator" model that performs best in the 2019 data is exactly what these rules target. Likely legal options are 30+ night furnished rentals, licensed hotel or aparthotel inventory, and possibly 1–2 family homes, which have different rules. Each of these needs verification.
2. **Stale data.** The snapshot is from 2019: before COVID, before Local Law 18, and before years of price changes. Supply, prices and demand have almost certainly changed. Refresh with current data before sizing the opportunity.
3. **Weak proxies.** Reviews stand in for bookings, and the review rate differs by guest type and stay length. Revenue figures are modelled, not observed. Listed price is not the price actually paid.
4. **High churn.** About 40% of listings are dormant, which suggests many entrants fail or exit. Plan for slow ramp-up: newer listings in the data have fewer total reviews, which is a "cold start" problem.
5. **Concentration and competition.** Sonder (423 listings across two accounts), Blueground (232) and other corporate operators already hold the professional end in Manhattan.

## Recommendations

1. **Do not proceed on this data alone.** Before anything else, do (a) a legal review of what models are allowed under current NYC law and (b) a pull of current listing, calendar and pricing data.
2. **If the short-stay model is legally possible** (e.g., hotel-zoned or 1–2 family properties), the data favours:
   - entire homes with a 1–2 night minimum;
   - pricing at or around the neighbourhood median for that room type;
   - professional operations;
   - locations in transit- or airport-connected outer-borough neighbourhoods (Bed-Stuy/Bushwick, LIC/Astoria, Jamaica), which have strong demand and lower acquisition costs, plus a selective presence in Hell's Kitchen, Midtown and FiDi for top revenue per unit.
3. **If only 30+ night stays are allowed**, the comparable model is Blueground-style corporate housing. Validate demand and pricing with direct market data, because the review-based proxies are least reliable for long stays.
4. **Track real KPIs** (occupancy, average daily rate, revenue per available night, booking lead time, ratings) rather than review counts. Size the competition using *active* listings, not total listings.

*Assumptions: the snapshot date is 2019-07-08 (latest review); "active" means reviewed within 90 days; occupancy uses a 50% review rate, an average stay of max(minimum nights, 3) and a 70% cap; prices of $0 or above $1,000 are treated as errors or outliers.*
