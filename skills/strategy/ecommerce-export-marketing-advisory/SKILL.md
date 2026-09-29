---
name: ecommerce-export-marketing-advisory
description: 'Use when a seller wants buyers abroad: first export market, cross-border trust and proof, marketplace and partner routes, and campaigns capped by acquisition cost; produces the export marketing plan with buyer personas and a trust checklist; not for selling at home via WhatsApp or Instagram (use `social-commerce-strategy`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# E-Commerce Export Marketing Advisory

Turns an e-commerce diagnostic and unit-economics model into a practical export-marketing plan: market-specific messaging, cross-border trust and proof, localised channels, conversion fixes, partnership outreach and budgets held under CAC guardrails. It serves a company that wants to enter or grow in another EAC market or export market through digital channels, where every recommendation must fit the company's margin, CAC, logistics and payment reality.

<!-- dual-compat-start -->
## Use When

- We want to sell abroad (diaspora, the wider EAC, Europe, the Gulf or the US) and must pick the first export market on evidence.
- Overseas buyers do not trust a Ugandan or Kenyan web shop; we need certifications, reviews, shipping and returns proof.
- Our cross-border website, Amazon, Etsy or Alibaba listing gets visits from abroad but few orders.
- We need importers, distributors or retail partners and outreach messages to reach them.
- Export campaigns must stay under a customer acquisition cost (CAC) ceiling we can afford.

## Do Not Use When

- `social-commerce-strategy` for domestic selling through WhatsApp, Instagram, Mobile Money and local delivery.
- `brand-strategy-and-distinctive-assets` for naming, packaging and standing out from look-alike sellers.
- `playbook-post-click-strategy` for diagnosing checkout and landing-page conversion.
- Stop before stating customs, tariff, certification or export-compliance facts without current verified sources; flag them for the client's trade adviser.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Named target market (another EAC country or an export market) and customer segment | Client owner | Yes | Stop; no plan without a named market. |
| Company diagnostic: product/category, current channels, customer evidence, analytics and conversion data | Client systems or a prior e-commerce diagnostic | Yes | Build personas as labelled hypotheses and plan a pilot to test them. |
| Unit-economics guardrails: acceptable CAC, contribution margin, discount limits, route viability | Client finance or the unit-economics model | Yes before any paid or discount plan | Stop paid acquisition and discounting; deliver organic, partner and trust work only. |
| Payment, logistics, returns, compliance, language and customer-support constraints | Client operations; trade adviser | Yes | Mark the trust layer `not assessed` for each missing constraint; flag customs, tariff and certification facts for the trade adviser. |
| Channel, penetration or market-size statistics | Dated, cited sources via the digital research engine | Conditional | State the assumption and test it in the pilot; never cite an undated figure. |

## Workflow

1. Confirm one target market (or separate plans per market) and the unit-economics verdict; stop if no market is named or paid acquisition is asked for without known CAC and margin limits.
2. Define the target-market buyer and the cross-border trust problem.
3. Build personas from evidence: need, proof required, buying objections, payment preference, delivery expectations, language and support expectations.
4. Design the trust-and-proof layer: reviews, secure-payment signals, delivery promises, returns policy, authenticity proof, certifications, local partner cues and the customer-support route.
5. Review conversion leaks in the digital journey (mobile UX, product pages, checkout, payment options, shipping clarity, proof, support, remarketing) with the [trust and conversion review](references/trust-and-conversion-review.md).
6. Write market-entry messaging and value propositions localised to country, language, currency and norms.
7. Plan channels and campaigns within CAC and contribution-margin guardrails; draft partnership outreach (marketplaces, logistics firms, payment providers, local agents, sector bodies, influencers) only where it fits the route economics.
8. Define KPIs the company can track with its own tools and lay out the 90-day execution in the [plan template](references/export-marketing-plan-template.md); correct any section that fails the Quality Standards and rerun the check before hand-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Export marketing plan (market choice, positioning, channel plan, 90-day execution) | Client owner | Specific to one market or clearly separated by market; every channel row has budget, CAC guardrail, KPI and owner. |
| Cross-border customer personas | Marketing lead and copywriters | Each persona states need, trust barrier, payment preference, delivery expectation, proof required and main objection with response. |
| Trust-and-proof checklist and digital-channel conversion review | Web or marketplace owner | Every trust question and conversion area is answered or marked `not assessed`. |
| CAC-bounded campaign outline and partnership outreach messages | Marketing lead; client approver | Budget stays inside the CAC and margin guardrails; outreach drafts await approval before sending. |
| KPI and implementation tracker | Client owner | Only KPIs the company can measure with its actual tools. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Market and statistic source register | Table: claim, source, date | Every channel penetration, market-size or platform statistic is sourced and dated, or labelled an assumption. |
| Unit-economics check | Table linking each campaign to CAC and contribution margin | No campaign budget exceeds its guardrail. |
| Compliance flag list | List for the trade adviser | Customs, tariff, certification and export-compliance points are flagged, not asserted. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Partner outreach messages are drafts until the client approves and sends them.

## Degraded Mode

Without unit-economics guardrails or a named market, return the narrowest qualified result and mark the affected checks `not assessed`. Trust-layer and conversion reviews, persona hypotheses and a partner shortlist can still be delivered, with no paid budget.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| No target market is named | Stop and ask for one; do not write generic regional advice | Generic regional expansion advice |
| Market, fulfilment, compliance or unit-economics evidence is missing | Return a qualified readiness gap and stop before claiming market viability | Spending on acquisition before the export offer can be fulfilled profitably |
| Unit economics are unknown and the plan involves paid acquisition or discounting | Remove paid and discount lines until CAC and margin limits exist | Campaigns that lose money on every order |
| The task is only a domestic social-media content calendar | Route to the pipeline calendar or `social-commerce-strategy` | Export framing applied to home-market work |
| A statistic has no current source | State the assumption and test it in the pilot | Plans built on stale or invented figures |
| Customs, tariff or certification facts are needed | Flag them for the client's trade adviser | Stating compliance facts without verified sources |

## Quality Standards

- The plan is specific to one target market or clearly separated by market.
- Trust signals match known buyer objections and route risks.
- Campaign budget respects CAC and contribution-margin guardrails.
- Channel recommendations are measurable with the company's actual tools.
- Any channel penetration, market-size or platform statistic is sourced and dated.
- Copy is localised for language, currency, proof and norms; British English in the deliverable and the anti-slop gate passed.

## Anti-Patterns

- Generic regional expansion advice. Fix: name the market and build the plan from that market's buyer evidence.
- Paid campaigns without CAC limits. Fix: set the CAC and contribution-margin guardrail per channel before budgeting.
- Ignoring delivery, returns, payment and trust barriers. Fix: run the trust-layer questions before any campaign.
- Copy that is not localised for language, currency, proof or norms. Fix: localise the value proposition per market.
- KPIs the company has no way to measure. Fix: check each KPI against the analytics and funnel events that exist.

## References

- [Export marketing plan template](references/export-marketing-plan-template.md): read when laying out plan sections, personas, the channel plan, budget, partner outreach and KPIs.
- [Trust and conversion review](references/trust-and-conversion-review.md): read when checking trust signals and the conversion journey, and before citing any buyer-behaviour statistic.
- [`social-commerce-strategy`](../social-commerce-strategy/SKILL.md): read when the work is domestic selling through WhatsApp, Instagram, Mobile Money and local delivery.
- [`brand-strategy-and-distinctive-assets`](../brand-strategy-and-distinctive-assets/SKILL.md) ([e-commerce differentiation](../brand-strategy-and-distinctive-assets/references/ecommerce-differentiation.md)): read when naming, packaging or standing out from look-alike sellers is the problem.
- [`playbook-post-click-strategy`](../../playbooks/playbook-post-click-strategy/SKILL.md): read when checkout or landing-page conversion needs diagnosis.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read before any compliance, certification or comparative claim is released.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting messaging and outreach.
<!-- dual-compat-end -->

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.
