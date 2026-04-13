---
name: playbook-social-media-brand-style-guide
description: Generates a complete, formatted Social Media Brand Style Guide ready to hand over to a client's social media manager or in-house team. The guide covers brand voice, platform tone adjustments, vocabulary standards, emoji policy, image and video standards, hashtag rules, content approval workflow, breaking-news pause protocol, and language and grammar rules — everything an executor needs to maintain brand consistency without consultant oversight. Invoke when onboarding a new client (before content production begins), whenever a client's social media manager changes, or when a client requests a standalone governance document for their team.
---
# Social Media Brand Style Guide Generator

Produce one complete, formatted Brand Style Guide as a client-ready deliverable. This is not advice or a framework — it is a finished document the client hands to whoever manages their social media. Every section must be filled in with client-specific content. Placeholder text must not appear in the final output.

Apply British English throughout. Follow the `east-african-english` skill for prose register. Default to the Uganda/East Africa market unless the client specifies otherwise.

---

<!-- dual-compat:start -->
## Use when
- Generates a complete, formatted Social Media Brand Style Guide ready to hand over to a client's social media manager or in-house team. The guide covers brand voice, platform tone adjustments, vocabulary standards, emoji policy, image and video standards, hashtag rules, content approval workflow, breaking-news pause protocol, and language and grammar rules — everything an executor needs to maintain brand consistency without consultant oversight. Invoke when onboarding a new client (before content production begins), whenever a client's social media manager changes, or when a client requests a standalone governance document for their team.
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
- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

If the `04-brand-voice-intake` has already been completed for this client, request that document and extract the inputs from it. Do not ask the client to repeat information already captured.

If `04-brand-voice-intake` has not been completed, collect the following before generating anything:

- **Client business name** — exact spelling as it should appear in all communications
- **Industry and primary services or products**
- **Country and city** — defaults to Kampala, Uganda
- **Primary goal for social media** — awareness, leads, sales, community building, retention
- **Three brand tone adjectives** — the client's own words; these are mandatory. Do not proceed without them.
- **Active social media platforms** — list all current and planned platforms
- **Brand colours** — hex codes if available; descriptive if not
- **Approved product/service names** — exact spelling for every product or service
- **Competitor names** — how (or whether) to refer to competitors in content
- **Content approver** — name and role of the person who must approve posts before publishing
- **Content drafter** — name and role of the person who creates content
- **Turnaround time expectation** — how many hours between draft and approval deadline

---

## Output Structure

Generate the guide as a complete, headed document in the following order. Use the section titles exactly as listed.

---

## SECTION 1: BRAND VOICE

### 1.1 Voice Definition

State the three client-supplied tone adjectives. For each adjective, produce a "we are X, not Y" pairing that clarifies where the brand sits on a spectrum:

| We are… | We are not… |
|---|---|
| [Adjective 1 — e.g. Warm] | [Its shadow side — e.g. Familiar to the point of being unprofessional] |
| [Adjective 2] | [Its shadow side] |
| [Adjective 3] | [Its shadow side] |

Follow this table with a tone scale statement using the format below. Mark the brand's position with **[HERE]**:

```
Formal ←————————[HERE]————————→ Informal
```

Write one sentence explaining why this position is correct for this brand and audience.

### 1.2 Brand Voice Summary

Write one paragraph (5–7 sentences) that any new team member reads before writing a single word for this client. Describe the brand voice as if describing a person: who are they, what do they say, what do they never say? This paragraph must be specific to this client — it must be impossible to apply it to a different brand without rewriting.

---

## SECTION 2: PLATFORM-BY-PLATFORM TONE GUIDE

For each platform the client uses, generate a tone guide entry. Omit platforms the client is not active on and does not plan to use.

Use this format for each platform:

---

**[PLATFORM NAME]**

**Tone in one sentence:** [How the brand sounds on this specific platform]

**Rules:**
1. [Specific rule for this platform — formatting, length, opening style, etc.]
2. [Specific rule]
3. [Specific rule]

**Example post:** [A worked example using this client's actual product or service — not a generic placeholder]

---

Cover the following platforms if in scope:

**Facebook** — conversational, community-focused. Lead with a question or an invitation. Short paragraphs. This is where the brand acts as a neighbour, not a broadcaster.

**Instagram** — visual-first, aspirational or relatable depending on personas. The caption supports the image. The first line must work without the "more" button. Hashtags go at the end.

**LinkedIn** — professional, credibility-driven. Lead with an industry observation or data point. Full sentences. One strong idea per post. No more than one emoji if used at all.

**WhatsApp** — personal, direct, value-led. Treat every message as a one-to-one conversation, not a broadcast. Lead with context and value. One clear call to action. Maximum three sentences.

**TikTok** — energetic, entertaining, hook-first. The first word of the caption and the first second of video must earn attention. Use the vocabulary the audience actually uses.

**X / Twitter** — concise, opinionated, topical. One strong idea per post. Cut every word that is not working. A take or a question — never a press release.

---

## SECTION 3: VOCABULARY STANDARDS

### 3.1 Words and Phrases to Use

List 10–15 preferred terms drawn from the client's tone adjectives, industry, and EA professional register. Format as a table:

| Word or Phrase | Why it fits this brand |
|---|---|
| [Term] | [One-line rationale] |

### 3.2 Words and Phrases to Avoid

List 10–15 terms to avoid: overused marketing clichés, off-brand language, competitor terms, and anything that conflicts with the tone attributes. Always include the standard EA avoid list: "groundbreaking", "revolutionary", "game-changing", "amazing", "awesome", "unleash", "skyrocket". Format as a table:

| Word or Phrase | Why to avoid |
|---|---|
| [Term] | [One-line rationale] |

### 3.3 Brand-Specific Terminology

List every product, service, campaign, or internal term that has a specific approved spelling or formatting. Misuse of these terms in published content is not acceptable.

| Term | Correct usage | Common error to avoid |
|---|---|---|
| [Product/service name] | [Exact spelling and capitalisation] | [e.g. Do not abbreviate; do not lowercase] |

### 3.4 Competitor Naming Rules

State the policy clearly:

- **Naming policy:** [e.g. Do not name competitors directly in any published content / Refer to the category only, not specific brands / Approved reference: "other providers in this space"]
- **Comparative claims:** [Permitted with evidence / Not permitted]
- **If a competitor tags or mentions the brand:** [Escalate to approver / Respond using the approved template below / Ignore]

---

## SECTION 4: EMOJI AND STICKER POLICY

State the overall emoji philosophy in one sentence (e.g. "This brand uses emojis functionally and sparingly — they support the message, they do not replace it.").

### 4.1 Platform Emoji Limits

| Platform | Emojis permitted? | Maximum per post | Approved types |
|---|---|---|---|
| Facebook | Yes / Sparingly / No | [Number] | [e.g. Functional and expressive] |
| Instagram | Yes / Sparingly / No | [Number] | |
| LinkedIn | Sparingly / No | [Number — recommend 0–1] | [Functional only] |
| WhatsApp | Yes / Sparingly / No | [Number] | |
| TikTok | Yes / Sparingly / No | [Number] | |
| X / Twitter | Yes / Sparingly / No | [Number] | |

### 4.2 Emoji Categories

Define the policy for each category:

- **Functional emojis** (✅ ➡️ 📌 🔗 — organise or direct): [Permitted / Not permitted]
- **Expressive emojis** (😊 🙌 💙 — convey emotion): [Permitted / Limited to Facebook and WhatsApp only / Not permitted]
- **Decorative emojis** (🌟 ✨ 💫 — pure decoration): [Permitted / Not permitted]

### 4.3 Emojis to Avoid

List 5–8 specific emojis that are off-brand for this client, with a one-line note for each:

| Emoji | Reason to avoid |
|---|---|
| 🔥 | Overused; signals hype rather than substance |
| 💯 | Informal and aggressive in tone |
| 🚀 | Start-up cliché; does not fit this brand's register |
| [Add client-specific entries] | |

### 4.4 When Not to Use Emojis

Emojis are never used in:
- Crisis statements or holding statements (any level)
- Formal announcements (regulatory, legal, compliance)
- Condolence or sympathy posts
- Any post referencing national tragedies or disasters (see Section 8)
- LinkedIn posts on sensitive professional topics

---

## SECTION 5: IMAGE AND VIDEO STANDARDS

### 5.1 Aspect Ratios by Platform

| Platform | Format | Recommended ratio | Notes |
|---|---|---|---|
| Facebook Feed | Image / Video | 1:1 or 4:5 | 4:5 maximises screen space on mobile |
| Facebook Stories | Image / Video | 9:16 | Full screen; leave 14% top and bottom safe zone |
| Instagram Feed | Image / Video | 1:1 or 4:5 | 4:5 preferred |
| Instagram Stories | Image / Video | 9:16 | Same safe zone as Facebook Stories |
| Instagram Reels | Video | 9:16 | |
| TikTok | Video | 9:16 | |
| LinkedIn | Image | 1200 × 627px (1.91:1) | Landscape preferred for link posts |
| WhatsApp | Image | 1:1 or 4:5 | Avoid cropping faces |
| X / Twitter | Image | 16:9 or 1:1 | |
| YouTube Thumbnail | Image | 16:9 | 1280 × 720px minimum |

### 5.2 Watermark and Branding Policy

State the watermark rule clearly:
- **All original content:** [Logo placement — e.g. bottom-right corner, 10% of frame width, 70% opacity]
- **User-generated content shared with permission:** [e.g. Add logo watermark before reposting]
- **Stories and Reels:** [Logo in corner / No watermark — platform adds brand tag automatically]
- **Video intro/outro:** [Duration — e.g. 2-second branded end card on all videos over 60 seconds]

### 5.3 Colour Palette

| Colour role | Hex code or description | When to use |
|---|---|---|
| Primary | [Code] | Dominant colour in all graphics |
| Secondary | [Code] | Accents and contrast |
| Accent | [Code] | Calls to action; use sparingly |
| Background | [Code] | Default graphic background |
| Text on dark | [Code] | Overlays on dark images |
| Text on light | [Code] | Overlays on light images |

Colours to avoid: [List any colours associated with competitors or that clash with the palette.]

### 5.4 Photo Style

- **Subject matter:** [People / Products / Environments / Combination]
- **People in images:** [Real staff and customers preferred / Models permitted / Stock images: see policy below]
- **Setting:** [Indoor / Outdoor / Both — specify which settings work for this brand]
- **Mood:** [Warm / Neutral / Bold / Energetic] — [One sentence on what this looks like in practice]
- **Production level:** [Highly produced / Balanced / Raw and authentic] — justify with reference to the persona
- **Stock photography policy:** [Permitted only when no original image is available / Avoid entirely / Permitted for LinkedIn only] — if permitted, rule: images must reflect the East African demographic of the audience

### 5.5 Approved Filters and Presets

- **Approved presets:** [List preset names if the client uses Lightroom, VSCO, or a custom filter — e.g. "Warm Natural", "Client Preset A"]
- **Filters to avoid:** [e.g. Heavy black-and-white, oversaturated filters, beauty smoothing filters on product shots]

### 5.6 Video Length Standards

| Platform | Recommended length | Maximum |
|---|---|---|
| Facebook Feed | 60–90 seconds | 3 minutes |
| Instagram Reels | 15–30 seconds | 90 seconds |
| TikTok | 15–60 seconds | 3 minutes |
| LinkedIn | 30–90 seconds | 10 minutes |
| YouTube | 5–15 minutes | No limit |
| WhatsApp Status | 15–30 seconds | 30 seconds |

Longer formats require client approval before production.

---

## SECTION 6: HASHTAG USAGE RULES

### 6.1 Branded Hashtags

List 1–3 branded hashtags unique to this client. For each:

**#[Hashtag]**
- **Purpose:** [All organic content / Campaign-specific / Community and UGC]
- **Platforms:** [Where to use it]
- **Usage rule:** [Every post / Campaigns only / Specific content types]
- **Growing adoption:** [One-line instruction — e.g. "Ask followers to use this hashtag when sharing their experience"]

Advise the client to search each hashtag on Instagram and TikTok before first use to confirm it is not in widespread use by another brand.

### 6.2 Campaign Hashtags

State the protocol:
- Campaign hashtags are created fresh for each campaign and retired afterwards
- Campaign hashtags must be approved by [approver name/role] before use
- Format: [e.g. #[ClientName][CampaignYear] or #[CampaignTheme][Location]]

### 6.3 Community and Discovery Hashtags

Provide a set of supplementary hashtags for reach. These are not branded — they rotate:

- **Industry hashtags:** [3–5 relevant to the client's sector — e.g. #UgandaFinance #EastAfricaBusiness]
- **Location hashtags:** [3–5 — e.g. #Kampala #Uganda #EastAfrica #KampalaBusinesses]
- **Review frequency:** The content team reviews and refreshes community hashtags monthly

Branded hashtags are permanent. Community hashtags are refreshed monthly. Campaign hashtags are retired at campaign end.

### 6.4 Maximum Hashtag Count by Platform

| Platform | Recommended | Maximum | Notes |
|---|---|---|---|
| Instagram | 5–10 | 30 | Place at end of caption or in first comment |
| Facebook | 2–3 | 5 | Fewer hashtags perform better on Facebook |
| LinkedIn | 3–5 | 5 | Industry and professional topic hashtags only |
| TikTok | 3–5 | 8 | Include at least one trending hashtag where relevant |
| X / Twitter | 1–2 | 2 | Embedded in sentence where possible |
| WhatsApp | 0 | 0 | No hashtags in WhatsApp messages |

### 6.5 Hashtag Research Process

Before adding a new hashtag to the rotation:
1. Search the hashtag on Instagram and TikTok — check post volume and recent content type
2. Confirm recent posts are brand-safe and do not share the hashtag with unrelated or harmful content
3. Check that the hashtag is active — minimum 1,000 posts on Instagram
4. Add approved hashtags to the master hashtag list [stored in: specify location — e.g. Google Drive / Notion]
5. Review and retire underperforming hashtags monthly

---

## SECTION 7: CONTENT APPROVAL WORKFLOW

### 7.1 Roles

| Role | Name | Responsibility |
|---|---|---|
| Content Drafter | [Name] | Writes and designs all content; creates the draft for review |
| Content Reviewer | [Name or "not applicable"] | Reviews for brand voice, accuracy, and grammar before approval |
| Content Approver | [Name] | Final sign-off before any post is scheduled or published |

### 7.2 Standard Approval Process

1. **Drafter** creates content and submits to Reviewer (or Approver if no separate reviewer) via [channel — e.g. WhatsApp, Google Drive, Trello]
2. **Reviewer** checks against this style guide and returns feedback or approves within [X hours]
3. **Approver** gives final sign-off within [X hours of receiving the reviewed draft]
4. **Drafter** schedules the post on confirmation of approval — not before
5. **Turnaround deadline:** All content must be submitted for approval at least [X hours/days] before the intended publish time

### 7.3 Urgent Content

For time-sensitive posts (breaking news response, event announcements, same-day promotions):
- Drafter alerts Approver by WhatsApp immediately with the draft
- Approver has [X hours] to respond — if no response, content is held, not published
- Verbal approval is not sufficient — approval must be confirmed in writing (WhatsApp message or email)

### 7.4 What Requires Additional Approval

The following content types require explicit approval from [Approver name/role] before drafting begins — not just before publishing:

- Posts referencing competitor products or services
- Posts making any claim involving prices, statistics, or performance figures
- Posts featuring a named individual (other than own staff in approved formats)
- Any content related to a current news event or sensitive national topic
- Collaboration or partnership announcements

---

## SECTION 8: BREAKING-NEWS CONTENT PAUSE PROTOCOL

When a significant national or regional event occurs — a national tragedy, a major disaster, a public figure's death, civil unrest, or any event that dominates national conversation — all scheduled content must be paused immediately.

### 8.1 Triggers for a Content Pause

Pause all scheduled and planned content when:
- A national mourning period is declared by the Government of Uganda (or the relevant national government)
- A major disaster, attack, or tragedy is reported by two or more credible national news outlets
- A public figure's death is announced and is dominating social media conversation
- A significant political or civil event makes any commercial content appear tone-deaf

### 8.2 Pause Procedure

1. [Content Drafter / Social Media Manager] identifies the trigger event
2. Pause all scheduled posts immediately in [scheduling tool — e.g. Buffer, Hootsuite, Meta Business Suite]
3. WhatsApp [Approver name] within 30 minutes: "Content pause triggered. [One-sentence summary of event]. Awaiting your direction."
4. Do not post anything — including condolences — without approver sign-off
5. Do not resume normal content until the approver gives explicit instruction

### 8.3 During the Pause

- Monitor the situation closely — check credible news sources every two hours
- If the brand wishes to post a condolence or acknowledgement, draft it and submit for approval before posting
- Condolence posts: plain text, no emojis, no branded hashtags, no calls to action
- Do not use a tragedy as a content opportunity

### 8.4 Resuming Content

Resume normal content only when:
- The immediate crisis or mourning period has passed
- The approver gives explicit written approval to resume
- The first post back is neutral or informational — not promotional

---

## SECTION 9: LANGUAGE AND GRAMMAR RULES

Apply these rules consistently across all platforms and all content types.

### 9.1 English Standard

- **Primary standard:** British English — organisation, colour, programme, behaviour, analyse, recognise, centre, enquiry, favour, licence (noun), license (verb)
- **Local register:** Incorporate East African professional English where appropriate — follow the `east-african-english` skill for guidance
- **Spell-checker setting:** Set to English (United Kingdom) — not English (United States)

### 9.2 Number Formatting

| Type | Format | Example |
|---|---|---|
| Numbers 1–9 | Spell out | "three locations", "seven days" |
| Numbers 10 and above | Numerals | "15 products", "100 customers" |
| Large numbers | Numeral + word | "1.2 million", "50,000 customers" |
| Percentages | Numeral + % (no space) | "25%" not "25 percent" in social copy |
| Telephone numbers | Local format | +256 700 000 000 |

### 9.3 Currency Formatting

- **Primary currency:** UGX (Uganda Shillings) — format as UGX 50,000 (not USh, not UGX50,000 without space)
- **Comma as thousands separator:** UGX 1,500,000
- **Avoid abbreviations** unless space is a hard constraint (e.g. story text) — in that case: 1.5M
- **USD references:** Use USD [amount] — only where the product or service is priced in dollars

### 9.4 Date and Time Formatting

- **Date format:** DD/MM/YYYY — e.g. 19/03/2026 (never MM/DD/YYYY)
- **Written dates in copy:** 19 March 2026 (no ordinal suffix — not "19th March")
- **Time:** 12-hour clock with am/pm — e.g. 10:00am, 2:30pm (no space before am/pm)
- **Day ranges:** Monday–Friday (en dash, not hyphen)

### 9.5 Capitalisation Rules

- **Brand name:** Always as specified in Section 3.3 — check every post
- **Post copy:** Sentence case only — not Title Case For Every Word
- **Platform names:** Facebook, Instagram, LinkedIn, TikTok, WhatsApp, X (formerly Twitter), YouTube — capitalise exactly as shown
- **Job titles:** Capitalise only when preceding a name — "Managing Director Jane Akello" but "the managing director"
- **Acronyms:** Use on first instance only after spelling out in full — e.g. "small and medium enterprises (SMEs)"

### 9.6 Punctuation Standards

- **Apostrophes:** Contractions are acceptable on Facebook, Instagram, TikTok, and WhatsApp. Avoid on LinkedIn.
- **Exclamation marks:** Maximum one per post. Never two consecutive. Not used in formal announcements or LinkedIn.
- **Oxford comma:** Use in all lists of three or more items — "strategy, content, and reporting"
- **Ellipsis:** Use sparingly and only for genuine suspense or continuation — not as a trailing sentence ender in formal posts
- **Em dash (—):** Use for parenthetical asides and emphasis — not a hyphen

---

## Quality Criteria

Output meets production standard when it satisfies all of the following:

- The brand voice section produces "we are X, not Y" pairings that are specific and actionable — a new team member can use them to make a real writing decision, not just understand an abstract principle
- The platform tone guide shows a genuine, audible tonal shift between platforms using the same client's product or service — the worked examples are not the same sentence with different punctuation
- The vocabulary tables contain a minimum of three terms specific to this client's industry; generic EA professional vocabulary does not fill the list
- The emoji policy is specific enough to act on without further discussion — entries such as "use occasionally" or "as appropriate" are not acceptable
- The image and video standards section contains the client's actual colour codes and approved terminology — it is not a template with placeholders
- The approval workflow names specific roles and states specific turnaround times in hours — it does not use vague language such as "promptly" or "in due course"
- The breaking-news pause protocol names the specific approver and communication channel — it does not use generic role descriptions
- The language and grammar section applies the correct UGX formatting, DD/MM/YYYY dates, and British English throughout — inconsistency between sections is a failure
