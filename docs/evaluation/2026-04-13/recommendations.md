# Recommendations

## Priority Direction

Do not rebuild the repository from scratch. The base system is already strong. The right move is to add a market-adaptation layer above the existing skill architecture so the current suite becomes globally configurable rather than regionally fixed.

## System-Level Improvements

### 1. Add A Mandatory Context Injection Framework

Create a standard context block that every strategy, planning, platform, pricing, and reporting skill must consume before generating output. At minimum it should capture:

- country and city,
- sector and business model,
- target audience language and cultural profile,
- market maturity,
- platform usage realities,
- privacy/compliance environment,
- typical buying journey,
- purchasing power and budget band,
- preferred conversion path,
- brand risk sensitivity.

This should become the system's first-class override mechanism.

### 2. Add Market Overrides To AGENTS.md And CLAUDE.md

The repository-level instructions should explicitly say:

- East Africa is the default only when no market is specified.
- If another market is given, skills must replace channel, pricing, legal, and tone assumptions accordingly.
- Skills must state when a legal or cultural confidence threshold is too low and recommend specialist review.

### 3. Standardise Adaptation Fields Across SKILL.md Files

Many skills now have good execution sections. The next improvement is a consistent subsection inside `Required Input` or `Workflow` for:

- market context,
- regulatory context,
- cultural tone calibration,
- pricing and budget localisation,
- channel suitability by market.

This will reduce inconsistent adaptation between skills.

### 4. Create A Global Assumptions Library

Build structured reference files for market patterns rather than burying adaptations in prose. This library should store:

- market snapshots by country or region,
- platform adoption and trust patterns,
- compliance summaries,
- messaging sensitivities,
- pricing norms,
- conversion-path defaults.

That keeps `SKILL.md` concise while making adaptation operational.

## Skill-Level Improvements

### Business Development

- Add pricing localisation and procurement-path guidance.
- Add enterprise proposal variants for multinational and regulated clients.
- Add region-aware case-study framing logic so proof is translated for unfamiliar markets.

### Onboarding

- Expand intake forms to force market-specific data collection.
- Add questions about legal constraints, internal approval chains, and localisation needs.
- Include competitor geography and category maturity in every audit.

### Strategy

- Require explicit market diagnosis before channel recommendations.
- Separate default assumptions from market-derived decisions.
- Add stronger decision logic for when WhatsApp, email, SMS, LinkedIn, search, or communities should lead.

### Execution Playbooks

- Add market-specific customer service expectations and escalation norms.
- Add cultural review checkpoints before campaign rollout.
- Add localisation QA so playbooks distinguish between direct translation and true adaptation.

### Analytics

- Expand privacy and attribution guidance by market.
- Add server-side tracking and consent-mode options where relevant.
- Add region-specific benchmark interpretation guidance.

### AI

- Tie AI humanisation and bias review more directly to geography and culture.
- Add country-aware prompt variables.
- Add stronger quality checks for international factuality and cultural accuracy.

## New Skills To Add

### 1. `global-market-context-engine`

Purpose: Produce a standard market context block that all downstream skills inherit.

### 2. `country-market-brief`

Purpose: Generate a country-specific digital marketing brief covering platform mix, audience behaviour, legal risks, payment norms, and trust signals.

### 3. `cross-cultural-communication-calibration`

Purpose: Adjust tone, messaging, offer framing, persuasion style, and social proof by market and audience culture.

### 4. `global-pricing-localisation`

Purpose: Localise pricing models, retainers, budget bands, and proposal packaging by market maturity and purchasing power.

### 5. `global-regulatory-marketing-compliance`

Purpose: Route strategy and execution through the right privacy, consent, disclosure, and platform-compliance logic by country.

### 6. `platform-usage-by-market`

Purpose: Map platform relevance, audience behaviour, and conversion norms across countries and regions.

### 7. `international-market-entry-digital-strategy`

Purpose: Build launch and expansion strategies for brands entering new countries.

### 8. `global-benchmarking-and-kpi-calibration`

Purpose: Adapt KPIs, reporting expectations, and benchmark interpretation by sector, market, and channel maturity.

## Optional Structural Optimisations

These are optional and should not disrupt the current repository shape:

- Add `references/` folders selectively where a skill needs large market-specific supporting material.
- Add nested `AGENTS.md` only in domains where adaptation rules differ materially, such as `policy`, `meta`, or `platform-*`.
- Add a lightweight evaluation checklist that every new skill must pass before being considered globally adaptable.

## Implementation Sequence

1. Create the context engine and market brief skills.
2. Update repo-level instructions to make context adaptation mandatory.
3. Retrofit high-impact strategy, proposal, pricing, reporting, and platform skills to consume the context block.
4. Build the market assumptions reference library.
5. Expand regulatory and cultural calibration coverage.
6. Add benchmark and pricing localisation layers.

This sequence preserves the current repository and raises its global capability without breaking the East Africa-first strength that already exists.
