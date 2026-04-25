---
name: biz-dev-case-study
description: Generates a polished client case study in two formats — a 1-page written version and a 3-slide deck outline — from raw information the consultant provides. Invoke when a consultant needs to document and publish a client success story for use in credentials documents, proposals, the agency website, or pitches.
---
# Client Case Study Generator

Produce two outputs: (1) a 1-page written case study and (2) a 3-slide deck outline. Both must be ready to share or present without significant editing. Use specific metrics throughout — never vague claims. Apply East African English and third-person professional register.

<!-- dual-compat:start -->
## Use when
- Generates a polished client case study in two formats — a 1-page written version and a 3-slide deck outline — from raw information the consultant provides. Invoke when a consultant needs to document and publish a client success story for use in credentials documents, proposals, the agency website, or pitches.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Read files in `references/` only when the body points to them or when you need the deeper framework, examples, or evidence.
4. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use.

## References
- Read `references/proposal-frameworks.md` when you need the deeper framework, examples, or supporting material it contains.

<!-- dual-compat:end -->

## Required Input

Ask for the following before generating:

- **Client industry or anonymised descriptor** — e.g., "Kampala-based retail brand" or use the client's actual name if approved
- **Whether the client name can be used** — if yes, use it; if no, create a consistent anonymised descriptor throughout
- **Challenge faced** — the specific problem or situation the client was dealing with before engaging the consultant
- **What was done** — detailed description of the work: what was implemented, in what sequence, and why each step mattered
- **Results achieved** — specific metrics (follower growth numbers or percentages, engagement rate before and after, leads generated, revenue attributed, website traffic change, or any other measurable outcome)
- **Client testimonial** — direct quote if available; if not available, note this and insert the placeholder

If results are vague ("things improved"), ask the consultant to provide specific numbers before proceeding. The case study is only credible with real metrics.

---

## Output 1: 1-Page Written Case Study

Generate this as a standalone, shareable document. Use the exact four-section structure below. Do not reorder or add sections.

---

### Document Header

**[Client Name or Anonymised Descriptor]**
*[Industry / Sector] | [City, Country]*
*A case study by [Agency Name]*

---

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

---

## Output 2: 3-Slide Deck Version

Generate immediately after the written case study. Use the exact deck format from CLAUDE.md for all three slides.

**Slide N — [Slide Title]**
**Headline:** [The one thing the audience must remember]
**Bullets:**
- [3–5 bullets maximum]
**Speaker Notes:** [What the presenter says — context not shown on slide]
**Visual Direction:** [Layout, imagery, chart type, colour guidance]

---

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

---

## Formatting Rules

- Written case study: full prose for Problem and Approach; bullet list for Results; block quote for testimonial
- Deck outline: strict slide-by-slide format — no deviations from the four-field structure
- Anonymised descriptor must be consistent throughout both outputs (do not vary the phrasing)
- Dates and timeframes in British format (e.g., "over 90 days", "January–March 2025")
- Do not editoralise in the Problem section; save analysis for Approach and Speaker Notes
- Do not use the phrase "social media presence" as a stand-alone result — it is not a metric

---

## Persuasion Frameworks

Apply frameworks from `references/proposal-frameworks.md` when generating this document.

Key principles for case studies:
- Structure every case study using NOSE: the client's Need first, then the Outcome they achieved, then the Solution (the agency's approach), then the Evidence (specific numbers) (Sant: NOSE)
- Write the case study from the client's perspective — the client is the hero; the agency is the enabler (Hatton: Empathy Model)
- The most persuasive case study directly mirrors the prospective client's situation — match sector, challenge type, and scale (Sant: Evidence placement)
- Every case study must contain at least one specific number: enquiries generated, revenue attributed, percentage growth, cost per lead — general outcomes are not evidence (Sant: Quality Maxim)
- Eliminate Weasel language: "we helped them improve performance" is not evidence; "enquiries increased from 12 to 47 per month in 90 days" is (Sant: Fluff/Guff/Geek/Weasel Test)

Read `references/proposal-frameworks.md` for the NOSE structure and evidence standards.

---

## Quality Criteria

- Problem section is specific and factual with no vague observations
- Approach section explains the reasoning behind decisions, not just what was done
- Results section contains only specific, named metrics — no vague intensifiers
- Written case study fits on one printed page (approximately 350–450 words)
- Deck slides follow the exact four-field format with no missing fields
- Slide 3 headline leads with the strongest metric, not a generic phrase
- Client quote is genuine or clearly marked as a placeholder — never fabricated
- Anonymisation is consistent and plausible throughout both outputs
