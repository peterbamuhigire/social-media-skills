# Calibration and geo experiments

Read when turning experiment results into MMM priors or calibration targets, or when planning the geo test that will supply them, including power analysis and market selection. Parent: [marketing-mix-modelling](../SKILL.md).

## 1. Why calibrate

An MMM estimates channel effects from correlations in history; an experiment measures a causal effect for one channel, period and population. Meridian's guidance treats incrementality experiments as "perhaps the strongest basis" for setting ROI priors, while warning that different experiments can give different results and that there is no single formula to turn a result into a prior (register `GOOGLE-MERIDIAN-CALIBRATION`). Robyn uses experiment results as a third optimisation objective (MAPE against lift results) beside fit error and decomposition distance (register `META-ROBYN-ANALYST-GUIDE`).

## 2. Relevance check for each experiment (before it becomes a prior)

Adapted from Meridian's calibration page (register `GOOGLE-MERIDIAN-CALIBRATION`):

| Check | Question | If it fails |
|---|---|---|
| Recency | Did the test run inside the MMM window? | Widen the prior or drop the test |
| Duration | Did it last long enough to catch carry-over effects? | Treat it as a lower bound |
| Granularity | Does it measure the same channel grouping as the model? | Map carefully or drop |
| Population | Was the tested audience or area typical of the whole market? | Widen the prior; say which population it covers |
| Estimand | Did it compare against zero spend (the MMM counterfactual) or against a lower spend level? | Convert, or record the difference as an assumption |

Meridian provides a `CalibrationBuilder` for recency, duration and granularity adjustments and Meridian GeoX for geographic representativeness through stratified sampling (register `GOOGLE-MERIDIAN-CALIBRATION`). Record which, if any, was used.

## 3. Sources of experiment evidence

| Method | What it is | Status and caveat | Register |
|---|---|---|---|
| Geo holdout or matched markets | Ads on in some areas, off or lower in matched areas | Works for radio, outdoor and offline sales; needs enough comparable areas | `IAB-INCREMENTAL-COMMERCE-MEDIA-2025` |
| Meta GeoLift | Open-source R package for geo experiments using synthetic control methods, with power analysis and data-driven market selection | Research tool, not an official Meta product; Meta advises people-based tests where possible because they have higher power | `META-GEOLIFT` |
| Google Ads Conversion Lift | User-based or geography-based lift study; the geo version supports offline conversions | Not self-serve and not available to all accounts; request through a Google account representative | `GOOGLE-CONVERSION-LIFT` |
| Platform on-off or time-series read | Channel switched off for a period against a baseline | Weakest design; label it and use only as a wide prior | `IAB-INCREMENTAL-COMMERCE-MEDIA-2025` |

## 4. Planning a geo test: power and market selection (summary)

The full procedure, with the worksheet, is in [geo power and incrementality hierarchy](../../advertising-attribution-and-measurement/references/geo-power-and-incrementality-hierarchy.md). In short:

1. State the decision and the smallest lift that would change it (the minimum detectable effect).
2. Gather a pre-period of daily or weekly outcomes by area; GeoLift's documentation suggests a pre-treatment period ideally four to five times the test duration (register `META-GEOLIFT`).
3. Choose candidate test markets by how well the others can reproduce their history (synthetic control fit), not by convenience.
4. Simulate power for each candidate set, test length and spend level; pick the smallest, cheapest design that detects the minimum effect.
5. Pre-register hypothesis, markets, duration, spend and the decision rule.
6. Guard against spill-over: media that crosses area boundaries (national radio, TV, commuters between Kampala and Wakiso or Mukono).

East Africa note: with only two or three distinct regions and national radio, a true geo test may be impossible. Use regional stations or outdoor, an on-off design with a long baseline, or a platform lift study where the account is eligible, and widen the resulting prior.

## 5. Writing the calibration plan

For each channel: experiment used (or planned), date, result with its interval, relevance-check result, how it enters the model (prior, calibration target or none) and the prior width. Channels with no experiment are marked "model only" in the client report.

## Sources

`GOOGLE-MERIDIAN-CALIBRATION`, `META-ROBYN-ANALYST-GUIDE`, `META-GEOLIFT`, `GOOGLE-CONVERSION-LIFT`, `IAB-INCREMENTAL-COMMERCE-MEDIA-2025`.
