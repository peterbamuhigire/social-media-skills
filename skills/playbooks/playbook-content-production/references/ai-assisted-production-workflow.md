# AI-Assisted Production Workflow

Merged from skills/playbooks/playbook-ai-content-workflow on 2026-09-29 at 7c60138; preservation map: [playbook-ai-content-workflow.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/playbook-ai-content-workflow.md)

## When to use this reference

Use it when a client or delivery team wants AI tools (text, image, caption, video or audio tools) built into the content production process: choosing EA-accessible tools, calibrating AI to the brand voice, running a prompt set for captions, ideas, hashtags and repurposing, gating every AI draft through quality control, and fitting the result into a weekly production and scheduling rhythm. It produces an AI content workflow playbook for one client.

Scope limits:

- The photography, video and graphic briefs, batch shoot day and shoot checklist stay in the main [SKILL.md](../SKILL.md). This reference covers the AI drafting layer that feeds them and the captions that go with them.
- Operational automation (scheduling triggers, auto-repurposing pipelines, multi-platform distribution): use [ai-automation-recipes.md](../../playbook-marketing-automation/references/ai-automation-recipes.md) in `playbook-marketing-automation`.
- The full prompt set and copywriting frameworks: [`prompt-engineering-library`](../../../content-writing/prompt-engineering-library/SKILL.md).

## Inputs

Collect before generating the playbook:

| # | Input | Notes |
|---|---|---|
| 1 | Client name and industry | |
| 2 | Brand voice | 3 tone words from [`04-brand-voice-intake`](../../../pipeline/04-brand-voice-intake/SKILL.md) (e.g. warm, authoritative, direct) |
| 3 | Vocabulary avoid list | Words and phrases the client must never use (from `04-brand-voice-intake`) |
| 4 | Content pillars | Pillar names from [`10-content-pillars`](../../../pipeline/10-content-pillars/SKILL.md) |
| 5 | Platforms in scope | Only the platforms this client actively uses |
| 6 | Team size | Solo (owner-operated), small team (2–5) or large team (6+) |
| 7 | Country/city | Defaults to Uganda/East Africa if not specified |

## Decision rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| AI output contains an unsupported claim or generic filler | Return it to evidence and editorial review | Fast production of misleading content |
| No Brand Context Block exists for the client | Run Step 0 (brand voice calibration) before any AI content is generated | Generic output that sounds like every other brand in the industry |
| Client is at maturity Stage 1 | Use AI for ideation and caption drafting only; establish the posting rhythm first; do not prescribe Stage 4 tools | Automation that creates chaos, not efficiency |
| Tool stack not yet chosen | Start with ChatGPT and Canva only; add Grammarly in week two; defer all others | Ten tools recommended, none used consistently |
| Draft contains statistics, market data, product claims, named entities, dates or prices | Apply the Hallucination Management Gate in addition to the Accuracy Check | Plausible fabricated facts reaching the audience |
| Content concerns a reputational incident, a serious complaint or a crisis | Do not use AI; route to [`playbook-crisis-communications`](../../playbook-crisis-communications/SKILL.md) | Responses lacking human judgement, empathy and accountability |
| Content makes a claim to authority, expertise or personal experience | Apply the Proof of Human standard | Loss of audience trust in thought leadership |
| AI-generated image used in advertising, editorial or where the audience may assume it depicts a real person, place or event | Label it ("AI-generated image" or "Created with AI") | Misleading consumers |
| Content touches ethnic, religious, political or generational sensitivities | Human review by someone with direct community knowledge before AI drafts are used | Culturally harmful or tone-deaf output |
| Same prompt produces off-brand output in two or more sessions | Version and update the prompt template (Step 8) | A prompt library that never improves |

## Procedure

### Step 1: Stage the client on the content maturity model

Assess where the client currently sits before prescribing tools or workflows. Introducing automation to a client at Stage 1 creates chaos, not efficiency (Upadhyay, 2024).

| Stage | Description | AI use at this stage |
|---|---|---|
| **1 — Basic** | Posting inconsistently; no strategy; content reactive | Use AI for ideation and caption drafting only. Establish posting rhythm first. |
| **2 — Aligned** | Regular posting; brand voice defined; pillars in use | Use AI for full caption workflow, hashtag research and repurposing. This workflow is designed for Stage 2. |
| **3 — Multichannel** | Consistent across 3+ platforms; content plan in place | Use AI for cross-platform adaptation, email subject lines and blog outlines. Add `prompt-engineering-library`. |
| **4 — Automated** | Workflows documented; team trained; scheduling system live | Use AI for scheduling triggers, performance-based content adjustments and reporting summaries. Add `playbook-marketing-automation` ([AI automation recipes](../../playbook-marketing-automation/references/ai-automation-recipes.md)). |

Name the client's current stage in the playbook introduction. Do not prescribe Stage 4 tools to a Stage 1 client.

### Step 2: Choose the tools (EA-accessible)

Start with two tools only: ChatGPT and Canva. Add others once the workflow is established. Recommending ten tools at once guarantees none of them get used consistently.

| Tool | What it does | EA access |
|---|---|---|
| **ChatGPT** (OpenAI) | Text generation, ideation, caption drafting, copywriting | Free tier via browser; no app required |
| **Claude** (Anthropic) | Text generation, longer-form drafting, analysis | Free tier via browser |
| **Canva Magic Write / Magic Design** | AI-generated social graphics with copy suggestions | Free tier; used directly in Canva |
| **Grammarly** | Grammar check, tone review, British English correction | Free browser extension and web app |
| **CapCut AI Captions** | Automatic captions for videos; available on mobile | Free; works on Android and iOS |
| **Google Gemini** | Research assistance, ideation, summarisation | Free via Google account |
| **Magai / Poe** | Multi-model AI access in one interface | Paid; for advanced users only |
| **HeyGen** | AI video production; talking-head avatars | Paid; for advanced video users |
| **Tavus** | Personalised AI video at scale | Paid; for advanced personalisation workflows |
| **NotebookLM** | AI podcast production from source documents | Free (Google); browser-based |
| **Frase.io** | Content optimisation, pruning and gap analysis | Paid; for content-mature clients |
| **Make.com** | Workflow automation and multi-tool pipelines | Free tier; for Stage 3–4 clients |
| **Descript** | AI audio and video editing; transcription | Paid; for clients producing audio/video |
| **AdCreative.ai** | AI-generated ad creative variations | Paid; for clients running paid social |

Tool tiers and pricing change; verify the current free-tier terms before recommending a tool to a client.

**Starting recommendation:** ChatGPT for all text work and Canva for all graphic work. Both have free tiers, both work on a basic smartphone or laptop, and both are already familiar to most EA users. Introduce Grammarly in week two as a mandatory quality step. Defer all other tools until the core workflow is running smoothly. No paid tool is required for the core workflow: the ChatGPT, Canva and Grammarly free tiers are sufficient.

**Content pruning** (Roth and neuroflash, 2024/2025): removing or updating outdated content matters as much as new creation. Use Frase.io or manual audits quarterly to find and refresh content that is no longer accurate, performing or relevant. A content library that grows without pruning accumulates liability.

### Step 3: Calibrate the brand voice (Step 0 — before any AI content)

This step is not optional. Skipping it produces generic output that sounds like every other brand in the client's industry.

**Formal brand voice capture.** Before building the Brand Context Block, run [`brand-voice-ai-training`](../../../ai-marketing/brand-voice-ai-training/SKILL.md). That skill runs the full 6-step process: extracting tone words from real client language, building the vocabulary avoid list, generating reference examples and producing an AI-ready voice profile. The Brand Context Block draws directly from that output and from `04-brand-voice-intake`.

**The Brand Context Block** is a reusable prompt prefix. Paste it at the start of every new AI session. Complete every bracketed field before use.

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

**Saving and reusing the block:**

- **ChatGPT Custom Instructions (recommended):** profile → Custom Instructions → paste the completed block into the "What would you like ChatGPT to know about you?" field. It then loads into every new conversation. (Menu labels change; confirm the current path.)
- **Session-start paste method:** keep the completed block in a shared Google Doc or WhatsApp Saved Messages and paste it as the very first message in any new AI session before asking for content.
- **Team use:** if more than one person generates content for the same client, share the completed block in the team WhatsApp group. Everyone uses the same block; a team using different context blocks produces inconsistent content.

**Refining the block over time.** After four weeks of use, review AI outputs against the brand voice. If a pattern of off-brand outputs persists:

- AI consistently sounds too formal: add "We speak in a conversational, friendly tone — not corporate or stiff."
- AI ignores banned vocabulary: move the banned list higher in the block and bold it.
- AI defaults to American English despite the instruction: add "Spell-check: colour, organisation, behaviour, recognise, centre, programme, analyse."

Update the shared Brand Context Block document every time you change it. Date each version.

### Step 4: Draft with the core prompt templates

**Prompt structure: Alpha-Beta-Gamma-Delta-Epsilon.** Every effective AI prompt contains five elements (Upadhyay, 2024):

| Element | What it does | Example |
|---|---|---|
| **Alpha — Role** | Assigns expertise to the AI | "You are writing for a Kampala-based SME…" |
| **Beta — Context** | Provides background and brand parameters | The Brand Context Block |
| **Gamma — Task** | States the specific output required | "Write a 150-word Instagram caption about…" |
| **Delta — Constraints** | Sets limits (length, tone, language, exclusions) | "Under 100 characters. British English. No hashtags." |
| **Epsilon — Output format** | Specifies how the result should be presented | "Output: 3 numbered options." |

The Brand Context Block covers Alpha and Beta; every prompt below adds Gamma, Delta and Epsilon. Do not remove any element. The core prompts use PAS (Problem–Agitate–Solution) and AIDA (Attention–Interest–Desire–Action) by default; for all 7 frameworks (PAS, AIDA, BAB, FAB, SSS, PPPP and AFOREST) and further ready-to-use templates, use `prompt-engineering-library`. Every prompt specifies British English output; do not remove that instruction.

**Captions**

- **Prompt 1 — Short caption (under 100 characters, Instagram / WhatsApp):** `[CONTEXT BLOCK] Write a short social media caption of under 100 characters for [platform]. The post is about [topic or product]. Include one relevant emoji. Do not include hashtags. Output: one caption only. British English.`
- **Prompt 2 — Medium caption (100–200 characters, Facebook / LinkedIn):** `[CONTEXT BLOCK] Write a social media caption of 100–200 characters for [platform]. The post is about [topic or product]. Open with a strong first line that stops the scroll. Include a call to action at the end. Do not include hashtags. Output: two caption options to choose between. British English.`
- **Prompt 3 — Carousel or thread (5–7 slides / tweets):** `[CONTEXT BLOCK] Write a [5-slide carousel / 6-tweet thread] about [topic]. Each slide/tweet should make one clear point. Open with a hook that creates curiosity. Close with a call to action linking to [desired action]. Output: numbered slides or tweets, one line each. British English.`

**Content ideas**

- **Prompt 4 — Monthly content ideas from pillars:** `[CONTEXT BLOCK] Generate 30 social media content ideas for [month]. Distribute evenly across these pillars: [pillar 1], [pillar 2], [pillar 3]. Include a mix of educational, entertaining, and promotional content. For each idea: content type (post, Reel, Story, carousel), pillar, and a one-sentence description. Output: numbered table. British English.`
- **Prompt 5 — Seasonal or campaign content ideas:** `[CONTEXT BLOCK] Generate 10 social media content ideas for [occasion — e.g. Eid, end of financial year, back to school]. Relevant to [industry] and the Ugandan/East African context. For each idea: platform, format, one-sentence description. Output: numbered list. British English.`

**Hashtags**

- **Prompt 6 — Hashtag set for a specific post:** `[CONTEXT BLOCK] Suggest 15 relevant hashtags for a [platform] post about [topic]. Include: 3 broad hashtags (over 1 million uses), 6 mid-range (100k–1 million uses), 6 niche (under 100k uses). Include at least 2 Uganda or East Africa specific hashtags. Output: three labelled groups. British English.`

**Repurposing and community management**

- **Prompt 7 — Long content to short social post:** `[CONTEXT BLOCK] I have the following long-form content: [paste blog post, article, or transcript]. Extract the 3 most valuable insights and write a separate caption for each, suitable for [platform]. Each caption: 100–150 words, ends with a call to action. Output: 3 numbered captions. British English.`
- **Prompt 8 — Response to a complaint or negative review:** `[CONTEXT BLOCK] Write a response to the following complaint on [platform]: "[paste complaint]". Acknowledge the issue, apologise without admitting legal liability, offer to resolve privately via WhatsApp or DM, under 80 words. Do not be defensive. Output: one response. British English.`

For email subject lines, blog post outlines, positive review responses, video transcript captions and the full template set, use `prompt-engineering-library`. Test at least 3 of the 8 core prompts as written before handing the playbook to a client.

### Step 5: Run the quality control protocol

Every AI-generated output passes all six checks before publication, in order. Do not skip steps under time pressure.

- [ ] **Brand voice check:** read the output aloud. Does it match the 3 tone words? If it sounds generic, stiff or unlike the client, rewrite or re-prompt before proceeding.
- [ ] **British English check:** paste into Grammarly. Fix American spellings (color → colour, organization → organisation, analyze → analyse, program → programme, center → centre, recognize → recognise). Reject "apologize"; it should be "apologise".
- [ ] **Banned vocabulary check:** scan against the client's vocabulary avoid list AND the universal AI blacklist: *delve, tapestry, leverage, game-changer, groundbreaking, revolutionary, navigate, foster, realm, unleash, unlock, elevate, thriving, vibrant, seamless, robust, empower.* Delete and rewrite; do not just find-and-replace.
- [ ] **Accuracy check:** highlight every factual claim about the client's products, services, prices or history. Verify each one directly with the client or source document before publishing. AI fabricates plausible-sounding facts; assume no specific claim is correct.
- [ ] **Human touch check:** add one element AI could not have generated: a specific detail about the client's premises, a local reference (a Kampala neighbourhood, an EA seasonal moment, a current local context), a genuine customer name (with permission) or the owner's voice. Every published output contains at least one human edit. Not optional.
- [ ] **Cultural localisation check:** does the content reference at least one Uganda/EA-specific element? Generic "African" content is not enough. Name the specific country, city, market or moment; if absent, add one before publishing.

**Hallucination Management Gate** (Mizrahi, 2024; Evelyn, 2025). An explicit extra step for all content making factual, statistical or market-specific claims. For any draft containing specific statistics, market data, product claims, named entities, dates or prices, include this instruction in the prompt:

> "Use web search to find the latest news and resources, and cite your sources."

Then verify the cited sources independently before human review. Do not assume web-search output is correct; check the linked source directly. The Accuracy Check applies to all content; the Hallucination Gate applies specifically to claims of fact the audience might act on: statistics in proposals, market data in strategy documents, product specifications in captions.

**Proof of Human (high-stakes content)** (Schaefer, 2025). For thought leadership posts, strategy documents, personal brand content, or any post where audience trust is the currency, signal that a human wrote or heavily shaped the content. Show it rather than assert it:

- Share the process: a draft with visible edits, a voice note explaining your thinking, or a behind-the-scenes note.
- Name the author and include a personal observation specific to their experience.
- Reference a real, verifiable event, conversation or local context that AI could not have known.

Apply this whenever content makes a claim to authority, expertise or personal experience.

**Human Authenticity Gate.** All content produced through this workflow passes through the `anti-ai-slop` humanising rewrite passes ([humanising-rewrite-passes.md](../../../ai-marketing/anti-ai-slop/references/humanising-rewrite-passes.md)) before client delivery. This is not optional and cannot be omitted under time pressure. AI-generated or AI-assisted drafts meet the Golden Rule: every output must look, feel and sound as if crafted by the most skilled human creative with deep knowledge of the target audience. Generic, flat or culturally misaligned output is not acceptable, however efficiently it was produced.

### Step 6: Fit AI into the weekly production rhythm

AI does not replace the weekly content process; it compresses the time each step takes.

**Weekly AI-assisted workflow (5 posts per week, Instagram):**

| Block | Time | Actions |
|---|---|---|
| Monday — AI drafting | 10 minutes | Open ChatGPT. Paste the Brand Context Block. Run Prompt 4 to confirm the week's topics if not already planned. Run Prompt 1 or 2 five times, once per post. Save all five drafts in a shared Google Doc or Notion page labelled "[Client] — Week of [date] — AI drafts." |
| Monday — human review and edit | 30 minutes | Run the quality control protocol on each draft. Add the human touch element to each caption. Mark status: Approved / Needs Revision / Reject. Re-prompt or write rejected captions manually; never publish a draft that failed a check. |
| Monday — scheduling | 20 minutes | Load approved captions into Buffer or Hootsuite. Assign dates and times. Attach images. Set every post to schedule (not auto-publish) so the client can review before anything goes live. |
| **Total with AI** | **60 minutes per week** | |

**Time-saving calculation — 5-post Instagram account:**

| Task | Without AI | With AI |
|---|---|---|
| Researching and writing 5 captions | 75 minutes | 10 minutes (AI draft) + 30 minutes (edit) |
| Hashtag selection per post | 15 minutes | 5 minutes |
| Scheduling in Buffer/Hootsuite | 20 minutes | 20 minutes (unchanged) |
| **Total per week** | **110 minutes** | **65 minutes** |
| **Total per month (4 weeks)** | **7.3 hours** | **4.3 hours** |
| **Monthly saving** | — | **3 hours per client** |

(The 60-minute block total excludes the 5 minutes of hashtag selection counted in the 65-minute table total.) For a consultant managing five clients, AI-assisted workflows free up to 15 hours per month for strategy, client relationships and business development. These figures are a labelled planning scenario; replace them with the client's measured times once available.

For advanced automation (scheduling triggers, auto-repurposing pipelines, multi-platform distribution), use [ai-automation-recipes.md](../../playbook-marketing-automation/references/ai-automation-recipes.md).

### Step 7: Apply platform-specific AI adjustments

Generic AI outputs underperform on every platform; these adjustments close the gap.

| Platform | Adjustment |
|---|---|
| **LinkedIn** | B2B audiences, especially professionals in Kampala, Nairobi and Lagos, increasingly recognise AI-generated posts. The tell: perfectly structured paragraphs, no personal specificity, generic professional language. Always add a personal observation, a specific client experience or a genuine professional opinion. If the post reads like a thought leadership template, re-prompt or rewrite. |
| **TikTok** | AI-written scripts sound scripted on camera, and TikTok audiences skip within two seconds. Use AI for the opening hook only (the first line or first visual idea). Film the rest naturally and conversationally. CapCut AI captions are the single most useful AI application for TikTok; use them on every video. |
| **WhatsApp** | Broadcast recipients know when they are reading a template; AI-written WhatsApp messages have a generic warmth that is immediately recognisable. Use AI to draft the structure, then rewrite in the client's natural voice. Heavy personalisation (name, recent purchase, specific context) is mandatory. Never send a broadcast without at least one personal element per recipient segment. |
| **Instagram** | Feed captions suit AI drafting; quality control and a human edit produce good results. Stories and Reels voice-overs must be authentic: if the client speaks on camera, they speak from bullet points, not an AI script. Use AI to generate caption options for Reels after filming, not to script what the creator says. |
| **Email** | Subject lines are the highest-value AI application in email marketing: run the email subject-line template in `prompt-engineering-library` (§ Email Subject Line and Preview Text; "Prompt 8" in the retired source's numbering) and test multiple options. Body copy benefits from an AI draft that is then substantially edited: check every claim, rewrite the opening paragraph in the client's real voice, and make sure the call to action matches the actual offer. |

### Step 8: Disclose, watermark, keep context and improve prompts

**AI disclosure policy.** Apply to every client account. When in doubt, disclose: EA audiences are becoming more sophisticated about AI use, and proactive transparency builds rather than erodes trust.

| Level | When | Label |
|---|---|---|
| Disclose — required | AI-generated images in advertising, editorial features, or any context where the audience might assume the image depicts a real person, place or event | "AI-generated image" or "Created with AI" |
| Disclose — best practice | Post substantially AI-generated (drafted and published with only minor edits); use selectively where the AI role was significant | "Created with AI assistance" |
| No disclosure required | AI used as a drafting tool, then substantially edited, rewritten and personalised by a human (industry-standard practice) | None |

For the formal client AI content policy covering legal considerations and disclosure obligations, use [`policy-ai-content-ethics`](../../../policies/policy-ai-content-ethics/SKILL.md). Platform and legal labelling rules change; verify current rules before citing them to a client.

**AI content watermarking** (Ching and Mothi, 2025). For AI-generated audio and visual assets, tag the original AI-generated files with persistent metadata or watermarks before any editing or compression.

- **Audio:** the source names SynthID (Google/DeepMind) as the current standard for AI-generated audio; it embeds a watermark that survives compression and editing. Verify current tool coverage before relying on it.
- **Images and video:** equivalent watermarking tools exist; apply to original source files before delivering to the client or publishing.
- **Production record:** note in the project file which assets were AI-generated and confirm that watermarking was applied to the original file.

This protects the agency if AI-generated content is later disputed and establishes a chain of custody for client deliverables.

**Contextual continuity** (Evelyn, 2025). In multi-step production workflows, AI loses coherence as context accumulates across exchanges.

- Do not assume context carries across sessions. When continuing a workflow from a previous session, re-paste the Brand Context Block before any new content instruction.
- In long sessions (more than 8–10 exchanges), re-state key context: "Remember: the brand is [X], tone is [Y], platform is [Z]." Reference previous outputs explicitly: "Using the caption you wrote in step 2, now write a matching Story caption." Never assume the AI remembers.
- When a different team member continues a session or picks up a draft, share the full conversation thread or paste a session summary, not just the prompt.

**Iterative prompt improvement** (Ching and Mothi, 2025). A prompt library that never changes never improves; document how the agency refines templates.

- **Triggers for an update:** off-brand output recurring across two or more sessions with the same prompt; repeated quality failures of the same type (e.g. AI consistently ignores a constraint); client feedback that an output type consistently misses the mark; platform algorithm changes that affect format or length requirements.
- **Documenting updates:** version the template (`caption-facebook-PAS-v1`, `caption-facebook-PAS-v2`); record what changed and why in the project file alongside the prompt; date every version and keep old versions for reference.
- **Sharing improved prompts:** store all versioned prompts in the shared team folder (Google Drive or Notion); notify the team via WhatsApp when a new version is live; review the full library quarterly and retire prompts consistently outperformed by newer versions.

This turns one-off prompting into a learning system. A library built over 12 months is a proprietary agency asset.

## Limits: what AI cannot do and must not be used for

Keep these two lists distinct: the first covers structural limitations, the second operational prohibitions.

**What AI cannot do** (Schaefer, 2025). Structural limitations, not tool failures that future updates will fix:

- **Read local cultural tensions in real time.** AI does not know what is politically sensitive in Kampala this week, what a recent local event means to a specific community, or when a trending phrase has acquired a charged meaning. A human who lives in that context makes this call.
- **Produce genuinely novel ideas.** AI recombines existing content at scale; every output is a statistically likely arrangement of what has already been published. Original positioning, unexpected angles and new concepts come from human insight.
- **Create collective effervescence.** Shared human experiences (a live event, a community moment, a real crisis) generate emotion AI content cannot replicate. Content that matters to a community is anchored in real, lived moments.
- **Replicate unscripted employee or founder voice.** The way a business owner talks to customers (their humour, turns of phrase, directness) is not reproducible by AI. Capture it in `brand-voice-ai-training`; do not generate it from a prompt.
- **Understand what is socially sensitive in a specific EA community right now.** Ethnic, religious, political and generational sensitivities vary by country, region and moment, and AI has no current awareness. Do not let AI draft content touching these areas without human review by someone with direct community knowledge.

**What NOT to use AI for.** Each prohibition exists because real harm to the client, the audience or the consultancy is the predictable outcome of ignoring it:

- **Client testimonials or reviews.** Fabricated social proof is dishonest and illegal in many jurisdictions. Collect real ones.
- **Publishing without a human read.** AI invents product details, fabricates prices, misrepresents services and produces plausible errors. An unread AI post is a liability, not a time-saving.
- **Crisis communications responses.** A brand apology, a response to a serious complaint, or any statement during a reputational incident needs human judgement, empathy and accountability. Use `playbook-crisis-communications`.
- **Unverified statistics or data.** AI generates statistics that sound credible and are frequently wrong. Every number in a published post traces back to a verifiable source.
- **Generating the brand voice guide.** The brand voice comes from the client discovery session in `04-brand-voice-intake` and `brand-voice-ai-training`: real conversations, real examples, real dislikes.
- **AI images as photographic evidence.** AI image tools produce convincing fictions. Using them as if they depict the client's real premises, products, services or events misleads consumers.

## Companion skills

| Skill | When to use it |
|---|---|
| [`brand-voice-ai-training`](../../../ai-marketing/brand-voice-ai-training/SKILL.md) | Step 0, before any AI content is generated for a new client |
| [`prompt-engineering-library`](../../../content-writing/prompt-engineering-library/SKILL.md) | Full prompt set and 7 copywriting frameworks |
| [`anti-ai-slop`](../../../ai-marketing/anti-ai-slop/SKILL.md) ([humanising rewrite passes](../../../ai-marketing/anti-ai-slop/references/humanising-rewrite-passes.md)) | Making AI drafts sound human before publishing |
| [`playbook-marketing-automation`](../../playbook-marketing-automation/SKILL.md) ([AI automation recipes](../../playbook-marketing-automation/references/ai-automation-recipes.md)) | Stage 3–4 clients; scheduling triggers and pipeline automation |
| [`playbook-crisis-communications`](../../playbook-crisis-communications/SKILL.md) | Any reputational incident; do not use AI for crisis response |
| [`policy-ai-content-ethics`](../../../policies/policy-ai-content-ethics/SKILL.md) | Formal AI disclosure and legal compliance documentation |

## Acceptance checklist

The AI content workflow playbook meets production standard when:

- [ ] The Brand Context Block template is complete with all fields identified and names `brand-voice-ai-training` as the source for tone words and vocabulary.
- [ ] The Alpha-Beta-Gamma-Delta-Epsilon structure is explained clearly enough that a team member with no prompt training can apply it immediately.
- [ ] All 8 core prompts produce usable, on-brand outputs when run as written; at least 3 were tested before handover.
- [ ] The quality control protocol includes all six checks, including cultural localisation, and is specific enough to catch real AI errors, not general advice to "review the content".
- [ ] British English is enforced throughout, including inside every prompt template (each specifies "British English").
- [ ] The content maturity model stages the client, and the playbook introduction names the current stage.
- [ ] The workflow states specific time estimates per step and a time-saving calculation with actual figures, not vague efficiency claims.
- [ ] "What AI cannot do" (structural limitations) is kept distinct from "What NOT to use AI for" (operational prohibitions).
- [ ] No paid tools are required for the core workflow (ChatGPT, Canva and Grammarly free tiers suffice).
- [ ] Platform-specific notes are specific enough to act on immediately.
- [ ] Every draft passed the Human Authenticity Gate before client delivery.

## Sources

Citations are carried as the retired source gave them; forms that conflict elsewhere in the engine are flagged for reconciliation before external citation.

- Upadhyay (2024) *Generative AI for Marketing*. Alpha-Beta-Gamma-Delta-Epsilon prompt structure; content maturity model. Note: the engine cites this title as Upadhyay, N. (Kogan Page), Upadhyay, S. and Upadhyay, M. A. (Packt); reconcile author initials and publisher.
- Schaefer, M. (2025). "Proof of Human" standard and structural limits of AI (the retired source gives no title). Note: the engine cites Schaefer, M. W. (2025) *Audacious: How Humans Win in an AI Marketing World*, Schaefer Marketing Solutions, and attributes "Proof of Human" to Schaefer, M. (2023) *Belonging to the Brand*; reconcile.
- Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing Teams*. Content pruning.
- Ching, V. and Mothi, D. (2025) *AI for Creatives: Unlocking Expressive Digital Potential*. CRC Press. Iterative prompt improvement; AI content watermarking (SynthID). (Initials verified as Vivian Ching and Dinesh Mothi on the Routledge/CRC page, 29 Sep 2026; the publisher imprint is Auerbach Publications.)
- Mizrahi, T. (2024). Hallucination management (title not given in the retired source).
- Evelyn, A. (2025). Hallucination Management Gate; contextual continuity (title not given in the retired source).

No `docs/source-registers/source-register.json` ID was cited by the retired source; tool tiers, platform labelling rules and watermarking coverage are volatile and must be verified before client use.
