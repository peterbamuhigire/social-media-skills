# S09 preservation log — B09-pipeline-b

Worker: S09 B09 worker (Claude Opus 5.5), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. Frontmatter, `## Use When` and `## Do Not Use When` are byte-identical to HEAD (routecheck 0 changed). All pipeline hand-offs are kept as workflow steps, decision rows, output consumers or References links: 07 → `06`/`email-copywriter`/`playbook-marketing-automation`; 08 → `09`/`strategy-creator-monetisation`; 09 → `05`/`13`/`11`/`premium-commercial-writing`/`meta-reporting`; 10 → `11`/`content-ideas`/`05`, ← `03`/`04`; 12 → `blog-writer`/`11`/`seo-geo-optimisation`/`07`, ← `09`/`11`; 13 ← `09`, → platform skills, `creative-brief-and-big-idea`, `ad-copy-and-hook-lab`. `11-content-calendar` (worked example) was not touched.

## 07-email-marketing-strategy — 446 → 123 lines (gated shared ratio 6.5 % → 3.1 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro (authoritative email deliverable; client-specific; British English; Uganda/EA default) and platform paragraph (Mailchimp or Brevo; Brevo cost-effective, Mailchimp integrations) | CONDENSED-IN-PLACE + MOVED | SKILL.md intro; full text → references/strategy-document-sections.md § Platform default |
| 2 | Generated contract prose (generic input/output/evidence rows, Capability, Degraded, 2 generic decision rows, workflow 1–6, generic Quality Standards paragraph, 4 generic anti-patterns, worked example, Read next, "Follow the directly linked…") | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision row "belongs to `06-digital-marketing-strategy`" | KEPT (tightened) | SKILL.md § Decision Rules row 8 |
| 4 | Decision rows win-back, funnel build (+ launch), lead magnet | KEPT | SKILL.md § Decision Rules rows 2–4 |
| 5 | Anti-pattern "Publishing, spending or editing a live account" | KEPT (domain wording) | SKILL.md § Anti-Patterns 7 |
| 6 | References list (anti-ai-slop, 4 reference files) and Read next links | KEPT | SKILL.md § References with "read when" phrasing |
| 7 | "## Required Input" (9 intake items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs rows 1, 2, 4, 5, 6; text → references/strategy-document-sections.md § Intake questions |
| 8 | "## Document Structure" and "### 1. List Building Strategy" … "### 6. Reactivation Sequence" | MOVED (text unchanged) | references/strategy-document-sections.md § Document Structure, §§ 1–6; segmentation-size rule also SKILL.md § Decision Rules row 7; suppress-not-delete and 6-month review also § Anti-Patterns 3; evergreen 8-week rule also § Anti-Patterns 4 |
| 9 | "## Eleven Psychological Principles of Copywriting" (Edwards, Edwards and Douglas, 1991) | MOVED (text unchanged) | references/strategy-document-sections.md § Eleven Psychological Principles |
| 10 | "### 7A. Strategic Email Programme Principles" (90/90 rule, content-to-sales ratio, AI send-time optimisation) | MOVED (text unchanged) + MERGED | references/strategy-document-sections.md § 7A; cadence and 50 % rules also SKILL.md § Decision Rules rows 5–6, § Workflow step 4, § Anti-Patterns 1 |
| 11 | "### 7. KPIs and Target Benchmarks" (two KPI tables, UTM note, open-rate caveat) | MOVED (text unchanged) | references/strategy-document-sections.md § 7; CTOR/MPP caveat also SKILL.md § Anti-Patterns 2 |
| 12 | "### 8. Twelve Subject Line Formulas with Uganda/EA Examples" | MOVED (text unchanged) | references/strategy-document-sections.md § 8 |
| 13 | "## Quality Criteria" (10 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 10 in 8 bullets: welcome + promotional merged; subject-line + platform-differences merged) |

Checks: factcheck 0 missing; linecheck 8 flagged → 8 scaffolding, 0 paraphrased, 0 lost; validator clean; gated 3.1 % (was 1.5 % before other batches landed; the shared-line set moves as workers finish).
Paraphrased lines: none flagged.
Noticed, not changed:
- Email cadence (orchestrator reconciles): this skill's 7A says "For most EA clients: weeks 1–12 → 2 emails per week; months 4–12 → weekly or fortnightly" (now in references/strategy-document-sections.md § 7A verbatim and SKILL.md § Decision Rules row 5); references/email-funnel-build-sequence.md (unchanged, line 67) says "Under 500 subscribers | Weekly"; the "1–2 a month" B2C figure is in `skills/strategy/peso-integrated-strategy/references/owned-media-assets.md`, outside this batch and untouched. Newsletter default is also "fortnightly" in § 4.
- Two KPI tables compete: global "Bounce rate (hard) <1%", "Opt-out rate <0.1% per send", "Open rate 10–15%" versus EA "Bounce under 2%", "Unsubscribe under 0.5% per send", "Open rate 25–35%". Both kept.
- Platform-plan claims (Mailchimp free plan 500 contacts; Brevo unlimited contacts on free plan; send-time optimisation on Mailchimp Standard and Brevo Business) are undated.
- Citations Edwards, Edwards and Douglas (1991), Bly (2018) and Johnsen (2024) carry no title or publisher.
- Existing references still point to "SKILL.md `7A`", "SKILL.md `3. Welcome Sequence`" and "SKILL.md `1. List Building Strategy`"; those sections now live in references/strategy-document-sections.md under the same headings (existing reference text not edited).

## 08-influencer-marketing-strategy — 420 → 124 lines (gated shared ratio 7.2 % → 3.1 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro (Uganda/EA ecosystem context, not global averages; strategy and execution only; no legal contracts, refer to a lawyer) | CONDENSED-IN-PLACE + MOVED | SKILL.md intro; full text → references/influencer-strategy-document-sections.md § Scope and market default |
| 2 | Generated contract prose (generic rows, Capability, Degraded, 2 generic decision rows, workflow, generic Quality Standards paragraph, 4 generic anti-patterns, worked example, Read next, "Follow the directly linked…") | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows AI discovery / virtual creators; UGC; "belongs to `09-campaign-strategy`" | KEPT | SKILL.md § Decision Rules rows 3, 4, 8 |
| 4 | References (anti-ai-slop, legal gate, creative gate, 4 reference files, creator monetisation) and Read next | KEPT | SKILL.md § References |
| 5 | "## Required Input" (7 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs rows 1–5; text → references/influencer-strategy-document-sections.md § Intake questions |
| 6 | "## Document Structure", "### 1. Influencer Tier Definitions" … "### 7. Red Flags to Avoid" | MOVED (text unchanged; one link re-based to the sibling file) | references/influencer-strategy-document-sections.md §§ 1–7; red-flag thresholds also SKILL.md § Decision Rules row 1; location rule row 2; lawyer triggers row 5; disclosure row 6; 48-hour catch-up row 7; follow-up rule § Anti-Patterns 3; paid-ad usage § Anti-Patterns 4 |
| 7 | "## The Creator Economy — Structural Principles" with "### Why Influencer Marketing Works", "### The Influencer Industry Structure (Hund, 2023)", "### Winfluence — The Influence Continuum (Falls, 2021)" | MOVED (text unchanged) | references/influencer-strategy-document-sections.md § The Creator Economy; buyer's lens and five mechanisms also SKILL.md § Anti-Patterns 1; 3–4 touchpoints § Anti-Patterns 5; micro-vs-macro claim § Anti-Patterns 6 |
| 8 | "## Quality Criteria" (13 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (12 in 8 bullets); "British English … UGX" → references/influencer-strategy-document-sections.md § Quality checklist |

Checks: factcheck 0 missing; linecheck 9 flagged → 9 scaffolding, 0 paraphrased, 0 lost; validator clean; gated 3.1 % (was 1.5 % before other batches landed; the shared-line set moves as workers finish).
Paraphrased lines: none flagged.
Noticed, not changed: EA engagement figures remain labelled unsourced screening heuristics; "3R" is marked of uncertain origin and not Hennessy's; Kenya BCLB, UCC and Rwanda disclosure items stay `NOT_ASSESSED`; the "UGX 1 million" lawyer trigger is engine-authored and undated.

## 09-campaign-strategy — 438 → 122 lines (gated shared ratio 7.0 % → 3.1 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro (one campaign; client-specific; British English; Uganda/EA default; distinct from always-on in `05-social-media-strategy`) | CONDENSED-IN-PLACE + MOVED | SKILL.md intro; full text → references/campaign-strategy-document-sections.md § Scope and market default |
| 2 | Generated contract prose (generic rows, Capability, Degraded, 2 generic decision rows, workflow, generic Quality Standards paragraph, 4 generic anti-patterns, worked example, Read next, "Follow the directly linked…") | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows contest/giveaway and "belongs to `13-campaign-brief`" | KEPT | SKILL.md § Decision Rules rows 6–7 |
| 4 | References (anti-ai-slop, campaign exemplars, creative review gate, contests reference) and Read next | KEPT | SKILL.md § References (existing unlinked reference sequence-and-proof-architecture.md now linked too) |
| 5 | "## Required Input" (9 items, persona note, 4 conversion-critical details, "not ready" rule) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs rows 1–6, § Workflow step 2, § Decision Rules row 1; text → references/campaign-strategy-document-sections.md § Intake questions |
| 6 | "## Document Structure", "### 1. Campaign Objective" … "### 10. One-Page Campaign Brief" | MOVED (text unchanged) | references/campaign-strategy-document-sections.md §§ 1–10; two-persona rule also SKILL.md § Decision Rules row 2; premium spine row 3; UGX 20,000–50,000 boost floor row 4; budget shortfall row 5; secondary objectives, channel roles, genuine urgency, cut-off-message assets and out-of-scope production also § Anti-Patterns 1–5 |
| 7 | "## Quality Criteria" (11 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 11 in 8 bullets) |

Checks: factcheck 0 missing; linecheck 9 flagged → 9 scaffolding, 0 paraphrased, 0 lost; validator clean; gated 3.1 %.
Paraphrased lines: none flagged.
Noticed, not changed: "Minimum effective boost spend … approximately UGX 20,000–50,000 per day … (2,000–5,000 people)" is unsourced and undated; post-campaign report timing competes with `13-campaign-brief` ("within 5 working days of campaign close" here vs "[Date + 7 days]" in 13).

## 10-content-pillars — 257 → 115 lines (gated shared ratio 17.6 % → 3.6 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro (two outputs; `east-african-english`; do not generate until Required Input confirmed) | CONDENSED-IN-PLACE | SKILL.md intro; confirmation rule → § Workflow step 1 |
| 2 | Generated contract prose (generic rows, Capability, Degraded, 2 generic decision rows, workflow, generic Quality Standards paragraph, 4 generic anti-patterns, worked example, Read next, "Follow the directly linked…") | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision row "belongs to `11-content-calendar`" | KEPT (extended to `content-ideas`) | SKILL.md § Decision Rules row 7 |
| 4 | References (anti-ai-slop) and Read next | KEPT | SKILL.md § References |
| 5 | "## Required Input" (7 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs; text → references/pillar-build-method.md § Intake questions |
| 6 | "## Frameworks to Apply" (10-4-1, Bodnar and Cohen 2012; Hero/Hub/Hygiene) | MOVED (text unchanged) + MERGED | references/pillar-build-method.md § Frameworks to Apply; SKILL.md § Workflow step 4, § Decision Rules row 4 |
| 7 | "## Content Type Taxonomy (Handley, 2012)" (table and rule of thumb) | MOVED (text unchanged) | references/pillar-build-method.md; three-of-five and Tabasco rules also SKILL.md § Anti-Patterns 3–4 |
| 8 | "## Step 1: Determine the Number of Pillars" | MOVED (text unchanged) + MERGED | references/pillar-build-method.md § Step 1; SKILL.md § Decision Rules rows 1–3 |
| 9 | "## Step 2: Generate Each Pillar" (eight elements, "### 1." … "### 8.") | MOVED (text unchanged) | references/pillar-build-method.md § Step 2; element list also SKILL.md § Workflow step 3; naming and post-type rules § Anti-Patterns 1–2 |
| 10 | "## Step 3: Content Pillar Map", "## Step 4: Content Pillar Reference Card" and the 10-4-1 consultant note | MOVED (text unchanged) | references/pillar-build-method.md §§ Step 3–4; consultant note also SKILL.md § Decision Rules rows 5–6 |
| 11 | "## The 8 Imprints Rule — Why Frequency Matters" (Pinskey, 1997) | MOVED (text unchanged) | references/pillar-build-method.md; also SKILL.md § Workflow step 6, § Anti-Patterns 5 |
| 12 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |

Checks: factcheck 0 missing; linecheck 10 flagged → 10 scaffolding, 0 paraphrased, 0 lost; validator clean; gated 3.6 %.
Paraphrased lines: none flagged.
Noticed, not changed: Hero/Hub/Hygiene is attributed only to "(YouTube/Google)" with no date or source; the Handley (2012) and Pinskey (1997) citations carry no title or publisher.

## 12-website-content-plan — 273 → 119 lines (gated shared ratio 14.8 % → 3.3 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro (four outputs; planning only; `blog-writer` for articles; `east-african-english`) | CONDENSED-IN-PLACE | SKILL.md intro |
| 2 | Generated contract prose (generic rows, Capability, Degraded, 2 generic decision rows, workflow, generic Quality Standards paragraph, 4 generic anti-patterns, worked example, Read next, "Follow the directly linked…") | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Decision rows buyer-question harvest and "belongs to `11-content-calendar`" | KEPT | SKILL.md § Decision Rules rows 4 and 8 |
| 4 | References (anti-ai-slop, buyer-question-content-plan) and Read next | KEPT | SKILL.md § References |
| 5 | "## Required Input" (8 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs rows 1–5; text → references/content-plan-build-method.md § Intake questions |
| 6 | "## Pre-Requisite: The 7 Website Content Priorities (Sheridan, 2019)" | MOVED (text unchanged) + MERGED | references/content-plan-build-method.md; Priorities 1/2/7 rule, 3-second load, Big 5 gaps also SKILL.md § Workflow step 2, § Decision Rules rows 1–3, § Required Inputs row 6 |
| 7 | "## Section 1: 12 Blog Post Briefs" (nine elements "### 1." … "### 9.") | MOVED (text unchanged) | references/content-plan-build-method.md § Section 1; title, heading and keyword rules also SKILL.md § Anti-Patterns 1–4 |
| 8 | "## Section 2: Editorial Calendar" (table and sequencing rules) | MOVED (text unchanged) | references/content-plan-build-method.md § Section 2; campaign-alignment rule also § Decision Rules row 6; consecutive-topic rule § Anti-Patterns 6 |
| 9 | "## Section 3: Internal Linking Structure" | MOVED (text unchanged) | references/content-plan-build-method.md § Section 3; 5-link cap also SKILL.md § Quality Standards 5 |
| 10 | "## Section 4: Content Upgrade and Lead Magnet Ideas" (incl. Uganda/EA format guidance) | MOVED (text unchanged) | references/content-plan-build-method.md § Section 4; calculator-developer rule also § Decision Rules row 7; 8-page cap § Anti-Patterns 5 |
| 11 | "## Coordination Note" (11-content-calendar alignment; briefs and lead magnets to `blog-writer`) | MOVED (text unchanged) + MERGED | references/content-plan-build-method.md § Coordination Note; SKILL.md § Workflow step 8, § References |
| 12 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |

Checks: factcheck 0 missing; linecheck 9 flagged → 9 scaffolding, 0 paraphrased, 0 lost; validator clean; gated 3.3 %.
Paraphrased lines: none flagged.
Noticed, not changed: Sheridan (2019) statistics ("for me"/"should I" searches up 120 %; 40 % abandon beyond 3 seconds; average 8–12 seconds) are secondary and undated; publication frequency "1 per week or 2 per month" sits beside a fixed 12-articles-in-90-days plan; references/buyer-question-content-plan.md still says the Big 5 priority is "named in SKILL.md (Priority 2)" — it now lives in references/content-plan-build-method.md (existing reference text not edited).

## 13-campaign-brief — 315 → 140 lines (gated shared ratio 12.8 % → 2.7 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Intro and "Distinction from 09-campaign-strategy" paragraph | CONDENSED-IN-PLACE + MOVED | SKILL.md intro; full text → references/brief-document-sections.md § Scope and distinction |
| 2 | Generated contract prose (generic rows, Capability, Degraded, 2 generic decision rows, workflow 1–6, generic Quality Standards paragraph, 4 generic anti-patterns, worked example, Read next, "Follow the directly linked…") | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 3 | Workflow step 7 (reader-first brief and evidence/rights record; quarantine rule) | KEPT | SKILL.md § Workflow step 6 |
| 4 | Decision row "belongs to `09-campaign-strategy`" | KEPT | SKILL.md § Decision Rules row 8 |
| 5 | References (anti-ai-slop, 2 reference files, exemplars, creative gate) and Read next | KEPT | SKILL.md § References |
| 6 | "## Required Input" (10 items) | MERGED-INTO-CONTRACT + MOVED | SKILL.md § Required Inputs rows 1–5, Kampala default in § Workflow step 1; text → references/brief-document-sections.md § Intake questions |
| 7 | "## Brief Document Structure" and "### Section 1" … "### Section 10" (incl. "#### Platform specifications and copy") | MOVED (text unchanged; platform links re-based with one `../`) | references/brief-document-sections.md; spec-verification rule also SKILL.md § Decision Rules row 1; channel-fit row 2; CTA row 3; captions row 4; late feedback row 5; emergency sign-off row 6; anti-patterns 1–6 |
| 8 | "## Quality Criteria" (9 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 9 in 8 bullets: timeline + late-feedback merged) |
| 9 | "## Five Outcomes gate before sign-off" (canonical reference, rule, 5-row table) | KEPT | SKILL.md § Five Outcomes gate before sign-off (retained domain section) |
| 10 | "### How to apply at sign-off" (wording template, fail/missing rule, accessibility evidence rule) | MOVED (text unchanged) | references/brief-document-sections.md § Five Outcomes: how to apply at sign-off; fail rule also SKILL.md § Decision Rules row 7, § Workflow step 7 |
| 11 | "## Bounded example" (synthetic retail example link and caveat) | MERGED-INTO-CONTRACT | SKILL.md § References (link and full caveat) |

Checks: factcheck 0 missing; linecheck 10 flagged → 10 scaffolding, 0 paraphrased, 0 lost; validator clean; gated 2.7 %.
Paraphrased lines: none flagged.
Noticed, not changed: post-campaign report timing "[Date + 7 days]" competes with `09-campaign-strategy` "within 5 working days of campaign close"; example budget rates (graphic design UGX 500,000; video UGX 1,200,000) are illustrative and undated.
