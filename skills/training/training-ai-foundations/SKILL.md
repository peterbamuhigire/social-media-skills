---
name: training-ai-foundations
description: 'Use when a marketing team is new to ChatGPT, Claude or Gemini and needs training: what AI can and cannot do, safe use of client data, checking outputs, and a follow-on prompt-writing workshop; produces the AI training guide with supervised exercises; not for a reusable prompt template library (use `prompt-engineering-library`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Foundations for Marketing Teams — Training Guide

Produces a facilitator-ready, four-module AI literacy guide (about 150 minutes) that frames AI as augmented intelligence and ends with supervised practice; the prompt-writing workshop follows as a second session.

<!-- dual-compat-start -->
## Use When

- Staff are using AI tools without guidance and need a beginner session on how they work, their limits and hallucinations.
- We need rules for safe use: client confidentiality, Uganda DPPA 2019 personal data, disclosure and human review.
- A team that knows the basics needs a hands-on prompt-writing workshop using the Alpha-Beta-Gamma-Delta-Epsilon structure and PAS and AIDA copy frameworks.
- Managers want supervised practice and proof that trainees can critique and improve prompts.

## Do Not Use When

- `prompt-engineering-library` for a reusable library of text, image, audio and video prompt templates.
- `training-client-team` for a social-media handover workshop or DIY content handbook.
- `policy-ai-content-ethics` for the organisation's AI content policy.
- Stop before exercises put real client personal data into public AI tools; use synthetic examples instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name, industry, country/city and primary goal | Client lead | Yes | Default to Uganda / East Africa; ask for the goal and hold the guide until it is stated. |
| Team size and prior AI experience (none / basic / intermediate) | Client lead or pre-session survey | Yes | Assume no experience and deliver foundations before any prompt-writing module. |
| Primary platforms used (e.g. Facebook, Instagram, WhatsApp) | Client lead | Yes | Use Facebook, Instagram and WhatsApp and label the platform table provisional. |
| Training format and time available (2-hour express / half-day / 4 weekly sessions) | Client lead | Yes | Plan the 150-minute half-day and mark cuts for a 2-hour express. |
| Tool access: Android, free tier, 3G connection for the five hands-on tools | Facilitator check before the session | Yes | Mark unverified tools `not assessed` and run those segments as demonstrations. |
| Synthetic practice material (no real client personal data) | Facilitator | Yes | Write synthetic briefs; never paste client personal data into public tools. |

## Workflow

1. Run the intake in [training-guide-plan.md](references/training-guide-plan.md) and decide whether the team needs foundations, the prompt-writing follow-on module, or both in sequence.
2. Verify tool access (Android, free tier, 3G) and prepare synthetic exercise material; stop before any exercise would put real client personal data into a public AI tool.
3. Write the Training Overview block with the four sources, then open with the augmented-intelligence frame and junior assistant analogy from [foundations-and-limits.md](references/foundations-and-limits.md).
4. Generate Modules 1–2 (what AI is; what it can and cannot do, with the EA platform table) from [foundations-and-limits.md](references/foundations-and-limits.md), adding the Co-Pilot vs Co-Thinker and Three Waves segments.
5. Generate Modules 3–4 (five hands-on tools; the human quality standard) and the exercises summary from [tools-and-human-review.md](references/tools-and-human-review.md).
6. If the team is ready, schedule the follow-on session from [prompt-writing-module.md](references/prompt-writing-module.md) after this guide, never before it.
7. Check the guide against the Quality Standards, apply `anti-ai-slop` and block release on an F from `ai-slop-audit`; correct any failing section and rerun the affected check before hand-off to the facilitator.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Facilitator-ready training guide, four modules, about 150 minutes | Client facilitator or marketing manager | A non-technical manager can run it without extra preparation; client name, industry, platforms and city appear throughout. |
| Supervised exercise set (Co-Pilot/Co-Thinker audit, Three Waves, tool practice, 3-step edit) | Trainees and facilitator | Each exercise uses synthetic or approved material and has a stated debrief question. |
| Follow-on prompt-writing session plan (when chosen) | Facilitator | Scheduled after foundations and built from the prompt-writing module. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Tool-access check | Table: tool, Android, free tier, 3G, date checked | Every hands-on tool is verified or marked `not assessed`. |
| Trainee critique record | Before/after prompt or edited output per trainee | Shows each trainee critiqued and improved an output using the 3-step edit. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Exercises use synthetic data; any use of client data in AI tools needs a Uganda DPPA 2019 check and client sign-off.

## Degraded Mode

Without confirmed team experience level and tool access, return the narrowest qualified result and mark the affected checks `not assessed`. The augmented-intelligence frame, Modules 1–2 and the human quality standard can still be delivered as a classroom session without live tools.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Learners lack a shared AI mental model | Teach literacy and risk before prompt technique | Prompt recipes create confidence without judgement |
| Learners understand basic AI limits and need repeatable prompting practice | Deliver the prompt-writing module from [prompt-writing-module.md](references/prompt-writing-module.md) with worked exercises, human review and verified facts | Participants copy prompts without checking outputs |
| An exercise would use real client or customer personal data | Replace it with synthetic data; escalate any real-data use for DPPA 2019 review | Personal data leaked into public AI tools |
| A hands-on tool fails on Android, free tier or 3G | Swap to a demonstration or a lighter alternative and note bandwidth guidance | A session stalled by access the team does not have |
| The client asks for a tool, feature or tier claim to be stated as current | Verify it on the date of training or mark it `not assessed`; the guide teaches judgement, not a tool catalogue | Out-of-date AI tool claims taught as fact |
| The client wants trainees to publish AI drafts during the session | Keep outputs as reviewed drafts; publishing needs the approval rule and client authority | Unreviewed AI copy on live client accounts |

## Quality Standards

- Augmented intelligence framing is used consistently throughout (AI assists humans, it does not replace them); the junior assistant analogy is included.
- All three AI types (Mechanical / Thinking / Feeling) are explained with Uganda/East Africa marketing examples.
- The "What AI cannot do" section is specific and EA-calibrated, not a generic global list; Luganda/Swahili limitations and cultural intelligence gaps are named explicitly.
- All 5 hands-on tools (ChatGPT, Gemini, Canva, FeedHive, Otter.ai) are verified as accessible on Android, free tier, and 3G connection; bandwidth guidance is included.
- The human quality standard section includes the banned vocabulary list, the 5 signs of AI text, and the 3-step edit process.
- Platform AI applications are presented as a table with EA-specific notes per channel, not a single generic list.
- Output is structured so a non-technical marketing manager can facilitate the session without additional preparation.
- British English spelling throughout; imperative language used in all instructions; Uganda/East Africa, EAT, UGX and WhatsApp-first assumptions stated where they apply.

## Anti-Patterns

- Teaching prompt recipes before the team shares a mental model of AI limits. Fix: run foundations first and schedule the prompt-writing module after it.
- Using real customer lists or client files in live exercises. Fix: use synthetic briefs and keep real-data use behind a DPPA 2019 check.
- Presenting a generic global "what AI cannot do" list. Fix: name Luganda/Swahili limits and local cultural intelligence gaps.
- Assuming every trainee has a laptop, paid tier and fast connection. Fix: verify Android, free tier and 3G access and plan demonstrations as a fallback.
- Treating the Co-Pilot mode as the whole of AI use. Fix: run the Co-Pilot vs Co-Thinker audit so the team practises thought-partner work.
- Letting AI output go out unread because it "looks fine". Fix: teach the 3-step edit and the approval rule, and record each trainee's edited output.

## References

- [training-guide-plan.md](references/training-guide-plan.md): read when running intake, writing the Training Overview block or teaching Co-Pilot/Co-Thinker and the Three Waves.
- [foundations-and-limits.md](references/foundations-and-limits.md): read when writing the core frame and Modules 1–2.
- [tools-and-human-review.md](references/tools-and-human-review.md): read when writing Modules 3–4, the banned vocabulary and the exercises summary.
- [prompt-writing-module.md](references/prompt-writing-module.md): read when the team needs the follow-on prompt-writing session (Alpha-Beta-Gamma-Delta-Epsilon, copywriting frameworks, iterative refinement); it routes to [prompt-foundations-and-structure.md](references/prompt-foundations-and-structure.md) and [copy-frameworks-and-practice.md](references/copy-frameworks-and-practice.md).
- [prompt-foundations-and-structure.md](references/prompt-foundations-and-structure.md): read when writing prompt-writing Modules 1–2.
- [copy-frameworks-and-practice.md](references/copy-frameworks-and-practice.md): read when writing prompt-writing Modules 3–4 and worked prompt examples.
- [AI transparency and provenance](../../policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md): read when teaching when AI output must be labelled, how platform AI labels work and who is accountable for AI output.
- [Certification and competency register](../../playbooks/playbook-agency-operations/references/certification-and-competency-register.md): read when recording AI training or pointing trainees to Meta's AI and Performance Marketing badge.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md): read when teaching humanising rewrite passes, the editing checklist and banned vocabulary.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read when scoring the finished training guide before release.
- [`brand-voice-ai-training`](../../ai-marketing/brand-voice-ai-training/SKILL.md): read when the team must train AI tools on a specific brand voice.
- [`prompt-engineering-library`](../../content-writing/prompt-engineering-library/SKILL.md): read when trainees need ready-made prompt templates for common marketing content types.
- [`training-client-team`](../training-client-team/SKILL.md): read when the team needs general social media training for content creation and community management.
- [AGENTS.md](../../../AGENTS.md): read when checking repository-wide doctrine.
<!-- dual-compat-end -->
