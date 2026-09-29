# social-media-skills Agent Guide

## Codex-only model setup and Kaizen review

Apply this section only when the active runner is Codex. Claude and other
runners must skip it and retain their own models and full engine capabilities.

Before substantive Codex work, resolve this engine's directory and an available
Python 3.11+ interpreter (use its absolute path if absent from PATH), then run
`python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check`.
If it reports configuration drift, Peter authorises the bounded
`--runtime codex --apply` repair, followed by `--check`. The helper backs up
changes and preserves unrelated settings. If Python or configuration access is
unavailable, report the limitation; do not replace the user's config wholesale.
Read `.codex/model-policy.md` for the full contract. Use Luna (`gpt-6-luna`)
with high reasoning by default for root orchestration, research, audit, review,
and execution. Use Astra (`gpt-6-astra`) only when Peter explicitly selects it
for the task; never select or fall back to GPT-5.6. Report unavailable required
GPT-6 models. A running session may need restarting for root settings to apply.

Every Kaizen cycle MUST check latest official model releases and actual
runtime availability, record dated evidence and a retain/change decision,
and evaluate better candidates before recommending replacement. Preserve the
pins until Peter authorises a verified change. Missing model-currentness
evidence is `NOT_ASSESSED`. This Codex adapter must not change CLAUDE.md,
Claude configuration, domain doctrine, permission settings or skill access.

## Universal agent integration

See `.skills-engine/engine-manifest.yaml` for the declarative contract used by the optional universal coordination package. The router and domain SKILL.md files remain authoritative.

The package may read the router, discover skills, inspect Git, and run only declared checks. Missing evidence is NOT ASSESSED; writes, pulls, publication, submissions, ledger/filing changes, deployment, or control changes require explicit approval.

Project context: if the working project root holds a `PROJECT.md` with `project_schema: 1`, read it before planning. It points to this engine's own context sources and never replaces them.

## Rules

Always-on cross-cutting principles live in `rules/` — see `rules/README.md`.
Load `rules/common/core.md` alongside the routed skill for any non-trivial task;
it is short and does not replace the skill, only sets the baseline the skill
operates within.

## Mandatory Digital Research currentness gate for Kaizen

Every Kaizen audit, skill edit, reference update, validator change, and
standardisation decision MUST begin with the Digital Research Engine at
`C:\wamp64\www\digital-research-engine`. Read its `source-evaluation` and
`source-verification` skills and the currentness gate reference
`docs/continuous-improvement/kaizen-currentness-gate.md`.

Before admitting any standard, policy, law, technology, platform capability,
software version, command, security control, benchmark, or lifecycle claim,
record source scope, publication/version date, access date, freshness class,
review date, support status, and uncertainty. Use current authoritative
primary sources; quarantine stale/ambiguous/unsupported claims and mark them
`NOT_ASSESSED`. Books are durable concept inputs only.

Shared agent, command, hook, evidence, and handoff behavior is mapped for
social-media work in [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md)
and governed centrally by `C:\wamp64\www\chwezi-dev-engine\docs\engine-control-plane.md`.

## Purpose

This repository is the Chwezi digital marketing and advertising consultancy engine (historical name `social-media-skills`), a dual-compatible skills system for professional digital marketing, advertising and social media consultancy work in Uganda and East Africa. It plans, specifies, writes, audits and reports on advertising strategy, media planning, budgets, creative briefs and concepts, ad copy, campaign build specifications, testing, scaling, optimisation and measurement; spending money, changing live ad accounts, publishing or contacting people always requires explicit client authority. It must continue to work for Claude Code while also being directly usable by Codex from the standard skill repository layout.

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

Skills are grouped into thematic categories under `skills/`: `ai-marketing/`, `business-development/`, `content-writing/`, `frameworks/`, `language/`, `meta-analytics-ops/`, `meta-utility/`, `pipeline/`, `platforms/`, `playbooks/`, `policies/`, `seo-discovery/`, `sectors/`, `strategy/`, `training/`, and `advertising/`. Treat every `skills/<category>/<skill-name>/SKILL.md` file as a skill. The repository root is reserved for project documentation and operational folders such as `docs/`, `skills/`, and `projects/`; do not add new skill directories directly at root, and do not place a skill directly under `skills/` — it must sit inside a category. (The former category-level standards file `skills/content-writing/SKILL.md` is now the inactive alias `skills/content-writing/ALIAS.md`; its standards live in `skills/content-writing/premium-commercial-writing/references/content-writing-standards.md`, and the shared `skills/content-writing/references/` folder stays in place.)

## Default Context

- Market: Uganda / East Africa unless the user specifies another market
- Language: British English
- Currency: UGX by default
- Timezone: EAT (UTC+3)
- Channel reality: WhatsApp-first, then Facebook/Instagram/TikTok/YouTube/LinkedIn/X depending on audience

If the user specifies another market, replace East Africa assumptions rather than layering the new market on top of them. Adapt channel, pricing, legal, tone, and conversion-path assumptions to the named market. If confidence is low, state the uncertainty and recommend specialist review where appropriate.

## Baseline Skills

Kaizen is mandatory for the engine and every campaign/content/report product. Load
`skills/meta-utility/kaizen-improvement-system/SKILL.md`; cap published audits at 65/100 and
target 95/100 with evidence, experiment, standardisation, and re-audit records. Current
platform, market, legal, and policy claims route through the source register and Digital Research.

Apply these alongside the main deliverable skill when relevant:

- `language/east-african-english`: tone, register, British spelling, EA business phrasing
- `language/language-standards`: multilingual standards where English, French, or Kiswahili output is required
- `content-writing/` (category): readability, headlines, persuasion, scannability
- `meta-utility/skill-writing`: authoring or revising skills in this repository
- `meta-utility/skill-safety-audit`: safety review for imported or substantially changed skills
- `ai-marketing/anti-ai-slop`: MANDATORY pre-ship gate — run its ship-gate checklist on every generated social output (caption, post, carousel, campaign, ad copy, blog, email, deck, image/video brief) before delivery or publishing
- `ai-marketing/ai-slop-audit`: auto-run whenever the user asks to analyse, review, evaluate, audit, critique, score, or de-slop any content/campaign/image/video, or asks "does this look AI-generated?"
- `ai-marketing/ai-generative-search-optimisation/references/ai-search-and-social-discovery-rules.md`:
  qualified concept input for response-mode planning, entity clarity, outcome
  separation and reversible experiments; it never supplies current platform facts.
- `content-writing/references/direct-marketing-ethics-filter.md`: mandatory for
  every ad, offer, outreach sequence, influencer brief and sales page.

## Routing Rules

For integrated digital marketing, start with `skills/pipeline/06-digital-marketing-strategy/SKILL.md` and its premium growth operating contract. For advertising (strategy, budget, media, creative, copy, paid search, paid social, testing, attribution), start with `skills/advertising/advertising-strategy-and-budget/SKILL.md` and route to the specific `advertising/` skill; paid social execution specifications live in `skills/playbooks/playbook-paid-social-advertising/SKILL.md`; the website handoff is `skills/advertising/ad-to-site-journey-handoff/SKILL.md`. For channel choice across all acquisition channels use `strategy/traction-channel-bullseye`; for segmentation and positioning use `strategy/marketing-foundations-stp-positioning`. Scope includes research, positioning, search, paid media, social, content, email, permissioned messaging, conversion, CRM, retention and measurement. Route builds and visual production to their canonical engines; planning text alone is not execution evidence. For professional consulting acquisition, connect `platform-linkedin` to website proof and CRM opportunity acceptance.
Use the skill whose directory name and `description` most closely match the deliverable. Prefixes matter:

- `biz-dev-`: credentials, proposals, pricing, outreach, practitioner positioning
- `00-` to `04-`: intake and onboarding
- `05-` to `09-`: strategy
- `10-` to `13-`: planning
- `platform-`: platform-specific plans
- `playbook-`: execution SOPs and operating playbooks
- Deck outline output: use only a matched skill that explicitly declares a slide-by-slide outline; no standalone deck category is active
- `meta-`: audits, measurement, analytics, models, reporting
- `training-`: client team training guides
- `policy-`: internal or client-facing policy documents
- `ai-`, `brand-voice-`, `prompt-`: AI strategy, prompting, automation, evaluation
- `caption-writer`, `email-copywriter`, `blog-writer`, `content-ideas`: direct content generation (hashtag strategy is part of `caption-writer`)
- `framework-`, `peso-`, `owned-media-`, `social-commerce-`, `strategy-`: strategic frameworks and specialist strategy modules
- `advertising/`: advertising strategy and budget, media planning, creative brief and big idea, ad copy and hook lab, paid search, testing and scaling, attribution and measurement, direct-response economics, ad-to-site journey handoff
- `business-development/eac-call-for-applications-campaign`: donor-compliant calls for applications, EOIs, applicant FAQs, partner dissemination kits, fairness protocols, and evidence logs across EAC markets
- `strategy/ecommerce-export-marketing-advisory`: export marketing plans for e-commerce companies, cross-border trust/proof layers, conversion reviews, CAC-bounded campaign outlines, and partner outreach

If two skills overlap:

1. Prefer the more specific deliverable skill.
2. Use cross-cutting language or writing skills alongside it.
3. Consult companion skills named in the chosen skill's `References` section before inventing new structure.

### Retired skill routes

A retired skill keeps its folder, but its `SKILL.md` is renamed `ALIAS.md` and is inactive. Never execute an `ALIAS.md`: look up its folder in `docs/skill-aliases.yml` (`inactive_skill_aliases`) and use the active owner it routes to; the retired skill's unique content lives in that owner's `references/`. The active catalogue is capped at 120 skills (`active_skill_policy.hard_cap`), checked by `scripts/check_skill_aliases.py` (Social Kaizen 2026-09-29, decision D-SK-03, dev-engine parity).

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

## Current evidence and release gates

- For changing platform, legal, regulatory or market claims, use `docs/source-registers/source-register.json`, open the underlying source, and record the source ID, access date, relevant section/table and limitation. Run `python -X utf8 scripts/check_source_freshness.py`; an overdue or unavailable source makes the affected check `not assessed`.
- Campaign work uses `docs/world-class-exemplars/campaign-exemplars.md` as a quality model, never as client evidence or a source of benchmark results.
- Reporting and ROI work uses `docs/evidence-packs/measurement-proof-pack.md` to define, reconcile and trace metrics.
- All finished creative uses `docs/quality-gates/creative-review-gate.md`. Paid media, WhatsApp, influencer, AI, UGC, public-sector and current-market work also uses `docs/quality-gates/legal-market-release-gate.md`.
- Legal gates are screening and escalation controls, not legal advice or certification. Missing counsel, rights, approval, source evidence or platform access never becomes a pass.

## Working Rules

- Preserve the standard directory layout unless a change is clearly necessary.
- Keep skills in `skills/<category>/<skill-name>/SKILL.md`.
- Do not weaken Claude triggers in `description`; improve Codex compatibility by layering structure on top.
- Keep all `SKILL.md` files under 500 lines. Move deep detail into `references/` when needed.
- Keep frontmatter within `docs/standards/skill-authoring-standard.md`; retain required `name`, `description` and portable `metadata`.
- Use British English throughout unless the target market or requested language requires otherwise.
- Keep outputs as text deliverables only. This repo does not produce code, web builds, graphic design, or video production.
- Never store book extractions or book summaries in this repository (owner rule, 2026-09-23). Fold book knowledge into task-oriented skill `references/` with a short citation; `scripts/source_ingestion_guardrail.py` enforces this.
- Reference files must not be single-book digests. Synthesise across sources into the engine's own task structure (inputs, decision rules, procedures, templates, checklists, localised original examples), in your own order and wording. Do not reproduce a book's numbered lists in its sequence, an author's full catalogue of beat/step/strategy names, book case studies or near-verbatim text, or "Strategy N" / chapter numbering. Name a framework with a brief attribution (for example "value ladder (Brunson)") and apply it; cite sources briefly as Author (Year) *Title*, Publisher.
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

## Engine conventions (moved from CLAUDE.md, M10-02)

The sections below were moved verbatim from the former `CLAUDE.md` when it became the thin bridge (portfolio bridge contract, M10-02). They bind every runner.

### Purpose and scope boundary

This repository is the Chwezi **digital marketing and advertising** consultancy engine (the repository keeps its historical name, `social-media-skills`). Skills produce every document in the consultancy lifecycle — credentials, proposals, marketing and advertising strategies, media plans, budgets, creative briefs and concepts, ad copy, campaign build specifications, content plans, platform and paid-media playbooks, testing and scaling plans, measurement and attribution frameworks, reports and training guides — and the agency's own operating system (prospecting, pricing, retention and key-account management).

**Scope boundary.** The engine plans, specifies, writes, audits and reports. It covers advertising strategy, media planning, budgeting, creative briefs and concepts, ad copy, campaign build specifications, testing and scaling logic, optimisation recommendations and reporting across paid search, paid social, display/video, audio, outdoor and direct response. **Spending money, changing live ad accounts, publishing or contacting people still requires explicit, action-specific client authority.** Finished visual execution hands off to `design-system-skills`; website implementation hands off to `website-skills` through the channel-to-site journey handoff (`skills/advertising/ad-to-site-journey-handoff/`); formal tenders to `proposal-skills`; business and full marketing plan documents to `business-plan-skills`; tax, accounting and financial statements to `chwezi-accounting-doctrine`; current facts to `digital-research-engine`. Skills generate text documents, structured plans, specifications and slide outlines — not code, builds or finished designs.

### Active Roadmap

The current system-upgrade roadmap lives in:

- `docs/plans/2026-04-14-world-class-consultancy-engine/00-roadmap-index.md`

Treat that roadmap as the controlling sequence for major repository improvements. Its target end-state is a world-class, market-adaptive consultancy engine rather than a fixed East Africa-only prompt library.

### Blog & Article Research — Always Use the Digital Research Engine

**Every blog post, article, or thought-leadership piece must be researched with the digital-research-engine before drafting.** Never write a blog post from assumed knowledge alone. Real examples, statistics, market figures, and any cited research must come from a live research wave, with sources verified and credit given to the original authors (named researchers, institutions, regulators).

- **Engine location:** `digital-research-engine` (on this machine: `C:\wamp64\www\digital-research-engine\skills\`). The repo is cloned on every device Peter works on; if the path differs, locate the `digital-research-engine` repo locally rather than skipping research.
- **Method:** Start with `research-orchestration/SKILL.md` and run a planned multi-agent wave — one research agent per cohort/region (e.g. one per country), each briefed per the engine's standard agent-brief structure. The orchestrator (you) does the synthesis; research agents return raw, sourced findings only.
- **Article SEO/SERP standard:** Before drafting any article, blog post or thought-leadership piece, run the digital-research-engine's three-wave article study: map intent and 3–7 query clusters; read the accessible top five results for each cluster; then synthesise the content gap, AI-answer opportunities, keyword map, internal links and verified primary-source plan. Use an approved search/API tool rather than direct Google SERP scraping. Record query date, provider, exact queries, result URLs and read status. Treat search visibility as competitive evidence, never as proof or a ranking promise; do not invent search volumes. For bilingual content, research English and French intent separately and translate the decision, not just the words. Social cut-downs inherit the article's verified intent and source map.
- **Attribution is mandatory.** Cite real, locatable sources with URLs. Name the student/academic researchers, universities, and regulators whose work you draw on. Mark anything you cannot directly verify as UNVERIFIED and either confirm it or frame it without inventing authors, titles, or statistics. Never fabricate a citation.
- **Output:** Weave credits naturally into the prose and close each piece with a short "Sources & the researchers worth crediting" block. See `projects/tech-guy-peter/blog-posts/N2-cloud-erp-migration-east-africa.md` as the reference example of this standard.

### Naming Conventions

| Prefix | Category | Examples |
|---|---|---|
| `biz-dev-` | Business development | biz-dev-proposal, biz-dev-credentials |
| `01-` through `04-` | Client onboarding | 01-client-brief, 03-audience-personas |
| `05-` through `09-` | Strategy | 05-social-media-strategy, 07-email-marketing-strategy |
| `10-` through `13-` | Planning | 10-content-pillars, 11-content-calendar |
| `platform-` | Platform-specific plans | platform-facebook, platform-linkedin |
| `playbook-` | Execution playbooks | playbook-crisis-communications |
| Deck outline output | Slide-by-slide outline declared by the matched skill; final visual production routes to `design-system-skills` | No standalone deck route is active |
| `meta-` | Analytical / reporting | meta-reporting, meta-roi-framework |
| `advertising/` skills (plain names) | Advertising strategy, media, creative, copy, search, testing, attribution | advertising-strategy-and-budget, media-planning, ad-copy-and-hook-lab |
| `training-` | Training guides | training-client-team, training-diy-content |
| Plain name | Utility / generation | caption-writer, content-ideas, blog-writer |

### Skill Categories

Skills are organised into thematic subdirectories under `skills/`. The canonical path for any skill is `skills/<category>/<skill-name>/SKILL.md`.

| Category | Contents |
|---|---|
| `ai-marketing/` | AI-prefixed skills, brand voice AI training, AI strategy and governance |
| `business-development/` | `biz-dev-*` — credentials, proposals, pricing, outreach, practitioner positioning |
| `content-writing/` | Blog, caption, email, copywriting, direct-response, prompt libraries, hashtag, image-prompt skills |
| `pipeline/` | Numbered onboarding-to-planning flow `00-` through `13-` |
| `frameworks/` | Inactive aliases only since Social Kaizen S06: `framework-community-trust` routes to `playbook-community-management` and `framework-digital-transparency` to `strategy-csr-purpose-communications` |
| `meta-analytics-ops/` | `meta-*` analytics, reporting, measurement, audit skills |
| `platforms/` | `platform-*` per-channel plans |
| `playbooks/` | `playbook-*` execution SOPs |
| `policies/` | `policy-*` governance and compliance |
| `strategy/` | `strategy-*` plus `peso-integrated-strategy` (absorbed `owned-media-strategy`), `social-commerce-strategy`, `ecommerce-*`, `marketing-foundations-stp-positioning`, `traction-channel-bullseye` |
| `advertising/` | Advertising strategy and budget, media planning, creative brief and big idea, ad copy and hook lab, paid search, testing and scaling, attribution and measurement, direct-response economics, and the ad-to-site journey handoff |
| `training/` | `training-*` client team training guides |
| `seo-discovery/` | `seo-geo-optimisation`, `demand-forecasting` |
| `sectors/` | Sector-specific social media skills — `healthcare` (first); future: financial services, education, hospitality, NGO |
| `language/` | `east-african-english`, `language-standards` |
| `meta-utility/` | `skill-writing`, `skill-safety-audit` — for authoring/auditing skills themselves |

When referencing a skill in documentation or prompts, use the full path: `skills/<category>/<skill-name>/SKILL.md`.

### Authoring Rules (All Skills)

The binding contract is `docs/standards/skill-authoring-standard.md`; use `docs/templates/SKILL.template.md` for new skills.

1. **Portable SKILL.md entrypoint** — every skill lives at `skills/<category>/<skill-name>/SKILL.md` with directory-matching `name`, a single-line `Use when` description, and portable Claude Code/Codex metadata. Keep deep material in linked `references/`; do not add README.md or CHANGELOG.md inside skill folders.
2. **No skills at `skills/` root** — every skill must live inside one of the category subdirectories listed above. Pick the category whose theme best matches the skill; add a new category only when no existing one fits.
3. **500-line hard limit** — SKILL.md must stay under 500 lines. Detailed reference material goes in `references/` subfolder and is linked from SKILL.md with a note on when to read it.
4. **British English throughout** — organisation, colour, programme, behaviour, analyse, strategise, recognise, centre, enquiry. Never American spellings.
5. **Imperative language** — "Ask for…", "Generate…", "Apply…", "Include…". Not "you should" or "Claude will".
6. **Composition contracts** — every skill declares sources and absent-input behaviour, outputs and acceptance, evidence, capability permissions, degraded mode, decision risks, stop/recovery workflow, quality standards, five corrected anti-patterns, and direct references.
7. **Read-only analysis** — audits, reviews, diagnostics, critiques, analysis, and planning default to read-only. Publishing, spend, outreach, production mutation, destructive work, personal-data processing, and certification claims require explicit authority.
8. **Release gates** — run `python -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json`, `python -X utf8 scripts/routing_smoke_test.py`, repository tests, and canonical per-skill validation. Failure counts must remain empty.

### Anti-AI-Slop Quality Gate (Mandatory)

Two skills under `skills/ai-marketing/` enforce that nothing leaving this engine reads as AI slop:

- **`anti-ai-slop` — MANDATORY, applied in REAL TIME.** This is a live constraint applied **continuously while generating** — to every caption, post, slide, line, and image-brief sentence as it is written, not only as a final pre-ship pass. The moment a banned word, generic placeholder, unverified figure/brand/price, or template default appears, fix it in place. Run its ship-gate checklist on **every generated social output** — caption, post, thread, carousel, campaign, ad copy, blog draft, email, deck outline, image/video brief — before it is delivered to a client or published. No output ships with an unticked ship-gate box. Apply it alongside the deliverable skill and its humanising rewrite passes (`skills/ai-marketing/anti-ai-slop/references/humanising-rewrite-passes.md`, which absorbed the retired `ai-content-humaniser`), not instead of them.
- **`ai-slop-audit` — RUNS AFTER EACH MAJOR ITERATION (not only on request).** Run it after each completed unit of work — a drafted caption/post, a finished thread/carousel, a completed campaign or content calendar, a deck outline, a significant revision — logging a verdict each time; a grade **F blocks progression** to the next asset or submission until the blocking findings are fixed. It also auto-runs whenever the user asks to **analyse, review, evaluate, audit, critique, score, or de-slop** any content, campaign, image, or video, or asks "does this look AI-generated / is this AI slop / why does this feel off?", and as the final gate before publishing. It returns a graded report (A/B/C/F) with evidenced findings and concrete fixes.

The two skills share one verified evidence base and one merged banned-vocabulary list (the canonical anti-slop lexicon plus the list of the retired `ai-content-humaniser`, now merged into `anti-ai-slop`). Preserve their verified citations verbatim: Merriam-Webster 2025 Word of the Year; Kommers et al. *"Why Slop Matters"* (arXiv 2601.06060); Spracklen et al. (USENIX Security 2025, 19.7%); Veracode (45% / XSS 86% / log-injection 88%). Do not add unsourced statistics to either skill.

### Default Country Context: Uganda / East Africa

All skills default to the Ugandan/East African market unless the user specifies otherwise. This affects examples, platform penetration data, pricing, cultural references, and audience characteristics.

If another market is specified, replace those assumptions rather than keeping Uganda/East Africa defaults in place. Make market-specific assumptions explicit where they materially affect strategy, platform selection, pricing, evaluation, or compliance guidance.

**Platform defaults for Uganda/EA:**

| Platform | Role in EA |
|---|---|
| WhatsApp | Dominant messaging channel in East Africa; no source measures its share of smartphone users, so state no percentage unless it is a named, dated figure with its base (best-attributed: Pew 2023 adults, 8-country median 73%; Yazi unattributed internet-user estimates) and check the client's own audience data (register MK-03, WA-01, 2026-09-24) |
| Facebook | Broad reach and community. In Uganda the status is unstable; verify access at the campaign date (access reported restored on 13 Jun 2026 after the January 2021 block, no UCC statement found; register UG-FACEBOOK-ACCESS-2026). Meta ad-reach figures for Uganda were measured during the block, so treat them as a floor (register MK-02) |
| Instagram | Urban, 18–35, aspirational content |
| TikTok | Fast-growing, 16–30, entertainment-first |
| YouTube | Research, tutorial, long-form video |
| LinkedIn | B2B, professionals, formal sector |
| X/Twitter | Opinion leaders, journalists, public figures, public sector |

### Strategic Frameworks to Reference

Apply where relevant; cite on first use:

- **POEM model** (Paid/Owned/Earned) — channel classification
- **RACE framework** (Reach/Act/Convert/Engage) — Chaffey (2024)
- **10-4-1 rule** — Bodnar and Cohen (2012): 10 shares, 4 original posts, 1 promotional
- **Hero/Hub/Hygiene** — content tier model (YouTube/Google)
- **Minto's Pyramid Principle** — conclusion-first slide sequencing
- **SMART objectives** — all goals must be Specific, Measurable, Achievable, Relevant, Time-bound
- **ROI formula** — (TLV − COCA) ÷ COCA — Bodnar and Cohen (2012)
- **Playing to Win** — where to play / how to win logic for strategic choice
- **Good Strategy/Bad Strategy** — diagnosis, guiding policy, coherent action
- **Kennedy + Brunson direct-response** — whenever a brief requires *selling* (not awareness), use `direct-response-funnel-copy` and its `references/` (funnel architecture and scripts, long-copy sales-letter system, offer/proposition and price integrity, consultative sales and positioning), always with `skills/content-writing/references/direct-marketing-ethics-filter.md`.
- **Advertising doctrine** — 4-level measurement (message, communication, media, business), budget triangulation with a minimum-effective floor, reach/frequency/GRP media maths, the strategic creative brief and effectiveness scale, lines in the sand and the retest→extend→roll-out ladder. Start at `skills/advertising/advertising-strategy-and-budget/SKILL.md`.
- **Channel choice** — Bullseye across all 19 traction channels (`strategy/traction-channel-bullseye`) before assigning roles within social (`strategy-channel-architecture`).

**Key references to cite:**
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*
- Kotler, P. et al. (2023) *Marketing Management*
- Kennedy, D. and Marrs, J. (2011) *No B.S. Price Strategy*; Kennedy, D. (2004) *No B.S. Sales Success*; Kennedy, D. (2000) *The Ultimate Sales Letter*; Brunson, R. *DotComSecrets Ignite*
- Kelley, L. D. and Sheehan, K. B. (c. 2021–22) *Advertising Management in a Digital Environment*, Routledge
- Landa, R. (2022) *Strategic Creativity*, Routledge
- Serling, B. (2002) *How to Write Million Dollar Ads, Sales Letters & Web Marketing Pieces*, The Internet Marketing Center
- Stockwell, J. and Shaw, H. M. (1994) *Direct Marketing Checklists*, NTC Business Books
- Weinberg, G. and Mares, J. (2014) *Traction*, S-curves Publishing; Croll, A. and Yoskovitz, B. (2013) *Lean Analytics*, O'Reilly

### Book extractions are never stored in this repository (owner rule, 2026-09-23)

Do not create `book-extractions/`, book summaries or "extraction" files anywhere in this repository. Book knowledge lands only as task-oriented skill content and `references/` files (procedures, checklists, templates, decision rules, phrase banks) with a short citation (Author (Year) *Title*, Publisher). Paraphrase; quotes stay at or under 25 words. `scripts/source_ingestion_guardrail.py` fails any file under a book-extraction path.

### Deck outline format

Any matched skill that declares a slide-by-slide deck outline must use this structured markdown format. Every slide entry must follow this exact format:

```
**Slide N — [Slide Title]**
**Headline:** The one thing the audience must remember from this slide
**Bullets:**
- Point one
- Point two
- Point three
**Speaker Notes:** What the presenter says — context, data, anecdotes not on the slide
**Visual Direction:** What the slide should look like — layout, imagery, colour, chart type
```

Output is paste-ready into PowerPoint, Canva, or Google Slides. The skill does not generate .pptx files.

### Existing Skills in This Repo

These skills are available under `skills/<category>/<skill-name>/SKILL.md` and should be referenced (not duplicated) where relevant:

| Skill | Path | Purpose |
|---|---|---|
| `east-african-english` | `skills/language/east-african-english/` | Language and tone standard — British English, EA professional register |
| `language-standards` | `skills/language/language-standards/` | Grammar, punctuation, and vocabulary rules |
| `content-writing-standards` | `skills/content-writing/premium-commercial-writing/references/content-writing-standards.md` | General content writing standards (formerly the category-level `skills/content-writing/SKILL.md`) |
| `blog-writer` | `skills/content-writing/blog-writer/` | Blog post content generation (text, SEO, captions — no web dev) |
| `content-ideas` | `skills/content-writing/content-ideas/` | Generate content and blog topic ideas and briefs (absorbed `blog-idea-generator`) |
| `platform-linkedin` | `skills/platforms/platform-linkedin/` | LinkedIn personal and Company Page work, including Company Page setup, growth, Sub-Pages and Events (absorbed `platform-linkedin-company-pages`) |
| `advertising-strategy-and-budget` | `skills/advertising/advertising-strategy-and-budget/` | Entry point for advertising strategy, budget triangulation, measurement architecture and agency–client governance |
| `direct-marketing-ethics-filter` | `skills/content-writing/references/direct-marketing-ethics-filter.md` | Canonical ethics filter for ads, offers, outreach and influencer work |
| `anti-ai-slop` | `skills/ai-marketing/anti-ai-slop/` | MANDATORY pre-ship guardrail — ship-gate checklist run on every generated social output so it cannot read as AI slop |
| `ai-slop-audit` | `skills/ai-marketing/ai-slop-audit/` | Auto-run detector — grades any social artefact (A/B/C/F) for AI slop with evidenced findings and concrete fixes |

### Out of Scope

- Finished graphic design or visual asset production (route to `design-system-skills`)
- Video editing or video production
- Executing spend, changing live ad accounts, publishing or contacting people without explicit client authority (planning, specification, optimisation recommendations and reporting ARE in scope)
- Web design or web development (route to `website-skills` via the journey handoff)
- Legal advice or certification — influencer and advertising agreements get a pre-lawyer term sheet here; counsel drafts and approves

### Upgrade Priority

When improving this repository, prioritise in this order:

1. Market-context and localisation layers
2. Core strategy and proposal quality
3. Platform and execution coherence
4. Measurement and evaluation quality
5. AI governance and augmentation
6. Commercial packaging and operating system depth

<!-- design-system-skills:trigger v3 -->
### Design / typography / UI/UX (cross-cutting — consult IN ADDITION)

Any work touching how an artifact LOOKS — font/typeface choice, type scale, colour, layout/grid,
visual identity, web/desktop/mobile UI screens, or the visual formatting of a DOCX/PPTX/PDF/XLSX
— routes to the **`design-system-skills`** engine, the single home for ALL design/UI/UX skills
and the anti-AI-slop doctrine.

**Resolve its location on THIS device from the active runner's global engine-routing table or
`AGENTS.md`** — never assume an absolute path; it varies per machine. Then read its
`README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md` fresh and route by
frontmatter (read SKILL.md directly, not via the Skill tool). Content and structure stay in THIS
engine; presentation comes from design-system-skills. Hard rule: never use a banned AI-slop font
as primary type — hard ban: Inter, Geist, Roboto, Open Sans, Lato, Arial, Fraunces, IBM Plex (all
faces); secondary ban: Space Grotesk, Instrument Serif, Instrument Sans, Poppins, Montserrat, Nunito, Nunito Sans, Newsreader, Cormorant (all cuts), Crimson Pro, Plus Jakarta Sans, DM Sans, Outfit, Playfair Display, Lora, Space Mono;
Roboto Mono and IBM Plex Mono are banned as monospace choices; Source Sans 3 only as a paired
body face; no bare system stacks alone. State the chosen typeface and reason before producing
any artifact.
<!-- /design-system-skills:trigger -->

## Human-English editorial standard (2026-08 Kaizen)

Load [`human-english-craft-standard.md`](skills/language/language-standards/references/human-english-craft-standard.md), [`human-professional-phrase-bank.md`](skills/content-writing/references/human-professional-phrase-bank.md) and [`skills/language/language-standards/references/english-collocations-and-lexical-precision-2026-09-02.md`](skills/language/language-standards/references/english-collocations-and-lexical-precision-2026-09-02.md) for every caption, post, script, email, comment, campaign, calendar, report, training asset, and client message. Apply its five passes with the channel skill, native-language skill, rights review, and anti-slop gate.

Social writing must be channel-native without becoming careless: one real idea, one audience, one honest action, concrete detail, correct grammar, natural rhythm, and local texture only when true. Do not use forced slang, hashtag piles, fake intimacy, invented lived experience, or typos to imitate people. Record audience, channel, purpose, source/rights status, claim checks, language review, proof status, gaps, reviewer, and date.

## DOMAIN PROMPT GENERATION CONTRACT

For a prompt handoff, read the local [domain prompt contract](docs/ai-prompting/domain-prompt-compilation-contract.md). Generate a ready-to-paste prompt with channel, audience, one communication job, hook, proof, CTA, format, language, rights/moderation constraints, visual/audio direction, and measurement checks. **Ready-to-paste prompt:** include assumptions, rights/safety flags, and next action. **Failure action:** repair the single failed content unit or regenerate when the concept is wrong.

## PORTFOLIO CRAFT CONTRACT

Load `C:\wamp64\www\chwezi-engine-agents\docs\operations\portfolio-craft-standard-2026-09-04.md` when available. Build a campaign in deliberate content units: frame the audience and channel job, select one post or asset, inspect brand and evidence context, draft with a distinct point of view, check platform fit and moderation risk, review the visual/audio treatment, refine, and record the approval and measurement plan. Real examples, source status, correction handling, and a meaningful next action matter more than volume. Do not generate a calendar full of interchangeable posts. Apply `Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure` to kaizen itself. Missing source, rights, platform, render, approval, or performance evidence is `NOT ASSESSED`, never a pass.
