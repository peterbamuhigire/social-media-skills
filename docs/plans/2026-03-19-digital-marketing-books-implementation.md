# Digital Marketing Books — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Extract insights from 11 digital marketing books across 4 thematic groups, produce a consolidated gap analysis, then create new skills and strengthen existing ones — with every output meeting the Golden Rule (AI-powered internally; every deliverable looks, feels, and sounds like the work of the best skilled humans).

**Architecture:** Parallel extraction by thematic group → single consolidated gap analysis → parallel skill execution → cleanup commit. The `ai-content-humaniser` skill is the enforcement layer for the Golden Rule and is strengthened as a priority task.

**Tech Stack:** Skill files (SKILL.md), British English, CLAUDE.md conventions, PDFs at `C:\Users\Peter\Downloads\Documents\`

---

## Quality Gate (applies to every SKILL.md produced in this plan)

Before committing any skill file, verify all of the following:
- [ ] Frontmatter has `name` and `description` only — no other fields
- [ ] `description` states what the skill does AND when to invoke it
- [ ] **Required Input** section asks for: client business name, industry, country/city, primary goal (plus any skill-specific inputs)
- [ ] **Quality Criteria** section has 5–8 bullets
- [ ] File is under 500 lines
- [ ] British English throughout (organisation, colour, programme, behaviour, analyse, strategise, recognise, centre, enquiry)
- [ ] Imperative language ("Ask for…", "Generate…") — never "you should" or "Claude will"
- [ ] No README.md or auxiliary files created alongside the skill

---

## Phase 1 — Parallel Extraction

Run Tasks 1–4 simultaneously. Each task writes a temp file to the repo root.

---

### Task 1: Extract Group 1 — Foundations & Strategy

**Books:**
- `_OceanofPDF.com_Digital_Marketing_Foundations_and_Strategy_5th_edition_-_Debra_Zahay.pdf`
- `_OceanofPDF.com_Digital_Marketing_-_Yoram_Wind.pdf`
- `_OceanofPDF.com_The_SAGE_Handbook_of_Digital_Marketing_-_Hanlon_A.pdf`

**Path prefix:** `C:\Users\Peter\Downloads\Documents\`

**Step 1: Read all three PDFs**

Read each PDF (first 15–20 pages for overview, then key chapters identified by table of contents). Focus on:
- Strategic frameworks and models
- Channel integration approaches
- Digital marketing planning methodologies
- Any frameworks not already in the suite (POEM, RACE, SMART are already covered)

**Step 2: Write extraction file**

Write to: `_temp_dm_g1_foundations.txt`

Structure:
```
BOOK: [Title] — [Author]
FRAMEWORKS: [list with brief description]
TACTICS: [actionable items applicable to the skill suite]
GAPS: [concepts not covered by any existing skill]
CITATIONS: [exact quotes worth using, with page numbers]
---
```

Repeat for each book in the group. End with:
```
GROUP SYNTHESIS:
[3–5 sentences on cross-book themes and highest-priority gaps for this group]
```

**Step 3: Verify file exists and is non-empty**

Check `_temp_dm_g1_foundations.txt` exists in the repo root and has content.

---

### Task 2: Extract Group 2 — AI in Marketing

**Books:**
- `_OceanofPDF.com_Advances_in_Digital_Marketing_in_the_Era_of_AI_-_Moez_Ltifi.pdf`
- `_OceanofPDF.com_AI_In_Digital_Marketing_-_Maria_Johnsen.pdf`

**Step 1: Read both PDFs**

Focus on:
- AI workflow frameworks for marketing teams
- Quality control processes for AI-generated content
- Automation use cases by channel
- Ethics, disclosure, and bias frameworks
- What these books say that is NOT already in `ai-content-humaniser` or `policy-ai-content-ethics`

**Step 2: Write extraction file**

Write to: `_temp_dm_g2_ai.txt`

Same structure as Task 1. Note explicitly: which insights strengthen `ai-content-humaniser`, which strengthen `policy-ai-content-ethics`, and which require new skills.

**Step 3: Verify file exists and is non-empty**

---

### Task 3: Extract Group 3 — Analytics & Velocity

**Books:**
- `_OceanofPDF.com_Web_Analytics_Blueprint_-_Saif_Ali_Raaz.pdf`
- `_OceanofPDF.com_High-Velocity_Digital_Marketing_-_Steven_Mark_Kahan.pdf`

**Step 1: Read both PDFs**

Focus on:
- Web analytics setup, metrics frameworks, and reporting structures
- Velocity/agile marketing decision-making
- Attribution models and UTM practices
- KPIs and dashboard design
- What these books say that is NOT already in `meta-roi-framework`, `meta-reporting`, `meta-utm-tracking`

**Step 2: Write extraction file**

Write to: `_temp_dm_g3_analytics.txt`

Same structure as Task 1. Note explicitly: which insights strengthen `meta-roi-framework` and `meta-reporting`, and which require new skills.

**Step 3: Verify file exists and is non-empty**

---

### Task 4: Extract Group 4 — Tactical & Trust

**Books:**
- `_OceanofPDF.com_Get_Scrappy_-_Nick_Westergaard.pdf`
- `_OceanofPDF.com_Digital_Marketing_in_2023_-_Martin_Pidsley.pdf`
- `_OceanofPDF.com_The_Digital_Marketing_Handbook_-_Robert_W_Bly.pdf`
- `_OceanofPDF.com_Consumer_Trust_in_Digital_Markets_-_Ahmed_Rageh.pdf`

**Step 1: Read all four PDFs**

Focus on:
- SME-appropriate tactics for lean budgets (Westergaard's "scrappy" framework)
- 2023 trends still relevant to the EA market today
- Direct response and conversion copywriting principles (Bly)
- Consumer trust-building in digital environments (Rageh) — especially relevant to low-trust digital markets like EA
- What these books say that is NOT already covered by existing skills

**Step 2: Write extraction file**

Write to: `_temp_dm_g4_tactical.txt`

Same structure as Task 1. Note explicitly: which insights strengthen `06-digital-marketing-strategy`, `biz-dev-proposal`, and `framework-community-trust`, and which require new skills.

**Step 3: Verify file exists and is non-empty**

---

## Phase 2 — Consolidated Gap Analysis

### Task 5: Write gap analysis

**Files to read before writing:**
- `_temp_dm_g1_foundations.txt`
- `_temp_dm_g2_ai.txt`
- `_temp_dm_g3_analytics.txt`
- `_temp_dm_g4_tactical.txt`
- `docs/gap-analysis-2026-03.md`
- `docs/gap-analysis-2026-03-ai-books.md`
- `docs/gap-analysis-2026-03-new-books.md`
- `CLAUDE.md`

**Step 1: Read all eight files above**

**Step 2: Cross-reference against existing skills**

Run a mental audit: for each gap identified across the four extraction files, check whether any existing skill already covers it (fully, partially, or not at all). Use the skill directory listing in CLAUDE.md and the existing gap analyses as reference.

**Step 3: Write gap analysis**

Write to: `docs/gap-analysis-2026-03-digital-marketing-books.md`

Structure:
```markdown
# Gap Analysis — Digital Marketing Books (March 2026)

**Date:** 2026-03-19
**Books analysed:** 11
**Method:** Parallel thematic extraction; cross-referenced against 3 prior gap analyses and 100+ skill suite

---

## Books Analysed
[table: #, Title, Author, Group]

---

## The Golden Rule Audit
[List any existing content-generating skills that lack an explicit human authenticity / quality gate.
These are high-priority for strengthening regardless of the book insights.]

---

## New Skills to Create

### HIGH Priority
| Slug | Purpose | Source Books |

### MEDIUM Priority
| Slug | Purpose | Source Books |

### LOW Priority
| Slug | Purpose | Source Books |

---

## Existing Skills to Strengthen

For each skill: name it, list the specific additions from the books.
Priority order: ai-content-humaniser first, then 06-digital-marketing-strategy, then others.

---

## Bibliography
[Full citations for all 11 books]
```

**Step 4: Verify file exists at `docs/gap-analysis-2026-03-digital-marketing-books.md`**

**Step 5: Commit**

```bash
git add docs/gap-analysis-2026-03-digital-marketing-books.md
git commit -m "Add gap analysis: 11 digital marketing books"
```

---

## Phase 3 — Skill Execution

Read the gap analysis before starting. Tasks 6–8 can run in parallel where the files don't overlap.

---

### Task 6: Strengthen `ai-content-humaniser`

**File:** `ai-content-humaniser/SKILL.md`

**Step 1: Read the current skill**

Read `ai-content-humaniser/SKILL.md` in full.

**Step 2: Read the G2 extraction for AI-specific additions**

Read `_temp_dm_g2_ai.txt` — note all insights flagged as strengthening this skill.

**Step 3: Identify additions**

The skill already covers the five AI quality risks and the Human Voice Checklist well. Additions from the books should include:
- Elevate the Golden Rule as the opening philosophy statement (AI-powered; human-authentic output)
- Any additional AI vocabulary or patterns from Ltifi / Johnsen not on the current banned list
- Any additional content-type editing guidance not yet covered
- Strengthen the "Proof of Human" standard with any new criteria from the books

**Step 4: Edit the skill**

Apply additions using Edit tool. Do not rewrite sections that already meet standard — add only what is genuinely new.

**Step 5: Quality gate check**

Verify all items in the Quality Gate checklist at the top of this plan.

**Step 6: Commit**

```bash
git add ai-content-humaniser/SKILL.md
git commit -m "Strengthen ai-content-humaniser with Golden Rule philosophy + book insights"
```

---

### Task 7: Strengthen `06-digital-marketing-strategy`

**File:** `06-digital-marketing-strategy/SKILL.md`

**Step 1: Read the current skill**

Read `06-digital-marketing-strategy/SKILL.md` in full.

**Step 2: Read G1 and G4 extractions for relevant additions**

Read `_temp_dm_g1_foundations.txt` and `_temp_dm_g4_tactical.txt`.

**Step 3: Identify additions**

Look for:
- Any strategic frameworks from Zahay, Wind, or Hanlon not yet in the skill (e.g. digital transformation maturity models, omnichannel integration frameworks)
- SME-appropriate shortcuts from Westergaard (lean budget decision trees)
- Consumer trust dimensions from Rageh relevant to the strategy document
- Any gaps in the current 12-month roadmap structure

**Step 4: Edit the skill**

Add only genuinely new content. The existing structure is solid — do not restructure, only add.

**Step 5: Quality gate check**

**Step 6: Commit**

```bash
git add 06-digital-marketing-strategy/SKILL.md
git commit -m "Strengthen 06-digital-marketing-strategy with book insights"
```

---

### Task 8: Build new skills from gap analysis

**Step 1: Read the gap analysis**

Read `docs/gap-analysis-2026-03-digital-marketing-books.md` and identify all HIGH priority new skills.

**Step 2: For each HIGH priority new skill:**

a. Create directory: `mkdir <skill-slug>/`
b. Write `<skill-slug>/SKILL.md` following the CLAUDE.md conventions
c. Run quality gate check
d. Commit after each skill (do not batch multiple skills in one commit)

Commit message format:
```bash
git commit -m "Add [skill-slug]: [one-line description]"
```

**Step 3: For each MEDIUM priority new skill** (after all HIGH are done):

Same process as Step 2.

**Step 4: Strengthen any other existing skills** flagged in the Golden Rule Audit section of the gap analysis

For each: Read the existing skill, apply additions, quality gate check, commit.

---

## Phase 4 — Cleanup & Final Commit

### Task 9: Delete all temp files and commit

**Step 1: Delete extraction files from this session**

```bash
rm _temp_dm_g1_foundations.txt
rm _temp_dm_g2_ai.txt
rm _temp_dm_g3_analytics.txt
rm _temp_dm_g4_tactical.txt
```

**Step 2: Delete all temp files from previous sessions**

```bash
rm _temp_inf_*.txt
rm _temp_linkedin_*.txt
rm _temp_pb_*.txt
```

**Step 3: Verify no temp files remain**

```bash
ls _temp_*.txt 2>/dev/null && echo "TEMP FILES STILL EXIST" || echo "Clean"
```

Expected: `Clean`

**Step 4: Stage and commit the strategy-personal-brand modification**

Check `strategy-personal-brand/SKILL.md` — it is currently modified. Read it and apply quality gate. Then:

```bash
git add strategy-personal-brand/SKILL.md
git commit -m "Update strategy-personal-brand with book insights"
```

**Step 5: Final cleanup commit**

```bash
git add -u
git commit -m "Remove all temp extraction files from previous sessions"
```

**Step 6: Update README.md**

Read `README.md`. Add any new skills created in Task 8. Commit:

```bash
git add README.md
git commit -m "Update README with new skills from digital marketing book batch"
```

---

## Success Criteria

- All 11 books have been read and their insights are reflected in at least one skill
- `docs/gap-analysis-2026-03-digital-marketing-books.md` exists and is thorough
- `ai-content-humaniser` explicitly encodes the Golden Rule as its opening philosophy
- Every new and modified skill passes the full Quality Gate checklist
- No `_temp_*` files remain in the repo root
- All commits are clean and descriptive
