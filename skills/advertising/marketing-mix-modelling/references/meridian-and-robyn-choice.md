# Meridian and Robyn choice

Read when choosing the open-source tool, the model form and the validation rules for a marketing mix model. Parent: [marketing-mix-modelling](../SKILL.md).

## 1. Status when read (29 Sep 2026)

| Tool | What the primary pages say | Register |
|---|---|---|
| Google Meridian | Open-source MMM framework for advertisers to run in-house models; Bayesian causal inference with MCMC (No-U-Turn sampler); geo-level or national models; reach and frequency; experiment calibration; budget optimisation and scenario planning; Python 3.11 to 3.13; Apache-2.0; version 2.1.0 listed on GitHub | `GOOGLE-MERIDIAN-REPO` |
| Meta Robyn | Ridge regression to handle collinearity and overfitting; Nevergrad evolutionary hyperparameter search with multi-objective optimisation; calibration with geo, lift and other ground-truth results; no personal data or cookies needed; R is the production version, Python is a beta translated with a language model that "might encounter bugs"; MIT licence; labelled experimental | `META-ROBYN` |

Check the repositories again at the time of use: versions, Python support and maintenance status change.

## 2. Choosing

| Situation | Lean towards | Reason |
|---|---|---|
| Several clean geographies with their own sales and spend | Meridian geo model | Hierarchical pooling across geos adds information |
| Only national data | Either; Meridian national needs three years of weekly data by its own guide | Fewer points; priors and grouping matter more |
| Strong experiment results to encode as ROI priors | Meridian | Priors are the native calibration route (register `GOOGLE-MERIDIAN-CALIBRATION`) |
| Channels with reach and frequency data (for example online video) | Meridian | Native reach and frequency support |
| Analyst team works in R and wants many candidate models to choose from | Robyn | Pareto set of models chosen with business judgement and calibration |
| Team needs production Python | Meridian, or Robyn only after accepting its beta status | Robyn's Python port is beta |

Whichever tool is chosen, record the reason, the version and the date in the assumption register.

## 3. Model form choices to write down

- Channel grouping and which channels are controls instead of modelled media.
- Adstock form: Robyn offers geometric (one parameter, simple, often too simple for digital) and Weibull (more flexible shape and scale) (register `META-ROBYN-ANALYST-GUIDE`).
- Saturation form: Robyn uses a Hill curve (shape and inflection parameters).
- Priors (Meridian): source for each ROI prior (experiment, benchmark or judgement) and its width.
- Time trend and seasonality: Meridian adjusts seasonality itself through time effects, so seasonality controls are not required (register `GOOGLE-MERIDIAN-COLLECT-DATA`); holidays and events still need flags.
- Level: channel, not campaign. Meridian's guide calls MMM a macro tool that works at channel level and warns that campaign-level modelling loses adstock memory (register `GOOGLE-MERIDIAN-DATA-AMOUNT`).

## 4. Validation and reading results honestly

Set pass and fail rules before looking at results:

| Check | What passes |
|---|---|
| Out-of-sample fit | Holdout weeks predicted within the error band agreed in advance |
| In-sample fit | High fit is necessary, not sufficient; Robyn's guide cites R squared above 0.9 as ideal (Vendor guidance, illustrative) |
| Stability | Channel ROI and contribution do not swing sharply when the model is refitted on a slightly different window |
| Priors against posteriors | Where the posterior simply repeats the prior, say the data added little for that channel |
| Plausibility | ROI per channel inside the range agreed with finance before modelling; outliers explained or excluded from decisions |
| Decomposition | Baseline share and media share make sense to the commercial team |
| Calibration agreement | Channels with experiments land near the experiment result, or the gap is explained |

Reading rules for the client version:

- Report ranges, not single numbers.
- Say which channels have experiment support and which rest on the model alone.
- Separate "the model estimates" from "the experiment showed".
- State what the model cannot see (unlogged radio, cash sales, competitor spend).
- Budget shifts are recommendations to test in steps, routed to [advertising strategy and budget](../../advertising-strategy-and-budget/SKILL.md).

## Sources

`GOOGLE-MERIDIAN-REPO`, `GOOGLE-MERIDIAN-CALIBRATION`, `GOOGLE-MERIDIAN-COLLECT-DATA`, `GOOGLE-MERIDIAN-DATA-AMOUNT`, `META-ROBYN`, `META-ROBYN-ANALYST-GUIDE`.
