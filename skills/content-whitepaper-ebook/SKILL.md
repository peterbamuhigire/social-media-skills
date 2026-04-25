---
name: content-whitepaper-ebook
description: >
  Produces a complete long-form content asset — either a whitepaper (research-led, evidence-based)
  or an eBook (practical guide, how-to) — for a client operating in Uganda or East Africa.
  Invoke this skill when a client needs a 2,000–5,000 word PDF-ready document for lead generation,
  thought leadership, donor reporting, investor communications, or conference distribution.
  Triggers: "write a whitepaper", "create an eBook", "lead magnet document", "thought leadership
  report", "donor report", "investor document", "long-form content asset".
---
# content-whitepaper-ebook

Generates a fully structured whitepaper or eBook for a client. Output is paste-ready body copy
organised by section, written to PDF-ready standard. Apply the `east-african-english` skill for
all tone and register decisions. This skill does not produce .pdf or .docx files — it produces
the text content that a designer or the client pastes into their chosen layout tool.

---

<!-- dual-compat:start -->
## Use when
- Produces a complete long-form content asset — either a whitepaper (research-led, evidence-based) or an eBook (practical guide, how-to) — for a client operating in Uganda or East Africa. Invoke this skill when a client needs a 2,000–5,000 word PDF-ready document for lead generation, thought leadership, donor reporting, investor communications, or conference distribution. Triggers: "write a whitepaper", "create an eBook", "lead magnet document", "thought leadership report", "donor report", "investor document", "long-form content asset".
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- The requested copy asset or idea set in markdown, written to publish, review, or adapt without major rework.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Inputs

Ask for all of the following before generating any content:

1. **Client business name** — trading name as it should appear on the document
2. **Industry** — sector (e.g. agri-finance, health NGO, professional services, FMCG)
3. **Country/city** — default Uganda/East Africa if not specified
4. **Document type** — whitepaper or eBook (see Section 1 for the decision rule)
5. **Topic or working title** — a draft title is sufficient; refine it during generation
6. **Target reader** — job role, organisation type, and the specific problem they are trying to solve
7. **Key argument / central thesis** — the single most important thing the document must convince the reader of
8. **Data or research the client can provide** — internal data, market surveys, programme results, third-party reports
9. **Intended use** — lead magnet, donor report, investor document, conference handout, media pitch support
10. **Distribution channel** — email gate, LinkedIn post, website download, conference handout, WhatsApp broadcast

If the client cannot answer items 7 or 8, pause and prompt them before proceeding. A whitepaper
without a thesis is a brochure. An eBook without a reader problem is a catalogue.

---

## Section 1 — Whitepaper vs eBook: Decision Rule

Apply this distinction before choosing a structure template.

**Whitepaper**
- Research-led, evidence-based, formal register
- Makes an argument using data, case studies, and analysis
- Common contexts: B2B, NGO/donor, public sector, professional services, policy advocacy
- Length: 3,000–6,000 words
- Format: sections with headers, executive summary, numbered references
- Reader motivation: "I need to understand this sector/problem at a deep level"
- Signal: the client wants to be seen as an expert who has done the research

**eBook**
- Practical guide, how-to, or curated advice
- Reader-centric, actionable, accessible register
- Common contexts: B2C thought leadership, service marketing, training, SME audiences
- Length: 2,000–4,000 words
- Format: conversational, bulleted, visual-friendly, chapter-based
- Reader motivation: "I need tools and steps I can use immediately"
- Signal: the client wants to give the reader practical value

**Decision rule:** If the primary output is an argument supported by evidence → whitepaper.
If the primary output is a set of actions the reader can take → eBook.

When the client is unsure, ask: "After reading this document, do you want the reader to think
differently about a problem, or to do something differently?" Thinking → whitepaper. Doing → eBook.

---

## Section 2 — Document Structure Templates

### Whitepaper Structure

Generate each section in order. Write the Executive Summary last, then position it first.

1. **Cover page** — title, subtitle, client name, date, classification label ("Public" or "Confidential")
2. **Executive Summary** (300–400 words) — problem statement + 3 key findings + 3 recommendations. Write this last.
3. **Introduction** — context, why this topic matters now in Uganda/EA, scope and limitations of the document
4. **Background / Market Context** — data on the sector, platform, or problem; cite every statistic
5. **Key Findings / Analysis** (2–4 sections) — each section presents one finding with supporting data and interpretation
6. **Case Study or Example** — one real-world example from the EA market; anonymise if the client requires it
7. **Recommendations** — 3–5 specific, actionable recommendations for the target reader; one recommendation per bullet
8. **Conclusion** — restate the central thesis; close with a clear call to action
9. **References / Sources** — full citations in Harvard style

### eBook Structure

Generate each chapter in order. The introduction sets reader expectations; every chapter delivers on them.

1. **Cover page** — title, subtitle, a clear "what you will learn" statement (3 bullets maximum)
2. **Introduction** — who this is for, what problem it solves, what the reader will be able to do after reading
3. **Chapter 1** — the problem or the first step (establish the context before offering the solution)
4. **Chapter 2** — the solution or second step (the core practical guidance)
5. **Chapter 3** — deepening the solution (nuance, common variations, sector-specific application)
6. **Chapter 4** — advanced application or common mistakes to avoid (raise the reader's confidence)
7. **Conclusion** — recap the key points; tell the reader exactly what to do next
8. **About [Business Name]** — one short paragraph on who the client is and what they offer; include contact details
9. **Call to Action page** — one clear action the reader should take now (book a consultation, join the newsletter, download a template)

---

## Section 3 — Writing Standards

Apply these on top of the `east-african-english` skill standards.

- **Executive Summary is written last, positioned first.** Complete all other sections, then write
  the Executive Summary as a standalone 300–400 word synthesis. Never draft it first.
- **Cite every statistic.** If the client cannot provide data, draw from publicly available EA sources:
  Uganda Bureau of Statistics (UBOS), World Bank Uganda open data, GSMA Mobile Economy Africa,
  Statista (with subscription note), Meta Audience Insights, TikTok for Business Africa data.
- **State the central thesis in both the Introduction and the Conclusion.** The reader must never
  finish the document wondering what it was trying to prove or recommend.
- **One recommendation per bullet.** Never bundle two recommendations into one point.
- **Match language to the target reader.** A whitepaper for Ugandan SME owners uses plain English
  and local market references. A whitepaper for DFID/FCDO programme officers uses development
  sector terminology and international benchmarks. Ask about the reader before writing.
- **Sub-headings every 400 words maximum.** EA professional readers frequently read on mobile.
  Long unbroken text blocks lose them. Use descriptive sub-headings, not decorative ones.
- **Avoid vague conclusions.** Every recommendation must answer: who should do this, what exactly,
  and by when or with what resources?

---

## Section 4 — Lead Generation Integration

Apply this section when the intended use is a lead magnet or gated download.

**Email gate setup:** Instruct the client to gate the document behind a sign-up form using one of:
- MailChimp (free up to 500 contacts) — recommended for clients starting from zero
- Brevo (free up to 300 emails/day) — recommended for clients who need automation
- ConvertKit — recommended for clients building a creator or coaching business

**Landing page copy template** — generate this copy block as part of the deliverable:

```
[Headline: the specific benefit the reader gets from downloading]
[Sub-headline: who this is for — job role or situation in one sentence]

What you will learn:
- [Benefit 1 — concrete and specific]
- [Benefit 2 — concrete and specific]
- [Benefit 3 — concrete and specific]

[Form: First name + Email address only — no additional fields]
[Button label: "Download the free guide" or "Get the whitepaper" — match document type]
[Trust signal: "No spam. Unsubscribe any time."]
```

**Four-channel launch plan** — generate a brief for each channel at launch:
1. LinkedIn post — professional context, why this topic matters, link to landing page
2. Facebook post — broader audience hook, visual description, link or DM instruction
3. Email to existing list — subject line + 3-sentence body + download link
4. WhatsApp broadcast — one sentence hook + shortened link (use Bitly or similar)

---

## Section 5 — Donor / Investor Variant

Apply this section in full when the intended use is a donor report or investor document.

- Use formal register throughout: no contractions, no colloquialisms, no first-person informality.
- Include an **impact metrics table** with columns: Indicator | Target | Achieved | Variance | Notes.
  Populate with the client's programme data; flag any gaps for the client to fill.
- Cite international frameworks where relevant: UN Sustainable Development Goals (SDGs),
  UNDP Human Development Index, World Bank poverty and inclusion data, IFC investment principles.
- Include a **Theory of Change description**: inputs → activities → outputs → outcomes → impact.
  Write this as a structured paragraph the designer can render as a diagram. Label each stage.
- Replace "beneficiaries" with "participants", "community members", or a specific descriptor
  agreed with the client (e.g. "smallholder farmers", "adolescent girls in Karamoja").
- Proofread all citations against original sources before delivering. Donor and investor audiences
  verify citations; errors undermine credibility immediately.
- Add a **financial accountability section** if the document is for a donor: budget allocated,
  budget spent, variance explanation, auditor or board sign-off status.

---

## Human Authenticity Gate

All content produced using this skill must pass through the `ai-content-humaniser` before client delivery. AI-generated or AI-assisted long-form documents must meet the Golden Rule: every whitepaper or eBook must look, feel, and sound as if it was researched and written by the most skilled human expert with genuine authority in the subject and deep knowledge of the East African context. Generic, flat, or culturally misaligned output is not acceptable regardless of how efficiently it was produced.

---

## Quality Criteria

Output meets the standard for this skill when all of the following are true:

- The whitepaper vs eBook distinction has been applied and the correct structure template used
- The Executive Summary is written last and positioned first, within the 300–400 word limit
- Every statistic in the document carries a named source; no unsourced claims appear
- The central thesis is stated explicitly in both the Introduction and the Conclusion
- All recommendations are specific, actionable, and written one per bullet with no bundling
- If the intended use is a lead magnet: a landing page copy block and a four-channel launch brief are included
- If the intended use is donor or investor: the impact metrics table, Theory of Change description,
  and formal register requirements are applied in full

---

## References

| Skill | When to use it |
|---|---|
| `blog-writer/SKILL.md` | Repurposing whitepaper or eBook content into blog posts for distribution |
| `owned-media-strategy/SKILL.md` | Planning how the document fits into the client's broader owned media ecosystem |
| `07-email-marketing-strategy/SKILL.md` | Building the email nurture sequence that follows a gated download |
| `east-african-english/SKILL.md` | All tone, register, and language decisions — read before writing any section |
