# social-media-skills Agent Guide

## Purpose

This repository is a dual-compatible skills system for professional social media and digital marketing consultancy work in Uganda and East Africa. It must continue to work for Claude Code while also being directly usable by Codex from the standard skill repository layout.

The portable unit is the skill directory:

```text
skills/
  [category]/
    [skill-name]/
      SKILL.md
      references/   # optional
      scripts/      # optional
      assets/       # optional
```

Skills are grouped into thematic categories under `skills/`: `ai-marketing/`, `business-development/`, `content-writing/`, `decks/`, `frameworks/`, `language/`, `meta-analytics-ops/`, `meta-utility/`, `pipeline/`, `platforms/`, `playbooks/`, `policies/`, `seo-discovery/`, `strategy/`, `training/`. Treat every `skills/<category>/<skill-name>/SKILL.md` file as a skill. The repository root is reserved for project documentation and operational folders such as `docs/`, `skills/`, and `projects/`; do not add new skill directories directly at root, and do not place a skill directly under `skills/` — it must sit inside a category.

## Default Context

- Market: Uganda / East Africa unless the user specifies another market
- Language: British English
- Currency: UGX by default
- Timezone: EAT (UTC+3)
- Channel reality: WhatsApp-first, then Facebook/Instagram/TikTok/YouTube/LinkedIn/X depending on audience

If the user specifies another market, replace East Africa assumptions rather than layering the new market on top of them. Adapt channel, pricing, legal, tone, and conversion-path assumptions to the named market. If confidence is low, state the uncertainty and recommend specialist review where appropriate.

## Baseline Skills

Apply these alongside the main deliverable skill when relevant:

- `language/east-african-english`: tone, register, British spelling, EA business phrasing
- `language/language-standards`: multilingual standards where English, French, or Kiswahili output is required
- `content-writing/` (category): readability, headlines, persuasion, scannability
- `meta-utility/skill-writing`: authoring or revising skills in this repository
- `meta-utility/skill-safety-audit`: safety review for imported or substantially changed skills
- `ai-marketing/anti-ai-slop`: MANDATORY pre-ship gate — run its ship-gate checklist on every generated social output (caption, post, carousel, campaign, ad copy, blog, email, deck, image/video brief) before delivery or publishing
- `ai-marketing/ai-slop-audit`: auto-run whenever the user asks to analyse, review, evaluate, audit, critique, score, or de-slop any content/campaign/image/video, or asks "does this look AI-generated?"

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
- `business-development/eac-call-for-applications-campaign`: donor-compliant calls for applications, EOIs, applicant FAQs, partner dissemination kits, fairness protocols, and evidence logs across EAC markets
- `strategy/ecommerce-export-marketing-advisory`: export marketing plans for e-commerce companies, cross-border trust/proof layers, conversion reviews, CAC-bounded campaign outlines, and partner outreach

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
6. Apply `ai-marketing/anti-ai-slop` in real time while generating — fix banned vocabulary, generic placeholders, unverified figures/brands/prices, and template defaults in place — and run its ship-gate checklist on the finished output before delivery. Run `ai-marketing/ai-slop-audit` after each major iteration (a drafted asset, a finished thread or carousel, a completed campaign or calendar, a significant revision) and whenever the user asks to analyse, review, audit, critique, score, or de-slop existing content; a grade of F blocks progression to the next asset or to submission until the blocking findings are fixed.

## Reference Handling

- Keep `SKILL.md` execution-focused.
- Use `references/` for deeper frameworks, examples, source notes, and long-form support material.
- If `references/` does not exist yet, use the inline instructions and keep future heavy content out of `SKILL.md`.
- Do not duplicate the same guidance across `SKILL.md` and `references/` unless brevity requires a short pointer in both places.

## Working Rules

- Preserve the standard directory layout unless a change is clearly necessary.
- Keep skills in `skills/<skill-name>/SKILL.md`.
- Do not weaken Claude triggers in `description`; improve Codex compatibility by layering structure on top.
- Keep all `SKILL.md` files under 500 lines. Move deep detail into `references/` when needed.
- Keep frontmatter minimal: `name` and `description` only.
- Use British English throughout unless the target market or requested language requires otherwise.
- Keep outputs as text deliverables only. This repo does not produce code, web builds, graphic design, or video production.
- For strategy, proposal, pricing, platform, reporting, and AI governance work, make market assumptions explicit rather than hidden.
- Follow the active roadmap in `docs/plans/2026-04-14-world-class-consultancy-engine/` when changing repository-level documentation or high-impact skills.

## Document and Spreadsheet Tooling

- Before promising `.docx`, `.pdf`, `.xlsx`, application registers, scoring matrices, budgets, monitoring dashboards, reports, or annexes, check whether document and spreadsheet tooling is available.
- Prefer available Codex/Claude document and spreadsheet plugins. If unavailable, use local Python libraries such as `openpyxl`, `XlsxWriter`, `pandas`, `python-docx`, `docxtpl`, `docxcompose`, `pypandoc`, `markdown`, `PyMuPDF`, `pypdf`, `pdfplumber`, and `reportlab`.
- Check binaries such as `pandoc`, LibreOffice/`soffice`, `wkhtmltopdf`, and `tesseract` when conversion or OCR is needed.
- Run a minimal DOCX/XLSX smoke test on a new machine before production export.
- Never claim a generated Word, PDF, or Excel file exists unless it was actually written and opened or validated.

## Quality Expectations

Every skill and every deliverable should be:

- Specific about when to use it and when not to
- Clear about required inputs
- Procedural rather than theoretical
- Explicit about outputs
- Grounded in East African market reality by default
- Adaptable to non-EA markets when specified
- Safe, factual, and reviewable

## Maintenance

- Follow `docs/standards/skill-authoring-standard.md` and start new skills from `docs/templates/SKILL.template.md`.
- Treat `quality-baseline.json` as a zero-debt assertion, not a waiver list. Run `python -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json` and `python -X utf8 scripts/routing_smoke_test.py` before release.
- The legacy `scripts/normalise_skills_for_dual_compat.py` is not an authoring substitute; it may repair marker syntax only and must not invent domain contracts.
- Run `skill-safety-audit` for third-party imports or major changes.
- When a skill approaches the line limit, move detailed material into `references/` and leave only the execution workflow in `SKILL.md`.

<!-- design-system-skills:trigger v1 -->
### Design / typography / UI/UX (cross-cutting — consult IN ADDITION)

Any work touching how an artifact LOOKS — font/typeface choice, type scale, colour, layout/grid,
visual identity, web/desktop/mobile UI screens, or the visual formatting of a DOCX/PPTX/PDF/XLSX
— routes to the **`design-system-skills`** engine, the single home for ALL design/UI/UX skills
and the anti-AI-slop doctrine.

**Resolve its location on THIS device from your global engine-routing table** (`~/.claude/CLAUDE.md`,
or `AGENTS.md` for Codex) — never assume an absolute path; it varies per machine. Then read its
`README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md` fresh and route by
frontmatter (read SKILL.md directly, not via the Skill tool). Content and structure stay in THIS
engine; presentation comes from design-system-skills. Hard rule: never use a banned AI-slop font
(Inter, Geist, Roboto, Arial, Open Sans, Lato, Space Grotesk, bare system stacks) as primary
type — state the chosen typeface and reason before producing any artifact.
<!-- /design-system-skills:trigger -->
