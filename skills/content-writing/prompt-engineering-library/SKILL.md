---
name: prompt-engineering-library
description: Use when a team wants reusable AI prompts for marketing work across text, image, voice, video and music tools; produces a prompt library with fill-in templates by task, Midjourney, DALL-E and Firefly image prompts with negative prompts, and ElevenLabs, HeyGen and Suno prompts; not for teaching staff to use AI (use `training-ai-foundations`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Prompt Engineering Library

Builds a reusable, tested prompt library for a client team: fill-in text templates by task, image prompts with negative prompts, and voice, avatar video and music prompts with consent and disclosure checks.

<!-- dual-compat-start -->
## Use When
- Our team gets bland or made-up answers from ChatGPT or Claude and wants tested prompt templates for captions, blog briefs, emails, personas and reports.
- We need prompts built per job role, or engagement questions that invite audience replies.
- We need AI image prompts for Midjourney, DALL-E or Firefly with negative prompts, seeds and accurate East African people and settings.
- The campaign needs prompts for voice-overs, avatar videos and music in tools such as ElevenLabs, HeyGen and Suno, with consent and disclosure checks.

## Do Not Use When
- `training-ai-foundations` for teaching beginners AI literacy and prompt writing in workshops.
- `brand-voice-ai-training` for training an AI on the brand voice or building a brand knowledge base.
- `caption-writer` for the finished captions themselves.
- Stop before generating a real person's likeness or voice without written consent, and label AI-generated media where platforms or law require it.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name (exact trading name), industry and sub-sector (for example financial services / SACCO), country/city | Client brief | Yes | Default to Uganda/Kampala; ask for the trading name and sub-sector. |
| Primary goal the library serves (for example lead generation, brand awareness, community growth) | Client lead | Yes | Stop and ask; templates cannot be calibrated without it. |
| Brand Context Block: brand voice descriptors, banned vocabulary, audience description and primary WhatsApp number | `brand-voice-ai-training` output or client | Yes | Build a provisional block from the supplied voice notes and mark it for client approval. |
| Active platforms and priority recurring tasks (captions, blogs, reports, etc.) | Client team | Yes | Cover captions, email subject lines and community responses for Facebook and WhatsApp, labelled provisional. |
| Representative fixtures (sample briefs and past outputs) for baseline testing | Client team | No | Deliver untested templates marked `NOT_ASSESSED` for effectiveness. |
| Written consent for any real person's likeness or voice, and the disclosure rules that apply | Client; talent; platform policy | Conditional | Exclude likeness and voice prompts for that person. |

The full intake list is in [prompt formula, components and techniques](references/prompt-formula-components-and-techniques.md#required-input).

## Workflow

1. Confirm the goal, platforms, priority tasks and approval boundary; route to `training-ai-foundations` for teaching staff or to `brand-voice-ai-training` for the brand knowledge base. Stop if the Brand Context Block, goal or active platforms are unknowable.
2. Run the PAO matrix (platform, audience by values and mindset, one objective) for every social content task.
3. Write each template on the Alpha-Beta-Gamma-Delta-Epsilon master formula (Upadhyay, 2024), prefixed by the Brand Context Block, drawing on the 10 prompt components and naming the copywriting framework (PAS, AIDA, BAB, FAB, SSS, PPPP, AFOREST, FOMO, SMILE) with a one-line rationale.
4. Use `{{double-brace}}` placeholders for every variable, `###` separators wherever instructions sit beside pasted material, an explicit emotion tied to a brand value, and the hallucination management gate for any factual output.
5. Add the media sections the client needs: image prompts with the eight-layer anatomy, negative prompts, seed record and East African cultural review; voice-over, podcast, avatar video and music prompts with the disclosure table and production record; role packs and engagement question banks.
6. Test a baseline and one changed version on representative fixtures; inspect factuality, safety, accessibility and failure slices; record version, adapter/model, evaluator, result, cost/latency effect and rollback path. Correct any failing template and rerun the test.
7. Label or remove every current platform, model, pricing, policy or performance claim without a current verified source (`NOT_ASSESSED`), then deliver one structured markdown document organised by task category, with each template named (for example `caption-facebook-PAS-v1`).

## Master formula at a glance

```
[Brand Context Block]

Consider the situation [Alpha — context and situation: what is happening, why it matters now].
Acting as [Beta — the creator persona AND a description of the target audience].
Perform [Gamma — the specific task to be completed].
In [Delta — the output format: caption, table, document, bullet list].
Using [Epsilon — boundaries, tone, style, length, platform rules, hard constraints].
```

Frameworks and formulas are optional drafting aids, not universal quality guarantees: every reusable prompt must make the outcome, audience, trusted context/source boundary, required content, hard constraints and non-goals, output shape, and acceptance or fallback rule visible.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Text prompt library organised by task category | Client content team | At least one template per active platform and one per priority task; every variable in `{{double-brace}}` or square brackets with a plain-English instruction. |
| Image prompt set with negative prompts and seed record | Designer or image generation operator | Eight-layer anatomy applied; East African people and settings reviewed for cultural accuracy. |
| Voice, avatar video and music prompt set with disclosure table | Production team | Consent recorded for every real likeness or voice; disclosure label named per platform. |
| Role prompt packs and engagement question banks, when requested | Team leads; community manager | Organised by job role; questions invite genuine replies. |
| Prompt test and version log | Client AI owner | Baseline versus changed version recorded with rollback path. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Prompt test record | Table: template, version, adapter/model, fixtures, evaluator, result, cost/latency, rollback | Every production template has a row or is marked `NOT_ASSESSED`. |
| Claim verification register | Table | Every current platform, model, price or policy claim has a dated source or is removed. |
| Consent and disclosure log | Table per likeness, voice or synthetic medium | Written consent and the disclosure rule are on record before generation. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Generating a real person's likeness or voice needs their written consent, and AI-generated media must be labelled where platforms or law require it.

## Degraded Mode

Without the Brand Context Block or representative fixtures, return the narrowest qualified result and mark the affected checks `not assessed`. Formula-compliant templates with placeholder brand fields can still be delivered, labelled untested.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The library needs AI image prompts (Midjourney, DALL-E 3, Stable Diffusion, Flux, Firefly) | Build them with the eight-layer anatomy, negative prompts, seed record and East African cultural review in `references/image-prompt-patterns.md`. | Generic AI imagery or culturally inaccurate depiction. |
| The library needs voice-over, podcast, avatar video or music prompts | Use the per-medium templates, disclosure table and production record in `references/image-audio-video-prompt-library.md`. | Robotic audio, stilted avatar video, thin music or undisclosed synthetic media. |
| A prompt asks for factual or statistical claims | Add the hallucination management gate and flag every claim for human verification before delivery. | Invented facts reaching the client. |
| A prompt mixes instructions with pasted briefs, drafts or examples | Separate them with `###` markers. | The model confusing instructions with material to process. |
| A prompting technique (prompt trail, multiple versions, chain-of-thought, iterative refinement) is proposed for production | Keep it only if a baseline comparison on representative fixtures shows a material benefit; ask for concise assumptions and checks rather than private chain-of-thought. | Ritual prompting with unmeasured cost. |
| A platform, model, pricing, policy or performance claim lacks a current verified source | Remove it or label it `NOT_ASSESSED`. | Stale tool advice presented as fact. |
| A prompt would generate a real person's likeness or voice | Stop until written consent is recorded. | Deepfake liability and reputational harm. |
| A prompt produces image, video, voice or avatar output that will run as an ad or post | Add the disclosure line to the prompt record: threshold met or not under the risk-based table, label wording ("AI-generated", or "AI-generated voice" for audio) and C2PA status, per [AI transparency and provenance](../../policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md#3-risk-based-disclosure-decision-table) (register `IAB-AI-DISCLOSURE-V2-2026`). | High-volume AI creative published without a labelling decision. |

## Quality Standards

- Every template follows the Alpha-Beta-Gamma-Delta-Epsilon structure and is prefixed by the Brand Context Block, with no exceptions.
- Each template uses the relevant of the 10 prompt components; components that do not apply are explicitly omitted, not left blank.
- A client team member can use each prompt without editing it; all variables are clearly marked.
- The library covers every recurring task the client identified and at least one template per active platform.
- All character limits, word counts and format rules in the Epsilon layer are specific and measurable; no "keep it short".
- Uganda/East Africa context is embedded where relevant: correct platform hierarchy, WhatsApp CTA format, UGX income ranges and EA cultural references.
- Each caption or content template names the correct copywriting framework for the audience mindset and conversion goal, with a one-line rationale.
- Delivered as a single structured markdown document organised by task category, footnoting AI-generated outputs with the exact prompt used.

## Anti-Patterns

- Describing the structure in prose ("make it compelling and build to a call to action"). Fix: name the formula directly (for example "using the PAS framework (Problem → Agitate → Solve)").
- Single-use prompts without placeholders. Fix: use consistent `{{double-brace}}` variables so the prompt becomes a reusable agency asset.
- Omitting platform, audience or objective. Fix: run the PAO matrix and place all three in the Alpha and Beta elements.
- Assuming AI-generated facts are correct. Fix: apply the hallucination gate and verify every fact before delivery.
- Manufactured urgency or artificial scarcity in prompts. Fix: add "do not use manufactured urgency or artificial scarcity" to the Epsilon layer.
- Western-market defaults in persona, strategy or image prompts. Fix: specify realistic Uganda/East Africa demographics, UGX ranges and settings.
- Generating a real person's likeness or voice, or unlabelled synthetic media. Fix: obtain written consent and apply the disclosure table.

## References

- [Prompt formula, components and techniques](references/prompt-formula-components-and-techniques.md): read when applying the master formula, 10 components, style frameworks, PAO matrix, prompt anatomy, formula activation, emotional resonance, placeholder and separator syntax, hallucination gate, prompting techniques, MVOSSTE, forward-reasoning or curiosity gap patterns, or checking a source citation.
- [Text prompt templates by task](references/text-prompt-templates-by-task.md): read when building caption, blog brief, email subject line, persona, platform selection, community response, report narrative or funnel-stage prompts, or showing the before/after comparison.
- [Image prompt patterns](references/image-prompt-patterns.md): read when the library must include AI image prompts (eight-layer anatomy, negative prompts, platform syntax, cultural accuracy review).
- [Image, audio and video prompt library](references/image-audio-video-prompt-library.md): read when the library must cover voice-over, podcast, avatar or personalised video, or music prompts and AI media disclosure.
- [AI transparency and provenance](../../policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md): read when deciding whether prompt output needs an AI label, and which platform label rules (Meta "AI info", TikTok) apply.
- [Role prompt packs and engagement question banks](references/role-prompt-packs-and-engagement-questions.md): read when building prompts per job role or audience questions that invite replies.
- [Team prompt operating system](references/team-prompt-operating-system.md): read when turning client prompts into managed team assets.
- [`caption-writer`](../caption-writer/SKILL.md): read when the client wants finished captions rather than prompts.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when reviewing AI output produced with these prompts.
- [Repository agent guide](../../../AGENTS.md): read when a prompt raises a consent, disclosure or market-safety question covered by the engine-wide gates.
<!-- dual-compat-end -->
