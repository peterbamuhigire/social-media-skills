# Design: 11-Book Digital Marketing Extraction & Skill Strengthening
**Date:** 2026-03-19
**Status:** Approved

---

## Context

The social-media-skills repository currently contains ~100 skills. Three gap analyses (March 2026) have been completed using previous book batches. Eleven new digital marketing PDFs have been provided. The goal is to extract insights, identify gaps, and strengthen the skill suite.

## The Golden Rule

Every output — text, posts, images, audio, video — produced by any skill must look, feel, and sound as if it was crafted by the most skilled human creatives with meticulous attention to detail and deep knowledge of the target audience. AI powers the operations; human authenticity defines the output. The `ai-content-humaniser` skill is the mandatory enforcement layer.

---

## Phase 1 — Parallel Extraction (4 agent groups)

Four agents run simultaneously, each reading a thematic group of books and extracting:
- Key frameworks and models
- Actionable tactics applicable to the skill suite
- Gaps in the current suite (cross-referenced against existing skills)
- Citable quotes and references

| Group | Books | Theme |
|---|---|---|
| G1 — Foundations & Strategy | Zahay · Wind · Hanlon (SAGE Handbook) | Digital marketing theory, strategy frameworks, channel architecture |
| G2 — AI in Marketing | Ltifi · Johnsen | AI workflows, automation, GenAI in marketing, ethics |
| G3 — Analytics & Velocity | Raaz (Web Analytics Blueprint) · Kahan (High-Velocity) | Data, measurement, velocity-driven decision-making, attribution |
| G4 — Tactical & Trust | Westergaard (Get Scrappy) · Pidsley · Bly (Handbook) · Rageh (Consumer Trust) | SME tactics, trust-building, practical playbooks, consumer behaviour |

**Output:** Four extraction temp files (`_temp_dm_*.txt`)

---

## Phase 2 — Consolidated Gap Analysis

One agent synthesises all four extraction outputs into:
`docs/gap-analysis-2026-03-digital-marketing-books.md`

The analysis cross-references all three existing gap analyses to avoid duplicating completed work. It produces:
- New skills to create (with priority: High / Medium / Low)
- Existing skills to strengthen (with specific additions per skill)
- Human Authenticity Gate audit: which existing skills currently lack the quality standard

---

## Phase 3 — Skill Execution (parallel)

Based on the gap analysis, parallel agents:
1. Build new skills (slugs defined by gap analysis)
2. Strengthen high-priority existing skills, particularly:
   - `06-digital-marketing-strategy`
   - `meta-roi-framework`
   - `meta-reporting`
   - `ai-content-humaniser` (elevate Golden Rule language)
   - `strategy-personal-brand` (currently modified/in-progress)
3. Add Human Authenticity Gate to any content-generating skill that lacks it

---

## Phase 4 — Cleanup & Commit

- Delete all `_temp_*` files from the previous session (influencer, LinkedIn, personal brand batches)
- Delete all `_temp_dm_*` extraction files from this session
- Commit all new and modified skills
- Update `README.md` if significant new skills were added

---

## Success Criteria

- All 11 books have been read and their insights are reflected in the skill suite
- Gap analysis document exists in `docs/`
- No temp files remain in the repo root
- Every new skill meets the Golden Rule: authentically human in voice and craft
- The `ai-content-humaniser` skill explicitly encodes the Golden Rule as its primary standard
