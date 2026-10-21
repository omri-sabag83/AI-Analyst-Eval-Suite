# NYC Short-Term Rental Market Entry: Analysis of Airbnb Listings

**Data:** `listings.csv` has 48,895 NYC Airbnb listings from 37,457 hosts. It is a single snapshot: the latest review date is 8 July 2019, so it shows the market as of mid-2019. It is not a trend, and it predates COVID and later regulation. All figures below need re-checking against current data before any investment decision.

## Summary

1. **About half of the listed supply is inactive.** Only 45% of listings had a review in the 90 days before the snapshot. 21% have never been reviewed and 20% have had no review for over a year. The number of listings overstates the real competition by about 2x.
2. **Minimum stay is the clearest difference between listings that perform well and those that perform poorly.** Among mature, active listings, those that require 1 night get about 2.6 reviews a month. Those that require 30 nights or more get about 0.4. This holds after controlling for room type, borough, price, host size and listing age. Low price and open calendars also help. Borough has almost no effect on how often a listing is booked, but it strongly affects price.
3. **Most revenue is in Manhattan entire homes.** The estimated median revenue is about $2,200 a month for active Manhattan entire homes and about $1,700 in Brooklyn and Queens. Hell's Kitchen, Financial District, Midtown, Murray Hill and Chelsea are the top neighbourhoods (about $2,500–3,200 a month). This is an **estimate** built from reviews, not observed revenue.
4. **The biggest risk is regulation, not demand.** 45.5% of all listings are entire homes rented for under 30 nights. That is the segment a company scaling in NYC would rely on, and it is the segment NYC law restricts (see Risks). The large professional operators already in the data have mostly moved to 30-night minimums. Those listings have far fewer reviews, so this dataset can't show how well they actually perform.

## How "performance" was measured (assumptions)

The file has no occupancy, booking or revenue fields, so I used proxies:

- **Activity status:** days from the last review to 8 Jul 2019. "Active" means a review within 90 days.
- **Booking velocity:** `reviews_per_month`. I only use it for **mature active** listings: at least 6 months of review history (number_of_reviews ÷ reviews_per_month) and a price of $20–$1,000. That leaves n = 16,226. I excluded new listings because they show inflated rates from only a few early reviews.
- **Revenue estimate:** nights per month = reviews_per_month ÷ 0.5 (an assumed 50% review rate) × max(minimum_nights, 3), capped at 70% occupancy. Revenue = estimated nights × price. I applied it to active listings with minimum stays under 30 nights (n = 21,103). 23% of these hit the cap, so the top end is compressed. Use these figures for comparing segments, not as forecasts.
- `price` is the listed nightly rate, not the price actually paid. I set aside 11 listings at $0 and 239 above $1,000 (up to $10,000) as unreliable.
- `availability_365 = 0` (36% of listings) is ambiguous: the calendar could be fully booked or blocked by the host. Activity patterns suggest it mostly means blocked or inactive: 48% of never-reviewed listings show 0.

## Findings and evidence

### 1. Listed supply overstates real competition

| Status at snapshot | Share of listings |
|---|---|
| Reviewed in last 90 days | 45.5% |
| Last review 3–12 months ago | 14.2% |
| Last review over 12 months ago | 19.8% |
| Never reviewed | 20.6% |

Manhattan has the highest share of inactive listings (only 42% active). Staten Island has the lowest (67% active), followed by the Bronx (58%). 85% of all listings are in Manhattan or Brooklyn.

### 2. What separates strong from weak listings

**Regression on mature active listings.** The outcome is log(reviews per month). The effects below are adjusted for room type, borough, log(price), minimum-nights band, host listing count, zero availability, availability days and years of review history. R² = 0.23, n = 16,226, with robust standard errors.

| Factor (vs. reference) | Adjusted effect on reviews/month |
|---|---|
| Min nights 2 (vs 1) | −22% |
| Min nights 3 | −37% |
| Min nights 4–7 | −55% |
| Min nights 8–29 | −75% |
| Min nights 30+ | −74% |
| Availability = 0 days | −43% |
| Host with more than 20 listings (vs 1) | −50% |
| Host with 2–5 listings (vs 1) | +7% to +10% |
| Private room (vs entire home) | −16% |
| Shared room (vs entire home) | −33% |
| Price +10% (within the other controls) | about −1.6% |
| Manhattan (vs Bronx) | +9% (p = 0.03). Other boroughs are not significant. |

Raw medians tell the same story. Mature active listings get 2.56 reviews a month at 1-night minimums, 1.51 at 3 nights, 0.99 at 4–7 nights and 0.39 at 30+ nights.

How to read this:
- Part of the minimum-stay effect is mechanical: longer stays produce fewer reviews per night booked. Even so, short minimums are clearly linked to being active at all. 48–57% of 1–2-night listings are active, compared with 24% of 30+-night listings, and 39% of 30+-night listings have never been reviewed.
- Bookings fall only slightly as price rises (about −0.16% per 1% price increase). So a higher-priced listing in a good location brings in more revenue rather than less: within each room type, the top revenue quintile has about double the median price of the bottom quintile ($260 vs $130 for entire homes).
- Hosts with 2–5 listings do slightly better than one-listing hosts. A one-listing host is the group most likely to be dormant (24% have had no review for over a year), which suggests casual hosts who list occasionally. Hosts with more than 20 listings look weak on reviews only because most of them run 30-night corporate stays. For example, Blueground (232 listings), Kara (121) and Kazuya (103) all have a median minimum stay of 30 nights and a median of 0 reviews.

**Top vs bottom revenue quintile among active entire homes:** median price $260 vs $130; 3.15 vs 0.52 reviews a month; 66% vs 36% in Manhattan; minimum stay of 2 vs 3 nights; open calendar of 187 vs 35 days a year. The pattern for private rooms is similar. **Strong listings are priced up, centrally located, accept short stays and keep their calendars open.**

### 3. Where the revenue is (estimated, active listings with minimum stays under 30 nights)

| Borough | Entire home: median price / est. nights/mo / est. revenue/mo | Private room: median est. revenue/mo |
|---|---|---|
| Manhattan (n = 4,801 entire) | $199 / 12 / **$2,234** | $1,129 |
| Brooklyn (4,535) | $149 / 12 / $1,702 | $720 |
| Queens (1,172) | $122 / 15 / $1,660 | $752 |
| Bronx (243) | $100 / 16 / $1,468 | $631 |
| Staten Island (124) | $100 / 13 / $1,381 | $476 |

Outer-borough listings get booked as much as Manhattan or more, but revenue follows price. The top entire-home neighbourhoods (at least 50 active listings) by median estimated revenue are Hell's Kitchen ($3,194), Financial District ($3,149), Midtown ($2,836), Murray Hill ($2,820), Chelsea ($2,554) and SoHo ($2,484). Long Island City ($2,069, with high booking velocity) is the strongest area outside Manhattan. The weakest include Greenpoint, Prospect Heights and Flatbush (about $1,200–1,300).

## Risks

1. **Regulation (highest).** This is outside knowledge, not something the data shows: New York State's Multiple Dwelling Law prohibits renting a whole apartment in a building with 3 or more units for under 30 days unless the permanent resident is present. NYC's Local Law 18 (enforced since 2023) added mandatory host registration and has sharply reduced short-term supply. In this data, 45.5% of listings (about 22,250) are entire homes with minimum stays under 30 nights. These are the listings that perform best on the measures above, and they are the ones most legally exposed. The large operators in the file appear to have already moved to 30-night stays.
2. **Data vintage.** The data is a 2019 snapshot with no trend information. Demand, prices and supply have very likely changed since then, especially after COVID and Local Law 18.
3. **Proxy risk.** Every performance measure here comes from reviews. Reviews per stay vary by guest type and stay length, and listed prices may differ from the prices actually paid.
4. **Competition from professional operators.** Large operators are already present, for example Sonder (327 listings, 2-night median minimum) and Blueground (232, 30-night).

## Recommendations

1. **Get the legal position settled before anything else.** Don't build a growth plan around entire-home stays of under 30 nights in multi-unit buildings unless legal counsel confirms a compliant route, such as eligible 1–2 family homes, hotel-zoned or licensed buildings, or host-present arrangements.
2. **If compliant short stays are possible,** focus on central Manhattan entire homes: Hell's Kitchen, Financial District, Midtown, Chelsea and Murray Hill. Set minimum stays to 1–2 nights, keep calendars open and price at the upper end. Long Island City is a lower-cost alternative with high booking velocity.
3. **Otherwise, consider the 30+-night furnished-rental model** that Blueground-style operators use. This dataset can't measure its performance, so separate demand data is needed first.
4. **Size the opportunity using active supply** (about 22,000 listings with a review in the last 90 days), not the 49,000 listed.
5. **Before committing capital, get better data:** current listings with occupancy or calendar data, actual revenue (for example from a data vendor or a pilot portfolio), and the current registration and licensing rules.
