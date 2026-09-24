# Search optimisation and audit

When to read: when auditing an existing account (read-only) or running the weekly and monthly optimisation cycle after an authorised launch.

## 1. Read-only audit sequence (rank findings by money at risk)

1. Tracking: do conversion actions fire once per real action; are primary and secondary actions separated; is consent handled for EEA/UK/CH traffic?
2. Spend concentration: which campaigns and themes carry most spend; what share converts?
3. Search terms: irrelevant queries, missing negatives, brand leakage into generic campaigns.
4. Structure: themes vs landing pages; ad groups that mix intents.
5. Ads and assets: message match with queries and pages; asset coverage; policy-limited ads.
6. Landing pages: message match, speed, mobile usability, form or WhatsApp friction (route fixes via `ad-to-site-journey-handoff`).
7. Bidding and budgets: strategy vs available conversion data; budget-limited winners; spend on losers.
8. Performance Max: channel performance reporting, brand exclusions, search themes, asset quality (AD-05).
9. Reporting: are brand and non-brand, and demand harvesting vs generation, reported separately?

Output each finding as: observation, evidence (export and date), estimated money at risk (range), fix, owner, check to confirm.

## 2. Weekly cycle

- Search terms review → add negatives, split new themes.
- CPA vs break-even per theme → one change per theme per window.
- Asset and ad checks → replace clear losers; keep a control.
- Conversion anomalies → check tags before changing campaigns.
- Log every change with date and reason.

## 3. Monthly cycle

- Theme-level economics: spend, conversions, CPA, value, trend against the line in the sand.
- Landing-page tests handed to the website team; read results.
- Budget re-allocation from losing to winning themes; scale winners in steps and watch CPA.
- Incrementality check where volume allows: brand-campaign holdout or geo split (see `advertising-attribution-and-measurement`).

## 4. Diagnostic order when CPA is too high

1. Query quality (are we paying for the wrong intent?)
2. Ad relevance (does the ad promise what the query asked?)
3. Landing page (does the page deliver on the ad; is it fast; is the action easy?)
4. Offer (is the offer competitive and clear?)
5. Bid and budget (only after 1–4)

Record each step's evidence; change one variable per window.

## 5. Kill and scale lines

- Kill or pause a theme when CPA stays above the break-even line for the agreed window after query, ad and page fixes.
- Scale a theme when CPA sits below the line for the agreed window with stable conversion quality; raise budget in steps and re-read before the next step.
- Channel decay is normal (all channels lose efficiency as they crowd); keep small tests running for the next theme (Weinberg & Mares 2014).

## 6. Monthly report skeleton

Executive summary (objective, spend, qualified conversions, CPA vs break-even) · brand vs non-brand · theme table · search-terms learnings · landing-page learnings · tests run and decisions · next month's plan with lines in the sand. State what the data cannot prove (e.g. last-click credit, modelled conversions under consent).
