# NYC short-term rental market entry: what the Airbnb listing data says

## Bottom line

1. **The biggest risk is legal, not commercial.** Most of the profitable segment in this data is entire homes rented for less than 30 nights. That is 22,254 listings, or 46% of all listings and 88% of entire homes. It is also the segment NYC law restricts. Short stays in a whole apartment, without the host living there, are generally illegal in multiple-dwelling buildings. Since Local Law 18 took effect in September 2023, hosts must register, and platforms cannot process bookings for unregistered listings. A plan based on the economics shown in this file depends on a model that is largely not permitted today.
2. **The data is a July 2019 snapshot and is now about 7 years old.** It comes from before COVID and before Local Law 18. Use it to understand the structure of the market (what drives demand, where it sits), not to size the market or forecast returns.
3. **Entire homes earn about 2.2–2.4× what private rooms earn (estimated).** The gap comes from price ($160 vs $70 median), not from more bookings. This was checked independently; see the caveats under Finding 3.
4. **The listing attributes in this file explain little about which listings do well.** Among active short-stay listings, the top and bottom quarters by review rate have the same median price, room-type mix and Manhattan share. The main visible differences are booking rules: minimum stay and how many days the calendar is open. What most likely sets winners apart (reviews/ratings, photos, host responsiveness, amenities, pricing tactics) is not in this file.
5. **About 40% of listings show no recent demand.** Raw listing counts overstate how much competition is actually active.

---

## Data and method (read first)

- **Grain and coverage:** 48,895 rows, one per Airbnb listing in NYC. There are no duplicate IDs. Fields: location (borough, 221 neighbourhoods, latitude/longitude), room type, price, minimum nights, number of reviews, last review date, reviews per month, the host's listing count, and availability_365.
- **Time window:** a single snapshot. The latest review date is 2019-07-08, which I treat as the snapshot date. Because it is one point in time, **nothing here is a trend**.
- **There is no booking, occupancy or revenue data.** Any "performance" measure has to be a proxy:
  - **Demand proxy:** reviews per month (rpm). Reviews track stays, not nights booked.
  - **Estimated revenue (an estimate, not a measurement):** I used the common Inside Airbnb-style model. Estimated occupancy = rpm ÷ 0.5 (assuming half of guests leave a review) × assumed stay length (the larger of 3 nights and the minimum stay) × 12 ÷ 365, capped at 70%. Revenue = occupancy × 365 × price. 18% of active listings hit the 70% cap. I checked results for assumed stays of 2, 3 and 5 nights. All figures are within this sample only.
- **Data-quality issues:**
  - 10,052 listings (21%) have **never been reviewed**, and 9,691 (20%) have had **no review in the past 12 months**. Only **29,152 (60%) are "active"** (reviewed in the past 12 months). Driver analysis uses only active listings priced $1–$1,000 (n = 29,080).
  - **availability_365 = 0 for 17,533 listings, and its meaning is unclear.** It could mean fully booked or blocked by the host. The evidence points to blocked or dormant: 7,742 of these are stale listings, and active listings with 0 availability have the *lowest* review rate (median rpm 0.51 vs 1.6–1.8 for listings open 30–270 days). I do not treat it as an occupancy measure.
  - Price: 11 listings at $0 and 239 above $1,000, up to $10,000. Many of these are stale or never reviewed, or are event spaces, film locations or yachts. They are excluded.
  - Very high rpm values (up to 58.5) come from listings that are only a few months old. Medians are used throughout so these do not distort results.

---

## Findings

Each claim is tagged: **[OBS]** = computed from the data; **[CON]** = the conclusion the evidence best supports; **[HYP]** = plausible but not shown.

### 1. Regulatory exposure is concentrated in the most profitable segment [OBS, plus legal context]

| Segment | Listings | Share of all |
|---|---|---|
| Entire home/apt, minimum stay under 30 nights | 22,254 | 46% |
| Entire home/apt, minimum stay 30+ nights | 3,155 | 6% |
| Private/shared room (host may be present) | 23,486 | 48% |

- 34% of listings belong to hosts with more than one listing. Large operators (21+ listings) are mainly corporate or furnished-rental businesses, such as Blueground, Sonder and "Corporate Housing". 56% of their active listings already require 30+ night stays. **[OBS]**
- My reading is that the professional operators had already moved toward 30-night stays by 2019, the legal model. **[HYP]** Confirming this would require host-level history over time.

### 2. Location: Manhattan wins on price, outer boroughs on review rate. The borough gap mostly disappears once listing mix is controlled for [OBS]

Active listings priced $1–$1,000:

| Borough | Active listings | Median price | Median reviews/month | Median est. revenue |
|---|---|---|---|---|
| Manhattan | 11,925 | $145 | 1.08 | $16.2k |
| Brooklyn | 12,202 | $95 | 1.10 | $10.0k |
| Queens | 3,873 | $70 | 1.64 | $9.7k |
| Bronx | 780 | $65 | 1.68 | $8.3k |
| Staten Island | 300 | $74 | 1.54 | $8.7k |

- I regressed log review rate on room type, borough, minimum-stay band, log price and host size. After those controls, Manhattan, Queens and Staten Island do not differ significantly from the Bronx; Brooklyn is about 10% lower. The higher raw review rates in the outer boroughs come mostly from their mix of listings (cheaper, shorter minimum stays), not from location itself. **[OBS]**
- **Neighbourhoods for entire homes** (active, under 30 nights, at least 40 listings):
  - **Financial District** ($229 median, rpm 1.81, ~$35k est.) and **Hell's Kitchen** ($209, rpm 1.98, ~$33k est.) rank at the top whether ranked by price × rpm or by modelled revenue. **[OBS]**
  - Murray Hill, Midtown and Chelsea rank high only under the revenue model's stay-length assumption, so treat them as less certain. **[OBS]**
  - Queens neighbourhoods near the airports (East Elmhurst rpm 4.01, Jamaica 2.99, Woodside 2.56) show the strongest demand per listing at lower prices ($100–$125). **[OBS]** Airport and transit-stopover demand is the likely reason. **[HYP]**
  - Popular Brooklyn areas such as Williamsburg (rpm 0.99) and Greenpoint (0.83) look crowded, with many listings and lower review rates. **[OBS]**

### 3. Room type: entire homes earn about 2.3× more, because of price rather than demand [CON, independently verified with a caveat]

Active listings, minimum stay under 30 nights:

| | Entire home/apt | Private room |
|---|---|---|
| Listings | 13,845 | 12,590 |
| Median price | $160 | $70 (ratio 2.29×) |
| Median reviews/month | 1.25 | 1.33 |
| Median est. revenue: 2-night stay assumed | $14.6k | $6.0k (ratio 2.43×) |
| Median est. revenue: 3-night stay assumed | $17.8k | $7.9k (ratio 2.26×) |
| Median est. revenue: 5-night stay assumed | $24.0k | $11.1k (ratio 2.17×) |

- A separate sub-agent, working only from the raw file, reproduced these figures. The result held with listings that have 10+ reviews and with means instead of medians.
- **Caveat:** entire homes have *lower* review rates only in Manhattan (1.12 vs 1.41). In Brooklyn, Queens, the Bronx and Staten Island, entire homes have *higher* review rates than private rooms. So outside Manhattan, demand adds to the price advantage instead of being neutral.
- By borough, the revenue ratio runs from 1.9× in Manhattan to 3.2× in Staten Island.

### 4. What sets strong performers apart from weak ones

**What the data shows [OBS]:**

Active listings with minimum stay under 30 nights, split into quarters by review rate:

| | Bottom quarter | Top quarter |
|---|---|---|
| Median reviews/month | 0.28 | 3.85 |
| Median price | $110 | $100 |
| Share entire home | 53% | 50% |
| Share in Manhattan | 39% | 39% |
| Share with minimum stay ≤ 2 nights | 38% | 79% |
| Median days available per year | 22 | 131 |
| Share single-listing hosts | 70% | 57% |

**How to read it:**

- **Price, room type and borough barely differ** between the top and bottom quarters. The regression explains only about 20% of the variation in review rate. Whatever makes a listing perform well is mostly **not in this file**. **[CON]**
- **Minimum stay is the strongest visible factor, but mostly by construction.** Review rate falls steadily as the minimum stay rises. Relative to a 1-night minimum, the regression gives about −20% for 2 nights, −40% for 3 nights, −57% for 4–6 nights and −74% for 7–29 nights. The pattern holds within every borough × room-type cell.
  - However, longer stays mean fewer stays, and so fewer reviews, for the same number of nights booked.
  - For established listings (10+ reviews), implied nights booked per month *rise* with the minimum stay: about 6 nights at a 1-night minimum vs about 15 at a 7–29-night minimum.
  - So short minimums clearly bring **more stays**. The data **cannot show that they bring more nights booked or more revenue**. **[HYP]** Confirming this needs booking-level data on nights per stay.
- **Open calendars:** listings that are open more days get more reviews, up to a point. Listings open 90–270 days have a median rpm of about 1.8, vs 0.51 for zero-availability listings. **[OBS]** Many weak performers are probably part-time or dormant hosts rather than listings guests turned down. **[HYP]**
- **Pricing near the local median:** relative to the median for the same neighbourhood and room type, review rate peaks for listings priced at 90–133% of that median (rpm about 1.32–1.38). It is lowest for those priced below 75% (rpm 0.91). **[OBS]**
  - Possible explanations are that cheap listings are lower quality, or that hosts with strong demand raise prices. Which one applies is unknown. **[HYP]**
  - Estimated revenue rises with relative price, but that is partly built into the revenue formula. **[OBS]**
- **Host scale:** hosts with 2–20 listings get 14–24% higher review rates than single-listing hosts, after controls. **[OBS]** Operational professionalism (fast responses, flexible check-in, consistent quality) is a likely factor. **[HYP]** Confirming it would need review scores and response-rate data.

---

## Recommendations

1. **Get the legal model settled before any spend.** Base the plan on activity that is legal today:
   - **30+ night furnished rentals**, the model the largest operators already used in 2019; or
   - **hosted private rooms** that comply with Local Law 18 registration; or
   - **properties legally licensed for transient use**, such as hotel-zoned or class B buildings.

   Do not budget on the under-30-night entire-home economics shown here.
2. **Buy current data before sizing the opportunity.** This 2019 file comes from before COVID and before Local Law 18. Get a recent Inside Airbnb scrape, or AirDNA-type occupancy and revenue data, plus the city's registration list. These would show how much short-stay supply has left and what 30-day rentals actually earn.
3. **Where to look first (subject to step 1):**
   - Financial District and Hell's Kitchen show the strongest combination of price and demand for entire homes.
   - Airport-adjacent Queens (East Elmhurst, Jamaica, Woodside) shows high demand at lower prices, which suits private rooms.
   - Avoid crowded Brooklyn areas where review rates are low (Greenpoint, Williamsburg).
4. **Operating practices consistent with the strong performers** (to test, not proven causes):
   - Keep calendars open.
   - Price close to the local median for the room type.
   - Run listings with the consistency of a multi-listing operator.
   - Keep minimum stays as short as the legal model allows. The benefit shown is in stays, not proven in revenue.
5. **For acquisitions, check activity, not listing counts.** 40% of listings in this file had no review in the past year. When assessing a portfolio or a neighbourhood, judge it by recent review activity rather than raw listing numbers.

## Limits of this analysis

- Reviews per month is a proxy for demand, and the revenue figures are model estimates that depend on the review-rate and stay-length assumptions.
- It is a single, 7-year-old snapshot with no trends.
- The file has no quality, amenity, rating or cost data, so profitability and causal drivers cannot be established.
- The legal points come from general knowledge of NYC law, not from the data. Confirm them with counsel.
