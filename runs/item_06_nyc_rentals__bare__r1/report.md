# NYC Short-Term Rental Market Entry: What the Airbnb Listing Data Shows

## Bottom line

1. **Supply is large but much of it is dormant.** Of 48,895 listings, only **49% show any guest activity in the last 6 months**. 21% have never had a review and 30% have gone quiet. Raw listing counts overstate the competition and overstate what a typical listing earns.
2. **Good and poor listings differ in how bookable they are, more than in where they are or what they cost.** The strongest predictors of high demand are a **short minimum stay (1–2 nights)**, a **calendar that is actually open**, and a **price set near the local going rate for that room type**. After controlling for these, borough adds almost nothing to booking pace.
3. **The best cash yield is not in prime Manhattan.** Estimated revenue per listing is highest for entire homes in outer-borough areas with high demand: Bed-Stuy, East Flatbush, Flushing, Jamaica, and the areas around the JFK and LGA airports. Manhattan commands higher prices but has lower activity rates, more competition and more dormant listings.
4. **Regulation is the biggest risk.** **88% of entire-home listings accept stays under 30 nights.** Those are exactly the profitable listings, and they are the format most exposed to NYC's restrictions on short-term rentals. Large operators that use 30-night minimums show very weak activity on Airbnb.

**Recommendation:** Enter selectively and keep the operation compliance-first. Do not build a portfolio of entire-unit rentals that depends on sub-30-night stays without legal sign-off. Within a compliant model, compete on bookability (short minimum stays where allowed, open calendars, prices at the local median) rather than on location prestige. Treat the outer-borough demand clusters as the yield opportunity.

---

## Data and how "performance" was measured

- `listings.csv`: 48,895 listings, 37,283 hosts, 221 neighbourhoods in 5 boroughs. The latest review date is **8 July 2019**, so this is a mid-2019 snapshot.
- **The file has no occupancy or revenue figures.** I used reviews as a stand-in for demand:
  - **Active** = last review within 180 days of the snapshot date.
  - **Booking pace** = `reviews_per_month` among active listings.
  - **Estimated revenue** (indicative only) = reviews/month ÷ 0.5 (assuming about half of guests leave a review) × assumed stay length (the larger of the minimum stay and 3 nights). Nights per month are capped at 21 (70% occupancy), then multiplied by 12 × price. This is a common outside-analyst heuristic. Treat it as a way to rank listings, not as a forecast.
- **Exclusions:** 250 listings priced at $0 or above $1,000 per night were removed from the price and revenue analysis. They look like placeholders or errors. The data had no duplicate rows.
- **Caveats:**
  - Reviews undercount bookings for long stays, so 30+-night listings look worse on pace than they really are.
  - `availability_365` is partly an *outcome*: booked nights reduce it. Its link to performance is therefore descriptive, not causal.
  - The data is from 2019. Prices, demand and especially regulation have changed since then.

## Finding 1: Half the market is inactive

| Status | Share of listings | Median price | Median nights available per year | Share with 0 days available |
|---|---|---|---|---|
| Active (reviewed in the last 6 months) | 49% | $104 | 122 | 11% |
| Stale (last review more than 6 months ago) | 30% | $100 | 0 | 69% |
| Never reviewed | 21% | $120 | 5 | 48% |

Inactive listings mostly have closed calendars. Listings with 0 days available have only a 15% activity rate and a median estimated revenue of about $770 per year. The effective competing supply is therefore roughly 24,000 listings, not 49,000.

Revenue is very concentrated. **The top 10% of listings generate an estimated 46% of all revenue.** The "average" listing is a poor benchmark.

## Finding 2: What separates strong from weak listings

**Top vs bottom quartile of booking pace (active listings only; quartile cut-offs ≥2.9 vs ≤0.7 reviews per month):**

| | Top quartile | Bottom quartile |
|---|---|---|
| Minimum stay of 2 nights or less | **80%** | 34% |
| Minimum stay of 30+ nights | 1% | **16%** |
| Median nights open per year | 134 | 90 |
| Median price vs neighbourhood/room-type median | 1.00× | 0.99× |
| Share entire home | 51% | 56% |
| Share in Manhattan | 40% | 44% |
| Median price | $100 | $114 |

To separate these factors from each other, I fitted two models on the same set of drivers: borough, room type, minimum nights, host portfolio size, price relative to local median, and availability.

- **Logistic regression for "is active"** (all listings, pseudo-R² 0.28):
  - **Minimum stay:** compared with a 2-night minimum, the odds of being active are 0.48× for a 4–7 night minimum, 0.19× for 8–29 nights and **0.12× for 30 nights**.
  - **Pricing:** listings priced at more than 2× the local median have **0.36×** the odds of being active. Listings priced at 1.33–2× have 0.67×.
  - **Host portfolio:** hosts with 3–5 listings have **2.0×** the odds of single-listing hosts. Hosts with 21 or more listings have 0.73×.
  - **Calendar:** listings with any open calendar have 15–23× the odds of those with 0 days open. This is largely mechanical (dormant listings block their calendars).
  - **Borough:** the effects are modest, at 1.2–1.3× relative to the Bronx.
- **OLS regression of log reviews per month** (active listings only, R² 0.24):
  - **Minimum stay:** a 1-night minimum gives about 25% more reviews per month than 2 nights. Minimums of 4–7 nights give 43% fewer, and 30+ nights about 65–70% fewer.
  - **Pricing:** listings priced at more than 2× the local median get 23% fewer reviews per month.
  - **Borough:** Manhattan, Brooklyn, Queens and Staten Island are all within about ±6% of the Bronx and not significant.

**Implications:**

- **Price to the local median for the room type.** Listings priced at 0.75–1.33× the local median perform about equally well. Undercutting gains little: cheaper listings are slightly more likely to be active, but their booking pace is no faster. Big premiums cut demand sharply. Premium listings can still earn the most per listing, because their mean revenue is the highest, but the results are highly variable.
- **Mid-sized, professionally run hosts (2–20 listings) perform best.** About 62–71% of their listings are active, against 43% for single-listing hosts. This suggests that operational discipline (responsiveness, calendar management) pays off.
- **Very large hosts (21+ listings) perform poorly on Airbnb activity:** 35% active, 45% never reviewed. These are mostly corporate-housing operators with 30-night minimums (e.g. Blueground, 232 listings, 10% active). They likely book through other channels. Either way, a "list many units at 30-night minimums on Airbnb" model is not proven by this data.
- **Listing titles add a little:** titles that mention transit or airports ("subway", "JFK/LGA") are linked to higher booking pace. Titles stressing "luxury", "view" or "loft" are linked to lower pace. These effects are small and correlational.

## Finding 3: Where the opportunity is

Median price and estimated revenue by borough and room type:

| Borough | Median price, entire home | Median price, private room | Share active | Median est. revenue, entire home |
|---|---|---|---|---|
| Manhattan | $190 | $90 | 46% | $6.5k |
| Brooklyn | $145 | $65 | 50% | $7.6k |
| Queens | $120 | $60 | 59% | $9.9k |
| Bronx | $100 | $54 | 62% | $11.4k |
| Staten Island | $100 | $50 | 70% | $13.4k* |

\*Small sample (174 listings).

Manhattan's higher prices are offset by lower activity and more dormant competition. **Entire homes earn about 2.5× what private rooms earn at the median** (about $7.4k vs $2.9k estimated per year).

**Top neighbourhoods for entire homes** (at least 75 listings; ranked by median estimated revenue):

| Neighbourhood | Listings | Share active | Median price | Median est. revenue |
|---|---|---|---|---|
| Flushing (Queens) | 105 | 73% | $120 | $18.1k |
| East New York (Brooklyn) | 93 | 87% | $100 | $17.6k |
| Jamaica (Queens) | 80 | 79% | $100 | $14.9k |
| Canarsie (Brooklyn) | 75 | 79% | $110 | $14.9k |
| Bedford-Stuyvesant (Brooklyn) | 1,585 | 65% | $130 | $13.6k |
| East Flatbush (Brooklyn) | 187 | 72% | $109 | $13.6k |
| Financial District (Manhattan) | 572 | 52% | $220 | $13.4k |
| Hell's Kitchen (Manhattan) | 1,181 | 51% | $200 | $11.7k |

- **Bedford-Stuyvesant** combines scale with strong activity. **Hell's Kitchen and the Financial District** are the strongest parts of Manhattan.
- The areas near the airports (East Elmhurst, Jamaica) have the fastest booking pace in the city: 2.7–4.4 reviews per month for active listings, against a citywide median of about 1.5.
- **Weak spots** (all room types): Theater District, Morningside Heights, Washington Heights, Bushwick and Ridgewood. These have low median estimated revenue, driven by low activity and low prices.

## Risks

1. **Regulation (the biggest risk; this context comes from outside the dataset).**
   - NYC law broadly prohibits renting a whole unit in a multi-unit building for fewer than 30 days unless the host is present.
   - Since 2023, Local Law 18 requires host registration, and enforcement has sharply cut short-term supply.
   - In this data, **45% of all listings are entire homes accepting stays under 30 nights**, and 4,287 of those belong to multi-listing hosts. Those are the most profitable listings and the most exposed ones. Any revenue case built on the 2019 patterns above must be stress-tested against these rules.
   - The compliant alternatives (30+ night stays, host-present private rooms) perform much worse on Airbnb in this data.
2. **Dormant competition can come back.** About 25,000 inactive listings could be reactivated in peak periods, which caps pricing power.
3. **Results are uneven.** Revenue is concentrated, and the median listing earns little. Underwriting should assume median outcomes, not mean outcomes. For entire homes, the mean estimated revenue is about $15.8k and the median about $7.4k.
4. **The measurement is weak.** Review-based demand estimates rest on assumptions. Before committing capital, validate them with real occupancy and average daily rate data (e.g. from an operator or a third-party data provider).
5. **The data is old.** It is a 2019 snapshot, before COVID and before the 2023 rules. Use it for the direction of the patterns, not for current levels.

## Recommendations

1. **Commission a legal and compliance review first**, and decide the operating model from it: host-present rooms, 30+-day stays, or the few building types that are exempt. Do not underwrite on sub-30-night entire-home revenue.
2. **If the model allows short stays:**
   - Prioritise outer-borough demand clusters (Bed-Stuy, East Flatbush, Flushing, Jamaica and the airport areas) over prime Manhattan for yield.
   - Use Hell's Kitchen and the Financial District for any Manhattan presence.
3. **Run listings for bookability:**
   - Use the shortest minimum stay that is operationally viable.
   - Keep calendars open.
   - Price at about 0.9–1.3× the local median for the room type, and avoid premiums above 1.3× unless there is clear differentiation.
   - Put transit and airport access in listing titles.
4. **Learn from the 2–20-listing operators, the best-performing host segment**: professional operations at moderate scale. The very large 30-night operators show weak traction on this channel.
5. **Before any investment decision, validate with current data**: a fresh listing snapshot and actual occupancy and average daily rate figures.
