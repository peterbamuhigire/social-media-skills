---
name: content-whitepaper-ebook
description: Use when content-whitepaper-ebook is needed to produce a content whitepaper ebook deliverable for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# content-whitepaper-ebook

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **content whitepaper ebook deliverable** and the supplied brief falls within content-whitepaper-ebook.

## Do Not Use When
- Use `caption-writer` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Content brief, channel, audience, message, format and call to action | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified content whitepaper ebook deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Channel, format and audience commitment level are known | Choose the hook, structure and call to action native to that context. | Copy that could be pasted unchanged onto any channel or brand. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact content whitepaper ebook deliverable, consumer, market, channel and approval boundary; route to `caption-writer` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete content whitepaper ebook deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Content whitepaper ebook deliverable | Requester, client reviewer or delivery team | The content whitepaper ebook deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested content whitepaper ebook deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [caption-writer](../caption-writer/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Generates a fully structured whitepaper or eBook for a client. Output is paste-ready body copy
organised by section, written to PDF-ready standard. Apply the `east-african-english` skill for
all tone and register decisions. This skill does not produce .pdf or .docx files — it produces
the text content that a designer or the client pastes into their chosen layout tool.

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

## Human Authenticity Gate
All content produced using this skill must pass through the `ai-content-humaniser` before client delivery. AI-generated or AI-assisted long-form documents must meet the Golden Rule: every whitepaper or eBook must look, feel, and sound as if it was researched and written by the most skilled human expert with genuine authority in the subject and deep knowledge of the East African context. Generic, flat, or culturally misaligned output is not acceptable regardless of how efficiently it was produced.

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

## References
| Skill | When to use it |
|---|---|
| `blog-writer/SKILL.md` | Repurposing whitepaper or eBook content into blog posts for distribution |
| `owned-media-strategy/SKILL.md` | Planning how the document fits into the client's broader owned media ecosystem |
| `07-email-marketing-strategy/SKILL.md` | Building the email nurture sequence that follows a gated download |
| `east-african-english/SKILL.md` | All tone, register, and language decisions — read before writing any section |
| `premium-commercial-writing/SKILL.md` | For thesis strength, proof density, authority signals, value framing, and premium commercial polish |
