# social-media-skills — Project Conventions

## Purpose

This repository is a complete documentation and deliverable toolkit for running a professional social media and digital marketing consultancy. Skills produce every document in the consultancy lifecycle: credentials, proposals, strategies, content plans, platform playbooks, presentation decks, reports, and training guides.

**This suite is content-only.** No web development, graphic design, video editing, or paid ad campaign management (bidding/creative testing). Skills generate text documents, structured plans, and slide outlines — not files, code, or designs.

## Active Roadmap

The current system-upgrade roadmap lives in:

- `docs/plans/2026-04-14-world-class-consultancy-engine/00-roadmap-index.md`

Treat that roadmap as the controlling sequence for major repository improvements. Its target end-state is a world-class, market-adaptive consultancy engine rather than a fixed East Africa-only prompt library.

---

## Blog & Article Research — Always Use the Digital Research Engine

**Every blog post, article, or thought-leadership piece must be researched with the digital-research-engine before drafting.** Never write a blog post from assumed knowledge alone. Real examples, statistics, market figures, and any cited research must come from a live research wave, with sources verified and credit given to the original authors (named researchers, institutions, regulators).

- **Engine location:** `digital-research-engine` (on this machine: `C:\Users\Peter\Documents\Claude Projects\digital-research-engine\skills\`). The repo is cloned on every device Peter works on; if the path differs, locate the `digital-research-engine` repo locally rather than skipping research.
- **Method:** Start with `research-orchestration/SKILL.md` and run a planned multi-agent wave — one research agent per cohort/region (e.g. one per country), each briefed per the engine's standard agent-brief structure. The orchestrator (you) does the synthesis; research agents return raw, sourced findings only.
- **Attribution is mandatory.** Cite real, locatable sources with URLs. Name the student/academic researchers, universities, and regulators whose work you draw on. Mark anything you cannot directly verify as UNVERIFIED and either confirm it or frame it without inventing authors, titles, or statistics. Never fabricate a citation.
- **Output:** Weave credits naturally into the prose and close each piece with a short "Sources & the researchers worth crediting" block. See `projects/tech-guy-peter/blog-posts/N2-cloud-erp-migration-east-africa.md` as the reference example of this standard.

---

## Naming Conventions

| Prefix | Category | Examples |
|---|---|---|
| `biz-dev-` | Business development | biz-dev-proposal, biz-dev-credentials |
| `01-` through `04-` | Client onboarding | 01-client-brief, 03-audience-personas |
| `05-` through `09-` | Strategy | 05-social-media-strategy, 07-email-marketing-strategy |
| `10-` through `13-` | Planning | 10-content-pillars, 11-content-calendar |
| `platform-` | Platform-specific plans | platform-facebook, platform-linkedin |
| `playbook-` | Execution playbooks | playbook-crisis-communications |
| `deck-` | Presentation deck outlines | deck-strategy-presentation, deck-monthly-report |
| `meta-` | Analytical / reporting | meta-reporting, meta-roi-framework |
| `training-` | Training guides | training-client-team, training-diy-content |
| Plain name | Utility / generation | caption-writer, hashtag-strategy, blog-post-writer |

---

## Skill Categories

Skills are organised into thematic subdirectories under `skills/`. The canonical path for any skill is `skills/<category>/<skill-name>/SKILL.md`.

| Category | Contents |
|---|---|
| `ai-marketing/` | AI-prefixed skills, brand voice AI training, AI strategy and governance |
| `business-development/` | `biz-dev-*` — credentials, proposals, pricing, outreach, practitioner positioning |
| `content-writing/` | Blog, caption, email, copywriting, direct-response, prompt libraries, hashtag, image-prompt skills |
| `pipeline/` | Numbered onboarding-to-planning flow `00-` through `13-` |
| `decks/` | All `deck-*` presentation outline skills |
| `frameworks/` | `framework-*` strategic frameworks |
| `meta-analytics-ops/` | `meta-*` analytics, reporting, measurement, audit skills |
| `platforms/` | `platform-*` per-channel plans |
| `playbooks/` | `playbook-*` execution SOPs |
| `policies/` | `policy-*` governance and compliance |
| `strategy/` | `strategy-*` plus `owned-media-strategy`, `peso-integrated-strategy`, `social-commerce-strategy`, `ecommerce-*`, `premium-social-selling` |
| `training/` | `training-*` client team training guides |
| `seo-discovery/` | `seo-geo-optimisation`, `demand-forecasting` |
| `sectors/` | Sector-specific social media skills — `healthcare` (first); future: financial services, education, hospitality, NGO |
| `language/` | `east-african-english`, `language-standards` |
| `meta-utility/` | `skill-writing`, `skill-safety-audit` — for authoring/auditing skills themselves |

When referencing a skill in documentation or prompts, use the full path: `skills/<category>/<skill-name>/SKILL.md`.

---

## Authoring Rules (All Skills)

1. **SKILL.md only** — every skill lives at `skills/<category>/<skill-name>/SKILL.md` with YAML frontmatter (`name` and `description` only). No README.md, CHANGELOG.md, or auxiliary docs.
2. **No skills at `skills/` root** — every skill must live inside one of the category subdirectories listed above. Pick the category whose theme best matches the skill; add a new category only when no existing one fits.
3. **500-line hard limit** — SKILL.md must stay under 500 lines. Detailed reference material goes in `references/` subfolder and is linked from SKILL.md with a note on when to read it.
4. **British English throughout** — organisation, colour, programme, behaviour, analyse, strategise, recognise, centre, enquiry. Never American spellings.
5. **Imperative language** — "Ask for…", "Generate…", "Apply…", "Include…". Not "you should" or "Claude will".
6. **Required Input section** — every skill must ask for: client business name, industry, country/city, and primary goal before generating any deliverable. For strategy, proposal, pricing, platform, reporting, and AI-governance skills, also capture market context, audience context, and relevant compliance or risk context.
7. **Quality Criteria section** — every skill must include 5–8 bullets defining what good output looks like for that specific skill.
8. **Frontmatter description** — must state both *what the skill does* and *when to invoke it* (triggers). This is the primary trigger mechanism.

---

## Anti-AI-Slop Quality Gate (Mandatory)

Two skills under `skills/ai-marketing/` enforce that nothing leaving this engine reads as AI slop:

- **`anti-ai-slop` — MANDATORY, applied in REAL TIME.** This is a live constraint applied **continuously while generating** — to every caption, post, slide, line, and image-brief sentence as it is written, not only as a final pre-ship pass. The moment a banned word, generic placeholder, unverified figure/brand/price, or template default appears, fix it in place. Run its ship-gate checklist on **every generated social output** — caption, post, thread, carousel, campaign, ad copy, blog draft, email, deck outline, image/video brief — before it is delivered to a client or published. No output ships with an unticked ship-gate box. Apply it alongside the deliverable skill and `ai-content-humaniser`, not instead of them.
- **`ai-slop-audit` — RUNS AFTER EACH MAJOR ITERATION (not only on request).** Run it after each completed unit of work — a drafted caption/post, a finished thread/carousel, a completed campaign or content calendar, a deck outline, a significant revision — logging a verdict each time; a grade **F blocks progression** to the next asset or submission until the blocking findings are fixed. It also auto-runs whenever the user asks to **analyse, review, evaluate, audit, critique, score, or de-slop** any content, campaign, image, or video, or asks "does this look AI-generated / is this AI slop / why does this feel off?", and as the final gate before publishing. It returns a graded report (A/B/C/F) with evidenced findings and concrete fixes.

The two skills share one verified evidence base and one merged banned-vocabulary list (the canonical anti-slop lexicon plus the existing `ai-content-humaniser` list). Preserve their verified citations verbatim: Merriam-Webster 2025 Word of the Year; Kommers et al. *"Why Slop Matters"* (arXiv 2601.06060); Spracklen et al. (USENIX Security 2025, 19.7%); Veracode (45% / XSS 86% / log-injection 88%). Do not add unsourced statistics to either skill.

---

## Default Country Context: Uganda / East Africa

All skills default to the Ugandan/East African market unless the user specifies otherwise. This affects examples, platform penetration data, pricing, cultural references, and audience characteristics.

If another market is specified, replace those assumptions rather than keeping Uganda/East Africa defaults in place. Make market-specific assumptions explicit where they materially affect strategy, platform selection, pricing, evaluation, or compliance guidance.

**Platform defaults for Uganda/EA:**

| Platform | Role in EA |
|---|---|
| WhatsApp | Dominant messaging; 90%+ smartphone users; primary for customer comms |
| Facebook | Largest social platform; all demographics |
| Instagram | Urban, 18–35, aspirational content |
| TikTok | Fast-growing, 16–30, entertainment-first |
| YouTube | Research, tutorial, long-form video |
| LinkedIn | B2B, professionals, formal sector |
| X/Twitter | Opinion leaders, journalists, public figures, public sector |

---

## Strategic Frameworks to Reference

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
- **Kennedy + Brunson direct-response** — whenever a brief requires *selling* (not awareness), use `direct-response-funnel-copy` and the `book-extractions/` Kennedy + Brunson files (Secret Formula, Value Ladder, 3 traffic types, 7 phases of a lead, Star-Story-Solution, Perfect Webinar, Soap Opera, Kennedy 28-step letter, 5 Propositions, Takeaway Selling, Creative P.S.). These are the canonical references for info-product, coaching, high-ticket service, membership, event, and webinar funnels.

**Key references to cite:**
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*
- Kotler, P. et al. (2023) *Marketing Management*
- Kennedy, D. and Marrs, J. (2011) *No B.S. Price Strategy*
- Kennedy, D. (2004) *No B.S. Sales Success*
- Kennedy, D. (2000) *The Ultimate Sales Letter*
- Brunson, R. (2013) *DotComSecrets Ignite*

---

## Deck Skill Format

All `deck-` skills output slide-by-slide content outlines in structured markdown. Every slide entry must follow this exact format:

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

---

## Existing Skills in This Repo

These skills are available under `skills/<category>/<skill-name>/SKILL.md` and should be referenced (not duplicated) where relevant:

| Skill | Path | Purpose |
|---|---|---|
| `east-african-english` | `skills/language/east-african-english/` | Language and tone standard — British English, EA professional register |
| `language-standards` | `skills/language/language-standards/` | Grammar, punctuation, and vocabulary rules |
| `content-writing` | `skills/content-writing/` (category-level standards) | General content writing standards |
| `blog-writer` | `skills/content-writing/blog-writer/` | Blog post content generation (text, SEO, captions — no web dev) |
| `blog-idea-generator` | `skills/content-writing/blog-idea-generator/` | Generate blog topic ideas and content briefs |
| `platform-linkedin-company-pages` | `skills/platforms/platform-linkedin-company-pages/` | LinkedIn Company Page setup, growth, Sub-Pages, Events, and content strategy for organisations |
| `anti-ai-slop` | `skills/ai-marketing/anti-ai-slop/` | MANDATORY pre-ship guardrail — ship-gate checklist run on every generated social output so it cannot read as AI slop |
| `ai-slop-audit` | `skills/ai-marketing/ai-slop-audit/` | Auto-run detector — grades any social artefact (A/B/C/F) for AI slop with evidenced findings and concrete fixes |

---

## Out of Scope

- Actual graphic design or visual asset production
- Video editing or video production
- Paid ad campaign management (bidding, targeting, creative testing)
- Web design or web development (separate suite)
- Influencer contracts or payments (legal territory — refer to a lawyer)

## Upgrade Priority

When improving this repository, prioritise in this order:

1. Market-context and localisation layers
2. Core strategy and proposal quality
3. Platform and execution coherence
4. Measurement and evaluation quality
5. AI governance and augmentation
6. Commercial packaging and operating system depth

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
