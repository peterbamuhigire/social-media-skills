# Data readiness and specification

Read when auditing whether a client can support a marketing mix model, writing the data specification, or planning around East African data gaps. Parent: [marketing-mix-modelling](../SKILL.md).

## 1. What the primary documents recommend

| Source | Recommendation (paraphrased, read 29 Sep 2026) | Register |
|---|---|---|
| Google Meridian, *Collect and organise your data* | At least two years of weekly data for geo-level models and three years for national models; at least three years if only monthly data exists; weekly is the preferred grain; KPI and media (except reach and frequency channels) must add up across geography and time | `GOOGLE-MERIDIAN-COLLECT-DATA` |
| Google Meridian, *Amount of data needed* | Two years of weekly national data against 26 parameters gives four points per parameter, which the page calls too low; its worked example reaches about 15 points per parameter, described as usable for directional results, by grouping channels, fewer time knots, dropping non-confounding controls or three years of data | `GOOGLE-MERIDIAN-DATA-AMOUNT` |
| Meta Robyn, *Analyst's guide to MMM* | At least two years of weekly history; with monthly data only, collect well over two years (the guide suggests four to five); observations should number roughly 7–10 times the independent variables | `META-ROBYN-ANALYST-GUIDE` |

These are the tools' rules of thumb, not guarantees. Anything shorter goes to degraded mode: an experiment plan and a data-collection timetable.

## 2. Readiness count (do this before promising a model)

1. Weeks of history with outcome and spend for every major channel.
2. Number of usable geographies (each with its own outcome and spend series).
3. Number of parameters: roughly channels × (effect, adstock, saturation) + controls + time-trend terms.
4. Data points per parameter = weeks × geographies ÷ parameters (the lenient view; partial pooling in geo models sits between the strict and lenient counts, as Meridian's page explains).
5. Verdict: go, go-with-limits (group channels, fewer controls, national model) or `NOT_ASSESSED`.

## 3. Series to specify

| Series | Grain | Notes |
|---|---|---|
| Outcome (KPI) | Week × geography | Sales value, units, orders or leads; say which and why |
| Revenue per KPI unit | Week | Needed to turn a count into ROI; approximate and label if not tracked |
| Media spend | Week × channel (× geography) | Same currency and tax treatment throughout |
| Media exposure | Week × channel | Impressions, GRPs, spots aired, outdoor faces live, or reach and frequency |
| Organic and owned activity | Week | Posts, WhatsApp broadcasts, PR; as organic media or controls |
| Non-media treatments | Week | Price, promotions, distribution points, stock-outs |
| Controls | Week | Only variables that move both sales and media timing |

Meridian needs complete series: zero-fill weeks when a channel was off, and interpolate or forward-fill gaps in outcome and controls rather than zero them (register `GOOGLE-MERIDIAN-COLLECT-DATA`).

## 4. Currency lock

- One reporting currency, UGX by default for Ugandan clients (KES, TZS or RWF for those markets).
- One exchange-rate rule for USD-billed platforms: for example the central bank's published rate on the invoice date, or its monthly average. Write the rule down and apply it to every week.
- Real or nominal: with material inflation over a three-year window, deflate spend and sales with the official consumer price index and state the base period. Confirm the index series at the time of use.
- Tax treatment: record spend consistently gross or net of VAT on non-resident digital services (register `UG-DIGITAL-TAX-ADS-2026`); finance treatment routes to the [Chwezi accounting doctrine](https://github.com/peterbamuhigire/chwezi-accounting-doctrine).
- Agency fees and production costs are either in every channel or in none.

## 5. External controls and events calendar

| Driver | East African examples | Treatment |
|---|---|---|
| Seasonality and holidays | Christmas and New Year, Ramadan and Eid, Easter, Martyrs' Day in Uganda | Tool's time trend plus holiday flags |
| School fees terms | Term openings, when household cash goes to fees; confirm each year's term dates | Weekly flag or control |
| Prices and promotions | Price changes, bundle offers, trade promotions | Non-media treatment |
| Distribution and stock | New outlets, stock-outs, distributor changes | Control; stock-out weeks flagged |
| Competitor activity | Competitor launches, heavy competitor radio | Control where data exist; otherwise log as omitted-variable risk |
| Internet shutdowns and platform blocks | Uganda's 2026 election-period suspension (register `UG-INTERNET-SHUTDOWN-2026`); Facebook access status (register `UG-FACEBOOK-ACCESS-2026`) | Event flag; never read as low digital effectiveness |
| Elections | Campaign periods shift attention, prices and media rates | Period flag |
| Weather and harvest | Rainy seasons, harvest income for agricultural clients | Control for agri, drinks, construction |
| Power and network outages | Regional outages that stop digital delivery | Event flag |

## 6. Adstock and saturation, in plain words

- **Adstock (carry-over):** an advert keeps working after the week it ran, fading over time. A radio burst in week 1 still lifts sales in weeks 2 and 3. The model estimates how fast the effect fades for each channel.
- **Saturation (diminishing returns):** each extra shilling in a channel buys less than the one before. The model estimates the curve, which is what makes budget reallocation advice possible.
- Tell the client: both are estimated from their own history, so short or flat spend histories give vague curves.

## 7. East Africa data constraints

| Constraint | What to do instead |
|---|---|
| Radio and outdoor are bought on monthly or annual contracts, not logged weekly | Rebuild weekly exposure from station flighting logs, spot certificates and site go-live dates; if not recoverable, treat as a control and say so |
| Sales close in cash, over WhatsApp or through distributors | Use the most complete outcome (distributor sell-in, POS, mobile-money receipts) and state the lag and coverage |
| Few clean geographies (Kampala versus upcountry; Nairobi versus the rest) | National model, or two or three large regions, calibrated with experiments; no claim of geo precision |
| Small budgets with long flat periods | Group channels; test with on-off or geo holdouts before modelling |
| Platform exports and reach figures are unstable or distorted by blocks (register `DATAREPORTAL-UG-KE-2026`) | Use spend and the client's own delivery logs; flag the affected weeks |
| One year of data or less | `NOT_ASSESSED`; experiment plan plus data-collection timetable to reach the floor |

## Sources

`GOOGLE-MERIDIAN-COLLECT-DATA`, `GOOGLE-MERIDIAN-DATA-AMOUNT`, `META-ROBYN-ANALYST-GUIDE`, `UG-INTERNET-SHUTDOWN-2026`, `UG-FACEBOOK-ACCESS-2026`, `UG-DIGITAL-TAX-ADS-2026`, `DATAREPORTAL-UG-KE-2026`.
