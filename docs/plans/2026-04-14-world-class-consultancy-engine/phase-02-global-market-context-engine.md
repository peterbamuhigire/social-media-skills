# Phase 02 - Global Market Context Engine

## Objective

Build the mandatory upstream context system that every major downstream skill must consume before generating plans, strategies, proposals, or reports.

## Problem Being Solved

The repository's biggest weakness is adaptability. It has strong East Africa-first defaults but no universal mechanism for switching country, culture, platform mix, regulation, trust signals, or buying behaviour before a deliverable is generated.

## Core Outputs

1. A new `global-market-context-engine` skill.
2. A new `country-market-brief` skill.
3. A shared reference library under `docs/` or skill `references/` for market snapshots.
4. A standard reusable context block that other skills can inherit or request.

## Repository Work

### 1. Design the context schema

The context engine should produce a structured block containing:

- country, city, and region,
- sector and business model,
- market maturity,
- language and communication norms,
- dominant platforms and their role,
- trust signals and social proof expectations,
- preferred conversion path,
- payment and pricing expectations,
- privacy, disclosure, and sector-specific compliance issues,
- major cultural sensitivities,
- key strategic opportunities,
- key strategic constraints.

### 2. Build country-level market brief logic

The `country-market-brief` skill should generate a practical summary, not a travel guide. It should answer:

- where audiences discover brands,
- what channels actually drive action,
- what offer framing tends to work,
- what decision-makers care about,
- what compliance red flags exist,
- what content norms and tone risks matter.

### 3. Build a market assumptions library

Start with the markets most likely to matter commercially:

- Uganda,
- Kenya,
- Tanzania,
- Rwanda,
- South Africa,
- United Kingdom,
- United States,
- United Arab Emirates.

The point is not to cover every country immediately. The point is to establish the architecture so new market modules can be added cleanly.

### 4. Define inheritance rules

Document which skills must consume the context block first:

- proposals,
- onboarding,
- strategy,
- platform plans,
- pricing,
- reporting,
- AI-humanisation and bias checks.

## Skills And Files Most Affected

- new: `global-market-context-engine`
- new: `country-market-brief`
- `01-client-brief`
- `05-social-media-strategy`
- `06-digital-marketing-strategy`
- `biz-dev-proposal`
- `biz-dev-pricing-menu`
- `meta-reporting`
- `meta-analytics-privacy`

## Completion Criteria

- A standard context block exists and can be reused.
- Market assumptions are separated from strategy recommendations.
- High-impact skills can no longer silently inherit Uganda/East Africa defaults when another market is specified.
- The repository has a repeatable method for adding new countries or regions.

## Risks To Control

- Turning market context into static trivia instead of decision-support.
- Making the context block too large to be practical.
- Pretending confidence in unfamiliar markets where real specialist review is needed.

## Reading Material To Buy For This Stage

- *The Culture Map* by Erin Meyer  
  Use it to model communication, trust, persuasion, disagreement, and decision-making differences across cultures.
- *Marketing Across Cultures* by Jean-Claude Usunier and Julie Anne Lee  
  Use it to design reusable market-adaptation logic instead of ad hoc localisation.
- *Digital Marketing: Strategy, Implementation and Practice* by Dave Chaffey and Fiona Ellis-Chadwick  
  Use it to keep adaptation tied to integrated planning rather than isolated channel tweaks.
