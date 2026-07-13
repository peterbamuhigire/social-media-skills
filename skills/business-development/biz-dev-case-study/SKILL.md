---
name: biz-dev-case-study
description: Use when Client Case Study Generator is needed to produce a evidence-backed case study for social-media or digital-marketing work; use `biz-dev-positioning` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Client Case Study Generator

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **evidence-backed case study** and the supplied brief falls within client case study generator.

## Do Not Use When
- Use `biz-dev-positioning` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Commercial brief, target buyer, offer, proof and requested next step | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified evidence-backed case study; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Buyer problem, proof strength and commercial objective align | Choose the offer and proof sequence that supports the requested buying decision. | A generic sales asset with unsupported claims or the wrong ask. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact evidence-backed case study, consumer, market, channel and approval boundary; route to `biz-dev-positioning` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete evidence-backed case study; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Evidence-backed case study | Requester, client reviewer or delivery team | The evidence-backed case study addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source/assumption register and completed release checklist | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested evidence-backed case study, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [biz-dev-positioning](../biz-dev-positioning/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Produce two outputs: (1) a 1-page written case study and (2) a 3-slide deck outline. Both must be ready to share or present without significant editing. Use specific metrics throughout — never vague claims. Apply East African English and third-person professional register.

## Required Input
Ask for the following before generating:

- **Client industry or anonymised descriptor** — e.g., "Kampala-based retail brand" or use the client's actual name if approved
- **Whether the client name can be used** — if yes, use it; if no, create a consistent anonymised descriptor throughout
- **Challenge faced** — the specific problem or situation the client was dealing with before engaging the consultant
- **What was done** — detailed description of the work: what was implemented, in what sequence, and why each step mattered
- **Results achieved** — specific metrics (follower growth numbers or percentages, engagement rate before and after, leads generated, revenue attributed, website traffic change, or any other measurable outcome)
- **Client testimonial** — direct quote if available; if not available, note this and insert the placeholder

If results are vague ("things improved"), ask the consultant to provide specific numbers before proceeding. The case study is only credible with real metrics.

## Output 1: 1-Page Written Case Study
Generate this as a standalone, shareable document. Use the exact four-section structure below. Do not reorder or add sections.

### Document Header
**[Client Name or Anonymised Descriptor]**
*[Industry / Sector] | [City, Country]*
*A case study by [Agency Name]*

### Problem
2–3 sentences. Describe the specific challenge the client faced before the engagement. Be concrete: name the platform, the gap, the business impact. Do not be vague. Do not editoralise or offer analysis in this section — describe the situation as it was.

> Example register: "A Kampala-based hospitality group with three properties had an active Facebook page but was generating fewer than 50 engagements per month on a following of 4,200. Their posting was inconsistent — sometimes daily, sometimes silent for two weeks — and their content was almost entirely promotional. Enquiries via social media had dropped by 30% over the previous six months."

### Approach
3–5 sentences. Describe what was done, in what sequence, and the reasoning behind key decisions. Be specific about tactics and tools without being jargon-heavy. Reference relevant frameworks where genuinely applicable — e.g., content pillars, Hero/Hub/Hygiene model (YouTube/Google), 10-4-1 rule (Bodnar and Cohen, 2012). Show the thinking, not just the activity.

> Example register: "The engagement began with a full content audit to understand what had performed historically and identify audience preferences. A three-pillar content strategy was developed — one pillar focused on behind-the-scenes hotel life, one on local Kampala travel inspiration, and one on direct promotional offers — following the Hero/Hub/Hygiene framework. A consistent posting schedule of five times per week across Facebook and Instagram was implemented, with each post individually captioned to match the pillar's tone. Community management was introduced with a four-hour response target during business hours."

### Results
Present as a short intro sentence followed by a bullet list of specific metrics. Use actual numbers from the input. If a metric improved, state the before and after. If only one data point exists, state it clearly. Never use "significantly", "dramatically", or other vague intensifiers.

Intro sentence: "Over [timeframe], the engagement delivered the following results:"

Bullet format:
- [Metric]: [Before figure or baseline] → [After figure] ([percentage change if applicable])
- [Metric]: [Absolute outcome]

> Example:
> - Facebook engagement rate: 1.1% → 4.7% over 90 days
> - Monthly post reach: 3,200 → 18,600 (average across final 30 days of engagement)
> - Enquiries via Facebook Messenger: 12 per month → 41 per month
> - Instagram followers: grew from 820 to 2,340 over 6 months

### What the Client Said
If a testimonial quote was provided, format it as:

> "[Direct quote from client.]"
> — [Client Name or Title, e.g. "Marketing Manager, [Company Name]"]

If no testimonial was provided, insert exactly:

> [Client quote to be added — request testimonial from [client name/descriptor].]

Do not fabricate a quote under any circumstances.

## Output 2: 3-Slide Deck Version
Generate immediately after the written case study. Use the exact deck format from CLAUDE.md for all three slides.

**Slide N — [Slide Title]**
**Headline:** [The one thing the audience must remember]
**Bullets:**
- [3–5 bullets maximum]
**Speaker Notes:** [What the presenter says — context not shown on slide]
**Visual Direction:** [Layout, imagery, chart type, colour guidance]

### Slide 1 — The Challenge
Headline should name the client (or anonymised descriptor) and capture the core problem in one phrase.
Bullets: 3–4 facts about the client's situation before the engagement.
Speaker Notes: Presenter adds context — how the consultant first heard about this client, what the initial discovery conversation revealed.
Visual Direction: Clean, minimal. Left column: client descriptor and industry icon or sector image. Right column: 3–4 bullet points. Muted colours (navy, grey). A single "before" metric can be displayed as a large number for visual impact.

### Slide 2 — The Approach
Headline should convey the strategic logic — not just "what was done" but why it worked.
Bullets: 3–5 steps or decisions, in sequence. Each is a short action phrase.
Speaker Notes: Presenter explains the reasoning behind 1–2 key decisions, connects the approach to the specific challenge on Slide 1.
Visual Direction: Timeline or numbered flow layout. Simple icons for each step. Brand colours or neutral palette. No dense text.

### Slide 3 — The Results
Headline must lead with the strongest metric.
Bullets: List all key metrics from the written case study results section. Prioritise the most impressive and most credible numbers.
Below bullets: Client quote if available (italicised, attributed).
Speaker Notes: Presenter comments on what the numbers mean in business terms — e.g., "41 enquiries a month from a single channel, at no additional ad spend."
Visual Direction: Data-forward layout. Feature the headline metric as a large typographic element (e.g., "4.7% engagement rate"). Secondary metrics as a compact list. Client quote at the bottom in a subtle callout box.

## Formatting Rules
- Written case study: full prose for Problem and Approach; bullet list for Results; block quote for testimonial
- Deck outline: strict slide-by-slide format — no deviations from the four-field structure
- Anonymised descriptor must be consistent throughout both outputs (do not vary the phrasing)
- Dates and timeframes in British format (e.g., "over 90 days", "January–March 2025")
- Do not editoralise in the Problem section; save analysis for Approach and Speaker Notes
- Do not use the phrase "social media presence" as a stand-alone result — it is not a metric

## Persuasion Frameworks
Apply frameworks from `references/proposal-frameworks.md` when generating this document.

Key principles for case studies:
- Structure every case study using NOSE: the client's Need first, then the Outcome they achieved, then the Solution (the agency's approach), then the Evidence (specific numbers) (Sant: NOSE)
- Write the case study from the client's perspective — the client is the hero; the agency is the enabler (Hatton: Empathy Model)
- The most persuasive case study directly mirrors the prospective client's situation — match sector, challenge type, and scale (Sant: Evidence placement)
- Every case study must contain at least one specific number: enquiries generated, revenue attributed, percentage growth, cost per lead — general outcomes are not evidence (Sant: Quality Maxim)
- Eliminate Weasel language: "we helped them improve performance" is not evidence; "enquiries increased from 12 to 47 per month in 90 days" is (Sant: Fluff/Guff/Geek/Weasel Test)

Read `references/proposal-frameworks.md` for the NOSE structure and evidence standards.

## Quality Criteria
- Problem section is specific and factual with no vague observations
- Approach section explains the reasoning behind decisions, not just what was done
- Results section contains only specific, named metrics — no vague intensifiers
- Written case study fits on one printed page (approximately 350–450 words)
- Deck slides follow the exact four-field format with no missing fields
- Slide 3 headline leads with the strongest metric, not a generic phrase
- Client quote is genuine or clearly marked as a placeholder — never fabricated
- Anonymisation is consistent and plausible throughout both outputs
