---
name: caption-writer
description: Use when Caption Writer is needed to produce a publication-ready copy for social-media or digital-marketing work; use `email-copywriter` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Caption Writer

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **publication-ready copy** and the supplied brief falls within caption writer.

## Do Not Use When
- Use `email-copywriter` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
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
1. Confirm the exact publication-ready copy, consumer, market, channel and approval boundary; route to `email-copywriter` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete publication-ready copy; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.
7. Check the caption against the audience's situation, narrative job, first-line information hierarchy, readability, one-action CTA, accessibility needs, and factual/permission register before release.

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
- Prefer concrete audience context, a purposeful sequence of hook/proof/choice/consequence, and plain language over decorative persuasion. If the post uses AI, route through its disclosure and human-review rules.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested publication-ready copy, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.
- Treating a strong hook as sufficient when the audience cannot understand the offer or next step. **Fix:** rewrite the information hierarchy and test the CTA on the target mobile format.
- Using a visual or claim without permission, alternative description, or source status. **Fix:** stop the post or supply the missing evidence.

## References
- [email-copywriter](../email-copywriter/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## How to Use This Skill
Collect the Required Input below. Generate 3 caption variations per request — labelled Short, Medium, and Long — each with a distinct approach, appropriate hashtag set, and platform-specific formatting. Apply British English throughout. Do not reuse the same hook across variations — each must be genuinely different in structure and tone.

When the post supports a premium offer, executive audience, high-ticket service, or trust-sensitive category, apply `premium-commercial-writing` before finalising. The caption should create value, show proof or judgement, and ask for a next step without sounding desperate or discount-led.

## Required Input
Ask for the following before writing:

- **Client name / brand name** — the business publishing the post
- **Industry** — sector (e.g. food and beverage, retail, professional services)
- **Country / city** — default Uganda/East Africa
- **Primary goal** — what the caption should achieve (awareness / engagement / enquiries / sales)
- **Platform** — Instagram / Facebook / LinkedIn / TikTok / WhatsApp broadcast / X (Twitter)
- **Content type** — photo / video / carousel / text post / Reel / Story
- **Topic** — what the post is about (one sentence)
- **Key message** — the single most important thing the audience should take away (one sentence)
- **CTA** — what the audience should do after reading (one clear action)
- **Tone** — professional / conversational / aspirational / educational (or specific brand tone words)
- **Any keywords or phrases to include** — mandatory phrases, product names, or campaign lines
- **Any banned vocabulary** — from 04-brand-voice-intake if available

## Platform-Specific Rules
Apply these conventions when generating captions. Do not blend conventions across platforms.

### Instagram
- Hook in the first line — the first 125 characters appear before the "more" cut; everything depends on this line
- Use line breaks between paragraphs — Instagram compresses unbroken text
- Conversational or aspirational tone depending on the brand
- Optimal length: 125–150 characters for maximum reach; up to 300 words for educational or storytelling content
- Hashtags: 5–10, placed at the end of the caption or noted as suitable for first comment; mix niche, community, and 1–2 branded tags
- No more than 2 emojis in the hook line

### Facebook
- Warm, community-focused tone; question-based CTAs perform well ("Have you tried this? Let us know below")
- Optimal length: 40–80 characters for highest organic reach; up to 250 words for storytelling or event posts
- If the post includes a link, include it in the caption text — not only in the link preview
- Hashtags: 1–3 maximum; Facebook hashtags add limited discoverability — use sparingly
- Write as if speaking to a neighbour, not an audience

### LinkedIn
- Professional, evidence-based, direct
- First 2 lines carry the entire weight — they appear before the "see more" cut; make them count
- No emoji overuse — 0–2 per post, purposeful only
- Optimal length: 150–300 words for engagement; 50–100 words for reach-focused posts
- Hashtags: 3–5 maximum, placed at the end; industry-relevant only — never generic tags
- No buzzwords — no "synergy", "leverage", "game-changing", "disruptive"

### TikTok
- Punchy, casual, hooks the first scroll — caption is secondary to the video but still matters
- Optimal length: 100–150 characters
- CTA drives comments: "Comment 'YES' if this resonates" / "Tell me in the comments"
- Hashtags: 3–5 — 1 niche + 1 trending or broad + 1 branded; placed at end or woven naturally into text
- Conversational tone; can be playful — match the energy of the video

### WhatsApp Broadcast
- Personal and direct — write as if to one person you know
- Open with "Hi [first name]" or equivalent warm greeting
- Short paragraphs — one idea per paragraph; easy to read on a small screen
- No hashtags
- One clear action: reply / click link / visit store — not multiple options
- Optimal length: under 150 words; every word must earn its place

### X / Twitter
- Punchy, take a position, conversational
- 240–280 characters for a single post; use thread format for longer content (indicate thread breaks with 1/, 2/, etc.)
- 1–2 hashtags maximum; weave them naturally into the text — do not stack them at the end
- Hook with a take or observation, not an announcement
- Conversational, opinionated, direct — not corporate

## Caption Quality Standards
Apply to every variation before outputting:

- Hook must work as a standalone sentence that creates curiosity or compels action
- One CTA per caption — never two competing actions
- British English: organisation, colour, programme, behaviour, analyse, recognise, centre, enquiry
- No banned vocabulary: leverage, game-changing, groundbreaking, revolutionary, delve, tapestry
- No filler phrases: "in today's world", "it's important to note", "at the end of the day", "we are excited to announce"
- Consistent with brand tone (from 04-brand-voice-intake if provided)
- Active voice throughout — not "great service is offered by us" but "we offer great service"

## EA-Specific Hashtag Communities
Suggest relevant tags from this list when generating hashtag sets for Uganda/EA clients:

**Uganda-specific:** #UgandaTwitter #MadeInUganda #KampalaLife #UgandaEntrepreneur #BuyUgandaBuildUganda #DiscoverUganda #KampalaEats #KampalaFashion #UgandaFood #UgandaTech

**East Africa regional:** #EastAfricaBusiness #NairobiTwitter #EastAfricaCreatives #NairobiBusiness #DarEsSalaamBusiness #EastAfricaHealth #MadeInKenya

**Pan-African:** #AfricanEntrepreneur #MadeInAfrica #AfricanWomenInBusiness #AfricaRising #SMEAfrica #StartupAfrica #BlackOwnedBusiness #SocialEnterprise

Select and combine: 1–2 local/city tags + 1–2 niche industry tags + 1–2 community tags for most platforms. Adjust count to match platform conventions above.

## Output Format
For each caption request, output in this structure:

**CAPTION — [Platform] | [Content Type] | [Brand Name]**

**SHORT VARIATION**
*Approach: [describe the hook strategy — e.g. question-led / bold statement / curiosity gap]*

[Caption text — short version]

*Hashtags:*
[hashtag set appropriate to platform and count]

**MEDIUM VARIATION**
*Approach: [describe the hook strategy — different from Short]*

[Caption text — medium version]

*Hashtags:*
[hashtag set]

**LONG VARIATION**
*Approach: [describe the hook strategy — different from Short and Medium]*

[Caption text — long version]

*Hashtags:*
[hashtag set]

**NOTES FOR THIS POST:**
- [Any platform-specific recommendation — e.g. "For Instagram, consider placing hashtags in the first comment to keep the caption clean"]
- [Any timing recommendation if relevant — e.g. "Post between 7–9pm EAT for highest Facebook reach among Kampala audiences"]
- [Flag if the brief contained ambiguity — e.g. "CTA was not specified — assumed WhatsApp link. Confirm before scheduling."]

## Example Application (Uganda — Food and Beverage)
**Brief:** Platform: Instagram | Content type: Photo | Topic: New seasonal menu launch | Key message: Fresh, locally sourced ingredients | CTA: Visit the restaurant this weekend | Tone: Warm, aspirational | Brand: Nakibuuka Kitchen

**SHORT VARIATION**
*Approach: Bold statement — leads with the product benefit, not the announcement*

Fresh food tastes different when it travels 12 kilometres, not 1,200.

Our new seasonal menu is here — every ingredient sourced within Central Uganda. Come taste the difference this weekend.

🔗 Reserve your table via the link in bio.

*Hashtags:*
#NakibuukaKitchen #KampalaEats #MadeInUganda #UgandaFood #FarmToTable

**MEDIUM VARIATION**
*Approach: Question-led — draws the reader into a shared experience before revealing the offer*

When did you last eat a meal where you knew exactly where every ingredient came from?

Our new seasonal menu answers that question. Every vegetable, every grain, every cut of meat — sourced from farms within Central Uganda. Fresher. Better. Ours.

The menu changes with the season. This one is available until the end of April.

Visit us at [location] this weekend. Reservations via the link in bio.

*Hashtags:*
#NakibuukaKitchen #KampalaEats #UgandaFood #MadeInUganda #FarmToTable #KampalaLife #DiscoverUganda

**LONG VARIATION**
*Approach: Story-led — opens with a behind-the-scenes narrative before the offer*

Every Thursday morning, our kitchen team drives out to Wakiso District.

Not to shop at a supermarket. To collect directly from the farmers we have worked with for three years — the people who grow our tomatoes, harvest our plantain, and raise the free-range poultry that has been on our menu since we opened.

This week, we launched our new seasonal menu. It is the freshest one we have made.

Every dish reflects what is ready right now — not what is convenient. That means the flavours change. The menu changes. And the meals you eat here in April will taste different from the ones you enjoyed in January.

We think that is exactly as it should be.

Come and eat with us this weekend. Bring someone who has not been before.

Reservations: link in bio. Walk-ins welcome before 1pm.

*Hashtags:*
#NakibuukaKitchen #KampalaEats #UgandaFood #MadeInUganda #FarmToTable #KampalaLife #DiscoverUganda #UgandaEntrepreneur

## Human Authenticity Gate
All content produced using this skill must pass through the `ai-content-humaniser` before client delivery. AI-generated or AI-assisted captions must meet the Golden Rule: every caption must look, feel, and sound as if it was crafted by the most skilled human copywriter with deep knowledge of the target audience and their cultural context. Generic, flat, or culturally misaligned output is not acceptable regardless of how efficiently it was produced.

## Quality Criteria
- [ ] Each variation genuinely differs in length and approach — not the same caption padded or shortened
- [ ] Hook line of each variation is distinct and compelling — three different strategies, not three versions of the same opener
- [ ] CTA is clear, specific, and matches platform convention (one action only)
- [ ] Hashtag count and placement match the platform rules specified in this skill
- [ ] No banned vocabulary in any variation
- [ ] British English spelling throughout all variations
- [ ] Tone matches the brand descriptor provided in the brief
- [ ] Output format follows the structure above — labelled, consistent, ready to copy
- [ ] Premium or high-ticket captions show specificity, proof, and value before asking for action
