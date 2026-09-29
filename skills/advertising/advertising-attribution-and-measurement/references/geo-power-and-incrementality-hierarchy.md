# Geo power and incrementality hierarchy

Read when designing a geo or matched-market test that must be powered and have its markets chosen on evidence, or when explaining to a client how strong each kind of incrementality evidence is and which assumptions it rests on. Parent: [advertising-attribution-and-measurement](../SKILL.md).

## 1. The incrementality hierarchy

The IAB and IAB Europe *Guidelines for Incremental Measurement in Commerce Media* (November 2025) rate four method families by causal strength (register `IAB-INCREMENTAL-COMMERCE-MEDIA-2025`):

| Rank | Family | Examples | Causal strength (IAB) | Engine use |
|---|---|---|---|---|
| 1 | Experiment-based | Randomised holdouts, ghost ads, matched markets | Strong | Proving that a channel causes sales; calibrating models |
| 2 | Model-based counterfactual | Synthetic control (GeoLift), propensity models | Strong to moderate | Geo tests with few areas; retrospective reads |
| 3 | Econometric | Marketing mix modelling, time-series regression | Moderate to weak | Cross-channel budget allocation; route to [marketing-mix-modelling](../../marketing-mix-modelling/SKILL.md) |
| 4 | Hybrid proxies | Baseline versus exposed, platform-reported incrementality, simple multi-touch | Weak | Fast in-flight tuning only, with the limit stated |

The guidance asks that the method follow the business question, not the tool available, and that high-stakes decisions such as budget allocation and proving ROI use stronger causal methods.

## 2. Assumptions to disclose with any lift result

The IAB guidance sets three conditions for a causal claim: a credible counterfactual, control of bias and separation of signal from noise. With every result, state:

- the counterfactual (who or where saw no ads, or less);
- how the control was chosen (random, matched, synthetic);
- known contamination (national radio, commuters, other platforms reaching the control);
- confounders controlled and those not controlled (price, stock, competitor activity, outages);
- the interval around the lift and whether it excludes zero;
- test length and whether carry-over after the test was measured.

## 3. Powering a geo test and choosing markets

Tools: Meta's open-source GeoLift (R) provides synthetic-control inference, power analysis and data-driven market selection (register `META-GEOLIFT`); Google Ads Conversion Lift offers user-based and geography-based studies but is not self-serve (register `GOOGLE-CONVERSION-LIFT`). Meta advises people-based tests where possible because they have more statistical power than geo tests (register `META-GEOLIFT`).

Procedure:

1. **Decision and minimum detectable effect.** Write the decision the test informs and the smallest lift that would change it, for example "a 10% sales lift in test regions justifies adding the second radio station" (illustrative).
2. **Pre-period data.** Collect daily or weekly outcomes per area; GeoLift's documentation suggests a pre-treatment period ideally four to five times the test length (register `META-GEOLIFT`). Flag outage, holiday and stock-out days.
3. **Candidate markets.** List every area with its own outcome series and media that can be switched on or off independently (regional radio, outdoor, geo-targeted digital). Exclude areas reached by media you cannot control.
4. **Market selection.** Rank candidate test sets by how well the remaining areas reproduce their pre-period (synthetic-control fit), their share of total sales and practical constraints (distribution, sales team coverage).
5. **Power simulation.** For each candidate set, simulate test length, spend level and effect size against historical noise; keep designs that detect the minimum effect with acceptable power and false-positive rate, then choose the cheapest.
6. **Pre-register.** Hypothesis, markets, duration, spend, primary metric, guard-rail metric, analysis method and the action if the result is above, below or inside the uncertain zone.
7. **Run and read.** Hold spend steady in control areas; record contamination; report lift with its interval and the disclosed assumptions in §2.

Worksheet row per design: test markets | control markets | pre-period weeks | test weeks | spend (UGX) | minimum detectable effect | simulated power | fit error | constraints.

## 4. East Africa limits

- Few independent areas: Kampala, Wakiso and Mukono share commuters and media; national radio reaches everywhere. Prefer regional stations, outdoor or geo-targeted digital as the tested lever.
- Sales recorded only nationally or by distributor make area outcomes hard to get; ask for distributor or branch sell-out by area before promising a geo test.
- When no powered design exists, say so, run an on-off test with a long baseline and label the result weak evidence.

## Sources

`IAB-INCREMENTAL-COMMERCE-MEDIA-2025`, `META-GEOLIFT`, `GOOGLE-CONVERSION-LIFT`.
