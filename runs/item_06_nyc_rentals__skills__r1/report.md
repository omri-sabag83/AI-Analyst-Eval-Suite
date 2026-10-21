# NYC short-term rental market entry: what the Airbnb listing data shows

## Bottom line

1. **The data is a single snapshot from July 2019** (latest review: 2019-07-08). It is more than seven years old, and it was taken before NYC's 2023 short-term rental registration law (Local Law 18) began to be enforced. **Do not size or price an entry from this file alone.** Use it for the *structural* patterns, and buy or scrape a current listing file before committing capital.
2. **Regulation is the biggest risk, and it isn't a data question.** 45.5% of all listings were entire homes offered for stays under 30 nights. My understanding of NYC law is that this is generally not permitted in most multiple-dwelling buildings. This comes from my general knowledge, not from the data, and counsel should confirm it. The large professional operators in the data had already split into two models: 30+ night "corporate housing" (Blueground, Corporate Housing, and others) and short-stay (Sonder).
3. **The market looks much bigger than it is.** 40% of listings with plausible prices had no review in the previous 12 months (20.6% had never been reviewed). Only 45% had a review in the last 90 days. The real competitive set is about 22–29k active listings, not 49k.
4. **What separates strong from weak performers is mostly price level and location (Manhattan), not booking frequency.** Within entire homes, the top revenue-proxy quartile has a much higher median price ($225 vs $135–149) and more Manhattan exposure (62% vs 39–44%). Booking velocity barely falls as price rises. The listing-level operating choices that matter are **short minimum stays** and **keeping the calendar open**. These are the levers an operator controls.
5. **Recommendation:** if the company goes ahead, concentrate on legally robust formats: 30+ night furnished rentals for entire units, or host-present private rooms. Target the Manhattan neighbourhoods with high revenue proxies (Financial District, Hell's Kitchen, Midtown, Chelsea, Theater District), and validate against current data first.

---

## Data and how "performance" was measured

- `listings.csv`: 48,895 listings, 37,457 hosts, 16 fields. There are no duplicate IDs. The only missing values are `last_review` and `reviews_per_month`, which are blank for exactly the 10,052 never-reviewed listings, plus a handful of blank names.
- **The file has no bookings, occupancy or revenue.** I therefore used two proxies:
  - **Review velocity** (`reviews_per_month`, with 0 for never reviewed) as a proxy for booking frequency. Airbnb computes it over the listing's lifetime, so it is a long-run average, not current demand.
  - **Revenue proxy** = price × 365 × estimated occupancy. Occupancy is estimated the Inside Airbnb way: reviews/month ÷ 0.5 (assumed review rate) × average stay (minimum nights, at least 3 and at most 30) ÷ 30, capped at 70%. **This is an estimate built on assumptions, not observed revenue.** Changing the review rate rescales every listing by the same factor, so rankings are stable. The stay-length assumption, however, strongly inflates 30+ night listings (see Risks).
- **Exclusions for the revenue/performance analysis:** I dropped 11 listings priced $0 and 239 priced above $1,000 as likely placeholders or errors, and kept listings reviewed in the last 12 months ("active", n = 29,080).
- `availability_365` shows days *open* on the calendar, not days booked. A value of 0 usually means the listing is blocked or dormant: 44% of zero-availability listings were last reviewed more than a year earlier. I don't treat it as occupancy.
- Everything below is correlation in a single snapshot. There is no time series, so none of it is a trend.

## Finding 1: A large share of supply is inactive

| Listing status (as of 2019-07-08) | Share | Count |
|---|---|---|
| Reviewed in last 90 days | 45.5% | 22,230 |
| Last review 91–365 days ago | 14.2% | 6,922 |
| Last review > 1 year ago | 19.8% | 9,691 |
| Never reviewed | 20.6% | 10,052 |

- Inactivity is worst in Manhattan (21.5% stale plus 23.2% never reviewed) and lowest in Staten Island, Bronx and Queens.
- Listings with long minimum stays are far more likely never to have been reviewed: 39% at 30+ nights vs 12–15% at 2–3 nights. Part of this is that monthly guests leave fewer reviews, so review-based metrics understate these listings.
- **Implication:** headline listing counts overstate the competition. Size the market on active listings.

## Finding 2: Room type and location set the price level; Manhattan leads on revenue

Active listings, price $10–1,000:

| Room type | n | Median price | Median est. occupancy | Median revenue proxy |
|---|---|---|---|---|
| Entire home/apt | 15,255 | $158 | 34% | ~$19.0k/yr |
| Private room | 13,150 | $70 | 33% | ~$8.2k/yr |
| Shared room | 675 | $43 | 32% | ~$4.6k/yr |

| Borough | n | Median price | Median est. occupancy | Median revenue proxy |
|---|---|---|---|---|
| Manhattan | 11,925 | $145 | 34% | ~$16.3k |
| Brooklyn | 12,202 | $95 | 30% | ~$10.1k |
| Queens | 3,873 | $70 | 40% | ~$9.8k |
| Staten Island | 300 | $74 | 35% | ~$8.8k |
| Bronx | 780 | $65 | 37% | ~$8.4k |

- Estimated occupancy is similar across room types. **The revenue gap comes almost entirely from price.**
- Queens and the Bronx book more often, with clusters near the JFK and LGA airports among the fastest-reviewed listings. They don't make up for the lower prices.
- **Top entire-home neighbourhoods by median revenue proxy** (at least 50 active listings): Tribeca (~$35k, but only 57 listings), Financial District (~$35k, 331), Hell's Kitchen (~$30k, 697), Midtown (~$27k, 517), Murray Hill, Chelsea and SoHo (~$24–27k). East Harlem (~$22k, at a $150 median price) is the value option. The bottom of the list includes Inwood, Morningside Heights and several Brooklyn neighbourhoods (~$8–12k).

## Finding 3: What separates strong from weak performers

**Entire homes, split into revenue-proxy quartiles:**

| Quartile | Median price | Median reviews/mo | % Manhattan | % multi-listing host | Median days open | Median # reviews |
|---|---|---|---|---|---|---|
| Q1 (weakest) | $135 | 0.31 | 39% | 19% | 7 | 6 |
| Q2 | $149 | 1.00 | 44% | 26% | 76 | 15 |
| Q3 | $139 | 1.98 | 43% | 32% | 136 | 28 |
| Q4 (strongest) | $225 | 2.81 | 62% | 31% | 187 | 26 |

- **Weak performers have barely any bookings, and their calendars are mostly closed** (a median of 7 open days). Many look like occasional or semi-dormant hosts rather than poorly priced units.
- **Strong performers combine a higher price with high velocity.** A higher price does not cost much demand. Across entire-home price quintiles, median reviews/month is flat (1.26 → 1.03–1.12) and estimated occupancy falls only from 40% to 30%, while the revenue proxy rises from ~$12k to ~$41k. *Caveat:* expensive listings are probably larger or better units, so this doesn't show that raising price on a given unit is free.

**Regression on log reviews/month** (active listings, robust SEs, R² ≈ 0.28). It controls jointly for room type, borough, log price, minimum-night band, host portfolio size and availability band:

- **Minimum nights is the strongest factor.** Compared with 1-night minimums, review velocity is about 19% lower at 2 nights, 38% lower at 3, 55% lower at 4–6, 73% lower at 7–29 and 79% lower at 30+. Part of this is mechanical: longer stays mean fewer stays and fewer reviews per month.
- **An open calendar matters.** Any availability vs zero is associated with 2.0–2.7× the velocity. This mostly separates live listings from dormant ones.
- **Price:** a 10% higher price is linked to only about 1.7% lower velocity, holding the other factors fixed.
- **Room type:** private rooms are about 19% lower than entire homes after controls.
- **Host scale:** hosts with 2–5 listings are about 9–12% higher than single-listing hosts, which suggests that operating discipline helps. Hosts with 21+ listings are about 31% lower because they are mostly 30-night operators (68% of their listings).
- **Robustness:** the results are the same in direction and similar in size when I keep only listings with at least 6 reviews, where velocity is less noisy.

## Finding 4: Professionalisation and the two operating models

- 34% of listings belong to hosts with more than one listing. The top hosts are companies: Sonder (327 + 96 listings, short stays, almost all entire homes), Blueground (232, all 30+ nights), Corporate Housing (91, 30+ nights) and several 30+ night portfolios of 50–120 units in Manhattan.
- Among short-stay listings (under 30-night minimums), large hosts (21+ listings) have the highest median revenue proxy, about $25k vs $10–12k for others. That points to professional pricing and premium Manhattan units. The sample is small, though: 428 listings, dominated by Sonder.

## Risks and caveats

- **Regulatory (highest stakes, from outside the data):** short stays of entire units in NYC face severe legal limits, and Local Law 18 enforcement since 2023 has, to my knowledge, removed much of the short-stay supply. A 2019 file can't show today's legal, competitive or price landscape. Treat any short-stay entire-home plan as high risk until counsel and current data confirm it.
- **Stale data:** prices, demand, competitors and even which operators still exist will all have changed since 2019. Use these findings only for relative patterns: which locations and formats perform better.
- **Proxy risk:** reviews are a noisy, biased stand-in for bookings. Long-stay guests review less often. The revenue proxy for 30+ night listings (median ~$20k at a 64% estimated occupancy, with 47% hitting the 70% cap) depends heavily on the 30-night stay assumption and **should not be relied on**.
- **Selection:** listings that perform well differ in unobserved ways (size, quality, photos, ratings), and none of these are in the file. The associations above aren't causal effects.

## Recommendations

1. **Before any decision, get a current listing and calendar dataset** (post-2023) and a legal opinion on permitted formats. Re-run this analysis on that data.
2. **Lead with legally robust formats:** 30+ night furnished entire units (the Blueground and corporate-housing model), and possibly host-present private rooms. Avoid building a strategy on sub-30-night entire homes.
3. **Location:** target the Manhattan neighbourhoods with high revenue proxies and deep markets (Financial District, Hell's Kitchen, Midtown, Chelsea, Murray Hill). Use East Harlem as the value option. Outer boroughs book well but earn roughly half as much per unit.
4. **Operating levers in your control:** keep calendars open, keep minimum stays as short as the law allows, and price toward the top of the local range. Demand in this data is not very price-sensitive across quality tiers. Run a professional, multi-unit operation: mid-size hosts show higher velocity than single-listing hosts.
5. **Size the opportunity on active listings only.** About 40% of 2019 supply was inactive, so headline counts overstate the competition.
