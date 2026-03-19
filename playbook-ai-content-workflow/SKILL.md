---
name: playbook-ai-content-workflow
description: Generates a step-by-step operational guide for integrating AI tools into a client's social media content production process — covering tool selection, brand voice training, a ready-to-use prompt library, quality control, and a clear list of what AI must never be used for. Invoke this skill when a client is already using AI tools without a structured process, when onboarding a new client who wants to scale content production, or when a consultant needs to document and hand over an AI-assisted content workflow to an in-house team. This skill does not replace the brand voice guide (04-brand-voice-intake) or the content calendar (11-content-calendar) — it plugs them into an AI-assisted production system.
---

# AI Content Workflow Playbook

## Required Input

Collect the following before generating the playbook:

- **Client name** and industry
- **Brand voice** — 3 tone words from 04-brand-voice-intake (e.g. warm, authoritative, direct)
- **Vocabulary avoid list** — words and phrases the client must never use (from 04-brand-voice-intake)
- **Content pillars** — pillar names from 10-content-pillars
- **Platforms in scope** — list only the platforms this client actively uses
- **Team size** — solo (owner-operated), small team (2–5), or large team (6+)
- **Country/city** — defaults to Uganda/East Africa if not specified

---

## 1. AI Tool Overview (EA-Accessible)

Start with two tools only: ChatGPT and Canva. Add others once the workflow is established. Recommending ten tools at once guarantees none of them get used consistently.

| Tool | What It Does | EA Access |
|---|---|---|
| **ChatGPT** (OpenAI) | Text generation, ideation, caption drafting, copywriting | Free tier via browser; no app required |
| **Claude** (Anthropic) | Text generation, longer-form drafting, analysis | Free tier via browser |
| **Canva Magic Write / Magic Design** | AI-generated social graphics with copy suggestions | Free tier; used directly in Canva |
| **Grammarly** | Grammar check, tone review, British English correction | Free browser extension and web app |
| **CapCut AI Captions** | Automatic captions for videos; available on mobile | Free; works on Android and iOS |
| **Google Gemini** | Research assistance, ideation, summarisation | Free via Google account |
| **Magai / Poe** | Multi-model AI access in one interface | Paid; for advanced users only |

**Starting recommendation:** Use ChatGPT for all text work and Canva for all graphic work. Both have free tiers, both work on a basic smartphone or laptop, and both are already familiar to most EA users. Introduce Grammarly in week two as a mandatory quality step. Defer all other tools until the core workflow is running smoothly.

---

## 2. Brand Voice Training in AI

AI tools produce generic content by default. The only way to get on-brand output is to give the tool the brand context before every session. Do not start a new ChatGPT conversation without this block in place.

### The Brand Context Block

This is a reusable prompt prefix. Paste it at the start of every new AI session. Complete every bracketed field before use.

```
You are writing social media content for [Brand Name], a [industry] business
based in [city], Uganda. Our brand voice is [tone word 1], [tone word 2], and
[tone word 3]. We speak to [persona description — e.g. "urban women aged 25–40
who value quality and convenience"]. We always use British English spelling —
never American spellings. We never use the following words or phrases:
[vocabulary avoid list]. Our content pillars are: [pillar 1], [pillar 2],
[pillar 3]. Do not use these words under any circumstances: delve, tapestry,
leverage, game-changer, groundbreaking, revolutionary, navigate, foster, realm,
unleash, unlock, elevate.
```

### How to Save and Reuse the Brand Context Block

**ChatGPT Custom Instructions (recommended):** Go to your profile → Custom Instructions → paste the completed Brand Context Block into the "What would you like ChatGPT to know about you?" field. This loads automatically into every new conversation.

**Session-start paste method:** Keep the completed Brand Context Block in a shared Google Doc or WhatsApp Saved Messages. Paste it as the very first message in any new AI session before asking for content.

**Team use:** If more than one person is generating content for the same client, share the completed Brand Context Block in the team WhatsApp group. Everyone uses the same block. A team using different context blocks will produce inconsistent content.

### Refining the Brand Context Block Over Time

After four weeks of use, review the AI outputs against the brand voice. If a pattern of off-brand outputs persists, adjust the block:

- If the AI consistently sounds too formal: add "We speak in a conversational, friendly tone — not corporate or stiff."
- If the AI ignores banned vocabulary: move the banned list higher in the block and bold it.
- If the AI defaults to American English despite the instruction: add "Spell-check: colour, organisation, behaviour, recognise, centre, programme, analyse."

Update the shared Brand Context Block document every time you make a change. Date each version.

---

## 3. Prompt Library — Core Templates

Every prompt below follows this structure: **[CONTEXT BLOCK]** + specific instruction + output format instruction. Replace [CONTEXT BLOCK] with the completed brand context before running.

All prompts specify British English output. Do not remove this instruction.

### Captions

**Prompt 1 — Short caption (under 100 characters, for Instagram / WhatsApp)**
> [CONTEXT BLOCK] Write a short social media caption of under 100 characters for [platform]. The post is about [topic or product]. Include one relevant emoji. Do not include hashtags. Output: one caption only.

**Prompt 2 — Medium caption (100–200 characters, for Facebook / LinkedIn)**
> [CONTEXT BLOCK] Write a social media caption of 100–200 characters for [platform]. The post is about [topic or product]. The caption should open with a strong first line that stops the scroll. Include a call to action at the end. Do not include hashtags. Output: two caption options for me to choose between.

**Prompt 3 — Thread or carousel caption (5–7 slides or tweets)**
> [CONTEXT BLOCK] Write a [5-slide carousel / 6-tweet thread] about [topic]. Each slide/tweet should be one clear point. Open with a hook that creates curiosity. Close with a call to action linking to [desired action — e.g. "WhatsApp us" or "link in bio"]. Output: numbered slides or tweets, one line each, in British English.

### Content Ideas

**Prompt 4 — 30 content ideas from pillars**
> [CONTEXT BLOCK] Generate 30 social media content ideas for the month of [month]. Distribute them evenly across these pillars: [pillar 1], [pillar 2], [pillar 3]. Include a mix of educational, entertaining, and promotional content. For each idea, provide: the content type (post, Reel, Story, carousel), the pillar it belongs to, and a one-sentence description. Output: a numbered table.

**Prompt 5 — Seasonal or campaign content ideas**
> [CONTEXT BLOCK] Generate 10 social media content ideas for [upcoming occasion — e.g. Eid, end of financial year, back to school]. Ideas should be relevant to [industry] and the Ugandan/East African context. For each idea, provide: platform, format, and a one-sentence description. Output: numbered list.

### Hashtag Research

**Prompt 6 — Hashtag set for a specific post**
> [CONTEXT BLOCK] Suggest 15 relevant hashtags for a [platform] post about [topic]. Include a mix of: 3 broad hashtags (over 1 million uses), 6 mid-range hashtags (100k–1 million uses), and 6 niche hashtags (under 100k uses). Include at least 2 Uganda or East Africa specific hashtags where relevant. Output: three groups, labelled Broad, Mid-range, and Niche.

**Prompt 7 — Evergreen hashtag bank for the account**
> [CONTEXT BLOCK] Create an evergreen hashtag bank of 30 hashtags for a [industry] business on [platform]. Group them into sets of 10 by content type: educational content, promotional content, and community content. Output: three labelled groups of 10 hashtags each.

### Email Subject Lines

**Prompt 8 — Subject line options for a campaign email**
> [CONTEXT BLOCK] Write 10 email subject line options for an email about [email topic or offer]. Subject lines should be under 50 characters, written in British English, and match the brand voice. Include a mix of: curiosity-driven, benefit-led, and urgency-based approaches. Output: 10 numbered subject lines with the approach type labelled next to each.

**Prompt 9 — Newsletter subject lines (recurring)**
> [CONTEXT BLOCK] Write 5 subject line options for [Client Name]'s monthly newsletter for [month]. The main content of this newsletter is: [describe 2–3 key topics]. Subject lines should be conversational and feel personal. Under 50 characters each. Output: 5 numbered options.

### Blog Post Outlines

**Prompt 10 — Full blog post outline**
> [CONTEXT BLOCK] Write a structured outline for a blog post titled "[working title]". The target reader is [persona]. The post should rank for the keyword "[primary keyword]". Include: an introduction paragraph summary, 4–6 H2 section headings with 2–3 bullet points under each, and a conclusion with a call to action. Output: structured outline in British English.

**Prompt 11 — Blog post from an existing piece of content**
> [CONTEXT BLOCK] I have the following content: [paste source material — could be a speech, WhatsApp message, recorded transcript]. Turn this into a blog post outline with an introduction, 3–5 sections, and a conclusion. Keep the original voice. Do not add claims or statistics I have not provided. Output: structured outline in British English.

### Community Management Responses

**Prompt 12 — Response to a positive review or comment**
> [CONTEXT BLOCK] Write 3 response options for the following positive comment on [platform]: "[paste comment]". Each response should feel personal and genuine — not a copy-paste template. Include the commenter's name if provided. Match the brand voice. Under 60 words each. Output: 3 numbered options.

**Prompt 13 — Response to a complaint or negative review**
> [CONTEXT BLOCK] Write a response to the following complaint on [platform]: "[paste complaint]". The response should: acknowledge the issue, apologise without admitting legal liability, offer to resolve the matter privately via WhatsApp or DM, and be under 80 words. Do not be defensive. Match the brand voice. Output: one response.

### Repurposing

**Prompt 14 — Long content to short social post**
> [CONTEXT BLOCK] I have the following long-form content: [paste blog post, article, or transcript]. Extract the 3 most valuable insights and write a separate social media caption for each one, suitable for [platform]. Each caption: 100–150 words, ends with a call to action, and is in British English. Output: 3 numbered captions.

**Prompt 15 — Video script or transcript to caption**
> [CONTEXT BLOCK] I have the following video transcript: [paste transcript]. Write a social media caption to accompany this video on [platform]. The caption should summarise the main point in the first line, expand in 2–3 sentences, and close with a call to action. Under 150 words. British English. Output: one caption.

---

## 4. Quality Control Protocol

Every AI-generated output must pass all five checks before it is published. Run the checks in order. Do not skip steps under time pressure — AI errors in published content damage the brand and the consultant's credibility.

- [ ] **Brand voice check:** Read the output aloud. Does it match the 3 tone words? If it sounds generic, stiff, or unlike the client, rewrite or re-prompt before proceeding.
- [ ] **British English check:** Paste into Grammarly. Fix any American spellings (color → colour, organization → organisation, analyze → analyse, program → programme, center → centre, recognize → recognise). Reject "apologize" — it should be "apologise".
- [ ] **Banned vocabulary check:** Scan the output against the client's vocabulary avoid list AND this universal AI vocabulary blacklist: *delve, tapestry, leverage, game-changer, groundbreaking, revolutionary, navigate, foster, realm, unleash, unlock, elevate, thriving, vibrant, seamless, robust, empower.* If any appear, delete and rewrite — do not just find-and-replace.
- [ ] **Accuracy check:** Highlight every factual claim about the client's products, services, prices, or history. Verify each one directly with the client or source document before publishing. AI fabricates plausible-sounding facts. Do not assume any specific claim is correct.
- [ ] **Human touch check:** Add one element that AI could not have generated — a specific detail about the client's premises, a local reference (a Kampala neighbourhood, an EA seasonal moment, a current local context), a genuine customer name (with permission), or the owner's voice. Every published output must contain at least one human edit. This is not optional.

---

## 5. Workflow Integration

### Weekly AI-Assisted Content Workflow (5 posts per week, Instagram)

AI does not replace the weekly content process — it compresses the time required for each step.

**Monday — AI Drafting (10 minutes)**
Open ChatGPT. Paste the Brand Context Block. Run Prompt 4 (content ideas) to confirm the week's topics if not already planned. Run Prompt 1 or 2 five times, once per post. Save all five drafts in a shared Google Doc or Notion page labelled "[Client] — Week of [date] — AI drafts."

**Monday — Human Review and Edit (30 minutes)**
Open the five drafts. Run the Quality Control Protocol on each one. Add the human touch element to each caption. Mark the status of each draft: Approved / Needs Revision / Reject. For any rejected draft, either re-prompt or write the caption manually — do not publish a draft that failed a quality check.

**Monday — Scheduling (20 minutes)**
Load approved captions into Buffer or Hootsuite. Assign dates and times. Attach images. Set all posts to schedule (not auto-publish) so the client can review before anything goes live.

**Total time with AI: 60 minutes per week**

### Time Saving Calculation — 5-Post Instagram Account

| Task | Without AI | With AI |
|---|---|---|
| Researching and writing 5 captions | 75 minutes | 10 minutes (AI draft) + 30 minutes (edit) |
| Hashtag selection per post | 15 minutes | 5 minutes |
| Scheduling in Buffer/Hootsuite | 20 minutes | 20 minutes (unchanged) |
| **Total per week** | **110 minutes** | **65 minutes** |
| **Total per month (4 weeks)** | **7.3 hours** | **4.3 hours** |
| **Monthly saving** | — | **3 hours per client** |

For a consultant managing five clients, AI-assisted workflows free up to 15 hours per month — time that goes back into strategy, client relationships, and business development.

---

## 6. What NOT to Use AI For

These prohibitions are not suggestions. Each one exists because real harm — to the client, the audience, or the consultancy — is the predictable outcome of ignoring it.

- **Do not use AI to generate client testimonials or reviews.** Fabricated social proof is dishonest and illegal in many jurisdictions. If a client needs testimonials, collect real ones.
- **Do not publish AI-generated content without a human read.** AI hallucinates. It invents product details, fabricates prices, misrepresents services, and produces plausible errors. An unread AI post is a liability, not a time-saving.
- **Do not use AI for crisis communications responses.** A brand apology, a response to a serious complaint, or any statement during a reputational incident requires human judgement, empathy, and accountability. See playbook-crisis-communications for the correct protocol.
- **Do not allow AI to state specific statistics or data without verifying each figure.** AI generates statistics that sound credible and are frequently wrong. Any number in a published post must trace back to a verifiable source.
- **Do not let AI generate the brand voice guide.** AI describes brands in generic marketing language ("innovative", "customer-focused", "passionate"). The brand voice comes from the client discovery session in 04-brand-voice-intake — real conversations, real examples, real dislikes. AI cannot do this work.
- **Do not use AI-generated images as photographic evidence of real products, services, or events.** AI image tools produce convincing fictions. Using them as if they depict the client's real premises or products misleads consumers.

---

## 7. AI Disclosure Policy

Apply this guidance to every client account. When in doubt, disclose — audiences in the EA market are becoming more sophisticated about AI use, and proactive transparency builds rather than erodes trust.

**Disclose — required:**
Use a clear label ("AI-generated image" or "Created with AI") when AI-generated images are used in advertising, editorial features, or any context where the audience might assume the image depicts a real person, place, or event.

**Disclose — best practice:**
If a post is substantially AI-generated (drafted and published with only minor edits), a light disclosure such as "Created with AI assistance" builds long-term audience trust. Use it selectively on posts where the AI role was significant.

**No disclosure required:**
Using AI as a drafting tool that is then substantially edited, rewritten, and personalised by a human is industry-standard practice and does not require disclosure — the same way a consultant using a spell-checker or Grammarly does not disclose it.

For the formal client AI content policy document covering legal considerations and disclosure obligations, invoke **policy-ai-content-ethics**.

---

## 8. Platform-Specific AI Tips

Apply these notes when generating content for each platform. Generic AI outputs underperform on every platform — these adjustments close the gap.

**LinkedIn**
B2B audiences on LinkedIn — especially professionals in Kampala, Nairobi, and Lagos — are increasingly skilled at recognising AI-generated posts. The tell: perfectly structured paragraphs, no personal specificity, and generic professional language. Always add a personal observation, a specific client experience, or a genuine professional opinion. If the post reads like a thought leadership template, re-prompt or rewrite.

**TikTok**
AI-written scripts sound scripted on camera — and TikTok audiences will skip within two seconds. Use AI for the opening hook only (the first line or first visual idea). Film the rest naturally and conversationally. CapCut AI captions are the single most useful AI application for TikTok — use them on every video.

**WhatsApp**
Broadcast message recipients know when they are reading a template. AI-written WhatsApp messages have a generic warmth that is immediately recognisable. Use AI to draft the structure, then rewrite in the client's natural voice — the way they actually message a trusted customer. Heavy personalisation (name, recent purchase, specific context) is mandatory. Never send a broadcast without at least one personal element per recipient segment.

**Instagram**
Feed captions are well-suited to AI drafting — quality control and a human edit produce good results. Stories and Reels voice-overs must be authentic. If the client is speaking on camera, they should speak naturally from bullet points, not read an AI script. Use AI to generate caption options for Reels after filming — not to script what the creator says.

**Email**
Subject lines are the highest-value AI application in email marketing — run Prompt 8 or 9 and test multiple options. Email body copy benefits from an AI draft that is then substantially edited: check every claim, rewrite the opening paragraph in the client's real voice, and ensure the call to action matches the actual offer.

---

## Quality Criteria

Output meets production standard when it satisfies all of the following:

- The Brand Context Block template is complete with all fields identified and can be filled in and used for any client without modification to the structure
- All 15 prompt templates produce usable, on-brand outputs when run as written — test at least 3 before handing over to a client
- The Quality Control Protocol is specific enough to catch real AI errors (fabricated statistics, American spellings, banned vocabulary, missing human edit) — not just general advice to "review the content"
- British English is enforced throughout, including inside every prompt template (each prompt specifies "British English" explicitly)
- The workflow section states specific time estimates for each step and includes a time-saving calculation with actual figures, not vague efficiency claims
- The "What NOT to Use AI For" list covers the specific risks most likely to affect EA SME clients — fabrication, hallucination, crisis misuse, and false statistics — with a reason given for each prohibition
- No paid tools are required to implement the core workflow — ChatGPT free tier, Canva free tier, and Grammarly free tier are sufficient
- Platform-specific notes are specific enough to act on immediately, not generic recommendations
