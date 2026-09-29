# Prompt-Writing Module: AI Prompt Writing for Marketing Teams

Merged from skills/training/training-ai-prompt-writing on 2026-09-29 at 69cca10 (S06 tree); preservation map: [training-ai-prompt-writing.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/training-ai-prompt-writing.md)

## When to use this reference

The parent [SKILL.md](../SKILL.md) delivers AI Foundations: literacy, safe use and limits for teams new to AI. This reference is the follow-on session. Use it when:

- learners already understand basic AI limits and now need repeatable prompting practice for marketing work;
- the client asks for prompt-writing training, prompt construction and critique, or copywriting frameworks inside prompts;
- a team produces captions, emails, blogs, WhatsApp broadcasts, SMS or ad copy with AI tools and the output is generic.

Deliver it after AI Foundations. If learners lack a shared AI mental model, teach the parent's foundations modules first; prompt recipes without that grounding create confidence without judgement.

The output is a complete, facilitator-ready training guide in four modules, not a slide deck. This repository has no active standalone slide-deck route; if slides are commissioned, hand the approved content to [chwezi-design-engine](https://github.com/peterbamuhigire/chwezi-design-engine).

## Inputs

Ask for these before generating the guide (in addition to the parent's required input):

- **Client business name and industry**: trading name and sector (for example telecoms, microfinance, FMCG, hospitality).
- **Country / city**: default Uganda / East Africa.
- **Primary goal**: what the client wants the team to achieve after training.
- **Team size and prior AI experience level**: number of participants and experience (none / basic / intermediate).
- **Primary content types produced**: captions, emails, blogs, WhatsApp broadcasts, SMS, ad copy and so on.
- **Preferred AI tools**: ChatGPT, Gemini, Claude or other (specify versions where known; tool names, tiers and model versions change, so verify before stating them as current, no register record).
- **Training format**: in-person half-day / virtual session / self-guided handout.

## Decision rules

| # | Condition | Action | Failure avoided |
|---|---|---|---|
| 1 | Learners understand basic AI limits and need repeatable prompting practice | Use worked exercises with human review and verified facts | Participants copy prompts without checking outputs |
| 2 | Learners have no shared AI mental model yet | Run the parent's foundations modules first, then this module | Prompt recipes without judgement |
| 3 | An exercise asks the AI for a statistic, price or platform fact | Supply the verified figure in the Beta (context) element; never let the AI invent it | Invented numbers reaching published copy |
| 4 | A prompt change looks better on one example | Keep it only if it survives the evidence-first test below | Anecdotal "improvements" that fail on real content |

## Evidence-first prompt practice

Teach frameworks as optional memory aids, not laws. Every exercise should identify:

- the outcome;
- the audience;
- the trusted context and source boundary;
- the required content;
- hard constraints;
- the output shape;
- the acceptance or fallback rule.

Test a baseline prompt and one changed prompt on a small representative set, inspect the failure slices, and keep a change only when the improvement survives factuality, safety, accessibility, cost, latency and approval checks. Current platform, model, policy, pricing and performance claims need a current verified source; otherwise mark them `NOT_ASSESSED`.

## Procedure

1. Collect the inputs above. Confirm the team has completed, or does not need, the AI Foundations session.
2. Write the Training Overview block (below), filling every bracketed placeholder.
3. Generate the four modules in full, using the client's name, industry, preferred AI tools and primary content types throughout. Plain English, no jargon; tone practical, encouraging and professional.
   - Modules 1 and 2: load [prompt-foundations-and-structure.md](prompt-foundations-and-structure.md) (why prompt quality matters; the Alpha-Beta-Gamma-Delta-Epsilon framework, the 10 prompt components, common mistakes, the build-your-own-prompt activity).
   - Modules 3 and 4: load [copy-frameworks-and-practice.md](copy-frameworks-and-practice.md) (the seven copywriting frameworks in the Gamma element; the prompt library, prompting approaches, iterative refinement, the AI content quality checklist, East African context notes, the eight prompt types, examples-first few-shot method, worked prompt examples).
4. Apply the evidence-first practice rules to every exercise.
5. Check the guide against the release checklist, then apply `ai-marketing/anti-ai-slop` and block release on an F from `ai-marketing/ai-slop-audit`.

## Template: Training Overview

```
Programme: AI Prompt Writing for Marketing Teams
Total duration: approximately 2.5 hours (150 minutes)
Audience: marketing, communications and content staff with any level of AI experience
Format: [Insert training format]
Prepared for: [Client Business Name]
Industry: [Industry]
Primary sources: Upadhyay (2024) Generative AI for Marketing; Anderson (2022) AI in Digital Marketing Training Guide
```

Module timing (totals 150 minutes):

| Module | Title | Minutes | Hands-on activity |
|---|---|---|---|
| 1 | Why Prompt Quality Matters | 30 | Live GIGO demonstration and discussion |
| 2 | The Alpha-Beta-Gamma-Delta-Epsilon Framework | 45 | 15-minute build-your-own-prompt activity |
| 3 | Copywriting Frameworks in Prompts | 45 | 20-minute PAS caption and AIDA subject-line exercises |
| 4 | Practical Prompt Library and Iterative Refinement | 30 | Live three-prompt refinement; few-shot voice exercise |

## Currentness notes

- Instagram hashtag counts: the worked examples ask for 2–3 hashtags, within Instagram's five-hashtag cap on posts and Reels (register INSTAGRAM-HASHTAG-LIMIT-PRIMARY; rollout to every account NOT_ASSESSED).
- Character guidance in the moved modules (captions under 150 characters, SMS under 160, subject lines under 50) is house practice, not platform rule: verify before stating as a platform limit (no register record).
- Model and tool behaviour (ChatGPT, Gemini, Claude) changes often: verify before stating features, tiers or versions as current (no register record).

## Release checklist

The completed training guide meets the standard if:

- [ ] All four modules are included with time allocations totalling approximately 2.5 hours.
- [ ] The Alpha-Beta-Gamma-Delta-Epsilon framework is explained in full, with at least one complete worked example per element.
- [ ] All seven copywriting frameworks are named, defined and illustrated with a Uganda/East Africa brand example.
- [ ] Hands-on activities are specified in Modules 2, 3 and 4, not lecture content only.
- [ ] All worked examples use Ugandan/East African brands, UGX pricing and local cultural references where relevant.
- [ ] The guide is structured so a non-technical facilitator can deliver it without additional preparation.
- [ ] The `prompt-engineering-library` and `anti-ai-slop` (humanising rewrite passes) skills are explicitly referenced as companion resources.
- [ ] The guide is written in British English with imperative language throughout.

## Companion skills

- `content-writing/prompt-engineering-library`: ready-made prompt templates used in Module 4.
- `ai-marketing/anti-ai-slop`: humanising rewrite passes and the full quality checklist used in Module 4.
- `ai-marketing/brand-voice-ai-training`: training AI tools on a specific brand voice (extends the few-shot method).

## Sources

- Upadhyay, M.A. (2024) *Generative AI for Marketing*, Packt.
- Anderson, D. (2022) *AI in Digital Marketing Training Guide*, self-published.
