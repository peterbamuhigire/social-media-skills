---
name: seo-geo-optimisation
description: Use when the main deliverable is page-level generative-search citation readiness; use ai-generative-search-optimisation for the wider social, profile, reputation, and measurement decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# SEO and GEO Optimisation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Optimise one page or content unit for people-first usefulness, evidence clarity,
search eligibility, entity comprehension, and a measurable next action. GEO is
not a separate guaranteed ranking system.

<!-- dual-compat-start -->
## Use When

- A brief names one page, article, landing page, FAQ, profile-linked destination,
  or canonical resource that should be easier for search and AI systems to find,
  understand, or cite.
- The work needs a page-level content, entity, technical, source, or measurement
  review after the broader strategy is set.

## Do Not Use When

- Use `ai-generative-search-optimisation` for a programme-wide AI-search,
  social-profile, reputation, or prompt-tracking decision.
- Do not proceed with a current platform, market, legal, regulated, or performance
  claim until it is verified in the source register.
- Do not publish, change a live property, collect data, or spend without explicit
  authority and the relevant release gate.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Page URL or draft, page job, audience, market, language, and CTA | Client brief and supplied content | yes | Stop and request the missing page decision |
| Verified business facts, proof, authorship, dates, sources, and rights | Client evidence pack and Digital Research | yes for claims | Remove, narrow, or mark the claim `NOT_ASSESSED` |
| Route map, canonical rules, structured-data facts, and measurement plan | Website/build owner | conditional | Provide a content-only review and mark technical checks `not assessed` |
| Approval, privacy, accessibility, legal, and publication constraints | Accountable owner | conditional | Withhold release and return an approval checklist |

## Capability and Permission Boundaries

Read and search are sufficient for an audit or draft. Editing repository guidance
is permitted for maintainers with explicit authorisation. Live website changes,
Search Console or webmaster changes, publication, personal-data processing, and
third-party access require separate authority.

## Degraded Mode

Fallback:
Without the page, source evidence, network, render, or deployment context, return
only the supported content and checklist findings. Mark unavailable checks
`not assessed`; do not claim indexing, citation, rich-result eligibility, or
performance improvement.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The page answers a real audience question with evidence and a clear job | Preserve or improve the human-readable answer, structure, proof, and CTA | AI-facing formatting that harms readers |
| A current claim concerns Google, Bing, OpenAI, a platform, law, market, or tool | Use a dated primary source and record scope, freshness, support, and limit | Stale or invented guidance |
| The fact is a proven entity, offer, author, location, review, or date | Represent only the visible, verified fact in metadata or schema | Misleading structured data |
| The observation is a citation, referral, lead, or sale | Report the exact outcome and its attribution limit | Conflated “AI rank” |
| A page is indexed but duplicated, stale, inaccessible, or inaccurate | Repair the specific failure, recheck, and retain the rollback path | Citation of the wrong or unsafe page |

## Workflow

1. Frame the page job, audience, query or decision, market/language, proof burden,
   CTA, owner, and consequence of error.
2. Audit the opening answer, heading structure, definitions, facts, sources,
   authorship, dates, local relevance, internal links, media text, accessibility,
   and conversion path. Do not impose a fixed word count or FAQ requirement. Stop
   if the page job or proof burden is unknowable.
3. Apply the Carter planning lens: evergreen identity and offer facts for
   remembered knowledge; dated updates for retrieval; sourced depth, trade-offs,
   and working for complex reasoning. Label this as a planning synthesis.
4. Make entity relationships explicit in natural language—who the organisation
   is, what it does, for whom, where, and under what limits. Avoid keyword or
   token manipulation, formulaic filler, and unsupported superlatives.
5. Check canonical, indexability, snippets, headings, visible text, structured
   data, internal links, sitemap/robots coherence, page experience, and locale
   signals against the actual route map. Use schema only when visible facts and
   consumer eligibility support it.
6. For current Google Search features, apply official Google guidance: core SEO,
   crawlability, useful people-first content, and Search Console measurement are
   the foundation. `llms.txt`, artificial chunking, special AI markup, and
   inauthentic mentions are not default requirements.
7. Define one reversible improvement and one measurement slice. Separate page
   visibility/citation observation, referral, qualified action, and revenue.
8. Review content, source, rights, legal/market, language, accessibility,
   anti-slop, and visual/render checks. Correct or quarantine failed evidence.
9. Hand off the page, source map, assumptions, test results, owner, rollback,
   unresolved gaps, and re-audit date.

Apply the [Garner, Woolley, and Bishop/Starkey independent synthesis](../../../book-extractions/garner-woolley-starkey-content-and-language-synthesis-2026.md)
as a qualified editorial lens: map the audience journey and intent before
choosing a phrase, add original value and proof, and preserve a distinctive
human voice. Do not import the books' dated platform, algorithm, or metric
claims without current primary-source verification.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Page-level GEO readiness audit | Content, SEO, or client reviewer | Findings map to the page job, evidence, route, and named acceptance checks |
| Revised page brief or copy | Writer or build operator | Direct, useful, sourced, accessible content with accurate entity and CTA details |
| Technical and metadata checklist | SEO/build owner | Each applicable signal has an owner, fact basis, test, and no conflicting control |
| Measurement and handoff record | Analyst and release owner | Metric definitions, source limits, consent, baseline, experiment, and next review are explicit |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Page fact and source map | Table | Claim, source ID, locator, tier, support state, dates, uncertainty, owner, and visible page location are recorded |
| Before/after content audit | Table or annotated draft | Page job, audience, proof, language, accessibility, rights, and unresolved gaps are visible |
| Technical/render test record | Markdown or CI output | Canonical, indexability, schema, links, mobile/keyboard states, and claimed live behaviour are tested or marked `not assessed` |
| Experiment row | Tracker or Markdown | Hypothesis, primary measure, guardrail, stop rule, result, rollback, and standardisation decision exist |

## Quality Standards

- Use British English and explicit Uganda/East Africa assumptions only where
  applicable; localise language and slug decisions rather than translating blindly.
- Open with the answer when that serves the reader, but do not force a word-count
  or heading formula. Every section must have a reader or business job.
- Preserve source quality and visible truth. Do not hide weak evidence in schema,
  markdown, crawler files, FAQs, or social proof.
- Report Google Search Console, Bing AI Performance, analytics, prompt tracking,
  or server-log observations with the exact documented scope; missing access is
  `NOT_ASSESSED`.
- Run the relevant anti-slop, accessibility, visual, rights, legal/market, and
  security checks before release.

## Anti-Patterns

- **Guaranteed AI citation or rank.** Fix: state the controllable work and exact observation.
- **Book or AI answer used as current platform authority.** Fix: verify the primary source or quarantine it.
- **Fixed 50-word opening, FAQ-everywhere, monthly cadence, or three-second rule.** Fix: make it a documented local experiment or remove it.
- **Schema facts not visible or not proven.** Fix: omit them and log the evidence gap.
- **Manufactured third-party mentions, reviews, or UGC.** Fix: use authentic, rights-cleared evidence and moderation.
- **One page cloned for every query variant.** Fix: consolidate around a real audience need and add only useful coverage.
- **Citation, referral, and conversion treated as one KPI.** Fix: define and reconcile each outcome separately.

## References

- [Carter independent synthesis](../../../book-extractions/carter-new-rules-ai-search-synthesis-2026.md)
- [Garner, Woolley, and Bishop/Starkey independent synthesis](../../../book-extractions/garner-woolley-starkey-content-and-language-synthesis-2026.md)
- [Social source register](../../../docs/source-registers/source-register.json)
- [Digital Research currentness gate](../../../../digital-research-engine/docs/continuous-improvement/kaizen-currentness-gate.md)
- [Digital Research source evaluation](../../../../digital-research-engine/skills/source-evaluation/SKILL.md)
- [Digital Research source verification](../../../../digital-research-engine/skills/source-verification/SKILL.md)
- [AI Generative Search Optimisation](../../ai-marketing/ai-generative-search-optimisation/SKILL.md)
- [AI slop ship gate](../../ai-marketing/anti-ai-slop/SKILL.md)
<!-- dual-compat-end -->
