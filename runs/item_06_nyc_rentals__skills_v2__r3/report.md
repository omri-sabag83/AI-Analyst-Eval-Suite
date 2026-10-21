# NYC Short-Term Rental Market Entry: What the Airbnb Listing Data Shows

## Bottom line

1. **Most of this market is dormant.** Of 48,895 listings, only **49% (24,131) had a review in the six months before the snapshot**. 21% have never been reviewed and 20% were last reviewed over a year earlier. Treat headline counts as "inventory on the site", not as active competitors.
2. **Revenue comes from entire homes in Manhattan, with a few Queens and Brooklyn outliers.** Among active listings, an entire home earns about **2.2x the estimated revenue of a private room** (median ~$20k vs ~$9k a year), after adjusting for borough, price position, minimum stay and host size. Manhattan earns the most per listing. Outer-borough entire homes (Queens, Bronx) get booked more often but at much lower prices.
3. **What separates strong listings from weak ones is mostly what the operator controls:** short minimum stays, mid-to-upper pricing *for the neighbourhood*, and staying active. Location and room type set the revenue ceiling.
4. **Regulation is the biggest risk to the entry plan, and it is concentrated in exactly the segment that pays best.** 88% of entire-home listings accept stays under 30 nights. New York State law generally prohibits renting an entire apartment for under 30 days when the permanent resident is not present (external context, not in the data). The large professional operators in this file already appear to have moved to 30-night minimums. A business model built on short-stay entire homes needs legal review before money is committed.

---

## Data and how "performance" was measured

- **Source:** `listings.csv`, 48,895 listings and 16 fields (location, room type, nightly price, minimum nights, review counts, host listing count, availability). It is a single snapshot. The latest review date is **8 July 2019**, so the data is several years old and **cannot show trends**. Current conditions need re-checking.
- **What the data lacks:** bookings, occupancy, revenue, ratings, amenities, size, and the photos or description quality. Performance therefore has to be inferred.
- **Main performance measure: `reviews_per_month` (RPM)**, the usual demand proxy, since each review stands for a stay. Its limits:
  - It counts **stays, not nights**. A 30-night-minimum listing can be fully booked and still collect ~1 review a month. RPM unfairly penalises long-stay listings.
  - It is averaged over the listing's whole life, so it **inflates new listings and deflates old ones**. RPM falls from ~1.85 for listings under 6 months old to ~0.33 for those over 4 years. To limit this, the analysis set was restricted to listings with at least 6 months of history, and listing age was included as a control.
- **Secondary measure: estimated revenue, which is a modelled ESTIMATE and not observed data.** Nights booked a month = RPM ÷ 0.5 (assuming half of guests leave a review) × max(minimum nights, 3), with occupancy capped at 70%. Revenue = occupancy × 365 × price. The *ranking* of segments holds up under other assumptions (review rate 0.3–0.72, average stay 3–4.5 nights), but the *dollar level* moves by roughly ±50%. Treat the dollar figures as relative. For 30+-night listings the estimate is weak: 52% of them hit the 70% cap.
- **`availability_365` was not used as a performance measure.** 36% of listings show 0 days available, and the data can't tell "fully booked" apart from "turned off". Activity was judged from review recency instead.
- **Analysis set (active listings):** reviewed within 180 days of the snapshot, price between $1 and $2,000, at least 6 months of history. **n = 17,706.** Excluded: 11 listings priced at $0 and 239 priced over $1,000 (outliers or data errors), plus inactive and too-new listings.

---

## Finding 1: About half the supply is inactive

| Listing status (all 48,895) | Share |
|---|---|
| Reviewed in the last 6 months | 49.4% |
| Last reviewed 6–12 months ago | 10.3% |
| Last reviewed more than 1 year ago | 19.8% |
| Never reviewed | 20.6% |

- Manhattan has the lowest active share (46%), so its listing count overstates competition the most. Staten Island (70%), the Bronx (62%) and Queens (59%) have higher active shares but small markets (373, 1,091 and 5,666 listings).
- 69% of listings are in Manhattan or Brooklyn.

**What this means:** real competition is about half of what the listing count suggests. It also means listing a property does not guarantee demand. About 1 in 5 listings never gets a single booking that leads to a review.

## Finding 2: Room type and borough set the revenue ceiling

Active analysis set, medians:

| Borough / room type | n | Nightly price | Reviews/mo | Est. occupancy | Est. annual revenue |
|---|---|---|---|---|---|
| Manhattan, entire home | 4,092 | $180 | 1.10 | 35% | ~$23k |
| Brooklyn, entire home | 4,056 | $145 | 1.52 | 39% | ~$19k |
| Queens, entire home | 917 | $119 | 2.11 | 47% | ~$18.5k |
| Bronx, entire home | 183 | $102 | 2.32 | 53% | ~$17.6k |
| Manhattan, private room | 2,770 | $90 | 1.73 | 42% | ~$13k |
| Brooklyn, private room | 3,485 | $65 | 1.43 | 35% | ~$8k |
| Queens, private room | 1,365 | $59 | 1.76 | 40% | ~$8.4k |

- **Booking frequency and revenue rank boroughs differently.** Queens and the Bronx book most often, but Manhattan earns the most per listing because of price. Holding other factors fixed, Manhattan listings earn about **74% more** estimated revenue than Bronx listings (regression coefficient 0.55 on the log scale). Brooklyn earns about 25% more and Queens about 16% more.
- **Room type is the strongest single factor.** Private rooms earn about **55% less** than entire homes after controls; shared rooms earn about 77% less. Private rooms get only slightly *more* reviews per month (median 1.61 vs 1.36), so the price gap is not made up by more frequent bookings.
- **Neighbourhoods that stand out for entire homes** (at least 30 active listings): Tribeca, Financial District, Hell's Kitchen, SoHo, Midtown and Chelsea (about $26–38k estimated). Queens has notable outliers: Woodside, Elmhurst, East Elmhurst and Long Island City reach about $25–29k on 50–70% estimated occupancy. This may reflect demand from LaGuardia airport, but that is a hypothesis. Brooklyn's Greenpoint, Prospect Heights and Brooklyn Heights rank lowest (about $13k), mainly because of low booking frequency.
- For private rooms, Hell's Kitchen (~$21.6k), Chelsea, Midtown and Chinatown lead.

## Finding 3: What separates strong performers from weak ones

Two multivariable regressions on the analysis set: log reviews per month (R² 0.22) and log estimated revenue (R² 0.33). Both control for borough, room type, minimum stay, host size, price position within the neighbourhood and room type, and listing age. Most of the variation is unexplained, which is expected without data on quality, photos or ratings.

**a) Minimum-stay policy is the strongest driver of booking frequency.** This holds within every room type:

| Minimum nights | Median reviews/mo (entire home) | Median reviews/mo (private room) |
|---|---|---|
| 1 | 2.59 | 2.36 |
| 2 | 1.93 | 1.81 |
| 3 | 1.45 | 1.31 |
| 4–7 | 0.92 | 0.91 |
| 8–29 | 0.45 | 0.49 |
| 30+ | 0.33 | 0.45 |

- 78% of top-quartile listings (≥2.8 reviews a month) have a minimum of 2 nights or less, compared with 46% of the rest.
- Part of this is built into the measure: fewer, longer stays produce fewer reviews. On estimated revenue, which accounts for stay length, **3–7-night minimums do worst** (about 20–30% below 1-night listings after controls). 30+-night listings appear to earn the most, but that estimate is unreliable (the 70% cap binds for half of them).
- *Interpretation:* listings take either nightly or monthly demand. The middle ground (3–7-night minimums) gets fewer bookings than nightly listings without the reliability of monthly lets.

**b) Pricing against the neighbourhood: mid-to-upper prices do best.** Each listing was ranked by price against the same room type in the same neighbourhood:
- The **cheapest fifth gets the fewest reviews** (median 1.25 a month vs 1.66 for the middle fifth) **and earns the least** (~$8.9k vs ~$14.5k).
- The priciest fifth gets somewhat fewer bookings but the highest revenue (~$20k), because price outweighs the lost volume.
- *Caveat:* price stands in for unobserved quality (size, finish, location within the neighbourhood). This does **not** show that raising prices raises revenue. It shows that being cheap is not what makes a listing perform well, and very cheap listings are often a warning sign.

**c) Host scale: small multi-listing hosts do best and very large portfolios do worst.**

| Host listing count | Share of all listings | Never reviewed | Median reviews/mo (active) |
|---|---|---|---|
| 1 | 66% | 22% | 1.41 |
| 2 | 14% | 14% | 1.73 |
| 3–5 | 11% | 12% | 1.73 |
| 6–20 | 5% | 22% | 1.38 |
| 21+ | 5% | **46%** | 0.30 |

- After controls, hosts with 2–20 listings earn about 8–9% more estimated revenue than single-listing hosts. **Hosts with 21+ listings earn about 19% less** and get about 50% fewer reviews per month.
- The largest operators include Sonder (327 + 96 listings), Blueground (232), Corporate Housing and others. Most have moved to **30-night minimums**, and many of their listings have never been reviewed (Blueground 88%, Sonder's second account 70%). This fits a pivot to monthly stays and/or units used on other channels. The data can't show which.
- *Implication for a company operating at scale:* running a large portfolio on Airbnb alone does not automatically outperform. The evidence suggests professional scale has been steered toward longer stays.

**d) Listing age.** Older active listings have lower lifetime RPM (coefficient −0.12 per log-month), which is mostly a measurement effect. RPM figures for new listings should be discounted.

## Finding 4: Risks

1. **Regulation (highest stakes; external context, not shown in the data).** New York State's Multiple Dwelling Law generally bars renting an entire unit for under 30 days without the permanent resident present. New York City actively enforces against illegal hotel use, and enforcement has tightened since this data was collected (the City's 2023 short-term rental registration rules). In this file, **88% of entire-home listings allow stays under 30 nights**. Among hosts with 3+ listings that share falls to **52%**, which suggests professional operators are already complying. The highest-revenue segment in Findings 2–3 (short-stay entire homes in Manhattan) is therefore the one most exposed to legal risk. Its revenue may not be achievable legally.
2. **Concentration of competition.** Manhattan and Brooklyn hold 69% of listings. Professional operators cluster in Manhattan entire homes.
3. **Activation risk.** About 20% of listings never get a review. A new entrant should plan for a slow start, since new listings have no review history.
4. **Data age and limits.** The data is a 2019 snapshot with no trend, no actual occupancy and no revenue. All revenue figures are modelled estimates.

## Recommendations

1. **Get a legal opinion before choosing a model.** Compare (a) **30+-night furnished rentals** of entire units, which fits what the professional operators here do and has revenue roughly in line with nightly lets under our estimates, with (b) **host-present private rooms** for nightly stays. Do not plan around sub-30-night entire-home rentals without legal approval.
2. **If going nightly (where permitted), prioritise Manhattan's Midtown/West side** (Hell's Kitchen, Chelsea, Midtown) for private rooms. Look at **Queens near the airport** (Woodside, Elmhurst, East Elmhurst, Long Island City) as a lower-cost alternative with high booking frequency.
3. **Operating playbook:** use 1–2-night minimums for nightly stays or a firm 30-night minimum for monthly ones, and avoid the 3–7-night middle. Price in the middle to upper part of the neighbourhood range rather than undercutting. Put effort into getting early reviews.
4. **Don't size the opportunity from listing counts.** Use the active-listing base (about half) and confirm demand with current booking data (for example a paid occupancy data source, or a pilot) before committing to a large portfolio.
5. **Refresh the analysis on current data.** Many facts here, especially regulation and the large operators' positions, have likely changed since 2019.

---

### Assumptions
- A review in the last 180 days counts as "active". About half of guests leave a review. Average stay is at least 3 nights or the minimum stay, whichever is longer. Occupancy is capped at 70%.
- Price is the listed nightly price (fees excluded). Listings priced at $0 or over $2,000 were excluded from performance analysis.
- The regulatory points are general domain knowledge, not data from this file, and need verification by counsel.
