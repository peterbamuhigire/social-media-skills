---
name: prompt-engineering-library
description: Generates a ready-to-use, client-specific prompt engineering library — a documented set of reusable prompt templates for all recurring marketing tasks. Every prompt follows the Alpha-Beta-Gamma-Delta-Epsilon master formula (Upadhyay, 2024) and is prefixed with the client's Brand Context Block. Invoke when onboarding a new client onto AI-assisted content production, or when a client team needs a standardised set of approved prompts for their own use.
---
# Prompt Engineering Library

<!-- dual-compat:start -->
## Use when
- Generates a ready-to-use, client-specific prompt engineering library — a documented set of reusable prompt templates for all recurring marketing tasks. Every prompt follows the Alpha-Beta-Gamma-Delta-Epsilon master formula (Upadhyay, 2024) and is prefixed with the client's Brand Context Block. Invoke when onboarding a new client onto AI-assisted content production, or when a client team needs a standardised set of approved prompts for their own use.
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
- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Before generating the library, ask for:

1. **Client business name** — exact trading name
2. **Industry** — sector and sub-sector (e.g. financial services / SACCO)
3. **Country/City** — defaults to Uganda/Kampala if not specified
4. **Primary goal** — the main business objective this library will serve (e.g. lead generation, brand awareness, community growth)
5. **Brand Context Block** — paste the output from `brand-voice-ai-training`, or provide: brand voice descriptors, banned vocabulary, audience description, and primary WhatsApp number
6. **Active platforms** — list the platforms the client publishes on
7. **Priority tasks** — which recurring tasks the team performs most often (captions, blogs, reports, etc.)

---

## The Master Prompt Formula

Source: Upadhyay, S. (2024) *Generative AI for Marketing*.

Every prompt in this library follows the Alpha-Beta-Gamma-Delta-Epsilon structure. Always prepend the client's Brand Context Block before the formula.

```
[Brand Context Block]

Consider the situation [Alpha — context and situation: what is happening, why it matters now].
Acting as [Beta — the creator persona AND a description of the target audience].
Perform [Gamma — the specific task to be completed].
In [Delta — the output format: caption, table, document, bullet list].
Using [Epsilon — boundaries, tone, style, length, platform rules, hard constraints].
```

**Alpha** — sets the scene. Include the product or service being promoted, the audience's current emotional or practical context, and any timely trigger (season, event, campaign phase).

**Beta** — defines two roles simultaneously: who is writing (the AI persona) and who they are writing for (the target reader). Both must be specific.

**Gamma** — states the task with precision. Vague tasks produce vague output. Include the copywriting framework (PAS, AIDA, etc.) when relevant.

**Delta** — specifies the exact format. "A caption" is insufficient; "a single caption with a line break after the hook, body text, and a CTA on a new line" is correct.

**Epsilon** — imposes hard constraints: language standard, word count, banned words, required elements (CTA, hashtags, WhatsApp link), and anything the output must never do.

---

## The 10 Prompt Components

Source: Upadhyay (2024). Every strong prompt draws on some or all of these components. Identify which are required for each task before writing the prompt.

| # | Component | What it controls |
|---|---|---|
| 1 | **Persona** | The creator role (e.g. social media copywriter) and the target audience (e.g. urban Ugandan women aged 25–40) |
| 2 | **Voice** | Tonality, emotional register, and formality level (e.g. warm and conversational; authoritative but approachable) |
| 3 | **Style** | The copywriting framework to apply: PAS, AIDA, BAB, FAB, SSS, PPPP, or AFOREST |
| 4 | **Parameters** | Length (word count, character limit), keywords to include, structural requirements |
| 5 | **Channel** | The exact platform (Facebook, LinkedIn, WhatsApp broadcast, email, blog) — each has different norms |
| 6 | **Output type** | The specific deliverable: caption, thread, email, table, bullet list, report narrative |
| 7 | **Subject/Objective** | The topic being covered and the specific goal of the piece (awareness, enquiry, purchase, retention) |
| 8 | **Actions** | The call-to-action required — what the reader should do next and how |
| 9 | **Reference** | A URL, competitor post, or LinkedIn profile the AI should learn from or match in quality |
| 10 | **Conditionality** | Hard constraints: never start with a question; always use British English; exclude competitor names; cite sources |

---

## Copywriting Style Frameworks

Apply via Component 3 (Style). Choose the framework that matches the audience's mindset and the content goal.

| Framework | Structure | When to use |
|---|---|---|
| **PAS** | Problem → Agitate → Solve | Complaint-heavy audiences; content that solves a specific pain point |
| **AIDA** | Attention → Interest → Desire → Action | Standard awareness-to-conversion sequence; new product announcements |
| **BAB** | Before → After → Bridge | Transformation stories; results-focused content; testimonials |
| **FAB** | Features → Advantages → Benefits | Product launches; explaining a new service or offering |
| **SSS** | Star → Story → Solution | Narrative-led content; personal brand posts; founder stories |
| **PPPP** | Picture → Promise → Prove → Push | Sales pages; high-stakes conversion content; premium offers |
| **AFOREST** | Alliteration → Facts → Opinions → Repetition → Examples → Statistics → Threes | Persuasive speeches; thought leadership articles; keynote scripts |

---

## Prompt Library — Templates by Task

Replace all content in square brackets with client-specific detail before use. The Brand Context Block is abbreviated as `[BCB]` below; always paste the full block.

---

### 1. Caption Writing

```
[BCB]

Consider the situation: [describe what the business is promoting and why it matters
to the audience right now — include the campaign phase or seasonal trigger].
Acting as a social media copywriter for [Brand] writing for [audience description:
age, location, aspiration, current pain point].
Write a [platform] caption using the [PAS / AIDA / BAB — choose one] framework.
In a single caption with a line break after the hook, body text, and a CTA on a
new line.
Using: British English; maximum 150 words; no banned vocabulary; end with a
WhatsApp CTA [wa.me/256XXXXXXXXX]; include [number] hashtags drawn from
[hashtag guidance or list]; never begin with "Are you".
```

---

### 2. Blog Post Brief

```
[BCB]

Consider the situation: [describe the target reader's search intent or problem —
what are they typing into Google or asking on WhatsApp right now].
Acting as a content strategist briefing a writer for [Brand].
Create a complete blog post brief including: SEO title (under 60 characters),
meta description (under 155 characters), primary keyword, 5 H2 headings,
one practical takeaway section, and a closing CTA.
In a structured markdown document.
Using: British English; 1,200–1,800 word target; first H2 must include the primary
keyword; all examples must be drawn from Uganda or East Africa; no Western-market
assumptions; link suggestion for one internal and one external source.
```

---

### 3. Email Subject Line and Preview Text

```
[BCB]

Consider the situation: [state the email campaign goal, the audience segment,
and the stage in the customer journey — e.g. re-engagement, post-purchase, onboarding].
Acting as an email marketer writing for [audience description].
Generate 5 subject line options and 5 matching preview texts.
In a table format with columns: Subject Line | Preview Text | Technique Used.
Using: subject line under 50 characters; preview text under 90 characters;
no clickbait or false urgency; techniques may include curiosity, benefit,
urgency, social proof, or personalisation; include at least one option with
a localised East African reference; British English throughout.
```

---

### 4. Audience Persona

```
Consider the situation: [business name, industry, and Uganda/East Africa market —
include any known data about current customers or target segment].
Acting as a market researcher building a detailed audience persona for [Brand].
Create a complete audience persona for [client's target segment name or description].
In a structured document with the following fields: Name (fictional), Age, Location
(specific EA city or town), Occupation, Monthly income (UGX), Education level,
Social platforms used, WhatsApp behaviour (how they use it for commerce and comms),
content formats they engage with, their primary problem, what they want to achieve,
objections to buying, and one direct quote that captures their mindset.
Using: only realistic Uganda/East Africa demographics and income ranges; cite
Facebook penetration data where relevant; no Western market assumptions; reference
Chaffey (2024) for audience segmentation methodology if applicable.
```

---

### 5. Social Media Strategy — Platform Selection Section

```
[BCB]

Consider the situation: [client's current social media presence, primary business
goal, competitive context in Uganda/EA, and budget constraints if known].
Acting as a social media strategist applying the RACE framework
(Reach/Act/Convert/Engage — Chaffey, 2024) for [Brand].
Produce the platform selection and channel roles section of a social media strategy.
In structured markdown: one summary table (Platform | Primary Role | Content Type |
Posting Frequency) followed by a rationale paragraph per recommended platform.
Using: Uganda/EA platform penetration data; WhatsApp as the primary owned channel
for customer communications; Facebook as the primary reach channel; recommend no
more than 3 platforms for a starter client; cite the POEM model
(Paid/Owned/Earned) when classifying channels.
```

---

### 6. Community Management Response

```
[BCB]

Consider the situation: [paste or describe the comment, DM, or WhatsApp message
verbatim — include the sentiment, platform, and whether it is public or private].
Acting as a community manager for [Brand] responding to a
[complaint / question / compliment / crisis comment].
Write a response that [acknowledges the issue and offers resolution /
answers the question directly / expresses genuine gratitude].
In a [public comment reply / private DM / WhatsApp message] of under 60 words.
Using: warm, respectful East African professional tone; move the conversation
to WhatsApp if resolution requires further discussion
[wa.me/256XXXXXXXXX]; never be defensive or dismissive; never delete a
complaint without resolution; British English throughout.
```

---

### 7. Monthly Performance Report Narrative

```
Consider the situation: [paste the month's key metrics — reach, impressions,
engagement rate, follower growth, link clicks, WhatsApp enquiries generated,
and any notable campaign results. Include the previous month's figures for
comparison where available].
Acting as a social media analyst writing an executive summary for
[client's management team — state their level of digital literacy].
Produce a 3-paragraph performance narrative covering: (1) overall summary
and standout metric; (2) what drove the best-performing content and what
underperformed; (3) one recommended action for next month.
In plain, jargon-free English formatted as three labelled paragraphs.
Using: British English; cite specific numbers in every paragraph;
no hollow phrases such as "robust performance" or "going forward";
conclude with a forward-looking recommendation framed as a SMART objective;
reference the RACE framework (Chaffey, 2024) if applicable.
```

---

## PAO Matrix — Pre-Prompt Checklist

Source: Joseph (c.2023–2024). Before writing any social media content prompt, confirm all three parameters simultaneously:

- **Platform** — which platform is this content for? (Each platform has different norms, formats, and audience expectations.)
- **Audience** — who specifically is this for, defined by values and mindset, not just demographics? (e.g. "first-generation entrepreneurs who value financial independence" not "25–40-year-olds")
- **Objective** — what is the specific objective? Choose one: awareness / engagement / conversion / retention.

Omitting any one parameter forces the AI to make assumptions that produce generic output. All three must appear explicitly in every social media content prompt, in the Alpha and Beta elements of the master formula.

---

## Prompt Anatomy Reference

Source: GPT Penguin (2024). Five-component anatomy that maps directly onto the Alpha-Beta-Gamma-Delta-Epsilon formula:

| GPT Penguin Component | Description | Maps to Formula Element |
|---|---|---|
| **Act Instruction** | The role and expertise level assigned to the AI (e.g. "Act as a senior social media copywriter") | Beta (creator persona) |
| **Context** | The situation, background, and why it matters now | Alpha |
| **Task** | The specific action to perform | Gamma |
| **Constraints** | Hard limits: length, tone, banned words, format rules | Epsilon |
| **Additional Guidance** | Style, examples, references, conditional instructions | Delta + any residual Epsilon |

Use this five-component map as a diagnostic: if a prompt is producing poor output, identify which component is missing or underdeveloped.

---

## Copywriting Formula Prompt Activation

Source: Mizrahi (2024). Naming the formula in the prompt is more effective than describing the desired structure in prose. The activation pattern:

```
Write [content type] using the [FORMULA NAME] framework ([brief description of the sequence]).
```

**Examples:**

```
Write a Facebook caption using the PAS framework (Problem → Agitate → Solve).
Write a LinkedIn post using the AIDA framework (Attention → Interest → Desire → Action).
Write a promotional WhatsApp broadcast using the FOMO framework (Fear Of Missing Out — create urgency around a time-limited opportunity).
Write a community post using the SMILE framework (Subscriber, Meaningful, Inspiring, Likeable, Educational — positive engagement-first content).
```

Never describe the structure in prose ("make it compelling and build to a call to action") when you can name the formula directly. Named formulas produce structurally correct output; prose descriptions produce approximations.

---

## Emotional Resonance Pattern

Source: GPT Penguin (2024). Human-sounding copy requires explicit emotional instruction. Every prompt for brand content must specify:

1. **The emotion to evoke** — trust, urgency, nostalgia, excitement, relief, pride, curiosity. Name it explicitly.
2. **The brand value to connect it to** — e.g. "connect the urgency to the brand's commitment to making financial services accessible."
3. **The instruction to avoid manufactured urgency** — add to the Epsilon layer: "Do not use artificial scarcity or false countdown language."

Activation pattern:
```
Using: evoke [EMOTION] by connecting to [BRAND VALUE]; do not use manufactured urgency or artificial scarcity.
```

---

## Placeholder Variable Syntax

Source: Wright (2025). Every prompt template must use `{{double-brace}}` placeholders for all variable inputs:

```
{{company name}}, {{prospect name}}, {{industry}}, {{product/service}}, {{tone}}, {{platform}}, {{CTA link}}
```

**Why this matters:** Prompts without placeholders are single-use. Prompts with placeholders are agency assets — reusable across every client engagement. A prompt library built with consistent `{{double-brace}}` syntax can be searched, shared, and updated systematically. Apply to all templates in this library.

---

## Hallucination Management Gate

Source: Evelyn (2025, p.51); Mizrahi (2024). For any output making factual or statistical claims, include this instruction in the prompt:

```
Use web search to find the latest news and resources, and cite your sources.
```

Every factual claim, statistic, named entity, date, or product claim in AI output must be flagged for human verification before client delivery. Do not assume AI-generated facts are correct. The hallucination gate is not optional — it is a production standard for any content that makes claims of fact.

---

## ### Separator Syntax

Source: Evelyn (2025). Any prompt containing both instructions and material to process (a brief, content to rewrite, example posts) must use triple hash marks (`###`) to separate sections. This prevents the model from confusing instructions with content to process.

Structure:
```
[Instructions here]

###

[Material to process — e.g. a brief, a draft to rewrite, example posts to learn from]

###
```

Apply whenever a prompt includes: pasted client briefs, existing copy for rewriting, competitor examples, or reference posts. Never mix instructions and source material in continuous prose.

---

## Prompting Techniques

Source: Upadhyay (2024). Apply these methods when a single prompt does not produce sufficient output quality.

**Prompt trail** — break a complex deliverable into logical steps. Validate the AI's thinking at each step before proceeding to the next. Example: generate the strategy outline first, confirm it, then ask for the full narrative.

**Multiple versions** — request three variations of the same output (e.g. "Write three versions of this caption using three different frameworks"). Review all three, then ask the AI to merge the strongest elements into a final version.

**Iterative refinement** — use precise follow-up instructions to improve a draft. Example: "Add a local Uganda example to the second paragraph" or "Shorten the CTA to under 10 words."

**Chain-of-thought** — ask the AI to walk through its reasoning before writing the final version. Example: "Before writing the caption, explain which copywriting framework you are choosing and why it suits this audience." Review the reasoning; correct it if wrong before accepting the output.

**Template approach** — when a prompt produces excellent output, save the exact prompt (with client variables noted in brackets) as a named template in the client's project folder. Name templates clearly: `caption-facebook-PAS-v1`, `email-subject-reengagement-v2`. Reuse and iterate; do not start from scratch each time.

---

## MVOSSTE Prompting Workflow (Randazzo, 2024)

Use this sequence when developing full marketing strategies with AI assistance:

| Step | Prompt focus |
|---|---|
| **Mission** | "Draft 3 mission statement options for [client] that reflect [values]…" |
| **Vision** | "Write a 5-year vision statement assuming [growth scenario]…" |
| **Objective** | "Generate 5 SMART marketing objectives for [goal] in [timeframe]…" |
| **Situation** | "Conduct a SWOT analysis for [client] in [industry] in [market]…" |
| **Strategy** | "Suggest 3 strategic options for achieving [objective], with trade-offs…" |
| **Tactics** | "List 10 specific social media tactics for [strategy] with [budget] budget…" |
| **Execution** | "Create a 30-day action plan with weekly milestones for [tactic]…" |

**Professional practice:** Footnote every AI-generated output with the exact prompt used. This enables clients to audit, reproduce, and modify outputs — and protects the consultant if outputs are later questioned.

---

## Sales Funnel Stage-Specific Prompts

Source: GPT Penguin (2024). Calibrate content prompts by buyer journey stage:

**Top-of-Funnel (Attract)** — first-time visitors; no prior relationship with the brand.
```
[BCB]
Consider the situation: {{prospect description}} has just discovered {{brand name}} for the first time. They do not know the brand. Acting as a social media copywriter for {{brand name}} writing for {{audience values description}}. Write a {{platform}} post that introduces the brand's core value proposition without selling — educate and intrigue first. In a single post of under 120 words. Using: British English; no promotional language; no price mentions; end with a curiosity question or an invitation to learn more.
```

**Middle-of-Funnel (Nurture)** — leads who have shown interest (followed, engaged, clicked).
```
[BCB]
Consider the situation: {{prospect description}} has interacted with {{brand name}} content before. They know who the brand is. Acting as a social media copywriter for {{brand name}} writing for an audience that is considering but not yet committed. Write a {{platform}} post that provides proof of value — a case study, testimonial, or behind-the-scenes detail. In a narrative post of 100–150 words. Using: British English; specific and credible detail (no vague claims); include one social proof element; end with a soft CTA: "Find out how we helped [type of client]."
```

**Bottom-of-Funnel (Decision)** — decision-stage prospects ready to act.
```
[BCB]
Consider the situation: {{prospect description}} is actively deciding whether to work with {{brand name}}. They have seen the brand before. Acting as a social media copywriter for {{brand name}} writing for a warm, ready-to-act audience. Write a {{platform}} post that makes a direct, specific offer with a clear CTA. In a concise post of under 100 words. Using: British English; one specific offer or guarantee; one frictionless CTA ("Message us on WhatsApp: {{WhatsApp link}}"); no watered-down language; genuine urgency only where a real deadline exists.
```

---

## Before/After Prompt Comparison — Social Caption

Source: Chavaux (2025). The most effective technique for making the quality gap between weak and strong prompts tangible.

**BEFORE — Weak Prompt:**
```
Write a caption for a Ugandan coffee brand.
```
*Typical output:* Generic, Western coffee-culture language. No local context. No CTA. No emotional pull.

**AFTER — Strong Prompt:**
```
[BCB for {{brand name}}, a specialty Ugandan coffee brand targeting urban Kampala professionals aged 28–42 who value locally-produced quality]

Consider the situation: It is Monday morning. Our audience is starting their working week and already thinking about productivity. Acting as a social media copywriter for {{brand name}} writing for ambitious Kampala professionals who take pride in supporting Ugandan-grown products. Write a Facebook caption using the AIDA framework (Attention → Interest → Desire → Action) that positions our coffee as the professional's daily ritual. In a single caption with a line break after the hook, body text, and CTA on a new line. Using: British English; maximum 120 words; evoke morning energy and local pride; end with a WhatsApp CTA {{WhatsApp link}}; include 3 relevant hashtags; never begin with "Are you".
```
*Typical output:* Locally grounded, emotionally resonant, framework-structured, with a clear CTA.

---

## Forward-Reasoning Strategy Prompt

Source: Wright (2025). For strategic deliverables, use this pattern to generate differentiated thinking:

```
Imagine {{client's desired future state — e.g. "{{brand name}} is the most trusted financial services brand in Kampala"}}. Work backward to identify the key decisions and unexpected moves that contributed to this success. What did the brand do differently from competitors? What risks did it take? What did it stop doing?
```

This pattern bypasses generic strategic advice and produces counter-intuitive, specific insights by anchoring the AI's reasoning at the outcome rather than the starting point. Use for strategy documents, brand positioning, and 3–5 year planning sections.

---

## Curiosity Gap Technique

Source: Wright (2025). The gap between what the reader knows and what they want to know creates click compulsion — the psychological pull that drives opens, clicks, and continued reading. Apply by naming it explicitly in the prompt:

```
Write [content type] that uses an intrigue gap to [desired response — e.g. "make the reader want to find out the answer," "compel them to open the full post," "create anticipation for the next step"].
```

The curiosity gap works by revealing enough to make the reader aware of what they do not know, then withholding the resolution until they take the desired action (click, open, reply, scroll). It is distinct from clickbait because it delivers the promised insight — it never misleads.

---

## Quality Criteria

Output from this skill meets the standard when:

1. Every prompt template strictly follows the Alpha-Beta-Gamma-Delta-Epsilon structure and is prefixed by the Brand Context Block — no exceptions.
2. Each template contains all 10 prompt components relevant to that task; components that do not apply are explicitly omitted, not left blank.
3. Prompts produce output that a client team member can use without editing the prompt itself — all variables are clearly marked in square brackets with a plain-English instruction.
4. The library covers every recurring task the client identified in the Required Input and includes at least one template per active platform.
5. All character limits, word counts, and format rules in the Epsilon layer are specific and measurable — no vague instructions such as "keep it short."
6. Uganda/East Africa context is embedded in every relevant template: correct platform hierarchy, WhatsApp CTA format, UGX income ranges, and EA cultural references where applicable.
7. The copywriting framework specified in each caption or content template is the correct match for the task's audience mindset and conversion goal, with a one-line rationale provided.
8. The completed library is delivered as a single structured markdown document, organised by task category, ready to be saved in the client's project folder and shared with their team.

---

## References

- Chavaux, L. (2025) — Before/After prompt comparison methodology.
- Erné, R. (2024) — 5-Step Perfect Prompt framework: Role, Context, Task, Format, Constraints.
- Evelyn, A. (2025) — Hallucination Management Gate; ### separator syntax; contextual continuity management.
- GPT Penguin (2024) — Prompt Anatomy five-component model; Emotional Resonance Pattern; Sales Funnel Stage-Specific Prompts.
- Joseph, P. (c.2023–2024) — PAO Matrix (Platform–Audience–Objective) pre-prompt checklist.
- Mizrahi, T. (2024) — Copywriting Formula Prompt Activation; FOMO and SMILE frameworks; hallucination management.
- Roth, J. and neuroflash (2024) — 8 Golden Rules of Prompting for AI-assisted content production.
- Upadhyay, S. (2024) *Generative AI for Marketing*. — Alpha-Beta-Gamma-Delta-Epsilon master prompt formula; 10 prompt components; prompting techniques.
- Randazzo, C. (2024) — MVOSSTE prompting workflow for AI-assisted marketing strategy development.
- Wright, D. (2025) — Placeholder Variable Syntax; Forward-Reasoning Strategy Prompt; Curiosity Gap technique.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. — RACE framework; POEM model; audience segmentation.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. — 10-4-1 content rule; ROI formula.
