# NYC short-term rental market entry: what the Airbnb listing data shows

## Summary

1. **The data is a single snapshot from July 2019, more than seven years old.** It contains no bookings, occupancy or revenue. NYC regulation has changed a lot since then: Local Law 18 has been enforced since 2023 (this is outside knowledge, not something in the file). Use the file to understand *what kinds of listings perform well*, not to size today's market.
2. **The biggest risk is regulatory.** 22,203 listings (45%) are entire homes that accept stays of under 30 nights. That is the product NYC law restricts. Any entry plan that depends on whole-unit short stays carries legal risk that this data cannot price.
3. **A large share of the listed supply is dormant.** Only 45% of listings had a review in the 90 days before the snapshot. 21% have never been reviewed, and 20% have not been reviewed for more than a year. The headline count of 48,895 listings overstates real competition by roughly half.
4. **What separates strong listings from weak ones, among the factors an operator controls:**
   - **Price close to the local median for the same neighbourhood and room type.** Listings priced at more than 2x that median do clearly worse on every measure. Very cheap listings (under 0.75x) also do a little worse.
   - **Run by a host with 2–20 listings.** These listings are much more likely to be active than those from single-listing hosts.
   - **Short minimum stays (1–3 nights)** go with higher activity. However, part of this gap comes from how performance is measured (see Finding 4).
5. **Location involves a trade-off between demand and price.** After controlling for listing mix, Queens, the Bronx and Staten Island show about 25–35% higher review intensity (a demand proxy) than Manhattan. Manhattan and Brooklyn are about equal. Manhattan still produces the highest *estimated* revenue per listing because its prices are much higher.

## Data and method (read first)

- **Grain:** one row per listing. There are 48,895 listings from 37,457 hosts, with no duplicate IDs. The snapshot date is about 2019-07-08, the latest `last_review` in the file.
- **No direct performance measure exists.** I used three proxies:
  - **(a)** `reviews_per_month` (review intensity), counted only for listings that have reviews;
  - **(b)** "active": the listing had a review in the 90 days before the snapshot;
  - **(c)** an **estimated** monthly revenue, explained under Finding 6.
- **Known biases in these proxies:**
  - Reviews come from guest stays, so long stays produce fewer reviews per night booked.
  - The review counts are lifetime totals, which mixes listings of different ages. I used listing ID as an age proxy and controlled for it.
- **Data quality:**
  - 11 listings have price $0, and a few are priced up to $10,000. I excluded the $0 listings and those above $2,000 from the modelling (97 rows in total).
  - 10,052 listings have no reviews, so `reviews_per_month` and `last_review` are blank for them.
  - `availability_365 = 0` applies to 36% of listings. It does **not** mean "fully booked": only 11% of those listings were active. Most of them are blocked or dormant calendars. Because this column effectively records the outcome rather than explaining it, I left it out of the driver analysis.
- **Methods:** segment tables, plus regressions of each proxy on room type, borough, minimum-nights band, host portfolio size, price relative to the neighbourhood and room-type median, and listing-age quintile. All effects are **associations, not proven causes**.

## Findings

Tags used below: **[OBS]** = computed directly from the data; **[CON]** = the reading the evidence best supports; **[HYP]** = plausible but not shown by this data.

### 1. Market structure [OBS]

| Borough | Listings | Entire-home share | Median price, entire home | Median price, private room |
|---|---|---|---|---|
| Manhattan | 21,661 | 61% | $191 | $90 |
| Brooklyn | 20,104 | 48% | $145 | $65 |
| Queens | 5,666 | 37% | $120 | $60 |
| Bronx | 1,091 | 35% | $100 | $54 |
| Staten Island | 373 | 47% | $100 | $50 |

- **Supply is fragmented.** 66% of listings belong to hosts with only one listing.
- **A few professional operators stand out.** Sonder (327 + 96 listings), Blueground (232), Corporate Housing (91) and others mostly run 30-night-minimum "corporate housing". These are the closest analogues to the client.

### 2. Dormant supply [OBS]

- 45.5% of listings are active.
- 14% were last reviewed 90–365 days before the snapshot.
- 20% were last reviewed more than a year before.
- 21% have never been reviewed.

[CON] The effective competitive set is about half the listed count. A new entrant competes mainly with the roughly 22,000 active listings.

### 3. Pricing relative to the neighbourhood is the clearest lever an operator controls

Bands are price ÷ median price for the same neighbourhood and room type:

| Relative price band | n | Active (90d) | Never reviewed | Median reviews/month (reviewed listings) |
|---|---|---|---|---|
| <0.75x | 10,124 | 38% | 20% | 0.43 |
| 0.75–0.95x | 11,450 | 46% | 17% | 0.69 |
| ~median (0.95–1.05x) | 5,500 | 50% | 18% | 0.95 |
| 1.05–1.33x | 9,808 | 51% | 18% | 0.94 |
| 1.33–2x | 8,260 | 47% | 24% | 0.85 |
| >2x | 3,753 | 39% | 34% | 0.66 |

- [OBS] The penalty for pricing above 2x survives controls in every specification:
  - log review rate: −0.50;
  - log-odds of being active: −0.58;
  - log estimated nights among active listings: −0.25.
- [CON] Pricing at about the median up to 1.33x the median performs best. Listings priced well below the median also underperform. [HYP] Cheap listings may be cheap because their quality is low; the data has no quality fields to test this.

### 4. Minimum stay: a real difference, but partly an artefact of the measure

| Minimum nights | n | Active (90d) | Never reviewed | Median reviews/month |
|---|---|---|---|---|
| 1 | 12,720 | 48% | 22% | 1.21 |
| 2 | 11,696 | 57% | 12% | 1.09 |
| 3 | 7,999 | 51% | 15% | 0.78 |
| 4–7 | 9,147 | 39% | 21% | 0.40 |
| 8–29 | 2,826 | 25% | 35% | 0.27 |
| 30+ | 4,507 | 24% | 39% | 0.25 |

- [OBS] With controls, a 30+ night minimum is associated with much lower odds of being active (log-odds −1.33 vs a 1-night minimum).
- **Caution:** a 30-night guest leaves at most one review per stay. Among active listings, *estimated nights booked* are **not** lower for long minimums; the 30+ group hits the estimate's cap.
- [CON] The data cannot tell us whether long-stay listings are booked less, or just reviewed less. Short minimums (2 nights is best) do go with fewer dormant and never-reviewed listings.
- 30+ night stays are also the legally safest format for entire homes. This trade-off matters more than the review gap.

### 5. Host portfolio size

| Host's listing count | n | Active (90d) | Never reviewed | Median reviews/month |
|---|---|---|---|---|
| 1 | 32,303 | 40% | 22% | 0.56 |
| 2 | 6,658 | 57% | 14% | 1.00 |
| 3–5 | 5,138 | 66% | 12% | 1.36 |
| 6–20 | 2,591 | 57% | 22% | 1.00 |
| 21+ | 2,205 | 27% | 46% | 0.26 |

- [OBS] Hosts with 2–20 listings are clearly more likely to be active (with controls, log-odds +0.75 to +1.20 vs single-listing hosts).
- The weak raw numbers for 21+ hosts are mainly a mix effect: 1,508 of their 2,205 listings require 30+ nights. Excluding those, 52% of their listings are active.
- [HYP] Managed, multi-unit operation (pricing, calendar upkeep, responsiveness) improves performance. This fits the client's model, but the data cannot show the cause.

### 6. Location: outer boroughs have higher demand intensity, Manhattan earns more (corrected after independent check)

- [OBS] Raw median reviews/month: Manhattan 0.61, Brooklyn 0.66, Queens 1.21, Bronx 1.38, Staten Island 1.41.
- After controlling for room type, minimum nights, host size, relative price and listing age (within-cell comparisons), Queens, Bronx and Staten Island remain **about +0.24 to +0.33 log points (~27–39%) above Manhattan**. Brooklyn is about equal to Manhattan.
- My first draft said borough had no effect. That was wrong: the model had included the dormant-calendar (availability) variable, which hid the gap. An independent re-analysis corrected it.
- **Estimated monthly revenue.** This is an *estimate* for active listings with minimum stays under 30 nights. It assumes 1 review per 2 stays, an average stay of max(3, minimum nights) nights, and a cap of 21 nights per month. Treat the figures as a relative index, not as dollars.

| Borough | Entire home, median est./month | Private room, median est./month |
|---|---|---|
| Manhattan | ~$2,230 | ~$1,130 |
| Brooklyn | ~$1,700 | ~$720 |
| Queens | ~$1,660 | ~$750 |
| Bronx | ~$1,460 | ~$630 |
| Staten Island | ~$1,370 | ~$480 |

- Neighbourhoods with the highest estimates (100 or more active listings): Financial District (~$2,800), Murray Hill, Midtown, Hell's Kitchen and Chelsea (~$2,100–2,350).
- Neighbourhoods with the lowest estimates: Elmhurst, Flatbush, Washington Heights and Sunset Park (~$700–800).
- Bronx and Staten Island have little volume (1,091 and 373 listings), so their demand advantage rests on small segments.
- [CON] Manhattan wins on revenue per unit because of price; Queens offers stronger demand per listing at lower (unobserved) acquisition cost. Property costs are not in the data, so **profitability cannot be ranked from this file**.

## Recommendations

1. **Settle the legal model first.** Before entering, decide between 30+ night furnished rentals (the Blueground/Sonder model) and short stays only in compliant formats (host-present rooms, or licensed hotel/B&B stock). Get legal advice on current NYC rules. 45% of the 2019 supply would likely not be allowed to operate the same way today.
2. **Refresh the data before committing capital.** Get a current listings snapshot, plus calendar and occupancy data and your own lease-cost data by neighbourhood. This 2019 file should only shape hypotheses.
3. **Price within about 0.95–1.33x the median for the neighbourhood and room type**, and avoid pricing above 2x. This is the most consistent pattern in the data.
4. **Use the operator advantage.** Professionally run small portfolios beat single-unit hosts. Invest in calendar management and responsiveness, and keep calendars open.
5. **Location strategy:** Manhattan core (Financial District, Midtown, Murray Hill, Chelsea, Hell's Kitchen) for revenue per unit. Pilot Queens and Brooklyn if unit costs are much lower, where demand intensity is equal or higher. Decide using the cost data from Recommendation 2.
6. **Competitive read:** roughly half the listed supply is inactive, and the active market is fragmented. That leaves room for a professional operator, but the main competitors (Sonder, Blueground) already hold the compliant long-stay niche.

## Limitations

- These are reviews-based proxies, not bookings. Associations are not causes.
- The data is a single 2019 snapshot, so there are no trends.
- There are no fields on cost, quality, ratings, or amenities.
- The revenue figures rest on the stated assumptions about review rate and stay length.
