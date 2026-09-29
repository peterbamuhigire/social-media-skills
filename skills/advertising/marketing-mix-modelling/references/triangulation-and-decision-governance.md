# Triangulation and decision governance

Read when deciding which evidence source governs which marketing decision, when MMM, experiments and platform attribution disagree, or when writing the assumptions disclosure. Parent: [marketing-mix-modelling](../SKILL.md).

## 1. Causal strength of the four method families

The IAB and IAB Europe *Guidelines for Incremental Measurement in Commerce Media* (November 2025) group incrementality methods into four families and rate their causal strength (register `IAB-INCREMENTAL-COMMERCE-MEDIA-2025`). The guidance is written for commerce media, but the ladder applies to any channel mix.

| Family | Examples | Causal strength (IAB) | Scope |
|---|---|---|---|
| Experiment-based | Randomised tests, holdouts, ghost ads, matched markets | Strong | Usually one platform or channel |
| Model-based counterfactual | Synthetic control, machine-learning propensity models | Strong to moderate | Medium |
| Econometric | Marketing mix modelling, time-series regression | Moderate to weak | High: all measured channels and non-media drivers |
| Hybrid proxies | Baseline versus exposed, platform-reported incrementality, simple multi-touch attribution | Weak | Narrow, one platform or campaign |

The same document rates each family as a strong, conditional or limited fit for each business need. It rates econometric models as designed for budget allocation and long-term cross-channel planning, experiments as the gold standard for proving causal lift, and proxies as quick directional reads that need corroborating tests. It advises stronger causal methods for high-stakes decisions such as budget allocation and proving ROI, and accepts lighter proxies for fast tactical optimisation when their limits are stated.

## 2. Which source governs which decision

| Decision | Governing source | Supporting source | Never decided by |
|---|---|---|---|
| Annual or quarterly split across channels | MMM (calibrated) | Experiments for the largest channels | Platform-reported ROAS |
| Whether a channel causes sales at all | Experiment (holdout, geo, lift study) | MMM as context | MMM alone, or last-click |
| Priors and calibration for the MMM | Experiments that pass the relevance check | Judgement, labelled | Platform dashboards |
| In-flight bids, creative rotation and audience tweaks | Platform attribution and analytics | Periodic holdouts | MMM (too slow) |
| Allowable CPA and break-even ROAS | [Attribution and measurement economics](../../advertising-attribution-and-measurement/references/economics-and-incrementality.md) | Finance | Model ROI alone |
| Board ROI business case | `meta-roi-framework` | MMM and experiment outputs as inputs | Unreconciled platform claims |

When two sources disagree, report both, check estimand, window and population, and let the governing source decide that decision only.

## 3. Assumptions to disclose (every client version)

The IAB guidance names three conditions for a causal claim: a credible counterfactual, control of bias, and separation of signal from noise. It asks for explicit identification assumptions, confounder controls and statistical checks such as intervals that exclude zero (register `IAB-INCREMENTAL-COMMERCE-MEDIA-2025`). Disclose:

- the counterfactual used (zero spend, lower spend, synthetic control);
- controls included and known omitted drivers;
- currency, exchange-rate and inflation treatment;
- adstock and saturation forms and the priors with their sources;
- intervals or credible ranges, not only point estimates;
- which channels rest on the model alone.

## 4. Data clean rooms (note only)

IAB Tech Lab lists a *Data Clean Rooms Guidance* (v1.0, July 2024) and names PAIR as the standard for secure matching of advertiser and publisher first-party data, replacing the earlier Open Private Join and Activation specification; it also lists the Attribution Data Matching Protocol (ADMaP, v1.0, February 2025) for privacy-safe conversion matching (register `IAB-TECHLAB-CLEAN-ROOM`). Clean rooms need large first-party datasets and a platform, publisher or retailer partner willing to match data; many East African clients have neither. Treat them as out of scope unless a client already has one; any customer-data matching needs a lawful basis and client authority.

## Sources

`IAB-INCREMENTAL-COMMERCE-MEDIA-2025`, `IAB-TECHLAB-CLEAN-ROOM`.
