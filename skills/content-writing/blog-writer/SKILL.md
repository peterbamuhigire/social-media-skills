---
name: blog-writer
description: Use when Blog Writer is needed to produce a publication-ready copy for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Blog Writer

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **publication-ready copy** and the supplied brief falls within blog writer.

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
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified publication-ready copy; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Channel, format and audience commitment level are known | Choose the hook, structure and call to action native to that context. | Copy that could be pasted unchanged onto any channel or brand. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact publication-ready copy, consumer, market, channel and approval boundary; route to `caption-writer` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete publication-ready copy; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Publication-ready copy | Requester, client reviewer or delivery team | The publication-ready copy addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested publication-ready copy, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [caption-writer](../caption-writer/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Generate a complete, professional blog post from a brief. The output is a finished article in markdown — ready to paste into a CMS, share with a client, or hand to a web developer.

## Required Input
Ask for these before writing:

1. **Client business name and industry**
2. **Country / city** (default: Uganda/East Africa)
3. **Article topic or working title**
4. **Target reader** — who is this for? (job role, situation, problem they have)
5. **Search intent** — are they looking to learn, compare, or decide?
6. **Key questions** the article must answer (3–5)
7. **Word count target** (default: 1,200–1,800 words)
8. **Call to action** — what should the reader do at the end?
9. **Tone** — professional / conversational / authoritative (default: professional)

If any input is missing, ask before writing. Do not guess intent.

## Article Structure
Generate in this order:

### Frontmatter block
```
Title: [SEO-optimised title, under 60 characters, primary keyword included]
Meta description: [Under 155 characters, includes primary keyword and location]
Primary keyword: [The main search phrase this article targets]
Secondary keywords: [2–3 related phrases]
Estimated read time: [X min read at 200 words/min]
```

### Article body
1. **Opening hook** (1–2 paragraphs) — do not open with a definition or generic statement. Use one of: a specific scenario the reader recognises, a surprising fact, a question that surfaces a real problem, or a short story with a lesson.
2. **Nut paragraph** — if the opening uses a story or scenario, follow it immediately with a grounding paragraph that states what the article covers and why it matters.
3. **Body sections** — 4–7 H2 sections. Each section answers one of the key questions provided. Use H3 subheadings where a section has distinct sub-topics.
4. **Practical takeaways** — at least one section must give the reader something concrete to act on (a checklist, a decision framework, a step-by-step).
5. **Conclusion** — reconnect to the opening (full-circle structure). End with a natural, non-pushy CTA.

## Writing Standards
Apply the `east-african-english` skill for language and tone. Also:

- **British spelling** — organisation, programme, colour, analyse, recognise
- **Active voice** — 90%+ of sentences. Passive only when the actor is unknown.
- **Sentence variety** — mix short (8–12 words) and medium (20–28 words). No sentence over 35 words.
- **One idea per paragraph** — 2–4 sentences each.
- **Concrete and specific** — use numbers, named places, real examples. No vague abstractions.
- **No AI vocabulary** — never use: delve, tapestry, landscape (metaphorical), leverage, navigate (metaphorical), foster, realm, game-changer, revolutionary, groundbreaking.
- **No filler phrases** — cut: "in order to" → "to", "due to the fact that" → "because", "it is important to note that" → state it directly.
- **No weak modifiers** — cut: really, very, quite, basically, actually, somewhat.
- **Take positions** — at least 2 clear opinions or recommendations per article. "I recommend" not "one might consider".
- **Commit, do not hedge** — "This approach works for SMEs" not "This could potentially be a viable option".

For premium thought leadership or lead-generation articles, also apply `premium-commercial-writing`: build a message spine before drafting, state a clear point of view, make the mechanism visible, add proof density, and structure the article so both readers and AI-search systems can extract the main answer.

## SEO Requirements
- Primary keyword in: title, first 100 words, at least one H2, and the conclusion.
- Secondary keywords distributed naturally through body. Never keyword-stuff.
- Internal linking suggestions: note 2–3 places where the client could link to related pages (service pages, about, contact) — mark as `[LINK: suggested anchor text → page type]`.
- External links: suggest 1–2 authoritative sources to cite where data or claims need backing.

## Platform Adaptation Notes
If the article will be shared as social content after publication, include at the end:

**Social cut-downs:**
- LinkedIn post (150 words) — professional tone, key insight as the hook
- Facebook post (80 words) — warmer, question-led
- X/Twitter thread opener (280 characters) — bold claim or surprising fact

Only include this section if the user requests it.

## Human Authenticity Gate
All content produced using this skill must pass through the `ai-content-humaniser` before client delivery. AI-generated or AI-assisted blog drafts must meet the Golden Rule: every article must look, feel, and sound as if it was crafted by the most skilled human writer with genuine expertise in the subject and deep knowledge of the East African reader. Generic, flat, or culturally misaligned output is not acceptable regardless of how efficiently it was produced.

## Quality Criteria
Good output meets all of these:

- [ ] Opening hook captures attention without being generic or clichéd
- [ ] Every H2 section answers a real question the target reader would have
- [ ] At least one section provides a concrete, actionable takeaway
- [ ] No banned vocabulary or filler phrases
- [ ] Primary keyword placed naturally in title, opening, at least one H2, and conclusion
- [ ] British spelling throughout
- [ ] Conclusion reconnects to the opening and includes a clear CTA
- [ ] Tone matches the client's industry and the East African professional register
- [ ] Article reads as written by a human with genuine expertise, not as generated content

## References
| File | When to Read |
|---|---|
| `references/human-voice-standards.md` | If the article risks sounding generic or AI-generated — run the voice checklist |
| `references/writing-craft.md` | For sentence structure, opening hook techniques, paragraph rhythm |
| `references/editorial-standards.md` | For punctuation, capitalisation, and grammar rules |
| `east-african-english/SKILL.md` | For tone calibration, British English spelling list, courteous phrasing |
| `premium-commercial-writing/SKILL.md` | For premium positioning, proof density, value framing, and SEO/GEO-aware authority structure |
