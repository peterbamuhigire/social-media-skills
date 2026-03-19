# social-media-skills — Project Conventions

## Purpose

This repository is a complete documentation and deliverable toolkit for running a professional social media and digital marketing consultancy. Skills produce every document in the consultancy lifecycle: credentials, proposals, strategies, content plans, platform playbooks, presentation decks, reports, and training guides.

**This suite is content-only.** No web development, graphic design, video editing, or paid ad campaign management (bidding/creative testing). Skills generate text documents, structured plans, and slide outlines — not files, code, or designs.

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

## Authoring Rules (All Skills)

1. **SKILL.md only** — every skill directory contains a `SKILL.md` with YAML frontmatter (`name` and `description` only). No README.md, CHANGELOG.md, or auxiliary docs.
2. **500-line hard limit** — SKILL.md must stay under 500 lines. Detailed reference material goes in `references/` subfolder and is linked from SKILL.md with a note on when to read it.
3. **British English throughout** — organisation, colour, programme, behaviour, analyse, strategise, recognise, centre, enquiry. Never American spellings.
4. **Imperative language** — "Ask for…", "Generate…", "Apply…", "Include…". Not "you should" or "Claude will".
5. **Required Input section** — every skill must ask for: client business name, industry, country/city, and primary goal before generating any deliverable. Additional inputs as needed per skill.
6. **Quality Criteria section** — every skill must include 5–8 bullets defining what good output looks like for that specific skill.
7. **Frontmatter description** — must state both *what the skill does* and *when to invoke it* (triggers). This is the primary trigger mechanism.

---

## Default Country Context: Uganda / East Africa

All skills default to the Ugandan/East African market unless the user specifies otherwise. This affects examples, platform penetration data, pricing, cultural references, and audience characteristics.

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

**Key references to cite:**
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*
- Kotler, P. et al. (2023) *Marketing Management*

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

These skills are available and should be referenced (not duplicated) where relevant:

| Skill | Purpose |
|---|---|
| `east-african-english` | Language and tone standard — British English, EA professional register |
| `language-standards` | Grammar, punctuation, and vocabulary rules |
| `content-writing` | General content writing standards |
| `blog-writer` | Blog post content generation (text, SEO, captions — no web dev) |
| `blog-idea-generator` | Generate blog topic ideas and content briefs |

---

## Out of Scope

- Actual graphic design or visual asset production
- Video editing or video production
- Paid ad campaign management (bidding, targeting, creative testing)
- Web design or web development (separate suite)
- Influencer contracts or payments (legal territory — refer to a lawyer)
