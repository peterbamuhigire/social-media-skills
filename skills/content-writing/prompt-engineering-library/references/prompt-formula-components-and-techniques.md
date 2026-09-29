# Prompt formula, components and techniques

Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`); text unchanged apart from three headings renamed (separator syntax, full quality criteria, sources). Citations corrected afterwards per D-SK-10c (Chaffey and Ellis-Chadwick 2022; Ltifi 2024; see evidence/S09/citation-verification.md). Read when asking the intake questions, applying the Alpha-Beta-Gamma-Delta-Epsilon master formula, the 10 prompt components, the copywriting style frameworks, the PAO matrix, the hallucination gate, separator and placeholder syntax, prompting techniques, MVOSSTE, or checking a source citation.

## Evidence-first prompt standard

The frameworks and formulas below are optional drafting aids, not universal quality guarantees. Every reusable prompt must make the outcome, audience, trusted context/source boundary, required content, hard constraints and non-goals, output shape, and acceptance or fallback rule visible. Use a framework only when it clarifies a material requirement. Test a baseline and one changed version on representative fixtures, inspect factuality, safety, accessibility and failure slices, and record the version, adapter/model, evaluator, result, cost/latency effect and rollback path. Current platform, model, pricing, policy and performance claims require a current verified source; otherwise remove or label them `NOT_ASSESSED`.

## Required Input
Before generating the library, ask for:

1. **Client business name** — exact trading name
2. **Industry** — sector and sub-sector (e.g. financial services / SACCO)
3. **Country/City** — defaults to Uganda/Kampala if not specified
4. **Primary goal** — the main business objective this library will serve (e.g. lead generation, brand awareness, community growth)
5. **Brand Context Block** — paste the output from `brand-voice-ai-training`, or provide: brand voice descriptors, banned vocabulary, audience description, and primary WhatsApp number
6. **Active platforms** — list the platforms the client publishes on
7. **Priority tasks** — which recurring tasks the team performs most often (captions, blogs, reports, etc.)

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

## PAO Matrix — Pre-Prompt Checklist
Source: Joseph (c.2023–2024). Before writing any social media content prompt, confirm all three parameters simultaneously:

- **Platform** — which platform is this content for? (Each platform has different norms, formats, and audience expectations.)
- **Audience** — who specifically is this for, defined by values and mindset, not just demographics? (e.g. "first-generation entrepreneurs who value financial independence" not "25–40-year-olds")
- **Objective** — what is the specific objective? Choose one: awareness / engagement / conversion / retention.

Omitting any one parameter forces the AI to make assumptions that produce generic output. All three must appear explicitly in every social media content prompt, in the Alpha and Beta elements of the master formula.

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

## Emotional Resonance Pattern
Source: GPT Penguin (2024). Human-sounding copy requires explicit emotional instruction. Every prompt for brand content must specify:

1. **The emotion to evoke** — trust, urgency, nostalgia, excitement, relief, pride, curiosity. Name it explicitly.
2. **The brand value to connect it to** — e.g. "connect the urgency to the brand's commitment to making financial services accessible."
3. **The instruction to avoid manufactured urgency** — add to the Epsilon layer: "Do not use artificial scarcity or false countdown language."

Activation pattern:
```
Using: evoke [EMOTION] by connecting to [BRAND VALUE]; do not use manufactured urgency or artificial scarcity.
```

## Placeholder Variable Syntax
Source: Wright (2025). Every prompt template must use `{{double-brace}}` placeholders for all variable inputs:

```
{{company name}}, {{prospect name}}, {{industry}}, {{product/service}}, {{tone}}, {{platform}}, {{CTA link}}
```

**Why this matters:** Prompts without placeholders are single-use. Prompts with placeholders are agency assets — reusable across every client engagement. A prompt library built with consistent `{{double-brace}}` syntax can be searched, shared, and updated systematically. Apply to all templates in this library.

## Hallucination Management Gate
Source: Evelyn (2025, p.51); Mizrahi (2024). For any output making factual or statistical claims, include this instruction in the prompt:

```
Use an authorised current source or the Digital Research Engine's verified evidence record for claims that depend on current news, rules, platform behaviour, prices, products, or named entities; cite the source and preserve the verification date.
```

Every factual claim, statistic, named entity, date, or product claim in AI output must be flagged for human verification before client delivery. Do not assume AI-generated facts are correct. The hallucination gate is not optional — it is a production standard for any content that makes claims of fact.

## Separator Syntax (`###`)
Source: Evelyn (2025). Any prompt containing both instructions and material to process (a brief, content to rewrite, example posts) must use triple hash marks (`###`) to separate sections. This prevents the model from confusing instructions with content to process.

Structure:
```
[Instructions here]

###

[Material to process — e.g. a brief, a draft to rewrite, example posts to learn from]
###
```
Apply whenever a prompt includes: pasted client briefs, existing copy for rewriting, competitor examples, or reference posts. Never mix instructions and source material in continuous prose.

## Prompting Techniques
Source: Upadhyay (2024). Apply these methods when a single prompt does not produce sufficient output quality.

### Evidence-first qualification

Use these techniques only when a baseline comparison on representative fixtures shows a material benefit. For reasoning-heavy work, request concise assumptions, criteria, trade-offs, checks, and unresolved gaps rather than requiring private chain-of-thought disclosure. Record prompt version, source boundary, adapter/model, evaluator, result, cost/latency effect, and rollback path when the prompt is reused in production. Frameworks, example counts, separators, and provider parameters remain optional and adapter-scoped.

**Prompt trail** — break a complex deliverable into logical steps. Validate the AI's thinking at each step before proceeding to the next. Example: generate the strategy outline first, confirm it, then ask for the full narrative.

**Multiple versions** — request three variations of the same output (e.g. "Write three versions of this caption using three different frameworks"). Review all three, then ask the AI to merge the strongest elements into a final version.

**Iterative refinement** — use precise follow-up instructions to improve a draft. Example: "Add a local Uganda example to the second paragraph" or "Shorten the CTA to under 10 words."

**Chain-of-thought** — ask the AI to walk through its reasoning before writing the final version. Example: "Before writing the caption, explain which copywriting framework you are choosing and why it suits this audience." Review the reasoning; correct it if wrong before accepting the output.

**Template approach** — when a prompt produces excellent output, save the exact prompt (with client variables noted in brackets) as a named template in the client's project folder. Name templates clearly: `caption-facebook-PAS-v1`, `email-subject-reengagement-v2`. Reuse and iterate; do not start from scratch each time.

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

## Forward-Reasoning Strategy Prompt
Source: Wright (2025). For strategic deliverables, use this pattern to generate differentiated thinking:

```
Imagine {{client's desired future state — e.g. "{{brand name}} is the most trusted financial services brand in Kampala"}}. Work backward to identify the key decisions and unexpected moves that contributed to this success. What did the brand do differently from competitors? What risks did it take? What did it stop doing?
```

This pattern bypasses generic strategic advice and produces counter-intuitive, specific insights by anchoring the AI's reasoning at the outcome rather than the starting point. Use for strategy documents, brand positioning, and 3–5 year planning sections.

## Curiosity Gap Technique
Source: Wright (2025). The gap between what the reader knows and what they want to know creates click compulsion — the psychological pull that drives opens, clicks, and continued reading. Apply by naming it explicitly in the prompt:

```
Write [content type] that uses an intrigue gap to [desired response — e.g. "make the reader want to find out the answer," "compel them to open the full post," "create anticipation for the next step"].
```

The curiosity gap works by revealing enough to make the reader aware of what they do not know, then withholding the resolution until they take the desired action (click, open, reply, scroll). It is distinct from clickbait because it delivers the promised insight — it never misleads.

## Quality Criteria (full list)
Output from this skill meets the standard when:

1. Every prompt template strictly follows the Alpha-Beta-Gamma-Delta-Epsilon structure and is prefixed by the Brand Context Block — no exceptions.
2. Each template contains all 10 prompt components relevant to that task; components that do not apply are explicitly omitted, not left blank.
3. Prompts produce output that a client team member can use without editing the prompt itself — all variables are clearly marked in square brackets with a plain-English instruction.
4. The library covers every recurring task the client identified in the Required Input and includes at least one template per active platform.
5. All character limits, word counts, and format rules in the Epsilon layer are specific and measurable — no vague instructions such as "keep it short."
6. Uganda/East Africa context is embedded in every relevant template: correct platform hierarchy, WhatsApp CTA format, UGX income ranges, and EA cultural references where applicable.
7. The copywriting framework specified in each caption or content template is the correct match for the task's audience mindset and conversion goal, with a one-line rationale provided.
8. The completed library is delivered as a single structured markdown document, organised by task category, ready to be saved in the client's project folder and shared with their team.

## Sources
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
- Chaffey, D. and Ellis-Chadwick, F. (2022) *Digital Marketing: Strategy, Implementation and Practice*. 8th edn. Harlow: Pearson. — RACE framework; POEM model; audience segmentation.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. — 10-4-1 content rule; ROI formula.
