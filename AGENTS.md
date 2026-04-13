# social-media-skills Agent Guide

## Purpose

This repository is a dual-compatible skills system for professional social media and digital marketing consultancy work in Uganda and East Africa. It must continue to work for Claude Code while also being directly usable by Codex without moving skills into a different folder structure.

The portable unit is the skill directory:

```text
[skill-name]/
  SKILL.md
  references/   # optional
  scripts/      # optional
  assets/       # optional
```

Treat every top-level directory containing `SKILL.md` as a skill. Do not assume a `skills/` parent folder exists or is required.

## Default Context

- Market: Uganda / East Africa unless the user specifies another market
- Language: British English
- Currency: UGX by default
- Timezone: EAT (UTC+3)
- Channel reality: WhatsApp-first, then Facebook/Instagram/TikTok/YouTube/LinkedIn/X depending on audience

## Baseline Skills

Apply these alongside the main deliverable skill when relevant:

- `east-african-english`: tone, register, British spelling, EA business phrasing
- `language-standards`: multilingual standards where English, French, or Kiswahili output is required
- `content-writing`: readability, headlines, persuasion, scannability
- `skill-writing`: authoring or revising skills in this repository
- `skill-safety-audit`: safety review for imported or substantially changed skills

## Routing Rules

Use the skill whose directory name and `description` most closely match the deliverable. Prefixes matter:

- `biz-dev-`: credentials, proposals, pricing, outreach, practitioner positioning
- `00-` to `04-`: intake and onboarding
- `05-` to `09-`: strategy
- `10-` to `13-`: planning
- `platform-`: platform-specific plans
- `playbook-`: execution SOPs and operating playbooks
- `deck-`: slide-by-slide presentation outlines
- `meta-`: audits, measurement, analytics, models, reporting
- `training-`: client team training guides
- `policy-`: internal or client-facing policy documents
- `ai-`, `brand-voice-`, `prompt-`: AI strategy, prompting, automation, evaluation
- `caption-writer`, `email-copywriter`, `blog-writer`, `content-ideas`, `hashtag-strategy`: direct content generation
- `framework-`, `peso-`, `owned-media-`, `social-commerce-`, `strategy-`: strategic frameworks and specialist strategy modules

If two skills overlap:

1. Prefer the more specific deliverable skill.
2. Use cross-cutting language or writing skills alongside it.
3. Consult companion skills named in the chosen skill's `References` section before inventing new structure.

## How To Execute A Skill

1. Read the selected skill's frontmatter and opening purpose text.
2. Read its `Use when`, `Do not use when`, `Required Input`, `Workflow`, `Outputs`, and `Quality Criteria` or `Quality Standards`.
3. Load only the referenced files needed for the current task. Do not bulk-load every file in `references/`.
4. Produce the deliverable in markdown unless the skill explicitly specifies another format.
5. Validate the output against the skill's quality section before returning it.

## Reference Handling

- Keep `SKILL.md` execution-focused.
- Use `references/` for deeper frameworks, examples, source notes, and long-form support material.
- If `references/` does not exist yet, use the inline instructions and keep future heavy content out of `SKILL.md`.
- Do not duplicate the same guidance across `SKILL.md` and `references/` unless brevity requires a short pointer in both places.

## Working Rules

- Preserve the current directory layout unless a change is clearly necessary.
- Do not relocate skills into a `skills/` folder just to satisfy one agent.
- Do not weaken Claude triggers in `description`; improve Codex compatibility by layering structure on top.
- Keep all `SKILL.md` files under 500 lines. Move deep detail into `references/` when needed.
- Keep frontmatter minimal: `name` and `description` only.
- Use British English throughout unless the target market or requested language requires otherwise.
- Keep outputs as text deliverables only. This repo does not produce code, web builds, graphic design, or video production.

## Quality Expectations

Every skill and every deliverable should be:

- Specific about when to use it and when not to
- Clear about required inputs
- Procedural rather than theoretical
- Explicit about outputs
- Grounded in East African market reality by default
- Safe, factual, and reviewable

## Maintenance

- Use `scripts/normalise_skills_for_dual_compat.py` to refresh the shared compatibility sections across top-level skills.
- Run `skill-safety-audit` for third-party imports or major changes.
- When a skill approaches the line limit, move detailed material into `references/` and leave only the execution workflow in `SKILL.md`.
