# Phase 03 - Cross-Cultural, Regulatory, And Pricing Localisation Layer

## Objective

Build the system components that convert a market context block into culturally credible messaging, legally safer recommendations, and commercially realistic pricing logic.

## Why This Phase Matters

A market brief alone is not enough. The repository still needs three translation layers:

- how to communicate in that market,
- what rules shape marketing and data use in that market,
- how to package and price services credibly in that market.

## Core Outputs

1. A new `cross-cultural-communication-calibration` skill.
2. A new `global-regulatory-marketing-compliance` skill.
3. A new `global-pricing-localisation` skill.
4. Shared localisation fields added to high-impact SKILL files.

## Repository Work

### 1. Cross-cultural calibration

This skill should help the operator adjust for:

- direct versus indirect language,
- humour tolerance,
- prestige and authority signalling,
- urgency and call-to-action intensity,
- collectivist versus individualist framing,
- local proof and trust mechanisms,
- taboo or sensitive themes,
- translation versus true adaptation.

### 2. Regulatory routing

The compliance skill should not attempt to replace a lawyer. Its job is to:

- surface likely legal and platform-risk issues,
- flag when legal review is mandatory,
- distinguish privacy, disclosure, contest, ad, and data-retention concerns,
- account for regulated sectors such as health, finance, education, and politics.

### 3. Pricing localisation

This skill should turn commercial credibility into a system. It should cover:

- purchasing-power-aware pricing,
- retainer versus project norms,
- budget bands by market maturity,
- procurement and approval expectations,
- multi-tier packaging,
- proposal framing for SMEs versus enterprise clients.

### 4. Add localisation fields into core skills

Retrofit a standard subsection across selected skills:

- cultural calibration,
- legal/compliance notes,
- pricing/budget localisation,
- confidence and escalation note.

## Skills And Files Most Affected

- new: `cross-cultural-communication-calibration`
- new: `global-regulatory-marketing-compliance`
- new: `global-pricing-localisation`
- `biz-dev-pricing-menu`
- `biz-dev-proposal`
- `05-social-media-strategy`
- `06-digital-marketing-strategy`
- `playbook-social-media-contests`
- `meta-analytics-privacy`
- `policy-ai-content-ethics`
- `policy-ai-ip-and-copyright`

## Completion Criteria

- The repository can explain how recommendations change by culture, law, and budget reality.
- Proposal and pricing outputs no longer rely on UGX logic when another market is named.
- High-risk sectors and ambiguous legal situations trigger clear escalation language.
- The system distinguishes localisation from simple wording changes.

## Risks To Control

- Overclaiming legal certainty.
- Replacing human judgement with simplistic country stereotypes.
- Creating pricing outputs that sound locally incorrect to experienced buyers.

## Reading Material To Buy For This Stage

- *Cultures and Organisations: Software of the Mind* by Geert Hofstede, Gert Jan Hofstede, and Michael Minkov  
  Use it for structured comparative cultural variables that can feed repeatable decision rules.
- *The Long and the Short of It* by Les Binet and Peter Field  
  Use it to localise budget and channel decisions without losing commercial rigour.
- *How Brands Grow* by Byron Sharp  
  Use it to keep localisation grounded in evidence about reach, memory, and growth rather than folklore.
