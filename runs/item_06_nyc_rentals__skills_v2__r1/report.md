# NYC Short-Term Rental Market Entry: What the Airbnb Listing Data Shows

**Data:** `listings.csv` has 48,895 NYC Airbnb listings. The most recent review is dated 2019-07-08, so this is a **single snapshot from about July 2019** and cannot show trends.
**Bottom line:** Demand is real, but roughly 40% of listed supply is dormant. The things that separate busy listings from quiet ones are mostly **how a listing is run** (short minimum stays, an open calendar, competitive pricing), not **where it is**. Manhattan entire homes earn the most per listing. The biggest risk is **regulatory**, not commercial: the operators already working at scale here run 30-night minimums, and the data shows that model gets far fewer bookings per listing.

---

## 1. How "performance" is measured, and its limits

The file contains **no revenue, occupancy or booking data**. Performance is therefore proxied by **reviews per month** (`reviews_per_month`), which tracks booking frequency.

- **Analysis set:** 29,080 listings with a review in the last 12 months and a price between $1 and $1,000. I excluded:
  - 10,052 listings with no reviews ever;
  - 9,691 listings whose last review is more than 12 months old;
  - 11 listings priced at $0 and 239 priced above $1,000 (likely placeholders or data errors; the maximum is $10,000).
- **Caveats on the proxy:**
  - Reviews count **stays, not nights**, so long-stay listings look worse than they are.
  - Not every guest leaves a review.
  - Very new listings can have inflated rates. To control for this, I repeated the main model on listings with at least 12 months of review history (16,810 listings). The conclusions did not change.
- **Revenue estimate (rough):** I estimated monthly revenue as follows:
  - stays per month = reviews per month ÷ 0.5 (I assumed about half of guests leave a review);
  - nights per month = stays × the larger of the minimum stay and 3 nights, capped at about 28.5 nights (95% of a month);
  - revenue = nights × listed price.

  This is an **estimate for ranking segments only**, not a forecast.
- **`availability_365` is ambiguous.** It means the number of open calendar days. A value of 0 (17,533 listings, 36%) does *not* mean "fully booked": 44% of those listings have no review in over a year, and another 28% have never been reviewed. Mostly they are switched-off listings. Because availability is partly an outcome of booking activity, I use it as a control, not as a lever.

## 2. Key findings

### F1. About 40% of listed supply is inactive
19,743 listings (40.4%) have either never been reviewed or not been reviewed in the past 12 months. The headline count of about 49k overstates real competition; the active market is about 29k listings. Dormancy is highest at the two ends of the host-size range:

| Listings per host | Dormant share |
|---|---|
| 1 (single hosts) | 46% |
| 2 | 28% |
| 3–5 | 20% |
| 6–20 | 28% |
| More than 20 | 56% |

### F2. Minimum-stay rules are the strongest differentiator
Among active listings, top-quartile listings (≥2.59 reviews per month) are compared with bottom-quartile listings (≤0.47):

| | Top quartile | Bottom quartile |
|---|---|---|
| Minimum stay ≤ 3 nights | **91%** | 47% |
| Minimum stay ≥ 30 nights | 1% | 18% |
| Median open days per year | 134 | 54 |
| Median price | $100 | $113 |
| Share that are entire homes | 51% | 57% |
| Share in Manhattan | 39% | 43% |

Location and room type look similar across the two groups; operating settings do not.

I also fitted a regression of log reviews per month on room type, borough, log price, minimum-stay band, host portfolio size and availability band (n = 29,080, R² = 0.28; robust standard errors). Holding the other factors constant, compared with a 1-night minimum:

| Minimum stay | Change in reviews per month |
|---|---|
| 2 nights | −20% |
| 3 nights | −39% |
| 4–7 nights | −59% |
| 30+ nights | −79% |

All of these are p < 0.001, and the pattern is the same in the ≥12-month-history subset. Part of this is the proxy itself: a 30-night stay produces one review where several short stays would produce several. So the gap in *nights booked* is smaller than the gap in reviews.

### F3. Price and room type matter, but less than how the listing is run
- **Price:** a 10% higher price goes with about 1.5% fewer reviews per month (price elasticity of review activity ≈ −0.16). Demand is not very price-sensitive, which favours higher prices where the market supports them.
- **Room type:** holding other factors constant, private rooms get 19% fewer reviews per month than entire homes, and shared rooms 33% fewer.
- **Borough:** once room type, price and the other factors are controlled for, borough effects are small. Manhattan is +10% (p = 0.007), Queens +8% (p = 0.04), and Brooklyn and Staten Island show no significant difference. In the ≥12-month subset, no borough effect is significant. On the raw numbers, outer boroughs look busier (median reviews per month: Staten Island 1.00, Bronx 0.87, Queens 0.76, Manhattan 0.28). That difference is driven by mix, mainly Manhattan's higher share of long-minimum and dormant listings, not by location.

### F4. Revenue per listing favours Manhattan entire homes
Estimated median monthly revenue for active listings (method in Section 1):

| Borough | Entire home | Private room | Shared room |
|---|---|---|---|
| Manhattan | **$1,854** | $934 | $786 |
| Queens | $1,512 | $663 | $293 |
| Bronx | $1,411 | $521 | $274 |
| Brooklyn | $1,373 | $567 | $293 |
| Staten Island | $1,345 | $401 | $191 |

Median *estimated* booked nights are similar across boroughs (about 9–12 per month), so the revenue gap comes mainly from price. Median entire-home prices are $191 in Manhattan, $145 in Brooklyn and $120 in Queens.

**Neighbourhoods with the highest estimated revenue for entire homes** (at least 30 active listings):

| Neighbourhood | Estimated median monthly revenue | Active listings |
|---|---|---|
| Theater District | ~$3.6k | 48 |
| Flatiron District | ~$3.0k | 33 |
| Financial District | ~$2.9k | 331 |
| Tribeca | ~$2.9k | 57 |
| Hell's Kitchen | ~$2.6k | 697 |
| Chelsea | ~$2.3k | 412 |
| Midtown | ~$2.2k | 517 |

There are also outer-borough niches with high booking frequency, probably airport-adjacent: East Elmhurst (about 4.0 reviews per month), Woodside and Springfield Gardens in Queens. Their prices are lower, but they have fewer competitors.

The **lowest** estimated revenue for entire homes is in Midwood, Kensington, Morningside Heights, Inwood and Brooklyn Heights (about $0.5–0.9k per month).

Treat these neighbourhood rankings as indicative only: some are based on small samples (30–60 listings), and they inherit the assumptions of the revenue estimate.

### F5. Large professional operators already run a 30-day model and score poorly on short-stay activity
- 38 hosts have more than 20 listings each, together holding 2,205 listings. They include Sonder (327 + 96 listings), Blueground (232) and Corporate Housing (91).
- Of their listings, 68% have minimums of 30 nights or more and 78% are entire homes.
- Their median is 0.05 reviews per month, and 56% are dormant. Holding other factors constant, they get 30–55% fewer reviews than single-listing hosts.
- Hosts with 2–5 listings do best: about 10–15% more reviews than single hosts, and the lowest dormancy (20–28%).
- 88% of *all* entire-home listings advertise minimum stays under 30 nights.

## 3. Risks

1. **Regulation (the most important risk; this context comes from outside the data).** New York State and City law generally bans renting an *entire* apartment in a multiple-dwelling building for less than 30 days unless the host is present. Enforcement has tightened since this snapshot; NYC's Local Law 18 host registration took effect in 2023. The pattern in F5 fits this: scale operators already avoid stays under 30 days, while the busiest segment in the data (entire homes with 1–3 night minimums) is the most legally exposed. A business plan that depends on that segment is a compliance bet, not a market bet. **Get legal review before committing.**
2. **The data is old and is one snapshot.** It is from 2019, before COVID and before the rule changes. It gives no trend, seasonality or post-2023 view.
3. **The proxy may mislead.** Reviews undercount long stays, and the revenue estimate depends on an assumed review rate of about 50% and on stay length. Rankings between segments are more reliable than the dollar levels.
4. **Crowded core areas.** The neighbourhoods with the highest revenue (Hell's Kitchen, Midtown, Chelsea, Financial District) also have the most active competitors (400–700 entire homes each).

## 4. Recommendations

1. **Settle the legal model first.** Choose one of: (a) a compliant 30+ day / corporate-housing model, like Blueground and Sonder; (b) host-present private rooms; or (c) stays under 30 days only in buildings that are legally permitted (e.g. 1–2 family homes or hotel-zoned buildings).
2. **If running a 30+ day model,** do not judge it by review counts. Build the business case on monthly rental rates and occupancy data from a source that records nights booked, not reviews.
3. **Where short stays are legal,** run listings the way top-quartile listings are run:
   - minimum stays of 1–3 nights;
   - calendars kept open (top-quartile median is 134 open days, against 54 for the bottom quartile);
   - prices near the neighbourhood median, since demand is not very price-sensitive so there is no need to undercut.
4. **Target Manhattan entire homes for revenue per unit:** Midtown West, Theater District, Financial District and Chelsea. Test airport-adjacent Queens (East Elmhurst, Woodside) as a lower-cost, high-frequency niche.
5. **Before investing, get better data:** a current scrape (2024 or later), calendar and occupancy data, and actual nightly revenue. That would confirm whether these 2019 patterns still hold under the current rules.

---
*Assumptions: snapshot date taken as 2019-07-08 (latest review date); "active" means a review within 365 days of that date; prices are nightly list prices in USD; revenue figures are illustrative estimates, not observed earnings; the regulatory context comes from general knowledge, not from this file.*
