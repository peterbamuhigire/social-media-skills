---
name: seo-geo-optimisation
description: Use when one page, article, FAQ or landing page should be easier for Google and AI answer engines such as ChatGPT or Perplexity to find, understand and cite; produces the page-level readiness audit, revised brief or copy, metadata checklist and measurement note; not for a brand-wide AI search programme (use `ai-generative-search-optimisation`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# SEO and GEO Optimisation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Optimise one page or content unit for people-first usefulness, evidence clarity, search eligibility, entity comprehension, and a measurable next action. GEO is not a separate guaranteed ranking system.

<!-- dual-compat-start -->
## Use When

- A named page, article, FAQ or fees page never comes up in search results or when people ask ChatGPT or Google's AI answers, and the client wants that one page fixed.
- Page copy needs clearer answers, sources, entity details and a single next action.
- Titles, meta descriptions, structured data and canonical tags on one page need checking against the page's job.
- The team wants to measure whether a page change moved clicks or citations.

## Do Not Use When

- `ai-generative-search-optimisation` for a programme-wide AI search, social profile, reputation or prompt-tracking decision.
- `12-website-content-plan` for a 90-day website content plan.
- `blog-writer` for writing a new article from scratch.
- Stop before editing a live page or promising rankings or AI citations; deliver recommendations for the site owner.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Page URL or draft, page job, audience, market, language, and CTA | Client brief and supplied content | yes | Stop and request the missing page decision |
| Verified business facts, proof, authorship, dates, sources, and rights | Client evidence pack and Digital Research | yes for claims | Remove, narrow, or mark the claim `NOT_ASSESSED` |
| Route map, canonical rules, structured-data facts, and measurement plan | Website/build owner | conditional | Provide a content-only review and mark technical checks `not assessed` |
| Approval, privacy, accessibility, legal, and publication constraints | Accountable owner | conditional | Withhold release and return an approval checklist |

## Workflow

1. Frame the page job, audience, query or decision, market/language, proof burden, CTA, owner, and consequence of error. For SaaS content webs, comparison pages or LinkedIn-linked destinations, read [the social-to-website handoff](references/saas-content-web-handoff.md) before reviewing the page and return its intent, proof, destination and measurement record. For any article, run and retain the mandatory three-wave SERP study before drafting ([SERP study and editorial lens](references/serp-study-and-editorial-lens.md)).
2. Audit the opening answer, heading structure, definitions, facts, sources, authorship, dates, local relevance, internal links, media text, accessibility, and conversion path. Do not impose a fixed word count or FAQ requirement. Stop if the page job or proof burden is unknowable.
3. Apply the Carter planning lens: evergreen identity and offer facts for remembered knowledge; dated updates for retrieval; sourced depth, trade-offs, and working for complex reasoning. Label this as a planning synthesis. Apply the customer-language and voice lens in the same reference as a qualified editorial lens.
4. Make entity relationships explicit in natural language: who the organisation is, what it does, for whom, where, and under what limits. Avoid keyword or token manipulation, formulaic filler, and unsupported superlatives.
5. Check canonical, indexability, snippets, headings, visible text, structured data, internal links, sitemap/robots coherence, page experience, and locale signals against the actual route map. Use schema only when visible facts and consumer eligibility support it.
6. For current Google Search features, apply official Google guidance: core SEO, crawlability, useful people-first content, and Search Console measurement are the foundation. `llms.txt`, artificial chunking, special AI markup, and inauthentic mentions are not default requirements. Apply the evidence-checked SEO/AEO/GEO/AIO/SXO disposition in `../../ai-marketing/ai-generative-search-optimisation/SKILL.md`: no fixed 40–60-word answer rule, no universal FAQ/HowTo requirement, no training-data or citation promise, and no quarterly refresh without a substantive trigger.
7. Define one reversible improvement and one measurement slice. Separate page visibility/citation observation, referral, qualified action, and revenue.
8. Review content, source, rights, legal/market, language, accessibility, anti-slop, and visual/render checks. Correct or quarantine failed evidence, then rerun the failed check.
9. Hand off the page, source map, assumptions, test results, owner, rollback, unresolved gaps, and re-audit date.

## Outputs

| Artefact | Consumer | Acceptance condition |
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

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Editing repository guidance is permitted for maintainers with explicit authorisation; live website changes, Search Console or webmaster changes, and third-party access require separate authority.

## Degraded Mode

Without the page, source evidence, network, render, or deployment context, return the narrowest qualified result and mark the affected checks `not assessed`. Only the supported content and checklist findings can still be delivered; do not claim indexing, citation, rich-result eligibility, or performance improvement.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The page answers a real audience question with evidence and a clear job | Preserve or improve the human-readable answer, structure, proof, and CTA | AI-facing formatting that harms readers |
| A current claim concerns Google, Bing, OpenAI, a platform, law, market, or tool | Use a dated primary source and record scope, freshness, support, and limit | Stale or invented guidance |
| The fact is a proven entity, offer, author, location, review, or date | Represent only the visible, verified fact in metadata or schema | Misleading structured data |
| The observation is a citation, referral, lead, or sale | Report the exact outcome and its attribution limit | Conflated “AI rank” |
| A page is indexed but duplicated, stale, inaccessible, or inaccurate | Repair the specific failure, recheck, and retain the rollback path | Citation of the wrong or unsafe page |
| The plan mass-produces pages, hosts third-party or sponsored content on the client's domain, or buys an expired domain to rank | Screen it against Google's spam policies (scaled content abuse, site reputation abuse, expired domain abuse; register `GOOGLE-SPAM-POLICIES`) and drop or redesign any part whose main purpose is to manipulate ranking | Manual action or ranking loss for the whole site |
| The client wants to limit what Search or AI Overviews show from a page | Record a deliberate choice of `nosnippet`, `data-nosnippet`, `max-snippet` or `noindex` with its owner and trade-off; Google-Extended governs Gemini training and grounding use, not Search or AI Overviews inclusion (registers `GOOGLE-AI-FEATURES-2025`, `GOOGLE-EXTENDED-2026`) | Blocking the wrong crawler, or losing Search visibility by accident |
| Page speed or Core Web Vitals fail ("good" = LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at the 75th percentile; register `WEBDEV-CORE-WEB-VITALS`) | Record the failing metric and hand the fix to the build owner via [website-skills](https://github.com/peterbamuhigire/website-skills); this skill does not change code | Content edits presented as a speed fix |

## Quality Standards

- Use British English and explicit Uganda/East Africa assumptions only where applicable; localise language and slug decisions rather than translating blindly.
- Open with the answer when that serves the reader, but do not force a word-count or heading formula. Every section must have a reader or business job.
- Preserve source quality and visible truth. Do not hide weak evidence in schema, markdown, crawler files, FAQs, or social proof.
- Report Google Search Console, Bing AI Performance, analytics, prompt tracking, or server-log observations with the exact documented scope; missing access is `NOT_ASSESSED`.
- Run the relevant anti-slop, accessibility, visual, rights, legal/market, and security checks before release.

## Anti-Patterns

- **Guaranteed AI citation or rank.** Fix: state the controllable work and exact observation.
- **Book or AI answer used as current platform authority.** Fix: verify the primary source or quarantine it.
- **Fixed 50-word opening, FAQ-everywhere, monthly cadence, or three-second rule.** Fix: make it a documented local experiment or remove it.
- **Schema facts not visible or not proven.** Fix: omit them and log the evidence gap.
- **Manufactured third-party mentions, reviews, or UGC.** Fix: use authentic, rights-cleared evidence and moderation.
- **One page cloned for every query variant.** Fix: consolidate around a real audience need and add only useful coverage.
- **Citation, referral, and conversion treated as one KPI.** Fix: define and reconcile each outcome separately.

## References

- [SaaS content web handoff](references/saas-content-web-handoff.md): read when the page is part of a SaaS content web, a comparison page or a LinkedIn-linked destination.
- [SERP study and editorial lens](references/serp-study-and-editorial-lens.md): read when running the three-wave SERP study before drafting an article or applying the customer-language and voice lens.
- [AI search and social discovery rules](../../ai-marketing/ai-generative-search-optimisation/references/ai-search-and-social-discovery-rules.md): read when mapping customer language and intent.
- [Customer-language bank and intent map](../../ai-marketing/ai-generative-search-optimisation/references/ai-search-and-social-discovery-rules.md) and the [real-time bridge and voice contract](../../playbooks/playbook-content-production/references/real-time-content-bridge-and-voice.md): read when choosing phrases and preserving a human voice.
- [Social source register](../../../docs/source-registers/source-register.json): read when a platform or market claim needs its dated register entry.
- [Digital Research currentness gate](https://github.com/peterbamuhigire/digital-research-skills/blob/main/docs/continuous-improvement/kaizen-currentness-gate.md): read when a current Google, Bing, OpenAI or platform claim must be dated.
- [Digital Research source evaluation](https://github.com/peterbamuhigire/digital-research-skills/blob/main/skills/source-evaluation/SKILL.md): read when grading a source's tier.
- [Digital Research source verification](https://github.com/peterbamuhigire/digital-research-skills/blob/main/skills/source-verification/SKILL.md): read when verifying a claim before it goes on the page.
- [AI Generative Search Optimisation](../../ai-marketing/ai-generative-search-optimisation/SKILL.md): read when the question is programme-wide or the SEO/AEO/GEO disposition is needed.
- [AI slop ship gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting or revising page copy.
<!-- dual-compat-end -->
