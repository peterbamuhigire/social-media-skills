---
name: playbook-ai-content-workflow
description: Generates a step-by-step operational guide for integrating AI tools into a client's social media content production process — covering tool selection, brand voice calibration, a core prompt library (with reference to the full prompt-engineering-library), quality control, content maturity staging, and a clear list of what AI must never be used for. Draws on frameworks from Upadhyay (2024) and Schaefer (2025). Invoke this skill when a client is already using AI tools without a structured process, when onboarding a new client who wants to scale content production, or when a consultant needs to document and hand over an AI-assisted content workflow to an in-house team. This skill does not replace the brand voice guide (04-brand-voice-intake) or the content calendar (11-content-calendar) — it plugs them into an AI-assisted production system.
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

## 2. Brand Voice Calibration (Step 0)

Complete this step before any AI content is generated. It is not optional — skipping it produces generic output that sounds like every other brand in the client's industry.

### Step 0 — Formal Brand Voice Capture

Before building the Brand Context Block, run `brand-voice-ai-training`. That skill executes the full 6-step process: extracting tone words from real client language, building the vocabulary avoid list, generating reference examples, and producing an AI-ready voice profile. The Brand Context Block below draws directly from that output.

### The Brand Context Block

This is a reusable prompt prefix. Paste it at the start of every new AI session. Complete every bracketed field before use. Fields are populated from the `brand-voice-ai-training` output and 04-brand-voice-intake.

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

### Saving and Reusing the Brand Context Block

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

### Prompt Structure: Alpha-Beta-Gamma-Delta-Epsilon

Every effective AI prompt contains five elements (Upadhyay, 2024):

| Element | What It Does | Example |
|---|---|---|
| **Alpha — Role** | Assigns expertise to the AI | "You are writing for a Kampala-based SME…" |
| **Beta — Context** | Provides background and brand parameters | The Brand Context Block |
| **Gamma — Task** | States the specific output required | "Write a 150-word Instagram caption about…" |
| **Delta — Constraints** | Sets limits (length, tone, language, exclusions) | "Under 100 characters. British English. No hashtags." |
| **Epsilon — Output format** | Specifies how the result should be presented | "Output: 3 numbered options." |

The Brand Context Block covers Alpha and Beta. Every prompt below adds Gamma, Delta, and Epsilon. Do not remove any element.

**Copywriting frameworks available:** The core prompts below use PAS (Problem–Agitate–Solution) and AIDA (Attention–Interest–Desire–Action) by default. For the full library of 7 frameworks — PAS, AIDA, BAB, FAB, SSS, PPPP, and AFOREST — plus 7 additional ready-to-use templates, invoke `prompt-engineering-library`.

All prompts specify British English output. Do not remove this instruction.

---

### Captions

**Prompt 1 — Short caption (under 100 characters, Instagram / WhatsApp)**
> [CONTEXT BLOCK] Write a short social media caption of under 100 characters for [platform]. The post is about [topic or product]. Include one relevant emoji. Do not include hashtags. Output: one caption only. British English.

**Prompt 2 — Medium caption (100–200 characters, Facebook / LinkedIn)**
> [CONTEXT BLOCK] Write a social media caption of 100–200 characters for [platform]. The post is about [topic or product]. Open with a strong first line that stops the scroll. Include a call to action at the end. Do not include hashtags. Output: two caption options to choose between. British English.

**Prompt 3 — Carousel or thread (5–7 slides / tweets)**
> [CONTEXT BLOCK] Write a [5-slide carousel / 6-tweet thread] about [topic]. Each slide/tweet should make one clear point. Open with a hook that creates curiosity. Close with a call to action linking to [desired action]. Output: numbered slides or tweets, one line each. British English.

---

### Content Ideas

**Prompt 4 — Monthly content ideas from pillars**
> [CONTEXT BLOCK] Generate 30 social media content ideas for [month]. Distribute evenly across these pillars: [pillar 1], [pillar 2], [pillar 3]. Include a mix of educational, entertaining, and promotional content. For each idea: content type (post, Reel, Story, carousel), pillar, and a one-sentence description. Output: numbered table. British English.

**Prompt 5 — Seasonal or campaign content ideas**
> [CONTEXT BLOCK] Generate 10 social media content ideas for [occasion — e.g. Eid, end of financial year, back to school]. Relevant to [industry] and the Ugandan/East African context. For each idea: platform, format, one-sentence description. Output: numbered list. British English.

---

### Hashtags

**Prompt 6 — Hashtag set for a specific post**
> [CONTEXT BLOCK] Suggest 15 relevant hashtags for a [platform] post about [topic]. Include: 3 broad hashtags (over 1 million uses), 6 mid-range (100k–1 million uses), 6 niche (under 100k uses). Include at least 2 Uganda or East Africa specific hashtags. Output: three labelled groups. British English.

---

### Repurposing and Community Management

**Prompt 7 — Long content to short social post**
> [CONTEXT BLOCK] I have the following long-form content: [paste blog post, article, or transcript]. Extract the 3 most valuable insights and write a separate caption for each, suitable for [platform]. Each caption: 100–150 words, ends with a call to action. Output: 3 numbered captions. British English.

**Prompt 8 — Response to a complaint or negative review**
> [CONTEXT BLOCK] Write a response to the following complaint on [platform]: "[paste complaint]". Acknowledge the issue, apologise without admitting legal liability, offer to resolve privately via WhatsApp or DM, under 80 words. Do not be defensive. Output: one response. British English.

---

For email subject lines, blog post outlines, positive review responses, video transcript captions, and the full 15-template set, invoke `prompt-engineering-library`.

---

## 4. Quality Control Protocol

Every AI-generated output must pass all six checks before it is published. Run the checks in order. Do not skip steps under time pressure.

- [ ] **Brand voice check:** Read the output aloud. Does it match the 3 tone words? If it sounds generic, stiff, or unlike the client, rewrite or re-prompt before proceeding.
- [ ] **British English check:** Paste into Grammarly. Fix any American spellings (color → colour, organization → organisation, analyze → analyse, program → programme, center → centre, recognize → recognise). Reject "apologize" — it should be "apologise".
- [ ] **Banned vocabulary check:** Scan against the client's vocabulary avoid list AND the universal AI blacklist: *delve, tapestry, leverage, game-changer, groundbreaking, revolutionary, navigate, foster, realm, unleash, unlock, elevate, thriving, vibrant, seamless, robust, empower.* Delete and rewrite — do not just find-and-replace.
- [ ] **Accuracy check:** Highlight every factual claim about the client's products, services, prices, or history. Verify each one directly with the client or source document before publishing. AI fabricates plausible-sounding facts. Do not assume any specific claim is correct.
- [ ] **Human touch check:** Add one element that AI could not have generated — a specific detail about the client's premises, a local reference (a Kampala neighbourhood, an EA seasonal moment, a current local context), a genuine customer name (with permission), or the owner's voice. Every published output must contain at least one human edit. This is not optional.
- [ ] **Cultural localisation check:** Does the content reference at least one Uganda/EA-specific element? Generic "African" content is not sufficient. Name the specific country, city, market, or moment. If not present, add one before publishing.

### Proof of Human (High-Stakes Content)

For thought leadership posts, strategy documents, personal brand content, or any post where audience trust is the currency: signal that a human wrote or heavily shaped this content. Do not just assert it — show it (Schaefer, 2025). Methods:

- Share the process: post a draft with visible edits, a voice note explaining your thinking, or a behind-the-scenes note
- Name the author and include a personal observation specific to their experience
- Reference a real, verifiable event, conversation, or local context that AI could not have known

Apply this standard whenever the content is making a claim to authority, expertise, or personal experience.

For AI humanisation of draft content before publishing, invoke `ai-content-humaniser`.

---

## 5. Workflow Integration

### Weekly AI-Assisted Content Workflow (5 posts per week, Instagram)

AI does not replace the weekly content process — it compresses the time required for each step.

**Monday — AI Drafting (10 minutes)**
Open ChatGPT. Paste the Brand Context Block. Run Prompt 4 to confirm the week's topics if not already planned. Run Prompt 1 or 2 five times, once per post. Save all five drafts in a shared Google Doc or Notion page labelled "[Client] — Week of [date] — AI drafts."

**Monday — Human Review and Edit (30 minutes)**
Open the five drafts. Run the Quality Control Protocol on each one. Add the human touch element to each caption. Mark the status: Approved / Needs Revision / Reject. For any rejected draft, re-prompt or write the caption manually — do not publish a draft that failed a quality check.

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

For advanced automation (scheduling triggers, auto-repurposing pipelines, multi-platform distribution), invoke `playbook-ai-automation-workflow`.

---

## 6. Content Maturity Model

Assess where the client currently sits before prescribing tools or workflows. Introducing automation to a client at Stage 1 creates chaos, not efficiency (Upadhyay, 2024).

| Stage | Description | AI Use at This Stage |
|---|---|---|
| **1 — Basic** | Posting inconsistently; no strategy; content reactive | Use AI for ideation and caption drafting only. Establish posting rhythm first. |
| **2 — Aligned** | Regular posting; brand voice defined; pillars in use | Use AI for full caption workflow, hashtag research, and repurposing. This playbook is designed for Stage 2. |
| **3 — Multichannel** | Consistent across 3+ platforms; content plan in place | Use AI for cross-platform adaptation, email subject lines, and blog outlines. Add `prompt-engineering-library`. |
| **4 — Automated** | Workflows documented; team trained; scheduling system live | Use AI for scheduling triggers, performance-based content adjustments, and reporting summaries. Add `playbook-ai-automation-workflow`. |

Identify the client's current stage in the playbook introduction. Do not prescribe Stage 4 tools to a Stage 1 client.

---

## 7. What AI Cannot Do

These are structural limitations — not tool failures that future updates will fix. Understanding them prevents misplaced reliance (Schaefer, 2025).

- **Read local cultural tensions in real time.** AI does not know what is politically sensitive in Kampala this week, what a recent local event means to a specific community, or when a trending phrase has acquired a charged meaning. A human who lives in that context must make this call.
- **Produce genuinely novel ideas.** AI recombines existing content at scale. It does not create. Every output is a statistically likely arrangement of what has already been published. Original positioning, unexpected angles, and genuinely new concepts come from human insight.
- **Create collective effervescence.** Shared human experiences — a live event, a community moment, a real crisis — generate emotion that AI content cannot replicate. Content that matters to a community must be anchored in real, lived moments.
- **Replicate unscripted employee or founder voice.** The specific way a business owner talks to customers — their humour, their turns of phrase, their directness — is not reproducible by AI. Capture it in `brand-voice-ai-training`; do not try to generate it from a prompt.
- **Understand what is socially sensitive in a specific EA community right now.** Ethnic, religious, political, and generational sensitivities vary by country, region, and moment. AI has no current awareness. Do not let AI draft content touching on any of these areas without a human review by someone with direct community knowledge.

---

## 8. What NOT to Use AI For

These prohibitions are not suggestions. Each one exists because real harm — to the client, the audience, or the consultancy — is the predictable outcome of ignoring it.

- **Do not use AI to generate client testimonials or reviews.** Fabricated social proof is dishonest and illegal in many jurisdictions. If a client needs testimonials, collect real ones.
- **Do not publish AI-generated content without a human read.** AI hallucinates. It invents product details, fabricates prices, misrepresents services, and produces plausible errors. An unread AI post is a liability, not a time-saving.
- **Do not use AI for crisis communications responses.** A brand apology, a response to a serious complaint, or any statement during a reputational incident requires human judgement, empathy, and accountability. See `playbook-crisis-communications` for the correct protocol.
- **Do not allow AI to state specific statistics or data without verifying each figure.** AI generates statistics that sound credible and are frequently wrong. Any number in a published post must trace back to a verifiable source.
- **Do not let AI generate the brand voice guide.** The brand voice comes from the client discovery session in 04-brand-voice-intake and `brand-voice-ai-training` — real conversations, real examples, real dislikes. AI cannot do this work.
- **Do not use AI-generated images as photographic evidence of real products, services, or events.** AI image tools produce convincing fictions. Using them as if they depict the client's real premises or products misleads consumers.

---

## 9. AI Disclosure Policy

Apply this guidance to every client account. When in doubt, disclose — audiences in the EA market are becoming more sophisticated about AI use, and proactive transparency builds rather than erodes trust.

**Disclose — required:**
Use a clear label ("AI-generated image" or "Created with AI") when AI-generated images are used in advertising, editorial features, or any context where the audience might assume the image depicts a real person, place, or event.

**Disclose — best practice:**
If a post is substantially AI-generated (drafted and published with only minor edits), a light disclosure such as "Created with AI assistance" builds long-term audience trust. Use it selectively on posts where the AI role was significant.

**No disclosure required:**
Using AI as a drafting tool that is then substantially edited, rewritten, and personalised by a human is industry-standard practice and does not require disclosure.

For the formal client AI content policy document covering legal considerations and disclosure obligations, invoke `policy-ai-content-ethics`.

---

## 10. Platform-Specific AI Tips

Apply these notes when generating content for each platform. Generic AI outputs underperform on every platform — these adjustments close the gap.

**LinkedIn**
B2B audiences on LinkedIn — especially professionals in Kampala, Nairobi, and Lagos — are increasingly skilled at recognising AI-generated posts. The tell: perfectly structured paragraphs, no personal specificity, and generic professional language. Always add a personal observation, a specific client experience, or a genuine professional opinion. If the post reads like a thought leadership template, re-prompt or rewrite.

**TikTok**
AI-written scripts sound scripted on camera — and TikTok audiences will skip within two seconds. Use AI for the opening hook only (the first line or first visual idea). Film the rest naturally and conversationally. CapCut AI captions are the single most useful AI application for TikTok — use them on every video.

**WhatsApp**
Broadcast message recipients know when they are reading a template. AI-written WhatsApp messages have a generic warmth that is immediately recognisable. Use AI to draft the structure, then rewrite in the client's natural voice. Heavy personalisation (name, recent purchase, specific context) is mandatory. Never send a broadcast without at least one personal element per recipient segment.

**Instagram**
Feed captions are well-suited to AI drafting — quality control and a human edit produce good results. Stories and Reels voice-overs must be authentic. If the client is speaking on camera, they should speak from bullet points, not read an AI script. Use AI to generate caption options for Reels after filming — not to script what the creator says.

**Email**
Subject lines are the highest-value AI application in email marketing — run Prompt 8 from `prompt-engineering-library` and test multiple options. Email body copy benefits from an AI draft that is then substantially edited: check every claim, rewrite the opening paragraph in the client's real voice, and ensure the call to action matches the actual offer.

---

## Related Skills

| Skill | When to Use It |
|---|---|
| `brand-voice-ai-training` | Step 0 — before any AI content is generated for a new client |
| `prompt-engineering-library` | Full prompt set (15 templates, 7 copywriting frameworks) |
| `ai-content-humaniser` | Making AI drafts sound human before publishing |
| `playbook-ai-automation-workflow` | Stage 3–4 clients; scheduling triggers and pipeline automation |
| `playbook-crisis-communications` | Any reputational incident — do not use AI for crisis response |
| `policy-ai-content-ethics` | Formal AI disclosure and legal compliance documentation |

---

## Human Authenticity Gate

All content produced through the workflow documented in this playbook must pass through the `ai-content-humaniser` before client delivery. This is not optional and is not a step that can be omitted under time pressure. AI-generated or AI-assisted drafts must meet the Golden Rule: every output must look, feel, and sound as if it was crafted by the most skilled human creative with deep knowledge of the target audience. Generic, flat, or culturally misaligned output is not acceptable regardless of how efficiently it was produced.

---

## Quality Criteria

Output meets production standard when it satisfies all of the following:

- The Brand Context Block template is complete with all fields identified and explicitly references `brand-voice-ai-training` as the source for tone words and vocabulary
- The Alpha-Beta-Gamma-Delta-Epsilon prompt structure is explained clearly enough that a team member with no prior prompt training can apply it immediately
- All 8 core prompts produce usable, on-brand outputs when run as written — test at least 3 before handing over to a client
- The Quality Control Protocol includes all six checks, including the cultural localisation check, and is specific enough to catch real AI errors — not just general advice to "review the content"
- British English is enforced throughout, including inside every prompt template (each prompt specifies "British English" explicitly)
- The Content Maturity Model is used to stage the client correctly — the playbook introduction names the client's current stage
- The workflow section states specific time estimates for each step and includes a time-saving calculation with actual figures, not vague efficiency claims
- The "What AI Cannot Do" section is distinct from "What NOT to Use AI For" — the former covers structural limitations, the latter covers operational prohibitions
- No paid tools are required to implement the core workflow — ChatGPT free tier, Canva free tier, and Grammarly free tier are sufficient
- Platform-specific notes are specific enough to act on immediately, not generic recommendations
