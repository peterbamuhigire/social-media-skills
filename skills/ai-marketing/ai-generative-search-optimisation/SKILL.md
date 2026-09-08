---
name: ai-generative-search-optimisation
description: Use when an AI-search or generative-search visibility deliverable is required for social-media or digital-marketing work; use ai-readiness-diagnostic for a broader AI maturity assessment.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Generative Search Optimisation (GEO)
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Use this skill to plan evidence-bounded discoverability across AI answers,
search, social profiles, communities, and the destination a customer uses next.
It is a planning and audit route, not a promise of inclusion, ranking, or sales.

<!-- dual-compat-start -->
## Use When

- The deliverable is an AI-search visibility plan, audit, content system, or
  measurement loop for a social or digital-marketing engagement.
- The work must connect social profiles, native content, off-site reputation,
  website destinations, and customer action.

## Do Not Use When

- Use `ai-readiness-diagnostic` for a general AI maturity, data, team, or
  deployment assessment.
- Use `seo-discovery/seo-geo-optimisation` for one page or article only.
- Do not publish, send, spend, alter a live account, collect personal data, or
  claim a certification without explicit authority and the relevant release gate.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Business name, offer, audience, market, goal, channels, and intended decision | Approved brief and client fact sheet | yes | Stop the affected recommendation; state a narrow assumption only where safe |
| Existing profiles, content, destinations, analytics, referral data, and customer questions | Supplied exports, URLs, CRM or platform evidence | conditional | Mark the check `not assessed`; do not infer visibility or performance |
| Current platform, market, legal, privacy, rights, and AI-search claims | Social source register and Digital Research verification | yes for material claims | Quarantine the claim and narrow the deliverable |
| Approval, access, budget, language, accessibility, and moderation constraints | Accountable owner | conditional | Stop publication, spend, collection, or live changes |

## Capability and Permission Boundaries

Read and search are the minimum capabilities. Planning and audit are read-only.
Edits to repository guidance are in scope for maintainers; live publishing,
outreach, spend, personal-data processing, production changes, and certification
claims require separate explicit authority.

## Degraded Mode

If evidence, network, platform access, native-language review, rights review,
or measurement data is unavailable, return the narrowest useful plan and label
each affected item `not assessed`. Never convert a missing check into a pass.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The claim is current, material, and supported by the source register | Cite the source at the point of use and record scope, dates, freshness, and limit | Stale platform or market advice |
| The observation is a mention, citation, referral, sentiment, or conversion | Name that exact outcome; keep it separate from the others | False “AI rank” or attribution certainty |
| The profile or post contains a factual, regulated, sensitive, or rights-bearing claim | Require owner evidence and the relevant legal/rights/market gate | Harm, rights breach, or fabricated proof |
| A destination is useful to people and agents | Improve clear facts, accessible text, consent-safe CTA, and failure path | Optimising a surface that cannot complete the job |
| Evidence is partial or contradictory | Narrow, quarantine, or mark `NOT_ASSESSED`; preserve the contradiction | Confident synthesis from a weak source |

## Workflow

1. Frame one audience, channel, customer job, business outcome, market, and
   approval boundary. Record the consequence of getting it wrong.
2. Establish the baseline: customer questions, profile/entity consistency,
   content and source quality, canonical destinations, available referrals,
   self-report, prompt observations, platform data, and (where authorised) logs.
3. Apply the three-mode planning lens from the Carter synthesis: evergreen
   brand/offer facts for remembered knowledge; current sourced updates for
   retrieval; deep evidence, trade-offs, and working for reasoning. This is a
   durable planning lens, not a fixed platform taxonomy.
4. Select one content or profile slice. State its hypothesis, primary outcome,
   trust/cultural/accessibility guardrail, owner, time-box, stop rule, and
   rollback path.
5. Make the slice legible: who the brand is, what it does, for whom, where,
   under what limits, with a clear next action and an accurate canonical link.
   Use native channel conventions without forcing slang, hashtags, or claims.
6. Verify every current claim, source, statistic, quote, rights assertion, and
   platform rule. Run anti-slop, creative, legal/market, language, and
   accessibility reviews that apply to the asset.
7. Measure separately: representation, retrieval/citation observation, referral,
   qualified action, and revenue. Record sample, date, denominator, consent,
   and attribution limits.
8. Check normal and failure paths, including inaccurate AI descriptions,
   negative or misleading UGC, broken destinations, opt-out, moderation, and
   no-data states. Correct, quarantine, or rerun the affected check.
9. Standardise only a demonstrated improvement in the skill, reference,
   template, source register, fixture, or gate. Record the next re-audit.

Use the [Garner, Woolley, and Bishop/Starkey independent synthesis](../../../book-extractions/garner-woolley-starkey-content-and-language-synthesis-2026.md)
to add three checks to the slice: the outside-in customer journey, an
intent/customer-language map, and a recognisable human voice. Retain native
adaptation, source/rights/approval handoffs, moderation, and a correction path;
the supplied books are historical or editorial inputs, not current platform
authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI-search visibility audit or plan | Strategist, client reviewer, or delivery team | Audience, channel job, evidence boundary, outcome definitions, sequence, owners, and gaps are explicit |
| Content/profile action brief | Content or community operator | One real slice has channel-native copy guidance, source/rights status, CTA, moderation path, and acceptance checks |
| Measurement and learning record | Analyst and accountable owner | Prompt observations, platform data, referrals, self-report, and qualified outcomes are not conflated |
| Decision and gap note | Approver or next workflow | Unsupported, unauthorised, stale, and `NOT_ASSESSED` items are visible with a recovery action |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Source and claim register | Inline table or linked JSON/Markdown record | Every material current claim has a verified source, scope, date, freshness, support state, uncertainty, and owner |
| Content/profile fact map | Table | Identity, offer, audience, location, proof, limits, rights, and canonical destination are traceable |
| Experiment record | Markdown or tracker row | Hypothesis, baseline, measure, guardrail, stop rule, result, rollback, and standardisation decision exist |
| Release review | Completed gates | Anti-slop, rights, legal/market, cultural, language, accessibility, and approval status are explicit |

## Quality Standards

- Use British English and Uganda/East Africa defaults only where they apply;
  record any different market, language, currency, timezone, or channel reality.
- Keep the human job primary. Clear answers, evidence, honest limits, and a
  usable destination matter more than AI-facing formatting.
- Make social and community presence part of the discoverability surface without
  buying, seeding, manufacturing, or suppressing mentions or reviews.
- Use `llms.txt`, markdown mirrors, APIs, MCP, or agent integrations only as a
  named, reversible experiment for a real consumer or task; never as a default
  ranking lever.
- Run `ai-marketing/anti-ai-slop` during drafting and `ai-marketing/ai-slop-audit`
  after major iterations; an F blocks progression until fixed.

## Anti-Patterns

- **Unsupported benchmark or adoption number.** Fix: verify the primary source or remove it.
- **“AI rank” reported as a metric.** Fix: name mention, citation, referral, action, or revenue.
- **FAQ, 50-word opening, monthly cadence, or speed target treated as universal.** Fix: make it a tested local acceptance choice or remove it.
- **Inauthentic mentions, seeded comments, or manufactured reviews.** Fix: use authentic, rights-cleared evidence and moderation.
- **A profile optimised without an accurate destination.** Fix: trace the click, consent, form/WhatsApp path, and failure recovery.
- **A calendar presented as learning.** Fix: add a hypothesis, guardrail, stop rule, and result.
- **A current platform claim copied from a book or AI answer.** Fix: route it through Digital Research and mark it `NOT_ASSESSED` until verified.

## References

- [Carter independent synthesis](../../../book-extractions/carter-new-rules-ai-search-synthesis-2026.md)
- [Garner, Woolley, and Bishop/Starkey independent synthesis](../../../book-extractions/garner-woolley-starkey-content-and-language-synthesis-2026.md)
- [Social source register](../../../docs/source-registers/source-register.json)
- [Digital Research currentness gate](../../../../digital-research-engine/docs/continuous-improvement/kaizen-currentness-gate.md)
- [Digital Research source evaluation](../../../../digital-research-engine/skills/source-evaluation/SKILL.md)
- [Digital Research source verification](../../../../digital-research-engine/skills/source-verification/SKILL.md)
- [AI slop ship gate](../anti-ai-slop/SKILL.md)
- [AI slop audit](../ai-slop-audit/SKILL.md)
- [Page-level GEO route](../../seo-discovery/seo-geo-optimisation/SKILL.md)
<!-- dual-compat-end -->
